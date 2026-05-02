from __future__ import annotations

import re

from .utils import clean_value, dedupe_keep_order


ID_RE = re.compile(r"\bID=(\d{6,})\b")
# Runtime mod-load lines often look like:
#   LOG  : Mod > mod "tsarslib" overrides media/lua/...
# Those quoted values are the active Mod IDs that actually loaded, which are
# much cleaner than blindly choosing among every mod.info variant in a Workshop item.
ACTIVE_MOD_RE = re.compile(r'\bmod\s+"([^"]+)"\s+overrides\b', re.IGNORECASE)
# Catch lines like: LOG : Mod > loading NoTraitPyro
MOD_LOADING_RE = re.compile(r'\bMod\s*>\s*loading\s+(\S+)', re.IGNORECASE)
WORKSHOP_URL_RE = re.compile(r"(?:id=|sharedfiles/filedetails/\?id=)(\d{6,})")
PLAIN_ID_RE = re.compile(r"\b\d{6,}\b")


def extract_workshop_ids_from_console_text(text: str) -> list[str]:
    return dedupe_keep_order(match.group(1) for match in ID_RE.finditer(text))


def extract_active_mod_ids_from_console_text(text: str) -> list[str]:
    """Extract Mod IDs that PZ actually loaded at runtime.

    Catches both:
      mod "tsarslib" overrides ...      (high-confidence: explicit override line)
      LOG : Mod > loading NoTraitPyro   (also useful: loading-line IDs)
    These are much cleaner than blindly choosing among every mod.info variant.
    """
    ids: list[str] = []
    for m in ACTIVE_MOD_RE.finditer(text):
        ids.append(clean_value(m.group(1)))
    for m in MOD_LOADING_RE.finditer(text):
        val = clean_value(m.group(1))
        if val:
            ids.append(val)
    return dedupe_keep_order(ids)


def extract_workshop_ids_from_free_text(text: str) -> list[str]:
    ids: list[str] = []
    ids.extend(match.group(1) for match in WORKSHOP_URL_RE.finditer(text))
    ids.extend(match.group(0) for match in PLAIN_ID_RE.finditer(text))
    return dedupe_keep_order(ids)
