# Eligible repository sample audit

Generated: 2026-06-19 00:49:54 (local)
Source: `data/interim/eligible_repos.jsonl` (83 repositories at time of report).

Sampling method: deterministic random draw (`random.seed(42)`). Descriptions are **inferred** 
from repository name and matched artifact paths; Phases 1–2 do not persist GitHub descriptions.

## Population snapshot

| Metric | Count |
|--------|------:|
| Total eligible | 83 |
| `agent_product_flag=true` | 80 (96.4%) |
| `agent_product_flag=false` | 3 |

### Instruction artifact categories (all eligible)

- `*.prompt.md`: 20
- `system-prompt.*`: 9
- `AGENTS.md`: 8
- `system_prompt.*`: 6
- `.clinerules`: 6
- `copilot-instructions.md`: 6
- `.cursor/rules`: 5
- `CLAUDE.md`: 5
- `GEMINI.md`: 5
- `prompts/`: 5
- `.github/copilot-instructions.md`: 5
- `.cursorrules`: 3
- `.github/chatmodes`: 2
- `.aider.conf.yml`: 2
- `.aiderignore`: 1
- `.windsurfrules`: 1

## Sample A — 20 random eligible repositories

### 1. `CSlawyer1985/case-type-guide`

- **Stars:** 13
- **Short description:** Inferred AI tooling / agent configuration (`case type guide`); seed hits via *.prompt.md.
- **Why eligible:** ≥10 stars (13); active since 2024-06-01 (last push 2026-01-24); instruction artifact present in code search; not fork/archived/mirror/template; passed keyword heuristics (or agent-product retention); evidence: tests.
- **Instruction artifacts:** queries=['*.prompt.md']; paths=['prompt.md']
- **CI evidence:** None detected
- **Release evidence:** None detected
- **agent_product_flag:** True
- **URL:** https://github.com/CSlawyer1985/case-type-guide

### 2. `AI45Lab/Code`

- **Stars:** 137
- **Short description:** Inferred AI tooling / agent configuration (`Code`); seed hits via *.prompt.md.
- **Why eligible:** ≥10 stars (137); active since 2024-06-01 (last push 2026-06-17); instruction artifact present in code search; not fork/archived/mirror/template; passed keyword heuristics (or agent-product retention); evidence: CI + tests.
- **Instruction artifacts:** queries=['*.prompt.md']; paths=['core/prompts/analysis/intent_classify_system.md', 'core/prompts/common/boundaries.md']
- **CI evidence:** .github/workflows; tests: Cargo.toml
- **Release evidence:** tags=1, releases=1
- **agent_product_flag:** True
- **URL:** https://github.com/AI45Lab/Code

### 3. `0xdpfly/gin-app-start`

- **Stars:** 37
- **Short description:** Inferred AI tooling / agent configuration (`gin app start`); seed hits via .cursor/rules.
- **Why eligible:** ≥10 stars (37); active since 2024-06-01 (last push 2025-11-20); instruction artifact present in code search; not fork/archived/mirror/template; passed keyword heuristics (or agent-product retention); evidence: tests.
- **Instruction artifacts:** queries=['.cursor/rules']; paths=['.cursor/rules/CLAUDE.md']
- **CI evidence:** None detected
- **Release evidence:** None detected
- **agent_product_flag:** True
- **URL:** https://github.com/0xdpfly/gin-app-start

### 4. `Alexli18/binex`

- **Stars:** 62
- **Short description:** Inferred AI tooling / agent configuration (`binex`); seed hits via *.prompt.md.
- **Why eligible:** ≥10 stars (62); active since 2024-06-01 (last push 2026-04-19); instruction artifact present in code search; not fork/archived/mirror/template; passed keyword heuristics (or agent-product retention); evidence: CI + tests.
- **Instruction artifacts:** queries=['*.prompt.md']; paths=['src/binex/prompts/edu-essay-evaluator-encouraging.md']
- **CI evidence:** .github/workflows; tests: tests/
- **Release evidence:** tags=1, releases=1
- **agent_product_flag:** True
- **URL:** https://github.com/Alexli18/binex

### 5. `Agnuxo1/OpenCLAW-P2P`

