from __future__ import annotations

import argparse
import os
from pathlib import Path

from .constants import DEFAULT_PORT
from .utils import expand_path, read_file_text, detect_default_workshop_path
from .log_parser import (
    extract_workshop_ids_from_console_text,
    extract_active_mod_ids_from_console_text,
    extract_workshop_ids_from_free_text,
)
from .analysis import analyze, apply_selection
from .models import AnalysisResult
from .reports import write_reports
from .web import run_app, run_web
from .steam_api import expand_workshop_ids_with_collections_and_required_items


def make_cli_result(args: argparse.Namespace) -> AnalysisResult:
    workshop_path = expand_path(args.workshop_path)
    if not workshop_path.exists():
        raise SystemExit(f"Workshop path does not exist: {workshop_path}")

    active_mod_ids: list[str] = []
    console_text = ""
    if args.console:
        console_text = read_file_text(expand_path(args.console))
        workshop_ids = extract_workshop_ids_from_console_text(console_text)
        active_mod_ids = extract_active_mod_ids_from_console_text(console_text)
    elif args.ids_file:
        text = read_file_text(expand_path(args.ids_file))
        workshop_ids = extract_workshop_ids_from_free_text(text)
    else:
        raise SystemExit("Expected --console or --ids-file")

    if not workshop_ids:
        if not active_mod_ids:
            raise SystemExit("No Workshop IDs found.")

    if getattr(args, "fetch_steam_deps", False) and workshop_ids:
        steam_api_key = (
            getattr(args, "steam_api_key", None)
            or os.environ.get("PZ_MODSMITH_STEAM_API_KEY")
            or os.environ.get("STEAM_WEB_API_KEY")
        )
        workshop_ids = expand_workshop_ids_with_collections_and_required_items(
            workshop_ids,
            max_depth=getattr(args, "deps_depth", 2),
            api_key=steam_api_key,
        )

    return analyze(
        workshop_ids,
        workshop_path,
        active_mod_ids,
        console_text=console_text,
        prefer_highest_version=getattr(args, "prefer_highest_version", False),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="PZ Modsmith - Project Zomboid server mod-list helper")
    parser.add_argument("--web", action="store_true", help="Launch local web UI")
    parser.add_argument("--app", action="store_true", help="Launch local app-style web UI and open a browser")
    parser.add_argument("--host", default="127.0.0.1", help="Web UI bind host")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="Web UI port")

    source = parser.add_mutually_exclusive_group(required=False)
    source.add_argument("--console", type=Path, help="Path to ~/Zomboid/console.txt from a server join attempt")
    source.add_argument("--ids-file", type=Path, help="Path to a file containing Workshop IDs/URLs")

    parser.add_argument(
        "--workshop-path",
        type=Path,
        default=Path(detect_default_workshop_path()),
        help="Path to Steam workshop content/108600 folder",
    )
    parser.add_argument("--out", type=Path, default=Path("./pzmodsmith-output"), help="CLI output folder")
    parser.add_argument(
        "--fetch-steam-deps",
        dest="fetch_steam_deps",
        action="store_true",
        help='Fetch Steam Workshop "required items" (online) and include them',
    )
    parser.add_argument(
        "--steam-api-key",
        dest="steam_api_key",
        default=None,
        help="Steam Web API key (optional; also read from PZ_MODSMITH_STEAM_API_KEY/STEAM_WEB_API_KEY)",
    )
    parser.add_argument(
        "--deps-depth",
        type=int,
        default=2,
        help="Dependency expansion depth when using --fetch-steam-deps",
    )
    parser.add_argument(
        "--prefer-highest-version",
        action="store_true",
        help="When the same Mod ID has multiple variants, keep the highest version",
    )

    args = parser.parse_args()

    if args.web:
        run_web(args.host, args.port)
        return

    if args.app:
        run_app(args.host, args.port)
        return

    if not args.console and not args.ids_file:
        parser.error("CLI mode requires --console or --ids-file. Or use --web or --app.")

    result = make_cli_result(args)
    write_reports(result, expand_path(args.out))
    print((expand_path(args.out) / "summary.txt").read_text(encoding="utf-8"))
    print(f"\nWrote reports to: {expand_path(args.out)}")


if __name__ == "__main__":
    main()
