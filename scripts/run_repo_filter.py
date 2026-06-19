#!/usr/bin/env python3
"""CLI entry point for Phase 2 repository filtering."""

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
    ELIGIBLE_REPOS_PATH,
    EXCLUDED_REPOS_PATH,
    FILTER_SUMMARY_PATH,
    REPO_CANDIDATES_PATH,
)
from vsdlc_mining.github_client import GitHubClient, GitHubRateLimitExceeded  # noqa: E402
from vsdlc_mining.models import RepoCandidate  # noqa: E402
from vsdlc_mining.repo_filter import filter_repositories  # noqa: E402
from vsdlc_mining.utils import read_jsonl, setup_logging, write_jsonl  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Phase 2 repository filtering.")
    parser.add_argument(
        "--input",
        type=Path,
        default=REPO_CANDIDATES_PATH,
        help="JSONL input from Phase 1.",
    )
    parser.add_argument(
        "--eligible-output",
        type=Path,
        default=ELIGIBLE_REPOS_PATH,
    )
    parser.add_argument(
        "--excluded-output",
        type=Path,
        default=EXCLUDED_REPOS_PATH,
    )
    parser.add_argument(
        "--summary-output",
        type=Path,
        default=FILTER_SUMMARY_PATH,
    )
    parser.add_argument(
        "--limit-repos",
        type=int,
        default=None,
        metavar="N",
        help="Process only the first N candidate repositories (quick pilot testing).",
    )
    resume_group = parser.add_mutually_exclusive_group()
    resume_group.add_argument(
        "--resume",
        action="store_true",
        help="Skip repositories already present in eligible/excluded JSONL outputs.",
    )
    resume_group.add_argument(
        "--no-resume",
        action="store_true",
        help="Ignore existing outputs and restart filtering from scratch.",
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
    if args.limit_repos is None:
        return
    if args.eligible_output == ELIGIBLE_REPOS_PATH:
        logger.warning(
            "Pilot limit with default main eligible output %s; "
            "use --eligible-output data/interim/pilot_agents_eligible.jsonl.",
            ELIGIBLE_REPOS_PATH,
        )
    if args.excluded_output == EXCLUDED_REPOS_PATH:
        logger.warning(
            "Pilot limit with default main excluded output %s; "
            "use --excluded-output data/interim/pilot_agents_excluded.jsonl.",
            EXCLUDED_REPOS_PATH,
        )
    if args.summary_output == FILTER_SUMMARY_PATH:
        logger.warning(
            "Pilot limit with default main summary output %s; "
            "use --summary-output data/interim/pilot_agents_summary.json.",
            FILTER_SUMMARY_PATH,
        )


def main() -> int:
    args = parse_args()
    setup_logging(getattr(logging, args.log_level))
    logger = logging.getLogger("run_repo_filter")
    _warn_if_pilot_options_use_main_outputs(args, logger)

    if args.limit_repos is not None and args.limit_repos < 1:
        logger.error("--limit-repos must be >= 1")
        return 1

    if not args.input.exists():
        logger.error(
            "Input file not found: %s\n"
            "Run Phase 1 first: python scripts/run_seed_search.py\n"
            "If interrupted, resume with: python scripts/run_seed_search.py --resume",
            args.input,
        )
        return 1

    candidates = read_jsonl(args.input, RepoCandidate)
    logger.info("Loaded %d candidates from %s", len(candidates), args.input)

    resume = args.resume
    if args.no_resume:
        resume = False
    elif not args.resume and (
        args.eligible_output.exists() or args.excluded_output.exists()
    ):
        resume = True
        logger.info(
            "Existing filter outputs detected; resuming and skipping processed repos. "
            "Use --no-resume to restart from scratch.",
        )

    with GitHubClient(wait_for_rate_limit=not args.exit_on_rate_limit) as client:
        try:
            eligible, excluded, summary = filter_repositories(
                client,
                candidates,
                limit_repos=args.limit_repos,
                eligible_output_path=args.eligible_output,
                excluded_output_path=args.excluded_output,
                summary_output_path=args.summary_output,
                resume=resume,
            )
        except GitHubRateLimitExceeded as exc:
            logger.warning("%s", exc)
            logger.info(
                "Filter outputs are incremental. Resume after quota reset with:\n"
                "  python scripts/run_repo_filter.py --resume"
            )
            return 0

    logger.info("Eligible: %d -> %s", len(eligible), args.eligible_output)
    logger.info("Excluded: %d -> %s", len(excluded), args.excluded_output)
    logger.info("Summary -> %s", args.summary_output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
