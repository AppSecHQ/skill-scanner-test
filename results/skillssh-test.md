# AI Agent Skills Security Scan Report

**Generated:** 2026-01-31T17:35:16.941777
**Scanner:** cisco-ai-skill-scanner
**Analyzers:** static, behavioral, trigger

---

## Executive Summary

| Metric | Count |
|--------|-------|
| Total Skills Scanned | 12 |
| Safe Skills | 10 (83%) |
| Skills with Issues | 2 (17%) |
| Scan Errors | 0 |

### Severity Breakdown

| Severity | Count |
|----------|-------|
| CRITICAL | 3 |
| HIGH | 7 |
| MEDIUM | 10 |
| LOW | 7 |
| **Total Findings** | **27** |

### Findings by Category

| Category | Count |
|----------|-------|
| data_exfiltration | 10 |
| policy_violation | 7 |
| command_injection | 6 |
| unauthorized_tool_use | 2 |
| resource_abuse | 1 |
| hardcoded_secrets | 1 |

---

## Results by Skill

| # | Skill | Safe | Findings | Max Severity |
|---|-------|------|----------|--------------|
| 1 | clickup | **No** | 14 | **CRITICAL** |
| 2 | agent-browser | **No** | 8 | **HIGH** |
| 3 | birthday-reminder | Yes | 1 | LOW |
| 4 | find-skills | Yes | 1 | LOW |
| 5 | remotion-best-practices | Yes | 1 | LOW |
| 6 | seo-audit | Yes | 1 | LOW |
| 7 | web-design-guidelines | Yes | 1 | LOW |
| 8 | frontend-design | Yes | 0 | SAFE |
| 9 | skill-creator | Yes | 0 | SAFE |
| 10 | vercel-composition-patterns | Yes | 0 | SAFE |
| 11 | vercel-react-best-practices | Yes | 0 | SAFE |
| 12 | vercel-react-native-skills | Yes | 0 | SAFE |

---

## Top Risks (Critical/High Severity)

### 1. [HIGH] agent-browser - unauthorized_tool_use

**Rule:** ALLOWED_TOOLS_BASH_VIOLATION
**Location:** None

Skill restricts tools to ['Bash(agent-browser:*)'] but code executes bash commands

### 2. [HIGH] clickup - resource_abuse

**Rule:** RESOURCE_ABUSE_INFINITE_LOOP
**Location:** None

Pattern detected: while True:

### 3. [CRITICAL] clickup - hardcoded_secrets

**Rule:** YARA_credential_harvesting
**Location:** None

Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export CLICKUP_API_TOKEN

### 4. [CRITICAL] clickup - data_exfiltration

**Rule:** BEHAVIOR_ENV_VAR_EXFILTRATION
**Location:** None

Script accesses environment variables and makes network calls in skills/clawhub-clickup-skill/scripts/clickup_client.py

### 5. [HIGH] clickup - data_exfiltration

**Rule:** BEHAVIOR_SUSPICIOUS_URL
**Location:** None

Script contains suspicious URL that may be used for data exfiltration

### 6. [HIGH] clickup - data_exfiltration

**Rule:** BEHAVIOR_SUSPICIOUS_URL
**Location:** None

Script contains suspicious URL that may be used for data exfiltration

### 7. [HIGH] clickup - data_exfiltration

**Rule:** BEHAVIOR_SUSPICIOUS_URL
**Location:** None

Script contains suspicious URL that may be used for data exfiltration

### 8. [HIGH] clickup - data_exfiltration

**Rule:** BEHAVIOR_SUSPICIOUS_URL
**Location:** None

Script contains suspicious URL that may be used for data exfiltration

### 9. [HIGH] clickup - data_exfiltration

**Rule:** BEHAVIOR_SUSPICIOUS_URL
**Location:** None

Script contains suspicious URL that may be used for data exfiltration

### 10. [CRITICAL] clickup - data_exfiltration

**Rule:** BEHAVIOR_CROSSFILE_ENV_VAR_EXFILTRATION
**Location:** None

Environment variable access with network calls in scripts/clickup_client.py

---

## Clean Skills (No Findings)

- frontend-design
- skill-creator
- vercel-composition-patterns
- vercel-react-best-practices
- vercel-react-native-skills

---

## Methodology

- **Scanner:** cisco-ai-skill-scanner
- **Analyzers:** static_analyzer, behavioral_analyzer, trigger_analyzer
- **Scan Date:** 2026-01-31T17:35:16.941777

### Limitations

- LLM-based semantic analysis not used (requires API key)
- VirusTotal binary scanning not used (requires API key)
- Static analysis only - no runtime verification
