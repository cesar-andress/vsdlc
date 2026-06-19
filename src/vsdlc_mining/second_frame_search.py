"""Discover repositories for the AI-topic second discovery frame."""

from __future__ import annotations

import json
import logging
import time
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

from vsdlc_mining.config import (
    MAX_SEARCH_RESULTS,
    MIN_PUSHED_AT,
    MIN_STARS,
    SEARCH_QUERY_DELAY_SECONDS,
    SECOND_FRAME_TOPIC_QUERIES,
)
from vsdlc_mining.github_client import GitHubClient, GitHubClientError, GitHubRateLimitExceeded
from vsdlc_mining.metadata import extract_github_metadata
from vsdlc_mining.models import RepoCandidate
from vsdlc_mining.seed_search import (
    _deserialize_aggregate,
    _enrich_candidates,
    _license_spdx,
    _merge_candidate,
    _parse_datetime,
    _serialize_aggregate,
    load_checkpoint,
    save_checkpoint,
)
from vsdlc_mining.utils import read_json, read_jsonl, salvage_json, write_json, write_jsonl

logger = logging.getLogger(__name__)


def build_topic_repository_query(topic_predicate: str) -> str:
    """Compose a reproducible GitHub repository-search query."""
    return (
        f"{topic_predicate} stars:>={MIN_STARS} "
        f"pushed:>={MIN_PUSHED_AT.date().isoformat()} fork:false archived:false"
    )


def select_topic_queries(query_text: str | None) -> list[tuple[str, str]]:
    if not query_text:
        return list(SECOND_FRAME_TOPIC_QUERIES)
    needle = query_text.casefold()
    matched = [
        (predicate, label)
        for predicate, label in SECOND_FRAME_TOPIC_QUERIES
        if needle in label.casefold() or needle in predicate.casefold()
    ]
    if not matched:
        raise ValueError(f"No second-frame topic query matches {query_text!r}")
    return matched


def run_second_frame_search(
    client: GitHubClient,
    *,
    resume: bool = False,
    fresh_start: bool = False,
    checkpoint_path: Path,
    output_path: Path,
    query_filter: str | None = None,
    max_pages: int | None = None,
) -> list[RepoCandidate]:
    """Execute topic repository searches with checkpointing and incremental JSONL output."""
    aggregate: dict[str, dict[str, Any]] = {}
    completed_queries: list[str] = []
    enriched_full_names: set[str] = set()
    search_completed = False
    query_hit_counts: dict[str, int] = defaultdict(int)
    topic_queries = select_topic_queries(query_filter)
    max_results = MAX_SEARCH_RESULTS
    if max_pages is not None:
        max_results = min(max_results, max_pages * client.per_page)

    if fresh_start and checkpoint_path.exists():
        checkpoint_path.unlink()
        logger.info("Fresh start: removed checkpoint at %s", checkpoint_path)

    if resume and not fresh_start:
        checkpoint = load_checkpoint(checkpoint_path)
        if checkpoint:
            aggregate = _deserialize_aggregate(checkpoint.get("aggregate", {}))
            completed_queries = list(checkpoint.get("completed_queries", []))
            enriched_full_names = set(checkpoint.get("enriched_full_names", []))
            search_completed = bool(checkpoint.get("search_completed", False))
            logger.info(
                "Resuming second-frame search: %d queries done, %d repos, %d enriched.",
                len(completed_queries),
                len(aggregate),
                len(enriched_full_names),
            )
        else:
            logger.warning("No checkpoint found at %s; starting fresh.", checkpoint_path)

    if not search_completed:
        pending = [
            (predicate, label)
            for predicate, label in topic_queries
            if label not in completed_queries
        ]
        for index, (predicate, label) in enumerate(pending):
            if index > 0:
                time.sleep(SEARCH_QUERY_DELAY_SECONDS)

            api_query = build_topic_repository_query(predicate)
            logger.info("Searching repositories: %s (%s)", label, api_query)
            try:
                items = client.search_repositories(
                    api_query,
                    max_results=max_results,
                    max_pages=max_pages,
                )
            except GitHubRateLimitExceeded:
                raise
            except Exception as exc:  # noqa: BLE001
                logger.error("Topic query failed for %s: %s", label, exc)
                continue

            query_hit_counts[label] = len(items)
            logger.info("Topic query %s returned %d hits", label, len(items))

            for item in items:
                full_name = item.get("full_name")
                if not full_name:
                    continue
                repository_url = item.get("html_url") or f"https://github.com/{full_name}"
                _merge_candidate(
                    aggregate,
                    full_name=full_name,
                    query_label=label,
                    matched_path=label,
                    repository_url=repository_url,
                )

            completed_queries.append(label)
            save_checkpoint(
                checkpoint_path,
                completed_queries=completed_queries,
                aggregate=aggregate,
                search_completed=False,
                enriched_full_names=sorted(enriched_full_names),
            )

        search_completed = True
        save_checkpoint(
            checkpoint_path,
            completed_queries=completed_queries,
            aggregate=aggregate,
            search_completed=True,
            enriched_full_names=sorted(enriched_full_names),
        )

    logger.info("Unique repositories after topic deduplication: %d", len(aggregate))

    if fresh_start or not resume or not output_path.exists():
        write_jsonl(output_path, [])

    new_candidates = _enrich_candidates(
        client,
        aggregate,
        enriched_full_names=enriched_full_names,
        output_path=output_path,
        checkpoint_path=checkpoint_path,
        completed_queries=completed_queries,
        search_completed=search_completed,
    )

    if enriched_full_names:
        all_candidates = read_jsonl(output_path, RepoCandidate) if output_path.exists() else []
    else:
        all_candidates = new_candidates

    logger.info("Enriched second-frame candidates: %d", len(all_candidates))
    for label, count in sorted(query_hit_counts.items()):
        logger.debug("Raw topic hits for %s: %d", label, count)
    return all_candidates
