from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path

import pytest

from vsdlc_mining.annotation_agreement import cohens_kappa, compute_annotation_agreement
from vsdlc_mining.decontamination_schema import PRIMARY_LABELS
from vsdlc_mining.gold_sample import (
    CLASSIFICATION_TEMPLATE_FIELDS,
    GOLD_SAMPLE_FIELDS,
    stratified_sample,
    write_gold_sample_csv,
)
from vsdlc_mining.metadata import extract_github_metadata, sample_stratum, star_bucket
from vsdlc_mining.models import EligibleRepo, EvidenceFlags


def _eligible(
    full_name: str,
    *,
    stars: int = 100,
    queries: list[str] | None = None,
    agent_product_flag: bool = False,
) -> EligibleRepo:
    return EligibleRepo(
        full_name=full_name,
        repository_url=f"https://github.com/{full_name}",
        stars=stars,
        pushed_at=datetime(2025, 1, 1),
        default_branch="main",
        queries=queries or ["AGENTS.md"],
        matched_paths=["AGENTS.md"],
        agent_product_flag=agent_product_flag,
        evidence=EvidenceFlags(has_ci_evidence=True, ci_paths=[".github/workflows/ci.yml"]),
    )


def test_extract_github_metadata_preserves_missing_values() -> None:
    metadata = extract_github_metadata({"topics": None})
    assert metadata["github_description"] is None
    assert metadata["github_topics"] == []
    assert metadata["primary_language"] is None


def test_star_bucket_boundaries() -> None:
    assert star_bucket(10) == "10-49"
    assert star_bucket(49) == "10-49"
    assert star_bucket(50) == "50-199"
    assert star_bucket(1000) == "1000+"


def test_stratified_sample_includes_all_when_below_target() -> None:
    repos = [_eligible(f"org/repo{i}", stars=10 + i) for i in range(5)]
    sample = stratified_sample(repos, sample_size=120, seed=1)
    assert len(sample) == 5


def test_stratified_sample_respects_target_size() -> None:
    repos = [
        _eligible(
            f"org/repo{i}",
            stars=10 + (i % 4) * 60,
            queries=[f"query-{i % 3}"],
            agent_product_flag=bool(i % 2),
        )
        for i in range(200)
    ]
    sample = stratified_sample(repos, sample_size=120, seed=7)
    assert len(sample) == 120
    assert len({repo.full_name for repo in sample}) == 120


def test_write_gold_sample_csv_leaves_annotation_fields_empty(tmp_path: Path) -> None:
    repo = _eligible(
        "acme/service",
        stars=120,
        queries=["AGENTS.md", "path:.cursor/rules"],
        agent_product_flag=True,
    )
    output = tmp_path / "gold.csv"
    count = write_gold_sample_csv(output, [repo])
    assert count == 1
    with output.open(encoding="utf-8", newline="") as handle:
        row = next(csv.DictReader(handle))
    assert row["primary_label"] == ""
    assert row["secondary_tags"] == ""
    assert row["confidence"] == ""
    assert row["annotator_id"] == ""
    assert row["adjudicated_label"] == ""
    assert row["schema_version"] == "0.2"
    assert set(row.keys()) == set(GOLD_SAMPLE_FIELDS)
    assert set(CLASSIFICATION_TEMPLATE_FIELDS).issubset(set(row.keys()))


def test_cohens_kappa_perfect_agreement_three_class() -> None:
    labels = list(PRIMARY_LABELS)
    kappa = cohens_kappa(labels, labels, PRIMARY_LABELS)
    assert kappa == pytest.approx(1.0)


def test_compute_annotation_agreement_reports_disagreements(tmp_path: Path) -> None:
    fields = [
        "repo_full_name",
        "primary_label",
        "confidence",
        "adjudicated_label",
    ]
    rows = [
        {
            "repo_full_name": "org/one",
            "primary_label": "AI_PRODUCT",
            "confidence": "high",
            "adjudicated_label": "",
        },
        {
            "repo_full_name": "org/two",
            "primary_label": "CONVENTIONAL_SOFTWARE",
            "confidence": "high",
            "adjudicated_label": "",
        },
        {
            "repo_full_name": "org/three",
            "primary_label": "EXCLUDE",
            "confidence": "medium",
            "adjudicated_label": "",
        },
    ]
    a_path = tmp_path / "a.csv"
    b_path = tmp_path / "b.csv"
    for path in (a_path, b_path):
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)

    rows_b = [
        rows[0],
        {**rows[1], "primary_label": "AI_PRODUCT"},
        rows[2],
    ]
    with b_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows_b)

    result = compute_annotation_agreement(a_path, b_path)
    assert result["paired_repositories"] == 3
    assert len(result["disagreements"]) == 1
    assert result["disagreements"][0]["repo_full_name"] == "org/two"
    assert result["primary_three_class"]["kappa"] is not None
    assert result["binary_decontamination"]["kappa"] is not None


def test_compute_annotation_agreement_legacy_label_warns(tmp_path: Path) -> None:
    fields = ["repo_full_name", "label", "confidence"]
    rows = [
        {"repo_full_name": "org/one", "label": "CONVENTIONAL_SOFTWARE", "confidence": "high"},
    ]
    a_path = tmp_path / "a.csv"
    b_path = tmp_path / "b.csv"
    for path in (a_path, b_path):
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)

    with pytest.warns(UserWarning, match="legacy 'label' column"):
        result = compute_annotation_agreement(a_path, b_path)

    assert result["compatibility_warnings"]
    assert result["paired_repositories"] == 1
