# Scan: agent-browser

- **Verdict:** ISSUES FOUND
- **Max severity:** HIGH
- **Findings:** 10
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:35:34.409433+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| HIGH | unauthorized_tool_use | Code executes bash but Bash tool not in allowed-tools | SKILL.md |
| LOW | unauthorized_tool_use | Code uses search/grep patterns but Grep tool not in allowed-tools | SKILL.md |
| INFO | policy_violation | Skill does not specify a license | SKILL.md |
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | templates/capture-workflow.sh:76 |
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | templates/capture-workflow.sh:79 |
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | templates/capture-workflow.sh:86 |
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | templates/capture-workflow.sh:91 |
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | templates/capture-workflow.sh:97 |
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | templates/capture-workflow.sh:105 |
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | templates/capture-workflow.sh:114 |
