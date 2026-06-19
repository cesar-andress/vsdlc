"""Bootstrap confidence intervals for Cohen's kappa on paired categorical labels."""

from __future__ import annotations

import random
from typing import Callable

from vsdlc_mining.annotation_agreement import cohens_kappa

PairFilter = Callable[[str, str], bool]
LabelTransform = Callable[[str, str], tuple[str, str] | None]


def agreement_rate(labels_a: list[str], labels_b: list[str]) -> float | None:
    if not labels_a or len(labels_a) != len(labels_b):
        return None
    return sum(1 for a, b in zip(labels_a, labels_b) if a == b) / len(labels_a)


def apply_pair_transform(
    labels_a: list[str],
    labels_b: list[str],
    transform: LabelTransform,
) -> tuple[list[str], list[str]]:
    transformed_a: list[str] = []
    transformed_b: list[str] = []
    for left, right in zip(labels_a, labels_b):
        pair = transform(left, right)
        if pair is None:
            continue
        transformed_a.append(pair[0])
        transformed_b.append(pair[1])
    return transformed_a, transformed_b


def filter_pairs(
    labels_a: list[str],
    labels_b: list[str],
    predicate: PairFilter,
) -> tuple[list[str], list[str]]:
    filtered_a: list[str] = []
    filtered_b: list[str] = []
    for left, right in zip(labels_a, labels_b):
        if predicate(left, right):
            filtered_a.append(left)
            filtered_b.append(right)
    return filtered_a, filtered_b


def percentile_ci(values: list[float], alpha: float = 0.05) -> tuple[float, float]:
    if not values:
        raise ValueError("Cannot compute percentile CI from an empty bootstrap sample.")
    sorted_values = sorted(values)
    lower_index = int((alpha / 2) * len(sorted_values))
    upper_index = int((1 - alpha / 2) * len(sorted_values)) - 1
    lower_index = max(0, min(lower_index, len(sorted_values) - 1))
    upper_index = max(0, min(upper_index, len(sorted_values) - 1))
    return sorted_values[lower_index], sorted_values[upper_index]


def bootstrap_paired_metrics(
    labels_a: list[str],
    labels_b: list[str],
    categories: tuple[str, ...],
    *,
    n_bootstrap: int = 10_000,
    seed: int = 42,
    alpha: float = 0.05,
    min_pairs: int = 2,
) -> dict[str, float | int | None]:
    if len(labels_a) != len(labels_b):
        raise ValueError("Paired label lists must have equal length.")
    n = len(labels_a)
    if n < min_pairs:
        return {
            "n": n,
            "agreement": None,
            "agreement_ci_lower": None,
            "agreement_ci_upper": None,
            "kappa": None,
            "kappa_ci_lower": None,
            "kappa_ci_upper": None,
            "bootstrap_replicates": 0,
            "bootstrap_valid_replicates": 0,
        }

    point_kappa = cohens_kappa(labels_a, labels_b, categories)
    point_agreement = agreement_rate(labels_a, labels_b)

    rng = random.Random(seed)
    kappa_samples: list[float] = []
    agreement_samples: list[float] = []
    for _ in range(n_bootstrap):
        indices = [rng.randrange(n) for _ in range(n)]
        sample_a = [labels_a[index] for index in indices]
        sample_b = [labels_b[index] for index in indices]
        if len(sample_a) < min_pairs:
            continue
        sample_kappa = cohens_kappa(sample_a, sample_b, categories)
        sample_agreement = agreement_rate(sample_a, sample_b)
        if sample_kappa is None or sample_agreement is None:
            continue
        kappa_samples.append(sample_kappa)
        agreement_samples.append(sample_agreement)

    if not kappa_samples:
        return {
            "n": n,
            "agreement": point_agreement,
            "agreement_ci_lower": None,
            "agreement_ci_upper": None,
            "kappa": point_kappa,
            "kappa_ci_lower": None,
            "kappa_ci_upper": None,
            "bootstrap_replicates": n_bootstrap,
            "bootstrap_valid_replicates": 0,
        }

    kappa_lower, kappa_upper = percentile_ci(kappa_samples, alpha=alpha)
    agreement_lower, agreement_upper = percentile_ci(agreement_samples, alpha=alpha)
    return {
        "n": n,
        "agreement": point_agreement,
        "agreement_ci_lower": agreement_lower,
        "agreement_ci_upper": agreement_upper,
        "kappa": point_kappa,
        "kappa_ci_lower": kappa_lower,
        "kappa_ci_upper": kappa_upper,
        "bootstrap_replicates": n_bootstrap,
        "bootstrap_valid_replicates": len(kappa_samples),
    }
