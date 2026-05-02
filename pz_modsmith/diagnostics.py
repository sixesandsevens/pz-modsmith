from __future__ import annotations

import re
from pathlib import Path

from .models import DiagnosticFinding, WorkshopItem
from .utils import dedupe_keep_order


MISSING_DICT_RE = re.compile(r'Missing dictionary string on client[:\s]+(\S+)', re.IGNORECASE)
MISSING_SCRIPT_RE = re.compile(r'Warning client has no script for dictionary info[:\s]+(\S+)', re.IGNORECASE)
LUA_MOD_RUNTIME_RE = re.compile(r'Lua\(\(MOD:([^)]+)\)\)', re.IGNORECASE)
LUA_FILE_ERROR_RE = re.compile(
    r'SEVERE.*?Error found in LUA file:.*?/108600/(\d{6,})/mods/([^/\n]+)/(\S+)',
    re.IGNORECASE,
)
WORLD_DICT_FATAL_RE = re.compile(r'WorldDictionary.*Cannot load world due to WorldDictionary error', re.IGNORECASE)

# Low-confidence prefix hints: (prefix_pattern, likely_mod_ids, description).
# Used as heuristic guesses, never asserted as definitive.
PREFIX_HINTS: list[tuple] = [
    (re.compile(r"^NC_", re.IGNORECASE), ["Neat_Crafting", "NeatUI_Framework"], "Neat Crafting / Neat Framework"),
    (re.compile(r"^Phun\.", re.IGNORECASE), ["phunlib", "phuncure2", "phunsprinters2", "phunzones2"], "Phun mods (phunlib and related)"),
    (re.compile(r"^(TCGMusic|TrueMusic|TrueMoozic|TCBoombox)", re.IGNORECASE), [], "True Music / True Moozic"),
    (re.compile(r"^(ATA_|Autotsar)", re.IGNORECASE), ["tsarslib"], "Autotsar mods (may require tsarslib)"),
    (re.compile(r"^KI5", re.IGNORECASE), [], "KI5 vehicle pack"),
    (re.compile(r"^(LKP_|Legendary)", re.IGNORECASE), [], "Legendary Katana/Wakizashi pack"),
    (re.compile(r"^zdk", re.IGNORECASE), ["zdk"], "ZDK framework"),
    (re.compile(r"^Tsar", re.IGNORECASE), ["tsarslib"], "tsarslib-dependent mod"),
]

_SCANNABLE_EXTENSIONS = frozenset({".lua", ".txt", ".json", ".xml", ".info", ".script"})
_MAX_SCAN_FILE_BYTES = 512 * 1024  # 512 KB per file


def _get_prefix_hints(key: str) -> list[str]:
    hints: list[str] = []
    for pattern, mod_ids, _ in PREFIX_HINTS:
        if pattern.search(key):
            hints.extend(mod_ids)
    return dedupe_keep_order(hints)


def extract_diagnostic_findings(text: str) -> list[DiagnosticFinding]:
    """Parse failure patterns from a PZ console log into DiagnosticFinding objects.

    No certainty is claimed — language is deliberately hedged.  Local file scans
    happen later in enrich_findings() once the full workshop inventory is known.
    """
    findings: list[DiagnosticFinding] = []
    seen: set[tuple[str, str]] = set()

    has_world_dict_fatal = bool(WORLD_DICT_FATAL_RE.search(text))
    if has_world_dict_fatal:
        findings.append(DiagnosticFinding(
            severity="error",
            category="world_dict_fatal",
            raw_value="WorldDictionary",
            message="World failed to load: WorldDictionary error. Dictionary findings below are likely causal.",
            evidence_line="WorldDictionary: Cannot load world due to WorldDictionary error",
            likely_mod_ids=[],
            likely_workshop_ids=[],
            recommendation="Resolve all missing dictionary strings and missing client scripts before reconnecting.",
        ))

    for line in text.splitlines():
        # Missing dictionary string on client
        m = MISSING_DICT_RE.search(line)
        if m:
            key = m.group(1).strip()
            dedup = ("world_dictionary", key)
            if dedup not in seen:
                seen.add(dedup)
                findings.append(DiagnosticFinding(
                    severity="error" if has_world_dict_fatal else "warning",
                    category="world_dictionary",
                    raw_value=key,
                    message=f"Missing dictionary string: {key}",
                    evidence_line=line.strip()[:200],
                    likely_mod_ids=_get_prefix_hints(key),
                    likely_workshop_ids=[],
                    recommendation=f"Likely related mod not selected or wrong variant selected for '{key}'.",
                ))

        # Client has no script for dictionary info
        m = MISSING_SCRIPT_RE.search(line)
        if m:
            item_ref = m.group(1).strip()
            dedup = ("missing_client_script", item_ref)
            if dedup not in seen:
                seen.add(dedup)
                findings.append(DiagnosticFinding(
                    severity="warning",
                    category="missing_client_script",
                    raw_value=item_ref,
                    message=f"Client missing script: {item_ref}",
                    evidence_line=line.strip()[:200],
                    likely_mod_ids=_get_prefix_hints(item_ref),
                    likely_workshop_ids=[],
                    recommendation=f"Mod defining item '{item_ref}' may be missing or using the wrong variant.",
                ))

        # Lua runtime stack trace: Lua((MOD:name))
        for m in LUA_MOD_RUNTIME_RE.finditer(line):
            mod_display = m.group(1).strip()
            dedup = ("lua_runtime", mod_display)
            if dedup not in seen:
                seen.add(dedup)
                findings.append(DiagnosticFinding(
                    severity="warning",
                    category="lua_runtime",
                    raw_value=mod_display,
                    message=f"Lua runtime error in mod: {mod_display}",
                    evidence_line=line.strip()[:200],
                    likely_mod_ids=[mod_display],
                    likely_workshop_ids=[],
                    recommendation=f"Possibly incompatible version, missing dependency, or bad script in '{mod_display}'.",
                ))

        # SEVERE: Error found in LUA file: .../108600/WSID/mods/...
        m = LUA_FILE_ERROR_RE.search(line)
        if m:
            workshop_id = m.group(1)
            mod_folder = m.group(2)
            failing_file = m.group(3)
            dedup = ("lua_file_error", f"{workshop_id}/{failing_file}")
            if dedup not in seen:
                seen.add(dedup)
                findings.append(DiagnosticFinding(
                    severity="error",
                    category="lua_file_error",
                    raw_value=failing_file,
                    message=f"Lua file error in Workshop {workshop_id} ({mod_folder}): {failing_file}",
                    evidence_line=line.strip()[:200],
                    likely_mod_ids=[],
                    likely_workshop_ids=[workshop_id],
                    recommendation=f"Workshop item {workshop_id} has a broken Lua file. Check for a B42/MP-compatible version.",
                ))

    return findings


