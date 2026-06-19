#!/usr/bin/env python3
"""CLI entry point for Phase 1 seed search."""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from vsdlc_mining.config import REPO_CANDIDATES_PATH, SEED_SEARCH_CHECKPOINT_PATH  # noqa: E402
from vsdlc_mining.github_client import GitHubClient, GitHubRateLimitExceeded  # noqa: E402
from vsdlc_mining.seed_search import run_seed_search, select_seed_queries  # noqa: E402
from vsdlc_mining.utils import setup_logging  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Phase 1 GitHub seed search.")
    parser.add_argument(
        "--query",
        type=str,
        default=None,
        help="Run only seed queries whose label or API query contains TEXT (case-insensitive).",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=None,
        metavar="N",
        help="Maximum code-search pages per query (100 results per page).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=REPO_CANDIDATES_PATH,
        help="JSONL output path for repository candidates.",
    )
    parser.add_argument(
        "--checkpoint",
        type=Path,
        default=SEED_SEARCH_CHECKPOINT_PATH,
        help="Checkpoint file for resume support.",
    )
    resume_group = parser.add_mutually_exclusive_group()
    resume_group.add_argument(
        "--resume",
        action="store_true",
        help="Resume from checkpoint after interruption or rate limiting.",
    )
    resume_group.add_argument(
        "--no-resume",
        action="store_true",
        help="Ignore any existing checkpoint and start fresh.",
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
    )
    parser.add_argument(
        "--exit-on-rate-limit",
        action="store_true",
        help="Exit when core quota reset wait exceeds 5 minutes instead of blocking.",
    )
    return parser.parse_args()


def _warn_if_pilot_options_use_main_outputs(
    args: argparse.Namespace,
    logger: logging.Logger,
) -> None:
    pilot_flags = args.query is not None or args.max_pages is not None
    if not pilot_flags:
        return
    if args.output == REPO_CANDIDATES_PATH:
        logger.warning(
            "Pilot options with default main output %s; "
            "use --output data/raw/pilot_agents_candidates.jsonl to avoid overwrite.",
            REPO_CANDIDATES_PATH,
        )
    if args.checkpoint == SEED_SEARCH_CHECKPOINT_PATH:
        logger.warning(
            "Pilot options with default main checkpoint %s; "
            "use --checkpoint data/interim/pilot_agents_checkpoint.json to isolate runs.",
            SEED_SEARCH_CHECKPOINT_PATH,
        )


def main() -> int:
    args = parse_args()
    setup_logging(getattr(logging, args.log_level))
    logger = logging.getLogger("run_seed_search")
    _warn_if_pilot_options_use_main_outputs(args, logger)

    if args.query:
        try:
            selected = select_seed_queries(args.query)
        except ValueError as exc:
            logger.error("%s", exc)
            return 1
        logger.info("Selected %d seed queries for filter %r.", len(selected), args.query)

    if args.max_pages is not None and args.max_pages < 1:
        logger.error("--max-pages must be >= 1")
        return 1

    with GitHubClient(wait_for_rate_limit=not args.exit_on_rate_limit) as client:
        try:
            candidates = run_seed_search(
                client,
                resume=args.resume,
                fresh_start=args.no_resume,
                checkpoint_path=args.checkpoint,
                output_path=args.output,
                query_filter=args.query,
                max_pages=args.max_pages,
            )
        except GitHubRateLimitExceeded as exc:
            logger.warning("%s", exc)
            logger.info(
                "Progress is checkpointed. Resume after quota reset with:\n"
                "  python scripts/run_seed_search.py --resume"
            )
            return 0

    logger.info("Wrote %d candidates to %s", len(candidates), args.output)
    if args.checkpoint.exists():
        logger.info("Checkpoint saved at %s", args.checkpoint)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
