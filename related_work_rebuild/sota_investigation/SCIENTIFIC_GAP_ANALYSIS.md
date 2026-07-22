# Scientific Gap Discovery

**Date:** 2026-07-22  
**Corpus:** `related_work_rebuild/sota_investigation/` (Crossref-verified; OpenAlex abstracts)  
**Manuscript:** not modified  
**Stance:** adversarial IST reviewer

---

## Framing (what “our problem” is)

Our paper’s claimed problem is **not** “GitHub is noisy.” That is already known.

The operational problem is:

> When researchers discover GitHub repositories by searching for **AI-instruction artifacts** (path/filename predicates such as `AGENTS.md`, Cursor rules, Copilot instructions, prompt paths), a hit does not establish membership in the **analytic population** named by the research question. Contamination is **target-conditional**, may **cluster by predicate family**, and the resulting **contamination rate is not invariant to the consensus protocol** used to aggregate multi-coder labels.

Anything weaker than this is not a gap; it is a restatement of Kalliamvakou / Baltes.

---

## Area-by-area gap matrix

For each area: **Solved / Partial / Unsolved / Closest papers / Why they fail our problem**.

### 1. Mining Software Repositories (MSR)

| | |
|---|---|
| **Solved** | MSR as a research programme, tooling, and large-scale workflows (Hassan 2008; GHTorrent; PyDriller; World of Code). |
| **Partial** | Methodological self-critique exists, but often stops at retrieval quality or general perils. |
| **Unsolved** | Routine treatment of **path-predicate discovery** as a validity object with estimand-level sensitivity analysis. |
| **Closest** | Hassan 2008; Gousios & Spinellis 2012; Spadini et al. 2018; Ma et al. 2019. |
| **Why not us** | They solve **access and mining cost**, not sample–target membership after instruction-file search. |

### 2. Repository discovery

| | |
|---|---|
| **Solved** | Multi-forge / archive-scale discovery (World of Code; Software Heritage). |
| **Partial** | Discovery expands coverage; composition validity remains author-defined. |
| **Unsolved** | Discovery **frames** built specifically from AI-instruction filenames, with family-level composition audits. |
| **Closest** | Ma et al. 2019; Pietri et al. 2019; Abramatic/Di Cosmo/Zacchiroli 2018. |
| **Why not us** | Infrastructure ≠ population membership. |

### 3. Repository sampling

| | |
|---|---|
| **Solved** | Empirical descriptions of how MSR samples GitHub (Dabic et al. 2021). |
| **Partial** | Sampling practice is studied; instruction-artifact predicates are not. |
| **Unsolved** | Sampling designs whose inclusion event is “has instruction file X,” then audited for target fit. |
| **Closest** | Dabic et al. 2021; Cosentino et al. 2017. |
| **Why not us** | They study sampling *as practiced*, not contamination of instruction-file frames. |

### 4. Sampling methodology

| | |
|---|---|
| **Solved** | Critical review + guidelines for frames, populations, generalization (Baltes & Ralph 2022); “no random sampling” warnings (Ralph et al. related). |
| **Partial** | Guidelines exist; **operational worksheets** for a new discovery class do not. |
| **Unsolved** | A reusable audit that makes consensus protocol and predicate family reportable design parameters for instruction-artifact frames. |
| **Closest** | Baltes & Ralph 2022. |
| **Why not us** | Normative methodology without the empirical instruction-frame audit (and without protocol-sensitivity of contamination rates). |

### 5. Sampling bias

| | |
|---|---|
| **Solved** | Classic forge/GitHub perils: not-software entities, proxy fragility, activity illusions (Howison 2004; Kalliamvakou 2014/2015). |
| **Partial** | Bias taxonomies are mature; **new bias channels** from agent-instruction ecosystems are under-characterized. |
| **Unsolved** | Bias arising because instruction files appear in apps, AI SDKs, prompt packs, coursework, and mirrors—often still “engineered.” |
| **Closest** | Kalliamvakou et al. 2014, 2015. |
| **Why not us** | They prove the *class* of problem; they do not measure instruction-predicate family structure or consensus sensitivity. |

