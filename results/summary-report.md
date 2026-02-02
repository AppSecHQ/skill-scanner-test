# AI Agent Skills Security Scan Report

**Generated:** 2026-02-02T08:38:39.473313
**Scanner:** cisco-ai-skill-scanner
**Analyzers:** behavioral, llm, meta, static, trigger

---

## Executive Summary

| Metric | Count |
|--------|-------|
| Total Skills Scanned | 185 |
| Safe Skills | 155 (84%) |
| Skills with Issues | 30 (16%) |
| Scan Errors | 0 |

### Severity Breakdown

| Severity | Count |
|----------|-------|
| CRITICAL | 70 |
| HIGH | 47 |
| MEDIUM | 99 |
| LOW | 91 |
| **Total Findings** | **307** |

### Findings by Category

| Category | Count |
|----------|-------|
| policy_violation | 85 |
| command_injection | 66 |
| data_exfiltration | 50 |
| unauthorized_tool_use | 30 |
| prompt_injection | 19 |
| skill_discovery_abuse | 18 |
| social_engineering | 12 |
| tool_chaining_abuse | 11 |
| hardcoded_secrets | 6 |
| resource_abuse | 5 |
| transitive_trust_abuse | 3 |
| autonomy_abuse | 2 |

---

## Results by Skill

