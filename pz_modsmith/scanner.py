from __future__ import annotations

import re
from pathlib import Path

from .models import ModInfo
from .utils import dedupe_keep_order


BAD_SIGN_PATTERNS = [
    ("B41", re.compile(r"\bB41\b|build 41", re.IGNORECASE)),
    ("single-player/SP", re.compile(r"\bSP\b|singleplayer|single player", re.IGNORECASE)),
    ("legacy/pre-version", re.compile(r"legacy|pre[\s_-]?42|pre[\s_-]?mp|pre[\s_-]?42\.13", re.IGNORECASE)),
    ("disable/do-not-activate", re.compile(r"disable|don't activate|do not activate", re.IGNORECASE)),
    ("optional/patch", re.compile(r"optional|patch|compat|compatibility|addon", re.IGNORECASE)),
    ("no MP", re.compile(r"\bNOMP\b|no[\s_-]?mp", re.IGNORECASE)),
    ("old unstable wording", re.compile(r"unstable|deprecated", re.IGNORECASE)),
]

GOOD_SIGN_PATTERNS = [
    ("B42", re.compile(r"\bB42\b|build 42", re.IGNORECASE)),
    ("MP", re.compile(r"\bMP\b|multiplayer", re.IGNORECASE)),
    ("current/fixed", re.compile(r"current|fixed|maintained", re.IGNORECASE)),
]

# Known PZ library/framework mod IDs (lowercase). These are load-bearing mods that
# many other mods depend on; flagging them stops accidental removal.
KNOWN_LIBRARY_MOD_IDS: frozenset[str] = frozenset({
    "tsarslib",
    "tchernolib",
    "starlitlibrary",
    "thatdamnlibrary",
    "damnlib",
    "bb_utils",
    "bravenutils",
    "bravencore",
})

# Smell-detection regexes used by detect_smell_flags().
# These drive UI warnings and are intentionally separate from the scoring system.
_LIB_ID_SUFFIX_RE = re.compile(r"lib(?:rary)?$|framework$|api$", re.IGNORECASE)
_LIB_NAME_RE = re.compile(
    r"\b(?:lib(?:rary)?|framework|api|utils?|utilities|toolkit|shared)\b",
    re.IGNORECASE,
)
_TILE_RE = re.compile(r"\btiles?\b", re.IGNORECASE)
_VEHICLE_FRAMEWORK_RE = re.compile(
    r"\bvehicle[\s_-]?(?:framework|pack|lib(?:rary)?)\b", re.IGNORECASE
)
_PATCH_ADDON_RE = re.compile(r"\bpatch\b|\bcompat(?:ibility)?\b|\baddon\b", re.IGNORECASE)
_VARIANT_B41_RE = re.compile(r"\bB41\b|build[\s_-]?41", re.IGNORECASE)
_VARIANT_B42_RE = re.compile(r"\bB42\b|build[\s_-]?42", re.IGNORECASE)
_VARIANT_NOMP_RE = re.compile(r"\bNOMP\b|no[\s_-]?mp\b", re.IGNORECASE)
_VARIANT_SP_RE = re.compile(r"(?<!\w)SP(?!\w)|singleplayer|single[\s_]player", re.IGNORECASE)
_VARIANT_MP_RE = re.compile(r"(?<!\w)MP(?!\w)|multiplayer", re.IGNORECASE)
_VARIANT_LEGACY_RE = re.compile(r"\blegacy\b|\bdeprecated\b|pre[\s_-]?42|pre[\s_-]?mp", re.IGNORECASE)

_VERSION_IN_PATH_RE = re.compile(r"(?<!\d)(\d{1,3})\.(\d{1,3})(?:\.(\d{1,3}))?(?!\d)")


def _parse_version_tuple(value: str) -> tuple[int, int, int] | None:
    m = _VERSION_IN_PATH_RE.search(value)
    if not m:
        return None
    major = int(m.group(1))
    minor = int(m.group(2))
    patch = int(m.group(3) or 0)
    return (major, minor, patch)


def collapse_to_highest_version(mods: list[ModInfo]) -> list[ModInfo]:
    """Collapse multiple mod.info variants per Mod ID to the highest version.

    Workshop items often ship multiple versions of the same mod ID (e.g., 42.0, 42.15)
    in different subfolders. In most server setups you want only the newest one.
    """
    if not mods:
        return []

    def key_for(mod: ModInfo) -> tuple:
        # Prefer confirmed variants, then higher version (if present), then score.
        # If no version is present, treat it as 0.0.0.
        version = _parse_version_tuple(mod.path) or (0, 0, 0)
        return (
            1 if mod.confirmed_from_log else 0,
            version,
            mod.score,
            -len(mod.path),
        )

    best_by_id: dict[str, ModInfo] = {}
    for mod in mods:
        mod_id_key = mod.mod_id.casefold()
        if mod_id_key not in best_by_id or key_for(mod) > key_for(best_by_id[mod_id_key]):
            best_by_id[mod_id_key] = mod

    # Preserve stable ordering by original appearance of each mod_id.
    ordered_keys = dedupe_keep_order(m.mod_id.casefold() for m in mods)
    out: list[ModInfo] = []
    for k in ordered_keys:
        if k in best_by_id:
            out.append(best_by_id[k])
    return out


