# Related Work traceability matrix

**Source text:** `papers/sections/07_related_work.tex` (current rebuilt Related Work).  
**Rule applied:** every scientific statement needs ≥1 verified citation that actually supports *that* claim.  
**Strength scale:** Strong / Moderate / Weak / Analogy-only / None.  
**Confidence:** High / Medium / Low (that the claim is both true *and* honestly supported by the cited work).

**Legend for “Unsupported”:** claim has no adequate verified citation for the precise assertion (missing cite, wrong cite job, or leap beyond what the reference shows).

---

## Paragraph inventory

Paragraphs are numbered in reading order within each subsection. Multi-sentence blocks that form one logical paragraph in the `.tex` are one unit; compound paragraphs are split into **claims** (rows).

---

## 0. Opening (lines 4–10)

### ¶0.1 Phenomenon + retrieval ≠ membership

| # | Scientific claim | Supporting refs | Strength | Contradictory evidence | Confidence |
|---|---|---|---|---|---|
| 0.1a | ESE *increasingly* forms GitHub corpora by searching for agent-instruction files | *(none peer-reviewed)*; grey docs only show files *exist* | **None** for “increasingly” / practice prevalence | No survey of MSR sampling practice using `AGENTS.md`/Cursor rules cited | **Low** |
| 0.1b | A path match is a retrieval event, not membership proof for the analytic population | Conceptual; weakly backed by Kalliamvakou/Baltes only as *general* mismatch | Weak (definitional) | — | Medium (as definition); Low as empirical claim |
| 0.1c | Doc mirrors, prompt packs, coursework, AI-builder tooling can satisfy the same discovery predicate as conventional apps | **None** for instruction predicates; Kalliamvakou shows *other* non-project / wrong entities | **None** for listed artifact types | — | **Low** |
| 0.1d | Contaminated repos in the denominator bias downstream statistics if membership is assumed | `kalliamvakou2014`, `kalliamvakou2015indepth`, `zimmermann2008` | Moderate for general mismatch/domain effects; Weak for instruction-frame denominators | — | Medium |
| 0.1e | Sample–target mismatch on GitHub is already established (not newly discovered) | `kalliamvakou2014`, `kalliamvakou2015indepth`, `baltes2022sampling`, `howison2004perils` | **Strong** | — | **High** |
| 0.1f | Open question: instruction-artifact frames need audit that is target-conditional, family-structured, protocol-sensitive | Framing claim / gap assertion | None (this paper’s question) | Closest priors solve adjacent problems (Munaiah, Baltes) | Medium as *gap framing*; N/A as fact |
| 0.1g | Instruction-file predicates are easy to operationalize as search queries | `agentsmd2025`, `cursor2024docs`, `brown2024copilot`, `claude2024docs`, `anthropic2024mcp` | **Strong** as primary-source predicate existence | — | **High** |
| 0.1h | Corresponding membership checks remain *largely implicit* in published empirical designs | `baltes2022sampling`, `chen2025promptware`, `hou2024llm4se` | **Weak**: absences inferred from surveys/guidelines, not a dedicated negative search report | Possible unpublished / niche studies not cited | **Low** |

**Unsupported / under-supported in ¶0.1:** **0.1a**, **0.1c**, **0.1h** (and 0.1b if treated as empirical rather than definitional).

---

## 1. MSR methodology (`subsec:rw-msr`)

### ¶1.1 History + infrastructure

| # | Claim | Refs | Strength | Contradictory | Confidence |
|---|---|---|---|---|---|
| 1.1a | MSR recovers process/product knowledge from archival data | `hassan2008road` | Strong | — | High |
| 1.1b | Convenience of repos does not guarantee construct match | `hassan2008road`, `wohlin2012` | Moderate (Wohlin general; Hassan agenda) | — | High |
| 1.1c | Event streams/mirrors lowered candidate-set cost | `gousios2013`, `gousios2014lean` | Strong | — | High |
| 1.1d | Commit tooling reduced history-traversal burden | `spadini2018pydriller` | Strong | — | High |
| 1.1e | Cross-forge corpora expand coverage beyond one forge API | `ma2019woc`, `pietri2019swh`, `dicossmo2017softwareheritage` | Strong | — | High |
| 1.1f | Mapping catalogues topical breadth of GitHub SE research | `cosentino2017mapping` | Strong | — | High |

**Unsupported:** none in ¶1.1 (descriptive cites fit).

### ¶1.2 Access solved; membership not