- **Stars:** 44
- **Short description:** Inferred AI tooling / agent configuration (`OpenCLAW P2P`); seed hits via .aider.conf.yml.
- **Why eligible:** ≥10 stars (44); active since 2024-06-01 (last push 2026-06-11); instruction artifact present in code search; not fork/archived/mirror/template; passed keyword heuristics (or agent-product retention); evidence: CI.
- **Instruction artifacts:** queries=['.aider.conf.yml']; paths=['paperclaw/integrations/aider/.aider.conf.yml']
- **CI evidence:** .github/workflows
- **Release evidence:** tags=1, releases=0
- **agent_product_flag:** True
- **URL:** https://github.com/Agnuxo1/OpenCLAW-P2P

### 6. `AgentWrapper/agent-orchestrator`

- **Stars:** 7599
- **Short description:** Inferred AI tooling / agent configuration (`agent orchestrator`); seed hits via copilot-instructions.md.
- **Why eligible:** ≥10 stars (7599); active since 2024-06-01 (last push 2026-06-17); instruction artifact present in code search; not fork/archived/mirror/template; passed keyword heuristics (or agent-product retention); evidence: CI + tests.
- **Instruction artifacts:** queries=['copilot-instructions.md']; paths=['.github/copilot-instructions.md']
- **CI evidence:** .github/workflows; tests: tests/
- **Release evidence:** tags=1, releases=1
- **agent_product_flag:** True
- **URL:** https://github.com/AgentWrapper/agent-orchestrator

### 7. `AIStoryBuilders/AIStoryBuilders`

- **Stars:** 67
- **Short description:** Inferred AI tooling / agent configuration (`AIStoryBuilders`); seed hits via *.prompt.md.
- **Why eligible:** ≥10 stars (67); active since 2024-06-01 (last push 2026-05-27); instruction artifact present in code search; not fork/archived/mirror/template; passed keyword heuristics (or agent-product retention); evidence: CI.
- **Instruction artifacts:** queries=['*.prompt.md']; paths=['wiki-content/Anatomy-Of-A-Prompt.md']
- **CI evidence:** .github/workflows
- **Release evidence:** tags=1, releases=1
- **agent_product_flag:** True
- **URL:** https://github.com/AIStoryBuilders/AIStoryBuilders

### 8. `AI-Planning/l2p`

- **Stars:** 58
- **Short description:** Inferred AI tooling / agent configuration (`l2p`); seed hits via *.prompt.md.
- **Why eligible:** ≥10 stars (58); active since 2024-06-01 (last push 2026-06-16); instruction artifact present in code search; not fork/archived/mirror/template; passed keyword heuristics (or agent-product retention); evidence: CI + tests.
- **Instruction artifacts:** queries=['*.prompt.md']; paths=['l2p/templates/custom/prompt_initial_goal_metric.md']
- **CI evidence:** .github/workflows; tests: tests/
- **Release evidence:** tags=1, releases=1
- **agent_product_flag:** True
- **URL:** https://github.com/AI-Planning/l2p

### 9. `BUZZARDGTA/Session-Sniffer`

- **Stars:** 87
- **Short description:** Inferred AI tooling / agent configuration (`Session Sniffer`); seed hits via .github/copilot-instructions.md.
- **Why eligible:** ≥10 stars (87); active since 2024-06-01 (last push 2026-06-18); instruction artifact present in code search; not fork/archived/mirror/template; passed keyword heuristics (or agent-product retention); evidence: CI.
- **Instruction artifacts:** queries=['.github/copilot-instructions.md']; paths=['.github/copilot-instructions.md']
- **CI evidence:** .github/workflows
- **Release evidence:** tags=1, releases=1
- **agent_product_flag:** True
- **URL:** https://github.com/BUZZARDGTA/Session-Sniffer

### 10. `9mtm/Agent-Player`

- **Stars:** 11
- **Short description:** Inferred AI tooling / agent configuration (`Agent Player`); seed hits via system-prompt.*.
- **Why eligible:** ≥10 stars (11); active since 2024-06-01 (last push 2026-03-21); instruction artifact present in code search; not fork/archived/mirror/template; passed keyword heuristics (or agent-product retention); evidence: CI.
- **Instruction artifacts:** queries=['system-prompt.*']; paths=['packages/backend/src/tools/system-prompts.ts']
- **CI evidence:** .github/workflows
- **Release evidence:** tags=1, releases=1
- **agent_product_flag:** True
- **URL:** https://github.com/9mtm/Agent-Player

### 11. `Automattic/wp-calypso`

