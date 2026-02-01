# AI Agent Skills Security Scan Report

**Generated:** 2026-02-01T12:07:29.039611
**Scanner:** cisco-ai-skill-scanner
**Analyzers:** behavioral, llm, meta, static, trigger

---

## Executive Summary

| Metric | Count |
|--------|-------|
| Total Skills Scanned | 62 |
| Safe Skills | 57 (92%) |
| Skills with Issues | 5 (8%) |
| Scan Errors | 0 |

### Severity Breakdown

| Severity | Count |
|----------|-------|
| CRITICAL | 4 |
| HIGH | 10 |
| MEDIUM | 32 |
| LOW | 16 |
| **Total Findings** | **62** |

### Findings by Category

| Category | Count |
|----------|-------|
| data_exfiltration | 24 |
| policy_violation | 11 |
| command_injection | 9 |
| unauthorized_tool_use | 6 |
| prompt_injection | 4 |
| social_engineering | 3 |
| resource_abuse | 2 |
| tool_chaining_abuse | 2 |
| hardcoded_secrets | 1 |

---

## Results by Skill

| # | Skill | Source | Safe | Findings | Max Severity |
|---|-------|--------|------|----------|--------------|
| 1 | [clickup](clickup-skill-scan.md) | clawhub.ai | **No** | 14 | **CRITICAL** |
| 2 | [agent-browser](agent-browser-scan.md) | skills.sh | **No** | 8 | **HIGH** |
| 3 | [browser-use](browser-use-scan.md) | skills.sh | **No** | 8 | **HIGH** |
| 4 | [expo-api-routes](expo-api-routes-scan.md) | skills.sh | **No** | 4 | **CRITICAL** |
| 5 | [Agent Wallet](agent-wallet-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 6 | [canvas-design](canvas-design-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 7 | [doc-coauthoring](doc-coauthoring-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 8 | [launch-strategy](launch-strategy-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 9 | [marketing-psychology](marketing-psychology-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 10 | [subtitles](subtitles-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 11 | [video-transcript](video-transcript-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 12 | [youtube-playlist](youtube-playlist-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 13 | [birthday-reminder](Birthday%20Reminder-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 14 | [captions](captions-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 15 | [find-skills](find-skills-scan.md) | skills.sh | Yes | 1 | LOW |
| 16 | [next-best-practices](next-best-practices-scan.md) | skills.sh | Yes | 1 | LOW |
| 17 | [remotion-best-practices](remotion-best-practices-scan.md) | skills.sh | Yes | 1 | LOW |
| 18 | [seo-audit](seo-audit-scan.md) | skills.sh | Yes | 1 | LOW |
| 19 | [web-design-guidelines](web-design-guidelines-scan.md) | skills.sh | Yes | 1 | LOW |
| 20 | [webapp-testing](webapp-testing-scan.md) | skills.sh | Yes | 1 | MEDIUM |
| 21 | [writing-plans](writing-plans-scan.md) | skills.sh | Yes | 1 | LOW |
| 22 | [youtube-channels](youtube-channels-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 23 | [youtube-data](youtube-data-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 24 | [youtube-full](youtube-full-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 25 | [analytics-tracking](analytics-tracking-scan.md) | skills.sh | Yes | 0 | SAFE |
| 26 | [audit-website](audit-website-scan.md) | skills.sh | Yes | 0 | SAFE |
| 27 | [brainstorming](brainstorming-scan.md) | skills.sh | Yes | 0 | SAFE |
| 28 | [building-native-ui](building-native-ui-scan.md) | skills.sh | Yes | 0 | SAFE |
| 29 | [copy-editing](copy-editing-scan.md) | skills.sh | Yes | 0 | SAFE |
| 30 | [copywriting](copywriting-scan.md) | skills.sh | Yes | 0 | SAFE |
| 31 | [create-auth-skill](better-auth-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 32 | [docx](docx-scan.md) | skills.sh | Yes | 0 | SAFE |
| 33 | [expo-deployment](expo-deployment-scan.md) | skills.sh | Yes | 0 | SAFE |
| 34 | [expo-dev-client](expo-dev-client-scan.md) | skills.sh | Yes | 0 | SAFE |
| 35 | [expo-tailwind-setup](expo-tailwind-setup-scan.md) | skills.sh | Yes | 0 | SAFE |
| 36 | [frontend-design](frontend-design-scan.md) | skills.sh | Yes | 0 | SAFE |
| 37 | [marketing-ideas](marketing-ideas-scan.md) | skills.sh | Yes | 0 | SAFE |
| 38 | [mcp-builder](mcp-builder-scan.md) | skills.sh | Yes | 0 | SAFE |
| 39 | [native-data-fetching](native-data-fetching-scan.md) | skills.sh | Yes | 0 | SAFE |
| 40 | [onboarding-cro](onboarding-cro-scan.md) | skills.sh | Yes | 0 | SAFE |
| 41 | [page-cro](page-cro-scan.md) | skills.sh | Yes | 0 | SAFE |
| 42 | [pdf](pdf-scan.md) | skills.sh | Yes | 0 | SAFE |
| 43 | [pptx](pptx-scan.md) | skills.sh | Yes | 0 | SAFE |
| 44 | [pricing-strategy](pricing-strategy-scan.md) | skills.sh | Yes | 0 | SAFE |
| 45 | [programmatic-seo](programmatic-seo-scan.md) | skills.sh | Yes | 0 | SAFE |
| 46 | [react-native-best-practices](react-native-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 47 | [schema-markup](schema-markup-scan.md) | skills.sh | Yes | 0 | SAFE |
| 48 | [skill-creator](skill-creator-scan.md) | skills.sh | Yes | 0 | SAFE |
| 49 | [social-content](social-content-scan.md) | skills.sh | Yes | 0 | SAFE |
| 50 | [supabase-postgres-best-practices](supabase-postgres-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 51 | [systematic-debugging](systematic-debugging-scan.md) | skills.sh | Yes | 0 | SAFE |
| 52 | [test-driven-development](test-driven-development-scan.md) | skills.sh | Yes | 0 | SAFE |
| 53 | [theme-factory](theme-factory-scan.md) | skills.sh | Yes | 0 | SAFE |
| 54 | [ui-ux-pro-max](ui-ux-pro-max-scan.md) | skills.sh | Yes | 0 | SAFE |
| 55 | [upgrading-expo](upgrading-expo-scan.md) | skills.sh | Yes | 0 | SAFE |
| 56 | [vercel-composition-patterns](vercel-composition-patterns-scan.md) | skills.sh | Yes | 0 | SAFE |
| 57 | [vercel-react-best-practices](vercel-react-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 58 | [vercel-react-native-skills](vercel-react-native-skills-scan.md) | skills.sh | Yes | 0 | SAFE |
| 59 | [vue-best-practices](vue-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 60 | [xlsx](xlsx-scan.md) | skills.sh | Yes | 0 | SAFE |
| 61 | [youtube-api](youtube-api-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 62 | [youtube-search](youtube-search-scan.md) | clawhub.ai | Yes | 0 | SAFE |

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

### 3. [HIGH] browser-use - command_injection

**Rule:** LLM_COMMAND_INJECTION
**Location:** None

The skill allows execution of arbitrary browser-use CLI commands through Bash without input validation or sanitization. An attacker could craft malicious URLs or commands that execute arbitrary code through command injection. The skill accepts user-provided URLs and text inputs that are passed directly to shell commands without escaping or validation.

### 4. [HIGH] browser-use - data_exfiltration

**Rule:** LLM_DATA_EXFILTRATION
**Location:** None

The 'real' browser mode explicitly uses the user's Chrome browser with cookies, extensions, and logged-in sessions. This exposes all authenticated sessions, credentials, and personal browsing data to the automation context. An attacker could craft instructions to navigate to malicious sites, extract session cookies, or exfiltrate authentication tokens from the user's active browser sessions.

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

- analytics-tracking
- audit-website
- brainstorming
- building-native-ui
- copy-editing
- copywriting
- create-auth-skill
- docx
- expo-deployment
- expo-dev-client
- expo-tailwind-setup
- frontend-design
- marketing-ideas
- mcp-builder
- native-data-fetching
- onboarding-cro
- page-cro
- pdf
- pptx
- pricing-strategy
- programmatic-seo
- react-native-best-practices
- schema-markup
- skill-creator
- social-content
- supabase-postgres-best-practices
- systematic-debugging
- test-driven-development
- theme-factory
- ui-ux-pro-max
- upgrading-expo
- vercel-composition-patterns
- vercel-react-best-practices
- vercel-react-native-skills
- vue-best-practices
- xlsx
- youtube-api
- youtube-search

---

## Methodology

- **Scanner:** cisco-ai-skill-scanner
- **Analyzers:** behavioral_analyzer, llm_analyzer, meta_analyzer, static_analyzer, trigger_analyzer
- **Scan Date:** 2026-02-01T12:07:29.039611

### Limitations

- VirusTotal binary scanning not used (requires API key)
- No runtime verification - static and semantic analysis only