| # | Claim | Refs | Strength | Contradictory | Confidence |
|---|---|---|---|---|---|
| 1.2a | This line largely solves access and extraction cost | Synthesis of ¶1.1 cites | Moderate (author synthesis) | Coverage still incomplete in practice | Medium |
| 1.2b | It does *not* establish that path/filename retrieval implies population membership | Logical; no direct cite on sentence | **None on sentence**; implied by Baltes/Kalliamvakou elsewhere | — | Medium as logic; **unsupported as cited claim** |
| 1.2c | When discovery is cheap, binding constraint shifts to target match; retrieval completeness cannot answer validity | `baltes2022sampling`, `wohlin2012`, `runeson2009` | Moderate (Baltes strongest; Runeson weaker fit) | — | Medium |
| 1.2d | MSR methodology is backdrop, not the instruction-frame audit | Positioning | None needed | — | High as author stance |

**Unsupported:** **1.2b** (asserted without local citation).

---

## 2. Repository discovery and GitHub sampling

### ¶2.1 Sampling practice + metadata + archives

| # | Claim | Refs | Strength | Contradictory | Confidence |
|---|---|---|---|---|---|
| 2.1a | Dabic examines how MSR studies sample projects / shape corpora | `dabic2021sampling` | Strong | — | High |
| 2.1b | Baltes & Ralph: frames, populations, generalization must be explicit | `baltes2022sampling` | Strong | — | High |
| 2.1c | Stars/social signals are fragile popularity/contribution proxies | `borges2016popularity`, `tsay2014influence` | Strong | — | High |
| 2.1d | Therefore metadata ranking alone does not settle membership | Inference from 2.1c | Moderate | — | High |
| 2.1e | SWH/WoC redesign discovery for archive-scale coverage/provenance | `ma2019woc`, `pietri2019swh`, `dicossmo2017softwareheritage` | Strong | — | High |
| 2.1f | Larger coverage still leaves membership as author-defined validity judgment | `baltes2022sampling` | Moderate (Baltes on frames; not about WoC specifically) | — | Medium |

**Unsupported:** none critical; **2.1f** is a mild over-extension of Baltes onto WoC/SWH.

### ¶2.2 Engineered curation residual

| # | Claim | Refs | Strength | Contradictory | Confidence |
|---|---|---|---|---|---|
| 2.2a | RepoReapers classifies engineered vs non-engineered | `munaiah2017curating` | Strong | — | High |
| 2.2b | PHANTOM revisits curation with time-series clustering | `phantom2020` | Strong | — | High |
| 2.2c | Filters remove substantial non-software noise; often right first screen | `munaiah2017curating`, `phantom2020`, `kalliamvakou2015indepth` | Strong for noise reduction | — | High |
| 2.2d | Engineered ≠ membership in study-specific analytic population for instruction-artifact research | Logical residual; cites don’t study instruction frames | **Analogy / logic only** | — | Medium |
| 2.2e | Engineered AI-builder SDK / prompt pack / doc mirror / coursework can survive engineered+activity filters while off-target for conventional-application studies | `munaiah2017curating`, `phantom2020`, `baltes2022sampling` | **Weak**: plausible given filter objectives; **not empirically shown** for those artifact types | If RepoReapers catches some “tooling” as non-engineered, claim narrows | **Low** |
| 2.2f | Same repo may be on-target for an AI-tooling study | Definitional target-conditionality | None | — | High as logic |
| 2.2g | Prevalence is target-conditional; cannot collapse to universal “is engineered?” | `baltes2022sampling`, `wohlin2012` | Moderate (theory); Strong as logical consequence of 2.2f | — | High |

**Unsupported / under-supported:** **2.2e** (key residual claim without empirical demonstration). **2.2d** under-cited if presented as fact rather than argument.

### ¶2.3 Operational remainder + family breakdown

| # | Claim | Refs | Strength | Contradictory | Confidence |
|---|---|---|---|---|---|
| 2.3a | Discovery infra + sampling guidelines leave an operational remainder | Synthesis | Weak | — | Medium |
| 2.3b | They do not specify how to audit frames whose inclusion event is “contains instruction file X” | `dabic2021sampling`, `baltes2022sampling` | **Weak**: negative claim from absence in those papers | Undiscovered methods papers | Low–Medium |
| 2.3c | They do not specify reporting whether heterogeneous instruction predicates induce heterogeneous contamination | same | **Weak** (gap by absence) | — | Low–Medium |
| 2.3d | Frame-wide contamination % without predicate-family breakdown answers the wrong question when filenames index different roles | `dabic2021sampling`, `baltes2022sampling`, `chen2025promptware` | **Weak**: Baltes/Dabic support stratified reporting generally; Chen does not show heterogeneous contamination by family | — | **Low** |

