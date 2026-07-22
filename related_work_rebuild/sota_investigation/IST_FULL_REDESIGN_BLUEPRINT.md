# Full manuscript redesign blueprint (IST acceptance maximization)

**Role:** Senior scientist redesigning narrative only.  
**Constraints:** Experiments frozen. No new data. No new analyses. No invented results. No changed statistics.  
**Governing sentence:**

> A methodology for auditing discovery-frame validity in Mining Software Repositories, demonstrated through AI-instruction artifacts.

**Primary empirical claim (must lead everywhere):**

> Contamination estimates are protocol-dependent estimands.

**Case role:** AI-instruction path predicates = motivating demonstration, not the object of knowledge.

**Frozen evidence anchors (do not alter):**

| Finding | Frozen numbers (use exactly) |
|---|---|
| Plurality non-target (CONV target) | 57.7% [52.0, 63.1], n=300 |
| Human-only non-target | 42.0% [36.6, 47.7], 78 unresolved |
| Protocol gap | **15.7 percentage points** |
| Target collapse (if AI products on-target) | 57.7% → 21.7% non-target |
| Human κ (three-class) | 74.0% agree, κ=0.579 |
| Human κ (AI vs CONV only) | 85.0%, κ=0.701 |
| EXCL in discordant pairs | 55.1% of discordant human pairs involve EXCL |
| LLM resolves human ties | 74 ties; among 78 discordant: 70.5% H1, 24.4% H2, 5.1% neither |
| Plurality vs inspector1 | 70.0%, κ=0.543 (n=50) |
| Inspector1 vs inspector2 | **50.0%**, κ=0.263 |
| Human2 vs inspection (panel A signal) | poorest alignment (wF1 0.209) — frame as boundary hardness / coder difficulty, not hide |

---

## How this redesign answers the five editorial criticisms

| # | Criticism | Redesign answer |
|---|---|---|
| 1 | Looks like reporting guidance | Guidance demoted to derived C3; C1 = protocol-dependent estimands; Title/Abstract/Intro/Conclusion never lead with checklists |
| 2 | Plurality looks LLM-dependent | **Human-only is primary estimand in narrative**; plurality = sensitivity comparator; LLM = optional tie-break factor whose contribution is *measured* (74 ties), not the oracle |
| 3 | Inspection disagreement kills credibility | RQ4 reframed as **boundary-hardness evidence**: metadata consensus ≠ easy gold; dual-inspector 50% shows membership margins remain hard under functional evidence — a validity finding the audit is designed to surface |
| 4 | Intro relies on product docs | Motivation = peer-reviewed sampling/perils/curation lineage + **documented negative search** for predicate-based membership audits (search protocol in Methods or appendix; no new experiments—literature search only as *narrative apparatus already implied by gap docs*). Product docs = case predicate definitions only |
| 5 | Discussion restates findings | Discussion becomes two layers: (i) methodological implications for MSR estimands; (ii) case observations; max 3 hinge numbers |

**Note on (4) under freeze:** A negative systematic search is *documentary*, not a new experiment on the GitHub frame. If authors refuse even that documentation, soften to: “Across the peer-reviewed sampling, curation, and validity clusters reviewed in Section X, we found no operational audit that jointly …” — still no product-doc spine.

---

# Part I — Section-by-section blueprint

## 0. Front matter package

### Title

| | |
|---|---|
| **Objective** | Signal measurement validity + MSR methodology; case optional. |
| **Key message** | This is an IST methods paper about estimands. |
| **Evidence** | N/A (positioning). |
| **Remove** | “Evidence-Based Reporting”; “AI-Instruction Artifacts” as hero noun. |
| **Move** | AI-instruction → “demonstrated on …” clause. |
| **Emphasize** | Discovery-frame validity; protocol-dependent estimates. |
| **De-emphasize** | Reporting; agents; AGENTS.md. |

**Recommended title:**  
**Discovery-Frame Validity in Mining Software Repositories: Protocol-Dependent Contamination Estimands Demonstrated on AI-Instruction Path Predicates**

**Shorter alternative:**  
**When Retrieval Is Not Membership: Auditing Discovery-Frame Validity in Repository Mining**

### Running title

