from __future__ import annotations

import argparse
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
from .web import run_web


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
        raise SystemExit("No Workshop IDs found.")

    return analyze(workshop_ids, workshop_path, active_mod_ids, console_text=console_text)


def main() -> None:
    parser = argparse.ArgumentParser(description="PZ Modsmith - Project Zomboid server mod-list helper")
    parser.add_argument("--web", action="store_true", help="Launch local web UI")
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

    args = parser.parse_args()

    if args.web:
        run_web(args.host, args.port)
        return

    if not args.console and not args.ids_file:
        parser.error("CLI mode requires --console or --ids-file. Or use --web.")

    result = make_cli_result(args)
    write_reports(result, expand_path(args.out))
    print((expand_path(args.out) / "summary.txt").read_text(encoding="utf-8"))
    print(f"\nWrote reports to: {expand_path(args.out)}")


if __name__ == "__main__":
    main()