- **Stars:** 12635
- **Short description:** Inferred AI tooling / agent configuration (`wp calypso`); seed hits via AGENTS.md.
- **Why eligible:** ≥10 stars (12635); active since 2024-06-01 (last push 2026-06-18); instruction artifact present in code search; not fork/archived/mirror/template; passed keyword heuristics (or agent-product retention); evidence: CI + tests.
- **Instruction artifacts:** queries=['AGENTS.md']; paths=['client/landing/stepper/AGENTS.md']
- **CI evidence:** .circleci, .buildkite; tests: test/
- **Release evidence:** tags=1, releases=1
- **agent_product_flag:** True
- **URL:** https://github.com/Automattic/wp-calypso

### 12. `1Password/SCAM`

- **Stars:** 130
- **Short description:** Inferred AI tooling / agent configuration (`SCAM`); seed hits via AGENTS.md.
- **Why eligible:** ≥10 stars (130); active since 2024-06-01 (last push 2026-02-12); instruction artifact present in code search; not fork/archived/mirror/template; passed keyword heuristics (or agent-product retention); evidence: tests.
- **Instruction artifacts:** queries=['AGENTS.md']; paths=['AGENTS.md']
- **CI evidence:** None detected
- **Release evidence:** None detected
- **agent_product_flag:** True
- **URL:** https://github.com/1Password/SCAM

### 13. `CERTCC/Vultron`

- **Stars:** 20
- **Short description:** Inferred AI tooling / agent configuration (`Vultron`); seed hits via *.prompt.md, prompts/.
- **Why eligible:** ≥10 stars (20); active since 2024-06-01 (last push 2026-06-18); instruction artifact present in code search; not fork/archived/mirror/template; passed keyword heuristics (or agent-product retention); evidence: CI + tests.
- **Instruction artifacts:** queries=['*.prompt.md', 'prompts/']; paths=['prompts/BUGS_FROM_LOGS_prompt.md']
- **CI evidence:** .github/workflows; tests: test/, specs/
- **Release evidence:** tags=1, releases=1
- **agent_product_flag:** True
- **URL:** https://github.com/CERTCC/Vultron

### 14. `BlackBeltTechnology/pi-agent-dashboard`

- **Stars:** 168
- **Short description:** Inferred AI tooling / agent configuration (`pi agent dashboard`); seed hits via *.prompt.md.
- **Why eligible:** ≥10 stars (168); active since 2024-06-01 (last push 2026-06-18); instruction artifact present in code search; not fork/archived/mirror/template; passed keyword heuristics (or agent-product retention); evidence: CI.
- **Instruction artifacts:** queries=['*.prompt.md']; paths=['openspec/changes/archive/2026-03-27-auto-resume-on-prompt/tasks.md']
- **CI evidence:** .github/workflows
- **Release evidence:** tags=1, releases=1
- **agent_product_flag:** True
- **URL:** https://github.com/BlackBeltTechnology/pi-agent-dashboard

### 15. `AgentOps-AI/agentops`

- **Stars:** 5643
- **Short description:** Inferred AI tooling / agent configuration (`agentops`); seed hits via AGENTS.md.
- **Why eligible:** ≥10 stars (5643); active since 2024-06-01 (last push 2026-03-19); instruction artifact present in code search; not fork/archived/mirror/template; passed keyword heuristics (or agent-product retention); evidence: CI + tests.
- **Instruction artifacts:** queries=['AGENTS.md']; paths=['docs/v2/examples/openai_agents.mdx']
- **CI evidence:** .github/workflows; tests: tests/
- **Release evidence:** tags=1, releases=1
- **agent_product_flag:** True
- **URL:** https://github.com/AgentOps-AI/agentops

### 16. `Agents2AgentsAI/ata`

- **Stars:** 90
- **Short description:** Inferred AI tooling / agent configuration (`ata`); seed hits via system_prompt.*.
- **Why eligible:** ≥10 stars (90); active since 2024-06-01 (last push 2026-06-17); instruction artifact present in code search; not fork/archived/mirror/template; passed keyword heuristics (or agent-product retention); evidence: CI.
- **Instruction artifacts:** queries=['system_prompt.*']; paths=['codex-rs/core/templates/research/researcher_system_prompt.md']
- **CI evidence:** .github/workflows
- **Release evidence:** tags=1, releases=1
- **agent_product_flag:** True
- **URL:** https://github.com/Agents2AgentsAI/ata