**Unsupported:** **2.3d** as empirical claim about instruction families (circular: this paper’s result, not prior evidence). Cite support is wrong job for Chen.

---

## 3. Construct validity and sampling bias

### ¶3.1 Perils + ToV lineage

| # | Claim | Refs | Strength | Contradictory | Confidence |
|---|---|---|---|---|---|
| 3.1a | SourceForge status/metadata mislead naive samples | `howison2004perils` | Strong | — | High |
| 3.1b | Many GitHub entities are not software projects; activity proxies unreliable; pipelines inherit mismatches | `kalliamvakou2014`, `kalliamvakou2015indepth` | Strong | — | High |
| 3.1c | Operational definitions/constructs are first-class validity objects | `wohlin2012`, `runeson2009` | Strong | — | High |
| 3.1d | Community disagrees on priority of internal vs external validity | `siegmund2015views` | Strong | — | High |
| 3.1e | Undeclared analytic targets especially risky when generalizing from retrieved samples | Inference from 3.1d + Baltes ethos | Moderate | — | Medium |
| 3.1f | Ampatzoglou taxonomize ToV in secondary studies | `ampatzoglou2019threats` | Strong | — | High |
| 3.1g | Verdecchia urge stronger alignment claimed vs measured constructs | `verdecchia2023threats` | Strong | — | High |
| 3.1h | Tangled commits break intended commit–defect links | `herzig2013tangled` | Strong (different construct) | — | High for claim; Low relevance |

**Unsupported:** none for stated claims; **3.1h** is supported but *tangential* (noise, not unsupported).

### ¶3.2 Implications for instruction frames

| # | Claim | Refs | Strength | Contradictory | Confidence |
|---|---|---|---|---|---|
| 3.2a | Peril includes path predicates retrieving *real software* of wrong product role | `kalliamvakou2015indepth`, `baltes2022sampling` | Moderate (general mismatch); **Weak** for “product role” / path predicates specifically | Kalliamvakou emphasize non-projects more than wrong product role | Medium |
| 3.2b | That mismatch survives toy/empty filters | `munaiah2017curating`, `phantom2020` | **Analogy**: filters remove non-engineered; do not prove survival of wrong-role engineered repos | — | **Low** |
| 3.2c | ToV lists without naming target, predicates, and label-aggregation leave estimand under-specified | `verdecchia2023threats`, `siegmund2015views`, `baltes2022sampling` | Moderate | — | Medium |
| 3.2d | Sampling-bias research motivates audit without performing it for AI-instruction discovery | Gap / positioning | None | — | Medium |
| 3.2e | Contribution boundary: not “can samples be wrong?” but how to audit instruction frames for measurable, comparable, protocol-aware wrongness | `kalliamvakou2015indepth`, `baltes2022sampling`, `verdecchia2023threats` | Weak as *citation support for novelty*; Strong as framing | — | Medium framing |

**Unsupported / under-supported:** **3.2b**; **3.2a** partially (product-role specificity).

---

## 4. Dataset contamination and adjacent senses

### ¶4.1 Leakage / duplication / domain mismatch

| # | Claim | Refs | Strength | Contradictory | Confidence |
|---|---|---|---|---|---|
| 4.1a | “Contamination” is overloaded; senses must be kept distinct | Meta / editorial | None | — | High as caution |
| 4.1b | Kaufman formalizes train/test leakage | `kaufman2012` | Strong | — | High |
| 4.1c | Moreno-Torres unify dataset shift | `moreno2012` | Strong | — | High |
| 4.1d | Kapoor & Narayanan document leakage-driven reproducibility failures | `kapoor2023leakage` | Strong | — | High |
| 4.1e | DéjàVu maps massive GitHub duplication | `lopes2017dejavu` | Strong | — | High |
| 4.1f | Allamanis: duplication inflates learned evaluations | `allamanis2019duplication` | Strong | — | High |
| 4.1g | Cross-project DP: domain mismatch collapses performance even when retrieval succeeds | `zimmermann2008` | Strong | — | High |

**Unsupported:** none.

### ¶4.2 Label quality + validation sensitivity

