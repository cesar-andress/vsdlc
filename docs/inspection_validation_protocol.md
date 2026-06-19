# Metadata vs repository inspection — validation protocol

**Inputs:** `data/processed/inspection_sample_50_blank.csv`  
**Reference (held out during inspection):** `data/processed/inspection_sample_50.csv`  
**Completed worksheet:** `data/processed/inspection_sample_50_completed.csv`  
**Schema:** `~/papers/vsdlc/docs/classification_schema.md` (v0.2)

---

## Purpose

Test whether labels derived from repository **metadata** (description, topics, detected instruction artifacts, CI/release evidence) and prior annotator passes are consistent with labels obtained after **inspecting repository-level evidence** that reflects repository reality, not only README prose.

The inspector works from the blind worksheet and must not use prior annotator labels.

---

## Functional evidence requirement

Inspection must validate **repository reality**, not only richer metadata or README claims.

Inspectors must inspect **at least two** of the following evidence sources **when available**:

1. **README or landing page**
2. **File tree / repository structure**
3. **Dependency or manifest files**
   - `package.json`
   - `pyproject.toml`
   - `requirements.txt`
   - `go.mod`
   - `Cargo.toml`
   - `pom.xml`
   - `csproj`
   - etc.
4. **Entrypoints or executable modules**
   - `src/`
   - `app/`
   - `main.*`
   - `cli/`
   - `server/`
   - `packages/`
5. **Prompt/agent/instruction artifacts and how they are consumed by code**

The inspector must record **one sentence of functional evidence** in `functional_evidence`, for example:

- `package.json exposes a CLI for MCP server tooling`
- `src/app implements a desktop writing application; prompts are internal assets`
- `repository is docs-only; no executable source found`

`inspection_evidence` may still summarize the overall inspection, but `functional_evidence` must cite concrete repository function or absence of executable product evidence.

---

## Procedure

For each repository row in `inspection_sample_50_blank.csv`:

1. **Open the repository URL** (`repo_url`) in a browser.
2. **Inspect available evidence sources** from the list above until at least two are covered when present in the repository.
3. **Decide one primary label** using the same 3-label instrument:

| Code | Definition |
|------|------------|
| `AI_PRODUCT` | Primary consumers build, evaluate, operate, secure, or orchestrate AI systems |
| `CONVENTIONAL_SOFTWARE` | Primary consumers are end users or non-AI developers; AI may be internal or a core feature |
| `EXCLUDE` | Non-product, dotfiles, docs-only, prompt packs, courses, awesome lists, insufficient evidence |

4. **Do not consult** `majority_label`, `claude_label`, `human1_label`, or `human2_label`. Those columns are absent from the blind worksheet by design.
5. **Record evidence:**
   - `functional_evidence`: one sentence of functional repository evidence (required)
   - `inspection_evidence`: optional overall inspection summary
6. **Mark inspected evidence sources** as `true` or `false`:
   - `inspected_readme`
   - `inspected_file_tree`
   - `inspected_dependencies`
   - `inspected_entrypoints`
   - `inspected_instruction_consumption`
7. Optionally set:
   - `inspection_confidence`: `high`, `medium`, or `low`
   - `inspection_notes`: free-text audit notes (disagreements, edge cases, follow-up)

Save the completed file as `data/processed/inspection_sample_50_completed.csv` with the same `repo_full_name` values and column order as the blank worksheet, with `inspection_label` filled for every row.

---

## Second independent inspector (same $n{=}50$ sample)

A second functional-evidence inspector can reassess the **same 50 repositories** under the same codebook without seeing prior labels.

**Blank worksheet:** `data/processed/inspection_sample_50_second_inspector_blank.csv`  
**Completed worksheet:** `data/processed/inspection_sample_50_second_inspector_completed.csv`

Generate the blank worksheet:

```bash
cd ~/papers/vsdlc/vsdlc
PYTHONPATH=src python3 scripts/create_second_inspector_blank.py
```

The second inspector must **not** consult:
- `majority_label`, `claude_label`, `human1_label`, `human2_label`
- inspector~1 fields (`inspection_label`, `functional_evidence`, etc.)

Allowed worksheet context matches inspector~1: repository URL, description/topics/language, matched-path provenance, CI/release evidence.

For each repository row:

1. Open `repo_url` and inspect at least two evidence sources when available (same source list as above).
2. Record:
   - `inspector2_label`: one of `AI_PRODUCT`, `CONVENTIONAL_SOFTWARE`, `EXCLUDE`
   - `inspector2_functional_note`: one sentence of functional repository evidence (required)
   - `inspector2_evidence_sources`: comma- or pipe-separated tokens from `readme`, `file_tree`, `dependencies`, `entrypoints`, `instruction_consumption`
   - `inspector2_confidence`: optional `high`, `medium`, or `low`
   - `inspector2_free_notes`: optional audit notes

Validate and evaluate after completion:

```bash
PYTHONPATH=src python3 scripts/validate_second_inspection.py
PYTHONPATH=src python3 scripts/evaluate_second_inspection.py
```

See `docs/reproducibility.md` for output artifacts and metric definitions.

---

## Evaluation

After inspection is complete, run:

```bash
cd ~/papers/vsdlc/vsdlc
PYTHONPATH=src python3.11 scripts/evaluate_inspection_validation.py
```

Metrics written to `data/processed/inspection_validation_results.json`:

- Agreement between `majority_label` (metadata-derived consensus) and `inspection_label`
- Cohen's kappa (three-class)
- Confusion matrix
- Disagreement list
- Agreement by class
- EXCLUDE vs non-EXCLUDE agreement
- AI_PRODUCT vs CONVENTIONAL_SOFTWARE agreement excluding EXCLUDE cases
- Functional-evidence compliance warnings

Evaluation warns when:

- `functional_evidence` is missing for a completed row
- fewer than two evidence-source booleans are `true`

---

## Constraints

- Do not fabricate inspection labels or evidence.
- Use repository-level inspection; metadata columns in the worksheet are sampling context, not a substitute for opening the URL and checking manifests, entrypoints, and code consumption.
- Running example for the wider V-SDLC paper remains **CSRCS** only; this validation study uses the mined GitHub sample.