**Critical note:** If the paper claims to “discover” sampling bias on GitHub, it is **not novel**.

### 6–8. Construct / internal / external validity

| | |
|---|---|
| **Solved** | Validity vocabularies and community debate (Wohlin; Runeson; Siegmund 2015; Ampatzoglou 2019; Verdecchia 2023). Tangled changes as construct failure (Herzig & Zeller 2013). |
| **Partial** | Authors are urged to discuss ToV; few treat **consensus aggregation** as an internal-validity threat to a prevalence estimand. |
| **Unsolved** | Demonstrating that an MSR prevalence estimate (contamination rate) **moves under alternative consensus protocols** on the same coded set, for instruction-artifact frames. |
| **Closest** | Siegmund et al. 2015; Verdecchia et al. 2023; Tantithamthavorn et al. 2017 (sensitivity of conclusions to validation choices—different estimand). |
| **Why not us** | Taxonomies/guidelines ≠ this estimand on this discovery class. |

### 9. Dataset contamination

| | |
|---|---|
| **Solved** | Leakage (Kaufman 2012); dataset shift (Moreno-Torres 2012); GitHub duplication (Lopes 2017; Allamanis 2019); ML science leakage crisis (Kapoor & Narayanan 2023). |
| **Partial** | “Contamination” is overloaded; SE rarely separates senses carefully. |
| **Unsolved** | **Sample–target contamination** of discovery frames (our sense), as distinct from train/test leakage and duplication. |
| **Closest** | Kaufman; Lopes; Allamanis; Kapoor. |
| **Why not us** | Wrong contamination construct. Using their word without disambiguation would be scientifically sloppy—and would destroy novelty claims. |

### 10. GitHub repository mining

| | |
|---|---|
| **Solved** | Affordances, APIs, mappings of GitHub-based SE research (Kalliamvakou; Cosentino; GHTorrent). |
| **Partial** | Filters (stars, forks, activity) are common but insufficient for product-role targets. |
| **Unsolved** | Mining pipelines that start from instruction-file search and then audit target fit as a first-class result. |
| **Closest** | Kalliamvakou; Cosentino 2017. |
| **Why not us** | Mining practice ≠ contamination audit for agent-instruction predicates. |

### 11–12. Dataset / benchmark construction

| | |
|---|---|
| **Solved** | Benchmarks need scope and validation (D’Ambros 2012); SZZ/process labels fail without manual checks (Herbold 2022); SWE-bench shows GitHub-issue filtering choices shape evaluation populations (Jimenez 2024; quality revisits 2025). |
| **Partial** | Validation culture exists for defect/LLM benchmarks; not for instruction-discovery frames. |
| **Unsolved** | Construction of **membership-labeled** instruction-artifact frames with protocol-sensitivity reporting. |
| **Closest** | Herbold 2022; Golzadeh 2021 (bots GT); SWE-bench line. |
| **Why not us** | Different constructs (bugs, bots, issue resolution), though the **method pattern** (manual GT + process audit) is cousin-level. |

### 13–14. Research artifacts / reproducibility

| | |
|---|---|
| **Solved** | Artifacts should be released and evaluated (Heumüller; Winter; Liu); repository studies are hard to replay (González-Barahona 2011/2023). |
| **Partial** | Norms exist; many studies still under-specify filters/labels. |
| **Unsolved** | Not a scientific “unknown”—this is a delivery expectation. Packaging alone is **not** novelty. |
| **Closest** | Heumüller 2020; Winter 2022; Liu 2024; González-Barahona 2023. |
| **Why not us** | Necessary hygiene. If positioned as primary contribution, novelty is weak. |

### 15. Reporting guidelines

