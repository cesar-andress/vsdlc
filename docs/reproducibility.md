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

## Manuscript reliability metrics (Cohen's $\kappa$ bootstrap CIs)

Frozen pilot outputs include `data/processed/kappa_bootstrap_ci.json`, produced by:

```bash
cd ~/papers/vsdlc/vsdlc
python3 scripts/compute_kappa_bootstrap_ci.py
```

Defaults:
- Human--human pairs: `data/processed/gold_sample_330_three_annotator_comparison.csv` (`human1_label` vs `human2_label`, $n{=}300$)
- Metadata vs inspection: `inspection_sample_50.csv` vs `inspection_sample_50_completed_fixed.csv` ($n{=}50$)

The script computes point estimates and **95% percentile bootstrap confidence intervals** (10{,}000 resamples, seed 42) for:
- three-class $\kappa$
- `AI_PRODUCT` vs `CONVENTIONAL_SOFTWARE` (pairs where neither side is `EXCLUDE`)
- collapsed `EXCLUDE` vs non-`EXCLUDE`

Unit tests: `pytest tests/test_kappa_bootstrap.py`

Disagreement attribution for the EXCLUDE finding (Table~\ref{tab:exclude-disagreement}, Figure~\ref{fig:exclude-disagreement}):

```bash
python3 scripts/compute_exclude_disagreement_stats.py
```

Output: `data/processed/exclude_disagreement_stats.json`

## Target-sensitivity analysis (RQ1 supplement)

Uses frozen consensus labels only (`data/processed/gold_sample_330_three_annotator_comparison.csv`); no relabeling.

```bash
cd ~/papers/vsdlc/vsdlc
PYTHONPATH=src python3 scripts/analyze_target_sensitivity.py
```

Outputs:

| Artifact | Path |
|----------|------|
| Sensitivity JSON | `data/processed/target_sensitivity_results.json` |
| Manuscript table | `data/processed/manuscript_table_target_sensitivity.tex` |

Unit tests: `pytest tests/test_target_sensitivity.py`

## Second functional-evidence inspector (RQ4 extension)

The frozen RQ4 sample (`n{=}50`) can be reassessed by a second independent inspector using the same codebook and blind protocol. The second inspector must not see metadata consensus labels, Round~1 coder labels, inspector~1 labels, or any prior worksheet labels.

### 1. Create the blank worksheet

```bash
cd ~/papers/vsdlc/vsdlc
PYTHONPATH=src python3 scripts/create_second_inspector_blank.py
```

Defaults:
- Source metadata: `data/processed/inspection_sample_50_blank.csv`
- Output: `data/processed/inspection_sample_50_second_inspector_blank.csv`

The blank worksheet exposes only repository context fields (`repo_full_name`, `repo_url`, description/topics/language, matched-path provenance, CI/release evidence) plus empty inspector~2 fields:
`inspector2_label`, `inspector2_confidence`, `inspector2_evidence_sources`, `inspector2_functional_note`, `inspector2_free_notes`.

Record `inspector2_evidence_sources` as comma- or pipe-separated tokens from:
`readme`, `file_tree`, `dependencies`, `entrypoints`, `instruction_consumption`.

Protocol details: `docs/inspection_validation_protocol.md` (second-inspector section).

### 2. Human completion

Save the completed worksheet as:

`data/processed/inspection_sample_50_second_inspector_completed.csv`

Use the same 50 `repo_full_name` values and column order as the blank worksheet. Do not add prior label columns.

### 3. Validate completed worksheet

```bash
PYTHONPATH=src python3 scripts/validate_second_inspection.py \
  --blank data/processed/inspection_sample_50_second_inspector_blank.csv \
  --completed data/processed/inspection_sample_50_second_inspector_completed.csv
```

Checks:
- all 50 repositories present
- `inspector2_label` in `{CONVENTIONAL_SOFTWARE, AI_PRODUCT, EXCLUDE}`
- non-empty `inspector2_functional_note`
- at least two evidence-source tokens when applicable

### 4. Evaluate dual-inspector concordance

```bash
PYTHONPATH=src python3 scripts/evaluate_second_inspection.py
```

Defaults:
- Metadata consensus reference: `data/processed/inspection_sample_50.csv`
- Inspector~1 completed worksheet: `data/processed/inspection_sample_50_completed_fixed.csv`
- Inspector~2 completed worksheet: `data/processed/inspection_sample_50_second_inspector_completed.csv`

Outputs:
- `data/processed/second_inspection_validation_results.json`
- `data/processed/second_inspection_confusion_matrices.csv`
- `data/processed/second_inspection_disagreement_stats.json`
- `data/processed/manuscript_table_rq4_second_inspector.tex`

Metrics computed for each comparison (`metadata_consensus_vs_inspector1`, `metadata_consensus_vs_inspector2`, `inspector1_vs_inspector2`):
- three-class agreement, Cohen's $\kappa$, 95\% bootstrap CI
- binary TARGET vs NON_TARGET agreement and $\kappa$
- `AI_PRODUCT` vs `CONVENTIONAL_SOFTWARE` excluding `EXCLUDE`
- `EXCLUDE` vs non-`EXCLUDE`
- confusion matrices and disagreement decomposition (`EXCLUDE` vs `CONVENTIONAL_SOFTWARE`, `EXCLUDE` vs `AI_PRODUCT`, `AI_PRODUCT` vs `CONVENTIONAL_SOFTWARE`)

