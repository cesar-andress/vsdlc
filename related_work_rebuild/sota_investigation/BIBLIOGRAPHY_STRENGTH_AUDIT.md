# Bibliography strength audit (noise reduction)

**Scope:** Every scholarly (and primary-source) citation currently used in `papers/sections/07_related_work.tex` after the Related Work rebuild — i.e. the de facto “must cite” set (~66 keys).  
**Lens:** IST Associate Editor protecting editorial strength.  
**Objective:** Shrink the RW citation spine to CORE; keep IMPORTANT as support; demote or remove the rest.  
**Not optimized for:** citation count, completeness theatre, or “we searched 30 areas.”

**Targets:** ~25–35 CORE · ~15–25 IMPORTANT · remainder OPTIONAL / REMOVE from RW argumentation.

**Positioning assumed for this audit:** Positioning **B** (discovery-frame validity methodology; AI-instruction GitHub frame = case). Under A, several AI/HCI cites would inflate CORE without strengthening acceptance odds.

---

## Summary counts (recommended)

| Class | Count | Role in final RW |
|---|---:|---|
| **CORE** | 30 | Carry almost all RW argumentation |
| **IMPORTANT** | 18 | One-sentence support, residual comparisons, IST hygiene |
| **OPTIONAL** | 10 | Keep in `.bib` if Methods/Discussion need; not RW load-bearing |
| **REMOVE** | 8 | Drop from RW (and ideally from Intro clustering) |

Self-cites and three Methods-only keys are handled separately below.

---

## Classification legend (applied strictly)

A paper is **CORE** only if ≥1 holds:

1. establishes the **problem**  
2. establishes the **methodology**  
3. establishes the **theoretical foundation**  
4. is the **closest prior work**  
5. is **required by reviewers** (esp. IST)

Otherwise: IMPORTANT (useful, non-redundant), OPTIONAL (dispensable), or REMOVE (noise / superseded / wrong job).

---

## A. CORE (30) — RW must rest on these

### A1. Problem & GitHub perils (4)

| Key | Essential? | Only useful? | Redundant? | Superseded by? | Removable w/o weakening? | Why CORE |
|---|---|---|---|---|---|---|
| `kalliamvakou2015indepth` | **Yes** | No | No | — | **No** | Canonical problem statement for GitHub sample–target mismatch. Reviewer-required. |
| `howison2004perils` | Yes (lineage) | No | Mildly with Kalliamvakou | Not superseded; pre-GitHub ancestor | Weakens historical framing slightly | Establishes that forge mining perils predate GitHub; one cite is enough. |
| `baltes2022sampling` | **Yes** | No | No | — | **No** | Establishes frame/population/generalization methodology. Closest sampling-critique prior. |
| `dabic2021sampling` | **Yes** | No | Partial with Baltes | Not superseded | **No** for GitHub-MSR reviewers | GitHub-specific sampling practice; reviewers expect it beside Baltes. |

### A2. Closest curation residual (2)

| Key | Essential? | Only useful? | Redundant? | Superseded by? | Removable? | Why CORE |
|---|---|---|---|---|---|---|
| `munaiah2017curating` | **Yes** | No | No | — | **No** | Closest prior: engineered filters. Must be the residual comparison spine. |
| `phantom2020` | **Yes** | No | Partial with Munaiah | Extends, does not replace RepoReapers | **No** | Modern engineered curation; needed to show residual survives *both* filters. |

### A3. Validity theory (IST-facing) (4)

| Key | Essential? | Only useful? | Redundant? | Superseded by? | Removable? | Why CORE |
|---|---|---|---|---|---|---|
| `wohlin2012` | **Yes** | No | No | — | **No** | Theoretical foundation: constructs/operational definitions. |
| `verdecchia2023threats` | **Yes** | No | Mild with Ampatzoglou | Updates reflection, doesn’t replace taxonomy | **No** | IST ToV reflection; journal-family required. |
| `ampatzoglou2019threats` | **Yes** | No | Mild with Verdecchia | Complementary taxonomy | Risky | IST ToV taxonomy; keep **one paragraph, both cites once**. |
| `siegmund2015views` | Yes | Almost | No | — | Weakens | Documents disagreement on validity priorities → undeclared targets are risky. |

