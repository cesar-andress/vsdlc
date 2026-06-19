"""Validation and evaluation for a second independent functional-evidence inspector."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Any

from vsdlc_mining.annotation_agreement import (
    cohens_kappa,
    confusion_matrix,
    per_class_metrics,
)
from vsdlc_mining.decontamination_schema import (
    BINARY_DECONTAMINATION_LABELS,
    PRIMARY_LABELS,
)
from vsdlc_mining.inspection_sample import (
    INSPECTOR2_EVIDENCE_SOURCE_TOKENS,
    MIN_INSPECTION_EVIDENCE_SOURCES,
    SECOND_INSPECTOR_BLANK_FIELDS,
    SECOND_INSPECTOR_BLANK_INSPECTION_FIELDS,
)
from vsdlc_mining.inspection_validation import (
    BINARY_AI_CONVENTIONAL_LABELS,
    BINARY_EXCLUDE_LABELS,
    compute_inspection_validation,
)
from vsdlc_mining.kappa_bootstrap import (
    apply_pair_transform,
    bootstrap_paired_metrics,
    filter_pairs,
)

AI_CONV_LABELS = frozenset({"AI_PRODUCT", "CONVENTIONAL_SOFTWARE"})
COMPARISON_NAMES = (
    "metadata_consensus_vs_inspector1",
    "metadata_consensus_vs_inspector2",
    "inspector1_vs_inspector2",
)


def _read_csv_rows(path: Path) -> dict[str, dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    keyed: dict[str, dict[str, str]] = {}
    for row in rows:
        repo = row.get("repo_full_name", "").strip()
        if repo:
            keyed[repo] = row
    return keyed


def _normalize_label(label: str) -> str:
    return label.strip().upper()


def _parse_inspector2_evidence_sources(value: str) -> set[str]:
    tokens: set[str] = set()
    for raw in value.replace("|", ",").split(","):
        token = raw.strip().lower()
        if token in INSPECTOR2_EVIDENCE_SOURCE_TOKENS:
            tokens.add(token)
    return tokens


def _collapse_exclude_binary(label: str) -> str | None:
    normalized = _normalize_label(label)
    if normalized == "EXCLUDE":
        return "EXCLUDE"
    if normalized in AI_CONV_LABELS:
        return "NON_EXCLUDE"
    return None


def _collapse_target_binary(label: str) -> str | None:
    normalized = _normalize_label(label)
    if normalized == "CONVENTIONAL_SOFTWARE":
        return "target_population"
    if normalized in {"AI_PRODUCT", "EXCLUDE"}:
        return "non_target"
    return None


def _collapse_exclude_pair(left: str, right: str) -> tuple[str, str] | None:
    collapsed_left = _collapse_exclude_binary(left)
    collapsed_right = _collapse_exclude_binary(right)
    if collapsed_left is None or collapsed_right is None:
        return None
    return collapsed_left, collapsed_right


def _collapse_target_pair(left: str, right: str) -> tuple[str, str] | None:
    collapsed_left = _collapse_target_binary(left)
    collapsed_right = _collapse_target_binary(right)
    if collapsed_left is None or collapsed_right is None:
        return None
    return collapsed_left, collapsed_right


def _paired_labels(
    reference: dict[str, dict[str, str]],
    left_rows: dict[str, dict[str, str]],
    right_rows: dict[str, dict[str, str]],
    *,
    left_field: str,
    right_field: str,
    expected_repos: list[str] | None = None,
) -> tuple[list[str], list[str], list[str]]:
    repos = expected_repos or sorted(set(reference) & set(left_rows) & set(right_rows))
    left_labels: list[str] = []
    right_labels: list[str] = []
    used_repos: list[str] = []

    for repo in repos:
        left = _normalize_label(left_rows[repo].get(left_field, ""))
        right = _normalize_label(right_rows[repo].get(right_field, ""))
        if left not in PRIMARY_LABELS or right not in PRIMARY_LABELS:
            continue
        left_labels.append(left)
        right_labels.append(right)
        used_repos.append(repo)

    return left_labels, right_labels, used_repos


def validate_second_inspection_completed(
    blank_path: Path,
    completed_path: Path,
) -> dict[str, Any]:
    """Validate the second-inspector worksheet before evaluation."""
    blank = _read_csv_rows(blank_path)
    completed = _read_csv_rows(completed_path)

    expected_repos = sorted(blank)
    errors: list[str] = []
    warnings: list[dict[str, str | int]] = []

    if len(expected_repos) != 50:
        errors.append(f"Expected 50 repositories in blank worksheet; found {len(expected_repos)}.")

    missing_repos = [repo for repo in expected_repos if repo not in completed]
    extra_repos = sorted(set(completed) - set(expected_repos))
    if missing_repos:
        errors.append(f"Missing completed rows for {len(missing_repos)} repositories.")
    if extra_repos:
        errors.append(f"Completed worksheet contains {len(extra_repos)} unexpected repositories.")

    for repo in expected_repos:
        if repo not in completed:
            continue
        row = completed[repo]
        label = _normalize_label(row.get("inspector2_label", ""))
        if label not in PRIMARY_LABELS:
            errors.append(f"{repo}: inspector2_label must be one of {', '.join(PRIMARY_LABELS)}.")
        functional_note = row.get("inspector2_functional_note", "").strip()
        if not functional_note:
            errors.append(f"{repo}: inspector2_functional_note is required.")
        evidence_sources = _parse_inspector2_evidence_sources(row.get("inspector2_evidence_sources", ""))
        if len(evidence_sources) < MIN_INSPECTION_EVIDENCE_SOURCES:
            warnings.append(
                {
                    "repo_full_name": repo,
                    "warning_type": "insufficient_evidence_sources",
                    "message": (
                        f"{repo}: only {len(evidence_sources)} evidence-source token(s) recorded; "
                        f"inspect at least {MIN_INSPECTION_EVIDENCE_SOURCES} sources when available."
                    ),
                    "evidence_source_count": len(evidence_sources),
                }
            )
        forbidden_fields = (
            "majority_label",
            "claude_label",
            "human1_label",
            "human2_label",
            "inspection_label",
            "inspector1_label",
        )
        for field in forbidden_fields:
            if row.get(field, "").strip():
                errors.append(f"{repo}: completed worksheet must not include prior label field {field}.")

    return {
        "schema_version": "0.2",
        "blank_file": str(blank_path),
        "completed_file": str(completed_path),
        "expected_repositories": len(expected_repos),
        "completed_repositories": len(completed),
        "valid": not errors,
        "errors": errors,
        "warnings": warnings,
        "warning_count": len(warnings),
    }


def _classify_disagreement(row_label: str, col_label: str) -> str:
    labels = {row_label, col_label}
    if labels == {"AI_PRODUCT", "CONVENTIONAL_SOFTWARE"}:
        return "ai_product_vs_conventional"
    if labels == {"EXCLUDE", "CONVENTIONAL_SOFTWARE"}:
        return "exclude_vs_conventional"
    if labels == {"EXCLUDE", "AI_PRODUCT"}:
        return "exclude_vs_ai_product"
    return "other"


def _disagreement_decomposition(
    labels_a: list[str],
    labels_b: list[str],
    *,
    comparison: str,
) -> dict[str, Any]:
    matrix = confusion_matrix(labels_a, labels_b, PRIMARY_LABELS)
    disagreements = [
        {
            "row_label": row_label,
            "col_label": col_label,
            "count": count,
            "pattern": _classify_disagreement(row_label, col_label),
        }
        for row_label, row in matrix.items()
        for col_label, count in row.items()
        if row_label != col_label and count
    ]
    total_disagreements = sum(item["count"] for item in disagreements)

    patterns: dict[str, int] = {
        "exclude_vs_conventional": 0,
        "exclude_vs_ai_product": 0,
        "ai_product_vs_conventional": 0,
        "other": 0,
    }
    for item in disagreements:
        patterns[item["pattern"]] += item["count"]

    def pct(count: int) -> float:
        return round(100 * count / total_disagreements, 1) if total_disagreements else 0.0

    return {
        "comparison": comparison,
        "paired_repositories": len(labels_a),
        "total_disagreements": total_disagreements,
        "disagreement_rate": round(total_disagreements / len(labels_a), 3) if labels_a else 0.0,
        "patterns": {
            key: {"count": count, "percent_of_disagreements": pct(count)}
            for key, count in patterns.items()
        },
        "exclude_involving": {
            "count": patterns["exclude_vs_conventional"] + patterns["exclude_vs_ai_product"],
            "percent_of_disagreements": pct(
                patterns["exclude_vs_conventional"] + patterns["exclude_vs_ai_product"]
            ),
        },
        "confusion_matrix": matrix,
        "off_diagonal_cells": disagreements,
    }


def _comparison_metrics(
    labels_a: list[str],
    labels_b: list[str],
    *,
    comparison: str,
    n_bootstrap: int,
    seed: int,
) -> dict[str, Any]:
    agreement_count = sum(1 for left, right in zip(labels_a, labels_b) if left == right)
    paired = len(labels_a)

    three_class = bootstrap_paired_metrics(
        labels_a,
        labels_b,
        PRIMARY_LABELS,
        n_bootstrap=n_bootstrap,
        seed=seed,
    )

    ai_conv_a, ai_conv_b = filter_pairs(
        labels_a,
        labels_b,
        lambda left, right: left in AI_CONV_LABELS and right in AI_CONV_LABELS,
    )
    ai_conv = bootstrap_paired_metrics(
        ai_conv_a,
        ai_conv_b,
        BINARY_AI_CONVENTIONAL_LABELS,
        n_bootstrap=n_bootstrap,
        seed=seed + 1,
    )

    exclude_a, exclude_b = apply_pair_transform(labels_a, labels_b, _collapse_exclude_pair)
    exclude_binary = bootstrap_paired_metrics(
        exclude_a,
        exclude_b,
        BINARY_EXCLUDE_LABELS,
        n_bootstrap=n_bootstrap,
        seed=seed + 2,
    )

    target_a, target_b = apply_pair_transform(labels_a, labels_b, _collapse_target_pair)
    target_binary = bootstrap_paired_metrics(
        target_a,
        target_b,
        BINARY_DECONTAMINATION_LABELS,
        n_bootstrap=n_bootstrap,
        seed=seed + 3,
    )

    return {
        "comparison": comparison,
        "paired_repositories": paired,
        "agreement_count": agreement_count,
        "agreement_rate": agreement_count / paired if paired else None,
        "cohens_kappa": cohens_kappa(labels_a, labels_b, PRIMARY_LABELS),
        "three_class": three_class,
        "target_vs_non_target": target_binary,
        "ai_product_vs_conventional_excluding_exclude": ai_conv,
        "exclude_vs_non_exclude": exclude_binary,
        "confusion_matrix": confusion_matrix(labels_a, labels_b, PRIMARY_LABELS),
        "target_vs_non_target_confusion_matrix": confusion_matrix(
            target_a,
            target_b,
            BINARY_DECONTAMINATION_LABELS,
        ),
        "per_class_metrics": per_class_metrics(labels_b, labels_a, PRIMARY_LABELS),
        "disagreement_decomposition": _disagreement_decomposition(
            labels_a,
            labels_b,
            comparison=comparison,
        ),
    }


def _confusion_rows(comparison: str, matrix: dict[str, dict[str, int]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for row_label, row in matrix.items():
        for col_label, count in row.items():
            rows.append(
                {
                    "comparison": comparison,
                    "row_label": row_label,
                    "col_label": col_label,
                    "count": count,
                }
            )
    return rows


def _format_percent(value: float | None) -> str:
    if value is None:
        return "NA"
    return f"{100 * value:.1f}\\%"


def _format_kappa(value: float | None) -> str:
    if value is None:
        return "NA"
    return f"{value:.3f}"


def _format_ci(lower: float | None, upper: float | None) -> str:
    if lower is None or upper is None:
        return "NA"
    return f"[{lower:.3f}, {upper:.3f}]"


def render_manuscript_table_rq4(results: dict[str, Any]) -> str:
    """Render a LaTeX table snippet for RQ4 dual-inspector concordance."""
    lines = [
        "% Auto-generated by evaluate_second_inspection.py",
        "\\begin{table}[t]",
        "  \\centering",
        "  \\footnotesize",
        "  \\caption{Functional-evidence proxy audit with two independent inspectors ($n{=}50$). "
        "Bracketed values are 95\\% bootstrap CIs.}",
        "  \\label{tab:rq4-second-inspector}",
        "  \\begin{tabular*}{\\columnwidth}{@{\\extracolsep{\\fill}}lrrl@{}}",
        "    \\toprule",
        "    Comparison & $n$ & Agree. & $\\kappa$ \\\\",
        "    \\midrule",
    ]

    for key, label in (
        ("metadata_consensus_vs_inspector1", "Metadata consensus vs.\\ inspector~1"),
        ("metadata_consensus_vs_inspector2", "Metadata consensus vs.\\ inspector~2"),
        ("inspector1_vs_inspector2", "Inspector~1 vs.\\ inspector~2"),
    ):
        block = results["comparisons"][key]["three_class"]
        agreement_ci = _format_ci(block["agreement_ci_lower"], block["agreement_ci_upper"])
        kappa_ci = _format_ci(block["kappa_ci_lower"], block["kappa_ci_upper"])
        lines.extend(
            [
                f"    {label} & {block['n']} & "
                f"{_format_percent(block['agreement'])} & {_format_kappa(block['kappa'])} \\\\",
                "    \\multicolumn{4}{@{}l@{}}"
                "{\\hfill {\\scriptsize " + agreement_ci + "}\\quad " + kappa_ci + "}} \\\\",
            ]
        )

    lines.extend(
        [
            "    \\bottomrule",
            "  \\end{tabular*}",
            "\\end{table}",
            "",
        ]
    )
    return "\n".join(lines)


def compute_second_inspection_evaluation(
    *,
    reference_path: Path,
    inspector1_completed_path: Path,
    inspector2_completed_path: Path,
    blank_path: Path,
    n_bootstrap: int = 10_000,
    seed: int = 42,
) -> dict[str, Any]:
    validation = validate_second_inspection_completed(blank_path, inspector2_completed_path)
    if not validation["valid"]:
        raise ValueError(
            "Second-inspector worksheet failed validation: " + "; ".join(validation["errors"])
        )

    reference = _read_csv_rows(reference_path)
    inspector1 = _read_csv_rows(inspector1_completed_path)
    inspector2 = _read_csv_rows(inspector2_completed_path)
    expected_repos = sorted(_read_csv_rows(blank_path))

    inspector1_as_labels = {
        repo: {"inspector1_label": row.get("inspection_label", "")} for repo, row in inspector1.items()
    }

    pairs = {
        "metadata_consensus_vs_inspector1": (
            reference,
            reference,
            inspector1_as_labels,
            "majority_label",
            "inspector1_label",
        ),
        "metadata_consensus_vs_inspector2": (
            reference,
            reference,
            inspector2,
            "majority_label",
            "inspector2_label",
        ),
        "inspector1_vs_inspector2": (
            reference,
            inspector1_as_labels,
            inspector2,
            "inspector1_label",
            "inspector2_label",
        ),
    }

    comparisons: dict[str, Any] = {}
    confusion_rows: list[dict[str, Any]] = []
    disagreement_stats: dict[str, Any] = {}

    for index, (name, (ref, left_rows, right_rows, left_field, right_field)) in enumerate(pairs.items()):
        labels_a, labels_b, repos = _paired_labels(
            ref,
            left_rows,
            right_rows,
            left_field=left_field,
            right_field=right_field,
            expected_repos=expected_repos,
        )
        if len(repos) != 50:
            raise ValueError(f"{name}: expected 50 paired repositories; found {len(repos)}.")

        comparisons[name] = _comparison_metrics(
            labels_a,
            labels_b,
            comparison=name,
            n_bootstrap=n_bootstrap,
            seed=seed + index * 10,
        )
        confusion_rows.extend(_confusion_rows(name, comparisons[name]["confusion_matrix"]))
        confusion_rows.extend(
            _confusion_rows(
                f"{name}_target_vs_non_target",
                comparisons[name]["target_vs_non_target_confusion_matrix"],
            )
        )
        disagreement_stats[name] = comparisons[name]["disagreement_decomposition"]

    inspector1_validation = compute_inspection_validation(reference_path, inspector1_completed_path)

    return {
        "schema_version": "0.2",
        "method": {
            "ci_level": 0.95,
            "bootstrap_replicates": n_bootstrap,
            "seed": seed,
            "estimator": "percentile bootstrap on paired repository labels",
        },
        "reference_file": str(reference_path),
        "inspector1_completed_file": str(inspector1_completed_path),
        "inspector2_completed_file": str(inspector2_completed_path),
        "blank_file": str(blank_path),
        "paired_repositories": 50,
        "validation": validation,
        "metadata_consensus_vs_inspector1_legacy": inspector1_validation,
        "comparisons": comparisons,
        "confusion_matrices": confusion_rows,
        "disagreement_stats": disagreement_stats,
        "required_completed_fields": list(SECOND_INSPECTOR_BLANK_INSPECTION_FIELDS),
    }