### 17. `Azure/kimojio-rs`

- **Stars:** 242
- **Short description:** Inferred AI tooling / agent configuration (`kimojio rs`); seed hits via .github/copilot-instructions.md.
- **Why eligible:** ≥10 stars (242); active since 2024-06-01 (last push 2026-06-17); instruction artifact present in code search; not fork/archived/mirror/template; passed keyword heuristics (or agent-product retention); evidence: CI + tests.
- **Instruction artifacts:** queries=['.github/copilot-instructions.md']; paths=['.github/copilot-instructions.md']
- **CI evidence:** .github/workflows; tests: Cargo.toml
- **Release evidence:** tags=1, releases=1
- **agent_product_flag:** True
- **URL:** https://github.com/Azure/kimojio-rs

### 18. `BintzGavin/helios`

- **Stars:** 86
- **Short description:** Inferred AI tooling / agent configuration (`helios`); seed hits via system-prompt.*.
- **Why eligible:** ≥10 stars (86); active since 2024-06-01 (last push 2026-06-18); instruction artifact present in code search; not fork/archived/mirror/template; passed keyword heuristics (or agent-product retention); evidence: CI + tests.
- **Instruction artifacts:** queries=['system-prompt.*']; paths=['.sys/plans/2026-05-29-CORE-AI-System-Prompt.md']
- **CI evidence:** .github/workflows; tests: tests/
- **Release evidence:** None detected
- **agent_product_flag:** True
- **URL:** https://github.com/BintzGavin/helios

### 19. `Ageniti/Ageniti`

- **Stars:** 30
- **Short description:** Inferred AI tooling / agent configuration (`Ageniti`); seed hits via AGENTS.md.
- **Why eligible:** ≥10 stars (30); active since 2024-06-01 (last push 2026-06-10); instruction artifact present in code search; not fork/archived/mirror/template; passed keyword heuristics (or agent-product retention); evidence: CI + tests.
- **Instruction artifacts:** queries=['AGENTS.md']; paths=['AGENTS.md']
- **CI evidence:** .github/workflows; tests: test/
- **Release evidence:** None detected
- **agent_product_flag:** True
- **URL:** https://github.com/Ageniti/Ageniti

### 20. `Automattic/newspack-workspace`

- **Stars:** 16
- **Short description:** Inferred Application or library codebase (`newspack workspace`); seed hits via CLAUDE.md.
- **Why eligible:** ≥10 stars (16); active since 2024-06-01 (last push 2026-06-18); instruction artifact present in code search; not fork/archived/mirror/template; passed keyword heuristics (or agent-product retention); evidence: CI.
- **Instruction artifacts:** queries=['CLAUDE.md']; paths=['plugins/newspack-blocks/CLAUDE.md']
- **CI evidence:** .github/workflows
- **Release evidence:** tags=1, releases=1
- **agent_product_flag:** False
- **URL:** https://github.com/Automattic/newspack-workspace

## Sample B — 10 random `agent_product_flag=true` repositories

Overlap with Sample A: 2 repositories (`AgentWrapper/agent-orchestrator, Alexli18/binex`)

### 1. `AgentWrapper/agent-orchestrator`

- **Stars:** 7599
- **Short description:** Inferred AI tooling / agent configuration (`agent orchestrator`); seed hits via copilot-instructions.md.
- **Why eligible:** ≥10 stars (7599); active since 2024-06-01 (last push 2026-06-17); instruction artifact present in code search; not fork/archived/mirror/template; passed keyword heuristics (or agent-product retention); evidence: CI + tests.
- **Instruction artifacts:** queries=['copilot-instructions.md']; paths=['.github/copilot-instructions.md']
- **CI evidence:** .github/workflows; tests: tests/
- **Release evidence:** tags=1, releases=1
- **agent_product_flag:** True
- **URL:** https://github.com/AgentWrapper/agent-orchestrator

### 2. `Azure-Samples/Copilot-Studio-with-Azure-AI-Search`

