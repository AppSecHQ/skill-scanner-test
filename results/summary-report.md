# AI Agent Skills Security Scan Report

**Generated:** 2026-02-01T09:09:07.671399
**Scanner:** cisco-ai-skill-scanner
**Analyzers:** behavioral, llm, meta, static, trigger

---

## Executive Summary

| Metric | Count |
|--------|-------|
| Total Skills Scanned | 22 |
| Safe Skills | 19 (86%) |
| Skills with Issues | 3 (14%) |
| Scan Errors | 0 |

### Severity Breakdown

| Severity | Count |
|----------|-------|
| CRITICAL | 3 |
| HIGH | 8 |
| MEDIUM | 21 |
| LOW | 7 |
| **Total Findings** | **39** |

### Findings by Category

| Category | Count |
|----------|-------|
| data_exfiltration | 20 |
| policy_violation | 7 |
| command_injection | 6 |
| unauthorized_tool_use | 3 |
| social_engineering | 1 |
| resource_abuse | 1 |
| hardcoded_secrets | 1 |

---

## Results by Skill

| # | Skill | Source | Safe | Findings | Max Severity |
|---|-------|--------|------|----------|--------------|
| 1 | [clickup](clickup-skill-scan.md) | clawhub.ai | **No** | 14 | **CRITICAL** |
| 2 | [agent-browser](agent-browser-scan.md) | skills.sh | **No** | 8 | **HIGH** |
| 3 | [Agent Wallet](agent-wallet-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 4 | [subtitles](subtitles-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 5 | [video-transcript](video-transcript-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 6 | [youtube-playlist](youtube-playlist-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 7 | [birthday-reminder](Birthday%20Reminder-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 8 | [captions](captions-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 9 | [find-skills](find-skills-scan.md) | skills.sh | Yes | 1 | LOW |
| 10 | [remotion-best-practices](remotion-best-practices-scan.md) | skills.sh | Yes | 1 | LOW |
| 11 | [seo-audit](seo-audit-scan.md) | skills.sh | Yes | 1 | LOW |
| 12 | [web-design-guidelines](web-design-guidelines-scan.md) | skills.sh | Yes | 1 | LOW |
| 13 | [youtube-channels](youtube-channels-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 14 | [youtube-data](youtube-data-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 15 | [youtube-full](youtube-full-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 16 | [frontend-design](frontend-design-scan.md) | skills.sh | Yes | 0 | SAFE |
| 17 | [skill-creator](skill-creator-scan.md) | skills.sh | Yes | 0 | SAFE |
| 18 | [vercel-composition-patterns](vercel-composition-patterns-scan.md) | skills.sh | Yes | 0 | SAFE |
| 19 | [vercel-react-best-practices](vercel-react-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 20 | [vercel-react-native-skills](vercel-react-native-skills-scan.md) | skills.sh | Yes | 0 | SAFE |
| 21 | [youtube-api](youtube-api-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 22 | [youtube-search](youtube-search-scan.md) | clawhub.ai | Yes | 0 | SAFE |

---

## Top Risks (Critical/High Severity)

### 1. [HIGH] agent-browser - unauthorized_tool_use

**Rule:** ALLOWED_TOOLS_BASH_VIOLATION
**Location:** None

Skill restricts tools to ['Bash(agent-browser:*)'] but code executes bash commands

### 2. [HIGH] Agent Wallet - unauthorized_tool_use

**Rule:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** None

The instructions reference 'wallet.py' as a file that should exist in the skill package, but it is not found. This creates ambiguity about how the skill actually executes wallet operations. An attacker could exploit this by providing a malicious wallet.py implementation that shadows the expected behavior, potentially intercepting API keys, modifying transaction parameters, or exfiltrating data before forwarding requests to the legitimate API.

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
- youtube-api
- youtube-search

---

## Methodology

- **Scanner:** cisco-ai-skill-scanner
- **Analyzers:** behavioral_analyzer, llm_analyzer, meta_analyzer, static_analyzer, trigger_analyzer
- **Scan Date:** 2026-02-01T09:09:07.671399

### Limitations

- VirusTotal binary scanning not used (requires API key)
- No runtime verification - static and semantic analysis only
