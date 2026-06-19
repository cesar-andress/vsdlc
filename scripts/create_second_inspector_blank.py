#!/usr/bin/env python3
"""Create a blind worksheet for the second functional-evidence inspector."""

from __future__ import annotations

import argparse
import csv
import logging
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from vsdlc_mining.inspection_sample import (  # noqa: E402
    INSPECTION_BLANK_METADATA_FIELDS,
    write_second_inspector_blank_csv,
)

logger = logging.getLogger(__name__)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("data/processed/inspection_sample_50_blank.csv"),
        help="Existing blind worksheet or reference metadata CSV for the same 50 repositories",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/processed/inspection_sample_50_second_inspector_blank.csv"),
        help="Second-inspector blank worksheet output",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    if not args.source.exists():
        logger.error("Input not found: %s", args.source)
        return 1

    with args.source.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    metadata_rows = [
        {field: row.get(field, "") for field in INSPECTION_BLANK_METADATA_FIELDS} for row in rows
    ]
    if len(metadata_rows) != 50:
        logger.warning("Source worksheet contains %d repositories (expected 50).", len(metadata_rows))

    count = write_second_inspector_blank_csv(args.output, metadata_rows)
    logger.info("Wrote %d repositories to %s", count, args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