**Recommended (≤75 chars):**  
`Discovery-frame validity: protocol-dependent contamination estimands`

### Abstract

| | |
|---|---|
| **Objective** | 4-beat measurement story; case late; guidance last. |
| **Key message** | Contamination rates are protocol-dependent estimands; we show how to audit that on one predicate-based frame. |
| **Evidence used** | 15.7 pp gap; 57.7 vs 42.0; family structure; boundary disagreement; inspection 70%/50%. |
| **Remove** | “Researchers increasingly…”; guidance as climax; package as scientific claim. |
| **Move** | AI predicates to beat 2; reporting to final sentence. |
| **Emphasize** | Estimand dependence; complementary protocols; one-frame honesty. |
| **De-emphasize** | Filename list; Zenodo. |

**Abstract beat sheet (frozen numbers only):**

1. In MSR, a retrieved repository is not automatically a member of the declared analytic population. When inclusion is a search predicate and membership is coder-mediated, reported contamination is an *estimand*.  
2. **Case:** We instantiate a discovery-frame audit on one public GitHub frame built from seventeen AI-instruction path predicates (selection criteria: path inclusion, heterogeneous families, membership not reducible to engineeredness).  
3. **Method:** discover → filter → annotate (multi-coder worksheet) → inspect; we report complementary consensus protocols on the same repositories.  
4. **Results:** Under a conventional-application target, three-way plurality yields 57.7% non-target versus 42.0% under a human-only protocol (**15.7 pp**); family rankings remain structured; disagreement concentrates at membership boundaries; plurality–inspection concordance is 70% while two inspectors agree on 50% (n=50).  
5. **Implication:** Predicate-based discovery studies must treat the consensus rule (and target) as part of the estimand. Reporting items and the replication package follow from that measurement result.

### Keywords

`mining software repositories; sampling validity; discovery frames; construct validity; consensus protocols; interrater reliability; reproducibility`

(AI / GitHub only if journal requires topical tag — secondary.)

### Highlights (IST style)

1. Contamination prevalence is a **protocol-dependent estimand** (15.7 pp gap between plurality and human-only on the same n=300).  
2. Misalignment is **structured by discovery-predicate family**; family rankings outlast frame-wide rates.  
3. Membership-boundary labels drive disagreement; dual-inspector agreement is 50% — boundary hardness, not a discarded anomaly.  
4. We contribute an operational **discovery-frame validity audit**, demonstrated on AI-instruction path predicates as a stress-test case.  
5. Portable product: report target, predicate families, and complementary consensus protocols with any contamination rate.

---

## 1. Introduction

| | |
|---|---|
| **Objective** | Establish MSR measurement-validity problem; justify case by criteria; announce findings-first contributions. |
| **Key message** | We do not rediscover GitHub perils; we show that contamination prevalence behaves as a protocol-dependent estimand under predicate-based discovery. |
| **Evidence** | Cite Kalliamvakou, Baltes, Munaiah/PHANTOM, Tantithamthavorn (analogy); freeze numbers previewed lightly or deferred to Results. |
| **Remove** | Product-doc opening; “MSR convention” for contamination; guidance-first contributions; Zimmermann as intro pillar; self-cite as gap partner. |
| **Move** | Product docs → Methods case predicates; adoption corpus → optional related data product. |
| **Emphasize** | Retrieval ≠ membership; engineered ≠ on-target; vignette target-conditionality; C1 = protocol-dependent estimands; single-frame honesty early. |
| **De-emphasize** | Instruction-file culture; package. |

**Intro architecture (≤6 short paragraphs):**

1. **MSR problem:** Discovery pipelines retrieve candidates; analytic populations require membership. Kalliamvakou/Baltes.  
2. **Open operational gap:** For *predicate-based* frames, the field lacks audits that treat consensus aggregation as part of the prevalence estimand and that stratify by predicate family (negative search / reviewed clusters — Criticism 4).  
3. **False friend:** Engineered curation removes non-software noise but does not equate to study-specific membership (Munaiah/PHANTOM residual).  
4. **Case criteria (not hype):** Need path predicates, heterogeneous families, likely engineered survivors, coder-mediated membership → AI-instruction paths instantiate these criteria.  
5. **This paper:** One frame; four RQs; human-only as primary narrative estimand; plurality as sensitivity.  
6. **Contributions:** C1 findings (estimand dependence, family structure, boundary hardness) → C2 audit protocol → C3 derived reporting items → C4 apparatus.