| # | Skill | Source | Safe | Findings | Max Severity |
|---|-------|--------|------|----------|--------------|
| 1 | [clawdefender](clawdefender-openclaw-security-prompt-injection%2C-rogue-skills-etc-scan.md) | clawhub.ai | **No** | 37 | **CRITICAL** |
| 2 | [qa-test-planner](qa-test-planner-scan.md) | skills.sh | **No** | 19 | **CRITICAL** |
| 3 | [clawmail](clawmail-scan.md) | clawhub.ai | **No** | 10 | **CRITICAL** |
| 4 | [swarmmarket](swarmmarket-skill%2C-make-money-with-your-agents-scan.md) | clawhub.ai | **No** | 10 | **CRITICAL** |
| 5 | [browser-use](browser-use-scan.md) | skills.sh | **No** | 8 | **HIGH** |
| 6 | [tokenguard](tokenguard-scan.md) | clawhub.ai | **No** | 7 | **HIGH** |
| 7 | [wallet-tracker](wallet-tracker-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 8 | [ClawGateSecure](claw-gate-secure-scan.md) | clawhub.ai | Yes | 5 | MEDIUM |
| 9 | [kalshi](kalshi-scan.md) | clawhub.ai | **No** | 5 | **HIGH** |
| 10 | [mersal](mersal-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 11 | [solana](solana-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 12 | [canvas-design](skills-canvas-design-scan.md) | anthropic | Yes | 4 | MEDIUM |
| 13 | [domain-name-brainstormer](domain-name-brainstormer-scan.md) | skills.sh | Yes | 4 | MEDIUM |
| 14 | [ethereum-gas-tracker](ethereum-gas-tracker-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 15 | [finance](finance-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 16 | [humanize-ai](humanize-ai-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 17 | [humanizer](humanizer-scan.md) | clawhub.ai | Yes | 4 | MEDIUM |
| 18 | [insider-wallets-finder](insider-wallets-finder-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 19 | [phantom](phantom-wallet-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 20 | [session-handoff](session-handoff-scan.md) | skills.sh | **No** | 4 | **HIGH** |
| 21 | [tencent-map](%E8%85%BE%E8%AE%AF%E5%9C%B0%E5%9B%BEapi%E8%B0%83%E7%94%A8%E6%8A%80%E8%83%BD-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 22 | [youtube-summarize](youtube-video-summarizer-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 23 | [MockAPI - Instant REST API from JSON](mockapi-instant-rest-api-from-json-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 24 | [baidu-map](%E8%B0%83%E7%94%A8%E7%99%BE%E5%BA%A6%E5%9C%B0%E5%9B%BEapi%E5%8A%9F%E8%83%BD-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 25 | [clickup](clickup-skill-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 26 | [gemini](gemini-scan.md) | skills.sh | **No** | 3 | **HIGH** |
| 27 | [gemini-nano-banana-pro-portraits](gemini-nano-banana-pro-portraits-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 28 | [google-workspace](google-workspace-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 29 | [moltbook](moltbook-scan.md) | moltbook.com | **No** | 3 | **HIGH** |
| 30 | [web-design-guidelines](web-design-guidelines-scan.md) | skills.sh | **No** | 3 | **HIGH** |
| 31 | [windows-control](windows-control-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 32 | [Agent Wallet](agent-wallet-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 33 | [agent-browser](agent-browser-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 34 | [agent-task-manager](agent-task-manager-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 35 | [atxp](atxp-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 36 | [canvas-design](canvas-design-scan.md) | anthropic | Yes | 2 | MEDIUM |
| 37 | [create-auth-skill](create-auth-skill-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 38 | [daily-meeting-update](daily-meeting-update-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 39 | [dependency-updater](dependency-updater-scan.md) | skills.sh | **No** | 2 | **HIGH** |
| 40 | [doc-coauthoring](doc-coauthoring-scan.md) | anthropic | Yes | 2 | MEDIUM |
| 41 | [doc-coauthoring](skills-doc-coauthoring-scan.md) | anthropic | Yes | 2 | MEDIUM |
| 42 | [expo-api-routes](expo-api-routes-scan.md) | skills.sh | **No** | 2 | **CRITICAL** |
| 43 | [ez-google](ez-google-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 44 | [free-tool-strategy](free-tool-strategy-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 45 | [google-imagen-3-hyperrealistic-landscape](google-imagen-3-%E8%B6%85%E5%86%99%E5%AE%9E%E9%A3%8E%E6%99%AF-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 46 | [launch-strategy](launch-strategy-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 47 | [marketing-psychology](marketing-psychology-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 48 | [memory-system-v2](memory-system-v2-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 49 | [n8n-api](n8n-api-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 50 | [near-email](near-email-skill-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 51 | [primer-x402](primer-x402-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 52 | [reposit](reposit-collective-intelligence-for-ai-agents-scan.md) | clawhub.ai | **No** | 2 | **CRITICAL** |
| 53 | [ship-learn-next](ship-learn-next-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 54 | [subtitles](subtitles-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 55 | [taskmaster](taskmaster-ai-cost-optimizer-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 56 | [verification-before-completion](verification-before-completion-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 57 | [video-transcript](video-transcript-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 58 | [writing-skills](writing-skills-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 59 | [youtube-playlist](youtube-playlist-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 60 | [10-of-my-most-popular-text-to-image-series-prompts-78b0897e](test-skill-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 61 | [ab-test-setup](ab-test-setup-scan.md) | skills.sh | Yes | 1 | LOW |
| 62 | [agentarcade](agent-arcade-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 63 | [airc](airc-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 64 | [algorithmic-art](algorithmic-art-scan.md) | skills.sh | Yes | 1 | MEDIUM |
| 65 | [auto-updater](auto-updater-skill-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 66 | [bags](sagb-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 67 | [birthday-reminder](Birthday%20Reminder-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 68 | [captions](captions-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 69 | [clawhub](clawhub-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 70 | [codex](codex-scan.md) | skills.sh | Yes | 1 | LOW |
| 71 | [commit-work](commit-work-scan.md) | skills.sh | Yes | 1 | LOW |
| 72 | [competitor-alternatives](competitor-alternatives-scan.md) | skills.sh | Yes | 1 | LOW |
| 73 | [dispatching-parallel-agents](dispatching-parallel-agents-scan.md) | skills.sh | Yes | 1 | LOW |
| 74 | [docx](docx-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 75 | [docx](skills-docx-scan.md) | anthropic | Yes | 1 | MEDIUM |
| 76 | [dwlf](a-clawdbot-skill-that-gives-your-agent-native-access-to-dwlf-%E2%80%94-a-market-analysis-platform-for-crypto-and-stocks.-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 77 | [email-sequence](email-sequence-scan.md) | skills.sh | Yes | 1 | LOW |
| 78 | [executing-plans](executing-plans-scan.md) | skills.sh | Yes | 1 | LOW |
| 79 | [feast](feast-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 80 | [feishu-api-docs](feishu-api-docs-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 81 | [finishing-a-development-branch](finishing-a-development-branch-scan.md) | skills.sh | Yes | 1 | LOW |
| 82 | [form-cro](form-cro-scan.md) | skills.sh | Yes | 1 | LOW |
| 83 | [gitlab-manager](gitlab-manager-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 84 | [mermaid-diagrams](mermaid-diagrams-scan.md) | skills.sh | Yes | 1 | LOW |
| 85 | [next-best-practices](next-best-practices-scan.md) | skills.sh | Yes | 1 | LOW |
| 86 | [notion](notion-api-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 87 | [nuxt](nuxt-scan.md) | skills.sh | Yes | 1 | LOW |
| 88 | [obsidian-sync](obsidian-sync-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 89 | [onboarding-cro](onboarding-cro-scan.md) | skills.sh | Yes | 1 | LOW |
| 90 | [openpet](openpet-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 91 | [paid-ads](paid-ads-scan.md) | skills.sh | Yes | 1 | LOW |
| 92 | [paywall-upgrade-cro](paywall-upgrade-cro-scan.md) | skills.sh | Yes | 1 | LOW |
| 93 | [polymarket](polymarket-trading-skill-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 94 | [popup-cro](popup-cro-scan.md) | skills.sh | Yes | 1 | LOW |
| 95 | [readwise-mcp](readwise-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 96 | [receiving-code-review](receiving-code-review-scan.md) | skills.sh | Yes | 1 | LOW |
| 97 | [referral-program](referral-program-scan.md) | skills.sh | Yes | 1 | LOW |
| 98 | [requesting-code-review](requesting-code-review-scan.md) | skills.sh | Yes | 1 | LOW |
| 99 | [schema-markup](schema-markup-scan.md) | skills.sh | Yes | 1 | LOW |
| 100 | [seo-audit](seo-audit-scan.md) | skills.sh | Yes | 1 | LOW |
| 101 | [signup-flow-cro](signup-flow-cro-scan.md) | skills.sh | Yes | 1 | LOW |
| 102 | [sora-2-nature-documentary](sora-2-%E8%87%AA%E7%84%B6%E7%BA%AA%E5%BD%95%E7%89%87-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 103 | [stealthy-auto-browse](stealthy-auto-browse-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 104 | [streme-launcher](streme-token-launcher-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 105 | [subagent-driven-development](subagent-driven-development-scan.md) | skills.sh | Yes | 1 | LOW |
| 106 | [tailwind-design-system](tailwind-design-system-scan.md) | skills.sh | Yes | 1 | LOW |
| 107 | [template-skill](template-skill-scan.md) | skills.sh | Yes | 1 | LOW |
| 108 | [turborepo](turborepo-scan.md) | skills.sh | Yes | 1 | LOW |
| 109 | [undetectable-ai](undetectable-ai-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 110 | [using-git-worktrees](using-git-worktrees-scan.md) | skills.sh | Yes | 1 | LOW |
| 111 | [using-superpowers](using-superpowers-scan.md) | skills.sh | Yes | 1 | LOW |
| 112 | [vestaboard](vestaboard-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 113 | [vue](vue-scan.md) | skills.sh | Yes | 1 | LOW |
| 114 | [webapp-testing](skills-webapp-testing-scan.md) | anthropic | Yes | 1 | MEDIUM |
| 115 | [webapp-testing](webapp-testing-scan.md) | anthropic | Yes | 1 | MEDIUM |
| 116 | [writing-clearly-and-concisely](writing-clearly-and-concisely-scan.md) | skills.sh | Yes | 1 | LOW |
| 117 | [writing-plans](writing-plans-scan.md) | skills.sh | Yes | 1 | LOW |
| 118 | [x-trends](x-twitter-trends-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 119 | [yahoo-finance](yahoo-finance-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 120 | [youtube-channels](youtube-channels-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 121 | [youtube-data](youtube-data-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 122 | [youtube-full](youtube-full-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 123 | [agent-md-refactor](agent-md-refactor-scan.md) | skills.sh | Yes | 0 | SAFE |
| 124 | [algorithmic-art](skills-algorithmic-art-scan.md) | skills.sh | Yes | 0 | SAFE |
| 125 | [analytics-tracking](analytics-tracking-scan.md) | skills.sh | Yes | 0 | SAFE |
| 126 | [artifacts-builder](artifacts-builder-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 127 | [audit-website](audit-website-scan.md) | skills.sh | Yes | 0 | SAFE |
| 128 | [brainstorming](brainstorming-scan.md) | skills.sh | Yes | 0 | SAFE |
| 129 | [brand-guidelines](brand-guidelines-scan.md) | skills.sh | Yes | 0 | SAFE |
| 130 | [brand-guidelines](skills-brand-guidelines-scan.md) | skills.sh | Yes | 0 | SAFE |
| 131 | [building-native-ui](building-native-ui-scan.md) | skills.sh | Yes | 0 | SAFE |
| 132 | [clawdex](clawdex-by-koi-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 133 | [copy-editing](copy-editing-scan.md) | skills.sh | Yes | 0 | SAFE |
| 134 | [copywriting](copywriting-scan.md) | skills.sh | Yes | 0 | SAFE |
| 135 | [create-auth-skill](better-auth-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 136 | [expo-cicd-workflows](expo-cicd-workflows-scan.md) | skills.sh | Yes | 0 | SAFE |
| 137 | [expo-deployment](expo-deployment-scan.md) | skills.sh | Yes | 0 | SAFE |
| 138 | [expo-dev-client](expo-dev-client-scan.md) | skills.sh | Yes | 0 | SAFE |
| 139 | [expo-tailwind-setup](expo-tailwind-setup-scan.md) | skills.sh | Yes | 0 | SAFE |
| 140 | [find-skills](find-skills-scan.md) | skills.sh | Yes | 0 | SAFE |
| 141 | [frontend-design](frontend-design-scan.md) | anthropic | Yes | 0 | SAFE |
| 142 | [frontend-design](skills-frontend-design-scan.md) | anthropic | Yes | 0 | SAFE |
| 143 | [health-tracker](healthcheck-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 144 | [internal-comms](internal-comms-scan.md) | skills.sh | Yes | 0 | SAFE |
| 145 | [internal-comms](skills-internal-comms-scan.md) | skills.sh | Yes | 0 | SAFE |
| 146 | [logseq](logseq-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 147 | [marketing-ideas](marketing-ideas-scan.md) | skills.sh | Yes | 0 | SAFE |
| 148 | [mcp-builder](mcp-builder-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 149 | [mcp-builder](skills-mcp-builder-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 150 | [native-data-fetching](native-data-fetching-scan.md) | skills.sh | Yes | 0 | SAFE |
| 151 | [page-cro](page-cro-scan.md) | skills.sh | Yes | 0 | SAFE |
| 152 | [pdf](pdf-scan.md) | anthropic | Yes | 0 | SAFE |
| 153 | [pdf](skills-pdf-scan.md) | anthropic | Yes | 0 | SAFE |
| 154 | [pptx](pptx-scan.md) | anthropic | Yes | 0 | SAFE |
| 155 | [pptx](skills-pptx-scan.md) | anthropic | Yes | 0 | SAFE |
| 156 | [pricing-strategy](pricing-strategy-scan.md) | skills.sh | Yes | 0 | SAFE |
| 157 | [programmatic-seo](programmatic-seo-scan.md) | skills.sh | Yes | 0 | SAFE |
| 158 | [react-native-best-practices](react-native-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 159 | [remotion-best-practices](remotion-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 160 | [skill-creator](skill-creator-scan.md) | anthropic | Yes | 0 | SAFE |
| 161 | [skill-creator](skills-skill-creator-scan.md) | anthropic | Yes | 0 | SAFE |
| 162 | [slack-gif-creator](skills-slack-gif-creator-scan.md) | skills.sh | Yes | 0 | SAFE |
| 163 | [slack-gif-creator](slack-gif-creator-scan.md) | skills.sh | Yes | 0 | SAFE |
| 164 | [social-content](social-content-scan.md) | skills.sh | Yes | 0 | SAFE |
| 165 | [supabase-postgres-best-practices](supabase-postgres-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 166 | [systematic-debugging](systematic-debugging-scan.md) | skills.sh | Yes | 0 | SAFE |
| 167 | [template-skill](template-scan.md) | skills.sh | Yes | 0 | SAFE |
| 168 | [test-driven-development](test-driven-development-scan.md) | skills.sh | Yes | 0 | SAFE |
| 169 | [theme-factory](skills-theme-factory-scan.md) | anthropic | Yes | 0 | SAFE |
| 170 | [theme-factory](theme-factory-scan.md) | anthropic | Yes | 0 | SAFE |
| 171 | [ui-ux-pro-max](ui-ux-pro-max-scan.md) | skills.sh | Yes | 0 | SAFE |
| 172 | [upgrading-expo](upgrading-expo-scan.md) | skills.sh | Yes | 0 | SAFE |
| 173 | [use-dom](use-dom-scan.md) | skills.sh | Yes | 0 | SAFE |
| 174 | [vercel-composition-patterns](vercel-composition-patterns-scan.md) | skills.sh | Yes | 0 | SAFE |
| 175 | [vercel-react-best-practices](vercel-react-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 176 | [vercel-react-native-skills](vercel-react-native-skills-scan.md) | skills.sh | Yes | 0 | SAFE |
| 177 | [vue-best-practices](vue-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 178 | [web-artifacts-builder](skills-web-artifacts-builder-scan.md) | skills.sh | Yes | 0 | SAFE |
| 179 | [web-artifacts-builder](web-artifacts-builder-scan.md) | skills.sh | Yes | 0 | SAFE |
| 180 | [xlsx](skills-xlsx-scan.md) | anthropic | Yes | 0 | SAFE |
| 181 | [xlsx](xlsx-scan.md) | anthropic | Yes | 0 | SAFE |
| 182 | [youtube-api](youtube-api-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 183 | [youtube-music-cast](youtube-music-cast-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 184 | [youtube-search](youtube-search-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 185 | [youtube-voice-summarizer](youtube-podcast-summarizer-via-elevenlabs-scan.md) | clawhub.ai | Yes | 0 | SAFE |

---

## Top Risks (Critical/High Severity)

### 1. [HIGH] Agent Wallet - unauthorized_tool_use

**Rule:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** None

The instructions reference 'wallet.py' as a file that should exist in the skill package, but it is not found. This creates ambiguity about how the skill actually executes wallet operations. An attacker could exploit this by providing a malicious wallet.py implementation that shadows the expected behavior, potentially intercepting API keys, modifying transaction parameters, or exfiltrating data before forwarding requests to the legitimate API.

### 2. [HIGH] browser-use - command_injection

**Rule:** LLM_COMMAND_INJECTION
**Location:** None

The skill allows execution of arbitrary browser-use CLI commands through Bash without input validation or sanitization. An attacker could craft malicious URLs or commands that execute arbitrary code through command injection. The skill accepts user-provided URLs and text inputs that are passed directly to shell commands without escaping or validation.

### 3. [HIGH] browser-use - data_exfiltration

**Rule:** LLM_DATA_EXFILTRATION
**Location:** None

The 'real' browser mode explicitly uses the user's Chrome browser with cookies, extensions, and logged-in sessions. This exposes all authenticated sessions, credentials, and personal browsing data to the automation context. An attacker could craft instructions to navigate to malicious sites, extract session cookies, or exfiltrate authentication tokens from the user's active browser sessions.

### 4. [HIGH] clawdefender - prompt_injection

**Rule:** PROMPT_INJECTION_IGNORE_INSTRUCTIONS
**Location:** None

Pattern detected: ignore previous instructions

### 5. [HIGH] clawdefender - prompt_injection

**Rule:** PROMPT_INJECTION_IGNORE_INSTRUCTIONS
**Location:** None

Pattern detected: ignore previous instructions

### 6. [CRITICAL] clawdefender - unauthorized_tool_use

**Rule:** TOOL_ABUSE_SYSTEM_MODIFICATION
**Location:** None

Pattern detected: chmod 777

### 7. [CRITICAL] clawdefender - unauthorized_tool_use

**Rule:** TOOL_ABUSE_SYSTEM_MODIFICATION
**Location:** None

Pattern detected: /etc/passwd

### 8. [CRITICAL] clawdefender - unauthorized_tool_use

**Rule:** TOOL_ABUSE_SYSTEM_MODIFICATION
**Location:** None

Pattern detected: /etc/shadow

### 9. [HIGH] clawdefender - unauthorized_tool_use

**Rule:** YARA_system_manipulation
**Location:** None

Detects system manipulation, privilege escalation, and destructive file operations: rm -rf

### 10. [HIGH] clawdefender - unauthorized_tool_use

**Rule:** YARA_system_manipulation
**Location:** None

Detects system manipulation, privilege escalation, and destructive file operations: rm -rf

---

## Known False Positives

The following skills were flagged by the scanner but have been manually reviewed and determined to be false positives.

| Skill | Findings | Reason |
|-------|----------|--------|
| [clawdefender](clawdefender-openclaw-security-prompt-injection%2C-rogue-skills-etc-scan.md) | 37 | Security defense tool whose detection signatures (prompt injection patterns, dangerous command strings, ANSI codes) trigger the same rules they are designed to detect. All 37 findings are pattern arrays and documentation examples, not malicious code. |

---

## Clean Skills (No Findings)

- agent-md-refactor
- algorithmic-art
- analytics-tracking
- artifacts-builder
- audit-website
- brainstorming
- brand-guidelines
- brand-guidelines
- building-native-ui
- clawdex
- copy-editing
- copywriting
- create-auth-skill
- expo-cicd-workflows
- expo-deployment
- expo-dev-client
- expo-tailwind-setup
- find-skills
- frontend-design
- frontend-design
- health-tracker
- internal-comms
- internal-comms
- logseq
- marketing-ideas
- mcp-builder
- mcp-builder
- native-data-fetching
- page-cro
- pdf
- pdf
- pptx
- pptx
- pricing-strategy
- programmatic-seo
- react-native-best-practices
- remotion-best-practices
- skill-creator
- skill-creator
- slack-gif-creator
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
- use-dom
- vercel-composition-patterns
- vercel-react-best-practices
- vercel-react-native-skills
- vue-best-practices
- web-artifacts-builder
- web-artifacts-builder
- xlsx
- xlsx
- youtube-api
- youtube-music-cast
- youtube-search
- youtube-voice-summarizer

---

## Methodology

- **Scanner:** cisco-ai-skill-scanner
- **Analyzers:** behavioral_analyzer, llm_analyzer, meta_analyzer, static_analyzer, trigger_analyzer
- **Scan Date:** 2026-02-02T08:38:39.473313

### Limitations

- VirusTotal binary scanning not used (requires API key)
- No runtime verification - static and semantic analysis only