def _scan_workshop_for_key(
    workshop_path: Path,
    key: str,
    selected_workshop_ids: set[str],
    max_hits: int = 8,
) -> tuple[list[str], list[str]]:
    """Search downloaded Workshop text files for an exact byte sequence.

    Returns (found_in_selected, found_in_unselected) as lists of workshop IDs.
    Bounded by max_hits to keep runtime predictable; one hit per workshop item.
    """
    found_sel: list[str] = []
    found_unsel: list[str] = []
    key_b = key.encode("utf-8", errors="replace")

    if not workshop_path.exists():
        return found_sel, found_unsel

    for item_dir in sorted(workshop_path.iterdir()):
        if len(found_sel) + len(found_unsel) >= max_hits:
            break
        if not item_dir.is_dir():
            continue
        workshop_id = item_dir.name
        for file_path in item_dir.rglob("*"):
            if not file_path.is_file():
                continue
            if file_path.suffix.lower() not in _SCANNABLE_EXTENSIONS:
                continue
            try:
                if file_path.stat().st_size > _MAX_SCAN_FILE_BYTES:
                    continue
                if key_b in file_path.read_bytes():
                    if workshop_id in selected_workshop_ids:
                        found_sel.append(workshop_id)
                    else:
                        found_unsel.append(workshop_id)
                    break  # one hit per workshop item is enough
            except OSError:
                continue

    return found_sel, found_unsel


def enrich_findings(
    findings: list[DiagnosticFinding],
    workshop_path: Path,
    items: list[WorkshopItem],
) -> None:
    """Run local file scans for dictionary/script findings and update scan_result + recommendation."""
    selected_ws_ids = {item.workshop_id for item in items if item.selected_mod_id}
    ws_to_mod_ids: dict[str, list[str]] = {
        item.workshop_id: [m.mod_id for m in item.mods] for item in items
    }

    for finding in findings:
        if finding.category not in ("world_dictionary", "missing_client_script"):
            continue

        found_sel, found_unsel = _scan_workshop_for_key(
            workshop_path, finding.raw_value, selected_ws_ids
        )

        if found_sel or found_unsel:
            finding.likely_workshop_ids = dedupe_keep_order(
                finding.likely_workshop_ids + found_sel + found_unsel
            )

        sel_names = [n for wid in found_sel for n in ws_to_mod_ids.get(wid, [wid])]
        unsel_names = [n for wid in found_unsel for n in ws_to_mod_ids.get(wid, [wid])]

        if found_sel and found_unsel:
            finding.scan_result = (
                f"Found in selected: {', '.join(sel_names[:3])}. "
                f"Also in unselected: {', '.join(unsel_names[:3])}."
            )
            finding.recommendation = (
                "Key exists in a selected mod but client still missed it — "
                "possible load order issue, wrong variant, or stale world save."
            )
        elif found_sel:
            finding.scan_result = f"Found in selected mod(s): {', '.join(sel_names[:3])}."
            finding.recommendation = (
                "Key exists in selected mod files but client missed it — "
                "possible load order issue, wrong variant, or stale world save."
            )
        elif found_unsel:
            finding.scan_result = f"Found in unselected item(s): {', '.join(unsel_names[:3])}."
            finding.recommendation = (
                f"This key appears in an unselected mod — you may need to add: "
                f"{', '.join(unsel_names[:3])}."
            )
            finding.likely_mod_ids = dedupe_keep_order(
                finding.likely_mod_ids + unsel_names[:3]
            )
        else:
            finding.scan_result = "Not found in downloaded Workshop files."
            finding.recommendation = (
                f"Could not locate '{finding.raw_value}' in downloaded mod files — "
                "possibly from a removed mod, old world save, or missing Workshop download."
            )
