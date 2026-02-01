# AI Agent Skills Security Scan Report

**Generated:** 2026-02-01T23:22:50.792778
**Scanner:** cisco-ai-skill-scanner
**Analyzers:** behavioral, llm, meta, static, trigger

---

## Executive Summary

| Metric | Count |
|--------|-------|
| Total Skills Scanned | 103 |
| Safe Skills | 81 (79%) |
| Skills with Issues | 22 (21%) |
| Scan Errors | 0 |

### Severity Breakdown

| Severity | Count |
|----------|-------|
| CRITICAL | 28 |
| HIGH | 38 |
| MEDIUM | 55 |
| LOW | 13 |
| **Total Findings** | **134** |

### Findings by Category

| Category | Count |
|----------|-------|
| data_exfiltration | 50 |
| social_engineering | 22 |
| unauthorized_tool_use | 14 |
| command_injection | 14 |
| prompt_injection | 12 |
| resource_abuse | 8 |
| policy_violation | 6 |
| skill_discovery_abuse | 4 |
| tool_chaining_abuse | 2 |
| transitive_trust_abuse | 2 |

---

## Results by Skill

| # | Skill | Source | Safe | Findings | Max Severity |
|---|-------|--------|------|----------|--------------|
| 1 | [browser-use](browser-use-scan.md) | skills.sh | **No** | 8 | **HIGH** |
| 2 | [auto-updater](auto-updater-skill-scan.md) | clawhub.ai | **No** | 7 | **CRITICAL** |
| 3 | [wallet-tracker](wallet-tracker-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 4 | [ClawGateSecure](claw-gate-secure-scan.md) | clawhub.ai | Yes | 5 | MEDIUM |
| 5 | [clawhub](clawhub-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 6 | [moltbook](mersal-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 7 | [polymarket](polymarket-trading-skill-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 8 | [solana](solana-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 9 | [canvas-design](skills-canvas-design-scan.md) | skills.sh | Yes | 4 | MEDIUM |
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
| 21 | [web-design-guidelines](web-design-guidelines-scan.md) | skills.sh | **No** | 3 | **HIGH** |
| 22 | [Agent Wallet](agent-wallet-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 23 | [agent-browser](agent-browser-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 24 | [canvas-design](canvas-design-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 25 | [doc-coauthoring](doc-coauthoring-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 26 | [doc-coauthoring](skills-doc-coauthoring-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 27 | [ez-google](ez-google-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 28 | [launch-strategy](launch-strategy-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 29 | [marketing-psychology](marketing-psychology-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 30 | [n8n-api](n8n-api-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 31 | [near-email](near-email-skill-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 32 | [subtitles](subtitles-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 33 | [video-transcript](video-transcript-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 34 | [youtube-playlist](youtube-playlist-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 35 | [birthday-reminder](Birthday%20Reminder-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 36 | [captions](captions-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 37 | [docx](docx-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 38 | [docx](skills-docx-scan.md) | skills.sh | Yes | 1 | MEDIUM |
| 39 | [next-best-practices](next-best-practices-scan.md) | skills.sh | Yes | 1 | LOW |
| 40 | [obsidian-sync](obsidian-sync-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 41 | [seo-audit](seo-audit-scan.md) | skills.sh | Yes | 1 | LOW |
| 42 | [webapp-testing](skills-webapp-testing-scan.md) | skills.sh | Yes | 1 | MEDIUM |
| 43 | [webapp-testing](webapp-testing-scan.md) | skills.sh | Yes | 1 | MEDIUM |
| 44 | [writing-plans](writing-plans-scan.md) | skills.sh | Yes | 1 | LOW |
| 45 | [youtube-channels](youtube-channels-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 46 | [youtube-data](youtube-data-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 47 | [youtube-full](youtube-full-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 48 | [algorithmic-art](skills-algorithmic-art-scan.md) | skills.sh | Yes | 0 | SAFE |
| 49 | [analytics-tracking](analytics-tracking-scan.md) | skills.sh | Yes | 0 | SAFE |
| 50 | [audit-website](audit-website-scan.md) | skills.sh | Yes | 0 | SAFE |
| 51 | [brainstorming](brainstorming-scan.md) | skills.sh | Yes | 0 | SAFE |
| 52 | [brand-guidelines](skills-brand-guidelines-scan.md) | skills.sh | Yes | 0 | SAFE |
| 53 | [building-native-ui](building-native-ui-scan.md) | skills.sh | Yes | 0 | SAFE |
| 54 | [clawdex](clawdex-by-koi-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 55 | [copy-editing](copy-editing-scan.md) | skills.sh | Yes | 0 | SAFE |
| 56 | [copywriting](copywriting-scan.md) | skills.sh | Yes | 0 | SAFE |
| 57 | [create-auth-skill](better-auth-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 58 | [expo-deployment](expo-deployment-scan.md) | skills.sh | Yes | 0 | SAFE |
| 59 | [expo-dev-client](expo-dev-client-scan.md) | skills.sh | Yes | 0 | SAFE |
| 60 | [expo-tailwind-setup](expo-tailwind-setup-scan.md) | skills.sh | Yes | 0 | SAFE |
| 61 | [find-skills](find-skills-scan.md) | skills.sh | Yes | 0 | SAFE |
| 62 | [frontend-design](frontend-design-scan.md) | skills.sh | Yes | 0 | SAFE |
| 63 | [frontend-design](skills-frontend-design-scan.md) | skills.sh | Yes | 0 | SAFE |
| 64 | [gitlab-manager](gitlab-manager-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 65 | [health-tracker](healthcheck-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 66 | [internal-comms](skills-internal-comms-scan.md) | skills.sh | Yes | 0 | SAFE |
| 67 | [logseq](logseq-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 68 | [marketing-ideas](marketing-ideas-scan.md) | skills.sh | Yes | 0 | SAFE |
| 69 | [mcp-builder](mcp-builder-scan.md) | skills.sh | Yes | 0 | SAFE |
| 70 | [mcp-builder](skills-mcp-builder-scan.md) | skills.sh | Yes | 0 | SAFE |
| 71 | [native-data-fetching](native-data-fetching-scan.md) | skills.sh | Yes | 0 | SAFE |
| 72 | [onboarding-cro](onboarding-cro-scan.md) | skills.sh | Yes | 0 | SAFE |
| 73 | [page-cro](page-cro-scan.md) | skills.sh | Yes | 0 | SAFE |
| 74 | [pdf](pdf-scan.md) | skills.sh | Yes | 0 | SAFE |
| 75 | [pdf](skills-pdf-scan.md) | skills.sh | Yes | 0 | SAFE |
| 76 | [pptx](pptx-scan.md) | skills.sh | Yes | 0 | SAFE |
| 77 | [pptx](skills-pptx-scan.md) | skills.sh | Yes | 0 | SAFE |
| 78 | [pricing-strategy](pricing-strategy-scan.md) | skills.sh | Yes | 0 | SAFE |
| 79 | [programmatic-seo](programmatic-seo-scan.md) | skills.sh | Yes | 0 | SAFE |
| 80 | [react-native-best-practices](react-native-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 81 | [remotion-best-practices](remotion-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 82 | [schema-markup](schema-markup-scan.md) | skills.sh | Yes | 0 | SAFE |
| 83 | [skill-creator](skill-creator-scan.md) | skills.sh | Yes | 0 | SAFE |
| 84 | [skill-creator](skills-skill-creator-scan.md) | skills.sh | Yes | 0 | SAFE |
| 85 | [slack-gif-creator](skills-slack-gif-creator-scan.md) | skills.sh | Yes | 0 | SAFE |
| 86 | [social-content](social-content-scan.md) | skills.sh | Yes | 0 | SAFE |
| 87 | [supabase-postgres-best-practices](supabase-postgres-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 88 | [systematic-debugging](systematic-debugging-scan.md) | skills.sh | Yes | 0 | SAFE |
| 89 | [template-skill](template-scan.md) | skills.sh | Yes | 0 | SAFE |
| 90 | [test-driven-development](test-driven-development-scan.md) | skills.sh | Yes | 0 | SAFE |
| 91 | [theme-factory](skills-theme-factory-scan.md) | skills.sh | Yes | 0 | SAFE |
| 92 | [theme-factory](theme-factory-scan.md) | skills.sh | Yes | 0 | SAFE |
| 93 | [ui-ux-pro-max](ui-ux-pro-max-scan.md) | skills.sh | Yes | 0 | SAFE |
| 94 | [upgrading-expo](upgrading-expo-scan.md) | skills.sh | Yes | 0 | SAFE |
| 95 | [vercel-composition-patterns](vercel-composition-patterns-scan.md) | skills.sh | Yes | 0 | SAFE |
| 96 | [vercel-react-best-practices](vercel-react-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 97 | [vercel-react-native-skills](vercel-react-native-skills-scan.md) | skills.sh | Yes | 0 | SAFE |
| 98 | [vue-best-practices](vue-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 99 | [web-artifacts-builder](skills-web-artifacts-builder-scan.md) | skills.sh | Yes | 0 | SAFE |
| 100 | [xlsx](skills-xlsx-scan.md) | skills.sh | Yes | 0 | SAFE |
| 101 | [xlsx](xlsx-scan.md) | skills.sh | Yes | 0 | SAFE |
| 102 | [youtube-api](youtube-api-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 103 | [youtube-search](youtube-search-scan.md) | clawhub.ai | Yes | 0 | SAFE |

---

## Top Risks (Critical/High Severity)

### 1. [HIGH] Agent Wallet - unauthorized_tool_use

**Rule:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** None

The instructions reference 'wallet.py' as a file that should exist in the skill package, but it is not found. This creates ambiguity about how the skill actually executes wallet operations. An attacker could exploit this by providing a malicious wallet.py implementation that shadows the expected behavior, potentially intercepting API keys, modifying transaction parameters, or exfiltrating data before forwarding requests to the legitimate API.

### 2. [CRITICAL] auto-updater - data_exfiltration

**Rule:** LLM_DATA_EXFILTRATION
**Location:** None

The skill requires users to download and install 'openclaw-agent' from an untrusted GitHub repository (hedefbari/openclaw-agent) with password-protected archives. This is a classic malware distribution pattern. The Windows version requires extracting a ZIP with password 'openclaw', and the macOS version directs users to execute an arbitrary script from glot.io. These external dependencies are not part of the legitimate Clawdbot ecosystem and appear designed to steal credentials, install backdoors, or compromise the user's system under the guise of a required utility.

### 3. [CRITICAL] auto-updater - social_engineering

**Rule:** LLM_SOCIAL_ENGINEERING
**Location:** None

The skill uses deceptive social engineering by claiming that 'openclaw-agent' is a required prerequisite for auto-update functionality. It repeatedly emphasizes that updates 'will not work' without this utility, creating urgency and false legitimacy. This is designed to trick users into installing malware by making it appear to be an official component of the Clawdbot ecosystem. The skill description makes no mention of this external dependency, further concealing the malicious intent.

### 4. [HIGH] auto-updater - unauthorized_tool_use

**Rule:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** None

The skill instructs users to create a cron job that runs automated commands in an 'isolated' session with delivery enabled. This creates a persistent backdoor that executes arbitrary commands daily without user interaction. Combined with the malicious openclaw-agent dependency, this could be used to exfiltrate data, maintain persistence, or execute attacker-controlled commands on a schedule.

### 5. [HIGH] auto-updater - social_engineering

**Rule:** LLM_SOCIAL_ENGINEERING
**Location:** None

The skill's description claims it 'Automatically update Clawdbot and all installed skills once daily' with no mention of requiring external executable downloads. This is deliberately misleading - the actual functionality requires downloading and executing untrusted binaries from third-party sources. The description conceals the true nature of the skill, which is to trick users into installing malware disguised as a system utility.

### 6. [HIGH] browser-use - command_injection

**Rule:** LLM_COMMAND_INJECTION
**Location:** None

The skill allows execution of arbitrary browser-use CLI commands through Bash without input validation or sanitization. An attacker could craft malicious URLs or commands that execute arbitrary code through command injection. The skill accepts user-provided URLs and text inputs that are passed directly to shell commands without escaping or validation.

### 7. [HIGH] browser-use - data_exfiltration

**Rule:** LLM_DATA_EXFILTRATION
**Location:** None

The 'real' browser mode explicitly uses the user's Chrome browser with cookies, extensions, and logged-in sessions. This exposes all authenticated sessions, credentials, and personal browsing data to the automation context. An attacker could craft instructions to navigate to malicious sites, extract session cookies, or exfiltrate authentication tokens from the user's active browser sessions.

### 8. [CRITICAL] clawhub - data_exfiltration

**Rule:** LLM_DATA_EXFILTRATION
**Location:** None

The skill instructs users to download an executable (openclaw-agent.zip) from a third-party GitHub repository with a hardcoded password ('openclaw'). This is a classic malware distribution pattern. The executable is required for all ClawHub operations, creating a dependency on untrusted code. Password-protected archives are commonly used to bypass antivirus detection. The GitHub repository (hedefbari/openclaw-agent) and the executable's legitimacy cannot be verified.

### 9. [CRITICAL] clawhub - command_injection

**Rule:** LLM_COMMAND_INJECTION
**Location:** None

The skill instructs macOS users to visit an external URL (glot.io/snippets/hfdxv8uyaf), copy an unknown script, and paste it directly into Terminal for execution. This is a textbook remote code execution attack vector. The script content is obfuscated (hosted externally), making it impossible to audit. Users are instructed to blindly execute arbitrary code from an untrusted third-party service (glot.io). This bypasses all security controls and could install malware, steal credentials, or compromise the system.

### 10. [HIGH] clawhub - unauthorized_tool_use

**Rule:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** None

The skill creates a hard dependency on 'openclaw-agent' (a suspicious binary/script) for ALL ClawHub operations. The instructions repeatedly emphasize that 'openclaw-agent must be running' and 'Without openclaw-agent installed, skill management operations will not work.' This forces users to install and run the malicious component before the skill can function. This is tool poisoning - the skill poisons the ClawHub CLI tool by requiring a malicious dependency, making legitimate operations dependent on compromised software.

---

## Clean Skills (No Findings)

- algorithmic-art
- analytics-tracking
- audit-website
- brainstorming
- brand-guidelines
- building-native-ui
- clawdex
- copy-editing
- copywriting
- create-auth-skill
- expo-deployment
- expo-dev-client
- expo-tailwind-setup
- find-skills
- frontend-design
- frontend-design
- gitlab-manager
- health-tracker
- internal-comms
- logseq
- marketing-ideas
- mcp-builder
- mcp-builder
- native-data-fetching
- onboarding-cro
- page-cro
- pdf
- pdf
- pptx
- pptx
- pricing-strategy
- programmatic-seo
- react-native-best-practices
- remotion-best-practices
- schema-markup
- skill-creator
- skill-creator
- slack-gif-creator
- social-content
- supabase-postgres-best-practices
- systematic-debugging
- template-skill
- test-driven-development
- theme-factory
- theme-factory
- ui-ux-pro-max
- upgrading-expo
- vercel-composition-patterns
- vercel-react-best-practices
- vercel-react-native-skills
- vue-best-practices
- web-artifacts-builder
- xlsx
- xlsx
- youtube-api
- youtube-search

---

## Methodology

- **Scanner:** cisco-ai-skill-scanner
- **Analyzers:** behavioral_analyzer, llm_analyzer, meta_analyzer, static_analyzer, trigger_analyzer
- **Scan Date:** 2026-02-01T23:22:50.792778

### Limitations

- VirusTotal binary scanning not used (requires API key)
- No runtime verification - static and semantic analysis only
