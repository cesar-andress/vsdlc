# Desk assessment — Introduction & Related Work only

**Role:** Senior Associate Editor, *Information and Software Technology*  
**Scope:** Introduction + Related Work (and abstract as framing context)  
**Stance:** Protect the journal. Prefer rejection if the front matter cannot justify review.

---

## Editorial decision (on these sections alone)

**Return without review / conditional desk reject.**

I would **not** send this manuscript to referees in its present form.

The Related Work is unusually careful about not overclaiming GitHub perils. That honesty is welcome. It is not enough. The Introduction still sells a paper whose **motivation, evidence of prevalence, and novelty hinge** are under-specified for IST. A competent reviewer pool will spend the first round arguing whether this is a methods note, a single-frame case study, or a restatement of Kalliamvakou/Baltes with new filenames. That is an editorial failure, not a referee problem.

Below is every material weakness I see in Intro + RW.

---

## 1. Weak motivation (fatal if unfixed)

### W1. “Increasingly sample GitHub via agent-instruction files” is unsupported as a research-practice claim
The opening sentence cites **product documentation** (AGENTS.md, Cursor, Copilot docs, MCP), not peer-reviewed studies that actually use these predicates as sampling frames.

**Why this is fatal:** IST readers accept grey literature as *phenomenon* evidence. They do not accept it as evidence that the *empirical SE community* has adopted a flawed sampling practice at scale. Without a short, concrete map of published papers (or preprints destined for peer review) that already mine by these filenames—and what they claim about populations—the motivation is speculative.

### W2. The paper motivates a validity crisis without showing harm in published estimates
You assert that contaminated denominators “bias downstream statistics,” citing Kalliamvakou and Zimmermann. Those citations support *general* mismatch risk, not that instruction-file sampling has already produced biased published rates.

**Missing:** at least one worked example of a published claim that would change under your audit (even retrospectively, on a public paper’s corpus definition).

### W3. Self-citation carries too much of the “gap” argument
`ai_convention_lifecycle_corpus2026` is used to say adoption work charts spread, then “neither line routinely audits…”. An editor reads this as: **authors define the gap relative to their own prior Zenodo line**. That is an editorial red flag unless accompanied by independent literature showing the same omission.

### W4. Motivation and Related Work repeat the same thesis three times
Intro, RW opening, and “Why this article is needed” restate sample≠population. IST does not need 2.5k words to re-earn permission to apply Baltes. Compression would help; repetition currently signals insecurity about novelty.

---

## 2. Novelty problems (core rejection risk)

### W5. The contribution list is soft relative to the Related Work’s own honesty
Intro contributions:
1. reporting guidance  
2. evidence that consensus protocols shift rates / family structure is robust  
3. reproducible protocol  

RW correctly demotes (1) and (3) as incremental relative to Baltes / artifact norms. That means **the paper’s publishability rests almost entirely on (2)**. The Introduction does not make (2) the sole primary claim. Editors will infer the authors are padding.

### W6. “Reporting guidance” is not an IST contribution unless it is empirically forced
Baltes & Ralph already demand frames/populations. Your checklist items (target, families, consensus protocol) are plausible specializations, but presenting “guidance” as a co-equal contribution invites the desk question: *Is this a guideline paper with an appendix study?*

### W7. Single-frame scope is disclosed late and weakly in the Intro
“Applied to one public GitHub frame” appears, but the Intro still speaks as if delivering regime-level methodology. For IST, one frame is acceptable **only if** positioned as an existence-proof measurement study with tightly scoped claims. Current Intro oscillates between case study and field guidance.

### W8. Conditional novelty language in RW (“If the audit shows…”) is an editorial own-goal
In Related Work you write that the scientific payload *is* a measurement-validity result **if** results hold. That belongs in Discussion, not in the literature justification. In front matter it reads as uncertainty about whether the paper has a result yet.

---

## 3. Unsupported / overclaimed statements

