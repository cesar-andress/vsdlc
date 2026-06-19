# Baseline pilot summary (30-repository sample)

**Status:** pilot analysis — not final results  
**Sample:** `data/processed/gold_sample_30_pilot.csv`  
**Annotator reference:** `data/processed/gold_sample_30_claude.csv` (`annotator_id: claude_r2`, Round 1)  
**Comparison script:** `scripts/evaluate_baseline_heuristics.py`

---

## Scope

This note summarizes a **pilot** baseline-comparison experiment on **30 eligible repositories** drawn from the decontamination gold sample. The goal was to test whether trivial heuristics can substitute for the manual three-label annotation instrument (`AI_PRODUCT`, `CONVENTIONAL_SOFTWARE`, `EXCLUDE`).

This is an **exploratory pilot only**. Results must be repeated on the full gold sample with independent dual annotation and adjudication before any go/no-go decision.

---

## Evaluated repositories

| Metric | Value |
|--------|-------|
| Evaluated repositories | **30** |
| Primary labels (instrument) | `AI_PRODUCT`, `CONVENTIONAL_SOFTWARE`, `EXCLUDE` |
| Baseline outputs | `AI_PRODUCT` or `CONVENTIONAL_SOFTWARE` only (never `EXCLUDE`) |

---

## Baseline accuracies

Accuracy is measured against the Round 1 instrument labels on the 30-repository pilot set.

| Baseline | Rule (summary) | Accuracy |
|----------|----------------|----------|
| `baseline_1_description_topics_keywords` | `AI_PRODUCT` if description/topics contain ai, agent, llm, prompt, mcp, copilot, claude, openai; else `CONVENTIONAL_SOFTWARE` | **0.633** |
| `baseline_2_name_topics_keywords` | `AI_PRODUCT` if repo name or topics contain agent, framework, sdk, library, benchmark, eval; else `CONVENTIONAL_SOFTWARE` | **0.500** |
| `baseline_3_instruction_artifact_triggers` | `AI_PRODUCT` if artifact is AGENTS.md, CLAUDE.md, prompts/, or system_prompt.*; else `CONVENTIONAL_SOFTWARE` | **0.467** |

The best-performing trivial baseline reaches only **63.3%** accuracy. None approaches the inter-rater reliability thresholds pre-registered for the decontamination study (κ ≥ 0.60 three-class, or κ ≥ 0.70 binary decontamination).

---

## Key finding

**Superficial heuristics are insufficient for decontaminating repositories with AI-instruction artifacts.**

Keyword, naming, and artifact-path rules systematically conflate distinct repository roles. They cannot reliably separate:

- AI-system products from AI-central end-user applications
- Runnable AI tooling from non-product prompt/skill collections
- Target conventional software from repositories with insufficient public evidence

---

## Specific failure modes

### 1. AI-central end-user apps misclassified as `AI_PRODUCT`

Heuristics fire on agent/AI keywords or artifact paths, but the **consumer test** assigns `CONVENTIONAL_SOFTWARE` because end users—not AI-system builders—are the primary audience.

**Examples:** `9mtm/Agent-Player`, `AIDotNet/OpenCowork`, `AIStoryBuilders/AIStoryBuilders`, `ARPAHLS/OPSIE`

### 2. Non-product prompt/skill collections misclassified as `AI_PRODUCT` or `CONVENTIONAL_SOFTWARE`

Markdown prompt packs and skill libraries lack a buildable software product. The instrument assigns `EXCLUDE`; baselines lack that class and force a binary guess.

**Examples:** `0xN0RMXL/BugBountySkills`, `Affitor/affiliate-skills`

### 3. Missing-evidence repositories misclassified as `CONVENTIONAL_SOFTWARE`

When description and topics are absent, baselines default to `CONVENTIONAL_SOFTWARE`. The instrument applies the evidence floor and assigns `EXCLUDE`.

**Examples:** `AI-Escape/open-ice`, `ActiveInferenceInstitute/GEO-INFER`, `26d0/vrchat-ime-chat`

### 4. Artifact-trigger heuristics misclassify conventional projects

Instruction-artifact presence in a path (e.g. embedded `AGENTS.md`, `.cursor/rules`, vendored docs) does not imply the repository is an AI product. Conventional software with ancillary instruction files is mislabeled.

**Examples:** `0-AI-UG/cate`, `0xdpfly/gin-app-start`, `AMAP-EAI/Nav-R2`, `ARCLab-MIT/kspdg`

---

## Interpretation

The proposed annotation instrument—consumer test, non-product gate, evidence floor, packaging cues, and runnable-vs-collection rule—**adds information beyond trivial regex baselines**.

Disagreements between instrument labels and baseline predictions identify scientifically informative cases: repositories where AI-instruction artifacts co-occur with ordinary software, end-user AI applications, or non-product content. These are precisely the cases a provenance study must decontaminate before estimating target-population completeness.

---

## Caveats

- **Pilot only; N = 30.** Not powered for definitive κ estimation or prevalence inference.
- **Single annotator round** on this subset (`claude_r2`); no adjudication yet on the pilot batch.
- Baselines cannot emit `EXCLUDE`, structurally inflating apparent agreement on binary splits.
- Must be **repeated on the full gold sample** with independent annotation (two annotators) and adjudication before drawing study-level conclusions.
- Do **not** treat these accuracies as final decontamination performance metrics.

---

## Next steps

1. Complete independent Round 1 annotation by a second annotator on the 30-repo pilot (or full gold sample).
2. Adjudicate disagreements → `adjudicated_label`.
3. Re-run `scripts/evaluate_baseline_heuristics.py` against adjudicated labels.
4. Compute inter-rater agreement via `scripts/compute_annotation_agreement.py`.
5. Apply go/no-go thresholds in `docs/decontamination_study_plan.md`.

---

*Pilot summary only. Not a final empirical report.*
