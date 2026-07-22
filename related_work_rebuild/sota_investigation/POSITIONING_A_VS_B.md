# Scientific repositioning decision

**Scope:** Full manuscript read; current framing ignored for the decision.  
**Task:** Choose A vs B; if B, redesign positioning without rewriting the manuscript.  
**Date:** 2026-07-22

---

## Decision

**Choose B.**

Present the paper as:

> **A reusable methodology for auditing discovery-frame validity in Mining Software Repositories**,  
> **demonstrated on one GitHub frame formed by AI-instruction path predicates.**

Do **not** present it as primarily “AI instruction artifact research.”

---

## Why B is stronger than A

### What the manuscript actually *measures*

The empirical payload is not about how agents behave, how prompts are engineered, or how Copilot changes productivity. The RQs measure:

| RQ | Scientific object | Generality |
|---|---|---|
| RQ1 | Sensitivity of a **membership/contamination prevalence** to **consensus protocol** and **target collapse** | General MSR measurement validity |
| RQ2 | Whether misalignment is **uniform** or **structured by discovery-predicate family** | General for heterogeneous discovery frames |
| RQ3 | Where coder disagreement concentrates (**membership boundary** vs role) | General annotation/validity |
| RQ4 | Concordance of metadata consensus vs functional inspection | General label-validation |

Those are classical MSR/ESE validity objects. The AI-instruction filenames are the **instrument that builds the frame**, not the scientific phenomenon under study.

### What A would force the paper to be

Under A, referees will ask for:
- theory of instruction artifacts / promptware,
- comparison to Copilot interaction studies,
- adoption/lifecycle claims,
- evidence that “the field already samples this way” at scale.

The manuscript does not deliver those. The AE desk assessment already flagged that failure. Keeping A makes the paper look like a thin AI-SE trend paper with a methods appendix.

### What B aligns with

Under B, the paper sits next to:
- Kalliamvakou (GitHub sample ≠ claimed population),
- Baltes & Ralph (frames/populations must be declared),
- Munaiah/PHANTOM (curation solves a *different* membership construct),
- Herbold/Golzadeh (manual validation / membership ground truth),
- Tantithamthavorn (methodological choice can move conclusions).

The distinctive claim becomes:

> Discovery-frame validity is not settled by retrieval success or engineered filters. When inclusion is predicate-based and membership is coder-mediated, **prevalence is an estimand**: it depends on analytic target, predicate-family composition, and consensus protocol. We provide an audit methodology and demonstrate those dependencies on one public frame.

That is narrower than “a complete MSR sampling theory,” but stronger than “AI instruction artifacts.”

### Honesty constraint (do not overclaim B either)

B is stronger **only if** claims stay at:

- methodology + demonstration on one case,  
not  
- universal constants for all MSR, or  
- replacement for RepoReapers / Baltes guidelines.

The Threats section already says counts are frame-specific. The positioning must match that humility.

---

## Redesigned scientific positioning (B)

### One-sentence positioning

This paper contributes a **discovery-frame validity audit** for MSR: a discover → filter → annotate → inspect protocol that treats contamination as target-conditional sample–target mismatch and reports prevalence under complementary consensus protocols and predicate-family strata; AI-instruction file search on GitHub is the motivating empirical case.

### Title direction (conceptual; not a rewrite)

Prefer titles of the form:
- “Auditing Discovery-Frame Validity in Repository Mining: Protocol Sensitivity and Predicate Structure”
- “When Retrieval Is Not Membership: A Validity Audit for Predicate-Based GitHub Frames”

Avoid titles that foreground “AI-Instruction Artifacts” as the object of knowledge.

### Contribution hierarchy under B

1. **Primary:** Measurement findings about discovery-frame validity (protocol sensitivity; family structure; boundary disagreement; target-conditionality).  
2. **Primary-supporting:** Operational audit protocol (phases, worksheet pattern separating membership vs role relative to a declared target).  
3. **Derived:** Reporting recommendations for predicate-based discovery studies.  
4. **Case vehicle:** AI-instruction predicates instantiate a heterogeneous, path-based discovery frame that is currently salient and hard to police with engineered-only filters.

### How AI instruction artifacts become *only* the motivating case