**Motivation replacement for product docs (Criticism 4) — choose A or B:**

- **A (preferred):** 1 paragraph: “We conducted a documented search of peer-reviewed MSR/ESE venues for audits that jointly report target-conditional membership error, predicate-family strata, and complementary consensus estimates for path-predicate discovery frames [databases, strings, date in Appendix S0]. We found none that close this joint gap; closest neighbors are [Kalliamvakou, Baltes, Munaiah, Golzadeh].”  
- **B (minimal):** No “increasingly”; open on validity literature only; grey docs appear first in Methods as predicate definitions.

---

## 2. Related Work

| | |
|---|---|
| **Objective** | Position next to sampling validity lineage; isolate residual. |
| **Key message** | Prior work proves samples can be wrong and engineered filters help; it does not treat contamination prevalence as a consensus-protocol estimand for predicate-based frames. |
| **Evidence** | CORE cites only (Baltes, Kalliamvakou 2015, Munaiah, PHANTOM, Dabic, Tantithamthavorn, Golzadeh, Herbold, Lopes, Verdecchia, Wohlin, Ahmed). |
| **Remove** | Copilot HCI tourism; Fan+Storey+Fantechi padding; triple restatement “why needed”; self-cite as predecessor. |
| **Move** | Promptware/grey docs → short “stress-test case” subsection; LLM annotation → consensus third-coder paragraph. |
| **Emphasize** | False friend RepoReapers; contamination-sense disambiguation; protocol-sensitivity cousin (Tantithamthavorn); membership GT cousin (Golzadeh). |
| **De-emphasize** | Artifact norms; AI-SE surveys. |

**RW order:** Access≠membership → Sampling guidelines → Engineered curation residual → Validity/ToV → Other contamination senses → Consensus/label validation → Stress-test case (short) → Residual gap.

---

## 3. Research Questions

| | |
|---|---|
| **Objective** | Make RQs measurement questions about estimands and validity diagnostics. |
| **Key message** | Same empirics; B linguistics; human-only primary in RQ1 narrative. |
| **Evidence** | Existing RQ1–RQ4 analyses unchanged. |
| **Remove** | RQ wording that centers “instruction-artifact reporting.” |
| **Move** | LLM role into Methods as protocol variant, not RQ topic. |
| **Emphasize** | Estimand / structure / boundary / concordance. |
| **De-emphasize** | AI filenames in RQ stems. |

**Redesigned RQ stems:**

- **RQ1.** To what extent is contamination prevalence in a predicate-based discovery frame sensitive to the consensus protocol and analytic target? *(Primary report: human-only; plurality as complementary sensitivity; disclose LLM tie-break contribution.)*  
- **RQ2.** Is misalignment uniform across the frame or structured by discovery-predicate family?  
- **RQ3.** Where does coder disagreement concentrate—membership boundaries or product-role distinctions?  
- **RQ4.** How stable are membership judgments when metadata consensus is reassessed under functional evidence—and across independent inspectors?

---

## 4. Methodology

| | |
|---|---|
| **Objective** | Separate general audit template from case instantiation; fix Criticism 2 optically. |
| **Key message** | The method audits estimands; the case supplies predicates and a target-relative codebook. |
| **Evidence** | Existing pipeline, n, worksheets, protocols — unchanged. |
| **Remove** | “Instruction-artifact study” as method name; CONV/AI_PRD as universal ontology. |
| **Move** | Predicate table → Case discovery predicates; LLM → “Protocol variants” subsection. |
| **Emphasize** | Declared target; **human-only as primary estimand definition**; plurality and LLM-assisted as sensitivity/adjudication variants; inspection as boundary probe. |
| **De-emphasize** | LLM capability claims. |

**Critical Methods block (Criticism 2) — narrative only:**

