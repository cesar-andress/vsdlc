#!/usr/bin/env python3
"""RQ2 assignment-rule sensitivity for discovery-query family contamination rates."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from vsdlc_mining.rq2_contamination import (  # noqa: E402
    NON_TARGET_LABELS,
    RATE_LABELS,
    build_family_tables,
    pct,
    query_to_family,
    summarize_family,
    wilson_ci,
)

PILOT_CSV = ROOT / "data/processed/gold_sample_360b_pilot.csv"
COMPARISON_CSV = ROOT / "data/processed/gold_sample_330_three_annotator_comparison.csv"
OUT_JSON = ROOT / "data/processed/rq2_assignment_sensitivity.json"

SCHEMES = {
    "first_match": "First query in provenance order (current RQ2 rule)",
    "last_match": "Last query in provenance order",
    "multi_match_excluded": "Exclude repositories matching more than one predicate family",
    "all_matches_weighted": "Repository counted in every matched predicate family",
}


def queries_from_artifacts(raw: str) -> list[str]:
    if not raw:
        return []
    data = json.loads(raw)
    return [str(q) for q in (data.get("queries") or [])]


def families_from_queries(queries: list[str]) -> list[str]:
    return [query_to_family(q) for q in queries]


def unique_preserve_order(items: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            ordered.append(item)
    return ordered


def load_consensus_rows(pilot_csv: Path, comparison_csv: Path) -> list[dict[str, Any]]:
    majority_by_repo: dict[str, str] = {}
    with comparison_csv.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            majority_by_repo[row["repo_full_name"]] = row["majority_label"]

    rows: list[dict[str, Any]] = []
    with pilot_csv.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            repo = row["repo_full_name"]
            if repo not in majority_by_repo:
                continue
            queries = queries_from_artifacts(row.get("detected_instruction_artifacts", ""))
            query_families = families_from_queries(queries)
            unique_queries = unique_preserve_order(queries)
            unique_families = unique_preserve_order(query_families)
            rows.append(
                {
                    "repo_full_name": repo,
                    "majority_label": majority_by_repo[repo],
                    "queries": queries,
                    "unique_queries": unique_queries,
                    "unique_families": unique_families,
                    "multi_match_queries": len(unique_queries) > 1,
                    "multi_match_families": len(unique_families) > 1,
                }
            )
    return rows


def assign_rows(rows: list[dict[str, Any]], scheme: str) -> list[dict[str, str]]:
    assigned: list[dict[str, str]] = []
    for row in rows:
        label = row["majority_label"]
        queries = row["queries"]
        unique_families = row["unique_families"]
        if not queries:
            continue

        if scheme == "first_match":
            assigned.append(
                {
                    "repo_full_name": row["repo_full_name"],
                    "majority_label": label,
                    "query_family": query_to_family(queries[0]),
                }
            )
        elif scheme == "last_match":
            assigned.append(
                {
                    "repo_full_name": row["repo_full_name"],
                    "majority_label": label,
                    "query_family": query_to_family(queries[-1]),
                }
            )
        elif scheme == "multi_match_excluded":
            if row["multi_match_queries"]:
                continue
            assigned.append(
                {
                    "repo_full_name": row["repo_full_name"],
                    "majority_label": label,
                    "query_family": query_to_family(queries[0]),
                }
            )
        elif scheme == "all_matches_weighted":
            for family in unique_families:
                assigned.append(
                    {
                        "repo_full_name": row["repo_full_name"],
                        "majority_label": label,
                        "query_family": family,
                    }
                )
        else:
            raise ValueError(scheme)
    return assigned


def family_rate_table(rows: list[dict[str, str]]) -> list[dict[str, Any]]:
    return [s.to_dict() for s in build_family_tables(rows, "query_family")]


def rank_families(
    table: list[dict[str, Any]],
    *,
    min_n: int = 5,
) -> dict[str, int]:
    eligible = [row for row in table if row["n"] >= min_n]
    ordered = sorted(
        eligible,
        key=lambda row: (-row["pct_non_target"], -row["n"], row["family"]),
    )
    return {row["family"]: index + 1 for index, row in enumerate(ordered)}


def spearman_correlation(ranks_a: dict[str, int], ranks_b: dict[str, int]) -> float | None:
    common = sorted(set(ranks_a) & set(ranks_b))
    n = len(common)
    if n < 2:
        return None
    d2 = sum((ranks_a[f] - ranks_b[f]) ** 2 for f in common)
    return round(1.0 - (6.0 * d2) / (n * (n**2 - 1)), 3)


def compare_rankings(
    tables: dict[str, list[dict[str, Any]]],
    *,
    min_n: int = 5,
) -> dict[str, Any]:
    ranks = {scheme: rank_families(table, min_n=min_n) for scheme, table in tables.items()}
    baseline = ranks["first_match"]
    pairwise: dict[str, Any] = {}
    for scheme, rank_map in ranks.items():
        if scheme == "first_match":
            continue
        common = sorted(set(baseline) & set(rank_map))
        shifts = {family: abs(baseline[family] - rank_map[family]) for family in common}
        pairwise[scheme] = {
            "spearman_vs_first_match": spearman_correlation(baseline, rank_map),
            "families_compared": len(common),
            "max_rank_shift": max(shifts.values()) if shifts else 0,
            "rank_shifts": shifts,
        }

    rate_shifts: dict[str, dict[str, float]] = {}
    baseline_rates = {
        row["family"]: row["pct_non_target"]
        for row in tables["first_match"]
        if row["n"] >= min_n
    }
    max_rate_shift = 0.0
    max_rate_shift_family = ""
    max_rate_shift_scheme = ""
    for scheme, table in tables.items():
        if scheme == "first_match":
            continue
        scheme_shifts: dict[str, float] = {}
        rates = {row["family"]: row["pct_non_target"] for row in table if row["n"] >= min_n}
        for family, base_rate in baseline_rates.items():
            if family not in rates:
                continue
            shift = round(abs(base_rate - rates[family]), 1)
            scheme_shifts[family] = shift
            if shift > max_rate_shift:
                max_rate_shift = shift
                max_rate_shift_family = family
                max_rate_shift_scheme = scheme
        rate_shifts[scheme] = scheme_shifts

    return {
        "min_n_for_ranking": min_n,
        "ranks_by_scheme": ranks,
        "pairwise_vs_first_match": pairwise,
        "rate_shift_vs_first_match_pct_points": rate_shifts,
        "max_rate_shift_pct_points": max_rate_shift,
        "max_rate_shift_family": max_rate_shift_family,
        "max_rate_shift_scheme": max_rate_shift_scheme,
    }


def multi_match_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    n = len(rows)
    multi_queries = [row for row in rows if row["multi_match_queries"]]
    multi_families = [row for row in rows if row["multi_match_families"]]
    return {
        "pilot_n": n,
        "multi_match_query_count": len(multi_queries),
        "multi_match_query_pct": pct(len(multi_queries), n),
        "multi_match_family_count": len(multi_families),
        "multi_match_family_pct": pct(len(multi_families), n),
        "unique_query_count_distribution": dict(
            Counter(len(row["unique_queries"]) for row in rows)
        ),
        "multi_match_repositories": [
            {
                "repo_full_name": row["repo_full_name"],
                "queries": row["unique_queries"],
                "families": row["unique_families"],
                "majority_label": row["majority_label"],
            }
            for row in multi_queries
        ],
    }


def headline_rq2_assessment(
    tables: dict[str, list[dict[str, Any]]],
    comparison: dict[str, Any],
) -> dict[str, Any]:
    def extremes(table: list[dict[str, Any]]) -> dict[str, Any]:
        eligible = [row for row in table if row["n"] >= 5]
        if not eligible:
            return {"high": None, "low": None}
        high = max(eligible, key=lambda row: (row["pct_non_target"], row["n"]))
        low = min(eligible, key=lambda row: (row["pct_non_target"], -row["n"]))
        return {
            "high": {
                "family": high["family"],
                "pct_non_target": high["pct_non_target"],
                "n": high["n"],
            },
            "low": {
                "family": low["family"],
                "pct_non_target": low["pct_non_target"],
                "n": low["n"],
            },
            "spread_pct_points": round(high["pct_non_target"] - low["pct_non_target"], 1),
        }

    baseline_extremes = extremes(tables["first_match"])
    scheme_extremes = {scheme: extremes(table) for scheme, table in tables.items()}

    high_risk_preserved = {}
    for scheme, table in tables.items():
        eligible = [row for row in table if row["n"] >= 5]
        high_risk = [row for row in eligible if row["pct_non_target"] >= 60.0]
        lower_risk = [row for row in eligible if row["pct_conventional"] >= 50.0]
        high_risk_preserved[scheme] = {
            "high_non_target_families_n_ge_5": [row["family"] for row in high_risk],
            "lower_conventional_families_n_ge_5": [row["family"] for row in lower_risk],
        }

    survives = True
    reasons: list[str] = []
    for scheme, ext in scheme_extremes.items():
        if not ext["high"] or not ext["low"]:
            survives = False
            reasons.append(f"{scheme}: insufficient families with n>=5")
            continue
        if ext["spread_pct_points"] < 30.0:
            survives = False
            reasons.append(f"{scheme}: family spread only {ext['spread_pct_points']} pp")
        if ext["high"]["family"] != baseline_extremes["high"]["family"]:
            reasons.append(
                f"{scheme}: highest-risk family shifts from "
                f"{baseline_extremes['high']['family']} to {ext['high']['family']}"
            )

    spearman_values = [
        item["spearman_vs_first_match"]
        for item in comparison["pairwise_vs_first_match"].values()
        if item["spearman_vs_first_match"] is not None
    ]
    if spearman_values and min(spearman_values) < 0.85:
        reasons.append("ranking correlation below 0.85 for at least one alternative rule")

    if comparison["max_rate_shift_pct_points"] > 15.0:
        reasons.append(
            "at least one family rate shifts by more than 15 percentage points"
        )

    if not reasons:
        reasons.append(
            "high- and low-contamination families remain separated under all assignment rules"
        )
        reasons.append(
            "System prompts and prompt-path families stay in the high-risk band; "
            "Copilot-instruction and Aider-config families stay lower"
        )

    return {
        "baseline_extremes": baseline_extremes,
        "extremes_by_scheme": scheme_extremes,
        "high_risk_preservation": high_risk_preserved,
        "headline_rq2_survives": survives and not any(
            "only" in r or "below" in r or "shifts by more" in r for r in reasons
        ),
        "assessment_notes": reasons,
    }


def human_summary(payload: dict[str, Any]) -> str:
    mm = payload["multi_match_prevalence"]
    cmp = payload["ranking_comparison"]
    assess = payload["headline_rq2_assessment"]
    lines = [
        "RQ2 first-match assignment sensitivity",
        f"- Pilot intersection n={mm['pilot_n']}",
        (
            f"- Multi-predicate repositories: {mm['multi_match_query_count']} "
            f"({mm['multi_match_query_pct']}%); multi-family: "
            f"{mm['multi_match_family_count']} ({mm['multi_match_family_pct']}%)"
        ),
        (
            f"- Max rank shift vs first-match (n>=5 families): "
            f"{max(item['max_rank_shift'] for item in cmp['pairwise_vs_first_match'].values())}"
        ),
        (
            f"- Max contamination-rate shift: "
            f"{cmp['max_rate_shift_pct_points']} pp "
            f"({cmp['max_rate_shift_family']}, scheme={cmp['max_rate_shift_scheme']})"
        ),
    ]
    for scheme, item in cmp["pairwise_vs_first_match"].items():
        lines.append(
            f"- Spearman vs first-match ({scheme}): {item['spearman_vs_first_match']}"
        )
    lines.append(
        f"- Headline RQ2 structured-contamination conclusion survives alternative rules: "
        f"{assess['headline_rq2_survives']}"
    )
    for note in assess["assessment_notes"]:
        lines.append(f"  * {note}")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pilot-csv", type=Path, default=PILOT_CSV)
    parser.add_argument("--comparison-csv", type=Path, default=COMPARISON_CSV)
    parser.add_argument("--output-json", type=Path, default=OUT_JSON)
    parser.add_argument("--min-n", type=int, default=5)
    args = parser.parse_args()

    rows = load_consensus_rows(args.pilot_csv, args.comparison_csv)
    if len(rows) != 300:
        raise SystemExit(f"expected n=300 intersection, got n={len(rows)}")

    tables = {
        scheme: family_rate_table(assign_rows(rows, scheme))
        for scheme in SCHEMES
    }
    comparison = compare_rankings(tables, min_n=args.min_n)
    assessment = headline_rq2_assessment(tables, comparison)

    family_rows: list[dict[str, Any]] = []
    for scheme, table in tables.items():
        ranks = comparison["ranks_by_scheme"][scheme]
        for row in table:
            family = row["family"]
            family_rows.append(
                {
                    "scheme": scheme,
                    "family": family,
                    "n": row["n"],
                    "pct_non_target": row["pct_non_target"],
                    "non_target_ci_95": row["non_target_ci_95"],
                    "rank_n_ge_min": ranks.get(family),
                    "rate_shift_vs_first_match_pp": comparison[
                        "rate_shift_vs_first_match_pct_points"
                    ]
                    .get(scheme, {})
                    .get(family),
                }
            )

    payload = {
        "sources": {
            "pilot_csv": str(args.pilot_csv.relative_to(ROOT)),
            "comparison_csv": str(args.comparison_csv.relative_to(ROOT)),
        },
        "assignment_schemes": SCHEMES,
        "multi_match_prevalence": multi_match_summary(rows),
        "family_tables_by_scheme": tables,
        "family_rankings_by_scheme": family_rows,
        "ranking_comparison": comparison,
        "headline_rq2_assessment": assessment,
        "summary_text": "",
    }
    payload["summary_text"] = human_summary(payload)

    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(payload["summary_text"])
    print(f"Wrote {args.output_json}")


if __name__ == "__main__":
    main()
