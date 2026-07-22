# Gap analysis — Related Work rebuild (IST/JSS)

**Audit date:** 2026-07-22  
**Paper problem (as framed in the manuscript):** GitHub frames built from AI-instruction-file predicates (e.g., `AGENTS.md`, editor rules, Copilot instructions) can include repositories that satisfy a path search but fall outside the analytic population the study claims. The manuscript audits sample–target fit, predicate-family structure, coder disagreement, and **sensitivity of contamination estimates to the consensus protocol**.

**Method:** Systematic queries in Crossref and OpenAlex (2026-07-22), DOI verification via Crossref, URL verification for grey literature, OpenReview for SWE-bench. Unverifiable candidates were discarded (see `verification_log.md`).

---

## 1. What is already solved

| Claim | Evidence | Status |
|---|---|---|
| Mining GitHub (and earlier forges) is perilous: not every entity is a software project; metadata proxies mislead | Howison & Crowston (2004); Kalliamvakou et al. (2014, 2015/16) | **Solved at awareness / taxonomy level** |
| SE sampling often fails to define frames and populations; guidelines exist | Baltes & Ralph (2022) | **Solved as guidance**, not as an operational audit for instruction artifacts |
| Engineered vs non-engineered GitHub projects can be curated | Munaiah et al. (2017); PHANTOM (2020) | **Solved for a different construct** (engineering status) |
| Large-scale discovery infrastructure exists (GHTorrent, World of Code, Software Heritage) | Gousios et al.; Ma et al. (2019); Pietri et al. (2019) | **Solved for coverage/retrieval** |
| Dataset/label quality failures are common and must be validated manually | Shepperd et al. (2013); Herbold et al. (2022); Herzig & Zeller (2013) | **Solved as a general lesson** for defect/data pipelines |
| Duplication and leakage contaminate learned evaluations | Lopes et al. (2017); Allamanis (2019); Kaufman et al. (2012); Kapoor & Narayanan (2023) | **Solved for ML/code-corpus contamination**, different sense of “contamination” |
| Replication packages and artifact evaluation matter | González-Barahona & Robles (2011, 2023); Heumüller et al. (2020); Winter et al. (2022); Liu et al. (2024) | **Solved as community norm** |
| Agreement statistics and multi-coder protocols are standard | Cohen (1960); Landis & Koch (1977); case-study guidelines (Runeson & Höst 2009) | **Solved as measurement tools** |
| LLMs can assist annotation (with caveats) | Gilardi et al. (2023); Ahmed et al. (2025); Zheng et al. (2023) | **Partially solved for annotation cost**, not for frame membership audits |
| Prompt/instruction artifacts are rising SE objects | Chen et al. (2026 Promptware); Copilot studies (Ziegler, Barke, Vaithilingam); product docs | **Solved as phenomenon documentation** |

---

## 2. What is partially solved

1. **Sample–target mismatch in MSR**  
   Kalliamvakou et al. and Baltes & Ralph make the conceptual case. They do **not** quantify how mismatch varies across **instruction-artifact predicate families**, nor how estimates move under **alternative consensus protocols** on the same repositories.

2. **Repository filtering / curation**  
   RepoReapers/PHANTOM filter “engineered” projects. That is a useful prior filter, but **engineering status ≠ membership in a study-specific analytic population** for agent-instruction research (e.g., conventional applications vs AI-builder SDKs vs prompt packs vs coursework mirrors).

3. **Threats-to-validity reporting**  
   Ampatzoglou et al. (2019) and Verdecchia et al. (2023) improve ToV discourse. Siegmund et al. (2015) show disagreement on internal vs external validity priorities. None operationalize a **discover → filter → annotate → inspect** worksheet for instruction-file frames.

4. **Sensitivity analysis culture**  
   Tantithamthavorn et al. (2017) show that validation-technique choice changes conclusions. That supports our **protocol-sensitivity** stance, but their estimand is model performance under CV schemes, not contamination rates under consensus rules.