| Role of AI-instruction artifacts | Under current A framing | Under proposed B framing |
|---|---|---|
| Scientific object | Central (“instruction-artifact research”) | Peripheral (“one discovery regime”) |
| Why chosen | Implied as the topic | Explicit selection criteria: path-based predicates; heterogeneous families; membership not reducible to engineeredness; coder-mediated labels |
| What generalizes | “Guidance for instruction-artifact frames” | “Audit checks for predicate-based discovery frames” |
| What stays case-specific | Filenames, CONV/AI_PRD codebook labels, 2024+ window | Same—clearly labeled as case schema / case window |
| Grey literature (AGENTS.md, Cursor, Copilot docs) | Motivation spine | Brief case justification only |

**Selection criteria to state once (Intro):**  
We needed a discovery frame where (i) inclusion is a search predicate, (ii) predicates are heterogeneous by design, (iii) ordinary engineered/activity filters are unlikely to remove all off-target mass, and (iv) membership judgments are metadata-mediated. AI-instruction path predicates satisfy those criteria today; the audit targets the criteria, not the AI topic per se.

### Non-claims under B (state explicitly)

- Not a theory of agents, prompts, or coding assistants.  
- Not a claim that all MSR must use instruction-file discovery.  
- Not a replacement for engineered-project curation.  
- Not a universal contamination rate for GitHub.  
- Not “AI instruction artifact research” except as case context.

---

## Section-by-section change list

*(Redesign only — no manuscript rewrite in this task.)*

### Front matter / packaging

| Artifact | Change needed |
|---|---|
| **Title** | Reframe to discovery-frame validity / predicate-based sampling audit; demote AI-instruction to subtitle or omit. |
| **Abstract** | Lead with discovery-frame validity problem; introduce AI-instruction predicates as the case frame in sentence 2–3; end with transferable audit checks, not “instruction-artifact reporting.” |
| **Keywords** | Prefer: mining software repositories; sampling validity; discovery frames; construct validity; inter-rater / consensus; reproducibility. Keep “AI” only if needed as secondary. |
| **Highlights** | Rewrite bullets around protocol sensitivity / family structure / membership-boundary disagreement / reusable audit; AI-instruction only as case mention if character budget allows. |
| **Cover letter** | Sell B positioning to IST methods track; case = instruction-file GitHub frame. |

### Section 1 — Introduction

| Change | Intent |
|---|---|
| Open on **MSR discovery-frame validity** (retrieval ≠ membership), not on AGENTS.md. | Make B the thesis. |
| Insert a short **case justification** paragraph: why this frame was chosen (criteria above). | AI becomes vehicle. |
| Replace “instruction-file adoption work” as gap partner with **sampling/curation/validity** lineage (Baltes, Kalliamvakou, Munaiah). | Stop A-shaped gap. |
| Reorder contributions: findings first; protocol second; reporting derived; case last. | Match B hierarchy. |
| Retarget RQs linguistically: “in a predicate-based discovery frame (case: AI-instruction paths)…” | RQs stay empirically identical, framing generalizes. |
| Soften/remove “MSR convention” contamination wording; define as target-conditional membership error. | Terminology hygiene. |

### Section 2 — Background and Motivation

| Change | Intent |
|---|---|
| Reframe as **design problems of discovery-frame audits** (frame vs target; heterogeneous predicates; consensus as estimand). | General methodology. |
| Move AI-instruction specificity to “Case setting” subsection or final paragraph. | Case demotion. |
| Keep target-conditionality and protocol-dependence as general principles illustrated by the case. | Preserve scientific core. |

### Section 3 — Related Work

| Change | Intent |
|---|---|
| Re-center clusters on MSR sampling validity; shorten AI-instruction / Copilot / Promptware to one case-motivation subsection. | Stop looking like AI-SE survey. |
| Cut or shrink LLM-annotation subsection unless tied to “third-coder sensitivity” as a **general** consensus-protocol issue. | Avoid A-topic drift. |
| Keep engineered-curation contrast as central “false friend.” | Strongest B differentiation. |
| Rewrite “existing studies using AI instruction artifacts” → “why path-predicate frames are a timely stress test” (short). | Case, not literature object. |
| Restate unsolved problem as: **auditing predicate-based discovery frames for target-conditional membership error under consensus and family structure.** | B gap statement. |

### Section 4 — Study Design

