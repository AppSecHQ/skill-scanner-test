# Scan: microsoft-foundry

- **Verdict:** ISSUES FOUND
- **Max severity:** CRITICAL
- **Findings:** 29
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:35:56.324266+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| CRITICAL | data_exfiltration | Cross-file env var exfiltration: 11 files |  |
| CRITICAL | data_exfiltration | Cross-file exfiltration chain: 11 files |  |
| LOW | policy_violation | Skill package contains many files | . |
| CRITICAL | data_exfiltration | Environment variable access with network calls detected | /Users/brianlevine/claude-projects/skill-scanner-test/skills/microsoft-azure-skills/.github/plugins/azure-skills/skills/microsoft-foundry/finetuning/scripts/common.py |
| CRITICAL | data_exfiltration | Environment variable access with network calls detected | /Users/brianlevine/claude-projects/skill-scanner-test/skills/microsoft-azure-skills/.github/plugins/azure-skills/skills/microsoft-foundry/finetuning/scripts/submit_training.py |
| MEDIUM | unauthorized_tool_use | Undeclared network usage | SKILL.md |
| CRITICAL | command_injection | Dangerous code execution functions that can execute arbitrary code | finetuning/scripts/calibrate_grader.py:54 |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | finetuning/scripts/deploy_model.py:120 |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | finetuning/scripts/deploy_model.py:141 |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | finetuning/scripts/deploy_model.py:167 |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | finetuning/scripts/deploy_model.py:178 |
| MEDIUM | data_exfiltration | Outbound network request primitives that can transmit data externally | finetuning/scripts/submit_training.py:84 |
| HIGH | prompt_injection | JAILBREAK detected by YARA | foundry-agent/toolbox/references/tool-azure-ai-search.md:11 |
| HIGH | prompt_injection | JAILBREAK detected by YARA | foundry-agent/toolbox/references/tool-azure-ai-search.md:23 |
| HIGH | prompt_injection | JAILBREAK detected by YARA | foundry-agent/toolbox/references/tool-azure-ai-search.md:60 |
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | foundry-agent/toolbox/references/tool-azure-ai-search.md:160 |
| HIGH | prompt_injection | JAILBREAK detected by YARA | foundry-agent/toolbox/references/tool-azure-ai-search.md:164 |
| HIGH | prompt_injection | JAILBREAK detected by YARA | foundry-agent/toolbox/references/tool-azure-ai-search.md:168 |
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | foundry-agent/toolbox/references/tool-code-interpreter.md:84 |
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | foundry-agent/toolbox/references/tool-file-search.md:18 |
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | foundry-agent/toolbox/references/tool-file-search.md:22 |
| HIGH | data_exfiltration | Bash: tainted data flows to dangerous sink | foundry-agent/toolbox/references/tool-file-search.md:26 |
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | foundry-agent/toolbox/references/tool-openapi.md:145 |
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | foundry-agent/toolbox/references/tool-work-iq.md:137 |
| HIGH | data_exfiltration | Sensitive source reaches a network sink | foundry-agent/toolbox/scripts/get-catalog-inputs.sh:81 |
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | foundry-agent/toolbox/scripts/get-catalog-inputs.sh:81 |
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | models/deploy-model/preset/references/preset-workflow.md:70 |
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | rbac/rbac.md:95 |
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | rbac/rbac.md:121 |
