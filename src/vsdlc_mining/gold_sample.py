"""Stratified gold-sample construction for decontamination validation."""

from __future__ import annotations

import csv
import random
from collections import defaultdict
from pathlib import Path

from vsdlc_mining.metadata import (
    format_ci_evidence,
    format_instruction_artifacts,
    format_release_evidence,
    sample_stratum,
)
from vsdlc_mining.models import EligibleRepo

# Matches data/processed/repo_classifications_template.csv (do not duplicate that file).
CLASSIFICATION_TEMPLATE_FIELDS = [
    "schema_version",
    "repo_full_name",
    "repo_url",
    "stars",
    "primary_language",
    "github_description",
    "github_topics",
    "detected_instruction_artifacts",
    "ci_evidence",
    "release_evidence",
    "primary_label",
    "secondary_tags",
    "confidence",
    "evidence_notes",
    "annotator_id",
    "annotation_round",
    "adjudication_status",
    "adjudicated_label",
    "adjudication_notes",
]

# Sampling metadata appended for decontamination stratification (not in the blank template).
SAMPLING_METADATA_FIELDS = [
    "agent_product_flag",
    "sample_stratum",
]

GOLD_SAMPLE_FIELDS = [
    *CLASSIFICATION_TEMPLATE_FIELDS[:10],
    *SAMPLING_METADATA_FIELDS,
    *CLASSIFICATION_TEMPLATE_FIELDS[10:],
]

DEFAULT_SAMPLE_SIZE = 120
SCHEMA_VERSION = "0.2"


def eligible_to_gold_row(repo: EligibleRepo) -> dict[str, str]:
    topics = repo.github_topics or []
    return {
        "schema_version": SCHEMA_VERSION,
        "repo_full_name": repo.full_name,
        "repo_url": repo.repository_url,
        "stars": str(repo.stars),
        "primary_language": repo.primary_language or "",
        "github_description": repo.github_description or "",
        "github_topics": "|".join(topics),
        "detected_instruction_artifacts": format_instruction_artifacts(
            queries=repo.queries,
            matched_paths=repo.matched_paths,
        ),
        "ci_evidence": format_ci_evidence(repo.evidence),
        "release_evidence": format_release_evidence(repo.evidence),
        "agent_product_flag": str(repo.agent_product_flag).lower(),
        "sample_stratum": sample_stratum(
            stars=repo.stars,
            queries=repo.queries,
            agent_product_flag=repo.agent_product_flag,
        ),
        "primary_label": "",
        "secondary_tags": "",
        "confidence": "",
        "evidence_notes": "",
        "annotator_id": "",
        "annotation_round": "",
        "adjudication_status": "",
        "adjudicated_label": "",
        "adjudication_notes": "",
    }


def stratified_sample(
    repos: list[EligibleRepo],
    *,
    sample_size: int = DEFAULT_SAMPLE_SIZE,
    seed: int = 42,
) -> list[EligibleRepo]:
    """Draw a stratified sample; return all repos if fewer than sample_size."""
    if len(repos) <= sample_size:
        return sorted(repos, key=lambda repo: repo.full_name)

    rng = random.Random(seed)
    strata: dict[str, list[EligibleRepo]] = defaultdict(list)
    for repo in repos:
        strata[
            sample_stratum(
                stars=repo.stars,
                queries=repo.queries,
                agent_product_flag=repo.agent_product_flag,
            )
        ].append(repo)

    total = len(repos)
    allocations: dict[str, int] = {}
    for key in sorted(strata):
        allocations[key] = max(1, round(len(strata[key]) / total * sample_size))
        allocations[key] = min(allocations[key], len(strata[key]))

    assigned = sum(allocations.values())
    while assigned > sample_size:
        reducible = [key for key in allocations if allocations[key] > 1]
        if not reducible:
            break
        key = max(reducible, key=lambda item: allocations[item])
        allocations[key] -= 1
        assigned -= 1

    while assigned < sample_size:
        expandable = [key for key in allocations if allocations[key] < len(strata[key])]
        if not expandable:
            break
        key = max(expandable, key=lambda item: len(strata[item]) - allocations[item])
        allocations[key] += 1
        assigned += 1

    selected: list[EligibleRepo] = []
    for key, count in allocations.items():
        bucket = sorted(strata[key], key=lambda repo: repo.full_name)
        selected.extend(rng.sample(bucket, k=count))

    return sorted(selected, key=lambda repo: repo.full_name)


def write_gold_sample_csv(path: Path, repos: list[EligibleRepo]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = [eligible_to_gold_row(repo) for repo in repos]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=GOLD_SAMPLE_FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)
