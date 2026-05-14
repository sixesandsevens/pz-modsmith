from __future__ import annotations

import json
import urllib.parse
import urllib.request

from .utils import dedupe_keep_order


STEAM_API_BASE = "https://api.steampowered.com"


def _post_form(url: str, data: dict[str, str], timeout_seconds: float = 10.0) -> dict:
    body = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "pz-modsmith/1.0 (+https://github.com/openai/codex-cli)",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout_seconds) as resp:  # noqa: S310 (explicit user opt-in)
        raw = resp.read().decode("utf-8", errors="replace")
    return json.loads(raw)


def get_published_file_details(
    workshop_ids: list[str],
    *,
    return_children: bool = True,
    timeout_seconds: float = 10.0,
) -> list[dict]:
    """Fetch Steam Workshop file details for up to N Workshop IDs.

    Uses ISteamRemoteStorage/GetPublishedFileDetails which does not require an API key
    for public items.
    """
    if not workshop_ids:
        return []

    data: dict[str, str] = {
        "itemcount": str(len(workshop_ids)),
    }
    if return_children:
        data["return_children"] = "true"

    for idx, wid in enumerate(workshop_ids):
        data[f"publishedfileids[{idx}]"] = str(wid)

    payload = _post_form(
        f"{STEAM_API_BASE}/ISteamRemoteStorage/GetPublishedFileDetails/v1/",
        data,
        timeout_seconds=timeout_seconds,
    )
    response = (payload or {}).get("response") or {}
    details = response.get("publishedfiledetails") or []
    return [d for d in details if isinstance(d, dict)]


def extract_required_workshop_ids(details: list[dict]) -> list[str]:
    """Extract dependency Workshop IDs ("children") from details payloads."""
    out: list[str] = []
    for d in details:
        for child in d.get("children") or []:
            if isinstance(child, str) and child.isdigit():
                out.append(child)
            elif isinstance(child, dict):
                wid = str(child.get("publishedfileid", "")).strip()
                if wid.isdigit():
                    out.append(wid)
    return dedupe_keep_order(out)


def expand_workshop_ids_with_required_items(
    workshop_ids: list[str],
    *,
    max_depth: int = 2,
    timeout_seconds: float = 10.0,
) -> list[str]:
    """Return workshop_ids plus Steam 'required items' closure (bounded)."""
    base = dedupe_keep_order(str(w).strip() for w in workshop_ids if str(w).strip().isdigit())
    if not base:
        return []

    all_ids: list[str] = list(base)
    frontier: list[str] = list(base)

    for _ in range(max_depth):
        if not frontier:
            break
        details = get_published_file_details(
            frontier,
            return_children=True,
            timeout_seconds=timeout_seconds,
        )
        deps = extract_required_workshop_ids(details)
        new_ids = [d for d in deps if d not in set(all_ids)]
        if not new_ids:
            break
        all_ids.extend(new_ids)
        frontier = new_ids

    return all_ids

