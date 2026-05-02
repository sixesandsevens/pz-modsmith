from __future__ import annotations

from pathlib import Path
from typing import Iterable

from .constants import DEFAULT_WORKSHOP_PATHS


def clean_value(value: str) -> str:
    return value.strip().replace("\r", "")


def dedupe_keep_order(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for value in values:
        if value and value not in seen:
            seen.add(value)
            out.append(value)
    return out


def expand_path(value: str | Path) -> Path:
    return Path(str(value)).expanduser().resolve()


def read_file_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        raise SystemExit(f"Could not read file: {path}\n{exc}") from exc


def detect_default_workshop_path() -> str:
    for candidate in DEFAULT_WORKSHOP_PATHS:
        path = expand_path(candidate)
        if path.exists():
            return str(path)
    return DEFAULT_WORKSHOP_PATHS[0]
