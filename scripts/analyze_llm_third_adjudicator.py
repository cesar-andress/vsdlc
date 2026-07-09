#!/usr/bin/env python3
"""Characterize model-assisted annotator behaviour in the three-coder plurality protocol."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from vsdlc_mining.annotation_agreement import (  # noqa: E402
    cohens_kappa,
    confusion_matrix,
    per_class_metrics,
)
from vsdlc_mining.decontamination_schema import PRIMARY_LABELS  # noqa: E402

COMPARISON_CSV = ROOT / "data/processed/gold_sample_330_three_annotator_comparison.csv"
INSPECTION_REF = ROOT / "data/processed/inspection_sample_50.csv"
INSPECTION_COMPLETED = ROOT / "data/processed/inspection_sample_50_completed_fixed.csv"
OUT_JSON = ROOT / "data/processed/llm_third_adjudicator_audit.json"
OUT_TEX = ROOT / "data/processed/manuscript_table_llm_adjudicator_audit.tex"

CATEGORIES = tuple(PRIMARY_LABELS)


def normalize(label: str) -> str:
    return (label or "").strip().upper()


def load_comparison(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        row["claude_label"] = normalize(row["claude_label"])
        row["human1_label"] = normalize(row["human1_label"])
        row["human2_label"] = normalize(row["human2_label"])
        row["majority_label"] = normalize(row["majority_label"])
        if "human_only_label" in row:
            row["human_only_label"] = normalize(row["human_only_label"])
        if "human_disagreement" in row:
            row["human_disagreement"] = row["human_disagreement"].strip().lower()
    return rows


def f1(precision: float, recall: float) -> float:
    if precision + recall == 0:
        return 0.0
    return 2 * precision * recall / (precision + recall)


def enrich_per_class(metrics: dict[str, dict[str, float | int]]) -> dict[str, dict[str, float | int]]:
    enriched: dict[str, dict[str, float | int]] = {}
    for cat, values in metrics.items():
        precision = float(values["precision"])
        recall = float(values["recall"])
        enriched[cat] = {
            **values,
            "f1": round(f1(precision, recall), 3),
            "precision": round(precision, 3),
            "recall": round(recall, 3),
        }
    return enriched


def aggregate_f1(
    per_class: dict[str, dict[str, float | int]],
    support: Counter[str],
) -> dict[str, float]:
    classes = [cat for cat in CATEGORIES if support.get(cat, 0) > 0]
    if not classes:
        return {"macro_f1": 0.0, "weighted_f1": 0.0}
    macro = sum(float(per_class[cat]["f1"]) for cat in classes) / len(classes)
    total = sum(support[cat] for cat in classes)
    weighted = (
        sum(float(per_class[cat]["f1"]) * support[cat] for cat in classes) / total if total else 0.0
    )
    return {"macro_f1": round(macro, 3), "weighted_f1": round(weighted, 3)}


def compare_pair(
    reference: list[str],
    comparison: list[str],
    *,
    reference_name: str,
    comparison_name: str,
) -> dict[str, Any]:
    if len(reference) != len(comparison):
        raise ValueError("label lists differ in length")
    n = len(reference)
    agreement = round(sum(1 for a, b in zip(reference, comparison) if a == b) / n, 3) if n else 0.0
    kappa = cohens_kappa(reference, comparison, CATEGORIES)
    matrix = confusion_matrix(reference, comparison, CATEGORIES)
    per_class = enrich_per_class(per_class_metrics(comparison, reference, CATEGORIES))
    support = Counter(reference)
    f1_scores = aggregate_f1(per_class, support)
    return {
        "reference": reference_name,
        "comparison": comparison_name,
        "n": n,
        "overall_agreement": agreement,
        "cohens_kappa": round(kappa, 3) if kappa is not None else None,
        "confusion_matrix_reference_rows": matrix,
        "per_class_metrics_reference_as_gold": per_class,
        "macro_f1": f1_scores["macro_f1"],
        "weighted_f1": f1_scores["weighted_f1"],
        "reference_label_distribution": dict(support),
        "comparison_label_distribution": dict(Counter(comparison)),
    }


def pairwise_audit(rows: list[dict[str, str]]) -> dict[str, Any]:
    h1 = [row["human1_label"] for row in rows]
    h2 = [row["human2_label"] for row in rows]
    llm = [row["claude_label"] for row in rows]
    return {
        "llm_vs_human1": compare_pair(h1, llm, reference_name="human1", comparison_name="llm"),
        "llm_vs_human2": compare_pair(h2, llm, reference_name="human2", comparison_name="llm"),
        "human1_vs_human2": compare_pair(h1, h2, reference_name="human1", comparison_name="human2"),
    }


def human_disagreement_audit(rows: list[dict[str, str]]) -> dict[str, Any]:
    subset = [
        row
        for row in rows
        if row.get("human_disagreement") == "true"
        or row["human1_label"] != row["human2_label"]
    ]
    llm_agrees_h1 = sum(1 for row in subset if row["claude_label"] == row["human1_label"])
    llm_agrees_h2 = sum(1 for row in subset if row["claude_label"] == row["human2_label"])
    llm_agrees_neither = sum(
        1
        for row in subset
        if row["claude_label"] != row["human1_label"] and row["claude_label"] != row["human2_label"]
    )
    majority = Counter(row["majority_label"] for row in subset if row["majority_label"] != "TIE")
    llm_labels = Counter(row["claude_label"] for row in subset)
    h1_labels = Counter(row["human1_label"] for row in subset)
    h2_labels = Counter(row["human2_label"] for row in subset)
    sided_with_h1 = sum(
        1
        for row in subset
        if row["majority_label"] != "TIE"
        and row["majority_label"] == row["human1_label"]
        and row["human1_label"] != row["human2_label"]
    )
    sided_with_h2 = sum(
        1
        for row in subset
        if row["majority_label"] != "TIE"
        and row["majority_label"] == row["human2_label"]
        and row["human1_label"] != row["human2_label"]
    )
    return {
        "n_human_disagreement": len(subset),
        "llm_agrees_human1_count": llm_agrees_h1,
        "llm_agrees_human1_pct": round(100.0 * llm_agrees_h1 / len(subset), 1) if subset else 0.0,
        "llm_agrees_human2_count": llm_agrees_h2,
        "llm_agrees_human2_pct": round(100.0 * llm_agrees_h2 / len(subset), 1) if subset else 0.0,
        "llm_agrees_neither_count": llm_agrees_neither,
        "llm_agrees_neither_pct": round(100.0 * llm_agrees_neither / len(subset), 1) if subset else 0.0,
        "plurality_sided_with_human1": sided_with_h1,
        "plurality_sided_with_human2": sided_with_h2,
        "plurality_label_distribution": dict(majority),
        "llm_label_distribution": dict(llm_labels),
        "human1_label_distribution": dict(h1_labels),
        "human2_label_distribution": dict(h2_labels),
        "repositories": [
            {
                "repo_full_name": row["repo_full_name"],
                "human1_label": row["human1_label"],
                "human2_label": row["human2_label"],
                "claude_label": row["claude_label"],
                "majority_label": row["majority_label"],
            }
            for row in subset
        ],
    }


def inspection_audit(
    comparison_rows: list[dict[str, str]],
    inspection_ref: Path,
    inspection_completed: Path,
) -> dict[str, Any]:
    by_repo = {row["repo_full_name"]: row for row in comparison_rows}
    completed = {}
    with inspection_completed.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            repo = row["repo_full_name"].strip()
            label = normalize(row.get("inspection_label", ""))
            if repo and label in CATEGORIES:
                completed[repo] = label

    repos = sorted(set(by_repo) & set(completed))
    inspection = [completed[repo] for repo in repos]
    comparisons = {
        "three_way_plurality": [by_repo[repo]["majority_label"] for repo in repos],
        "llm": [by_repo[repo]["claude_label"] for repo in repos],
        "human1": [by_repo[repo]["human1_label"] for repo in repos],
        "human2": [by_repo[repo]["human2_label"] for repo in repos],
    }
    results = {
        "n_inspected": len(repos),
        "repos": repos,
        "inspection_label_distribution": dict(Counter(inspection)),
    }
    for name, labels in comparisons.items():
        results[name] = compare_pair(
            inspection,
            labels,
            reference_name="functional_inspection",
            comparison_name=name,
        )
    return results


def render_tex(audit: dict[str, Any]) -> str:
    pairwise = audit["pairwise_agreement"]
    inspection = audit["functional_validation"]
    disagree = audit["human_disagreement_subset"]

    def row_for(key: str) -> str:
        item = pairwise[key]
        return (
            f"    {item['comparison']} vs.\\ {item['reference']} & {item['n']} & "
            f"{100 * item['overall_agreement']:.1f}\\% & {item['cohens_kappa']:.3f} & "
            f"{item['macro_f1']:.3f} & {item['weighted_f1']:.3f} \\\\"
        )

    lines = [
        "% Auto-generated by analyze_llm_third_adjudicator.py",
        "\\begin{table}[t]",
        "  \\centering",
        "  \\footnotesize",
        "  \\caption{Round~1 coder agreement on the 300-repository intersection.}",
        "  \\label{tab:llm-coder-agreement}",
        "  \\begin{tabular}{@{}lrrrrr@{}}",
        "    \\toprule",
        "    Comparison & $n$ & Agree. & $\\kappa$ & Macro F1 & Wtd.\\ F1 \\\\",
        "    \\midrule",
        row_for("llm_vs_human1"),
        row_for("llm_vs_human2"),
        row_for("human1_vs_human2"),
        "    \\bottomrule",
        "  \\end{tabular}",
        "\\end{table}",
        "",
        "\\begin{table}[t]",
        "  \\centering",
        "  \\footnotesize",
        "  \\caption{Functional-evidence comparison on $n{=}50$ inspected repositories (inspection label as reference).}",
        "  \\label{tab:llm-inspection-comparison}",
        "  \\begin{tabular}{@{}lrrrrr@{}}",
        "    \\toprule",
        "    Round~1 label source & $n$ & Agree. & $\\kappa$ & Macro F1 & Wtd.\\ F1 \\\\",
        "    \\midrule",
    ]
    for key, label in [
        ("three_way_plurality", "Three-way plurality"),
        ("llm", "LLM-assisted"),
        ("human1", "Human-1"),
        ("human2", "Human-2"),
    ]:
        item = inspection[key]
        lines.append(
            f"    {label} & {item['n']} & {100 * item['overall_agreement']:.1f}\\% & "
            f"{item['cohens_kappa']:.3f} & {item['macro_f1']:.3f} & {item['weighted_f1']:.3f} \\\\"
        )
    lines.extend(
        [
            "    \\bottomrule",
            "  \\end{tabular}",
            "\\end{table}",
            "",
            (
                f"% Human-disagreement subset: n={disagree['n_human_disagreement']}; "
                f"LLM agrees H1 {disagree['llm_agrees_human1_pct']}\\%; "
                f"H2 {disagree['llm_agrees_human2_pct']}\\%"
            ),
        ]
    )
    return "\n".join(lines) + "\n"


def build_audit(
    comparison_csv: Path,
    inspection_ref: Path,
    inspection_completed: Path,
) -> dict[str, Any]:
    rows = load_comparison(comparison_csv)
    pairwise = pairwise_audit(rows)
    disagree = human_disagreement_audit(rows)
    inspection = inspection_audit(rows, inspection_ref, inspection_completed)
    return {
        "source_comparison_csv": str(comparison_csv.relative_to(ROOT)),
        "pairwise_agreement": pairwise,
        "human_disagreement_subset": disagree,
        "functional_validation": inspection,
        "interpretation_notes": [
            "Metrics treat the first named annotator as reference for per-class precision/recall/F1.",
            "Overall agreement and Cohen's kappa are symmetric for pairwise coder comparisons.",
            "Functional validation uses inspection_label as reference on n=50 stratified repositories.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--comparison", type=Path, default=COMPARISON_CSV)
    parser.add_argument("--inspection-ref", type=Path, default=INSPECTION_REF)
    parser.add_argument("--inspection-completed", type=Path, default=INSPECTION_COMPLETED)
    parser.add_argument("--out-json", type=Path, default=OUT_JSON)
    parser.add_argument("--out-tex", type=Path, default=OUT_TEX)
    args = parser.parse_args()

    audit = build_audit(args.comparison, args.inspection_ref, args.inspection_completed)
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    args.out_tex.write_text(render_tex(audit), encoding="utf-8")
    print(f"Wrote {args.out_json}")
    print(f"Wrote {args.out_tex}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
