# Reviewer #2 — Related Work destruction report

**Role:** Hostile but competent IST reviewer. Objective: reject on Related Work alone if possible.  
**Target:** `papers/sections/07_related_work.tex` (pre-fix text audited below).  
**Estimated review comments generated from RW alone:** **42** (24 Major, 12 Minor, 6 Nit).  
**Disposition if RW unchanged:** Reject / Major revision with high reject risk.

---

## A. Overclaims (destroy novelty / honesty)

| # | Location | Overclaim | Why it dies |
|---|---|---|---|
| O1 | Opening L4 | “increasingly forms GitHub corpora by searching for…” | No prevalence study. Grey docs ≠ mining practice. |
| O2 | Opening L6 | Lists doc mirrors/prompt packs/coursework/AI-builder as if known contaminants | Uncited examples; Kalliamvakou/Zimmermann do not study those types. |
| O3 | Opening L10 | “membership checks remain largely implicit” | Absence claimed via Baltes/Promptware/Hou — none audit instruction-file MSR sampling. |
| O4 | L22–23 | Access “largely solved”; membership sentence uncited | Access still incomplete; membership claim needs Baltes/Kalliamvakou on-sentence. |
| O5 | L23 | Runeson cited for retrieval-completeness vs target match | Runeson is case-study guidelines — wrong job. |
| O6 | L33 | Baltes cited for WoC/SWH “membership still author-defined” | Baltes does not analyze WoC/SWH. |
| O7 | L39 | Engineered SDK/prompt/doc/coursework “can survive” RepoReapers/PHANTOM | **Not shown** by Munaiah/PHANTOM/Baltes. Speculative residual sold as fact. |
| O8 | L45 | Frame-wide % without family breakdown “answers the wrong question” | That is *this paper’s* thesis; Chen/Baltes/Dabic do not establish it for instruction families. |
| O9 | L58–59 | Path predicates retrieve wrong *product role*; mismatch “survives” filters | Kalliamvakou ≠ product-role taxonomy; Munaiah ≠ survival proof. |
| O10 | L62 | Cites on “contribution boundary” sentence | Novelty cannot be cited into existence via Kalliamvakou/Baltes/Verdecchia. |
| O11 | L73 | SWE-bench as “benchmark construction insists on scope/filtering” | True-ish but tourist; weak sibling for instruction frames. |
| O12 | L76 | Shepperd/Herbold/Zimmermann → “unvalidated denominators” intuition | Analogy stack; none are denominator-membership papers for path search. |
| O13 | L81 | Practical risk = mix apps with instruction hosts; cites Kalliamvakou+Munaiah+**DéjàVu** | **DéjàVu is duplication, not sample–target mix.** Mis-cite. |
| O14 | L93 | Baltes+Tantithamthavorn prove reporting items “consequential” in instruction frames | They don’t study instruction frames. |
| O15 | L107–108 | “Consensus rule… weakly treated” | Unsupported negative; no measurement-methods survey cited. |
| O16 | L109 | Verdecchia/Baltes support protocol-invariance warning for membership rates | Analogy only. |
| O17 | L115 | LLMs “increasingly” annotators | Prevalence uncited. |
| O18 | L123 | Disagreement “concentrates” at membership boundaries | Anticipates Results; Borges/Kalliamvakou don’t measure that concentration. |
| O19 | L124 | Cohen cited for “human-coded membership protocol whose consensus sensitivity can be measured” | Cohen defines κ, not membership protocols. |
| O20 | L137 | Practice adopts affordances “faster than” methodology audits | Narrative; Hou/Fan/Chen don’t measure adoption lag. |
| O21 | L149 | Ziegler as evidence of “retrieval of repositories that contain instruction artifacts” | Copilot HCI ≠ instruction-file discovery sampling. |
| O22 | L150 | Baltes/Kalliamvakou/Tantithamthavorn as evidence membership “rarely the estimand” in instruction studies | Wrong papers for that survey claim. |
| O23 | L163 | “No verified peer-reviewed study in our search closes jointly” | Search protocol absent from RW — unverifiable. |
| O24 | L184 | “MSR begins to assemble corpora by searching for agent-instruction files” | Same as O1; Promptware ≠ MSR corpus construction. |
| O25 | L185–186 | Family collapse / protocol over-interpretation as established needs | Needs are plausible; cited as if priors already showed the failure mode. |
| O26 | L192 | Self-cite `sanchez2026vsdlcMiningPilot` as contribution support in RW | Circular. |

---

## B. Citations that do not support the sentence (wrong-job cites)