5. **LLM-assisted labeling of SE artifacts**  
   Ahmed et al. (2025) ask whether LLMs can replace manual annotation. That is adjacent to our human/LLM adjudication discussion, but does not study **target-conditional contamination** of discovery frames.

6. **Bot / entity ground-truth datasets**  
   Golzadeh et al. (2021) show how to build membership ground truth for a GitHub entity class (bots). The **method pattern** (worksheet, multi-coder, model) is transferable; the **construct** is not instruction-artifact population membership.

---

## 3. What nobody has addressed (critical gap)

After verifying the corpus, **we found no peer-reviewed study that jointly**:

1. treats **AI-instruction-file path predicates** as a discovery mechanism for GitHub frames;  
2. defines **contamination** as satisfied search ∧ outside the **stated analytic population** (target-conditional);  
3. measures **sensitivity of binary contamination rates to complementary consensus protocols** on the same labeled set;  
4. reports **predicate-family structure** of misalignment (not only a single frame-wide rate);  
5. separates **membership-boundary disagreement** from product-role classification via a tiered inspect phase; and  
6. releases a **replayable worksheet + frozen labels + alternative-protocol scripts** as reporting guidance for this class of frames.

Closest neighbors and why they fall short:

| Neighbor | Why it does **not** close the gap |
|---|---|
| Kalliamvakou perils | General GitHub perils; no instruction-artifact predicates; no consensus-protocol sensitivity of contamination |
| Munaiah / PHANTOM | Engineered-project curation ≠ analytic-population membership for instruction studies |
| Baltes & Ralph | Sampling guidelines without an empirical instruction-frame audit template |
| Herbold SZZ validation | Dataset/label validation in defect prediction, different construct |
| Lopes / Allamanis duplication | Corpus duplication contamination, not path-search population mismatch |
| Chen Promptware | Conceptual SE framing of prompts; no mining-frame audit |
| Ahmed LLM annotation | Annotator replacement study; not discovery-frame contamination |
| Own prior lifecycle corpus (Zenodo) | Adoption/maintenance framing; not the contamination-audit contribution claimed here |

**Honesty check:** If a reviewer equates “Kalliamvakou already said GitHub is noisy” with our contribution, the paper must emphasize the **operational audit** (protocol sensitivity + predicate families + worksheet + target-conditional contamination). That is where novelty begins. We should **not** claim to invent the idea that GitHub samples can be polluted.

---

## 4. Exactly where our contribution begins

Contribution begins **after** retrieval and **after** generic “filter toy projects” advice:

1. **Construct:** contamination as *sample–target mismatch* for instruction-artifact frames (not engineeredness, not star thresholds, not duplication leakage).  
2. **Method object:** consensus protocol as a first-class determinant of the contamination estimand.  
3. **Structure:** predicate-family (and metadata-sparsity) decomposition rather than a single rate.  
4. **Validation design:** tiered inspection separating boundary disagreement from role classification.  
5. **Reporting artifact:** reusable worksheet + complementary consensus estimates + replay scripts.

---

## 5. Conflicting evidence (do not paper over)

- **LLM annotation quality:** Gilardi et al. (2023) report strong LLM annotation performance on political text; Ahmed et al. (2025) give a more cautious SE-artifact answer. **Disagreement:** domain transfer is not settled; our paper should treat LLM adjudication as optional/audited, not authoritative.  
- **Validity priorities:** Siegmund et al. (2015) document community disagreement on internal vs external validity. **Implication:** reporting analytic targets and protocol choices is necessary precisely because the community does not share one validity hierarchy.  
- **Curation classifiers:** RepoReapers/PHANTOM improve engineered-project recall/precision but can still admit repositories that are “engineered” yet off-target for a conventional-application population (AI SDKs, template orgs, etc.). **Implication:** engineered filters are neither necessary nor sufficient for our contamination construct.

---

## 6. Search coverage note

Peer-reviewed literature on **AGENTS.md / Cursor Rules / Copilot custom instructions / MCP as mining predicates** is still thin; primary documentation is necessarily grey literature. That scarcity is itself part of the motivation: empirical work is adopting these predicates faster than methodology papers are auditing them.
