#!/usr/bin/env python3
"""Filter second-frame topic candidates with main-study eligibility rules."""

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
    SECOND_FRAME_ELIGIBLE_PATH,
    SECOND_FRAME_EXCLUDED_PATH,
    SECOND_FRAME_FILTER_SUMMARY_PATH,
)
from vsdlc_mining.github_client import GitHubClient, GitHubRateLimitExceeded  # noqa: E402
from vsdlc_mining.models import RepoCandidate  # noqa: E402
from vsdlc_mining.repo_filter import filter_repositories  # noqa: E402
from vsdlc_mining.utils import read_jsonl, setup_logging  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=SECOND_FRAME_CANDIDATES_PATH)
    parser.add_argument("--eligible-output", type=Path, default=SECOND_FRAME_ELIGIBLE_PATH)
    parser.add_argument("--excluded-output", type=Path, default=SECOND_FRAME_EXCLUDED_PATH)
    parser.add_argument("--summary-output", type=Path, default=SECOND_FRAME_FILTER_SUMMARY_PATH)
    parser.add_argument("--limit-repos", type=int, default=None)
    resume_group = parser.add_mutually_exclusive_group()
    resume_group.add_argument("--resume", action="store_true")
    resume_group.add_argument("--no-resume", action="store_true")
    parser.add_argument("--exit-on-rate-limit", action="store_true")
    parser.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR"])
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    setup_logging(getattr(logging, args.log_level))
    logger = logging.getLogger("run_second_frame_filter")

    if not args.input.exists():
        logger.error("Input not found: %s", args.input)
        return 1

    candidates = read_jsonl(args.input, RepoCandidate)
    logger.info("Loaded %d second-frame candidates", len(candidates))

    resume = args.resume
    if args.no_resume:
        resume = False
    elif not args.resume and (args.eligible_output.exists() or args.excluded_output.exists()):
        resume = True
        logger.info("Existing second-frame filter outputs detected; resuming.")

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
                require_instruction_artifact=False,
            )
        except GitHubRateLimitExceeded as exc:
            logger.warning("%s", exc)
            logger.info(
                "Resume after quota reset with:\n"
                "  PYTHONPATH=src python3 scripts/run_second_frame_filter.py --resume"
            )
            return 0

    logger.info("Eligible: %d -> %s", len(eligible), args.eligible_output)
    logger.info("Excluded: %d -> %s", len(excluded), args.excluded_output)
    logger.info("Summary -> %s", args.summary_output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