- **Stars:** 26
- **Short description:** Inferred AI tooling / agent configuration (`Copilot Studio with Azure AI Search`); seed hits via .github/chatmodes.
- **Why eligible:** ≥10 stars (26); active since 2024-06-01 (last push 2026-06-12); instruction artifact present in code search; not fork/archived/mirror/template; passed keyword heuristics (or agent-product retention); evidence: CI + tests.
- **Instruction artifacts:** queries=['.github/chatmodes']; paths=['.github/chatmodes/README.md']
- **CI evidence:** .github/workflows; tests: tests/
- **Release evidence:** tags=1, releases=1
- **agent_product_flag:** True
- **URL:** https://github.com/Azure-Samples/Copilot-Studio-with-Azure-AI-Search

### 3. `Bugb-Technologies/guardlink`

- **Stars:** 16
- **Short description:** Inferred AI tooling / agent configuration (`guardlink`); seed hits via .clinerules.
- **Why eligible:** ≥10 stars (16); active since 2024-06-01 (last push 2026-05-13); instruction artifact present in code search; not fork/archived/mirror/template; passed keyword heuristics (or agent-product retention); evidence: CI + tests.
- **Instruction artifacts:** queries=['.clinerules']; paths=['.clinerules']
- **CI evidence:** .github/workflows; tests: tests/
- **Release evidence:** tags=1, releases=1
- **agent_product_flag:** True
- **URL:** https://github.com/Bugb-Technologies/guardlink

### 4. `Alexli18/binex`

- **Stars:** 62
- **Short description:** Inferred AI tooling / agent configuration (`binex`); seed hits via *.prompt.md.
- **Why eligible:** ≥10 stars (62); active since 2024-06-01 (last push 2026-04-19); instruction artifact present in code search; not fork/archived/mirror/template; passed keyword heuristics (or agent-product retention); evidence: CI + tests.
- **Instruction artifacts:** queries=['*.prompt.md']; paths=['src/binex/prompts/edu-essay-evaluator-encouraging.md']
- **CI evidence:** .github/workflows; tests: tests/
- **Release evidence:** tags=1, releases=1
- **agent_product_flag:** True
- **URL:** https://github.com/Alexli18/binex

### 5. `0-AI-UG/cate`

- **Stars:** 1662
- **Short description:** Inferred AI tooling / agent configuration (`cate`); seed hits via *.prompt.md.
- **Why eligible:** ≥10 stars (1662); active since 2024-06-01 (last push 2026-06-18); instruction artifact present in code search; not fork/archived/mirror/template; passed keyword heuristics (or agent-product retention); evidence: CI.
- **Instruction artifacts:** queries=['*.prompt.md']; paths=['src/agent/extensions/subagent/prompts/implement.md']
- **CI evidence:** .github/workflows
- **Release evidence:** tags=1, releases=1
- **agent_product_flag:** True
- **URL:** https://github.com/0-AI-UG/cate

### 6. `AMAP-EAI/Nav-R2`

- **Stars:** 20
- **Short description:** Inferred AI tooling / agent configuration (`Nav R2`); seed hits via AGENTS.md.
- **Why eligible:** ≥10 stars (20); active since 2024-06-01 (last push 2025-12-10); instruction artifact present in code search; not fork/archived/mirror/template; passed keyword heuristics (or agent-product retention); evidence: tests.
- **Instruction artifacts:** queries=['AGENTS.md']; paths=['environment-modules-customed/transformers_4.51.3-xwt-customed/transformers/docs/source/zh/agents.md']
- **CI evidence:** None detected
- **Release evidence:** None detected
- **agent_product_flag:** True
- **URL:** https://github.com/AMAP-EAI/Nav-R2

### 7. `Autonoma-Labs/Open-CoWork`

- **Stars:** 34
- **Short description:** Inferred AI tooling / agent configuration (`Open CoWork`); seed hits via system-prompt.*.
- **Why eligible:** ≥10 stars (34); active since 2024-06-01 (last push 2026-01-23); instruction artifact present in code search; not fork/archived/mirror/template; passed keyword heuristics (or agent-product retention); evidence: CI + tests.
- **Instruction artifacts:** queries=['system-prompt.*']; paths=['src/renderer/services/ai/system-prompt.ts']
- **CI evidence:** .github/workflows; tests: tests/
- **Release evidence:** None detected
- **agent_product_flag:** True
- **URL:** https://github.com/Autonoma-Labs/Open-CoWork

### 8. `Archeb/CyberGroupmate`