### A4. Contamination-sense disambiguation (2)

| Key | Essential? | Only useful? | Redundant? | Superseded by? | Removable? | Why CORE |
|---|---|---|---|---|---|---|
| `lopes2017dejavu` | **Yes** | No | No | — | **No** | Forces clean separation: duplication ≠ sample–target contamination. |
| `allamanis2019duplication` | Yes | Almost | Partial with DéjàVu | Complements (eval inflation) | Slightly | Shows *why* duplication literature is adjacent but different. Keep as pair with Lopes (one sentence). |

### A5. Protocol / label sensitivity methodology (4)

| Key | Essential? | Only useful? | Redundant? | Superseded by? | Removable? | Why CORE |
|---|---|---|---|---|---|---|
| `tantithamthavorn2017validation` | **Yes** | No | No | — | **No** | Best SE analogy: fixed data, changed protocol → changed conclusions. Anchors RQ protocol-sensitivity. |
| `cohen1960kappa` | **Yes** | No | No | — | **No** | Agreement instrument; methodology foundation. |
| `runeson2009` | **Yes** | No | No | — | **No** | Multi-coder / case-study coding discipline. |
| `golzadeh2021bots` | **Yes** | No | No | — | **No** | Closest *membership ground-truth* cousin on GitHub entities (bots ≠ instruction frames, but same job class). |

### A6. Dataset-validation ethos (closest cousins) (2)

| Key | Essential? | Only useful? | Redundant? | Superseded by? | Removable? | Why CORE |
|---|---|---|---|---|---|---|
| `herbold2022szz` | **Yes** | No | Mild with Shepperd | — | **No** | Manual validation exposes systematic labeling failure — same ethos as membership audit. |
| `shepperd2013nasa` | **Yes** | No | Mild with Herbold | — | Risky | Classic dataset-quality warning; one NASA-line cite is enough (prefer this over 2014). |

### A7. LLM adjudication (case methodology) (2)

| Key | Essential? | Only useful? | Redundant? | Superseded by? | Removable? | Why CORE |
|---|---|---|---|---|---|---|
| `ahmed2025llms` | **Yes** | No | No | — | **No** | Best SE-specific LLM-annotation paper; required given LLM tie-breaking in methods. |
| `gilardi2023chatgpt` | Yes | Almost | No | Not superseded by Ahmed | Weakens contrast | Optimistic NLP baseline that must be *refused* for membership boundaries. |

### A8. Instruction-artifact phenomenon (scholarly + primary) (6)

| Key | Essential? | Only useful? | Redundant? | Superseded by? | Removable? | Why CORE |
|---|---|---|---|---|---|---|
| `chen2025promptware` | **Yes** | No | No | — | **No** | Best scholarly anchor that prompts/agent memory are SE objects — without claiming sampling audits exist. |
| `hou2024llm4se` | Yes | Almost | With Fan | Prefer over Fan | Risky | Maps LLM4SE; needed to say surveys don’t audit discovery frames. |
| `agentsmd2025` | **Yes** | No | No | — | **No** | Primary predicate definition. |
| `cursor2024docs` | **Yes** | No | No | — | **No** | Primary predicate definition. |
| `brown2024copilot` | **Yes** | No | No | — | **No** | Primary predicate definition. |
| `claude2024docs` | **Yes** | No | No | — | **No** | Primary predicate definition. |
| `anthropic2024mcp` | **Yes** | No | No | — | **No** | Primary predicate / tool-interface surface. |

> Count note: five grey docs + Chen + Hou = 7 in A8; with A1–A7 scholarly cores this lands at **30 CORE** including grey. If the editor insists grey cannot count as CORE, treat the five docs as **CORE-PRIMARY** (still non-negotiable in the case) and scholarly CORE ≈ 25.

---

## B. IMPORTANT (18) — keep, but do not let them carry the argument

