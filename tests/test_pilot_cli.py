"""Tests for pilot-friendly CLI options."""

from __future__ import annotations

from datetime import datetime
from unittest.mock import MagicMock

import pytest

from vsdlc_mining.config import (
    ELIGIBLE_REPOS_PATH,
    EXCLUDED_REPOS_PATH,
    FILTER_SUMMARY_PATH,
    PILOT_AGENTS_CANDIDATES_PATH,
    PILOT_AGENTS_CHECKPOINT_PATH,
    PILOT_AGENTS_ELIGIBLE_PATH,
    PILOT_AGENTS_EXCLUDED_PATH,
    PILOT_AGENTS_SUMMARY_PATH,
    REPO_CANDIDATES_PATH,
    SEED_SEARCH_CHECKPOINT_PATH,
)
from vsdlc_mining.github_client import GitHubClient
from vsdlc_mining.models import RepoCandidate
from vsdlc_mining.repo_filter import filter_repositories
from vsdlc_mining.seed_search import run_seed_search, select_seed_queries
from vsdlc_mining.utils import write_jsonl


def test_select_seed_queries_filters_by_label() -> None:
    matched = select_seed_queries("AGENTS.md")
    assert len(matched) == 1
    assert matched[0][1] == "AGENTS.md"


def test_select_seed_queries_is_case_insensitive() -> None:
    matched = select_seed_queries("agents.md")
    assert len(matched) == 1
    assert matched[0][1] == "AGENTS.md"


def test_select_seed_queries_raises_when_no_match() -> None:
    with pytest.raises(ValueError, match="No seed query matches"):
        select_seed_queries("does-not-exist")


def test_search_code_respects_max_pages_override(monkeypatch) -> None:
    monkeypatch.setenv("GITHUB_TOKEN", "test-token")
    monkeypatch.setattr("vsdlc_mining.github_client.time.sleep", lambda _seconds: None)

    client = GitHubClient()
    pages_requested: list[int] = []

    def fake_get_json(path: str, params: dict | None = None):
        assert path == "/search/code"
        assert params is not None
        pages_requested.append(params["page"])
        return {
            "items": [
                {
                    "path": "AGENTS.md",
                    "repository": {"full_name": f"org/repo-{params['page']}-{i}"},
                }
                for i in range(100)
            ],
            "total_count": 500,
        }

    monkeypatch.setattr(client, "get_json", fake_get_json)

    results = client.search_code("filename:AGENTS.md", max_results=1000, max_pages=2)
    assert len(results) == 200
    assert pages_requested == [1, 2]


def test_run_seed_search_query_filter_and_max_pages(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr("vsdlc_mining.seed_search.SEARCH_QUERY_DELAY_SECONDS", 0)

    client = MagicMock()
    client.per_page = 100
    client.search_code.return_value = []
    client.get_repository.return_value = {
        "stargazers_count": 1,
        "pushed_at": "2025-01-01T00:00:00Z",
        "default_branch": "main",
        "license": None,
    }

    output_path = tmp_path / "pilot_candidates.jsonl"
    checkpoint_path = tmp_path / "pilot_checkpoint.json"

    run_seed_search(
        client,
        fresh_start=True,
        checkpoint_path=checkpoint_path,
        output_path=output_path,
        query_filter="AGENTS.md",
        max_pages=2,
    )

    client.search_code.assert_called_once()
    _, kwargs = client.search_code.call_args
    assert kwargs["max_pages"] == 2
    assert kwargs["max_results"] == 200


def test_pilot_output_does_not_touch_main_paths(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr("vsdlc_mining.seed_search.SEARCH_QUERY_DELAY_SECONDS", 0)

    main_output = tmp_path / "data" / "raw" / "repo_candidates.jsonl"
    main_checkpoint = tmp_path / "data" / "interim" / "seed_search_checkpoint.json"
    main_output.parent.mkdir(parents=True)
    main_checkpoint.parent.mkdir(parents=True)
    main_output.write_text('{"keep": true}\n', encoding="utf-8")
    main_checkpoint.write_text('{"keep": true}', encoding="utf-8")

    pilot_output = tmp_path / "data" / "raw" / "pilot_agents_candidates.jsonl"
    pilot_checkpoint = tmp_path / "data" / "interim" / "pilot_agents_checkpoint.json"

    client = MagicMock()
    client.per_page = 100
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

    run_seed_search(
        client,
        fresh_start=True,
        checkpoint_path=pilot_checkpoint,
        output_path=pilot_output,
        query_filter="AGENTS.md",
        max_pages=1,
    )

    assert pilot_output.exists()
    assert pilot_checkpoint.exists()
    assert main_output.read_text(encoding="utf-8") == '{"keep": true}\n'
    assert main_checkpoint.read_text(encoding="utf-8") == '{"keep": true}'


def test_pilot_paths_differ_from_main_defaults() -> None:
    assert PILOT_AGENTS_CANDIDATES_PATH != REPO_CANDIDATES_PATH
    assert PILOT_AGENTS_CHECKPOINT_PATH != SEED_SEARCH_CHECKPOINT_PATH
    assert PILOT_AGENTS_ELIGIBLE_PATH != ELIGIBLE_REPOS_PATH
    assert PILOT_AGENTS_EXCLUDED_PATH != EXCLUDED_REPOS_PATH
    assert PILOT_AGENTS_SUMMARY_PATH != FILTER_SUMMARY_PATH


def _candidate(full_name: str) -> RepoCandidate:
    return RepoCandidate(
        query="AGENTS.md",
        full_name=full_name,
        repository_url=f"https://github.com/{full_name}",
        stars=50,
        pushed_at=datetime(2025, 3, 1),
        default_branch="main",
        matched_path="AGENTS.md",
        queries=["AGENTS.md"],
        matched_paths=["AGENTS.md"],
    )


def test_filter_repositories_limit_repos() -> None:
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

    candidates = [_candidate("org/a"), _candidate("org/b"), _candidate("org/c")]
    eligible, excluded, summary = filter_repositories(client, candidates, limit_repos=2)

    assert client.get_repository.call_count == 2
    assert summary.input_candidates == 2
    assert len(eligible) + len(excluded) == 2


def test_filter_custom_output_paths(tmp_path) -> None:
    input_path = tmp_path / "pilot_candidates.jsonl"
    eligible_path = tmp_path / "pilot_eligible.jsonl"
    excluded_path = tmp_path / "pilot_excluded.jsonl"
    summary_path = tmp_path / "pilot_summary.json"

    write_jsonl(input_path, [_candidate("org/service")])

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

    from vsdlc_mining.utils import read_jsonl, write_json

    candidates = read_jsonl(input_path, RepoCandidate)
    eligible, excluded, summary = filter_repositories(client, candidates, limit_repos=1)
    write_jsonl(eligible_path, eligible)
    write_jsonl(excluded_path, excluded)
    write_json(summary_path, summary.model_dump())

    assert eligible_path.exists()
    assert excluded_path.exists()
    assert summary_path.exists()
    assert eligible_path.name == "pilot_eligible.jsonl"