| # | Claim | Refs | Strength | Contradictory | Confidence |
|---|---|---|---|---|---|
| 4.2a | NASA defect data quality issues | `shepperd2013nasa` | Strong | — | High |
| 4.2b | Researcher/process bias in defect prediction | `shepperd2014bias` | Strong | — | High |
| 4.2c | SZZ/feature failures under manual validation | `herbold2022szz` | Strong | — | High |
| 4.2d | Benchmark construction insists on explicit scope/filtering | `dambros2012defectbenchmark`, `tantithamthavorn2017validation`, `jimenez2024swebench` | Moderate–Strong; SWE-bench is stretch for “filtering” as general principle | — | Medium |
| 4.2e | Model-validation technique choice can change conclusions with fixed defect data | `tantithamthavorn2017validation` | Strong | — | High |

**Unsupported:** none; **4.2d** slightly over-cites SWE-bench for the general claim.

### ¶4.3 Distinguishing senses + practical risk

| # | Claim | Refs | Strength | Contradictory | Confidence |
|---|---|---|---|---|---|
| 4.3a | Unvalidated denominators / brittle operationalizations bias downstream claims | `herbold2022szz`, `shepperd2013nasa`, `zimmermann2008` | Moderate (analogy across settings) | — | Medium |
| 4.3b | Those results do not solve path-search population mismatch for instruction frames | Gap | None | — | High as negation |
| 4.3c | Leakage/duplication ≠ sample–target contamination (wrong repos in population even with no model) | `kalliamvakou2015indepth`, `baltes2022sampling` | Strong conceptually | — | High |
| 4.3d | Equating senses would mis-cite prior work and obscure estimand | Editorial logic | None | — | High |
| 4.3e | Reuse validation ethos; keep construct distinct | `herbold2022szz`, `dambros2012defectbenchmark` | Moderate | — | High |
| 4.3f | Practical risk: denominator mixes on-target apps with off-target instruction hosts that still look like software projects | `kalliamvakou2015indepth`, `munaiah2017curating`, `lopes2017dejavu` | **Weak**: cites support *possibility* of mismatch/engineered noise/duplication, not instruction-host mixing | — | **Low** |

**Unsupported:** **4.3f** (central risk statement for the case; not shown by cited papers).

---

## 5. Reporting guidelines and reproducibility

### ¶5.1 Norms exist

| # | Claim | Refs | Strength | Contradictory | Confidence |
|---|---|---|---|---|---|
| 5.1a | Case-study guidelines; experiment reporting; mapping updates; empirical standards | `runeson2009`, `jedlitschka2005reporting`, `petersen2015mapping`, `ralph2021standards` | Strong | — | High |
| 5.1b | Disclosure of design choices that determine the estimand improves comparability | `jedlitschka2005reporting`, `runeson2009`, `ralph2021standards` | Moderate | — | Medium |
| 5.1c | Replication mapping / artifact studies: uneven replayability, scarce artifacts | `silva2012replication`, `heumuller2020`, `winter2022artifacts`, `liu2024researchartifacts` | Strong | — | High |
| 5.1d | Repo studies hard to reproduce when retrieval/filters/labels underspecified | `gonzalez2011repro`, `gonzalez2023revisit` | Strong | — | High |
| 5.1e | Barriers persist a decade later | `gonzalez2023revisit` | Strong | — | High |

**Unsupported:** none.

### ¶5.2 Norms ≠ empirical hinge for instruction frames

| # | Claim | Refs | Strength | Contradictory | Confidence |
|---|---|---|---|---|---|
| 5.2a | Norms justify releasing worksheets, frozen labels, alternative-protocol scripts | `heumuller2020`, `winter2022artifacts`, `liu2024researchartifacts` | Moderate (artifact ethos; not specific checklist items) | — | Medium |
| 5.2b | They do not substitute for evidence that reporting items are *consequential* in instruction frames (protocols/families change rate meaning) | `baltes2022sampling`, `tantithamthavorn2017validation` | **Analogy only** for consequentiality; instruction-frame evidence is *this paper* | — | Low for prior literature; High as gap |
| 5.2c | Reporting guidance without empirical hinge remains generic vs Baltes | `baltes2022sampling` | Moderate | — | High |
| 5.2d | Replication package alone is hygiene, not scientific claim | `heumuller2020`, `gonzalez2023revisit` | Moderate (author valuation) | Artifact venues treat packages as contributions | Medium |

**Unsupported as prior evidence:** **5.2b**’s consequentiality claim (correctly framed as gap, but cites are analogies).