```text
Estimand definitions (same data):
  E_human   = human-only consensus (disagreements unresolved / TIE)
  E_plural  = three-way plurality (includes model-assisted labels where used)
  Gap       = |E_plural − E_human|   (= 15.7 pp under CONV target)

Scientific reading:
  E_human is the primary human-coded prevalence estimand.
  E_plural is reported for sensitivity analysis and to quantify how
  tie-breaking/adjudication changes the estimand (74 ties resolved).
  We do not treat LLM labels as ground truth.
```

**Inspection framing (Criticism 3) — Methods foreshadow:**

Inspection is not a claim of infallible gold. It is a **second measurement regime** (functional evidence) used to locate where metadata membership calls remain hard. Dual-inspector disagreement is an expected boundary-hardness signal.

**Motivation appendix (Criticism 4):** Appendix S0 = negative search protocol (no new GitHub data).

---

## 5. Results

| | |
|---|---|
| **Objective** | Deliver C1 with frozen numbers; never sell case rates as GitHub parameters. |
| **Key message** | Estimands move; structure persists; boundaries are hard. |
| **Evidence** | All existing tables/figures; same statistics. |
| **Remove** | Filename-hero captions; “population contamination rate for AGENTS.md.” |
| **Move** | Package mentions → Data Availability. |
| **Emphasize** | Lead every RQ1 subsection with human-only **then** plurality sensitivity; 15.7 pp; target collapse; family durability; EXCL-boundary disagreement; inspection 70% / dual 50%. |
| **De-emphasize** | LLM “outperforms” language; product implications. |

**Results narrative order (same analyses):**

1. **RQ1a — Primary estimand:** Human-only 42.0% [36.6, 47.7]; 78 unresolved.  
2. **RQ1b — Sensitivity:** Plurality 57.7%; gap 15.7 pp; human-agreement subset recovers plurality-like rate → sensitivity concentrated in disputed cases.  
3. **RQ1c — Target sensitivity:** 57.7% → 21.7% if AI products count as on-target.  
4. **RQ1d — Adjudication accounting:** 74 ties resolved by model-assisted pass — *explains* part of gap; does not license LLM-as-truth.  
5. **RQ2:** Family strata / sparsity (existing table).  
6. **RQ3:** κ patterns; EXCL-driven discord.  
7. **RQ4:** Plurality–inspector 70%; inspector–inspector 50%; Human2–inspection poor alignment — **boundary hardness cluster**.

**Caption rule:** “Case frame F; analytic target = conventional applications unless noted.”

---

## 6. Discussion

| | |
|---|---|
| **Objective** | Synthesize methodological implications (Criticism 5); quarantine case notes. |
| **Key message** | In predicate-based MSR discovery, a single contamination percentage without protocol and family context is not an interpretable scientific object. |
| **Evidence** | At most three hinges: 15.7 pp; family non-uniformity; 50% dual-inspector. |
| **Remove** | Phase-by-phase numeric restatement of Results; checklist-as-contribution voice. |
| **Move** | Dense numbers back to tables; reporting items to short derived subsection. |
| **Emphasize** | Estimand theory for MSR; false-friend engineered filters; boundary hardness as design constraint; what travels vs what does not. |
| **De-emphasize** | Agent tooling advice; package praise. |

**Discussion structure (mandatory):**

### 6.1 Methodological implication — estimands  
Contamination prevalence under multi-coder labeling is protocol-defined. Studies that publish only one aggregation rule overclaim precision. Complementary protocols are not optional polish; they are part of construct validity for prevalence estimands (cousin: Tantithamthavorn sensitivity culture).

### 6.2 Methodological implication — structure  
Frame-wide rates can hide predicate-family mixture. Heterogeneous discovery predicates require strata or the estimand is confounded by composition.

### 6.3 Methodological implication — boundary hardness (Criticism 3)  
Low dual-inspector agreement and EXCL-centered discord are **positive validity evidence** that membership margins are epistemically hard. An audit that reported perfect inspection concordance would be *less* credible for this construct. The correct scientific move is to localize uncertainty at boundaries and avoid over-interpreting point rates.

### 6.4 Case observations (quarantine)  
What this AI-instruction frame showed under target T=conventional applications (point to tables). No generalization of rates.

