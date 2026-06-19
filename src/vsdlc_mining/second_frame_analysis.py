"""Contamination analysis for the AI-topic second discovery frame."""

from __future__ import annotations

import csv
import math
import random
from pathlib import Path
from typing import Any

from vsdlc_mining.config import ORIGINAL_FRAME_NON_TARGET_REFERENCE
from vsdlc_mining.decontamination_schema import PRIMARY_LABELS
from vsdlc_mining.rq2_contamination import NON_TARGET_LABELS, wilson_ci

BINARY_TARGET_LABEL = "CONVENTIONAL_SOFTWARE"


def _read_annotation_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _normalize_label(label: str) -> str:
    return label.strip().upper()


def _count_labels(labels: list[str]) -> dict[str, int]:
    counts = {label: 0 for label in PRIMARY_LABELS if label != "TIE"}
    for label in labels:
        if label in counts:
            counts[label] += 1
    return counts


def _difference_ci_normal(
    p1: float,
    n1: int,
    p2: float,
    n2: int,
    *,
    z: float = 1.96,
) -> tuple[float, float]:
    if n1 <= 0 or n2 <= 0:
        return (0.0, 0.0)
    diff = p2 - p1
    se = math.sqrt((p1 * (1 - p1) / n1) + (p2 * (1 - p2) / n2))
    margin = z * se
    return (round(100.0 * (diff - margin), 1), round(100.0 * (diff + margin), 1))


def _bootstrap_difference_ci(
    second_labels: list[str],
    *,
    original_rate: float,
    n_bootstrap: int = 10_000,
    seed: int = 42,
) -> tuple[float, float]:
    if not second_labels:
        return (0.0, 0.0)
    n = len(second_labels)
    rng = random.Random(seed)
    samples: list[float] = []
    for _ in range(n_bootstrap):
        draw = [second_labels[rng.randrange(n)] for _ in range(n)]
        non_target = sum(1 for label in draw if label in NON_TARGET_LABELS)
        samples.append((non_target / n) - original_rate)
    samples.sort()
    lower = samples[int(0.025 * len(samples))]
    upper = samples[int(0.975 * len(samples)) - 1]
    return (round(100.0 * lower, 1), round(100.0 * upper, 1))


def analyze_second_frame_contamination(
    *,
    annotation_path: Path,
    sample_path: Path | None = None,
    n_bootstrap: int = 10_000,
    seed: int = 42,
) -> dict[str, Any]:
    rows = _read_annotation_rows(annotation_path)
    labels = [
        _normalize_label(row.get("primary_label", ""))
        for row in rows
        if _normalize_label(row.get("primary_label", "")) in PRIMARY_LABELS
    ]
    if not labels:
        raise ValueError(
            "No valid primary_label values found. Complete second_frame_annotation_blank.csv first."
        )

    counts = _count_labels(labels)
    n = len(labels)
    target_count = counts.get(BINARY_TARGET_LABEL, 0)
    non_target_count = sum(counts.get(label, 0) for label in NON_TARGET_LABELS)
    non_target_rate = non_target_count / n

    three_class_ci = {
        label: {
            "count": counts.get(label, 0),
            "rate_pct": round(100.0 * counts.get(label, 0) / n, 1),
            "wilson_ci_pct": list(wilson_ci(counts.get(label, 0), n)),
        }
        for label in ("CONVENTIONAL_SOFTWARE", "AI_PRODUCT", "EXCLUDE")
    }

    binary = {
        "target_count": target_count,
        "non_target_count": non_target_count,
        "n": n,
        "non_target_rate": non_target_rate,
        "non_target_rate_pct": round(100.0 * non_target_rate, 1),
        "wilson_ci_pct": list(wilson_ci(non_target_count, n)),
        "target_rate_pct": round(100.0 * target_count / n, 1),
        "target_wilson_ci_pct": list(wilson_ci(target_count, n)),
    }

    original = dict(ORIGINAL_FRAME_NON_TARGET_REFERENCE)
    original_rate = float(original["non_target_rate"])
    difference_pct = round(100.0 * (non_target_rate - original_rate), 1)

    comparison = {
        "original_frame": original,
        "second_frame_non_target_rate_pct": binary["non_target_rate_pct"],
        "second_frame_wilson_ci_pct": binary["wilson_ci_pct"],
        "absolute_difference_pct_points": difference_pct,
        "difference_normal_approx_ci_pct": list(
            _difference_ci_normal(
                original_rate,
                int(original["consensus_n"]),
                non_target_rate,
                n,
            )
        ),
        "difference_bootstrap_ci_pct": list(
            _bootstrap_difference_ci(
                labels,
                original_rate=original_rate,
                n_bootstrap=n_bootstrap,
                seed=seed,
            )
        ),
        "interpretation_scope": (
            "Minimal robustness extension comparing discovery mechanisms within audited frames; "
            "not validation of the instruction-artifact frame and not GitHub-wide generalization."
        ),
    }

    overlap_summary: dict[str, Any] = {}
    if sample_path is not None and sample_path.exists():
        with sample_path.open(encoding="utf-8", newline="") as handle:
            sample_rows = list(csv.DictReader(handle))
        overlap_summary = {
            "sample_file": str(sample_path),
            "sample_size": len(sample_rows),
            "instruction_frame_overlap_count": sum(
                1 for row in sample_rows if row.get("instruction_frame_overlap", "").strip().lower() == "true"
            ),
        }

    return {
        "schema_version": "0.2",
        "annotation_file": str(annotation_path),
        "annotated_repositories": n,
        "three_class_counts": counts,
        "three_class_rates": three_class_ci,
        "binary_target_vs_non_target": binary,
        "frame_comparison": comparison,
        "overlap_summary": overlap_summary,
        "method": {
            "ci_level": 0.95,
            "wilson_z": 1.96,
            "bootstrap_replicates": n_bootstrap,
            "bootstrap_seed": seed,
        },
    }