### W9. “Following MSR convention, we call a repository contaminated when…”
This is not an established MSR convention for *population mismatch*. In SE/ML, “contamination” usually means leakage/duplication. You later spend a subsection disambiguating—good—but the Intro still **appropriates a contested term as convention**. That is an overclaim of terminology.

### W10. “Neither line routinely audits sample-target fit…”
Strong negative existential claim. Supported only by narrative synthesis, not by a systematic scan protocol described in Intro/RW (search strings, inclusion rules, date range). As AE I treat “no study does X” as **unsupported** unless the search is reported.

### W11. “Studies often document retrieval yet leave implicit the analytic target…”
Which studies? How many? This is a straw pattern without citations to concrete offenders (anonymized if needed). Without examples, it is hand-waving.

### W12. Zimmermann et al. (cross-project defect prediction) is overstretched in the Intro
Citing cross-project prediction failure to support instruction-file population mismatch is analogical, not direct. Acceptable in RW with careful wording; in Intro sentence 3 it looks like citation padding.

### W13. Storey & Zagalsky (bots) is a weak pillar for “automation context”
In RW it is acknowledged as not about sampling predicates—then why is it there? It dilutes the argument.

### W14. Fantechi et al. (ChatGPT for RE inconsistency) is peripheral
It does not strengthen the contamination-audit gap. It reads as LLM-section filler.

---

## 4. Underclaims / missed opportunities (also a problem)

### W15. You under-sell the only potentially review-worthy claim
The sharp claim—**contamination prevalence is protocol-dependent; families are not exchangeable**—is buried under guidance/package language. An IST paper can survive as a measurement study. It cannot survive as “we provide reporting guidance and a worksheet.”

### W16. You under-engage RepoReapers/PHANTOM as the true novelty threat
RW says engineered ≠ on-target—correct—but does not pre-empt the obvious referee experiment: *run RepoReapers/PHANTOM on your frame; what residual contamination remains?* Without promising that comparison (even if results come later), novelty looks rhetorical.

### W17. Target-conditionality is asserted, not illustrated in Intro
Background states CONV vs AI tooling targets. Intro never gives a one-sentence concrete vignette (e.g., “same AGENTS.md hit is on-target for tooling study, off-target for application study”). Editors need that vignette early.

---

## 5. Missing literature (relative to what Intro/RW attempt)

I am not asking for encyclopedic coverage. I am asking for coverage of threats to *your* claim.

### Missing or underused relative to sampling / GitHub validity
- Explicit “no random sampling in SE” line (Ralph and co-authors) — you cite Baltes & Ralph 2022 but not the sharper companion claims about non-probability samples.
- GitHub Search / API affordance limitations beyond Kalliamvakou (query bias, visibility, indexing lag).
- Broader OSS selection-bias / representativeness work (beyond stars papers).
- Taxonomy papers on “what is a software project on GitHub” more recent than 2015–2017 curation.

### Missing relative to annotation / consensus as estimand
- Literature on **majority vs adjudication vs expert panel** as affecting prevalence estimates (even outside SE).
- SE annotation protocol papers beyond κ citations (requirements labeling, bug classification agreement studies) if you claim consensus-protocol sensitivity as novel.

### Missing relative to “AI instruction artifacts as discovery”
- Corpus-construction / filtering papers for LLM code datasets (The Stack, CodeSearchNet-style decontamination/filtering)—these are the closest *modern* cousins for “path/content predicates create polluted corpora.”
- Any peer-reviewed empirical paper that *already* mines AGENTS.md / `.cursorrules` / copilot-instructions (if none exist, say so explicitly with a dated search statement; do not imply absence via vibe).

### Missing relative to IST methodological audience
- Kitchenham-family secondary-study process (you cite Petersen/Ampatzoglou; Kitchenham is still expected furniture when claiming “no study jointly does X”).
- Stronger engagement with ACM SIGSOFT Empirical Standards *content*, not only the announcement note (`ralph2021standards`).

