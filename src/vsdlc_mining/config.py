"""Configuration constants for the mining pilot."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
INTERIM_DIR = DATA_DIR / "interim"
PROCESSED_DIR = DATA_DIR / "processed"

REPO_CANDIDATES_PATH = RAW_DIR / "repo_candidates.jsonl"
SEED_SEARCH_CHECKPOINT_PATH = INTERIM_DIR / "seed_search_checkpoint.json"
ELIGIBLE_REPOS_PATH = INTERIM_DIR / "eligible_repos.jsonl"
EXCLUDED_REPOS_PATH = INTERIM_DIR / "excluded_repos.jsonl"
FILTER_SUMMARY_PATH = INTERIM_DIR / "filter_summary.json"

# Recommended pilot paths (do not overwrite main outputs unless explicitly chosen).
PILOT_AGENTS_CANDIDATES_PATH = RAW_DIR / "pilot_agents_candidates.jsonl"
PILOT_AGENTS_CHECKPOINT_PATH = INTERIM_DIR / "pilot_agents_checkpoint.json"
PILOT_AGENTS_ELIGIBLE_PATH = INTERIM_DIR / "pilot_agents_eligible.jsonl"
PILOT_AGENTS_EXCLUDED_PATH = INTERIM_DIR / "pilot_agents_excluded.jsonl"
PILOT_AGENTS_SUMMARY_PATH = INTERIM_DIR / "pilot_agents_summary.json"

GITHUB_API_BASE = "https://api.github.com"
GITHUB_SEARCH_CODE_URL = f"{GITHUB_API_BASE}/search/code"

# Minimum activity and popularity thresholds (Phase 2).
MIN_STARS = 10
MIN_PUSHED_AT = datetime(2024, 6, 1)

# GitHub code-search queries: (api_query, human_label).
# Labels appear in audit output as the matched artifact category.
SEED_SEARCH_QUERIES: list[tuple[str, str]] = [
    ("filename:AGENTS.md", "AGENTS.md"),
    ("filename:.cursorrules", ".cursorrules"),
    ("path:.cursor/rules", ".cursor/rules"),
    ("filename:copilot-instructions.md", "copilot-instructions.md"),
    ("path:.github filename:copilot-instructions.md", ".github/copilot-instructions.md"),
    ("filename:CLAUDE.md", "CLAUDE.md"),
    ("filename:.aider.conf.yml", ".aider.conf.yml"),
    ("filename:.aiderignore", ".aiderignore"),
    ("filename:.aider.model.settings.yml", ".aider.model.settings.yml"),
    ("path:prompts/", "prompts/"),
    ("filename:system_prompt", "system_prompt.*"),
    ("filename:system-prompt", "system-prompt.*"),
    ("filename:.windsurfrules", ".windsurfrules"),
    ("filename:.clinerules", ".clinerules"),
    ("filename:GEMINI.md", "GEMINI.md"),
    ("path:.github/chatmodes", ".github/chatmodes"),
    ("extension:md prompt in:path", "*.prompt.md"),
]

# Heuristic keywords for excluding non-target repositories.
EXCLUSION_KEYWORDS: list[str] = [
    "tutorial",
    "tutorials",
    "example",
    "examples",
    "demo",
    "demos",
    "awesome",
    "awesome-list",
    "course",
    "courses",
    "dotfiles",
    "dotfile",
    "playground",
    "boilerplate",
    "starter",
    "starter-kit",
    "template-repo",
    "sample-app",
    "sample-project",
    "learning",
    "workshop",
    "cheatsheet",
    "mirror",
]

# Keywords suggesting the repo is AI-tooling product documentation (retain).
AGENT_PRODUCT_KEYWORDS: list[str] = [
    "cursor",
    "copilot",
    "aider",
    "cline",
    "windsurf",
    "claude-code",
    "agent",
    "agents",
    "prompt",
    "prompts",
    "llm",
    "ai-assistant",
    "ai assistant",
    "chatmode",
    "gemini",
    "devin",
    "codeium",
]

# Paths indicating CI or test evidence (checked via GitHub contents API).
CI_PATH_HINTS: list[str] = [
    ".github/workflows",
    ".travis.yml",
    ".circleci",
    "Jenkinsfile",
    "azure-pipelines.yml",
    ".gitlab-ci.yml",
    "bitbucket-pipelines.yml",
    ".buildkite",
]

TEST_PATH_HINTS: list[str] = [
    "pytest.ini",
    "tox.ini",
    "jest.config",
    "vitest.config",
    "karma.conf",
    "phpunit.xml",
    "go.mod",  # weak signal; combined with test dirs
    "Cargo.toml",
]

TEST_DIR_HINTS: list[str] = [
    "test/",
    "tests/",
    "__tests__/",
    "spec/",
    "specs/",
]

# HTTP client defaults.
DEFAULT_PER_PAGE = 100
MAX_SEARCH_RESULTS = 1000
MAX_CODE_SEARCH_PAGES = 10  # GitHub hard cap for code search pagination.
MAX_RETRIES = 5
INITIAL_BACKOFF_SECONDS = 2.0

# Throttle code-search bursts to avoid secondary rate limits (~30 search req/min).
SEARCH_PAGE_DELAY_SECONDS = 2.5
SEARCH_QUERY_DELAY_SECONDS = 8.0
SEARCH_RATE_LIMIT_BUFFER = 3  # pause when remaining search quota drops below this.

# Core REST API pacing (5000 req/hr authenticated).
CORE_REQUEST_MIN_INTERVAL_SECONDS = 0.75
CORE_RATE_LIMIT_BUFFER = 250
SECONDARY_RATE_LIMIT_MAX_SECONDS = 120.0
RATE_LIMIT_WAIT_CHUNK_SECONDS = 60.0
# When primary core quota is exhausted, exit for manual resume instead of blocking ~1 hour.
MAX_PRIMARY_RATE_LIMIT_SLEEP_SECONDS = 300.0
