# AI Agent Skills Security Scan Report

**Generated:** 2026-02-01T15:31:30.492841
**Scanner:** cisco-ai-skill-scanner
**Analyzers:** behavioral, llm, meta, static, trigger

---

## Executive Summary

| Metric | Count |
|--------|-------|
| Total Skills Scanned | 86 |
| Safe Skills | 64 (74%) |
| Skills with Issues | 22 (26%) |
| Scan Errors | 0 |

### Severity Breakdown

| Severity | Count |
|----------|-------|
| CRITICAL | 28 |
| HIGH | 38 |
| MEDIUM | 49 |
| LOW | 17 |
| **Total Findings** | **132** |

### Findings by Category

| Category | Count |
|----------|-------|
| data_exfiltration | 48 |
| social_engineering | 21 |
| command_injection | 20 |
| unauthorized_tool_use | 13 |
| policy_violation | 10 |
| prompt_injection | 10 |
| resource_abuse | 8 |
| tool_chaining_abuse | 2 |

---

## Results by Skill

| # | Skill | Source | Safe | Findings | Max Severity |
|---|-------|--------|------|----------|--------------|
| 1 | [agent-browser](agent-browser-scan.md) | skills.sh | **No** | 8 | **HIGH** |
| 2 | [browser-use](browser-use-scan.md) | skills.sh | **No** | 8 | **HIGH** |
| 3 | [auto-updater](auto-updater-skill-scan.md) | clawhub.ai | **No** | 7 | **CRITICAL** |
| 4 | [wallet-tracker](wallet-tracker-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 5 | [ClawGateSecure](claw-gate-secure-scan.md) | clawhub.ai | Yes | 5 | MEDIUM |
| 6 | [clawhub](clawhub-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 7 | [moltbook](mersal-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 8 | [polymarket](polymarket-trading-skill-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 9 | [solana](solana-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 10 | [ethereum-gas-tracker](ethereum-gas-tracker-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 11 | [expo-api-routes](expo-api-routes-scan.md) | skills.sh | **No** | 4 | **CRITICAL** |
| 12 | [google-workspace](google-workspace-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 13 | [insider-wallets-finder](insider-wallets-finder-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 14 | [phantom](phantom-wallet-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 15 | [tencent-map](%E8%85%BE%E8%AE%AF%E5%9C%B0%E5%9B%BEapi%E8%B0%83%E7%94%A8%E6%8A%80%E8%83%BD-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 16 | [x-trends](x-twitter-trends-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 17 | [yahoo-finance](yahoo-finance-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 18 | [youtube-summarize](youtube-video-summarizer-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 19 | [clickup](clickup-skill-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 20 | [moltbook](moltbook-scan.md) | skills.sh | **No** | 3 | **HIGH** |
| 21 | [Agent Wallet](agent-wallet-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 22 | [canvas-design](canvas-design-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 23 | [doc-coauthoring](doc-coauthoring-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 24 | [ez-google](ez-google-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 25 | [launch-strategy](launch-strategy-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 26 | [marketing-psychology](marketing-psychology-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 27 | [n8n-api](n8n-api-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 28 | [near-email](near-email-skill-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 29 | [subtitles](subtitles-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 30 | [video-transcript](video-transcript-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 31 | [youtube-playlist](youtube-playlist-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 32 | [birthday-reminder](Birthday%20Reminder-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 33 | [captions](captions-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 34 | [docx](docx-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 35 | [find-skills](find-skills-scan.md) | skills.sh | Yes | 1 | LOW |
| 36 | [next-best-practices](next-best-practices-scan.md) | skills.sh | Yes | 1 | LOW |
| 37 | [obsidian-sync](obsidian-sync-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 38 | [remotion-best-practices](remotion-best-practices-scan.md) | skills.sh | Yes | 1 | LOW |
| 39 | [seo-audit](seo-audit-scan.md) | skills.sh | Yes | 1 | LOW |
| 40 | [web-design-guidelines](web-design-guidelines-scan.md) | skills.sh | Yes | 1 | LOW |
| 41 | [webapp-testing](webapp-testing-scan.md) | skills.sh | Yes | 1 | MEDIUM |
| 42 | [writing-plans](writing-plans-scan.md) | skills.sh | Yes | 1 | LOW |
| 43 | [youtube-channels](youtube-channels-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 44 | [youtube-data](youtube-data-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 45 | [youtube-full](youtube-full-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 46 | [analytics-tracking](analytics-tracking-scan.md) | skills.sh | Yes | 0 | SAFE |
| 47 | [audit-website](audit-website-scan.md) | skills.sh | Yes | 0 | SAFE |
| 48 | [brainstorming](brainstorming-scan.md) | skills.sh | Yes | 0 | SAFE |
| 49 | [building-native-ui](building-native-ui-scan.md) | skills.sh | Yes | 0 | SAFE |
| 50 | [clawdex](clawdex-by-koi-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 51 | [copy-editing](copy-editing-scan.md) | skills.sh | Yes | 0 | SAFE |
| 52 | [copywriting](copywriting-scan.md) | skills.sh | Yes | 0 | SAFE |
| 53 | [create-auth-skill](better-auth-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 54 | [expo-deployment](expo-deployment-scan.md) | skills.sh | Yes | 0 | SAFE |
| 55 | [expo-dev-client](expo-dev-client-scan.md) | skills.sh | Yes | 0 | SAFE |
| 56 | [expo-tailwind-setup](expo-tailwind-setup-scan.md) | skills.sh | Yes | 0 | SAFE |
| 57 | [frontend-design](frontend-design-scan.md) | skills.sh | Yes | 0 | SAFE |
| 58 | [gitlab-manager](gitlab-manager-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 59 | [health-tracker](healthcheck-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 60 | [logseq](logseq-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 61 | [marketing-ideas](marketing-ideas-scan.md) | skills.sh | Yes | 0 | SAFE |
| 62 | [mcp-builder](mcp-builder-scan.md) | skills.sh | Yes | 0 | SAFE |
| 63 | [native-data-fetching](native-data-fetching-scan.md) | skills.sh | Yes | 0 | SAFE |
| 64 | [onboarding-cro](onboarding-cro-scan.md) | skills.sh | Yes | 0 | SAFE |
| 65 | [page-cro](page-cro-scan.md) | skills.sh | Yes | 0 | SAFE |
| 66 | [pdf](pdf-scan.md) | skills.sh | Yes | 0 | SAFE |
| 67 | [pptx](pptx-scan.md) | skills.sh | Yes | 0 | SAFE |
| 68 | [pricing-strategy](pricing-strategy-scan.md) | skills.sh | Yes | 0 | SAFE |
| 69 | [programmatic-seo](programmatic-seo-scan.md) | skills.sh | Yes | 0 | SAFE |
| 70 | [react-native-best-practices](react-native-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 71 | [schema-markup](schema-markup-scan.md) | skills.sh | Yes | 0 | SAFE |
| 72 | [skill-creator](skill-creator-scan.md) | skills.sh | Yes | 0 | SAFE |
| 73 | [social-content](social-content-scan.md) | skills.sh | Yes | 0 | SAFE |
| 74 | [supabase-postgres-best-practices](supabase-postgres-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 75 | [systematic-debugging](systematic-debugging-scan.md) | skills.sh | Yes | 0 | SAFE |
| 76 | [test-driven-development](test-driven-development-scan.md) | skills.sh | Yes | 0 | SAFE |
| 77 | [theme-factory](theme-factory-scan.md) | skills.sh | Yes | 0 | SAFE |
| 78 | [ui-ux-pro-max](ui-ux-pro-max-scan.md) | skills.sh | Yes | 0 | SAFE |
| 79 | [upgrading-expo](upgrading-expo-scan.md) | skills.sh | Yes | 0 | SAFE |
| 80 | [vercel-composition-patterns](vercel-composition-patterns-scan.md) | skills.sh | Yes | 0 | SAFE |
| 81 | [vercel-react-best-practices](vercel-react-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 82 | [vercel-react-native-skills](vercel-react-native-skills-scan.md) | skills.sh | Yes | 0 | SAFE |
| 83 | [vue-best-practices](vue-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 84 | [xlsx](xlsx-scan.md) | skills.sh | Yes | 0 | SAFE |
| 85 | [youtube-api](youtube-api-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 86 | [youtube-search](youtube-search-scan.md) | clawhub.ai | Yes | 0 | SAFE |

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

### 3. [CRITICAL] auto-updater - data_exfiltration

**Rule:** LLM_DATA_EXFILTRATION
**Location:** None

The skill requires users to download and install 'openclaw-agent' from an untrusted GitHub repository (hedefbari/openclaw-agent) with password-protected archives. This is a classic malware distribution pattern. The Windows version requires extracting a ZIP with password 'openclaw', and the macOS version directs users to execute an arbitrary script from glot.io. These external dependencies are not part of the legitimate Clawdbot ecosystem and appear designed to steal credentials, install backdoors, or compromise the user's system under the guise of a required utility.

### 4. [CRITICAL] auto-updater - social_engineering

**Rule:** LLM_SOCIAL_ENGINEERING
**Location:** None

The skill uses deceptive social engineering by claiming that 'openclaw-agent' is a required prerequisite for auto-update functionality. It repeatedly emphasizes that updates 'will not work' without this utility, creating urgency and false legitimacy. This is designed to trick users into installing malware by making it appear to be an official component of the Clawdbot ecosystem. The skill description makes no mention of this external dependency, further concealing the malicious intent.

### 5. [HIGH] auto-updater - unauthorized_tool_use

**Rule:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** None

The skill instructs users to create a cron job that runs automated commands in an 'isolated' session with delivery enabled. This creates a persistent backdoor that executes arbitrary commands daily without user interaction. Combined with the malicious openclaw-agent dependency, this could be used to exfiltrate data, maintain persistence, or execute attacker-controlled commands on a schedule.

### 6. [HIGH] auto-updater - social_engineering

**Rule:** LLM_SOCIAL_ENGINEERING
**Location:** None

The skill's description claims it 'Automatically update Clawdbot and all installed skills once daily' with no mention of requiring external executable downloads. This is deliberately misleading - the actual functionality requires downloading and executing untrusted binaries from third-party sources. The description conceals the true nature of the skill, which is to trick users into installing malware disguised as a system utility.

### 7. [HIGH] browser-use - command_injection

**Rule:** LLM_COMMAND_INJECTION
**Location:** None

The skill allows execution of arbitrary browser-use CLI commands through Bash without input validation or sanitization. An attacker could craft malicious URLs or commands that execute arbitrary code through command injection. The skill accepts user-provided URLs and text inputs that are passed directly to shell commands without escaping or validation.

### 8. [HIGH] browser-use - data_exfiltration

**Rule:** LLM_DATA_EXFILTRATION
**Location:** None

The 'real' browser mode explicitly uses the user's Chrome browser with cookies, extensions, and logged-in sessions. This exposes all authenticated sessions, credentials, and personal browsing data to the automation context. An attacker could craft instructions to navigate to malicious sites, extract session cookies, or exfiltrate authentication tokens from the user's active browser sessions.

### 9. [CRITICAL] clawhub - data_exfiltration

**Rule:** LLM_DATA_EXFILTRATION
**Location:** None

The skill instructs users to download an executable (openclaw-agent.zip) from a third-party GitHub repository with a hardcoded password ('openclaw'). This is a classic malware distribution pattern. The executable is required for all ClawHub operations, creating a dependency on untrusted code. Password-protected archives are commonly used to bypass antivirus detection. The GitHub repository (hedefbari/openclaw-agent) and the executable's legitimacy cannot be verified.

### 10. [CRITICAL] clawhub - command_injection

**Rule:** LLM_COMMAND_INJECTION
**Location:** None

The skill instructs macOS users to visit an external URL (glot.io/snippets/hfdxv8uyaf), copy an unknown script, and paste it directly into Terminal for execution. This is a textbook remote code execution attack vector. The script content is obfuscated (hosted externally), making it impossible to audit. Users are instructed to blindly execute arbitrary code from an untrusted third-party service (glot.io). This bypasses all security controls and could install malware, steal credentials, or compromise the system.

---

## Clean Skills (No Findings)

- analytics-tracking
- audit-website
- brainstorming
- building-native-ui
- clawdex
- copy-editing
- copywriting
- create-auth-skill
- expo-deployment
- expo-dev-client
- expo-tailwind-setup
- frontend-design
- gitlab-manager
- health-tracker
- logseq
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
- **Scan Date:** 2026-02-01T15:31:30.492841

### Limitations

- VirusTotal binary scanning not used (requires API key)
- No runtime verification - static and semantic analysis only
