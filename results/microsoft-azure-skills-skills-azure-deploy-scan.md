# Scan: azure-deploy

- **Verdict:** ISSUES FOUND
- **Max severity:** CRITICAL
- **Findings:** 6
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:36:04.364875+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| MEDIUM | command_injection | Discovery and execution chain (find -exec) | references/recipes/azd/ef-migrations.md:10 |
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | references/recipes/azd/post-deployment.md:79 |
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | references/recipes/azd/post-deployment.md:82 |
| CRITICAL | data_exfiltration | Bash: sensitive data exfiltration via network | references/recipes/azd/verify.md:26 |
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | references/recipes/terraform/README.md:82 |
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | references/recipes/terraform/README.md:89 |
