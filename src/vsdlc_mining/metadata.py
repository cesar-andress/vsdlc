"""GitHub repository metadata helpers for annotation and gold sampling."""

from __future__ import annotations

from typing import Any

from vsdlc_mining.models import EvidenceFlags


def extract_github_metadata(repo_payload: dict[str, Any]) -> dict[str, Any]:
    """Extract description, topics, and primary language from a GitHub repo payload."""
    topics = repo_payload.get("topics") or []
    if not isinstance(topics, list):
        topics = []
    return {
        "github_description": repo_payload.get("description"),
        "github_topics": [str(topic) for topic in topics],
        "primary_language": repo_payload.get("language"),
    }


def star_bucket(stars: int) -> str:
    if stars < 50:
        return "10-49"
    if stars < 200:
        return "50-199"
    if stars < 1000:
        return "200-999"
    return "1000+"


def primary_artifact_type(queries: list[str]) -> str:
    if not queries:
        return "unknown"
    return sorted(queries)[0]


def sample_stratum(*, stars: int, queries: list[str], agent_product_flag: bool) -> str:
    return (
        f"stars:{star_bucket(stars)}|"
        f"artifact:{primary_artifact_type(queries)}|"
        f"agent_flag:{str(agent_product_flag).lower()}"
    )


def format_ci_evidence(evidence: EvidenceFlags) -> str:
    if not evidence.has_ci_evidence and not evidence.has_test_evidence:
        return ""
    parts: list[str] = []
    if evidence.has_ci_evidence:
        parts.extend(evidence.ci_paths or ["ci_detected"])
    if evidence.has_test_evidence:
        parts.extend(evidence.test_paths or ["tests_detected"])
    return "; ".join(parts)


def format_release_evidence(evidence: EvidenceFlags) -> str:
    if not evidence.has_release_tag_evidence:
        return ""
    return f"tags={evidence.release_tag_count}; releases={evidence.release_count}"


def format_instruction_artifacts(*, queries: list[str], matched_paths: list[str]) -> str:
    import json

    return json.dumps(
        {"queries": queries, "matched_paths": matched_paths},
        sort_keys=True,
    )