### 6.5 Derived reporting items (short)  
Forced by 6.1–6.3: declare target; list predicate families; report ≥2 consensus protocols; report boundary/inspection diagnostics. Not a guideline paper — measurement consequences.

---

## 7. Threats to Validity

| | |
|---|---|
| **Objective** | Make single-case humility protect B; metabolize inspection/LLM threats. |
| **Key message** | The audit pattern travels; rates and codebook labels do not; LLM is a protocol threat, not a finding. |
| **Evidence** | Existing threats + frozen RQ4/LLM facts. |
| **Remove** | Threats that quietly cancel C1 without discussion synthesis. |
| **Move** | LLM threat → “primary estimand is human-only; plurality sensitivity discloses adjudication dependence.” |
| **Emphasize** | External: one frame; Construct: role classes are target-relative; Internal: estimand definition includes consensus rule; Reliability: boundary hardness limits point-estimate authority. |
| **De-emphasize** | Generic ToV laundry list. |

---

## 8. Conclusion

| | |
|---|---|
| **Objective** | Lock B; restate C1; forbid AGENTS.md reading. |
| **Key message** | Discovery-frame validity is auditable; contamination estimates are protocol-dependent estimands; demonstrated on one stress-test case. |
| **Evidence** | 15.7 pp + portable implications. |
| **Remove** | Instruction-first sentence; “contribution = guidance and package.” |
| **Move** | Package → final clause / Data Availability. |
| **Emphasize** | Methodology + demonstration; estimand dependence. |
| **De-emphasize** | AI artifacts as lasting object. |

**Conclusion beats:**

1. Retrieval ≠ membership is the known MSR problem class.  
2. Under predicate-based discovery, prevalence is protocol- and structure-sensitive (**15.7 pp** in this case).  
3. Boundary hardness is part of the validity story.  
4. Contribution = audit methodology + measurement demonstration; AI-instruction paths = case.  
5. Rates are not universal; reporting complementary estimands is.

---

## 9. Cover Letter (IST)

| | |
|---|---|
| **Objective** | Pre-empt desk reject; sell measurement validity. |
| **Key message** | Methods paper on discovery-frame estimands; case is AI-instruction paths; not a promptware/HCI paper. |
| **Remove** | “We provide reporting guidelines for AGENTS.md studies.” |
| **Emphasize** | Protocol-dependent estimands; frozen sensitivity results; single-frame honesty; why IST (sampling validity / ToV audience). |

**Cover letter spine (≈1 page):**

1. Why IST: sampling validity / construct validity / empirical standards audience.  
2. Problem: predicate-based GitHub discovery yields membership estimands that current curated filters and guidelines do not operationalize.  
3. Contribution: measurement demonstration that contamination prevalence moves 15.7 pp under complementary consensus protocols on the same repositories; family structure; boundary diagnostics.  
4. Case: AI-instruction path predicates chosen by methodological criteria, not as AI-SE theory.  
5. What we are *not*: not Copilot productivity; not a universal GitHub rate; not a guideline paper with an appendix study.  
6. Replication package available; single-frame scope disclosed.

---

# Part II — Global remove / move / emphasize map

| Material | Action |
|---|---|
| Product documentation | **Move** to Methods (predicate definitions only) |
| “Increasingly / begins to sample” | **Remove** |
| Reporting guidance as C1 | **Demote** to C3 |
| Replication package as C1 | **Demote** to C4 |
| Plurality as headline rate | **Demote**; human-only leads |
| LLM as authority | **Remove**; keep as measured adjudication factor |
| Inspection 50% / Human2 poor concordance | **Emphasize** as boundary hardness |
| RepoReapers residual | **Emphasize** as false-friend (narrative; no new analysis required beyond stating construct difference; if frozen residual table exists, use it—do not invent) |
| Copilot/Promptware surveys | **De-emphasize** to stress-test subsection |
| Filename storytelling | **De-emphasize** |
| 15.7 pp protocol gap | **Emphasize** everywhere front matter + Discussion hinge |
| Family structure | **Emphasize** as second primary finding |
| Target collapse 57.7→21.7 | **Emphasize** as target-conditionality proof |

---

# Part III — Estimated reduction in desk-rejection risk

