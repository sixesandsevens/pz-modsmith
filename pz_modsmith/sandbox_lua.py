from __future__ import annotations

from dataclasses import dataclass, field
import re


_ASSIGN_RE = re.compile(r"^\s*(?P<key>[A-Za-z_]\w*)\s*=\s*(?P<value>.+?)(?P<trailing>,\s*)?$")
_OPTION_RE = re.compile(r"^\s*--\s*(?P<num>-?\d+)\s*=\s*(?P<label>.+?)\s*$")
_DEFAULT_RE = re.compile(r"^\s*--\s*Default\s*=\s*(?P<default>.+?)\s*$", re.IGNORECASE)


@dataclass(frozen=True)
class SandboxSetting:
    key: str
    value_raw: str
    value_type: str
    comments: list[str] = field(default_factory=list)
    options: list[tuple[int, str]] = field(default_factory=list)
    default_raw: str | None = None
    default_value_raw: str | None = None


def _infer_value_type(value_raw: str) -> str:
    v = value_raw.strip()
    if v in {"true", "false"}:
        return "bool"
    if re.fullmatch(r"-?\d+", v):
        return "int"
    if re.fullmatch(r"-?\d+\.\d+", v):
        return "float"
    if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
        return "string"
    return "lua"


def _extract_options(comments: list[str]) -> list[tuple[int, str]]:
    out: list[tuple[int, str]] = []
    for c in comments:
        m = _OPTION_RE.match(c)
        if not m:
            continue
        try:
            out.append((int(m.group("num")), m.group("label").strip()))
        except ValueError:
            continue
    return out


def _extract_default_raw(comments: list[str]) -> str | None:
    for c in comments:
        m = _DEFAULT_RE.match(c)
        if m:
            return m.group("default").strip()
    return None


def _default_value_from_raw(
    default_raw: str | None,
    options: list[tuple[int, str]],
    value_type: str,
) -> str | None:
    if default_raw is None:
        return None

    d = default_raw.strip()
    if not d:
        return None

    if options:
        dl = d.casefold()
        for num, label in options:
            if label.casefold() == dl or label.casefold().startswith(dl):
                return str(num)

    # If it's a simple scalar default, return it as a lua-ish literal.
    if value_type == "bool":
        if d.casefold() in {"true", "false"}:
            return d.casefold()
    if value_type == "int":
        if re.fullmatch(r"-?\d+", d):
            return d
    if value_type == "float":
        if re.fullmatch(r"-?\d+\.\d+", d):
            return d
    return None


def parse_sandbox_vars_lua(text: str) -> list[SandboxSetting]:
    """Parse the top-level `SandboxVars = { ... }` table into editable settings."""
    settings: list[SandboxSetting] = []
    pending_comments: list[str] = []
    in_table = False

    for raw_line in text.splitlines():
        line = raw_line.rstrip("\r")
        stripped = line.strip()

        if not in_table:
            if stripped.startswith("SandboxVars") and "{" in stripped:
                in_table = True
            continue

        if stripped.startswith("}"):
            break

        if stripped.startswith("--"):
            pending_comments.append(stripped)
            continue

        m = _ASSIGN_RE.match(line)
        if not m:
            pending_comments = []
            continue

        key = m.group("key")
        value_raw = m.group("value").strip()
        value_type = _infer_value_type(value_raw)
        options = _extract_options(pending_comments)
        default_raw = _extract_default_raw(pending_comments)
        default_value_raw = _default_value_from_raw(default_raw, options, value_type)
        settings.append(
            SandboxSetting(
                key=key,
                value_raw=value_raw.rstrip(","),
                value_type=value_type,
                comments=list(pending_comments),
                options=options,
                default_raw=default_raw,
                default_value_raw=default_value_raw,
            )
        )
        pending_comments = []

    return settings


def apply_sandbox_vars_edits(text: str, updates: dict[str, str]) -> str:
    """Apply key->raw lua value edits inside the `SandboxVars = { ... }` block."""
    if not updates:
        return text

    out_lines: list[str] = []
    in_table = False

    for raw_line in text.splitlines(keepends=False):
        line = raw_line.rstrip("\r")
        stripped = line.strip()

        if not in_table:
            out_lines.append(line)
            if stripped.startswith("SandboxVars") and "{" in stripped:
                in_table = True
            continue

        if stripped.startswith("}"):
            out_lines.append(line)
            in_table = False
            continue

        m = _ASSIGN_RE.match(line)
        if not m:
            out_lines.append(line)
            continue

        key = m.group("key")
        trailing = m.group("trailing")
        if key in updates:
            indent = line[: len(line) - len(line.lstrip(" "))]
            new_val = updates[key].strip()
            comma = "," if trailing is not None or line.rstrip().endswith(",") else ""
            out_lines.append(f"{indent}{key} = {new_val}{comma}")
        else:
            out_lines.append(line)

    return "\n".join(out_lines) + ("\n" if text.endswith("\n") else "")
