#!/usr/bin/env python3
"""Validate the completed second-inspector functional-evidence worksheet."""

from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from vsdlc_mining.second_inspection_validation import (  # noqa: E402
    validate_second_inspection_completed,
)

logger = logging.getLogger(__name__)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--blank",
        type=Path,
        default=Path("data/processed/inspection_sample_50_second_inspector_blank.csv"),
        help="Second-inspector blank worksheet with the expected 50 repositories",
    )
    parser.add_argument(
        "--completed",
        type=Path,
        default=Path("data/processed/inspection_sample_50_second_inspector_completed.csv"),
        help="Completed second-inspector worksheet",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Optional JSON report path (stdout if omitted)",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    for path in (args.blank, args.completed):
        if not path.exists():
            logger.error("Input not found: %s", path)
            return 1

    result = validate_second_inspection_completed(args.blank, args.completed)
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"

    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
        logger.info("Wrote %s", args.output)
    else:
        print(payload, end="")

    for error in result["errors"]:
        logger.error("%s", error)
    for warning in result["warnings"]:
        logger.warning("%s", warning["message"])

    if result["valid"]:
        logger.info("Validation passed for %d repositories.", result["completed_repositories"])
        return 0

    logger.error("Validation failed with %d error(s).", len(result["errors"]))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