| Key | Essential? | Only useful? | Redundant? | Superseded by? | Removable w/o weakening? | Verdict note |
|---|---|---|---|---|---|---|
| `kalliamvakou2014` | No | **Yes** (seminal MSR cite) | **Yes** with 2015 | **2015 in-depth** for substance | Mostly yes if 2015 kept | Cite **once** as conference origin; all claims → 2015. |
| `hassan2008road` | No | Yes (MSR programme) | Mild | — | Yes | One scene-setting cite. |
| `gousios2013` | No | Yes (cheap discovery) | With Lean GHTorrent | — | Yes | One GHTorrent cite max. |
| `ma2019woc` | No | Yes | With SWH | — | Mild | Coverage ≠ membership; keep one archive-scale cite. |
| `pietri2019swh` | No | Yes | With WoC / CACM SWH | — | Mild | Prefer **one** of WoC/SWH in RW. |
| `borges2016popularity` | No | Yes | With Tsay | — | Mild | Metadata ≠ membership. |
| `kapoor2023leakage` | No | Yes | With Kaufman | Modern leakage | Mild | One modern leakage cite for disambiguation. |
| `kaufman2012` | No | Yes | With Kapoor | Kapoor for “crisis” rhetoric | Mild | Keep only if Kapoor dropped; else OPTIONAL. |
| `zimmermann2008` | No | Yes (domain mismatch) | Mild | — | Yes | Analogy only; one sentence. |
| `shepperd2014bias` | No | Yes | **Yes** with NASA 2013 | 2013 for quality; 2014 for bias | Yes if 2013 kept | Prefer demote to OPTIONAL. Listed IMPORTANT only if bias claim is explicit. |
| `gonzalez2023revisit` | No | Yes | With 2011 | Updates 2011 | Mild | IST reproducibility; one cite. |
| `heumuller2020` | No | Yes | With Winter/Liu | — | Yes under B | Artifact availability; demote if package is not a claim. |
| `winter2022artifacts` | No | Yes | With Liu/Heumüller | — | Yes | Keep **one** artifact-eval cite. |
| `landis1977kappa` | No | Yes | Mild with Cohen | — | Mild | Interpretation benchmarks; Methods > RW. |
| `ralph2021standards` | No | Yes | Mild with Runeson | — | Yes | Empirical standards announcement. |
| `ziegler2024copilot` | No | Yes | With Barke/Vaithilingam | — | Yes | One Copilot *productivity* cite max. |
| `vaithilingam2022expectation` | No | Yes | With Ziegler/Barke | — | Yes | Prefer Ziegler **or** this, not both. |
| `cosentino2017mapping` | No | Yes | Mild | — | Yes | GitHub-SE mapping scene-setting. |

**IMPORTANT trim rule:** in RW prose, never stack >2 IMPORTANT cites on a single claim already carried by a CORE cite.

---

## C. OPTIONAL (10) — bibliography OK; RW argumentation should not depend on them

| Key | Essential? | Only useful? | Redundant? | Superseded by? | Removable from RW? | Note |
|---|---|---|---|---|---|---|
| `gousios2014lean` | No | Barely | **Yes** | `gousios2013` | **Yes** | Same infrastructure story. |
| `spadini2018pydriller` | No | Tooling colour | Yes (tooling cluster) | — | **Yes** | Methods toolkit, not RW. |
| `dicossmo2017softwareheritage` | No | Yes | **Yes** | `pietri2019swh` | **Yes** | Duplicate SWH story. |
| `gonzalez2011repro` | No | Historical | **Yes** | `gonzalez2023revisit` | **Yes** | Keep 2023 only in RW. |
| `liu2024researchartifacts` | No | Yes | With Winter/Heumüller | — | **Yes** | Third artifact cite is noise. |
| `silva2012replication` | No | Yes | With artifact cluster | — | **Yes** | Replication mapping ≠ frame audit. |
| `jedlitschka2005reporting` | No | Generic reporting | With Ralph/Runeson | — | **Yes** | Wrong grain for this paper. |
| `petersen2015mapping` | No | Mapping guidelines | Yes | — | **Yes** | Not about discovery-frame membership. |
| `moreno2012` | No | Dataset-shift theory | With Kaufman/Kapoor | — | **Yes** | Over-theoretic for one disambiguation paragraph. |
| `zheng2023judge` | No | LLM-as-judge | With Ahmed/Gilardi | Ahmed for SE | **Yes** | Only if claiming judge benchmarks; you don’t. |