| | |
|---|---|
| **Solved** | Case-study, experiment, mapping, empirical-standards reporting lineages (Runeson; Jedlitschka; Petersen; Ralph/SIGSOFT). |
| **Partial** | Generic checklists do not name instruction-artifact predicate families or consensus protocols as mandatory reportables. |
| **Unsolved** | Domain-specific reporting items for **instruction-artifact discovery frames**. |
| **Closest** | Baltes & Ralph 2022; Verdecchia 2023. |
| **Why not us** | Guidelines without empirical demonstration of *why those items matter* (protocol sensitivity / family structure) are incremental. |

### 16. Metadata quality

| | |
|---|---|
| **Solved** | Stars/social signals are fragile (Borges 2016; Tsay 2014). |
| **Partial** | Metadata sparsity interacts with coding difficulty—known qualitatively. |
| **Unsolved** | Systematic link from metadata sparsity → disagreement → contamination-rate instability for instruction frames. |
| **Closest** | Borges; Tsay; Kalliamvakou. |
| **Why not us** | They warn about proxies; they do not measure our estimand. |

### 17–19. Human / consensus / multi-annotator protocols

| | |
|---|---|
| **Solved** | κ and agreement reporting (Cohen; Landis & Koch); multi-coder practice is standard ESE. |
| **Partial** | Papers report agreement; fewer treat **consensus rule choice** as changing the scientific estimand. |
| **Unsolved** | Showing complementary consensus protocols yield **different contamination rates** on the same repositories, with disagreement concentrated at membership boundaries. |
| **Closest** | Cohen; Landis & Koch; Golzadeh (multi-coder GT pattern); Runeson (triangulation). |
| **Why not us** | Tools and norms exist; the **estimand-level consequence** for instruction-frame contamination is not established in prior work we verified. |

**Critical note:** Multi-coder worksheets are **not** novel. Protocol-sensitivity of a prevalence estimand can be.

### 20–21. LLM / AI-assisted annotation

| | |
|---|---|
| **Solved** | LLMs can annotate some text tasks (Gilardi 2023); LLM-as-judge evaluation exists (Zheng 2023); SE-specific caution (Ahmed 2025). |
| **Partial** | Transfer to SE membership labels is contested. |
| **Unsolved** | Not our core gap. Using LLMs as primary membership oracles would be scientifically risky given conflicting evidence. |
| **Closest** | Ahmed 2025; Gilardi 2023; OLAF 2026 (emerging robust LLM annotation frameworks). |
| **Why not us** | Annotator technology ≠ discovery-frame contamination science. |

### 22–28. AI instruction artifacts / AGENTS.md / Cursor / Claude / Copilot / Promptware / MCP

| | |
|---|---|
| **Solved** | Phenomenon documentation (product docs); promptware as SE object (Chen 2026); Copilot interaction/productivity (Ziegler; Barke; Vaithilingam); LLM4SE maps (Hou; Fan). |
| **Partial** | Conceptual framing of prompts/instructions as artifacts; almost no methodological mining audits. |
| **Unsolved** | **Methodological consequences of using these files as discovery predicates.** |
| **Closest** | Chen 2026 Promptware; grey docs (AGENTS.md, Cursor rules, Copilot instructions, MCP); Copilot empirical studies. |
| **Why not us** | They study tools/phenomena, not sample–target validity of search hits. |

**Critical note:** Presence of grey literature only strengthens **motivation**, not novelty of “files exist.”

### 29. Repository discovery frames

| | |
|---|---|
| **Solved** | Frame/population language in sampling methodology (Baltes & Ralph). |
| **Partial** | Frames are discussed abstractly. |
| **Unsolved** | Concrete frame audits for instruction-artifact discovery with family decomposition. |
| **Closest** | Baltes & Ralph 2022. |
| **Why not us** | Vocabulary without this operationalization. |

### 30. Software Engineering methodology

| | |
|---|---|
| **Solved** | Broad ESE methodology stack (Wohlin; validity debates; reporting). |
| **Partial** | Methodology adapts slowly to new data-generation regimes (agentic SE). |
| **Unsolved** | Methodological standards for **agent-instruction–based corpus construction**. |
| **Closest** | Baltes & Ralph; Verdecchia; Siegmund. |
| **Why not us** | General methodology; not this regime. |