Unit tests: `pytest tests/test_second_inspection.py`

Existing RQ4 manuscript metrics remain unchanged until inspector~2 labels are completed and the dual-inspector evaluation is run deliberately for an updated analysis.

## Second discovery frame (AI-topic robustness extension)

Minimal robustness extension: an independent **AI-topic/metadata** discovery frame using GitHub **repository search** (not instruction-artifact code search). Results are framed as sensitivity to discovery mechanism within audited frames; they do not validate the instruction-artifact frame or generalize to all GitHub.

### Predicates (repository search)

| Label | API query fragment |
|-------|-------------------|
| `topic:llm` | `topic:llm` |
| `topic:ai-agent` | `topic:ai-agent` |
| `topic:mcp` | `topic:mcp` |
| `topic:generative-ai` | `topic:generative-ai` |
| `topic:copilot` | `topic:copilot` |
| `topic:ai-application` | `topic:ai-application` |
| `topic:agentic-ai` | `topic:agentic-ai` |

Each predicate is combined with shared eligibility qualifiers in search:

`stars:>=10 pushed:>=2024-06-01 fork:false archived:false`

Random seed for sampling: **42** (target sample size **100**; uses all eligible if fewer than 100 remain).

### Known deviations from the main instruction-artifact frame

- Discovery uses `/search/repositories` on topic predicates instead of `/search/code` on instruction-artifact paths.
- Phase~2 filtering skips the `missing_instruction_artifact` requirement (`require_instruction_artifact=False`).
- Overlap with the instruction-artifact eligible set is marked in `instruction_frame_overlap`; sampling prefers non-overlapping repositories first.
- Structural/keyword/CI-test filters otherwise follow `repo_filter.py` (stars, recency, fork/archived/template/mirror, exclusion keywords, CI or test evidence).

### Commands

```bash
cd ~/papers/vsdlc/vsdlc
export GITHUB_TOKEN="..."   # required; never commit

# Phase A — discover topic-frame candidates
PYTHONPATH=src python3 scripts/run_second_frame_search.py

# Phase B — apply eligibility filters (resume-safe)
PYTHONPATH=src python3 scripts/run_second_frame_filter.py --resume

# Phase C — sample n<=100 and create annotation blank worksheet
PYTHONPATH=src python3 scripts/create_second_frame_sample.py

# Phase D — after human annotation
# Save completed labels to data/processed/second_frame_annotation_completed.csv
PYTHONPATH=src python3 scripts/analyze_second_frame_contamination.py
```

Outputs:

| Artifact | Path |
|----------|------|
| Raw/interim candidates | `data/raw/second_frame_candidates.jsonl` |
| Eligible repositories | `data/interim/second_frame_eligible_repos.jsonl` |
| Filter summary | `data/interim/second_frame_filter_summary.json` |
| Sample manifest | `data/processed/second_frame_sample_100.csv` |
| Annotation blank | `data/processed/second_frame_annotation_blank.csv` |
| Analysis JSON | `data/processed/second_frame_contamination_results.json` |
| Manuscript table | `data/processed/manuscript_table_second_frame.md` |
| Manuscript paragraph | `data/processed/manuscript_paragraph_second_frame.md` |

Unit tests: `pytest tests/test_second_frame.py`

## Learned metadata baselines

Frozen pilot outputs include `data/processed/learned_baseline_results.json`, produced by:

```bash
cd ~/papers/vsdlc/vsdlc
python3 -m pip install -e ".[ml,dev]"
python3 scripts/evaluate_learned_baselines.py \
  --metadata data/processed/gold_sample_360b_pilot.csv \
  --labels data/processed/gold_sample_330_three_annotator_comparison.csv \
  --output data/processed/learned_baseline_results.json
```

Defaults:
- Reference labels: `majority_label` on the human--human intersection ($n{=}296$ after excluding four tied rows)
- Features: annotation-visible metadata only (no labels, no functional-evidence fields)
- Evaluation: stratified 5-fold cross-validation (seed 42)
- Models: TF-IDF + logistic regression, TF-IDF + random forest, sentence embeddings (`all-MiniLM-L6-v2`) + logistic regression

Use `--skip-embeddings` to omit the sentence-transformer model when the optional dependency is unavailable.

Unit tests: `pytest tests/test_learned_baselines.py`

Keyword-only strawman comparison (legacy): `python3 scripts/evaluate_baseline_heuristics.py` → `data/processed/baseline_comparison_330.json`

## Citation (Zenodo)

**Title:** VSDLC Mining Pilot

**Release:** VSDLC Replication Package v0.1.0 — AI Instruction Artifact Contamination Audit

**Version:** `v0.1.0-msr-contamination-audit`

**DOI:** [10.5281/zenodo.20754778](https://doi.org/10.5281/zenodo.20754778)

Cite the Zenodo record or `CITATION.cff` in `vsdlc/`.

```bibtex
@software{sanchez2026vsdlcMiningPilot,
  author    = {Andr{\'e}s, C{\'e}sar},
  title     = {{VSDLC Mining Pilot}},
  year      = {2026},
  version   = {v0.1.0-msr-contamination-audit},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.20754778},
  url       = {https://doi.org/10.5281/zenodo.20754778},
  note      = {VSDLC Replication Package v0.1.0 --- AI Instruction Artifact Contamination Audit}
}
```
