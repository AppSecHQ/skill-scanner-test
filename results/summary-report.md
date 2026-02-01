# AI Agent Skills Security Scan Report

**Generated:** 2026-02-01T05:23:20.339632
**Scanner:** cisco-ai-skill-scanner
**Analyzers:** static, behavioral, trigger

---

## Executive Summary

| Metric | Count |
|--------|-------|
| Total Skills Scanned | 22 |
| Safe Skills | 13 (59%) |
| Skills with Issues | 9 (41%) |
| Scan Errors | 0 |

### Severity Breakdown

| Severity | Count |
|----------|-------|
| CRITICAL | 10 |
| HIGH | 7 |
| MEDIUM | 10 |
| LOW | 18 |
| **Total Findings** | **45** |

### Findings by Category

| Category | Count |
|----------|-------|
| policy_violation | 18 |
| data_exfiltration | 10 |
| hardcoded_secrets | 8 |
| command_injection | 6 |
| unauthorized_tool_use | 2 |
| resource_abuse | 1 |

---

## Results by Skill

| # | Skill | Source | Safe | Findings | Max Severity |
|---|-------|--------|------|----------|--------------|
| 1 | [clickup](clickup-skill-scan.md) | clawhub.ai | **No** | 14 | **CRITICAL** |
| 2 | [agent-browser](agent-browser-scan.md) | skills.sh | **No** | 8 | **HIGH** |
| 3 | [Agent Wallet](agent-wallet-scan.md) | clawhub.ai | Yes | 2 | LOW |
| 4 | [captions](captions-scan.md) | clawhub.ai | **No** | 2 | **CRITICAL** |
| 5 | [subtitles](subtitles-scan.md) | clawhub.ai | **No** | 2 | **CRITICAL** |
| 6 | [video-transcript](video-transcript-scan.md) | clawhub.ai | **No** | 2 | **CRITICAL** |
| 7 | [youtube-channels](youtube-channels-scan.md) | clawhub.ai | **No** | 2 | **CRITICAL** |
| 8 | [youtube-data](youtube-data-scan.md) | clawhub.ai | **No** | 2 | **CRITICAL** |
| 9 | [youtube-full](youtube-full-scan.md) | clawhub.ai | **No** | 2 | **CRITICAL** |
| 10 | [youtube-playlist](youtube-playlist-scan.md) | clawhub.ai | **No** | 2 | **CRITICAL** |
| 11 | [birthday-reminder](Birthday%20Reminder-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 12 | [find-skills](find-skills-scan.md) | skills.sh | Yes | 1 | LOW |
| 13 | [remotion-best-practices](remotion-best-practices-scan.md) | skills.sh | Yes | 1 | LOW |
| 14 | [seo-audit](seo-audit-scan.md) | skills.sh | Yes | 1 | LOW |
| 15 | [web-design-guidelines](web-design-guidelines-scan.md) | skills.sh | Yes | 1 | LOW |
| 16 | [youtube-api](youtube-api-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 17 | [youtube-search](youtube-search-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 18 | [frontend-design](frontend-design-scan.md) | skills.sh | Yes | 0 | SAFE |
| 19 | [skill-creator](skill-creator-scan.md) | skills.sh | Yes | 0 | SAFE |
| 20 | [vercel-composition-patterns](vercel-composition-patterns-scan.md) | skills.sh | Yes | 0 | SAFE |
| 21 | [vercel-react-best-practices](vercel-react-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 22 | [vercel-react-native-skills](vercel-react-native-skills-scan.md) | skills.sh | Yes | 0 | SAFE |

---

## Top Risks (Critical/High Severity)

### 1. [HIGH] agent-browser - unauthorized_tool_use

**Rule:** ALLOWED_TOOLS_BASH_VIOLATION
**Location:** None

Skill restricts tools to ['Bash(agent-browser:*)'] but code executes bash commands

### 2. [CRITICAL] captions - hardcoded_secrets

**Rule:** YARA_credential_harvesting
**Location:** None

Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export TRANSCRIPT_API_KEY

### 3. [HIGH] clickup - resource_abuse

**Rule:** RESOURCE_ABUSE_INFINITE_LOOP
**Location:** None

Pattern detected: while True:

### 4. [CRITICAL] clickup - hardcoded_secrets

**Rule:** YARA_credential_harvesting
**Location:** None

Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export CLICKUP_API_TOKEN

### 5. [CRITICAL] clickup - data_exfiltration

**Rule:** BEHAVIOR_ENV_VAR_EXFILTRATION
**Location:** None

Script accesses environment variables and makes network calls in skills/clawhub-clickup-skill/scripts/clickup_client.py

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

### 10. [HIGH] clickup - data_exfiltration

**Rule:** BEHAVIOR_SUSPICIOUS_URL
**Location:** None

Script contains suspicious URL that may be used for data exfiltration

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
- **Scan Date:** 2026-02-01T05:23:20.339632

### Limitations

- LLM-based semantic analysis not used (requires API key)
- VirusTotal binary scanning not used (requires API key)
- Static analysis only - no runtime verification