### Grey literature balance
Product docs are fine. Using them as the spine of paragraph 1 is not.

---

## 6. Missing comparisons (must appear before review)

In Intro or early RW, add an explicit comparison table (even 6–8 rows):

| Approach | Construct | What it decides | What it does not decide |
|---|---|---|---|
| Kalliamvakou perils | GitHub entity validity | Many hits ≠ projects | Instruction-family structure; consensus sensitivity |
| Baltes & Ralph | Sampling reporting | Declare frame/population | Operational audit for instruction predicates |
| RepoReapers / PHANTOM | Engineeredness | Filter non-engineered | Product-role target for agent studies |
| Leakage/duplication | Train/eval pollution | Clean ML corpora | Sample–target membership |
| Golzadeh bots GT | Entity membership | Bot vs human | Instruction-artifact population |
| **This paper** | Target-conditional contamination under instruction-file discovery | … | Single frame; not a new sampling theory |

Without this table, referees will invent worse comparisons for you.

---

## 7. Logical jumps

### J1. From “path match ≠ membership” → “we need consensus-protocol sensitivity”
The first is definitional. The second is an empirical hypothesis. Intro presents both as if equally motivated. You need one sentence: *because membership is coder-mediated under metadata sparsity, aggregation rules can move prevalence.*

### J2. From “families are heterogeneous filenames” → “family-level contamination reporting is required”
Heterogeneous filenames do not logically entail heterogeneous contamination. That is empirical. Do not moralize it as methodological necessity before results.

### J3. From “LLM annotation exists” → long RW subsection
LLM annotation is not required for your gap. Either cut the subsection substantially or justify why adjudication appears in *your* protocol. Currently it is a distraction that invites off-topic reviews.

### J4. Enumerated “jointly unsolved” checklist risks moving goalposts
Listing five conjuncts that no paper jointly satisfies is a classic novelty-engineering pattern. Editors notice. Prefer: one primary unsolved estimand + two secondary reporting implications.

---

## 8. Structural / editorial red flags

### R1. Related Work is long, Intro is thin
IST prefers a sharp Intro (problem, gap, claim, contributions) and a leaner RW. Yours inverted: RW argues carefully; Intro still under-argues prevalence and over-lists contributions.

### R2. Background section exists separately (seen in outline)
If Background repeats RW theses, the front matter is bloated. Merge or cut.

### R3. Heavy dependence on authors’ Zenodo package in contribution sentence
Acceptable for reproducibility; dangerous when it appears as contribution #3 co-equal with science.

### R4. Category macros in Intro (`CONV`, `AI_PRD`, `EXCL`) before definitions
Readers hit notation before substance. Defer symbols to Study Design; keep Intro conceptual.

### R5. Citation hygiene optics
Multiple product URLs in sentence 1 + self Zenodo + broad surveys (Hou/Fan) create a “mixed register” that looks less like IST methodology and more like a tech-trend paper with a methods appendix.

### R6. Potential scope mismatch with IST
If the empirical payload is one audited frame, IST may still take it—but only as **measurement/method** with transferable findings. Current front matter does not lock that genre.

---

## 9. Outdated / weak reference choices (front-matter specific)

- Relying on Howison 2004 + Kalliamvakou 2014/15 as the *entire* perils spine is fine historically, but for a 2026 AI-instruction paper you need **at least one 2023–2026 peer-reviewed bridge** showing modern corpus-construction failure modes (beyond Promptware surveys).
- `storey2020` / bot disruption piece is dated relative to agent-instruction claims.
- Announcement-style `ralph2021standards` is weaker than citing the standards’ substantive requirements.

---

## 10. Bottom-line rejection rationale (one paragraph)

