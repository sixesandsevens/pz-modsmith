from __future__ import annotations

import json
import urllib.parse
import urllib.request

from .utils import dedupe_keep_order


STEAM_API_BASE = "https://api.steampowered.com"

# Steam enum values for IPublishedFileService/QueryFiles `query_type`.
QUERY_TYPE_RANKED_BY_TEXT_SEARCH = 12
# Per Steam client enums: RankedByTotalUniqueSubscriptions == 9.
QUERY_TYPE_RANKED_BY_TOTAL_UNIQUE_SUBSCRIPTIONS = 9
QUERY_TYPE_RANKED_BY_TREND = 3
QUERY_TYPE_RANKED_BY_PUBLICATION_DATE = 1
QUERY_TYPE_RANKED_BY_LAST_UPDATED_DATE = 21


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


def _get(url: str, params: dict[str, str], timeout_seconds: float = 10.0) -> dict:
    qs = urllib.parse.urlencode(params)
    full_url = f"{url}?{qs}"
    req = urllib.request.Request(
        full_url,
        headers={
            "User-Agent": "pz-modsmith/1.0 (+https://github.com/openai/codex-cli)",
        },
        method="GET",
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


def get_workshop_item_summaries(
    workshop_ids: list[str],
    *,
    batch_size: int = 100,
    timeout_seconds: float = 10.0,
) -> dict[str, dict[str, object]]:
    """Fetch basic metadata for Workshop IDs (no API key required).

    Returns a dict keyed by workshop id with fields commonly used in the UI:
    title, preview_url, time_updated, subscriptions, visibility.
    """
    clean = dedupe_keep_order(str(w).strip() for w in workshop_ids if str(w).strip().isdigit())
    if not clean:
        return {}

    out: dict[str, dict[str, object]] = {}
    for i in range(0, len(clean), batch_size):
        batch = clean[i : i + batch_size]
        details = get_published_file_details(batch, return_children=False, timeout_seconds=timeout_seconds)
        for d in details:
            wid = str(d.get("publishedfileid", "")).strip()
            if not wid:
                continue
            out[wid] = {
                "title": d.get("title") or "",
                "preview_url": d.get("preview_url") or "",
                "time_updated": int(d.get("time_updated") or 0),
                "subscriptions": int(d.get("subscriptions") or 0),
                "visibility": int(d.get("visibility") or 0),
            }
    return out

class SteamApiKeyMissing(Exception):
    """Raised when an API key is required but was not provided."""


def get_published_file_service_details(
    workshop_ids: list[str],
    *,
    api_key: str,
    include_children: bool = True,
    timeout_seconds: float = 10.0,
) -> list[dict]:
    """Fetch Workshop details using IPublishedFileService/GetDetails (API key required).

    This endpoint is required to reliably access "required items" (children) for many
    Workshop items. Unlike GetPublishedFileDetails, it requires a Steam Web API key.
    """
    clean_ids = [str(w).strip() for w in workshop_ids if str(w).strip().isdigit()]
    if not clean_ids:
        return []

    if not api_key or not api_key.strip():
        raise SteamApiKeyMissing("Steam Web API key required for IPublishedFileService/GetDetails")

    params: dict[str, str] = {
        "key": api_key.strip(),
        "itemcount": str(len(clean_ids)),
    }
    if include_children:
        params["includechildren"] = "true"
    for idx, wid in enumerate(clean_ids):
        params[f"publishedfileids[{idx}]"] = wid

    payload = _get(
        f"{STEAM_API_BASE}/IPublishedFileService/GetDetails/v1/",
        params,
        timeout_seconds=timeout_seconds,
    )
    response = (payload or {}).get("response") or {}
    details = response.get("publishedfiledetails") or []
    return [d for d in details if isinstance(d, dict)]


def query_workshop(
    *,
    api_key: str,
    search_text: str = "",
    page: int = 1,
    per_page: int = 20,
    query_type: int = QUERY_TYPE_RANKED_BY_TEXT_SEARCH,
    app_id: str = "108600",
    required_tags: list[str] | None = None,
    cursor: str | None = None,
    timeout_seconds: float = 15.0,
) -> dict:
    """Search/browse Workshop using IPublishedFileService/QueryFiles (API key required)."""
    if not api_key or not api_key.strip():
        raise SteamApiKeyMissing("Steam Web API key required for Workshop search/browse.")

    params: dict[str, str] = {
        "key": api_key.strip(),
        "query_type": str(query_type),
        "page": str(max(page, 1)),
        "numperpage": str(min(max(per_page, 1), 100)),
        "creator_appid": str(app_id),
        "appid": str(app_id),
        "cursor": cursor if cursor is not None else "*",
        "return_details": "true",
        "return_tags": "true",
        "return_previews": "true",
        "return_short_description": "true",
        "return_vote_data": "true",
    }

    # For RankedByTrend queries, Steam expects a day range for recent votes.
    if query_type == QUERY_TYPE_RANKED_BY_TREND:
        params["days"] = "7"
        params["include_recent_votes_only"] = "true"
    if search_text.strip():
        params["search_text"] = search_text.strip()
    if required_tags:
        for i, tag in enumerate(required_tags):
            params[f"requiredtags[{i}]"] = tag

    return _get(
        f"{STEAM_API_BASE}/IPublishedFileService/QueryFiles/v1/",
        params,
        timeout_seconds=timeout_seconds,
    )


def get_collection_details(
    collection_ids: list[str],
    *,
    timeout_seconds: float = 10.0,
) -> dict[str, list[str]]:
    """Resolve Workshop collection IDs to lists of member Workshop IDs.

    Uses ISteamRemoteStorage/GetCollectionDetails which does not require an API key.
    Returns a mapping of collection_id -> deduped list of member ids.
    """
    clean = dedupe_keep_order(str(c).strip() for c in collection_ids if str(c).strip().isdigit())
    if not clean:
        return {}

    data: dict[str, str] = {"collectioncount": str(len(clean))}
    for idx, cid in enumerate(clean):
        data[f"publishedfileids[{idx}]"] = cid

    payload = _post_form(
        f"{STEAM_API_BASE}/ISteamRemoteStorage/GetCollectionDetails/v1/",
        data,
        timeout_seconds=timeout_seconds,
    )
    response = (payload or {}).get("response") or {}
    collection_details = response.get("collectiondetails") or []

    out: dict[str, list[str]] = {}
    for col in collection_details:
        if not isinstance(col, dict):
            continue
        cid = str(col.get("publishedfileid", "")).strip()
        if not cid:
            continue
        children: list[str] = []
        for child in (col.get("children") or []):
            if isinstance(child, dict):
                wid = str(child.get("publishedfileid", "")).strip()
            else:
                wid = str(child).strip()
            if wid.isdigit():
                children.append(wid)
        out[cid] = dedupe_keep_order(children)

    return out


def expand_collection_ids(
    ids: list[str],
    *,
    timeout_seconds: float = 10.0,
) -> list[str]:
    """Expand any collection IDs in a mixed list into their member Workshop IDs.

    Steam's GetPublishedFileDetails response does not reliably include a `file_type`
    field, so we detect collections via GetCollectionDetails: ids that return a
    non-empty children list are treated as collections.
    """
    clean = dedupe_keep_order(str(i).strip() for i in ids if str(i).strip().isdigit())
    if not clean:
        return []

    col_members = get_collection_details(clean, timeout_seconds=timeout_seconds)
    out: list[str] = []
    for wid in clean:
        members = col_members.get(wid) or []
        if members:
            out.extend(members)
        else:
            out.append(wid)
    return dedupe_keep_order(out)


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
    api_key: str | None = None,
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
        if api_key:
            details = get_published_file_service_details(
                frontier,
                api_key=api_key,
                include_children=True,
                timeout_seconds=timeout_seconds,
            )
        else:
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


def expand_workshop_ids_with_collections_and_required_items(
    ids: list[str],
    *,
    max_depth: int = 2,
    timeout_seconds: float = 10.0,
    api_key: str | None = None,
) -> list[str]:
    """Expand collections first, then expand required-item dependencies."""
    expanded = expand_collection_ids(ids, timeout_seconds=timeout_seconds)
    return expand_workshop_ids_with_required_items(
        expanded,
        max_depth=max_depth,
        timeout_seconds=timeout_seconds,
        api_key=api_key,
    )