| Change | Intent |
|---|---|
| Add an explicit “Case instantiation” framing: general protocol template → this codebook/predicates/window. | Method vs case separation. |
| Present worksheet categories as **an instantiation** of (membership exclusion) + (role classes relative to declared target), not as universal ontology of software. | Portability. |
| Keep Table of predicates, but caption as “Case discovery predicates.” | Optics. |
| Rename narrative from “instruction-artifact audit” to “discovery-frame audit (case frame F).” | Consistency. |
| Optional AI-topic second frame: present as **sensitivity to alternate discovery mechanism**, supporting generality—not as second AI study. | Strengthens B. |

### Section 5 — Results

| Change | Intent |
|---|---|
| Minimal empirical change; **interpretive captions/text** shift: “in this case frame…” + “implies for predicate-based frames…” | Same numbers, B reading. |
| RQ1: emphasize estimand dependence (protocol + target) as methodological result. | Core B claim. |
| RQ2: emphasize heterogeneous discovery predicates generally, with instruction families as instance. | Generalize carefully. |
| RQ3–RQ4: keep as validity diagnostics of the audit method. | Method evaluation. |
| Avoid language that the finding is “about AGENTS.md contamination rates” as a population parameter. | Threats already say this; enforce in Results prose. |

### Section 6 — Discussion

| Change | Intent |
|---|---|
| Split discussion into: (i) methodological implications for MSR discovery-frame audits; (ii) case-specific observations about this frame. | B structure. |
| Reporting guidance → “minimum reporting items for predicate-based discovery studies,” illustrated by the case tables. | Derived, portable. |
| Practical checklist stays, but addressed to MSR study designers / benchmark curators generally. | Audience of B. |
| Demote Copilot/agent product implications unless clearly marked case-only. | Prevent A relapse. |

### Section 7 — Threats to Validity

| Change | Intent |
|---|---|
| Strengthen external-validity statement: one case frame; portability is the **protocol and reporting pattern**, not the rates. | Already partly there—make it the positioning anchor. |
| Add threat: case codebook (CONV/AI_PRD) may not transfer; other frames need role classes redefined relative to *their* target. | Honest B. |
| Keep LLM third-coder threat as consensus-protocol sensitivity, not AI-SE finding. | Align with B. |

### Section 8 — Conclusion

| Change | Intent |
|---|---|
| Rewrite summary as methodology + demonstration; AI-instruction as case only. | Final positioning lock. |
| Current conclusion already leans toward “any sampling frame”—push fully to B and remove instruction-first sentence. | Easy win. |

### Section 9 — Data Availability / replication package narrative

| Change | Intent |
|---|---|
| Describe package as “discovery-frame validity audit replication (case: AI-instruction GitHub frame).” | Metadata/Zenodo language. |
| Docs filenames can stay; README/CITATION conceptual framing should match B. | Artifact consistency. |

### Section 10 — Use of generative AI

| Change | Intent |
|---|---|
| Likely minor; ensure it does not re-center the paper as GenAI research. | Optics. |

### Front-matter adjacent texts

| Artifact | Change |
|---|---|
| Zenodo metadata / RELEASE notes | Align title/description with B. |
| Supplementary README | “Case frame” wording. |
| Any IEEE/EMSE leftover docs | Do not reintroduce A framing. |

---

## What does *not* need to change scientifically

- The four RQs’ empirical content.  
- Pipeline stages and frozen artifacts.  
- Core tables/figures (rates, κ, family strata, inspection concordance).  
- The finding that plurality vs human-only moves non-target prevalence by ~15.7 points.  
- The finding that family rankings are more stable than frame-wide rates.  

Those are already B-results wearing A-clothes.

---

## Risk if you keep A

- Desk rejection for weak practice motivation (grey docs).  
- Reviewers pull you into Copilot/promptware debates you do not win.  
- Novelty collapses to “Kalliamvakou on new filenames.”

## Risk if you move to B carelessly

- Overclaiming a general methodology from one frame.  
- Reviewers demand multi-frame validation.  

**Mitigation:** title and claims say “methodology demonstrated on one case”; Threats and Conclusion forbid universal rates; optional second discovery mechanism (already in design) is framed as transportability probe.

---

## Final recommendation

**Reposition to B immediately.**  
Treat AI-instruction artifacts as a **stress-test case** for predicate-based discovery-frame validity, not as the research domain.  
The manuscript’s evidence already supports B more than A; the current framing is the main liability.