---

## 6. Human annotation and consensus protocols

### ¶6.1 Tools and cousins

| # | Claim | Refs | Strength | Contradictory | Confidence |
|---|---|---|---|---|---|
| 6.1a | Chance-corrected agreement + interpretation benchmarks are coding baseline | `cohen1960kappa`, `landis1977kappa` | Strong | Kappa limitations literature exists (not cited) | High |
| 6.1b | Multi-coder protocols/triangulation standard in ESE case research | `runeson2009` | Strong | — | High |
| 6.1c | Golzadeh: membership GT for GitHub bots via careful labeling | `golzadeh2021bots` | Strong | — | High |
| 6.1d | Herbold: manual validation exposes automated labeling failure | `herbold2022szz` | Strong | — | High |
| 6.1e | Human inspection as corrective for process-induced error | `shepperd2013nasa`, `shepperd2014bias` | Moderate | — | High |

**Unsupported:** none; optional contradict: kappa criticism literature omitted (not fatal).

### ¶6.2 Consensus rule as part of estimand

| # | Claim | Refs | Strength | Contradictory | Confidence |
|---|---|---|---|---|---|
| 6.2a | Agreement tools + multi-coder discipline are solved | `cohen1960kappa`, `landis1977kappa`, `runeson2009` | Strong for availability | Practice often weak | High |
| 6.2b | Status of *consensus rule* as part of prevalence estimand is weakly treated | Gap assertion | **None** | Some survey methodology treats aggregation rules; not cited | Medium |
| 6.2c | Methodological choices can change conclusions with fixed observations | `tantithamthavorn2017validation` | Strong (model validation domain) | — | High in domain |
| 6.2d | Therefore contamination rate under one tie-break/majority rule should not be treated as protocol-invariant without evidence | `tantithamthavorn2017validation`, `baltes2022sampling`, `verdecchia2023threats` | **Analogy transfer** | — | Medium |
| 6.2e | Prior work lacks complementary consensus estimates of instruction-frame contamination on same repos; lacks locating disagreement at membership boundaries vs product-role classes for this regime | `golzadeh2021bots`, `herbold2022szz` (as cousins that don’t do this) | Weak (negative claim) | Undiscovered literature | Medium |

**Unsupported:** **6.2b** (no cite establishing “weakly treated”); **6.2e** depends on unreported negative search.

---

## 7. LLM-assisted annotation

### ¶7.1 Conflicting evidence survey

| # | Claim | Refs | Strength | Contradictory | Confidence |
|---|---|---|---|---|---|
| 7.1a | LLMs increasingly used as annotators/judges | Opening; weakly supported by following cites | Weak for “increasingly” | — | Medium |
| 7.1b | ChatGPT can outperform crowd workers on some text-annotation tasks | `gilardi2023chatgpt` | Strong | Replication/domain limits | High |
| 7.1c | Zheng evaluates LLM-as-judge reliability | `zheng2023judge` | Strong | — | High |
| 7.1d | Ahmed: cautious SE-specific answer on replacing manual annotation | `ahmed2025llms` | Strong | — | High |
| 7.1e | Human–AI guidelines caution unsupervised automation of consequential judgments | `amershi2019humanai` | Moderate (HCI guidelines ≠ membership labeling) | — | Medium |
| 7.1f | Preliminary RE ChatGPT uses need human oversight | `fantechi2023` | Weak venue/claim weight | — | Low–Medium |

**Unsupported:** **7.1a** “increasingly” without prevalence cite.

### ¶7.2 Transfer refusal

| # | Claim | Refs | Strength | Contradictory | Confidence |
|---|---|---|---|---|---|
| 7.2a | Evidence conflicting across domains | Synthesis of 7.1 | Strong | — | High |
| 7.2b | Optimistic NLP results do not automatically transfer to repo membership boundaries where metadata sparsity and product-role ambiguity concentrate disagreement | `gilardi2023chatgpt`, `ahmed2025llms`, `kalliamvakou2015indepth`, `borges2016popularity` | Moderate (Ahmed supports caution; sparsity/ambiguity partly inferred) | Gilardi optimistic | Medium |
| 7.2c | LLM assistance at best optional adjudication under audit; not substitute for human-coded protocol with measurable consensus sensitivity | `ahmed2025llms`, `amershi2019humanai`, `cohen1960kappa` | Moderate (normative from Ahmed) | Gilardi-style optimism | Medium |
| 7.2d | Treating LLM labels as authoritative membership imports unsettled transfer assumptions | `ahmed2025llms`, `gilardi2023chatgpt` | Strong as methodological warning | — | High |

