from __future__ import annotations

from datetime import datetime
from unittest.mock import MagicMock

import pytest

from vsdlc_mining.github_client import (
    GitHubClient,
    GitHubRateLimitExceeded,
    _is_rate_limited,
    _is_secondary_rate_limited,
)
from vsdlc_mining.models import EligibleRepo, ExcludedRepo, RepoCandidate
from vsdlc_mining.repo_filter import (
    _keyword_exclusion_reasons,
    _meets_activity_thresholds,
    _structural_exclusion_reasons,
    detect_agent_product_flag,
    detect_evidence,
    filter_repositories,
    load_filter_progress,
)
from vsdlc_mining.seed_search import (
    _merge_candidate,
    load_checkpoint,
    repair_checkpoint,
    run_seed_search,
    save_checkpoint,
)
from vsdlc_mining.utils import read_json, read_jsonl, salvage_json, write_json, write_jsonl


def test_repo_candidate_defaults_query_lists() -> None:
    candidate = RepoCandidate(
        query="AGENTS.md",
        full_name="org/repo",
        repository_url="https://github.com/org/repo",
        stars=12,
        pushed_at=datetime(2025, 1, 1),
        default_branch="main",
        matched_path="AGENTS.md",
    )
    assert candidate.queries == ["AGENTS.md"]
    assert candidate.matched_paths == ["AGENTS.md"]


def test_merge_candidate_deduplicates_repo() -> None:
    store: dict[str, dict] = {}
    _merge_candidate(
        store,
        full_name="org/repo",
        query_label="AGENTS.md",
        matched_path="AGENTS.md",
        repository_url="https://github.com/org/repo",
    )
    _merge_candidate(
        store,
        full_name="org/repo",
        query_label="CLAUDE.md",
        matched_path="CLAUDE.md",
        repository_url="https://github.com/org/repo",
    )
    assert len(store) == 1
    assert store["org/repo"]["queries"] == {"AGENTS.md", "CLAUDE.md"}


def test_structural_exclusion_reasons() -> None:
    payload = {"fork": True, "archived": False, "mirror_url": None, "is_template": False}
    assert _structural_exclusion_reasons(payload) == ["fork"]


def test_keyword_exclusion_skipped_for_agent_product() -> None:
    reasons = _keyword_exclusion_reasons(
        full_name="acme/awesome-demo",
        description="demo project",
        topics=["demo"],
        agent_product_flag=True,
    )
    assert reasons == []


def test_keyword_exclusion_detects_tutorial() -> None:
    reasons = _keyword_exclusion_reasons(
        full_name="acme/react-tutorial",
        description="learning react",
        topics=[],
        agent_product_flag=False,
    )
    assert reasons == ["keyword:tutorial"]


def test_activity_threshold_failures() -> None:
    reasons = _meets_activity_thresholds(stars=3, pushed_at=datetime(2023, 1, 1))
    assert "stars_below_10" in reasons
    assert "pushed_before_2024-06-01" in reasons


def test_detect_agent_product_flag() -> None:
    assert detect_agent_product_flag(
        full_name="acme/cursor-rules",
        description="Prompt templates for Cursor",
        topics=["ai"],
        matched_paths=[".cursor/rules/agent.mdc"],
    )


def test_detect_evidence_from_root_entries() -> None:
    client = MagicMock()
    client.list_repo_root_entries.return_value = [
        {"name": ".github", "path": ".github"},
        {"name": "tests", "path": "tests"},
        {"name": "pytest.ini", "path": "pytest.ini"},
    ]
    client.path_exists.side_effect = lambda _repo, path: path == ".github/workflows"
    client.list_tags.return_value = [{"name": "v1.0.0"}]
    client.list_releases.return_value = []

    evidence = detect_evidence(client, "org/repo")
    assert evidence.has_ci_evidence is True
    assert evidence.has_test_evidence is True
    assert evidence.has_release_tag_evidence is True


