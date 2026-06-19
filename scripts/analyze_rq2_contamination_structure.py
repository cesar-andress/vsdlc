#!/usr/bin/env python3
"""RQ2: contamination structure by query family, matched path, and metadata sparsity."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from vsdlc_mining.rq2_contamination import (  # noqa: E402
    build_family_tables,
    identify_risk_families,
    matched_path_to_family,
    metadata_sparsity,
    primary_language_group,
    primary_path_from_artifacts,
    primary_query_from_artifacts,
    query_to_family,
)

PILOT_CSV = ROOT / "data/processed/gold_sample_360b_pilot.csv"
COMPARISON_CSV = ROOT / "data/processed/gold_sample_330_three_annotator_comparison.csv"
OUT_JSON = ROOT / "data/processed/rq2_contamination_structure.json"
OUT_QUERY_CSV = ROOT / "data/processed/rq2_query_family_table.csv"
OUT_PATH_CSV = ROOT / "data/processed/rq2_matched_path_family_table.csv"
OUT_SPARSE_CSV = ROOT / "data/processed/rq2_sparse_metadata_table.csv"

TABLE_FIELDS = [
    "family",
    "n",
    "tie_count",
    "conventional_count",
    "ai_product_count",
    "exclude_count",
    "non_target_count",
    "pct_conventional",
    "pct_ai_product",
    "pct_exclude",
    "pct_non_target",
    "non_target_ci_low",
    "non_target_ci_high",
]


def load_intersection_rows(
    pilot_csv: Path,
    comparison_csv: Path,
) -> list[dict[str, str]]:
    majority_by_repo: dict[str, str] = {}
    with comparison_csv.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            majority_by_repo[row["repo_full_name"]] = row["majority_label"]

    rows: list[dict[str, str]] = []
    with pilot_csv.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            repo = row["repo_full_name"]
            if repo not in majority_by_repo:
                continue
            artifacts = row.get("detected_instruction_artifacts", "")
            rows.append(
                {
                    "repo_full_name": repo,
                    "majority_label": majority_by_repo[repo],
                    "query_family": query_to_family(primary_query_from_artifacts(artifacts)),
                    "matched_path_family": matched_path_to_family(
                        primary_path_from_artifacts(artifacts)
                    ),
                    "metadata_sparsity": metadata_sparsity(
                        row.get("github_description", ""),
                        row.get("github_topics", ""),
                    ),
                    "primary_language_group": primary_language_group(
                        row.get("primary_language", "")
                    ),
                }
            )
    return rows


def stats_to_csv_rows(stats: list[Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for item in stats:
        payload = item.to_dict()
        rows.append(
            {
                **{k: payload[k] for k in TABLE_FIELDS if k in payload},
                "non_target_ci_low": payload["non_target_ci_95"][0],
                "non_target_ci_high": payload["non_target_ci_95"][1],
            }
        )
    return rows


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=TABLE_FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pilot-csv", type=Path, default=PILOT_CSV)
    parser.add_argument("--comparison-csv", type=Path, default=COMPARISON_CSV)
    parser.add_argument("--output-json", type=Path, default=OUT_JSON)
    args = parser.parse_args()

    rows = load_intersection_rows(args.pilot_csv, args.comparison_csv)
    n = len(rows)
    if n != 300:
        raise SystemExit(f"expected n=300 intersection, got n={n}")

    query_stats = build_family_tables(rows, "query_family")
    path_stats = build_family_tables(rows, "matched_path_family")
    sparse_stats = build_family_tables(rows, "metadata_sparsity")
    language_stats = build_family_tables(rows, "primary_language_group")

    payload = {
        "n_intersection": n,
        "sources": {
            "pilot_csv": str(args.pilot_csv.relative_to(ROOT)),
            "comparison_csv": str(args.comparison_csv.relative_to(ROOT)),
        },
        "definitions": {
            "rate_denominator": "repositories with consensus label in {CONVENTIONAL_SOFTWARE, AI_PRODUCT, EXCLUDE}; TIE excluded from rates",
            "non_target": "AI_PRODUCT + EXCLUDE",
            "non_target_ci": "Wilson 95% interval on non_target rate",
        },
        "query_family_table": [s.to_dict() for s in query_stats],
        "matched_path_family_table": [s.to_dict() for s in path_stats],
        "sparse_metadata_table": [s.to_dict() for s in sparse_stats],
        "primary_language_group_table": [s.to_dict() for s in language_stats],
        "high_risk_query_families": identify_risk_families(query_stats)["high_non_target"],
        "lower_risk_query_families": identify_risk_families(query_stats)["lower_non_target"],
        "high_risk_path_families": identify_risk_families(path_stats)["high_non_target"],
        "high_exclude_query_families": sorted(
            [s.to_dict() for s in query_stats if s.n >= 5],
            key=lambda d: (-d["pct_exclude"], -d["n"]),
        )[:5],
        "high_exclude_path_families": sorted(
            [s.to_dict() for s in path_stats if s.n >= 5],
            key=lambda d: (-d["pct_exclude"], -d["n"]),
        )[:5],
    }

    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    write_csv(OUT_QUERY_CSV, stats_to_csv_rows(query_stats))
    write_csv(OUT_PATH_CSV, stats_to_csv_rows(path_stats))
    write_csv(OUT_SPARSE_CSV, stats_to_csv_rows(sparse_stats))

    print(f"Wrote {args.output_json}")
    print(f"Wrote {OUT_QUERY_CSV}")
    print(f"Wrote {OUT_PATH_CSV}")
    print(f"Wrote {OUT_SPARSE_CSV}")
    print(f"n={n}")
    print("Top NON_TARGET query families:")
    for row in payload["high_risk_query_families"][:5]:
        print(f"  {row['family']}: {row['pct_non_target']}% (n={row['n']})")


if __name__ == "__main__":
    main()
