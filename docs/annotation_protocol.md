# Second-stage classification — annotator protocol

**Templates:** `data/processed/repo_classifications_template.{jsonl,csv}` (empty scaffolds).  
**Synthetic reference:** `docs/annotation_example.json`.  
**Schema:** `~/papers/vsdlc/docs/classification_schema.md` (v0.2)

---

## Purpose

Classify eligible repositories with the **3-label primary instrument** for decontamination:

- Target population: `CONVENTIONAL_SOFTWARE`
- Non-target: `AI_PRODUCT` or `EXCLUDE`

Does **not** change Phase 2 eligibility.

### Deprecated v0.1 labels

`TOOL`, `ASSIST`, `MIXED`, `UNCLEAR` are **not** valid `primary_label` values. Use only optional `secondary_tags` or `evidence_notes` if needed for audit.

---

## Primary labels (exactly one)

| Code | Definition |
|------|------------|
| `AI_PRODUCT` | Primary consumers build, evaluate, operate, secure, or orchestrate AI systems |
| `CONVENTIONAL_SOFTWARE` | Primary consumers are end users or non-AI developers; AI may be internal or a core feature |
| `EXCLUDE` | Non-product, dotfiles, docs-only, prompt packs, courses, awesome lists, insufficient evidence |

---

## Secondary tags (optional, zero or more)

Pipe-separated in CSV:

`NON_PRODUCT` | `INSUFFICIENT_EVIDENCE` | `DUAL_REVIEW` | `BENCHMARK_OR_EVAL` | `PROMPT_COLLECTION` | `AI_SECURITY_LAB` | `AI_CENTRAL_END_USER_APP` | `RUNNABLE_PROMPT_TOOL` | `DOTFILES` | `DOCS_ONLY`

---

## Ordered decision flow

| Step | Rule | Label |
|------|------|-------|
| **0** | Non-product gate: dotfiles, docs-only, pure prompt/skill collection, course, awesome list, not buildable/usable | `EXCLUDE` |
| **1** | Evidence floor: no description **and** no topics | `EXCLUDE` unless name unambiguous |
| **2** | Consumer test: AI builders/operators/evaluators/security researchers vs end users/non-AI developers | `AI_PRODUCT` or `CONVENTIONAL_SOFTWARE` |
| **3** | Packaging cue: end-user app vs library/SDK/framework/server/MCP/benchmark/red-team/LLM infra | tie-break |
| **4** | Runnable-vs-collection: markdown-only prompts → `EXCLUDE`; runnable prompt tooling → `AI_PRODUCT` | |
| **5** | AI-central end-user app → `CONVENTIONAL_SOFTWARE` unless consumers are AI-system builders | |

Record which step decided the label in `evidence_notes`.

---

## Evidence sources

1. `github_description`
2. `github_topics` (pipe-separated in CSV)
3. README — summarise in `evidence_notes`
4. Dependencies — one manifest
5. `detected_instruction_artifacts`
6. `ci_evidence`, `release_evidence`

Optional backfill: `python3.11 scripts/backfill_metadata.py`

---

## Confidence

`high` | `medium` | `low` — see schema §4.

---

## Do not use `agent_product_flag`

Assign `primary_label` before opening `agent_product_flag`.

---

## Rounds and adjudication

| Round | `annotation_round` |
|-------|-------------------|
| Independent A / B | `1` |
| Adjudication | `1` or `2` → `adjudicated_label` |

`adjudication_status`: `pending` | `agreed` | `disputed` | `adjudicated` | `not_applicable`

---

## File workflow

1. Copy template or use `gold_sample_repos_enriched.csv`.
2. Fill `primary_label`, optional `secondary_tags`, `confidence`, `evidence_notes`, `annotator_id`, `annotation_round`.
3. Never overwrite `*_template.*` with annotations.

---

## Quality gate

Self-check against `annotation_example.json` before production Round 1.