On Introduction and Related Work alone, this manuscript does not yet demonstrate that the empirical software engineering community has a concrete, widespread validity failure in AI-instruction discovery sampling; it demonstrates that such a failure *could* exist given known GitHub perils and new filenames. The Related Work correctly refuses to reinvent Kalliamvakou/Baltes/Munaiah, which collapses the publishable core to a measurement claim about protocol sensitivity and family structure on one frame. The Introduction does not center that claim, leans on grey literature and self-citation for motivation, and offers reporting guidance as a primary contribution. That package is not ready for IST review.

---

## Precise modifications that would make me send it to peer review

### A. Rewrite the Introduction to this skeleton (≈1.5–2 pages max)

1. **Concrete vignette (5–8 lines):** one repository / one predicate / two analytic targets (application vs AI tooling) → opposite membership decisions.  
2. **Practice evidence (8–12 lines):** 5–10 published or archival studies that sample via instruction-like paths **or** an explicit dated negative search (“we found no peer-reviewed study using AGENTS.md as a discovery frame as of DATE”). No vibes.  
3. **Gap in one sentence:** engineered filters and sampling guidelines do not determine target-conditional membership under instruction-file discovery; contamination rates may depend on consensus protocol and predicate family.  
4. **Claim (bold, singular):** This paper provides a measurement audit showing [protocol sensitivity + family structure + boundary disagreement] on one public frame.  
5. **Contributions (reorder):**  
   - C1 empirical measurement findings (primary)  
   - C2 operational protocol enabling those findings  
   - C3 reporting implications (derived, not primary)  
6. **Non-claims (3 bullets):** not a new GitHub theory; not a replacement for RepoReapers; not a claim that all MSR must use these predicates.  
7. Remove contribution-level emphasis on Zenodo; keep it in Data Availability only.

### B. Cut Related Work by ~30–40%

Keep:
- GitHub perils + sampling guidelines  
- Engineered curation as closest false friend  
- Contamination-sense disambiguation (short)  
- Annotation/consensus as estimand (short)  
- Instruction artifacts + existing studies (short, with search statement)

Cut or merge hard:
- LLM-assisted annotation (≤1 paragraph or move to Discussion/Threats)  
- Long reproducibility sermon (≤1 paragraph)  
- Repeated “why needed” that restates Intro  

### C. Add the comparison table (mandatory)

Place at end of RW or after Intro contributions.

### D. Pre-empt the RepoReapers objection in Intro/RW

One paragraph: “Even after engineered/activity filters, product-role mismatch can remain; our audit is defined on the residual membership question.” Promise the residual analysis in Results (or report it).

### E. Fix terminology in Intro

Replace “MSR convention… contaminated” with: “We use *contamination* for target-conditional sample membership error, distinct from train/test leakage and code duplication [cites].”

### F. Replace existential gap rhetoric

Change “no study jointly does (1)–(5)” → “Prior work does not evaluate estimand E on discovery class D; we evaluate E on one instance of D.”

### G. Add one harm/illustrative estimate

Even a toy calculation: “If 20% of a denominator is off-target, adoption rate X becomes Y.” Speculative but grounded beats abstract bias talk.

### H. Align title/claim language

Title currently emphasizes “Evidence-Based Reporting…”. If the science is measurement sensitivity, retitle toward audit/measurement validity; otherwise reviewers will grade you as a reporting-guidelines paper and find you incremental to Baltes.

---

## What would still not be enough

Even after the above, I will desk-reject again if:
- results do **not** show meaningful protocol sensitivity or family structure; or  
- the paper continues to lead with “reporting guidance”; or  
- motivation remains only product docs + self Zenodo.

---

## Final editor note

The Related Work’s refusal to overclaim is the manuscript’s best asset and its biggest exposure: it reveals that novelty is narrow. **Narrow is publishable. Soft is not.** Center the narrow claim, prove the practice gap or the negative search, cut the scaffolding, and I will send it to reviewers. Keep the current Intro/RW balance, and I will reject to protect IST’s methods track from another “new filenames, old validity lecture” submission.
