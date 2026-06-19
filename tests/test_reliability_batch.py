from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path

from vsdlc_mining.gold_sample import GOLD_SAMPLE_FIELDS
from vsdlc_mining.models import EligibleRepo, EvidenceFlags
from vsdlc_mining.reliability_batch import (
    DEFAULT_RELIABILITY_SEED,
    balanced_stratified_sample,
    write_reliability_batch_csv,
)


def _eligible(
    full_name: str,
    *,
    stars: int,
    query: str,
) -> EligibleRepo:
    return EligibleRepo(
        full_name=full_name,
        repository_url=f"https://github.com/{full_name}",
        stars=stars,
        pushed_at=datetime(2025, 1, 1),
        default_branch="main",
        queries=[query],
        matched_paths=[f"path/{query}"],
        evidence=EvidenceFlags(has_ci_evidence=True, ci_paths=[".github/workflows"]),
    )


def test_balanced_sample_size_and_seed_reproducibility() -> None:
    repos = [
        _eligible(f"org/r{i}", stars=10 + (i % 4) * 80, query=f"q{i % 5}")
        for i in range(120)
    ]
    first = balanced_stratified_sample(repos, sample_size=50, seed=DEFAULT_RELIABILITY_SEED)
    second = balanced_stratified_sample(repos, sample_size=50, seed=DEFAULT_RELIABILITY_SEED)
    assert len(first) == 50
    assert [repo.full_name for repo in first] == [repo.full_name for repo in second]


def test_balanced_sample_includes_all_when_below_target() -> None:
    repos = [_eligible(f"org/r{i}", stars=20 + i, query="AGENTS.md") for i in range(12)]
    sample = balanced_stratified_sample(repos, sample_size=50, seed=1)
    assert len(sample) == 12


def test_balanced_sample_spreads_star_buckets(tmp_path: Path) -> None:
    repos: list[EligibleRepo] = []
    for stars in (15, 60, 250, 1500):
        for index in range(20):
            repos.append(
                _eligible(
                    f"bucket{stars}/repo{index}",
                    stars=stars,
                    query="AGENTS.md",
                )
            )
    sample = balanced_stratified_sample(repos, sample_size=50, seed=7)
    buckets = {15: "10-49", 60: "50-199", 250: "200-999", 1500: "1000+"}
    counts = {label: 0 for label in buckets.values()}
    for repo in sample:
        counts[buckets[repo.stars]] += 1
    assert all(count >= 10 for count in counts.values())


def test_write_reliability_batch_csv_has_annotation_fields(tmp_path: Path) -> None:
    repo = _eligible("acme/service", stars=120, query="AGENTS.md")
    output = tmp_path / "batch.csv"
    count = write_reliability_batch_csv(output, [repo])
    assert count == 1
    with output.open(encoding="utf-8", newline="") as handle:
        row = next(csv.DictReader(handle))
    assert row["primary_label"] == ""
    assert row["secondary_tags"] == ""
    assert row["confidence"] == ""
    assert "stars:50-199" in row["sample_stratum"]
    assert "artifact:AGENTS.md" in row["sample_stratum"]
    assert set(row.keys()) == set(GOLD_SAMPLE_FIELDS)
