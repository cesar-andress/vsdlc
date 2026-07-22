# References to remove or demote from the current manuscript

Scope: citations currently used in `papers/sections/07_related_work.tex` (and weak RW uses elsewhere).  
Criterion: outdated for the claim, weak venue for the claim, redundant with a stronger verified source, wrong conceptual fit, or previously flagged INVALID in the forensic audit.

## A. Remove from Related Work argumentation (keep elsewhere only if methods need them)

| Key | Reason |
|---|---|
| `cook1979_quasiexperimentation` | Classic quasi-experimentation text; too generic for a GitHub-frame contamination argument. Prefer Verdecchia 2023 / Ampatzoglou 2019 / Wohlin 2012 for validity discourse. |
| `fantechi2023` | Preliminary RE inconsistency detection with ChatGPT; weak support for mining-frame validity or annotation-protocol claims. Prefer Ahmed 2025 + Gilardi 2023 if LLM annotation is discussed. |
| `amershi2019humanai` | Excellent HCI paper; only loosely related to repository-frame auditing. Demote to a single optional citation in annotation design, or remove from RW. |
| `storey2020` (Storey & Zagalsky 2016) | Bots productivity keynote-style paper; tangential to instruction-file discovery contamination. |
| `cheng2026_genai_re` | GenAI-for-RE SLR; does not speak to GitHub sampling validity. Keep only if Discussion links to RE tooling, not in core RW. |
| `fan2023` | Broad FoSE survey; redundant with Hou 2024 for LLM4SE mapping. Keep at most one of Fan/Hou in RW. |
| `reimers2019sentencebert` | Tool citation for embeddings/baselines; not Related Work substance. |
| `wilson1927` | Wilson score intervals; methods/statistics, not RW. |
| `gauthier2024aider` | Product/tool site; acceptable in Background as phenomenon, not as scholarly RW evidence. |
| `kaufman2012` **if used as “repository contamination”** | Correct paper for *train/test leakage*, but easy to over-claim. Keep only when disambiguating contamination senses; otherwise replace with Kalliamvakou / Munaiah for sample composition. |
| `moreno2012` **if used as MSR contamination** | Dataset-shift theory paper; keep only in the disambiguation paragraph. |
| `dambros2012defectbenchmark` **if used as GitHub sampling** | Defect-prediction benchmark; keep for dataset-validation cousin, not for instruction-frame discovery. |
| `tantithamthavorn2017validation` **if used as sampling bias** | Model-validation sensitivity; keep for protocol-sensitivity analogy only. |
| `jimenez2024swebench` | Strong benchmark paper; only weakly related unless discussing benchmark construction/filtering. Optional in datasets cluster. |
| `ai_convention_lifecycle_corpus2026` | Own prior Zenodo corpus with adoption/maintenance framing; citing it heavily in RW risks circular novelty. Cite sparingly as phenomenon/data sibling, not as methodological predecessor that already solved contamination auditing. |

## B. Already INVALID / must not return (forensic audit)

These were previously withdrawn; do **not** reintroduce:

- `baltes2022replication` (hallucinated)
- `bird2020` (hallucinated chapter)
- `fucci2018` (unverifiable)
- `gottschalk2023` (unverifiable ASE paper)
- `hempel2020reproducibility` (DOI pointed to wrong article)
- `herbold2020` (DOI pointed to wrong article)

## C. Redundant pairs — keep the stronger one

| Weaker / redundant | Prefer |
|---|---|
| Kalliamvakou MSR 2014 alone | Add **Kalliamvakou EMSE 2015/16** in-depth study; keep MSR for seminal conference impact |
| Fan 2023 + Hou 2024 both as long surveys | Prefer **Hou 2024 TOSEM** as primary SLR; optional short Fan cite |
| da Silva 2014 + Heumüller 2020 + Liu 2024 + Winter 2022 all in one sentence | Keep **2**: Heumüller (artifact availability) + Winter or Liu (evaluation trends); move da Silva to replication mapping |
| Cohen + Landis both explained in RW | Keep in Methods; mention once in RW annotation paragraph |

## D. Product docs — keep, but label as primary sources

Do **not** remove `agentsmd2025`, `cursor2024docs`, `claude2024docs`, `brown2024copilot`, `anthropic2024mcp`.  
They are necessary phenomenon evidence. Update Cursor URL to `https://cursor.com/docs/rules` (old docs.cursor.com path redirects).
