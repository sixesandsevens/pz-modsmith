from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


def _collect_keys(value: Any) -> set[str]:
    if not isinstance(value, dict):
        return set()
    return set(value.keys())


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python -m pz_modsmith.inspect_steam_fixture <path/to/json>", file=sys.stderr)
        return 2

    path = Path(argv[1])
    payload = json.loads(path.read_text(encoding="utf-8"))

    response = (payload or {}).get("response") or {}
    details = response.get("publishedfiledetails") or []

    print(f"items: {len(details)}")
    if not details:
        return 0

    keys = sorted(_collect_keys(details[0]))
    print(f"first_item_keys({len(keys)}): {', '.join(keys)}")

    # A couple of common nested shapes worth surfacing.
    first = details[0]
    if isinstance(first, dict):
        file_type = first.get("file_type")
        if file_type is not None:
            print(f"file_type: {file_type}")

        visibility = first.get("visibility")
        if visibility is not None:
            print(f"visibility: {visibility}")

        children = first.get("children")
        if isinstance(children, list):
            print(f"children: {len(children)}")
            if children:
                child0 = children[0]
                print(f"children[0] keys: {', '.join(sorted(_collect_keys(child0)))}")

        tags = first.get("tags")
        if isinstance(tags, list):
            print(f"tags: {len(tags)}")
            if tags:
                tag0 = tags[0]
                print(f"tags[0] keys: {', '.join(sorted(_collect_keys(tag0)))}")

        vote_data = first.get("vote_data")
        if isinstance(vote_data, dict) and vote_data:
            print(f"vote_data keys: {', '.join(sorted(vote_data.keys()))}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