---

## Closest papers overall (ordered by threat to our novelty)

| Rank | Paper | Threat level | Residual gap |
|---:|---|---|---|
| 1 | Kalliamvakou et al. 2014/2015 | **High** | Already proved GitHub sample ≠ claimed population. If we only restate this for new filenames, we lose. |
| 2 | Baltes & Ralph 2022 | **High** | Already demand frames/populations/reporting. If we only “recommend reporting,” we are incremental. |
| 3 | Munaiah 2017 / PHANTOM 2020 | **High** | Automated curation of engineered projects. Reviewers will say “just filter.” Counter: engineered ≠ on-target product role for instruction studies. |
| 4 | Golzadeh et al. 2021 | **Medium** | Membership GT for a GitHub entity class (bots). Pattern cousin; different construct. |
| 5 | Herbold et al. 2022 | **Medium** | Manual validation exposing process/label failure. Cousin for validation ethos; different estimand. |
| 6 | Tantithamthavorn et al. 2017 | **Medium** | Sensitivity of conclusions to methodological choices. Analogical support, different estimand. |
| 7 | Chen 2026 Promptware | **Low–Medium** | Conceptual neighbor for instruction artifacts; no frame audit. |
| 8 | Ahmed 2025 | **Low** | Annotation replacement; not contamination rates. |
| 9 | Lopes / Allamanis / Kaufman | **Low** (but dangerous rhetorically) | Different contamination sense—easy to confuse reviewers if wording is sloppy. |

---

## What scientific problem still exists?

After the verified literature:

### The remaining problem is narrow and methodological

**Problem still open:**

In the emerging regime where GitHub corpora are formed by **searching for AI-instruction artifacts**, the community lacks an empirically grounded account of:

1. **Target-conditional membership error** among repositories that survive ordinary engineered/activity filters;  
2. **Non-exchangeability of discovery predicates** (family-level contamination structure);  
3. **Non-invariance of contamination prevalence to consensus protocol** (the aggregation rule is part of the estimand);  
4. **Where human disagreement concentrates** (membership boundary vs product-role), with inspection that separates those failure modes.

That is a **validity problem for a new discovery regime**, not a discovery that “GitHub is messy.”

### What is *not* still open (do not sell these as gaps)

- That GitHub mining has perils.  
- That sampling frames should be declared.  
- That toy/non-engineered repos should be filtered.  
- That datasets need validation.  
- That artifacts should be released.  
- That multi-coder agreement should be reported.  
- That prompts/Copilot/agents exist.

---

## Novelty verdict (extreme criticism)

### Is the paper novel?

**Conditionally yes — but only in a limited methodological sense.**

It is **not** novel as:

- a theory of GitHub bias;  
- a general sampling methodology;  
- an engineered-repo classifier;  
- an annotation method;  
- a promptware concept paper;  
- a reproducibility sermon.

A hostile but fair one-liner:

> “This is Kalliamvakou + Baltes + standard multi-coding, applied to AGENTS.md-like filenames.”

That attack **succeeds** unless the paper foregrounds evidence that:

- ordinary engineered filters **leave** substantial off-target mass in this regime;  
- **predicate families are not interchangeable**;  
- **consensus protocol changes the contamination rate** on the same repos;  
- disagreement is structurally located at membership boundaries.

Those empirical regularities—if held—are the novelty. The worksheet/package are supporting apparatus, not the scientific claim.

### Where novelty is limited

1. **Single public frame / one study instance** → weak external validity; contribution is protocol + existence proof, not a universal constant.  
2. **Reporting guidance** alone is incremental relative to Baltes & Ralph.  
3. **Three-class coding** is ordinary ESE practice.  
4. **Grey-literature phenomenon** is not a research contribution.  
5. Risk of looking like a sibling of the authors’ own adoption/lifecycle corpus if framing drifts to maintenance/adoption.

### Where contribution may be *stronger* than currently claimed

The current Related Work under-sells the sharpest claim by mixing it with broad surveys (LLM4SE, Copilot productivity, RE GenAI).