def test_filter_repositories_eligible_path() -> None:
    client = MagicMock()
    client.get_repository.return_value = {
        "stargazers_count": 50,
        "default_branch": "main",
        "description": "Application service",
        "topics": ["python"],
        "fork": False,
        "archived": False,
        "mirror_url": None,
        "is_template": False,
    }
    client.list_repo_root_entries.return_value = [
        {"name": ".github", "path": ".github"},
        {"name": "tests", "path": "tests"},
    ]
    client.path_exists.return_value = True
    client.list_tags.return_value = [{"name": "v1.0.0"}]
    client.list_releases.return_value = []

    candidates = [
        RepoCandidate(
            query="AGENTS.md",
            full_name="org/service",
            repository_url="https://github.com/org/service",
            stars=50,
            pushed_at=datetime(2025, 3, 1),
            default_branch="main",
            matched_path="AGENTS.md",
            queries=["AGENTS.md"],
            matched_paths=["AGENTS.md"],
        )
    ]

    eligible, excluded, summary = filter_repositories(client, candidates)
    assert len(eligible) == 1
    assert len(excluded) == 0
    assert summary.eligible_count == 1


def test_filter_repositories_writes_incrementally(tmp_path) -> None:
    client = MagicMock()
    client.get_repository.return_value = {
        "stargazers_count": 3,
        "default_branch": "main",
        "description": "tutorial repo",
        "topics": [],
        "fork": False,
        "archived": False,
        "mirror_url": None,
        "is_template": False,
    }
    client.list_repo_root_entries.return_value = []
    client.path_exists.return_value = False
    client.list_tags.return_value = []
    client.list_releases.return_value = []

    candidates = [
        RepoCandidate(
            query="AGENTS.md",
            full_name="org/tutorial",
            repository_url="https://github.com/org/tutorial",
            stars=3,
            pushed_at=datetime(2025, 3, 1),
            default_branch="main",
            matched_path="AGENTS.md",
            queries=["AGENTS.md"],
            matched_paths=["AGENTS.md"],
        )
    ]
    eligible_path = tmp_path / "eligible.jsonl"
    excluded_path = tmp_path / "excluded.jsonl"
    summary_path = tmp_path / "summary.json"

    eligible, excluded, summary = filter_repositories(
        client,
        candidates,
        eligible_output_path=eligible_path,
        excluded_output_path=excluded_path,
        summary_output_path=summary_path,
    )

    assert len(eligible) == 0
    assert len(excluded) == 1
    assert eligible_path.exists()
    assert eligible_path.read_text(encoding="utf-8") == ""
    assert excluded_path.read_text(encoding="utf-8").strip()
    assert summary.excluded_count == 1
    saved = read_json(summary_path)
    assert saved["excluded_count"] == 1
    assert saved["eligible_count"] == 0


def test_filter_repositories_resume_skips_processed(tmp_path) -> None:
    client = MagicMock()
    client.get_repository.return_value = {
        "stargazers_count": 50,
        "default_branch": "main",
        "description": "Application service",
        "topics": ["python"],
        "fork": False,
        "archived": False,
        "mirror_url": None,
        "is_template": False,
    }
    client.list_repo_root_entries.return_value = [
        {"name": ".github", "path": ".github"},
        {"name": "tests", "path": "tests"},
    ]
    client.path_exists.return_value = True
    client.list_tags.return_value = [{"name": "v1.0.0"}]
    client.list_releases.return_value = []

    candidates = [
        RepoCandidate(
            query="AGENTS.md",
            full_name="org/done",
            repository_url="https://github.com/org/done",
            stars=50,
            pushed_at=datetime(2025, 3, 1),
            default_branch="main",
            matched_path="AGENTS.md",
        ),
        RepoCandidate(
            query="AGENTS.md",
            full_name="org/pending",
            repository_url="https://github.com/org/pending",
            stars=50,
            pushed_at=datetime(2025, 3, 1),
            default_branch="main",
            matched_path="AGENTS.md",
        ),
    ]
    eligible_path = tmp_path / "eligible.jsonl"
    excluded_path = tmp_path / "excluded.jsonl"
    summary_path = tmp_path / "summary.json"

    filter_repositories(
        client,
        candidates[:1],
        eligible_output_path=eligible_path,
        excluded_output_path=excluded_path,
        summary_output_path=summary_path,
    )
    assert client.get_repository.call_count == 1

    client.get_repository.reset_mock()
    eligible, excluded, summary = filter_repositories(
        client,
        candidates,
        eligible_output_path=eligible_path,
        excluded_output_path=excluded_path,
        summary_output_path=summary_path,
        resume=True,
    )

    assert client.get_repository.call_count == 1
    assert client.get_repository.call_args.args[0] == "org/pending"
    assert len(eligible) == 2
    assert len(excluded) == 0
    assert summary.eligible_count == 2
    processed, loaded_eligible, loaded_excluded = load_filter_progress(
        eligible_output_path=eligible_path,
        excluded_output_path=excluded_path,
    )
    assert processed == {"org/done", "org/pending"}
    assert len(loaded_eligible) == 2
    assert loaded_excluded == []


