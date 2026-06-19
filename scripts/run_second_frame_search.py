#!/usr/bin/env python3
"""Discover repositories for the AI-topic second discovery frame."""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from vsdlc_mining.config import (  # noqa: E402
    SECOND_FRAME_CANDIDATES_PATH,
    SECOND_FRAME_CHECKPOINT_PATH,
)
from vsdlc_mining.github_client import GitHubClient, GitHubRateLimitExceeded  # noqa: E402
from vsdlc_mining.second_frame_search import run_second_frame_search  # noqa: E402
from vsdlc_mining.utils import setup_logging  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=SECOND_FRAME_CANDIDATES_PATH,
    )
    parser.add_argument(
        "--checkpoint",
        type=Path,
        default=SECOND_FRAME_CHECKPOINT_PATH,
    )
    parser.add_argument(
        "--query",
        default=None,
        help="Optional topic predicate filter (e.g. topic:llm).",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=None,
        metavar="N",
        help="Cap repository-search pages per topic predicate.",
    )
    resume_group = parser.add_mutually_exclusive_group()
    resume_group.add_argument("--resume", action="store_true")
    resume_group.add_argument("--fresh-start", action="store_true")
    parser.add_argument(
        "--exit-on-rate-limit",
        action="store_true",
        help="Exit when quota reset wait exceeds 5 minutes instead of blocking.",
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    setup_logging(getattr(logging, args.log_level))
    logger = logging.getLogger("run_second_frame_search")

    with GitHubClient(wait_for_rate_limit=not args.exit_on_rate_limit) as client:
        try:
            candidates = run_second_frame_search(
                client,
                resume=args.resume,
                fresh_start=args.fresh_start,
                checkpoint_path=args.checkpoint,
                output_path=args.output,
                query_filter=args.query,
                max_pages=args.max_pages,
            )
        except GitHubRateLimitExceeded as exc:
            logger.warning("%s", exc)
            logger.info(
                "Resume after quota reset with:\n"
                "  PYTHONPATH=src python3 scripts/run_second_frame_search.py --resume"
            )
            return 0

    logger.info("Second-frame candidates: %d -> %s", len(candidates), args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