def detect_smell_flags(mod_id: str, name: str, description: str, requires_raw: list[str]) -> list[str]:
    """Return semantic smell flags for a mod.

    These drive UI warnings and are intentionally separate from the score/notes
    system used for auto-selection ranking.  Flags to add later (dep graph):
    'required-by-N', 'missing-dependency'.
    """
    flags: list[str] = []
    id_name = f"{mod_id} {name}"
    # description included for semantic smells (library, tiles, patch) but NOT
    # variant checks — descriptions often reference old versions ("replaces my B41
    # mod") which would produce noisy false-positive variant flags.
    id_name_desc = f"{id_name} {description}"

    # Library / framework smell: known IDs, ID suffix, or name/description keyword
    if (
        mod_id.lower() in KNOWN_LIBRARY_MOD_IDS
        or _LIB_ID_SUFFIX_RE.search(mod_id)
        or _LIB_NAME_RE.search(id_name_desc)
    ):
        flags.append("likely-library")

    if _TILE_RE.search(id_name_desc):
        flags.append("tiles")

    if _VEHICLE_FRAMEWORK_RE.search(id_name_desc):
        flags.append("vehicle-framework")

    if _PATCH_ADDON_RE.search(id_name_desc):
        flags.append("patch-or-addon")

    if requires_raw:
        flags.append("has-requires")

    # Variant flags — stored for future cross-item collision detection (step 3).
    # Not displayed in the UI yet; the scoring notes already surface these.
    if _VARIANT_NOMP_RE.search(id_name):
        flags.append("variant-nomp")
    elif _VARIANT_B41_RE.search(id_name):
        flags.append("variant-b41")
    elif _VARIANT_B42_RE.search(id_name):
        flags.append("variant-b42")

    if _VARIANT_LEGACY_RE.search(id_name):
        flags.append("variant-legacy")
    if _VARIANT_SP_RE.search(id_name):
        flags.append("variant-sp")
    elif _VARIANT_MP_RE.search(id_name):
        flags.append("variant-mp")

    return flags


def score_text(mod_id: str, name: str, path: str) -> tuple[int, list[str]]:
    haystack = f"{mod_id} {name} {path}".replace("_", " ")
    score = 0
    notes: list[str] = []

    for label, pattern in GOOD_SIGN_PATTERNS:
        if pattern.search(haystack):
            score += 2
            notes.append(f"+{label}")

    for label, pattern in BAD_SIGN_PATTERNS:
        if pattern.search(haystack):
            score -= 3
            notes.append(f"-{label}")

    return score, notes


def parse_mod_info_file(path: Path, workshop_id: str) -> ModInfo | None:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None

    mod_id = ""
    name = ""
    description = ""
    poster = ""
    url = ""
    requires_raw: list[str] = []

    for raw_line in text.splitlines():
        line = raw_line.replace("\r", "").strip()
        if "=" not in line:
            continue
        key, _, val = line.partition("=")
        key = key.strip().lower()
        val = val.strip()

        if key == "id" and not mod_id:
            mod_id = val
        elif key == "name" and not name:
            name = val
        elif key == "description" and not description:
            description = val
        elif key == "poster" and not poster:
            poster = val
        elif key == "url" and not url:
            url = val
        elif key in ("require", "requires", "required"):
            for token in re.split(r"[,;]", val):
                token = token.strip()
                if token:
                    requires_raw.append(token)

    if not mod_id:
        return None
    if not name:
        name = "(no name in mod.info)"

    score, notes = score_text(mod_id, name, str(path))
    flags = detect_smell_flags(mod_id, name, description, requires_raw)
    return ModInfo(
        workshop_id=workshop_id,
        mod_id=mod_id,
        name=name,
        path=str(path),
        score=score,
        notes=notes,
        description=description,
        poster=poster,
        url=url,
        requires_raw=requires_raw,
        flags=flags,
    )


def scan_workshop_item(workshop_path: Path, workshop_id: str) -> list[ModInfo]:
    item_dir = workshop_path / workshop_id
    if not item_dir.exists():
        return []

    infos: list[ModInfo] = []
    for mod_info_path in item_dir.rglob("mod.info"):
        info = parse_mod_info_file(mod_info_path, workshop_id)
        if info:
            infos.append(info)

    # Dedupe duplicate mod.info variants by full tuple, but keep real variants.
    unique: dict[tuple[str, str, str], ModInfo] = {}
    for info in infos:
        unique[(info.mod_id, info.name, info.path)] = info

    return sorted(unique.values(), key=lambda x: (x.mod_id.lower(), x.name.lower(), x.path.lower()))


def choose_best_guess(mods: list[ModInfo]) -> ModInfo | None:
    if not mods:
        return None

    # Highest score wins, then prefer shorter/non-weird-looking IDs and names.
    return sorted(
        mods,
        key=lambda x: (x.score, -len(x.mod_id), -len(x.name)),
        reverse=True,
    )[0]
