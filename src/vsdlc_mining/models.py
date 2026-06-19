"""Typed data models for mining pipeline artifacts."""

from __future__ import annotations

from datetime import datetime, timezone

from pydantic import BaseModel, Field, model_validator


class RepoCandidate(BaseModel):
    """A repository discovered via GitHub code search (Phase 1)."""

    query: str
    full_name: str
    repository_url: str
    stars: int
    pushed_at: datetime
    default_branch: str
    matched_path: str
    license: str | None = None
    queries: list[str] = Field(default_factory=list)
    matched_paths: list[str] = Field(default_factory=list)
    github_description: str | None = None
    github_topics: list[str] = Field(default_factory=list)
    primary_language: str | None = None

    @model_validator(mode="after")
    def _default_query_lists(self) -> RepoCandidate:
        if not self.queries:
            self.queries = [self.query]
        if not self.matched_paths:
            self.matched_paths = [self.matched_path]
        return self


class EvidenceFlags(BaseModel):
    """Release, CI, and test evidence detected without cloning."""

    has_ci_evidence: bool = False
    has_test_evidence: bool = False
    has_release_tag_evidence: bool = False
    ci_paths: list[str] = Field(default_factory=list)
    test_paths: list[str] = Field(default_factory=list)
    release_tag_count: int = 0
    release_count: int = 0


class EligibleRepo(BaseModel):
    """Repository passing Phase 2 inclusion criteria."""

    full_name: str
    repository_url: str
    stars: int
    pushed_at: datetime
    default_branch: str
    license: str | None = None
    queries: list[str] = Field(default_factory=list)
    matched_paths: list[str] = Field(default_factory=list)
    agent_product_flag: bool = False
    evidence: EvidenceFlags = Field(default_factory=EvidenceFlags)
    github_description: str | None = None
    github_topics: list[str] = Field(default_factory=list)
    primary_language: str | None = None


class ExcludedRepo(BaseModel):
    """Repository excluded during Phase 2 filtering."""

    full_name: str
    repository_url: str
    stars: int
    pushed_at: datetime | None = None
    exclusion_reasons: list[str] = Field(default_factory=list)
    agent_product_flag: bool = False
    queries: list[str] = Field(default_factory=list)
    matched_paths: list[str] = Field(default_factory=list)


class FilterSummary(BaseModel):
    """Aggregate counts from Phase 2 filtering."""

    input_candidates: int = 0
    eligible_count: int = 0
    excluded_count: int = 0
    agent_product_flagged: int = 0
    exclusion_reason_counts: dict[str, int] = Field(default_factory=dict)
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