def test_filter_repositories_propagates_rate_limit(tmp_path) -> None:
    client = MagicMock()
    client.get_repository.side_effect = GitHubRateLimitExceeded(
        "quota exhausted",
        resource="core",
        sleep_seconds=2000.0,
        reset_at="2026-06-18 23:34:02",
    )
    candidates = [
        RepoCandidate(
            query="AGENTS.md",
            full_name="org/repo",
            repository_url="https://github.com/org/repo",
            stars=50,
            pushed_at=datetime(2025, 3, 1),
            default_branch="main",
            matched_path="AGENTS.md",
        )
    ]
    eligible_path = tmp_path / "eligible.jsonl"
    excluded_path = tmp_path / "excluded.jsonl"

    with pytest.raises(GitHubRateLimitExceeded):
        filter_repositories(
            client,
            candidates,
            eligible_output_path=eligible_path,
            excluded_output_path=excluded_path,
        )

    assert excluded_path.read_text(encoding="utf-8") == ""


def test_load_filter_progress_retries_metadata_failures(tmp_path) -> None:
    eligible_path = tmp_path / "eligible.jsonl"
    excluded_path = tmp_path / "excluded.jsonl"
    write_jsonl(
        excluded_path,
        [
            ExcludedRepo(
                full_name="org/rate-limited",
                repository_url="https://github.com/org/rate-limited",
                stars=1,
                exclusion_reasons=["metadata_fetch_failed"],
            ),
            ExcludedRepo(
                full_name="org/fork",
                repository_url="https://github.com/org/fork",
                stars=1,
                exclusion_reasons=["fork"],
            ),
        ],
    )

    processed, eligible, excluded = load_filter_progress(
        eligible_output_path=eligible_path,
        excluded_output_path=excluded_path,
        retry_metadata_failures=True,
    )

    assert processed == {"org/fork"}
    assert len(excluded) == 1
    assert excluded[0].full_name == "org/fork"
    assert "org/rate-limited" not in processed


