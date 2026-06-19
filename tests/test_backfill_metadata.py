from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path
from unittest.mock import MagicMock

import pytest

from vsdlc_mining.backfill_metadata import (
    backfill_eligible_repos,
    enrich_gold_csv_rows,
    merge_metadata,
    needs_metadata_backfill,
)
from vsdlc_mining.gold_sample import eligible_to_gold_row, write_gold_sample_csv
from vsdlc_mining.models import EligibleRepo, EvidenceFlags


def _eligible(
    full_name: str = "acme/service",
    *,
    description: str | None = None,
    topics: list[str] | None = None,
    language: str | None = None,
) -> EligibleRepo:
    return EligibleRepo(
        full_name=full_name,
        repository_url=f"https://github.com/{full_name}",
        stars=120,
        pushed_at=datetime(2025, 6, 1),
        default_branch="main",
        queries=["AGENTS.md"],
        matched_paths=["AGENTS.md"],
        agent_product_flag=True,
        evidence=EvidenceFlags(has_ci_evidence=True, ci_paths=[".github/workflows"]),
        github_description=description,
        github_topics=topics or [],
        primary_language=language,
    )


def test_needs_metadata_backfill_when_any_field_missing() -> None:
    assert needs_metadata_backfill(_eligible()) is True
    assert (
        needs_metadata_backfill(
            _eligible(description="App", topics=["python"], language="Go"),
        )
        is False
    )


def test_merge_metadata_preserves_existing_fields() -> None:
    repo = _eligible(description="Existing description", topics=["ai"], language="Python")
    merged = merge_metadata(
        repo,
        {
            "github_description": "New description",
            "github_topics": ["agent", "tooling"],
            "primary_language": "Go",
        },
    )
    assert merged.github_description == "Existing description"
    assert merged.github_topics == ["ai"]
    assert merged.primary_language == "Python"
    assert merged.stars == 120
    assert merged.agent_product_flag is True
    assert merged.evidence.has_ci_evidence is True


def test_merge_metadata_fills_missing_fields() -> None:
    repo = _eligible()
    merged = merge_metadata(
        repo,
        {
            "github_description": "A service",
            "github_topics": ["python", "agents"],
            "primary_language": "Python",
        },
    )
    assert merged.github_description == "A service"
    assert merged.github_topics == ["python", "agents"]
    assert merged.primary_language == "Python"


def test_backfill_eligible_repos_skips_complete_and_fills_missing() -> None:
    complete = _eligible(description="Done", topics=["x"], language="Rust")
    missing = _eligible(full_name="acme/other")
    client = MagicMock()
    client.get_repository.return_value = {
        "description": "Other app",
        "topics": ["go"],
        "language": "Go",
    }

    enriched, stats = backfill_eligible_repos(client, [complete, missing])

    assert stats.total_repos == 2
    assert stats.skipped_complete == 1
    assert stats.api_fetches == 1
    assert stats.successfully_enriched == 1
    assert enriched[0].github_description == "Done"
    assert enriched[1].github_description == "Other app"
    assert enriched[1].github_topics == ["go"]
    assert enriched[1].primary_language == "Go"
    client.get_repository.assert_called_once_with("acme/other")


def test_backfill_handles_missing_repo_gracefully() -> None:
    from vsdlc_mining.github_client import GitHubClientError

    repo = _eligible(full_name="missing/repo")
    client = MagicMock()
    client.get_repository.side_effect = GitHubClientError("GitHub API error 404")

    enriched, stats = backfill_eligible_repos(client, [repo])

    assert len(enriched) == 1
    assert enriched[0].github_description is None
    assert stats.failed_fetches == ["missing/repo"]


def test_enrich_gold_csv_leaves_annotation_fields_unchanged(tmp_path: Path) -> None:
    repo = _eligible()
    output = tmp_path / "gold.csv"
    write_gold_sample_csv(output, [repo])

    with output.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    rows[0]["primary_label"] = "CONVENTIONAL_SOFTWARE"
    rows[0]["confidence"] = "high"
    rows[0]["evidence_notes"] = "README shows product app"
    rows[0]["annotator_id"] = "annotator-a"

    lookup = {
        "acme/service": {
            "github_description": "Service description",
            "github_topics": "python|agents",
            "primary_language": "Python",
        }
    }
    enriched = enrich_gold_csv_rows(rows, lookup)[0]

    assert enriched["github_description"] == "Service description"
    assert enriched["github_topics"] == "python|agents"
    assert enriched["primary_language"] == "Python"
    assert enriched["primary_label"] == "CONVENTIONAL_SOFTWARE"
    assert enriched["confidence"] == "high"
    assert enriched["evidence_notes"] == "README shows product app"
    assert enriched["annotator_id"] == "annotator-a"
    assert enriched["adjudicated_label"] == ""


def test_enrich_gold_csv_does_not_overwrite_existing_metadata() -> None:
    rows = [
        {
            "repo_full_name": "acme/service",
            "github_description": "Keep me",
            "github_topics": "rust",
            "primary_language": "Rust",
            "primary_label": "",
            "confidence": "",
        }
    ]
    lookup = {
        "acme/service": {
            "github_description": "Replace me",
            "github_topics": "python",
            "primary_language": "Python",
        }
    }
    enriched = enrich_gold_csv_rows(rows, lookup)[0]
    assert enriched["github_description"] == "Keep me"
    assert enriched["github_topics"] == "rust"
    assert enriched["primary_language"] == "Rust"
