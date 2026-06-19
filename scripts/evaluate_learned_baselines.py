#!/usr/bin/env python3
"""Evaluate learned metadata-only baselines against annotation consensus."""

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

from vsdlc_mining.learned_baselines import run_learned_baseline_evaluation  # noqa: E402

logger = logging.getLogger(__name__)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--metadata",
        type=Path,
        default=Path("data/processed/gold_sample_360b_pilot.csv"),
        help="Metadata worksheet with annotation-visible fields",
    )
    parser.add_argument(
        "--labels",
        type=Path,
        default=Path("data/processed/gold_sample_330_three_annotator_comparison.csv"),
        help="Reference labels CSV (majority_label column)",
    )
    parser.add_argument(
        "--label-field",
        default="majority_label",
        help="Reference label column",
    )
    parser.add_argument("--folds", type=int, default=5)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument(
        "--skip-embeddings",
        action="store_true",
        help="Skip sentence-embedding baseline (faster; requires sentence-transformers otherwise)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/processed/learned_baseline_results.json"),
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    for path in (args.metadata, args.labels):
        if not path.exists():
            logger.error("Input not found: %s", path)
            return 1

    result = run_learned_baseline_evaluation(
        args.metadata,
        args.labels,
        label_field=args.label_field,
        n_splits=args.folds,
        random_state=args.seed,
        include_embeddings=not args.skip_embeddings,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    for task_name in ("three_class", "binary_contamination"):
        task = result[task_name]
        logger.info("Task: %s (n=%s)", task_name, task["n_repositories"])
        for model_name, metrics in task["models"].items():
            logger.info(
                "%s accuracy=%.3f precision=%.3f recall=%.3f f1=%.3f",
                model_name,
                metrics["accuracy"],
                metrics["precision_macro"],
                metrics["recall_macro"],
                metrics["f1_macro"],
            )
    logger.info("Wrote %s", args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
