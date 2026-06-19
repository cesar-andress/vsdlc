# Decontamination validation study plan

**Version:** 0.2 (final instrument)  
**Repository:** `vsdlc/vsdlc`  
**Related:** `~/papers/vsdlc/docs/classification_schema.md`, `docs/annotation_protocol.md`

---

## 1. Motivation

Before provenance reconstruction, validate that the eligible population can be **decontaminated**: separate `CONVENTIONAL_SOFTWARE` (target) from `AI_PRODUCT` and `EXCLUDE`.

The v0.1 four-class schema (`TOOL` / `ASSIST` / `MIXED` / `UNCLEAR`) is **deprecated for primary analysis** and retained only as optional secondary tagging or audit notes—not as `primary_label`.

---

## 2. Primary instrument (3 labels)

| `primary_label` | Role in study |
|-----------------|---------------|
| `CONVENTIONAL_SOFTWARE` | **Target population** for provenance |
| `AI_PRODUCT` | Non-target (AI-system product) |
| `EXCLUDE` | Non-target (out of scope / insufficient evidence) |

**Decision flow:** Steps 0–5 in `classification_schema.md` §4 (non-product gate → evidence floor → consumer test → packaging → runnable-vs-collection → AI-central app rule).

**Secondary tags (optional):** `NON_PRODUCT`, `INSUFFICIENT_EVIDENCE`, `DUAL_REVIEW`, `BENCHMARK_OR_EVAL`, `PROMPT_COLLECTION`, `AI_SECURITY_LAB`, `AI_CENTRAL_END_USER_APP`, `RUNNABLE_PROMPT_TOOL`, `DOTFILES`, `DOCS_ONLY`

---

## 3. Sampling plan

- Input: `data/interim/eligible_repos.jsonl`
- Gold sample: `scripts/create_gold_sample.py` → `data/processed/gold_sample_repos.csv` (≤120)
- Metadata: `scripts/backfill_metadata.py` (optional)

Gold CSV = template fields + `agent_product_flag` + `sample_stratum`; annotation columns empty.

---

## 4. Annotation plan

1. Train on protocol + schema Steps 0–5 + `annotation_example.json`
2. Independent Round 1 (annotators A, B): `primary_label`, optional `secondary_tags`
3. Adjudicate disagreements → `adjudicated_label`
4. Ignore `agent_product_flag` when labeling

---

## 5. Agreement metrics

`scripts/compute_annotation_agreement.py` → `data/processed/annotation_agreement.json`

| Metric | Definition |
|--------|------------|
| Three-class κ | `primary_label`: `AI_PRODUCT`, `CONVENTIONAL_SOFTWARE`, `EXCLUDE` |
| Binary κ | `target_population` = `CONVENTIONAL_SOFTWARE`; `non_target` = `AI_PRODUCT` ∪ `EXCLUDE` |
| Confusion matrix | Both schemes |
| Disagreements | Mismatched `primary_label` |
| Warnings | Legacy `label` column detected |

---

## 6. Go / no-go

**Continue** if: κ ≥ 0.60 (3-class) or κ ≥ 0.70 (binary); ≥30 `CONVENTIONAL_SOFTWARE`; ≥10 `CONVENTIONAL_SOFTWARE`.

**Pivot** if: `CONVENTIONAL_SOFTWARE` < 10% after adjudication.

**Stop** if: κ < 0.50 after schema revision and re-annotation.

---

## 7. Commands

```bash
cd ~/papers/vsdlc/vsdlc
python3.11 scripts/compute_annotation_agreement.py \
  --annotator-a data/processed/gold_sample_annotator_a.csv \
  --annotator-b data/processed/gold_sample_annotator_b.csv \
  --output data/processed/annotation_agreement.json
```

---

*No provenance completeness rates until go decision.*
