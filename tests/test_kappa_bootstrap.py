from __future__ import annotations

import pytest

from vsdlc_mining.annotation_agreement import cohens_kappa
from vsdlc_mining.decontamination_schema import PRIMARY_LABELS
from vsdlc_mining.kappa_bootstrap import (
    agreement_rate,
    apply_pair_transform,
    bootstrap_paired_metrics,
    filter_pairs,
    percentile_ci,
)


def test_agreement_rate_perfect() -> None:
    labels = ["A", "B", "C"]
    assert agreement_rate(labels, labels) == pytest.approx(1.0)


def test_filter_pairs_keeps_matching_predicate() -> None:
    left = ["AI_PRODUCT", "EXCLUDE", "CONVENTIONAL_SOFTWARE"]
    right = ["CONVENTIONAL_SOFTWARE", "EXCLUDE", "AI_PRODUCT"]
    filtered_left, filtered_right = filter_pairs(
        left,
        right,
        lambda a, b: a != "EXCLUDE" and b != "EXCLUDE",
    )
    assert filtered_left == ["AI_PRODUCT", "CONVENTIONAL_SOFTWARE"]
    assert filtered_right == ["CONVENTIONAL_SOFTWARE", "AI_PRODUCT"]


def test_apply_pair_transform_collapses_exclude_binary() -> None:
    left = ["EXCLUDE", "AI_PRODUCT", "CONVENTIONAL_SOFTWARE"]
    right = ["CONVENTIONAL_SOFTWARE", "EXCLUDE", "CONVENTIONAL_SOFTWARE"]

    def collapse(a: str, b: str) -> tuple[str, str] | None:
        return (
            "EXCLUDE" if a == "EXCLUDE" else "NON_EXCLUDE",
            "EXCLUDE" if b == "EXCLUDE" else "NON_EXCLUDE",
        )

    collapsed_left, collapsed_right = apply_pair_transform(left, right, collapse)
    assert collapsed_left == ["EXCLUDE", "NON_EXCLUDE", "NON_EXCLUDE"]
    assert collapsed_right == ["NON_EXCLUDE", "EXCLUDE", "NON_EXCLUDE"]


def test_percentile_ci_bounds() -> None:
    lower, upper = percentile_ci(list(range(101)))
    assert lower == pytest.approx(2.0)
    assert upper == pytest.approx(97.0)


def test_bootstrap_paired_metrics_recovers_point_estimate() -> None:
    labels = list(PRIMARY_LABELS) * 20
    metrics = bootstrap_paired_metrics(
        labels,
        labels,
        PRIMARY_LABELS,
        n_bootstrap=500,
        seed=7,
    )
    assert metrics["kappa"] == pytest.approx(1.0)
    assert metrics["agreement"] == pytest.approx(1.0)
    assert metrics["kappa_ci_lower"] == pytest.approx(1.0)
    assert metrics["kappa_ci_upper"] == pytest.approx(1.0)


def test_bootstrap_paired_metrics_matches_cohens_kappa() -> None:
    left = ["AI_PRODUCT", "CONVENTIONAL_SOFTWARE", "EXCLUDE", "AI_PRODUCT"]
    right = ["AI_PRODUCT", "AI_PRODUCT", "EXCLUDE", "CONVENTIONAL_SOFTWARE"]
    metrics = bootstrap_paired_metrics(
        left,
        right,
        PRIMARY_LABELS,
        n_bootstrap=1000,
        seed=3,
    )
    assert metrics["kappa"] == pytest.approx(cohens_kappa(left, right, PRIMARY_LABELS))
    assert metrics["kappa_ci_lower"] <= metrics["kappa"] <= metrics["kappa_ci_upper"]