**Unsupported:** none critical if 7.2c is normative; **7.2b** “concentrate disagreement” is anticipatory of this paper’s results.

---

## 8. AI instruction artifacts

### ¶8.1 Phenomenon cluster

| # | Claim | Refs | Strength | Contradictory | Confidence |
|---|---|---|---|---|---|
| 8.1a | Prompts, agent memory, tool interfaces becoming SE objects | `chen2025promptware`, `hou2024llm4se`, `fan2023` | Strong | — | High |
| 8.1b | Copilot studies characterize productivity/interaction, not corpus construction | `ziegler2024copilot`, `barke2023groundedcopilot`, `vaithilingam2022expectation` | Strong | — | High |
| 8.1c | Earlier bot work anticipated workflow automation without treating instruction files as sampling predicates | `storey2020` | Weak–Moderate | — | Medium |
| 8.1d | Primary docs specify concrete filenames/config surfaces searchable by miners | five grey docs | Strong (primary) | — | High |

**Unsupported:** none for 8.1a–d as stated.

### ¶8.2 Does not audit frames

| # | Claim | Refs | Strength | Contradictory | Confidence |
|---|---|---|---|---|---|
| 8.2a | Cluster documents phenomenon making instruction-file discovery available | Synthesis | Strong | — | High |
| 8.2b | Does not audit whether retrieved repos match claimed population; no family-level contamination reporting | `chen2025promptware`, `baltes2022sampling` | Weak (absence) | Own corpus paper if over-read | Medium |
| 8.2c | Scarcity of peer-reviewed methodological work on these predicates; practice can adopt affordances faster than methodology audits them | `hou2024llm4se`, `fan2023`, `chen2025promptware` | **Weak**: surveys don’t prove scarcity of *sampling* methods; “faster than” is narrative | Possible grey empirical mining studies | **Low** |

**Unsupported:** **8.2c** (motivation leap).

---

## 9. Existing studies using AI instruction artifacts

### ¶9.1 Cluster description

| # | Claim | Refs | Strength | Contradictory | Confidence |
|---|---|---|---|---|---|
| 9.1a | Published work clusters around tool use/adoption/capability, not discovery-frame validity | Synthesis | Moderate | — | Medium |
| 9.1b | Copilot studies measure interaction/productivity | Ziegler/Barke/Vaithilingam | Strong | — | High |
| 9.1c | Promptware articulates engineering concerns for prompt-enabled systems | `chen2025promptware` | Strong | — | High |
| 9.1d | LLM4SE surveys map tasks/open problems | `hou2024llm4se`, `fan2023` | Strong | — | High |
| 9.1e | Companion corpus charts instruction-file spread / adoption–maintenance | `ai_convention_lifecycle_corpus2026` | Strong for own corpus; **weak as independent prior** | Self-citation novelty risk | Medium (fact); Low (editorial) |
| 9.1f | SWE-bench filtering shapes evaluation populations; inclusion ≠ instruction-file presence | `jimenez2024swebench` | Strong for filtering; Strong for distinction | — | High |

**Unsupported:** none factually; **9.1e** is self-cite (editorial, not evidential independence).

### ¶9.2 Instrumental retrieval; cousins fall short

| # | Claim | Refs | Strength | Contradictory | Confidence |
|---|---|---|---|---|---|
| 9.2a | Across studies, retrieving repos with instruction artifacts is typically instrumental | `ziegler2024copilot`, `chen2025promptware`, `ai_convention_lifecycle_corpus2026` | Moderate; Copilot studies often *don’t* retrieve by instruction file | — | Medium |
| 9.2b | Membership (conventional apps vs AI tooling vs non-products) rarely the estimand; consensus-protocol sensitivity of contamination not reported | `baltes2022sampling`, `kalliamvakou2015indepth`, `tantithamthavorn2017validation` | **Weak**: cites don’t survey instruction studies; negative claim | — | **Low** |
| 9.2c | Grey docs are phenomenon evidence, not methodological audit | five docs | Strong | — | High |
| 9.2d | Closest methodological cousins: perils, sampling guidelines, engineered curation — none operationalize instruction-predicate family structure or consensus sensitivity for this regime | `kalliamvakou2015indepth`, `baltes2022sampling`, `munaiah2017curating`, `phantom2020` | Moderate (accurate residual if “this regime” true) | Depends on negative search quality | Medium |

