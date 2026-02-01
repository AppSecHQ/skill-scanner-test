# AI Agent Skills Security Scan Report

**Generated:** 2026-02-01T07:42:17.628091
**Scanner:** cisco-ai-skill-scanner
**Analyzers:** behavioral, llm, static, trigger

---

## Executive Summary

| Metric | Count |
|--------|-------|
| Total Skills Scanned | 22 |
| Safe Skills | 12 (55%) |
| Skills with Issues | 10 (45%) |
| Scan Errors | 0 |

### Severity Breakdown

| Severity | Count |
|----------|-------|
| CRITICAL | 10 |
| HIGH | 9 |
| MEDIUM | 22 |
| LOW | 39 |
| **Total Findings** | **80** |

### Findings by Category

| Category | Count |
|----------|-------|
| data_exfiltration | 32 |
| policy_violation | 18 |
| social_engineering | 8 |
| hardcoded_secrets | 8 |
| command_injection | 7 |
| unauthorized_tool_use | 4 |
| resource_abuse | 3 |

---

## Results by Skill

| # | Skill | Source | Safe | Findings | Max Severity |
|---|-------|--------|------|----------|--------------|
| 1 | [clickup](clickup-skill-scan.md) | clawhub.ai | **No** | 14 | **CRITICAL** |
| 2 | [Agent Wallet](agent-wallet-scan.md) | clawhub.ai | **No** | 9 | **HIGH** |
| 3 | [agent-browser](agent-browser-scan.md) | skills.sh | **No** | 8 | **HIGH** |
| 4 | [captions](captions-scan.md) | clawhub.ai | **No** | 7 | **CRITICAL** |
| 5 | [video-transcript](video-transcript-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 6 | [youtube-api](youtube-api-scan.md) | clawhub.ai | Yes | 5 | MEDIUM |
| 7 | [youtube-channels](youtube-channels-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 8 | [youtube-data](youtube-data-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 9 | [youtube-full](youtube-full-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 10 | [youtube-playlist](youtube-playlist-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 11 | [youtube-search](youtube-search-scan.md) | clawhub.ai | Yes | 4 | LOW |
| 12 | [subtitles](subtitles-scan.md) | clawhub.ai | **No** | 2 | **CRITICAL** |
| 13 | [birthday-reminder](Birthday%20Reminder-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 14 | [find-skills](find-skills-scan.md) | skills.sh | Yes | 1 | LOW |
| 15 | [remotion-best-practices](remotion-best-practices-scan.md) | skills.sh | Yes | 1 | LOW |
| 16 | [seo-audit](seo-audit-scan.md) | skills.sh | Yes | 1 | LOW |
| 17 | [web-design-guidelines](web-design-guidelines-scan.md) | skills.sh | Yes | 1 | LOW |
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

### 2. [HIGH] Agent Wallet - data_exfiltration

**Rule:** LLM_DATA_EXFILTRATION
**Location:** None

The wallet creation process returns an API key that grants full control over the agent's blockchain wallet. The instructions tell the agent to 'store this securely' but provide no secure storage mechanism. If the API key is logged, displayed to users, or stored in plain text, it could be compromised. The key provides bearer token authentication for all wallet operations including transfers and smart contract interactions.

### 3. [HIGH] Agent Wallet - unauthorized_tool_use

**Rule:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** None

The instructions reference 'wallet.py' as a file that should exist in the skill package, but this file is not found. This creates a tool shadowing vulnerability where a malicious actor could provide a fake wallet.py implementation that intercepts wallet operations, exfiltrates API keys, or redirects transactions to attacker-controlled addresses.

### 4. [CRITICAL] captions - hardcoded_secrets

**Rule:** YARA_credential_harvesting
**Location:** None

Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export TRANSCRIPT_API_KEY

### 5. [HIGH] clickup - resource_abuse

**Rule:** RESOURCE_ABUSE_INFINITE_LOOP
**Location:** None

Pattern detected: while True:

### 6. [CRITICAL] clickup - hardcoded_secrets

**Rule:** YARA_credential_harvesting
**Location:** None

Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export CLICKUP_API_TOKEN

### 7. [CRITICAL] clickup - data_exfiltration

**Rule:** BEHAVIOR_ENV_VAR_EXFILTRATION
**Location:** None

Script accesses environment variables and makes network calls in skills/clawhub-clickup-skill/scripts/clickup_client.py

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
- **Analyzers:** behavioral_analyzer, llm_analyzer, static_analyzer, trigger_analyzer
- **Scan Date:** 2026-02-01T07:42:17.628091

### Limitations

- Meta-analysis for false positive filtering not used
- VirusTotal binary scanning not used (requires API key)
- No runtime verification - static and semantic analysis only