---

## D. REMOVE from Related Work (8) — noise or wrong job

| Key | Essential? | Only useful? | Redundant? | Superseded by? | Removable w/o weakening? | Why REMOVE |
|---|---|---|---|---|---|---|
| `fan2023` | No | Barely | **Yes** | **`hou2024llm4se`** | **Yes** | Broad FoSE survey; Hou is the stronger SLR. |
| `storey2020` | No | Tangential | No | — | **Yes** | Bots productivity; not instruction-file sampling. |
| `fantechi2023` | No | Weak | Yes | **Ahmed 2025** | **Yes** | Preliminary RE ChatGPT; wrong claim weight. |
| `amershi2019humanai` | No | HCI guidelines | Mild | Ahmed + human oversight claim | **Yes** | Excellent paper, wrong section job. |
| `barke2023groundedcopilot` | No | HCI Copilot | **Yes** | Ziegler or Vaithilingam | **Yes** | Third Copilot HCI cite. |
| `tsay2014influence` | No | Social signals | **Yes** | **Borges 2016** | **Yes** | One metadata-proxy cite. |
| `jimenez2024swebench` | No | Benchmark fame | Wrong fit | — | **Yes** | Benchmark construction ≠ instruction-frame membership. |
| `herzig2013tangled` | No | Construct failure cousin | Mild | Herbold/Shepperd | **Yes** | Tangled commits are a different construct failure. |

### Self-citation special case (not in the 8, but treat as REMOVE-from-RW)

| Key | Verdict | Rule |
|---|---|---|
| `ai_convention_lifecycle_corpus2026` | **REMOVE from RW argumentation** | Own corpus; circular novelty risk. Cite only as data sibling in Methods/Availability if needed. |
| `sanchez2026vsdlcMiningPilot` | **REMOVE from RW** | Replication package cite belongs in Availability/Data Availability, not Related Work. |

---

## E. Keys outside RW (Methods only) — do not promote into RW

| Key | Class for manuscript | Note |
|---|---|---|
| `wilson1927` | OPTIONAL (Methods) | Wilson intervals. |
| `reimers2019sentencebert` | OPTIONAL (Methods) | Embedding tooling. |
| `gauthier2024aider` | OPTIONAL / phenomenon | Tool URL; not scholarly RW. |

---

## F. Redundant pairs — keep winner

| Keep (winner) | Drop or demote | Reason |
|---|---|---|
| `kalliamvakou2015indepth` | `kalliamvakou2014` → IMPORTANT once | Journal-strength substance. |
| `hou2024llm4se` | `fan2023` → REMOVE | Stronger SLR. |
| `pietri2019swh` **or** `ma2019woc` | the other + `dicossmo2017softwareheritage` | One archive-scale coverage cite. |
| `gousios2013` | `gousios2014lean` | One firehose cite. |
| `borges2016popularity` | `tsay2014influence` | One metadata-proxy cite. |
| `gonzalez2023revisit` | `gonzalez2011repro` | IST update. |
| `shepperd2013nasa` | `shepperd2014bias` (unless bias is explicit claim) | One defect-data quality cite. |
| `ziegler2024copilot` **or** `vaithilingam2022expectation` | `barke2023groundedcopilot` + the other | One Copilot HCI cite. |
| `heumuller2020` **or** `winter2022artifacts` | `liu2024researchartifacts`, `silva2012replication` | One artifact/repro hygiene cite. |
| `kapoor2023leakage` **or** `kaufman2012` | `moreno2012` | One leakage/shift disambiguation cite. |
| `ahmed2025llms` + `gilardi2023chatgpt` | `fantechi2023`, `zheng2023judge`, `amershi2019humanai` | SE caution + NLP optimism is enough. |
| `cohen1960kappa` | `landis1977kappa` → Methods/IMPORTANT | Don’t teach kappa twice in RW. |