Scale: expected **relative reduction in probability of desk reject / return-without-review** attributable to that redesign element, assuming other elements held fixed. AE lens (IST). Baseline = current A-framed manuscript.

| Redesign element | Addresses | Est. risk reduction | Rationale |
|---|---|---:|---|
| **R1. Title + Abstract lead with protocol-dependent estimands** | Crit 1 | **18–25%** | Stops “guideline paper” classification at 30-second skim |
| **R2. Contributions reordered C1→C4; guidance demoted** | Crit 1 | **12–18%** | Matches RW honesty; AE no longer sees padding |
| **R3. Human-only primary; plurality = sensitivity; LLM accounted not authoritative** | Crit 2 | **15–22%** | Removes “LLM labeled the science” reject path |
| **R4. Inspection discord framed as boundary hardness** | Crit 3 | **10–16%** | Converts fatal credibility hit into RQ4 scientific payload |
| **R5. Product-doc motivation replaced by validity lineage + negative search** | Crit 4 | **12–18%** | Fixes unsupported practice claim that AE called fatal |
| **R6. Discussion = implications not Results reprise** | Crit 5 | **6–10%** | Signals mature methods paper; fewer “so what?” desk notes |
| **R7. Case demotion (AI = stress test) throughout** | A→B | **10–15%** | Avoids Copilot/promptware referee pool mismatch |
| **R8. Single-frame honesty early + non-claims** | Overclaim | **5–8%** | Prevents “universal methodology” overreach reject |
| **R9. Cover letter pre-empts misclassification** | Process | **3–6%** | Helps AE assign correct track/referees |
| **R10. Running title / highlights / keywords aligned** | Optics | **2–4%** | Consistency reduces mixed-signal desk anxiety |

**Non-additive combined estimate (with overlap):**

| Package | Est. desk-reject risk |
|---|---|
| Current framing (baseline) | **High (~65–80%)** |
| After R1–R5 only (critical five) | **Moderate (~25–40%)** |
| After full R1–R10 | **Lower-moderate (~15–30%)** |
| Residual irreducible risk | Single-frame scope; no new RepoReapers residual analysis if referees demand it; boundary κ will still be debated — but now on *your* terms |

**What this redesign cannot fix (honesty):**

- Cannot create multi-frame external validity without new data.  
- Cannot make dual-inspector 50% into high reliability — only reframe its meaning.  
- Cannot prove “the field already mines by AGENTS.md” without literature evidence — hence negative search / demotion.  
- Cannot elevate package/guidance to novelty.

---

# Part IV — One-page narrative spine (post-redesign)

```text
TITLE/ABSTRACT
  Contamination estimates are protocol-dependent estimands.
  Case = AI-instruction path predicates.

INTRODUCTION
  MSR: retrieval ≠ membership (known).
  Open: predicate-based frames lack estimand-level audits.
  Case chosen by criteria; not an AGENTS.md paper.
  C1 = measurement findings.

RELATED WORK
  Baltes/Kalliamvakou/Munaiah/Tantithamthavorn/Golzadeh.
  Residual = joint audit we perform.

RQs
  Estimand sensitivity; family structure; boundary discord; inspection hardness.

METHODS
  Template vs case.
  E_human primary; E_plural sensitivity; LLM disclosed.

RESULTS
  42.0% vs 57.7% (15.7 pp); families; boundaries; 70%/50% inspection.

DISCUSSION
  Implications for MSR estimands; boundary hardness as design fact;
  case quarantine; derived reporting items.

THREATS
  One frame; codebook target-relative; rates do not travel.

CONCLUSION
  Methodology + demonstration; estimands, not filenames.
```

---

# Part V — Success test (AE 90-second skim)

After redesign, AE should answer:

1. **What is it?** Measurement-validity methodology for discovery frames in MSR.  
2. **What is new?** Protocol-dependent contamination estimands (+ family structure + boundary hardness), demonstrated on one case.  
3. **What is the case?** AI-instruction path predicates.  
4. **What is it not?** A reporting-guideline paper; an AGENTS.md paper; an LLM-annotation paper.

If any answer fails, the narrative is not done.

---

*Blueprint only. No manuscript text rewritten. No statistics changed. Date: 2026-07-22.*
