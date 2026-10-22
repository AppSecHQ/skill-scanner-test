# Scan: azure-validate

- **Verdict:** SAFE
- **Max severity:** MEDIUM
- **Findings:** 5
- **Analyzers:** static_analyzer, bytecode, pipeline, correlation, behavioral_analyzer, trigger_analyzer
- **Scanner version:** 2.3.1
- **Timestamp:** 2026-10-22T04:35:57.885751+00:00

## Findings

| Severity | Category | Title | File |
|---|---|---|---|
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | references/recipes/azd/scripts/set-aspire-aca-env.sh:80 |
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | references/recipes/azd/scripts/set-aspire-aca-env.sh:89 |
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | references/recipes/azd/scripts/set-aspire-aca-env.sh:94 |
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | references/recipes/azd/scripts/set-aspire-aca-env.sh:99 |
| MEDIUM | data_exfiltration | Bash: tainted data flows to dangerous sink | references/recipes/azd/scripts/set-aspire-aca-env.sh:104 |