**Unsupported:** **9.2a** partially (over-claims Copilot as instruction-file retrieval); **9.2b**.

---

## 10. What remains unsolved

### ¶10.1 Solved / partial / unsolved synthesis

| # | Claim | Refs | Strength | Contradictory | Confidence |
|---|---|---|---|---|---|
| 10.1a | Already solved (awareness/infra): perils, sampling-frame expectations, engineered curation for some Qs, leakage/duplication senses, label-validation culture, agreement tools, artifact/repro norms | long cite lists | Strong for each bullet’s *existence* | “Solved” overstates (awareness ≠ solved practice) | Medium |
| 10.1b | Partially solved: operational audits for new predicates; ToV without estimand worksheets; sensitivity culture elsewhere; LLM annotation transfer under conflict | Ampatzoglou/Verdecchia/Siegmund; Tantithamthavorn; Gilardi/Ahmed | Moderate | — | Medium |
| 10.1c | Unsolved jointly: target-conditional contamination + family structure + consensus protocols + boundary vs role disagreement + replayable worksheets | Gap list | **None** (author synthesis) | Any paper that jointly closes this would falsify | Medium–Low without documented search protocol |
| 10.1d–j | Closest neighbors fall short for stated structural reasons (Kalliamvakou, Baltes, RepoReapers/PHANTOM, leakage/dup, Promptware/Copilot, LLM annotation, Golzadeh) | respective cites | Strong as *characterization of those papers* | — | High |

**Unsupported:** **10.1c** “no verified peer-reviewed study closes jointly” — **strongest negative claim in the section; unsupported without explicit negative-search appendix**.

---

## 11. Why this article is needed

### ¶11.1 Necessity

| # | Claim | Refs | Strength | Contradictory | Confidence |
|---|---|---|---|---|---|
| 11.1a | MSR *begins* to assemble corpora by searching for agent-instruction files | grey docs + `chen2025promptware` | **Weak**: docs enable search; Promptware ≠ MSR corpus practice | — | **Low** |
| 11.1b | Perils/engineered filters/guidelines leave researchers without evidence-based checks when off-target repos may still look engineered | Kalliamvakou, Munaiah, PHANTOM, Baltes | Moderate residual logic | — | Medium |
| 11.1c | Without family-level reporting, heterogeneous predicates collapse into one uninterpretable rate | `dabic2021sampling`, `baltes2022sampling` | Moderate general; Weak for instruction predicates | — | Medium |
| 11.1d | Without consensus-protocol sensitivity, single % easy to over-interpret as protocol-invariant | `tantithamthavorn2017validation`, `cohen1960kappa`, `verdecchia2023threats` | Analogy | — | Medium |
| 11.1e | Without replayable worksheets, community cannot compare audits / revisit membership | `heumuller2020`, `gonzalez2023revisit`, `silva2012replication`, `winter2022artifacts` | Moderate | — | Medium |
| 11.1f | Literature says samples can be wrong; not how wrongness behaves under AI-instruction path predicates + multi-coder contamination rate | Baltes, Tantithamthavorn, Promptware | Gap | — | Medium |

### ¶11.2 Contribution boundary

| # | Claim | Refs | Strength | Contradictory | Confidence |
|---|---|---|---|---|---|
| 11.2a | Not new theory of GitHub bias / replacement for engineered curation / general sampling methodology | positioning cites | Strong as disclaimer | — | High |
| 11.2b | Artifact release / multi-coder worksheets not novel in isolation | `heumuller2020`, `cohen1960kappa`, `runeson2009` | Strong | — | High |
| 11.2c | Contribution: operational audit for AI-instruction frames + reporting guidance derived from it | `baltes2022sampling`, `verdecchia2023threats`, `sanchez2026vsdlcMiningPilot` | Self-cite for package; guidance claim is this paper | — | Medium |
| 11.2d | If rates move under protocols while family structure remains informative → measurement-validity result, not restatement of perils | `tantithamthavorn2017validation`, Kalliamvakou, Baltes | Conditional on Results | — | High as conditional |

**Unsupported:** **11.1a** (practice prevalence).

---

## Master list: unsupported or under-supported statements