| Sentence gist | Cited | Actual support | Verdict |
|---|---|---|---|
| Contaminants include prompt packs/coursework… bias stats | Kalliamvakou, Zimmermann | General mismatch / cross-project DP | **Fail** for listed types |
| Membership checks largely implicit | Baltes, Promptware, Hou | Sampling guidelines; prompt SE; LLM4SE map | **Fail** as prevalence of missing checks |
| Retrieval completeness ≠ target validity | Runeson | Case-study reporting | **Fail** |
| Coverage leaves membership author-defined (after WoC/SWH) | Baltes | General frames | **Stretch** |
| Survive engineered filters while off-target | Munaiah, PHANTOM, Baltes | Filter objectives / sampling critique | **Fail** as empirical survival |
| Family breakdown is the right question | Dabic, Baltes, Promptware | Sampling/strata ethos; prompt objects | **Fail** for instruction families |
| Wrong product role via path predicates | Kalliamvakou, Baltes | Perils / frames | **Partial fail** |
| Survives toy filters | Munaiah, PHANTOM | Engineeredness | **Fail** |
| Mix apps with instruction hosts | + **Lopes DéjàVu** | Duplication map | **Hard fail** |
| Worksheets consequential in instruction frames | Baltes, Tantithamthavorn | Frames; model-validation sensitivity | **Analogy only** |
| Concentrate disagreement at boundaries | Gilardi, Ahmed, Kalliamvakou, Borges | Annotation caution; GitHub noise | **Fail** for concentration |
| Cohen for consensus-sensitivity protocol | Cohen | κ coefficient | **Fail** |
| Faster than methodology | Hou, Fan, Chen | Surveys of LLM/prompt SE | **Fail** |
| Retrieval typically instrumental | Ziegler + … | Productivity study | **Fail** for Ziegler |
| Membership rarely estimand | Baltes, Kalliamvakou, Tantithamthavorn | Not a survey of instruction studies | **Fail** |
| MSR begins assembling via instruction files | Grey docs + Promptware | Filenames exist; prompt engineering | **Fail** for MSR practice |
| Contribution package cite in RW | sanchez2026… | Own replication package | **Fail** as prior work |

**Count of wrong-job cite instances:** ≥ **22**.

---

## C. Missing citations Reviewer #2 would demand

*(Papers/topics that should appear for an honest RW; presence checked against submission bib where possible.)*

| Missing item | Why R2 asks | In bib? |
|---|---|---|
| Explicit **negative search** protocol (databases, strings, date, hit count) for “no study closes jointly” | Otherwise gap is rhetoric | No |
| Any peer-reviewed study that **does** mine `AGENTS.md` / `.cursor/rules` / Copilot instructions as a corpus (if exists) — or a dated “none found” | O1/O24 | Unknown; not evidenced |
| Residual analysis vs RepoReapers/PHANTOM **on this sample** (Results pointer) | O7 without data is speculation | Results may exist; not in RW |
| Kappa **limitations** / alternative indices (e.g., prevalence/bias adjusted agreement) | You hinge on κ and protocol sensitivity | Not in RW |
| Clearer separation: **population mismatch** vs **label noise** vs **duplication** vs **leakage** with one sentence each and no cross-wiring | L81 DéjàVu abuse | Partial |
| Prefer **Kalliamvakou 2015** alone for substance; drop 2014 stacking | Redundant theatre | Both present |
| Drop or demote **Fan 2023** if Hou 2024 present | Redundant SLR | Both |
| Drop **Fantechi 2023**, **Amershi**, **Storey**, **SWE-bench**, **Herzig** from RW spine | Wrong job / tourist | Present |
| Independent prior on instruction-file **diffusion** (not own Zenodo) | Self-cite `ai_convention…` | Self only |
| Measurement literature on **estimator dependence on aggregation rules** (survey/methods) beyond Tantithamthavorn analogy | O15–O16 | Only analogy |
| IST expectation: Ampatzoglou + Verdecchia already present — good; but don’t cite them for novelty | — | OK |

---

## D. Estimated review-comment load

| Category | n | Examples |
|---|---:|---|
| Major (must fix) | 24 | O1–O10, O13, O20–O24, wrong-job blocks, missing negative search |
| Minor | 12 | Redundant cite stacks, tourist SWE-bench/Herzig, dual Kalliamvakou, Fan+Hou |
| Nit | 6 | “increasingly”, “begins to”, self-cite placement |
| **Total** | **42** | Enough to reject without reading Results |

**One-line R2 summary for AE:**  
*Related Work systematically cites the right grandparents for the wrong grandchildren: Baltes/Kalliamvakou/Munaiah are used as proof of instruction-frame practice, engineered-filter survival, family-strata necessity, and a joint literature gap that the manuscript never shows it searched for.*

---

## E. Paragraphs that must be rewritten (only these)

1. Opening (L4–10)  
2. MSR closing paragraph (L21–24)  
3. Engineered residual paragraph (L35–41)  
4. Operational remainder paragraph (L43–45)  
5. Validity implications paragraph (L57–62)  
6. Contamination practical-risk paragraph (L76–81)  
7. Reporting hinge paragraph (L92–95)  
8. Consensus-rule paragraph (L106–110)  
9. LLM paragraphs (L115–125)  
10. Instruction-artifacts closing (L135–137)  
11. Existing-studies section (L142–152)  
12. Unsolved “no study jointly” lead-in (L163–170)  
13. Why-needed section (L183–193)  

Non-problematic descriptive paragraphs (Hassan/GHTorrent/Howison factual sentences, leakage formalization sentences, Copilot-as-productivity characterization when not over-read) left intact except where listed.

---

*Pre-fix audit. Post-fix text should kill O1–O26 and wrong-job cites without inventing new unverified references.*
