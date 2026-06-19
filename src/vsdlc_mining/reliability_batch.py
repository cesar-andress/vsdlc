"""Balanced stratified sampling for inter-rater reliability annotation batches."""

from __future__ import annotations

import csv
import random
from collections import Counter, defaultdict
from pathlib import Path

from vsdlc_mining.gold_sample import GOLD_SAMPLE_FIELDS, eligible_to_gold_row
from vsdlc_mining.metadata import primary_artifact_type, star_bucket
from vsdlc_mining.models import EligibleRepo

DEFAULT_RELIABILITY_BATCH_SIZE = 50
DEFAULT_RELIABILITY_SEED = 42


def reliability_stratum(*, stars: int, queries: list[str]) -> str:
    return f"stars:{star_bucket(stars)}|artifact:{primary_artifact_type(queries)}"


def _balance_within_bucket(
    repos: list[EligibleRepo],
    target: int,
    rng: random.Random,
) -> list[EligibleRepo]:
    if target <= 0 or not repos:
        return []
    if target >= len(repos):
        return sorted(repos, key=lambda repo: repo.full_name)

    by_artifact: dict[str, list[EligibleRepo]] = defaultdict(list)
    for repo in repos:
        by_artifact[primary_artifact_type(repo.queries)].append(repo)

    artifact_keys = sorted(by_artifact)
    pools = {
        key: sorted(by_artifact[key], key=lambda repo: repo.full_name)
        for key in artifact_keys
    }
    indices = dict.fromkeys(artifact_keys, 0)
    picked: list[EligibleRepo] = []
    picked_names: set[str] = set()

    while len(picked) < target:
        progressed = False
        for key in artifact_keys:
            pool = pools[key]
            index = indices[key]
            while index < len(pool) and pool[index].full_name in picked_names:
                index += 1
            indices[key] = index
            if index < len(pool):
                repo = pool[index]
                picked.append(repo)
                picked_names.add(repo.full_name)
                indices[key] = index + 1
                progressed = True
                if len(picked) >= target:
                    break
        if not progressed:
            break

    if len(picked) < target:
        remaining = [repo for repo in repos if repo.full_name not in picked_names]
        extra = rng.sample(remaining, k=min(target - len(picked), len(remaining)))
        picked.extend(extra)

    return picked[:target]


def balanced_stratified_sample(
    repos: list[EligibleRepo],
    *,
    sample_size: int = DEFAULT_RELIABILITY_BATCH_SIZE,
    seed: int = DEFAULT_RELIABILITY_SEED,
) -> list[EligibleRepo]:
    """Sample with marginal balance across star buckets and artifact types."""
    if len(repos) <= sample_size:
        return sorted(repos, key=lambda repo: repo.full_name)

    rng = random.Random(seed)
    by_star: dict[str, list[EligibleRepo]] = defaultdict(list)
    for repo in repos:
        by_star[star_bucket(repo.stars)].append(repo)

    star_keys = sorted(by_star)
    base = sample_size // len(star_keys)
    remainder = sample_size % len(star_keys)

    selected: list[EligibleRepo] = []
    selected_names: set[str] = set()

    for index, star_key in enumerate(star_keys):
        bucket_target = base + (1 if index < remainder else 0)
        bucket_target = min(bucket_target, len(by_star[star_key]))
        bucket_pick = _balance_within_bucket(by_star[star_key], bucket_target, rng)
        for repo in bucket_pick:
            if repo.full_name not in selected_names:
                selected.append(repo)
                selected_names.add(repo.full_name)

    if len(selected) < sample_size:
        pool = [repo for repo in repos if repo.full_name not in selected_names]
        need = sample_size - len(selected)
        if pool:
            extra = rng.sample(pool, k=min(need, len(pool)))
            selected.extend(extra)

    if len(selected) > sample_size:
        selected = rng.sample(selected, k=sample_size)

    return sorted(selected, key=lambda repo: repo.full_name)


def star_bucket_distribution(repos: list[EligibleRepo]) -> dict[str, int]:
    return dict(Counter(star_bucket(repo.stars) for repo in repos))


def artifact_type_distribution(repos: list[EligibleRepo]) -> dict[str, int]:
    return dict(Counter(primary_artifact_type(repo.queries) for repo in repos))


def write_reliability_batch_csv(path: Path, repos: list[EligibleRepo]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    for repo in repos:
        row = eligible_to_gold_row(repo)
        row["sample_stratum"] = reliability_stratum(stars=repo.stars, queries=repo.queries)
        rows.append(row)

    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=GOLD_SAMPLE_FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)