| ID | Statement (short) | Problem | Fix for editorial strength |
|---|---|---|---|
| **U1** | ESE *increasingly* mines GitHub via instruction-file search | No peer-reviewed prevalence evidence | Soften to “can” / “are beginning to be usable as predicates”; or cite dated negative/positive search of MSR papers |
| **U2** | Doc mirrors, prompt packs, coursework, AI-builder tooling satisfy same predicates as apps | Illustrative, uncited for those types | Mark as *examples* / hypotheses; or cite inspection examples from *this* study’s Results (not RW) |
| **U3** | Membership checks *largely implicit* in published designs | Absence inferred from surveys | Explicit negative search sentence + date; or “we found no peer-reviewed audit of …” |
| **U4** | Path/filename retrieval does not establish membership (¶1.2b) | Uncited locally | Add Baltes/Kalliamvakou on that sentence |
| **U5** | Engineered AI-builder/prompt/doc/coursework *survive* RepoReapers/PHANTOM while off-target | Not empirically shown by cites | Demote to “can in principle”; or add residual analysis Results cite |
| **U6** | Toy/empty filters don’t catch wrong product-role software | Same residual leap | Same as U5 |
| **U7** | Frame-wide % without family breakdown is *wrong question* when filenames index different roles | Uses Chen/Baltes for a result this paper must show | Move to contribution/Results; in RW say “guidelines do not require family strata for path predicates” |
| **U8** | Practical risk = mixing apps with instruction hosts that look like software | Not shown by Kalliamvakou/Munaiah/DéjàVu | Case motivation → Results; RW keep as open risk |
| **U9** | Consensus-rule status “weakly treated” in prevalence estimands | Unsupported negative | Soften or cite measurement literature gap explicitly |
| **U10** | No peer-reviewed study jointly closes the five-point residual | Strongest gap claim; search not evidenced in RW | Add “search protocol / date / libraries” footnote or appendix |
| **U11** | MSR *begins* to assemble corpora by instruction-file search | Same as U1 | Soften |
| **U12** | Across “these studies,” retrieval by instruction artifacts is typical | Over-reads Copilot HCI papers | Restrict to corpus/Promptware/own sibling; don’t cite Ziegler for retrieval |
| **U13** | Membership rarely estimand; protocol sensitivity not reported (as survey of instruction studies) | Wrong cites (Baltes/Kalliamvakou/Tantithamthavorn) | Base on §9 cluster characterization only |
| **U14** | Practice adopts discovery affordances *faster than* methodology audits | Narrative | Delete or hedge heavily |
| **U15** | Disagreement concentrates at membership boundaries / product-role ambiguity (in LLM para) | Anticipates Results | Soften to “where ambiguity is plausible given GitHub metadata limits” |

---

## Claims that *are* strongly supported (keep as spine)

- GitHub/forge sample–target mismatch is known (`howison`, `kalliamvakou2015`, `baltes`).
- Engineered curation exists and removes non-software noise (`munaiah`, `phantom`).
- Sampling frames must be explicit (`baltes`, `dabic`).
- Leakage/duplication are distinct contamination senses (`kaufman`/`kapoor`, `lopes`/`allamanis`).
- Protocol/method choices can change conclusions on fixed data (`tantithamthavorn`).
- Agreement tools and multi-coder norms exist (`cohen`, `runeson`); membership GT pattern exists for bots (`golzadeh`).
- LLM annotation evidence conflicts; SE-specific caution (`gilardi` vs `ahmed`).
- Instruction filenames/surfaces are documented (grey primary sources); Promptware/LLM4SE establish SE objects (`chen`, `hou`).
- Neighbor characterizations in §10.1d–j (what each paper *does*) are generally high-confidence.

---

## Editorial summary

| Metric | Count (approx.) |
|---|---:|
| Distinct scientific claims audited | ~95 |
| Strongly supported | ~55 |
| Moderate / analogy | ~25 |
| **Unsupported or under-supported (U1–U15)** | **15** |
| Highest-risk unsupported for desk rejection | **U1/U11** (practice prevalence), **U5/U6** (engineered residual), **U10** (joint gap), **U7/U8** (family/risk as prior fact) |

**Bottom line:** Most *historical* and *cousin-method* statements are well cited. The **unsupported mass sits in the motivation and residual leaps**: that instruction-file mining is already common practice, that engineered filters demonstrably fail on instruction hosts, that family-stratified contamination is already the right question in prior work, and that no study jointly closes the five-point gap. Those must be hedged, moved to Results, or backed by an explicit negative search — not by piling Baltes/Kalliamvakou/Munaiah on sentences they do not support.

---

*Matrix date: 2026-07-22. Based on current `07_related_work.tex` only.*
