"""Command-line entry point for AnimeBench."""

from __future__ import annotations

import argparse
from collections.abc import Sequence

from animebench import __version__


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line argument parser."""
    parser = argparse.ArgumentParser(
        prog="animebench",
        description="Benchmark detailed anime knowledge in AI models.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the placeholder AnimeBench CLI."""
    parser = build_parser()
    parser.parse_args(argv)
    print("AnimeBench is scaffolded; benchmark questions are coming next.")
    return 0