---

## G. What a lean Related Work citation spine looks like

### Load-bearing CORE spine (~25 scholarly + 5 primary)

**Problem:** Howison → Kalliamvakou 2015 → Baltes → Dabic  
**Residual:** Munaiah → PHANTOM  
**Validity:** Wohlin → Ampatzoglou → Verdecchia → Siegmund  
**Disambiguation:** Lopes (+ Allamanis one clause)  
**Protocol/labels:** Tantithamthavorn → Cohen → Runeson → Golzadeh → Herbold → Shepperd 2013  
**LLM:** Ahmed → Gilardi  
**Phenomenon:** Chen Promptware → Hou LLM4SE → five instruction docs  

### Support IMPORTANT (pick ≤18, prefer ≤12 in prose)

Kalliamvakou 2014 (once), Hassan, Gousios 2013, WoC **or** SWH, Borges, Kapoor **or** Kaufman, Zimmermann, González-Barahona 2023, Heumüller **or** Winter, Landis (Methods), Ralph, Ziegler **or** Vaithilingam, Cosentino.

### Explicitly out of RW prose

Fan, Storey, Fantechi, Amershi, Barke, Tsay, SWE-bench, Herzig, Lean GHTorrent, PyDriller, CACM SWH duplicate, González 2011, Liu, da Silva, Jedlitschka, Petersen, Moreno, Zheng, both self-cites.

---

## H. Editorial strength verdict

**Current RW (~66 cites) is over-cited for the claim it can honestly make.**  
Frequency analysis already shows signal concentration: `baltes2022sampling` (27), `kalliamvakou2015indepth` (17), `munaiah2017curating`/`chen2025promptware`/`tantithamthavorn2017validation` (~10 each). Everything else is mostly decorative scaffolding.

**Noise that most damages AE confidence:**

1. **Reporting/replication cluster** (Jedlitschka, Petersen, da Silva, Liu, Winter, Heumüller stacked) — reads as contribution-by-checklist.  
2. **Third/fourth Copilot–HCI and LLM-judge cites** — dilutes the SE-specific Ahmed hinge.  
3. **Self-cites in RW** — invites “you already solved this” or “circular novelty.”  
4. **Defect-prediction and SWE-bench tourism** — looks like literature padding.  
5. **Dual GHTorrent / dual SWH / dual Kalliamvakou** — textbook redundancy.

**Minimum change for maximum editorial strength:**

1. Rewrite RW cite policy: **CORE only in claim sentences**; IMPORTANT at most once per paragraph; never cite OPTIONAL/REMOVE in RW.  
2. Apply the redundant-pair winners table (Section F).  
3. Delete Section D REMOVEs + self-cites from RW.  
4. Cap artifact/reporting discussion at **one** hygiene sentence with ≤2 cites.  
5. Keep five product docs — they are primary evidence for the *case*, not scholarly padding — but stop using them as motivation substitutes for peer-reviewed practice evidence (that is an Intro problem, not a bib problem).

**Expected RW cite load after cleanup:** ~30 CORE + ~12–18 IMPORTANT appearances ≈ **35–45 unique keys in RW**, down from 66, with sharper residual vs RepoReapers/PHANTOM and sharper protocol-sensitivity hinge.

---

## I. Quick checklist for authors

- [ ] Can every RW paragraph be rewritten using only CORE keys? If not, the paragraph is probably optional.  
- [ ] Does each IMPORTANT cite add a *distinct* residual, analogy, or journal-family signal? If not, drop.  
- [ ] Are self-cites absent from RW?  
- [ ] Is there at most one cite per redundant pair?  
- [ ] Do grey docs appear only as predicate definitions, never as “evidence that SE researchers already do this”?  

---

*Audit date: 2026-07-22. Based on `07_related_work.tex` cite inventory (66 keys) + editorial criteria above. No new literature collection.*