def render_manuscript_table(results: dict[str, Any]) -> str:
    original = results["frame_comparison"]["original_frame"]
    binary = results["binary_target_vs_non_target"]
    diff = results["frame_comparison"]
    lines = [
        "# Second-frame robustness comparison",
        "",
        "| Frame | $n$ | NON_TARGET % | 95% Wilson CI |",
        "|---|---:|---:|---|",
        (
            f"| Instruction-artifact (frozen pilot consensus) | {original['consensus_n']} | "
            f"{original['non_target_rate_pct']:.1f} | "
            f"{original['wilson_ci_pct'][0]:.1f}–{original['wilson_ci_pct'][1]:.1f} |"
        ),
        (
            f"| AI-topic/metadata (second frame) | {binary['n']} | "
            f"{binary['non_target_rate_pct']:.1f} | "
            f"{binary['wilson_ci_pct'][0]:.1f}–{binary['wilson_ci_pct'][1]:.1f} |"
        ),
        "",
        f"Absolute difference (second − instruction frame): **{diff['absolute_difference_pct_points']:+.1f}** "
        f"percentage points "
        f"(bootstrap 95% CI: {diff['difference_bootstrap_ci_pct'][0]:+.1f} to "
        f"{diff['difference_bootstrap_ci_pct'][1]:+.1f}).",
        "",
    ]
    if results.get("overlap_summary"):
        overlap = results["overlap_summary"].get("instruction_frame_overlap_count", 0)
        sample_n = results["overlap_summary"].get("sample_size", 0)
        lines.append(
            f"Instruction-frame overlap in second-frame sample: {overlap}/{sample_n} repositories."
        )
        lines.append("")
    return "\n".join(lines)


def render_manuscript_paragraph(results: dict[str, Any]) -> str:
    original = results["frame_comparison"]["original_frame"]
    binary = results["binary_target_vs_non_target"]
    diff = results["frame_comparison"]
    overlap = results.get("overlap_summary", {})
    overlap_text = ""
    if overlap:
        overlap_text = (
            f" The second-frame sample included {overlap.get('instruction_frame_overlap_count', 0)} "
            f"repositories already present in the instruction-artifact eligible set."
        )
    return (
        "As a minimal robustness extension, we replicated the contamination audit on an independent "
        "AI-topic/metadata discovery frame (GitHub repository search on topic predicates such as "
        "`topic:llm` and `topic:ai-agent`) with the same eligibility filters where feasible. "
        f"Under annotation consensus on $n={binary['n']}$ second-frame repositories, "
        f"{binary['non_target_rate_pct']:.1f}% "
        f"[{binary['wilson_ci_pct'][0]:.1f}, {binary['wilson_ci_pct'][1]:.1f}] were NON_TARGET "
        "relative to the conventional-application target, compared with "
        f"{original['non_target_rate_pct']:.1f}% "
        f"[{original['wilson_ci_pct'][0]:.1f}, {original['wilson_ci_pct'][1]:.1f}] in the frozen "
        f"instruction-artifact pilot ($n={original['consensus_n']}$). "
        f"The absolute difference was {diff['absolute_difference_pct_points']:+.1f} percentage points "
        f"(bootstrap 95% CI: {diff['difference_bootstrap_ci_pct'][0]:+.1f} to "
        f"{diff['difference_bootstrap_ci_pct'][1]:+.1f})."
        f"{overlap_text} "
        "This comparison tests sensitivity to discovery mechanism within audited frames; it does not "
        "validate the instruction-artifact frame or estimate GitHub-wide prevalence."
    )
