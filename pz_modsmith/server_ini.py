from __future__ import annotations

from dataclasses import dataclass, field
import re


_MIN_MAX_DEFAULT_RE = re.compile(
    r"\bMin:\s*(?P<min>-?\d+)\b|\bMax:\s*(?P<max>-?\d+)\b|\bDefault:\s*(?P<default>[^#\r\n]+)",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class ConfigSetting:
    key: str
    value: str
    value_type: str
    comments: list[str] = field(default_factory=list)
    section: str = "General"
    min_value: int | None = None
    max_value: int | None = None
    default: str | None = None


def get_first_ini_value(text: str, key: str) -> str | None:
    """Return the first value for KEY=VALUE in an INI-ish file (ignores commented lines)."""
    target = key.strip()
    if not target:
        return None
    for raw_line in text.splitlines():
        line = raw_line.rstrip("\r")
        stripped = line.lstrip()
        if not stripped or stripped.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        if k.strip() == target:
            return v.strip()
    return None


def apply_pzserver_ini_edits(text: str, updates: dict[str, str]) -> str:
    """Apply key->value edits to an INI text while preserving comments and ordering.

    Only updates lines that look like `Key=Value` (not commented). If a key appears
    multiple times, each occurrence is updated.
    """
    if not updates:
        return text

    out_lines: list[str] = []
    seen_keys: set[str] = set()
    for raw_line in text.splitlines(keepends=False):
        line = raw_line.rstrip("\r")
        stripped = line.lstrip()
        if not stripped or stripped.startswith("#") or "=" not in line:
            out_lines.append(line)
            continue
        key, sep, value = line.partition("=")
        key_stripped = key.strip()
        if key_stripped:
            seen_keys.add(key_stripped)
        if key_stripped in updates:
            new_value = updates[key_stripped]
            out_lines.append(f"{key_stripped}{sep}{new_value}")
        else:
            out_lines.append(line)

    # Append missing keys at the end (common when server ini lacks WorkshopItems=).
    missing = [k for k in updates.keys() if k not in seen_keys]
    if missing:
        if out_lines and out_lines[-1].strip():
            out_lines.append("")
        for k in missing:
            out_lines.append(f"{k}={updates[k]}")

    return "\n".join(out_lines) + ("\n" if text.endswith("\n") else "")


def _infer_value_type(value: str) -> str:
    v = value.strip()
    if v.lower() in {"true", "false"}:
        return "bool"
    if re.fullmatch(r"-?\d+", v):
        return "int"
    if re.fullmatch(r"-?\d+\.\d+", v):
        return "float"
    if ";" in v:
        return "semicolon_list"
    if "," in v:
        return "comma_list"
    return "string"


def _parse_min_max_default(comments: list[str]) -> tuple[int | None, int | None, str | None]:
    min_value: int | None = None
    max_value: int | None = None
    default: str | None = None

    for line in comments:
        for m in _MIN_MAX_DEFAULT_RE.finditer(line):
            if m.group("min") is not None:
                try:
                    min_value = int(m.group("min"))
                except ValueError:
                    pass
            if m.group("max") is not None:
                try:
                    max_value = int(m.group("max"))
                except ValueError:
                    pass
            if m.group("default") is not None and default is None:
                default = m.group("default").strip()

    return min_value, max_value, default


def parse_pzserver_ini(text: str) -> list[ConfigSetting]:
    """Parse `pzserver.ini`-style key/value config with comment blocks.

    Preserves the comment block immediately preceding a setting and infers:
    - basic value type
    - Min/Max/Default from common comment patterns
    """
    settings: list[ConfigSetting] = []
    pending_comments: list[str] = []
    current_section = "General"

    for raw_line in text.splitlines():
        line = raw_line.strip("\r")
        stripped = line.strip()

        if not stripped:
            pending_comments = []
            continue

        if stripped.startswith("#"):
            pending_comments.append(stripped.lstrip("#").strip())
            continue

        if stripped.startswith("[") and stripped.endswith("]") and len(stripped) > 2:
            current_section = stripped[1:-1].strip() or "General"
            pending_comments = []
            continue

        if "=" not in line:
            pending_comments = []
            continue

        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip()
        if not key:
            pending_comments = []
            continue

        value_type = _infer_value_type(value)
        min_value, max_value, default = _parse_min_max_default(pending_comments)
        settings.append(
            ConfigSetting(
                key=key,
                value=value,
                value_type=value_type,
                comments=list(pending_comments),
                section=current_section,
                min_value=min_value,
                max_value=max_value,
                default=default,
            )
        )
        pending_comments = []

    return settings