- **Stars:** 184
- **Short description:** Inferred AI tooling / agent configuration (`CyberGroupmate`); seed hits via *.prompt.md.
- **Why eligible:** ≥10 stars (184); active since 2024-06-01 (last push 2026-06-16); instruction artifact present in code search; not fork/archived/mirror/template; passed keyword heuristics (or agent-product retention); evidence: CI + tests.
- **Instruction artifacts:** queries=['*.prompt.md']; paths=['system-prompts/meta-agent/proactive-idle.md']
- **CI evidence:** .github/workflows; tests: tests/
- **Release evidence:** None detected
- **agent_product_flag:** True
- **URL:** https://github.com/Archeb/CyberGroupmate

### 9. `BuildWithHussain/hive`

- **Stars:** 16
- **Short description:** Inferred AI tooling / agent configuration (`hive`); seed hits via prompts/.
- **Why eligible:** ≥10 stars (16); active since 2024-06-01 (last push 2026-05-22); instruction artifact present in code search; not fork/archived/mirror/template; passed keyword heuristics (or agent-product retention); evidence: CI.
- **Instruction artifacts:** queries=['prompts/']; paths=['prompts/prd.md']
- **CI evidence:** .github/workflows
- **Release evidence:** None detected
- **agent_product_flag:** True
- **URL:** https://github.com/BuildWithHussain/hive

### 10. `ALT-F4-LLC/dotfiles.vorpal`

- **Stars:** 17
- **Short description:** Inferred AI tooling / agent configuration (`dotfiles.vorpal`); seed hits via AGENTS.md.
- **Why eligible:** ≥10 stars (17); active since 2024-06-01 (last push 2026-06-18); instruction artifact present in code search; not fork/archived/mirror/template; passed keyword heuristics (or agent-product retention); evidence: CI + tests.
- **Instruction artifacts:** queries=['AGENTS.md']; paths=['docs/changelog/skills/evolve-agents.md']
- **CI evidence:** .github/workflows; tests: Cargo.toml, tests/
- **Release evidence:** None detected
- **agent_product_flag:** True
- **URL:** https://github.com/ALT-F4-LLC/dotfiles.vorpal

## Classification rubric (audit-only, no rule changes)

- **A — Normal software with AI assistance:** application/library codebase signals dominate; 
instruction files appear as project conventions rather than product documentation.
- **B — AI tooling project:** agent/prompt/cursor/copilot artifacts dominate; repo reads as tooling, 
templates, or agent infrastructure.
- **C — Mixed:** substantive application code **and** prominent agent-instruction surfaces.

## Sample-level classification (heuristic)

### Sample A (n=20)

- **A:** 3
- **B:** 5
- **C:** 12

### Sample B — agent-flagged (n=10)

- **A:** 1
- **B:** 4
- **C:** 5

### Full eligible population (n=83)

- **A:** 9 (10.8%)
- **B:** 29 (34.9%)
- **C:** 45 (54.2%)

## Conclusion

**Primarily C (mixed): application or product codebases with embedded AI-instruction artifacts.**

80 of 83 eligible repos (96.4%) carry `agent_product_flag=true`, yet heuristic review classifies
most as **C (54%)** rather than pure tooling (**B, 35%**) or conventional apps without agent
surfaces (**A, 11%**). Seed queries intentionally target instruction-filename paths
(`AGENTS.md`, `.cursor/rules`, `copilot-instructions.md`, `*.prompt.md`, etc.), so eligibility
enriches repos where **normal software development coexists with agent configuration files**
(e.g. `Automattic/wp-calypso`, `AgentOps-AI/agentops`, `Azure/kimojio-rs`). Pure AI-tooling
repositories (prompt libraries, agent orchestrators, dotfiles/rules packs) are common but not
the sole profile. Conventional software **without** agent-product signals is rare in the current
eligible set (3 repos: `Automattic/newspack-workspace`, `AyayaXiaowang/Ayaya_Miliastra_Editor`,
`BNETDocs/bnetdocs-web`).

### Evidence from this audit

1. **Agent-product prevalence:** 80/83 eligible repos flagged.
2. **Artifact types:** dominant hits are markdown prompt/rule files and agent config paths, not application entrypoints alone.
3. **Engineering signals:** CI 72/83, tests 50/83, releases/tags 58/83 — eligible set is not 'docs-only'; most passed CI/test gate.
4. **Non-agent-flagged eligible repos (3):** `Automattic/newspack-workspace`, `AyayaXiaowang/Ayaya_Miliastra_Editor`, `BNETDocs/bnetdocs-web`
