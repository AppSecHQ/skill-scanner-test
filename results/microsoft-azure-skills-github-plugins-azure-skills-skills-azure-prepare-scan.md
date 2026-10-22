# Scan: azure-prepare

- **Verdict:** SAFE
- **Max severity:** MEDIUM
- **Findings:** 5
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:36:00.814875+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| LOW | policy_violation | Skill package contains many files | . |
| MEDIUM | obfuscation | Deeply nested file references detected | SKILL.md |
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | references/services/app-service/networking.md:133 |
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | references/services/container-apps/terraform.md:99 |
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | references/services/container-apps/terraform.md:106 |