The strongest scientific payload is not “we audited a frame,” but:

> **Contamination prevalence for instruction-artifact discovery is a protocol-dependent estimand, and predicate families induce structured—not merely noisy—misalignment.**

If results support that, this is closer to a **measurement-validity contribution for a new MSR regime** than to a descriptive dataset paper. That is stronger, and still honest—provided claims stay within one frame and do not pretend to rewrite MSR sampling theory.

### Where contribution may be *weaker* than claimed

If results show only that “some repos are off-target” without:

- meaningful protocol sensitivity, or  
- stable family structure, or  
- boundary-concentrated disagreement,

then the paper collapses to a **case study illustration of known perils**, and novelty is insufficient for IST as currently pitched.

---

## Strongest honest positioning (recommended)

### Title-level positioning (conceptual)

**Not:** “GitHub samples are contaminated.”  
**Not:** “A new sampling theory.”  
**Yes:** “Validity auditing for AI-instruction discovery frames on GitHub.”

### One-paragraph positioning (camera-ready honesty)

Empirical software engineering is beginning to assemble GitHub corpora by searching for agent-instruction files. Prior MSR research already established that retrieval does not equal population membership (Kalliamvakou), that sampling frames must be declared (Baltes & Ralph), and that engineered-project filters remove some non-software noise (Munaiah; PHANTOM). Those results do **not** determine whether repositories retrieved via instruction-file predicates match a study’s analytic target, whether that mismatch is uniform across predicate families, or whether multi-coder consensus rules change the resulting contamination rate. This paper treats that triple as the object of study: it contributes an operational audit protocol and empirical evidence—from one public instruction-artifact frame—that contamination estimates are protocol-sensitive while family-level structure remains informative, and it releases worksheets and replay scripts so others can repeat the checks before scaling claims.

### Contribution hierarchy (what to claim / demote)

| Claim | Strength | Keep? |
|---|---|---|
| Consensus protocol changes contamination rates on the same labeled set | **Primary scientific claim** (if results hold) | Keep as #1 |
| Misalignment clusters by predicate family (families not exchangeable) | **Primary structural claim** | Keep as #1/#2 |
| Disagreement concentrates at membership boundaries; inspect separates boundary vs role | **Supporting mechanistic claim** | Keep |
| Worksheet + replay package for instruction-artifact frames | **Methodological artifact** | Keep as enabler, not sole claim |
| Reporting checklist items (target, families, consensus protocol) | **Derived guidance** | Keep secondary |
| “GitHub is perilous” / “release artifacts” / “LLMs can annotate” | **Background only** | Do not claim as contribution |

### Positioning relative to closest priors (explicit differentiation sentence)

Unlike Kalliamvakou, we do not stop at documenting perils; unlike Baltes & Ralph, we do not stop at guidelines; unlike RepoReapers/PHANTOM, we do not treat engineeredness as the membership construct; unlike leakage/duplication work, we do not redefine contamination as train/test pollution; unlike Promptware/Copilot studies, we do not study assistant utility—we study **whether instruction-file search hits belong in the population the study claims**.

---

## Final answer

**What scientific problem still exists after reviewing all the literature?**

> A validity gap in a new discovery regime: when GitHub frames are built from AI-instruction path predicates, the field still lacks evidence-based methods to quantify **target-conditional membership error**, its **predicate-family structure**, and the **dependence of contamination prevalence on consensus aggregation**—after ordinary MSR filters have already been applied.

**Novelty:** limited but real **if and only if** the paper’s distinctive empirical regularities (protocol sensitivity + family structure + boundary disagreement) are the center of the claim.  
**If those are soft-pedaled** in favor of “we provide reporting guidance and a replication package,” novelty is **insufficient** relative to Baltes/Kalliamvakou/Munaiah.  
**If those are demonstrated cleanly,** the paper is a legitimate IST methodological contribution—not a paradigm shift, not a restatement of perils, but a **measurement-validity audit for agent-instruction discovery frames**.