def test_run_seed_search_enriches_candidates(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(
        "vsdlc_mining.seed_search.SEED_SEARCH_QUERIES",
        [("filename:AGENTS.md", "AGENTS.md")],
    )
    monkeypatch.setattr("vsdlc_mining.seed_search.SEARCH_QUERY_DELAY_SECONDS", 0)
    client = MagicMock()
    client.search_code.return_value = [
        {
            "path": "AGENTS.md",
            "repository": {
                "full_name": "org/repo",
                "html_url": "https://github.com/org/repo",
            },
        }
    ]
    client.get_repository.return_value = {
        "stargazers_count": 20,
        "pushed_at": "2025-01-15T10:00:00Z",
        "default_branch": "main",
        "license": {"spdx_id": "MIT"},
    }

    output_path = tmp_path / "candidates.jsonl"
    checkpoint_path = tmp_path / "checkpoint.json"
    candidates = run_seed_search(
        client,
        checkpoint_path=checkpoint_path,
        output_path=output_path,
    )
    assert len(candidates) == 1
    assert candidates[0].full_name == "org/repo"
    assert candidates[0].stars == 20
    assert candidates[0].license == "MIT"
    assert output_path.exists()
    assert checkpoint_path.exists()


def test_seed_search_checkpoint_resume(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr("vsdlc_mining.seed_search.SEARCH_QUERY_DELAY_SECONDS", 0)
    checkpoint_path = tmp_path / "checkpoint.json"
    save_checkpoint(
        checkpoint_path,
        completed_queries=["AGENTS.md"],
        aggregate={
            "org/repo": {
                "full_name": "org/repo",
                "repository_url": "https://github.com/org/repo",
                "queries": {"AGENTS.md"},
                "matched_paths": {"AGENTS.md"},
            }
        },
        search_completed=True,
        enriched_full_names=[],
    )

    client = MagicMock()
    client.get_repository.return_value = {
        "stargazers_count": 20,
        "pushed_at": "2025-01-15T10:00:00Z",
        "default_branch": "main",
        "license": {"spdx_id": "MIT"},
    }
    output_path = tmp_path / "candidates.jsonl"
    candidates = run_seed_search(
        client,
        resume=True,
        checkpoint_path=checkpoint_path,
        output_path=output_path,
    )
    client.search_code.assert_not_called()
    assert len(candidates) == 1
    loaded = load_checkpoint(checkpoint_path)
    assert loaded is not None
    assert loaded["search_completed"] is True


def test_seed_search_propagates_rate_limit_during_enrichment(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr("vsdlc_mining.seed_search.SEARCH_QUERY_DELAY_SECONDS", 0)
    checkpoint_path = tmp_path / "checkpoint.json"
    save_checkpoint(
        checkpoint_path,
        completed_queries=["AGENTS.md"],
        aggregate={
            "org/repo": {
                "full_name": "org/repo",
                "repository_url": "https://github.com/org/repo",
                "queries": {"AGENTS.md"},
                "matched_paths": {"AGENTS.md"},
            }
        },
        search_completed=True,
        enriched_full_names=[],
    )

    client = MagicMock()
    client.get_repository.side_effect = GitHubRateLimitExceeded(
        "quota exhausted",
        resource="core",
        sleep_seconds=2000.0,
        reset_at="2026-06-18 23:34:02",
    )
    output_path = tmp_path / "candidates.jsonl"

    with pytest.raises(GitHubRateLimitExceeded):
        run_seed_search(
            client,
            resume=True,
            checkpoint_path=checkpoint_path,
            output_path=output_path,
        )

    loaded = load_checkpoint(checkpoint_path)
    assert loaded is not None
    assert loaded["enriched_full_names"] == []
    assert output_path.exists() is False or output_path.read_text(encoding="utf-8") == ""


def test_is_rate_limited_detects_secondary_limit() -> None:
    response = MagicMock()
    response.status_code = 403
    response.json.return_value = {
        "message": "You have exceeded a secondary rate limit. Please wait a few minutes."
    }
    response.headers = {}
    assert _is_rate_limited(response) is True
    assert _is_secondary_rate_limited(response) is True


def test_secondary_rate_limit_sleep_is_capped(monkeypatch) -> None:
    sleeps: list[float] = []
    monkeypatch.setattr("vsdlc_mining.github_client.time.sleep", lambda seconds: sleeps.append(seconds))
    monkeypatch.setattr("vsdlc_mining.github_client.time.time", lambda: 1_000_000.0)

    response = MagicMock()
    response.status_code = 403
    response.json.return_value = {
        "message": "You have exceeded a secondary rate limit. Please wait a few minutes."
    }
    response.headers = {
        "X-RateLimit-Reset": str(1_002_207),  # would imply ~2207s if misapplied
        "X-RateLimit-Resource": "core",
    }

    client = GitHubClient(token="test-token")
    client._sleep_for_rate_limit(response, attempt=0)
    assert sleeps
    assert sleeps[0] <= 120.0


def test_primary_rate_limit_exits_instead_of_hour_long_sleep(monkeypatch) -> None:
    monkeypatch.setattr("vsdlc_mining.github_client.time.time", lambda: 1_000_000.0)
    sleeps: list[float] = []
    monkeypatch.setattr(
        "vsdlc_mining.github_client.time.sleep",
        lambda seconds: sleeps.append(seconds),
    )

    response = MagicMock()
    response.status_code = 403
    response.json.return_value = {"message": "API rate limit exceeded"}
    response.headers = {
        "X-RateLimit-Reset": str(1_002_207),
        "X-RateLimit-Resource": "core",
    }

    waiting_client = GitHubClient(token="test-token", wait_for_rate_limit=True)
    waiting_client.get_rate_limit = MagicMock(  # type: ignore[method-assign]
        return_value={"resources": {"core": {"remaining": 0, "limit": 5000}}}
    )
    waiting_client._sleep_for_rate_limit(response, attempt=0)
    assert sum(sleeps) == pytest.approx(2208.0)

    sleeps.clear()
    exiting_client = GitHubClient(token="test-token", wait_for_rate_limit=False)
    with pytest.raises(GitHubRateLimitExceeded) as exc_info:
        exiting_client._sleep_for_rate_limit(response, attempt=0)
    assert exc_info.value.sleep_seconds > 300
    assert sleeps == []


def test_jsonl_roundtrip(tmp_path) -> None:
    path = tmp_path / "candidates.jsonl"
    original = RepoCandidate(
        query="AGENTS.md",
        full_name="org/repo",
        repository_url="https://github.com/org/repo",
        stars=10,
        pushed_at=datetime(2025, 1, 1),
        default_branch="main",
        matched_path="AGENTS.md",
    )
    write_jsonl(path, [original])
    loaded = read_jsonl(path, RepoCandidate)
    assert loaded[0].full_name == "org/repo"


def test_write_json_atomic_roundtrip(tmp_path) -> None:
    path = tmp_path / "checkpoint.json"
    payload = {"completed_queries": ["AGENTS.md"], "search_completed": True}
    write_json(path, payload)
    assert read_json(path) == payload
    assert list(tmp_path.glob(".checkpoint.json.*.tmp")) == []


def test_salvage_json_recovers_truncated_document(tmp_path) -> None:
    path = tmp_path / "checkpoint.json"
    payload = {
        "completed_queries": ["AGENTS.md"],
        "search_completed": True,
        "enriched_full_names": ["org/repo"],
        "aggregate": {},
    }
    write_json(path, payload)
    raw = path.read_text(encoding="utf-8")
    path.write_text(raw.rstrip().removesuffix("}"), encoding="utf-8")
    recovered, _trimmed = salvage_json(path)
    assert recovered["completed_queries"] == ["AGENTS.md"]
    assert recovered["enriched_full_names"] == ["org/repo"]


def test_load_checkpoint_salvages_truncated_file(tmp_path) -> None:
    checkpoint_path = tmp_path / "checkpoint.json"
    save_checkpoint(
        checkpoint_path,
        completed_queries=["AGENTS.md"],
        aggregate={},
        search_completed=True,
        enriched_full_names=["org/repo"],
    )
    raw = checkpoint_path.read_text(encoding="utf-8")
    checkpoint_path.write_text(raw[:-30], encoding="utf-8")
    loaded = load_checkpoint(checkpoint_path)
    assert loaded is not None
    assert loaded["enriched_full_names"] == ["org/repo"]


def test_repair_checkpoint_syncs_enriched_from_jsonl(tmp_path) -> None:
    checkpoint_path = tmp_path / "checkpoint.json"
    output_path = tmp_path / "candidates.jsonl"
    save_checkpoint(
        checkpoint_path,
        completed_queries=["AGENTS.md"],
        aggregate={
            "org/repo": {
                "full_name": "org/repo",
                "repository_url": "https://github.com/org/repo",
                "queries": {"AGENTS.md"},
                "matched_paths": {"AGENTS.md"},
            }
        },
        search_completed=True,
        enriched_full_names=["org/repo", "org/stale"],
    )
    write_jsonl(
        output_path,
        [
            RepoCandidate(
                query="AGENTS.md",
                full_name="org/repo",
                repository_url="https://github.com/org/repo",
                stars=10,
                pushed_at=datetime(2025, 1, 1),
                default_branch="main",
                matched_path="AGENTS.md",
            )
        ],
    )
    repair_checkpoint(checkpoint_path, output_path=output_path)
    loaded = read_json(checkpoint_path)
    assert loaded["enriched_full_names"] == ["org/repo"]
