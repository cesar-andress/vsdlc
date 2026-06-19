"""Sampling and annotation worksheets for the AI-topic second discovery frame."""

from __future__ import annotations

import csv
import random
from pathlib import Path
from typing import Any

from vsdlc_mining.config import SECOND_FRAME_SAMPLE_SEED, SECOND_FRAME_SAMPLE_SIZE
from vsdlc_mining.gold_sample import SCHEMA_VERSION
from vsdlc_mining.metadata import format_ci_evidence, format_release_evidence
from vsdlc_mining.models import EligibleRepo

SECOND_FRAME_SAMPLE_FIELDS = [
    "repo_full_name",
    "repo_url",
    "stars",
    "pushed_at",
    "primary_language",
    "github_description",
    "github_topics",
    "discovery_predicate",
    "ci_evidence",
    "release_evidence",
    "agent_product_flag",
    "instruction_frame_overlap",
    "sample_seed",
]

SECOND_FRAME_ANNOTATION_FIELDS = [
    "schema_version",
    "repo_full_name",
    "repo_url",
    "github_description",
    "github_topics",
    "primary_language",
    "stars",
    "pushed_at",
    "discovery_predicate",
    "ci_evidence",
    "release_evidence",
    "primary_label",
    "confidence",
    "evidence_notes",
    "deciding_step",
]


def primary_discovery_predicate(repo: EligibleRepo) -> str:
    return repo.queries[0] if repo.queries else ""


def eligible_to_second_frame_row(
    repo: EligibleRepo,
    *,
    instruction_frame_overlap: bool,
    sample_seed: int,
) -> dict[str, str]:
    topics = repo.github_topics or []
    return {
        "repo_full_name": repo.full_name,
        "repo_url": repo.repository_url,
        "stars": str(repo.stars),
        "pushed_at": repo.pushed_at.isoformat(),
        "primary_language": repo.primary_language or "",
        "github_description": repo.github_description or "",
        "github_topics": "|".join(topics),
        "discovery_predicate": primary_discovery_predicate(repo),
        "ci_evidence": format_ci_evidence(repo.evidence),
        "release_evidence": format_release_evidence(repo.evidence),
        "agent_product_flag": str(repo.agent_product_flag).lower(),
        "instruction_frame_overlap": str(instruction_frame_overlap).lower(),
        "sample_seed": str(sample_seed),
    }


def eligible_to_annotation_blank_row(repo: EligibleRepo) -> dict[str, str]:
    topics = repo.github_topics or []
    return {
        "schema_version": SCHEMA_VERSION,
        "repo_full_name": repo.full_name,
        "repo_url": repo.repository_url,
        "github_description": repo.github_description or "",
        "github_topics": "|".join(topics),
        "primary_language": repo.primary_language or "",
        "stars": str(repo.stars),
        "pushed_at": repo.pushed_at.isoformat(),
        "discovery_predicate": primary_discovery_predicate(repo),
        "ci_evidence": format_ci_evidence(repo.evidence),
        "release_evidence": format_release_evidence(repo.evidence),
        "primary_label": "",
        "confidence": "",
        "evidence_notes": "",
        "deciding_step": "",
    }


def sample_second_frame_repositories(
    eligible: list[EligibleRepo],
    *,
    instruction_frame_names: set[str],
    sample_size: int = SECOND_FRAME_SAMPLE_SIZE,
    seed: int = SECOND_FRAME_SAMPLE_SEED,
    prefer_non_overlap: bool = True,
) -> tuple[list[EligibleRepo], dict[str, Any]]:
    """Sample repositories for annotation, preferring repos outside the instruction frame."""
    rng = random.Random(seed)
    pool = sorted(eligible, key=lambda repo: repo.full_name)

    non_overlap = [repo for repo in pool if repo.full_name not in instruction_frame_names]
    overlap = [repo for repo in pool if repo.full_name in instruction_frame_names]

    selected: list[EligibleRepo] = []
    if prefer_non_overlap:
        ranked_non_overlap = sorted(non_overlap, key=lambda repo: (-repo.stars, repo.full_name))
        ranked_overlap = sorted(overlap, key=lambda repo: (-repo.stars, repo.full_name))
        for repo in ranked_non_overlap:
            if len(selected) >= sample_size:
                break
            selected.append(repo)
        if len(selected) < sample_size:
            for repo in ranked_overlap:
                if len(selected) >= sample_size:
                    break
                selected.append(repo)
    else:
        ranked = sorted(pool, key=lambda repo: (rng.random(), repo.full_name))
        selected = ranked[:sample_size]

    selected = sorted(selected, key=lambda repo: repo.full_name)
    overlap_in_sample = sum(1 for repo in selected if repo.full_name in instruction_frame_names)

    summary = {
        "eligible_pool_size": len(pool),
        "non_overlap_pool_size": len(non_overlap),
        "overlap_pool_size": len(overlap),
        "requested_sample_size": sample_size,
        "selected_sample_size": len(selected),
        "overlap_in_sample": overlap_in_sample,
        "non_overlap_in_sample": len(selected) - overlap_in_sample,
        "sample_seed": seed,
        "prefer_non_overlap": prefer_non_overlap,
        "used_all_eligible": len(selected) < sample_size,
    }
    return selected, summary


def write_second_frame_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in fieldnames} for row in rows)
    return len(rows)
