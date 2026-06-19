# Reproducibility guide — VSDLC Mining Pilot

This document explains how to independently rerun the repository mining framework and regenerate the repository traceability dataset.

## Scope

Phases implemented in this artifact:

1. **Phase 1 — Seed search** (`scripts/run_seed_search.py`)
2. **Phase 2 — Repository filter** (`scripts/run_repo_filter.py`)

Later stages (cloning, release-unit extraction, trace scoring) are out of scope for this release.

## Prerequisites

- Python **3.11+**
- A GitHub personal access token with permission to call the public REST API
- Network access to `api.github.com`

## Environment

```bash
cd ~/papers/vsdlc/vsdlc
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
export GITHUB_TOKEN="ghp_..."   # never commit this token
```

Optional: store the token in a local `.env` file (ignored by git) and `source` it before running.

## Rerun procedure

### Quick pilot

Controlled test before the full mining run. Uses separate `pilot_*` paths so main outputs stay untouched.

```bash
python scripts/run_seed_search.py \
  --no-resume \
  --query AGENTS.md \
  --max-pages 2 \
  --output data/raw/pilot_agents_candidates.jsonl \
  --checkpoint data/interim/pilot_agents_checkpoint.json

python scripts/run_repo_filter.py \
  --input data/raw/pilot_agents_candidates.jsonl \
  --eligible-output data/interim/pilot_agents_eligible.jsonl \
  --excluded-output data/interim/pilot_agents_excluded.jsonl \
  --summary-output data/interim/pilot_agents_summary.json \
  --limit-repos 20
```

Expected pilot runtime: **~2–5 minutes** (mostly code-search rate limits).

### Full run — Phase 1 (seed search)

```bash
python scripts/run_seed_search.py
```

If interrupted by rate limits or manual stop:

```bash
python scripts/run_seed_search.py --resume
```

Expected full-run runtime: **~30–60+ minutes** for Phase 1 (17 queries + enrichment), plus additional time for Phase 2 on large corpora.

**Inputs:** GitHub code-search queries defined in `src/vsdlc_mining/config.py`.

**Outputs:**

| Path | Description |
|------|-------------|
| `data/raw/repo_candidates.jsonl` | Candidate rows for the repository traceability dataset |
| `data/interim/seed_search_checkpoint.json` | Local resume cache (gitignored) |

### Full run — Phase 2 (repository filter)

Requires Phase 1 output.

```bash
python scripts/run_repo_filter.py
```

**Outputs:**

| Path | Description |
|------|-------------|
| `data/interim/eligible_repos.jsonl` | Filtered eligible repositories |
| `data/interim/excluded_repos.jsonl` | Excluded repositories with reasons |
| `data/interim/filter_summary.json` | Aggregate exclusion counts |

## Rate limits and caching

- **Code search API** is the main bottleneck (~30 requests/minute plus secondary burst limits).
- The client retries on 403/429 with exponential backoff and sleeps between pages and queries.
- **Checkpointing** saves progress after each seed query and after each metadata enrichment.
- **Core REST API** (`/repos/...`) has a higher hourly quota; enrichment of thousands of repositories may still trigger throttling near the limit.

Exact result counts will vary with GitHub index state and API quotas at run time. Do not expect bit-identical outputs across months.

## Data policy

- Only **public GitHub metadata** is collected via the API.
- **No repository cloning** is performed in Phases 1–2.
- **No secrets** should appear in outputs; do not commit `GITHUB_TOKEN`.
- Redistributing mined metadata must respect **repository licenses** and **GitHub Terms of Service**.

## Quality checks before Zenodo release

```bash
pytest
ruff check src tests scripts
mypy src/vsdlc_mining
```

## Citation after Zenodo DOI assignment

1. Mint or reserve a DOI on Zenodo.
2. Replace `doi: 10.5281/zenodo.PLACEHOLDER` in `CITATION.cff`.
3. Replace repository URL placeholders in `CITATION.cff` and `pyproject.toml`.
4. Cite using the Zenodo record or the `CITATION.cff` metadata.

Example (fill after DOI assignment):

```bibtex
@software{vsdlc_mining_pilot_2026,
  author = {S{\'a}nchez, C{\'e}sar Andr{\'e}s and Moncunill, David Martin},
  title = {{VSDLC Mining Pilot}},
  year = {2026},
  version = {0.1.0},
  doi = {10.5281/zenodo.PLACEHOLDER},
  url = {https://github.com/PLACEHOLDER_ORG/vsdlc-mining}
}
```
