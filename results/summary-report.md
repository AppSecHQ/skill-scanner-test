# AI Agent Skills Security Scan Report

**Generated:** 2026-02-07T14:20:40.984939
**Scanner:** cisco-ai-skill-scanner
**Analyzers:** behavioral, llm, meta, static, trigger

---

## Executive Summary

| Metric | Count |
|--------|-------|
| Total Skills Scanned | 624 |
| Safe Skills | 475 (76%) |
| Skills with Issues | 149 (24%) |
| Scan Errors | 0 |

### Severity Breakdown

| Severity | Count |
|----------|-------|
| CRITICAL | 263 |
| HIGH | 261 |
| MEDIUM | 696 |
| LOW | 229 |
| **Total Findings** | **1449** |

### Findings by Category

| Category | Count |
|----------|-------|
| data_exfiltration | 427 |
| command_injection | 240 |
| policy_violation | 182 |
| transitive_trust_abuse | 157 |
| social_engineering | 121 |
| unauthorized_tool_use | 118 |
| tool_chaining_abuse | 56 |
| resource_abuse | 46 |
| hardcoded_secrets | 42 |
| prompt_injection | 37 |
| skill_discovery_abuse | 17 |
| autonomy_abuse | 3 |
| obfuscation | 3 |

---

## Results by Skill

| # | Skill | Source | Safe | Findings | Max Severity |
|---|-------|--------|------|----------|--------------|
| 1 | [hugging-face-evaluation](skills-hugging-face-evaluation-scan.md) | huggingface | **No** | 113 | **CRITICAL** |
| 2 | [hugging-face-datasets](skills-hugging-face-datasets-scan.md) | huggingface | **No** | 77 | **CRITICAL** |
| 3 | [zoho-email](zoho-email-integration-scan.md) | clawhub.ai | **No** | 69 | **CRITICAL** |
| 4 | [hugging-face-paper-publisher](skills-hugging-face-paper-publisher-scan.md) | huggingface | **No** | 65 | **CRITICAL** |
| 5 | [finance-news](finance-news-briefings-scan.md) | clawhub.ai | **No** | 33 | **HIGH** |
| 6 | [qa-test-planner](qa-test-planner-scan.md) | skills.sh | **No** | 19 | **CRITICAL** |
| 7 | [skill-scanner](ai-skill-scanner-scan.md) | clawhub.ai | **No** | 19 | **CRITICAL** |
| 8 | [yara-rule-authoring](plugins-yara-authoring-skills-yara-rule-authoring-scan.md) | trailofbits | **No** | 19 | **CRITICAL** |
| 9 | [zotero](zotero-scan.md) | clawhub.ai | **No** | 19 | **CRITICAL** |
| 10 | [hugging-face-model-trainer](skills-hugging-face-model-trainer-scan.md) | huggingface | **No** | 16 | **HIGH** |
| 11 | [hugging-face-tool-builder](skills-hugging-face-tool-builder-scan.md) | huggingface | **No** | 13 | **CRITICAL** |
| 12 | [slack](slack-scan.md) | clawhub.ai | Yes | 13 | MEDIUM |
| 13 | [base-trader](base-trader-scan.md) | clawhub.ai | **No** | 12 | **CRITICAL** |
| 14 | [openclaw-optimizer](startclaw-optimizer-scan.md) | clawhub.ai | **No** | 12 | **HIGH** |
| 15 | [imap-smtp-email](imap-smtp-email-scan.md) | clawhub.ai | **No** | 11 | **HIGH** |
| 16 | [constant-time-testing](plugins-testing-handbook-skills-skills-constant-time-testing-scan.md) | trailofbits | **No** | 10 | **CRITICAL** |
| 17 | [swarmmarket](swarmmarket-skill%2C-make-money-with-your-agents-scan.md) | clawhub.ai | **No** | 10 | **CRITICAL** |
| 18 | [technews](techmeme-news-scan.md) | clawhub.ai | **No** | 10 | **HIGH** |
| 19 | [video-agent](video-agent-scan.md) | clawhub.ai | **No** | 10 | **HIGH** |
| 20 | [capability-evolver](capability-evolver-scan.md) | clawhub.ai | **No** | 9 | **CRITICAL** |
| 21 | [reddit](reddit-scraper-scan.md) | clawhub.ai | **No** | 9 | **HIGH** |
| 22 | [crypto-gold-monitor](%E5%8A%A0%E5%AF%86%E8%B4%A7%E5%B8%81%E4%B8%8E%E8%B4%B5%E9%87%91%E5%B1%9E%E7%9B%91%E6%8E%A7-scan.md) | clawhub.ai | **No** | 8 | **CRITICAL** |
| 23 | [preview-markdown](preview-markdown-scan.md) | clawhub.ai | **No** | 8 | **CRITICAL** |
| 24 | [querit-search](querit-search-scan.md) | clawhub.ai | **No** | 8 | **CRITICAL** |
| 25 | [update-plus](update-plus-scan.md) | clawhub.ai | **No** | 8 | **CRITICAL** |
| 26 | [ClawDoro](clawdoro-scan.md) | clawhub.ai | Yes | 7 | MEDIUM |
| 27 | [atheris](plugins-testing-handbook-skills-skills-atheris-scan.md) | trailofbits | **No** | 7 | **CRITICAL** |
| 28 | [auto-updater](auto-updater-skill-scan.md) | clawhub.ai | **No** | 7 | **CRITICAL** |
| 29 | [browse](browserbase-scan.md) | clawhub.ai | Yes | 7 | MEDIUM |
| 30 | [channel](wechat-oa-channel-scan.md) | clawhub.ai | **No** | 7 | **CRITICAL** |
| 31 | [foundry](foundry-scan.md) | clawhub.ai | **No** | 7 | **CRITICAL** |
| 32 | [hugging-face-jobs](skills-hugging-face-jobs-scan.md) | huggingface | **No** | 7 | **HIGH** |
| 33 | [test-specialist](test-specialist-scan.md) | clawhub.ai | **No** | 7 | **CRITICAL** |
| 34 | [tokenguard](tokenguard-scan.md) | clawhub.ai | **No** | 7 | **HIGH** |
| 35 | [ABM Outbound](abm-outbound-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 36 | [Better Polymarket](polymarket-better-scan.md) | clawhub.ai | **No** | 6 | **HIGH** |
| 37 | [agent-task-manager](agent-task-manager-scan.md) | clawhub.ai | Yes | 6 | MEDIUM |
| 38 | [browser-agent](browser-agent-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 39 | [bybit-trading](bybit-trading-agent-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 40 | [clawhub](clawhub-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 41 | [coding-agent](coding-agent-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 42 | [excel](excel-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 43 | [google](google-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 44 | [omni-stories](omni-stories-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 45 | [openwork](openwork-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 46 | [phone-agent](phone-voice-agent-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 47 | [stealth-browser](stealth-browser-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 48 | [tinyfish](tinyfish-web-agent-scan.md) | clawhub.ai | **No** | 6 | **HIGH** |
| 49 | [wallet-tracker](wallet-tracker-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 50 | [Agent Browser](browser-automation-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 51 | [ClawGateSecure](claw-gate-secure-scan.md) | clawhub.ai | Yes | 5 | MEDIUM |
| 52 | [azure-eventhub-java](github-skills-azure-eventhub-java-scan.md) | microsoft | **No** | 5 | **CRITICAL** |
| 53 | [azure-storage-blob-java](github-skills-azure-storage-blob-java-scan.md) | microsoft | Yes | 5 | LOW |
| 54 | [base-trading-agent](base-trading-agent-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 55 | [browser-use](browser-use-scan.md) | skills.sh | **No** | 5 | **HIGH** |
| 56 | [clawdhub](clawdhub-cli-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 57 | [clawflows](clawflows-scan.md) | clawhub.ai | **No** | 5 | **HIGH** |
| 58 | [compound-engineering](compound-interest-calculator-scan.md) | clawhub.ai | **No** | 5 | **HIGH** |
| 59 | [context-manager](smart-context-manager-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 60 | [cryptocurrency-trader](cryptocurrency-trader-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 61 | [ffuf-web-fuzzing](ffuf-skill-scan.md) | jthack | Yes | 5 | MEDIUM |
| 62 | [gitclaw](gitclaw-scan.md) | clawhub.ai | **No** | 5 | **HIGH** |
| 63 | [health-tracker](healthcheck-scan.md) | clawhub.ai | Yes | 5 | MEDIUM |
| 64 | [job-auto-apply](job-auto-apply-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 65 | [libafl](plugins-testing-handbook-skills-skills-libafl-scan.md) | trailofbits | **No** | 5 | **CRITICAL** |
| 66 | [linear-autopilot](linear-autopilot-scan.md) | clawhub.ai | **No** | 5 | **HIGH** |
| 67 | [linkedin](linkedin-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 68 | [mersal](mersal-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 69 | [moltbook](moltbook-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 70 | [nano-banana-pro](nano-banana-pro-image-generation-%26-editing-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 71 | [solana](solana-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 72 | [veo3-video-gen](veo-3-video-gen-gemini-api-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 73 | [voice-agent](voice-agent-scan.md) | clawhub.ai | **No** | 5 | **HIGH** |
| 74 | [x-api](x-api-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 75 | [MoltMedia](moltmedia-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 76 | [adguard](adguard-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 77 | [apewisdom](apewisdom-reddit-scanner-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 78 | [binance-pay](binance-pay-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 79 | [canvas-design](skills-canvas-design-scan.md) | anthropic | Yes | 4 | MEDIUM |
| 80 | [ci-gen](ci-cd-pipeline-generator-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 81 | [claude-chrome](claude-chrome-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 82 | [clawmail](clawmail-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 83 | [compound-engineering](compound-engineering-scan.md) | clawhub.ai | Yes | 4 | MEDIUM |
| 84 | [ctxly](mymemory.bot-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 85 | [discord-voice](discord-voice-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 86 | [ethereum-gas-tracker](ethereum-gas-tracker-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 87 | [firebase-apk-scanner](plugins-firebase-apk-scanner-skills-firebase-apk-scanner-scan.md) | trailofbits | **No** | 4 | **CRITICAL** |
| 88 | [firebase-apk-scanner](plugins-firebase-apkner-skills-firebase-apkner-scan.md) | trailofbits | **No** | 4 | **HIGH** |
| 89 | [google-workspace](google-workspace-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 90 | [hyperliquid](hyperliquid-cli-with-hip3-support-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 91 | [insider-wallets-finder](insider-wallets-finder-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 92 | [libfuzzer](plugins-testing-handbook-skills-skills-libfuzzer-scan.md) | trailofbits | **No** | 4 | **CRITICAL** |
| 93 | [lightning](lightning-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 94 | [nano-pdf](nano-pdf-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 95 | [notebooklm](notebooklm-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 96 | [phantom](phantom-wallet-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 97 | [security-auditor](security-auditor-scan.md) | clawhub.ai | Yes | 4 | MEDIUM |
| 98 | [send-email](send-email-scan.md) | clawhub.ai | Yes | 4 | MEDIUM |
| 99 | [session-handoff](session-handoff-scan.md) | skills.sh | **No** | 4 | **HIGH** |
| 100 | [simmer](simmer-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 101 | [smtp-send](smtp-send-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 102 | [supermemory](supermemory-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 103 | [tencent-map](%E8%85%BE%E8%AE%AF%E5%9C%B0%E5%9B%BEapi%E8%B0%83%E7%94%A8%E6%8A%80%E8%83%BD-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 104 | [youtube-summarize](youtube-video-summarizer-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 105 | [youtube-transcript](youtube-transcript-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 106 | [2captcha](2captcha-cli-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 107 | [Docker Pro Diagnostic](docker-diag-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 108 | [MockAPI - Instant REST API from JSON](mockapi-instant-rest-api-from-json-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 109 | [activecampaign](activecampaign-crm-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 110 | [activecampaign](baby-connect-logger-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 111 | [agentarcade](agent-arcade-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 112 | [agnxi-search](agent-skills-search-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 113 | [alby-bitcoin-payments-cli-skill](alby-bitcoin-payments-cli-skill-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 114 | [algorithmic-art](algorithmic-art-scan.md) | skills.sh | Yes | 3 | MEDIUM |
| 115 | [amap](amap-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 116 | [api-docs-gen](api-docs-generator-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 117 | [api-gateway](api-gateway-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 118 | [atxp](atxp-scan.md) | skills.sh | Yes | 3 | MEDIUM |
| 119 | [azure-mgmt-fabric-py](github-skills-azure-mgmt-fabric-py-scan.md) | microsoft | **No** | 3 | **HIGH** |
| 120 | [baidu-map](%E8%B0%83%E7%94%A8%E7%99%BE%E5%BA%A6%E5%9C%B0%E5%9B%BEapi%E5%8A%9F%E8%83%BD-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 121 | [botcoin-miner](botcoin-miner-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 122 | [clawlist](clawlist-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 123 | [clickup](clickup-skill-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 124 | [cloudflare](skills-cloudflare-scan.md) | cloudflare | Yes | 3 | MEDIUM |
| 125 | [codemod-gen](codemod-generator-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 126 | [crypto-wallet](crypto-wallet-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 127 | [defi](defi-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 128 | [diagram-gen](diagram-generator-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 129 | [diff-summary](git-diff-summarizer-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 130 | [durable-objects](skills-durable-objects-scan.md) | cloudflare | Yes | 3 | MEDIUM |
| 131 | [error-handler-gen](error-handler-generator-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 132 | [etf-assistant](etf%E6%8A%95%E8%B5%84%E5%8A%A9%E7%90%86-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 133 | [gcloud](google-cloud-platform-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 134 | [giphy-gif](giphy-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 135 | [github-action-gen](github-action-generator-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 136 | [home-assistant](home-assistant-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 137 | [lighthouse-fixer](lighthouse-score-fixer-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 138 | [mcps](mcps-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 139 | [obsidian-sync](obsidian-sync-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 140 | [openclaw-checkpoint](openclaw-checkpoint-personal-ai-assistant-backup-%26-recovery-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 141 | [playwright-skill](skills-playwright-skill-scan.md) | lackeyjb | Yes | 3 | MEDIUM |
| 142 | [save-money](save-money-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 143 | [searxng](searxng-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 144 | [skill-scanner](skill-scanner-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 145 | [skill-scanner](skillner-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 146 | [talent-de-cv](digital-identity%2C-cv-%26-resume-creator-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 147 | [testing-handbook-generator](plugins-testing-handbook-skills-skills-testing-handbook-generator-scan.md) | trailofbits | Yes | 3 | MEDIUM |
| 148 | [trmnl](trmnl-display-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 149 | [ui-ux-pro-max](ui-ux-pro-max-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 150 | [web-design-guidelines](web-design-guidelines-scan.md) | skills.sh | **No** | 3 | **HIGH** |
| 151 | [windows-control](windows-control-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 152 | [wrangler](skills-wrangler-scan.md) | cloudflare | **No** | 3 | **CRITICAL** |
| 153 | [1inch](1inch-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 154 | [Agent Wallet](agent-wallet-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 155 | [Job Search MCP](job-search-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 156 | [Search Realtime Information](realtime-web-search-scan.md) | clawhub.ai | Yes | 2 | LOW |
| 157 | [YT Meta - YouTube Metadata Extractor](yt-meta-youtube-metadata-extractor-scan.md) | clawhub.ai | Yes | 2 | LOW |
| 158 | [aegis-security](aegis-security-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 159 | [agent-money-tracker](intelligent-budget-tracker-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 160 | [ai-pdf-builder](ai-pdf-builder-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 161 | [aifs](aifs-http-file-system-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 162 | [antigravity-image-gen](antigravity-image-generator-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 163 | [apewisdom](apewisdom-redditner-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 164 | [aws-agentic-ai](plugins-aws-agentic-ai-skills-aws-agentic-ai-scan.md) | zxkane | Yes | 2 | MEDIUM |
| 165 | [aws-cdk-development](plugins-aws-cdk-skills-aws-cdk-development-scan.md) | zxkane | Yes | 2 | MEDIUM |
| 166 | [aws-infra](aws-infra-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 167 | [azure-ai-contentunderstanding-py](github-skills-azure-ai-contentunderstanding-py-scan.md) | microsoft | Yes | 2 | MEDIUM |
| 168 | [azure-ai-document-intelligence-dotnet](github-skills-azure-ai-document-intelligence-dotnet-scan.md) | microsoft | Yes | 2 | MEDIUM |
| 169 | [azure-ai-evaluation-py](github-skills-azure-ai-evaluation-py-scan.md) | microsoft | Yes | 2 | MEDIUM |
| 170 | [azure-monitor-opentelemetry-exporter-py](github-skills-azure-monitor-opentelemetry-exporter-py-scan.md) | microsoft | Yes | 2 | MEDIUM |
| 171 | [building-ai-agent-on-cloudflare](skills-building-ai-agent-on-cloudflare-scan.md) | cloudflare | **No** | 2 | **CRITICAL** |
| 172 | [building-mcp-server-on-cloudflare](skills-building-mcp-server-on-cloudflare-scan.md) | cloudflare | **No** | 2 | **CRITICAL** |
| 173 | [canvas-design](canvas-design-scan.md) | anthropic | Yes | 2 | MEDIUM |
| 174 | [cargo-fuzz](plugins-testing-handbook-skills-skills-cargo-fuzz-scan.md) | trailofbits | **No** | 2 | **CRITICAL** |
| 175 | [chart-image](chart-image-generator-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 176 | [clawbridge](clawbridge-find-your-connections-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 177 | [clawbrowser](clawbrowser-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 178 | [clawkey](clawkey-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 179 | [clawops](clawops-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 180 | [code-explain](code-explainer-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 181 | [codex](codex-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 182 | [cold-email](machfive-cold-email-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 183 | [core-vitals-fixer](core-web-vitals-optimizer-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 184 | [dependency-updater](dependency-updater-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 185 | [deps-analyzer](deps-checker-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 186 | [dev-browser](skills-dev-browser-scan.md) | sawyerhood | Yes | 2 | MEDIUM |
| 187 | [doc-coauthoring](skills-doc-coauthoring-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 188 | [dockerfile-gen](dockerfile-generator-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 189 | [earnings-calendar](earnings-calendar-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 190 | [email](email-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 191 | [explorer](github-projects-explorer-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 192 | [expo-cicd-workflows](expo-cicd-workflows-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 193 | [ez-google](ez-google-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 194 | [feishu-api-docs](feishu-api-docs-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 195 | [feishu-bridge](feishu-bridge-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 196 | [finance](finance-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 197 | [fuzzing-dictionary](plugins-testing-handbook-skills-skills-fuzzing-dictionary-scan.md) | trailofbits | **No** | 2 | **CRITICAL** |
| 198 | [gemini](gemini-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 199 | [gitclassic](gitclassic-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 200 | [githunt](githunt-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 201 | [gitlab-manager](gitlab-manager-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 202 | [gold_price_mcp](gold-price-mcp-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 203 | [google-calendar](google-calendar-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 204 | [habitica](habitica-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 205 | [humanize-ai-text](humanize-ai-text-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 206 | [humanizer](humanizer-scan.md) | skills.sh | Yes | 2 | LOW |
| 207 | [instagram](instagram-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 208 | [intodns](intodns-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 209 | [kimi-integration](kimi-integration-scan.md) | clawhub.ai | Yes | 2 | LOW |
| 210 | [landing-gen](landing-page-generator-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 211 | [launch-strategy](launch-strategy-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 212 | [llm](llm-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 213 | [local-pandoc](md-to-office-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 214 | [mailgun](mailgun-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 215 | [memory-hygiene](memory-hygiene-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 216 | [moltbot-ha](moltbot-home-assistant-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 217 | [multi-llm](multi-llm-fallback-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 218 | [n8n-api](n8n-api-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 219 | [near-email](near-email-skill-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 220 | [openocean](openocean-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 221 | [openpet](openpet-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 222 | [payment](payment-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 223 | [primer-x402](primer-x402-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 224 | [rei](rei-clawd-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 225 | [reposit](reposit-collective-intelligence-for-ai-agents-scan.md) | clawhub.ai | **No** | 2 | **CRITICAL** |
| 226 | [search-reddit](search-reddit-scan.md) | clawhub.ai | **No** | 2 | **CRITICAL** |
| 227 | [senior-architect](senior-architect-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 228 | [ship-learn-next](ship-learn-next-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 229 | [spec-to-code-compliance](plugins-spec-to-code-compliance-skills-spec-to-code-compliance-scan.md) | trailofbits | Yes | 2 | MEDIUM |
| 230 | [stock-evaluator-v3](stock-evaluator-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 231 | [subtitles](subtitles-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 232 | [system_monitor](system-monitor-scan.md) | clawhub.ai | Yes | 2 | LOW |
| 233 | [taskmaster](taskmaster-ai-cost-optimizer-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 234 | [trading-coach](trading-coach-scan.md) | clawhub.ai | Yes | 2 | LOW |
| 235 | [twitter-openclaw](x-twitter-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 236 | [ui-test](ui-test-scan.md) | clawhub.ai | **No** | 2 | **CRITICAL** |
| 237 | [upgrade-stripe](skills-upgrade-stripe-scan.md) | stripe | **No** | 2 | **CRITICAL** |
| 238 | [verification-before-completion](verification-before-completion-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 239 | [video-transcript](video-transcript-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 240 | [writing-skills](writing-skills-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 241 | [wycheproof](plugins-testing-handbook-skills-skills-wycheproof-scan.md) | trailofbits | **No** | 2 | **CRITICAL** |
| 242 | [x402](x402-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 243 | [youtube-playlist](youtube-playlist-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 244 | [10-of-my-most-popular-text-to-image-series-prompts-78b0897e](test-skill-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 245 | [Meta Tags - SEO Tag Generator](meta-tags-seo-tag-generator-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 246 | [aflpp](plugins-testing-handbook-skills-skills-aflpp-scan.md) | trailofbits | Yes | 1 | MEDIUM |
| 247 | [agents-sdk](skills-agents-sdk-scan.md) | cloudflare | Yes | 1 | LOW |
| 248 | [algorand-vulnerability-scanner](plugins-building-secure-contracts-skills-algorand-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 249 | [ansible](ansible-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 250 | [audit-prep-assistant](plugins-building-secure-contracts-skills-audit-prep-assistant-scan.md) | trailofbits | Yes | 1 | MEDIUM |
| 251 | [azure-ai-voicelive-dotnet](github-skills-azure-ai-voicelive-dotnet-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 252 | [azure-communication-callautomation-java](github-skills-azure-communication-callautomation-java-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 253 | [azure-communication-chat-java](github-skills-azure-communication-chat-java-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 254 | [azure-containerregistry-py](github-skills-azure-containerregistry-py-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 255 | [azure-mgmt-apicenter-py](github-skills-azure-mgmt-apicenter-py-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 256 | [azure-mgmt-apimanagement-dotnet](github-skills-azure-mgmt-apimanagement-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 257 | [azure-security-keyvault-keys-java](github-skills-azure-security-keyvault-keys-java-scan.md) | microsoft | Yes | 1 | LOW |
| 258 | [azure-security-keyvault-secrets-java](github-skills-azure-security-keyvault-secrets-java-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 259 | [bags](sagb-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 260 | [birthday-reminder](Birthday%20Reminder-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 261 | [cairo-vulnerability-scanner](plugins-building-secure-contracts-skills-cairo-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 262 | [calendar](calendar-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 263 | [captions](captions-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 264 | [chromadb-memory](chromadb-memory-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 265 | [clawdbot-security](clawdbot-security-audit-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 266 | [codeql](plugins-testing-handbook-skills-skills-codeql-scan.md) | trailofbits | Yes | 1 | LOW |
| 267 | [cosmos-vulnerability-scanner](plugins-building-secure-contracts-skills-cosmos-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 268 | [coverage-analysis](plugins-testing-handbook-skills-skills-coverage-analysis-scan.md) | trailofbits | Yes | 1 | LOW |
| 269 | [daily-ai-news](daily-ai-news-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 270 | [database](database-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 271 | [doc-coauthoring](doc-coauthoring-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 272 | [docx](docx-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 273 | [docx](skills-docx-scan.md) | anthropic | Yes | 1 | MEDIUM |
| 274 | [domain-name-brainstormer](domain-name-brainstormer-scan.md) | skills.sh | Yes | 1 | MEDIUM |
| 275 | [dwlf](a-clawdbot-skill-that-gives-your-agent-native-access-to-dwlf-%E2%80%94-a-market-analysis-platform-for-crypto-and-stocks.-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 276 | [eslint-gen](eslint-config-generator-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 277 | [frontend-ui-dark-ts](github-skills-frontend-ui-dark-ts-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 278 | [fuzzing-obstacles](plugins-testing-handbook-skills-skills-fuzzing-obstacles-scan.md) | trailofbits | Yes | 1 | LOW |
| 279 | [gaussian-process-mlp-hybrid](ai-%E7%BC%96%E7%A0%81-prompt-skill-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 280 | [glm-coding-agent](glm-coding-agent-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 281 | [harness-writing](plugins-testing-handbook-skills-skills-harness-writing-scan.md) | trailofbits | Yes | 1 | LOW |
| 282 | [hugging-face-cli](skills-hugging-face-cli-scan.md) | huggingface | Yes | 1 | LOW |
| 283 | [hugging-face-trackio](skills-hugging-face-trackio-scan.md) | huggingface | Yes | 1 | LOW |
| 284 | [json-canvas](skills-json-canvas-scan.md) | kepano | Yes | 1 | LOW |
| 285 | [kalshi](kalshi-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 286 | [m365-agents-py](github-skills-m365-agents-py-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 287 | [marketing-psychology](marketing-psychology-scan.md) | skills.sh | Yes | 1 | MEDIUM |
| 288 | [memory-system-v2](memory-system-v2-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 289 | [notion](notion-api-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 290 | [notion](notion-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 291 | [npkill](npkill-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 292 | [obsidian-bases](skills-obsidian-bases-scan.md) | kepano | Yes | 1 | LOW |
| 293 | [obsidian-markdown](skills-obsidian-markdown-scan.md) | kepano | Yes | 1 | LOW |
| 294 | [ossfuzz](plugins-testing-handbook-skills-skills-ossfuzz-scan.md) | trailofbits | Yes | 1 | LOW |
| 295 | [para-second-brain](para-second-brain-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 296 | [paypal](paypal-scan.md) | clawhub.ai | **No** | 1 | **HIGH** |
| 297 | [perf-auditor](performance-auditor-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 298 | [pipedrive](pipedrive-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 299 | [polymarket](polymarket-trading-skill-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 300 | [popup-cro](popup-cro-scan.md) | skills.sh | Yes | 1 | LOW |
| 301 | [qmd](qmd-external-knowledge-base-search-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 302 | [railway](railway-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 303 | [ralph-loop](ralph-loop-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 304 | [react-expert](react-expert-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 305 | [readwise-mcp](readwise-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 306 | [receiving-code-review](receiving-code-review-scan.md) | skills.sh | Yes | 1 | LOW |
| 307 | [redis](redis-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 308 | [referral-program](referral-program-scan.md) | skills.sh | Yes | 1 | LOW |
| 309 | [remotion-video-toolkit](remotion-video-toolkit-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 310 | [requesting-code-review](requesting-code-review-scan.md) | skills.sh | Yes | 1 | LOW |
| 311 | [research-paper-writer](research-paper-writer-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 312 | [resume-builder](resume-builder-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 313 | [rssaurus-cli](rssaurus-agent-friendly-rss-feed-reader-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 314 | [ruzzy](plugins-testing-handbook-skills-skills-ruzzy-scan.md) | trailofbits | Yes | 1 | LOW |
| 315 | [schema-markup](schema-markup-scan.md) | skills.sh | Yes | 1 | LOW |
| 316 | [semgrep](plugins-testing-handbook-skills-skills-semgrep-scan.md) | trailofbits | Yes | 1 | LOW |
| 317 | [sendclaw](sendclaw-email-without-human-permission-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 318 | [senior-devops](senior-devops-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 319 | [seo-audit](seo-audit-scan.md) | skills.sh | Yes | 1 | LOW |
| 320 | [shorten](url-shortener-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 321 | [signup-flow-cro](signup-flow-cro-scan.md) | skills.sh | Yes | 1 | LOW |
| 322 | [solana-vulnerability-scanner](plugins-building-secure-contracts-skills-solana-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 323 | [sora-2-nature-documentary](sora-2-%E8%87%AA%E7%84%B6%E7%BA%AA%E5%BD%95%E7%89%87-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 324 | [soulcraft](soulcraft-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 325 | [spring-boot-engineer](spring-boot-engineer-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 326 | [sql-assistant](sql-assistant-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 327 | [sql-pro](sql-pro-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 328 | [ssh-essentials](ssh-essentials-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 329 | [stealthy-auto-browse](stealthy-auto-browse-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 330 | [stock-market-pro](stock-market-pro-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 331 | [streme-launcher](streme-token-launcher-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 332 | [stripe-best-practices](skills-stripe-best-practices-scan.md) | stripe | Yes | 1 | LOW |
| 333 | [subagent-driven-development](subagent-driven-development-scan.md) | skills.sh | Yes | 1 | LOW |
| 334 | [substrate-vulnerability-scanner](plugins-building-secure-contracts-skills-substrate-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 335 | [swift-expert](swift-expert-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 336 | [tailwind-design-system](tailwind-design-system-scan.md) | skills.sh | Yes | 1 | LOW |
| 337 | [taskr](taskr-remote-task-tracking-for-ai-agents-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 338 | [telegram-auto-topic](telegram-auto-topic-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 339 | [telegram-pairing-customization](%E6%80%BB%E6%98%AF%E5%93%8D%E5%BA%94%E6%9C%AA%E9%85%8D%E5%AF%B9%E7%94%A8%E6%88%B7%E7%9A%84-start-%E6%B6%88%E6%81%AF-always-respond-to-start-messages-from-unpaired-users-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 340 | [template-skill](template-skill-scan.md) | skills.sh | Yes | 1 | LOW |
| 341 | [tg](telegram-cli-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 342 | [ton-vulnerability-scanner](plugins-building-secure-contracts-skills-ton-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 343 | [trade-signal](trade-singal-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 344 | [transcribe](transcribe-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 345 | [turborepo](turborepo-scan.md) | skills.sh | Yes | 1 | LOW |
| 346 | [twitter](twitter-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 347 | [undetectable-ai](undetectable-ai-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 348 | [using-git-worktrees](using-git-worktrees-scan.md) | skills.sh | Yes | 1 | LOW |
| 349 | [using-superpowers](using-superpowers-scan.md) | skills.sh | Yes | 1 | LOW |
| 350 | [variant-analysis](plugins-variant-analysis-skills-variant-analysis-scan.md) | trailofbits | Yes | 1 | LOW |
| 351 | [vestaboard](vestaboard-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 352 | [vue](vue-scan.md) | skills.sh | Yes | 1 | LOW |
| 353 | [watch-my-money](watch-my-money-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 354 | [web-perf](skills-web-perf-scan.md) | cloudflare | Yes | 1 | LOW |
| 355 | [webapp-testing](skills-webapp-testing-scan.md) | anthropic | Yes | 1 | MEDIUM |
| 356 | [webapp-testing](webapp-testing-scan.md) | anthropic | Yes | 1 | MEDIUM |
| 357 | [webhook-gen](webhook-generator-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 358 | [wordpress-pro](wordpress-pro-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 359 | [writing-clearly-and-concisely](writing-clearly-and-concisely-scan.md) | skills.sh | Yes | 1 | LOW |
| 360 | [writing-plans](writing-plans-scan.md) | skills.sh | Yes | 1 | LOW |
| 361 | [x-trends](x-twitter-trends-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 362 | [yahoo-finance](yahoo-finance-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 363 | [youtube-channels](youtube-channels-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 364 | [youtube-data](youtube-data-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 365 | [youtube-full](youtube-full-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 366 | [youtube-watcher](youtube-watcher-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 367 | [yt-video-downloader](youtube-video-downloader-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 368 | [Content ID Guide](content-id-guide-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 369 | [ab-test-setup](ab-test-setup-scan.md) | skills.sh | Yes | 0 | SAFE |
| 370 | [academic-deep-research](academic-deep-research-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 371 | [actual-budget](actual-budget-cli-to-interact-with-the-actual-budget-api-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 372 | [address-sanitizer](plugins-testing-handbook-skills-skills-address-sanitizer-scan.md) | trailofbits | Yes | 0 | SAFE |
| 373 | [agent-browser](agent-browser-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 374 | [agent-builder](agent-builder-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 375 | [agent-framework-azure-ai-py](github-skills-agent-framework-azure-ai-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 376 | [agent-md-refactor](agent-md-refactor-scan.md) | skills.sh | Yes | 0 | SAFE |
| 377 | [agenticflow-skills](agenticflow-skills-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 378 | [airc](airc-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 379 | [algorand-vulnerability-scanner](plugins-building-secure-contracts-skills-algorand-vulnerabilityner-scan.md) | trailofbits | Yes | 0 | SAFE |
| 380 | [algorithmic-art](skills-algorithmic-art-scan.md) | skills.sh | Yes | 0 | SAFE |
| 381 | [analytics-tracking](analytics-tracking-scan.md) | skills.sh | Yes | 0 | SAFE |
| 382 | [answeroverflow](answer-overflow-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 383 | [anterior-cingulate-memory](anterior-cingulate-memory-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 384 | [api-designer](api-designer-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 385 | [artifacts-builder](artifacts-builder-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 386 | [ask-questions-if-underspecified](plugins-ask-questions-if-underspecified-skills-ask-questions-if-underspecified-scan.md) | trailofbits | Yes | 0 | SAFE |
| 387 | [audit-context-building](plugins-audit-context-building-skills-audit-context-building-scan.md) | trailofbits | Yes | 0 | SAFE |
| 388 | [audit-website](audit-website-scan.md) | skills.sh | Yes | 0 | SAFE |
| 389 | [auto-animate](auto-animate-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 390 | [aws-cost-operations](plugins-aws-cost-ops-skills-aws-cost-operations-scan.md) | zxkane | Yes | 0 | SAFE |
| 391 | [aws-mcp-setup](plugins-aws-common-skills-aws-mcp-setup-scan.md) | zxkane | Yes | 0 | SAFE |
| 392 | [aws-serverless-eda](plugins-serverless-eda-skills-aws-serverless-eda-scan.md) | zxkane | Yes | 0 | SAFE |
| 393 | [azd-deployment](github-skills-azd-deployment-scan.md) | microsoft | Yes | 0 | SAFE |
| 394 | [azure-ai-agents-persistent-dotnet](github-skills-azure-ai-agents-persistent-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 395 | [azure-ai-agents-persistent-java](github-skills-azure-ai-agents-persistent-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 396 | [azure-ai-anomalydetector-java](github-skills-azure-ai-anomalydetector-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 397 | [azure-ai-contentsafety-java](github-skills-azure-ai-contentsafety-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 398 | [azure-ai-contentsafety-py](github-skills-azure-ai-contentsafety-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 399 | [azure-ai-formrecognizer-java](github-skills-azure-ai-formrecognizer-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 400 | [azure-ai-ml-py](github-skills-azure-ai-ml-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 401 | [azure-ai-openai-dotnet](github-skills-azure-ai-openai-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 402 | [azure-ai-projects-dotnet](github-skills-azure-ai-projects-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 403 | [azure-ai-projects-java](github-skills-azure-ai-projects-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 404 | [azure-ai-projects-py](github-skills-azure-ai-projects-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 405 | [azure-ai-textanalytics-py](github-skills-azure-ai-textanalytics-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 406 | [azure-ai-transcription-py](github-skills-azure-ai-transcription-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 407 | [azure-ai-translation-document-py](github-skills-azure-ai-translation-document-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 408 | [azure-ai-translation-text-py](github-skills-azure-ai-translation-text-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 409 | [azure-ai-vision-imageanalysis-java](github-skills-azure-ai-vision-imageanalysis-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 410 | [azure-ai-vision-imageanalysis-py](github-skills-azure-ai-vision-imageanalysis-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 411 | [azure-ai-voicelive-java](github-skills-azure-ai-voicelive-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 412 | [azure-ai-voicelive-py](github-skills-azure-ai-voicelive-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 413 | [azure-appconfiguration-java](github-skills-azure-appconfiguration-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 414 | [azure-appconfiguration-py](github-skills-azure-appconfiguration-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 415 | [azure-communication-callingserver-java](github-skills-azure-communication-callingserver-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 416 | [azure-communication-common-java](github-skills-azure-communication-common-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 417 | [azure-communication-sms-java](github-skills-azure-communication-sms-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 418 | [azure-compute-batch-java](github-skills-azure-compute-batch-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 419 | [azure-cosmos-db-py](github-skills-azure-cosmos-db-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 420 | [azure-cosmos-java](github-skills-azure-cosmos-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 421 | [azure-cosmos-py](github-skills-azure-cosmos-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 422 | [azure-data-tables-java](github-skills-azure-data-tables-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 423 | [azure-data-tables-py](github-skills-azure-data-tables-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 424 | [azure-eventgrid-dotnet](github-skills-azure-eventgrid-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 425 | [azure-eventgrid-java](github-skills-azure-eventgrid-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 426 | [azure-eventgrid-py](github-skills-azure-eventgrid-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 427 | [azure-eventhub-dotnet](github-skills-azure-eventhub-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 428 | [azure-eventhub-py](github-skills-azure-eventhub-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 429 | [azure-identity-dotnet](github-skills-azure-identity-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 430 | [azure-identity-java](github-skills-azure-identity-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 431 | [azure-identity-py](github-skills-azure-identity-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 432 | [azure-keyvault-py](github-skills-azure-keyvault-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 433 | [azure-maps-search-dotnet](github-skills-azure-maps-search-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 434 | [azure-messaging-webpubsub-java](github-skills-azure-messaging-webpubsub-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 435 | [azure-messaging-webpubsubservice-py](github-skills-azure-messaging-webpubsubservice-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 436 | [azure-mgmt-apicenter-dotnet](github-skills-azure-mgmt-apicenter-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 437 | [azure-mgmt-apimanagement-py](github-skills-azure-mgmt-apimanagement-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 438 | [azure-mgmt-applicationinsights-dotnet](github-skills-azure-mgmt-applicationinsights-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 439 | [azure-mgmt-arizeaiobservabilityeval-dotnet](github-skills-azure-mgmt-arizeaiobservabilityeval-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 440 | [azure-mgmt-botservice-dotnet](github-skills-azure-mgmt-botservice-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 441 | [azure-mgmt-botservice-py](github-skills-azure-mgmt-botservice-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 442 | [azure-mgmt-fabric-dotnet](github-skills-azure-mgmt-fabric-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 443 | [azure-mgmt-mongodbatlas-dotnet](github-skills-azure-mgmt-mongodbatlas-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 444 | [azure-mgmt-weightsandbiases-dotnet](github-skills-azure-mgmt-weightsandbiases-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 445 | [azure-microsoft-playwright-testing-ts](github-skills-azure-microsoft-playwright-testing-ts-scan.md) | microsoft | Yes | 0 | SAFE |
| 446 | [azure-monitor-ingestion-java](github-skills-azure-monitor-ingestion-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 447 | [azure-monitor-ingestion-py](github-skills-azure-monitor-ingestion-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 448 | [azure-monitor-opentelemetry-exporter-java](github-skills-azure-monitor-opentelemetry-exporter-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 449 | [azure-monitor-opentelemetry-py](github-skills-azure-monitor-opentelemetry-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 450 | [azure-monitor-query-java](github-skills-azure-monitor-query-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 451 | [azure-monitor-query-py](github-skills-azure-monitor-query-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 452 | [azure-postgres-ts](github-skills-azure-postgres-ts-scan.md) | microsoft | Yes | 0 | SAFE |
| 453 | [azure-resource-manager-cosmosdb-dotnet](github-skills-azure-resource-manager-cosmosdb-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 454 | [azure-resource-manager-durabletask-dotnet](github-skills-azure-resource-manager-durabletask-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 455 | [azure-resource-manager-mysql-dotnet](github-skills-azure-resource-manager-mysql-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 456 | [azure-resource-manager-playwright-dotnet](github-skills-azure-resource-manager-playwright-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 457 | [azure-resource-manager-postgresql-dotnet](github-skills-azure-resource-manager-postgresql-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 458 | [azure-resource-manager-redis-dotnet](github-skills-azure-resource-manager-redis-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 459 | [azure-resource-manager-sql-dotnet](github-skills-azure-resource-manager-sql-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 460 | [azure-search-documents-dotnet](github-skills-azure-search-documents-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 461 | [azure-search-documents-py](github-skills-azure-search-documents-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 462 | [azure-security-keyvault-keys-dotnet](github-skills-azure-security-keyvault-keys-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 463 | [azure-servicebus-dotnet](github-skills-azure-servicebus-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 464 | [azure-servicebus-py](github-skills-azure-servicebus-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 465 | [azure-speech-to-text-rest-py](github-skills-azure-speech-to-text-rest-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 466 | [azure-storage-blob-py](github-skills-azure-storage-blob-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 467 | [azure-storage-file-datalake-py](github-skills-azure-storage-file-datalake-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 468 | [azure-storage-file-share-py](github-skills-azure-storage-file-share-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 469 | [azure-storage-queue-py](github-skills-azure-storage-queue-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 470 | [basal-ganglia-memory](basal-ganglia-memory-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 471 | [bat-cat](bat-cat-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 472 | [brainstorming](brainstorming-scan.md) | skills.sh | Yes | 0 | SAFE |
| 473 | [brand-guidelines](brand-guidelines-scan.md) | skills.sh | Yes | 0 | SAFE |
| 474 | [brand-guidelines](skills-brand-guidelines-scan.md) | skills.sh | Yes | 0 | SAFE |
| 475 | [building-native-ui](building-native-ui-scan.md) | skills.sh | Yes | 0 | SAFE |
| 476 | [burpsuite-project-parser](plugins-burpsuite-project-parser-skills-scan.md) | trailofbits | Yes | 0 | SAFE |
| 477 | [cairo-vulnerability-scanner](plugins-building-secure-contracts-skills-cairo-vulnerabilityner-scan.md) | trailofbits | Yes | 0 | SAFE |
| 478 | [chirp](chirp-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 479 | [claude-in-chrome-troubleshooting](plugins-claude-in-chrome-troubleshooting-skills-claude-in-chrome-troubleshooting-scan.md) | trailofbits | Yes | 0 | SAFE |
| 480 | [clawdbot-cost-tracker](cost-tracking-for-models-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 481 | [clawdbot-self-security-audit](clawdbot-security-check-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 482 | [clawdefender](clawdefender-openclaw-security-prompt-injection%2C-rogue-skills-etc-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 483 | [clawdex](clawdex-by-koi-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 484 | [code-maturity-assessor](plugins-building-secure-contracts-skills-code-maturity-assessor-scan.md) | trailofbits | Yes | 0 | SAFE |
| 485 | [codeql](plugins-static-analysis-skills-codeql-scan.md) | trailofbits | Yes | 0 | SAFE |
| 486 | [coding-agent](multi-coding-agent-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 487 | [commit-work](commit-work-scan.md) | skills.sh | Yes | 0 | SAFE |
| 488 | [competitor-alternatives](competitor-alternatives-scan.md) | skills.sh | Yes | 0 | SAFE |
| 489 | [constant-time-analysis](plugins-constant-time-analysis-skills-constant-time-analysis-scan.md) | trailofbits | Yes | 0 | SAFE |
| 490 | [copy-editing](copy-editing-scan.md) | skills.sh | Yes | 0 | SAFE |
| 491 | [copywriting](copywriting-scan.md) | skills.sh | Yes | 0 | SAFE |
| 492 | [cosmos-vulnerability-scanner](plugins-building-secure-contracts-skills-cosmos-vulnerabilityner-scan.md) | trailofbits | Yes | 0 | SAFE |
| 493 | [create-auth-skill](better-auth-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 494 | [create-auth-skill](create-auth-skill-scan.md) | skills.sh | Yes | 0 | SAFE |
| 495 | [cron-mastery](cron-mastery-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 496 | [daily-meeting-update](daily-meeting-update-scan.md) | skills.sh | Yes | 0 | SAFE |
| 497 | [decision-trees](decision-trees-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 498 | [differential-review](plugins-differential-review-skills-differential-review-scan.md) | trailofbits | Yes | 0 | SAFE |
| 499 | [discord-chat](discord-chat-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 500 | [dispatching-parallel-agents](dispatching-parallel-agents-scan.md) | skills.sh | Yes | 0 | SAFE |
| 501 | [dont-hack-me](dont-hack-me-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 502 | [dotnet-expert](dotnet-expert-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 503 | [dwarf-expert](plugins-dwarf-expert-skills-dwarf-expert-scan.md) | trailofbits | Yes | 0 | SAFE |
| 504 | [email-best-practices](email-best-practices-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 505 | [email-sequence](email-sequence-scan.md) | skills.sh | Yes | 0 | SAFE |
| 506 | [entry-point-analyzer](plugins-entry-point-analyzer-skills-entry-point-analyzer-scan.md) | trailofbits | Yes | 0 | SAFE |
| 507 | [error-guard](error-guard-%E2%80%94-control%E2%80%91plane-safety-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 508 | [exa-web-search-free](exa-web-search-free-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 509 | [executing-plans](executing-plans-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 510 | [expo-api-routes](expo-api-routes-scan.md) | skills.sh | Yes | 0 | SAFE |
| 511 | [expo-deployment](expo-deployment-scan.md) | skills.sh | Yes | 0 | SAFE |
| 512 | [expo-dev-client](expo-dev-client-scan.md) | skills.sh | Yes | 0 | SAFE |
| 513 | [expo-tailwind-setup](expo-tailwind-setup-scan.md) | skills.sh | Yes | 0 | SAFE |
| 514 | [ez-cronjob](ez-cronjob-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 515 | [fastapi-router-py](github-skills-fastapi-router-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 516 | [faster-whisper](faster-whisper-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 517 | [feast](feast-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 518 | [find-skills](find-skills-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 519 | [finishing-a-development-branch](finishing-a-development-branch-scan.md) | skills.sh | Yes | 0 | SAFE |
| 520 | [fix-review](plugins-fix-review-skills-fix-review-scan.md) | trailofbits | Yes | 0 | SAFE |
| 521 | [form-cro](form-cro-scan.md) | skills.sh | Yes | 0 | SAFE |
| 522 | [foundry-iq-py](github-skills-foundry-iq-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 523 | [free-tool-strategy](free-tool-strategy-scan.md) | skills.sh | Yes | 0 | SAFE |
| 524 | [frontend-design](frontend-design-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 525 | [frontend-design](skills-frontend-design-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 526 | [gemini-nano-banana-pro-portraits](gemini-nano-banana-pro-portraits-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 527 | [github-issue-creator](github-skills-github-issue-creator-scan.md) | microsoft | Yes | 0 | SAFE |
| 528 | [gitlab-cli-skills](gitlab-cli-skills-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 529 | [google-gemini-media](google-gemini-media-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 530 | [google-imagen-3-hyperrealistic-landscape](google-imagen-3-%E8%B6%85%E5%86%99%E5%AE%9E%E9%A3%8E%E6%99%AF-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 531 | [guidelines-advisor](plugins-building-secure-contracts-skills-guidelines-advisor-scan.md) | trailofbits | Yes | 0 | SAFE |
| 532 | [hackernews](hacker-news-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 533 | [hf-mcp](hf-mcp-skills-hf-mcp-scan.md) | huggingface | Yes | 0 | SAFE |
| 534 | [hosted-agents-v2-py](github-skills-hosted-agents-v2-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 535 | [humanize](humanize-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 536 | [humanize-ai](humanize-ai-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 537 | [hybrid-memory](hybrid-memory-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 538 | [insecure-defaults](plugins-insecure-defaults-skills-insecure-defaults-scan.md) | trailofbits | Yes | 0 | SAFE |
| 539 | [insula-memory](insula-memory-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 540 | [internal-comms](internal-comms-scan.md) | skills.sh | Yes | 0 | SAFE |
| 541 | [internal-comms](skills-internal-comms-scan.md) | skills.sh | Yes | 0 | SAFE |
| 542 | [interpreting-culture-index](plugins-culture-index-skills-interpreting-culture-index-scan.md) | trailofbits | Yes | 0 | SAFE |
| 543 | [juicebox-v5](juicy-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 544 | [language-learning](language-learning-tutor-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 545 | [lobster](lobster-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 546 | [local-falcon](local-falcon-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 547 | [logseq](logseq-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 548 | [m365-agents-dotnet](github-skills-m365-agents-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 549 | [marketing-ideas](marketing-ideas-scan.md) | skills.sh | Yes | 0 | SAFE |
| 550 | [mcp-builder](github-skills-mcp-builder-scan.md) | microsoft | Yes | 0 | SAFE |
| 551 | [mcp-builder](mcp-builder-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 552 | [mcp-builder](skills-mcp-builder-scan.md) | anthropic | Yes | 0 | SAFE |
| 553 | [memory-setup](memory-setup-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 554 | [mermaid-diagrams](mermaid-diagrams-scan.md) | skills.sh | Yes | 0 | SAFE |
| 555 | [microsoft-azure-webjobs-extensions-authentication-events-dotnet](github-skills-microsoft-azure-webjobs-extensions-authentication-events-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 556 | [modern-python](plugins-modern-python-skills-modern-python-scan.md) | trailofbits | Yes | 0 | SAFE |
| 557 | [molt-identity](molt-identity-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 558 | [moltbot-best-practices](moltbot-best-practices-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 559 | [native-data-fetching](native-data-fetching-scan.md) | skills.sh | Yes | 0 | SAFE |
| 560 | [next-best-practices](next-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 561 | [nextjs-expert](nextjs-expert-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 562 | [nuxt](nuxt-scan.md) | skills.sh | Yes | 0 | SAFE |
| 563 | [obsidian-tasks](obsidian-tasks-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 564 | [onboarding-cro](onboarding-cro-scan.md) | skills.sh | Yes | 0 | SAFE |
| 565 | [openclaw](comprehensive-skill-for-installing%2C-configuring%2C-and-managing-the-openclaw-ecosystem-gateway%2C-channels%2C-models%2C-automation%2C-nodes%2C-and-deployment-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 566 | [opencode-controller](opencode-controller-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 567 | [page-cro](page-cro-scan.md) | skills.sh | Yes | 0 | SAFE |
| 568 | [paid-ads](paid-ads-scan.md) | skills.sh | Yes | 0 | SAFE |
| 569 | [paywall-upgrade-cro](paywall-upgrade-cro-scan.md) | skills.sh | Yes | 0 | SAFE |
| 570 | [pdd](pdd-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 571 | [pdf](pdf-scan.md) | anthropic | Yes | 0 | SAFE |
| 572 | [pdf](skills-pdf-scan.md) | anthropic | Yes | 0 | SAFE |
| 573 | [podcast-generation](github-skills-podcast-generation-scan.md) | microsoft | Yes | 0 | SAFE |
| 574 | [pptx](pptx-scan.md) | anthropic | Yes | 0 | SAFE |
| 575 | [pptx](skills-pptx-scan.md) | anthropic | Yes | 0 | SAFE |
| 576 | [pricing-strategy](pricing-strategy-scan.md) | skills.sh | Yes | 0 | SAFE |
| 577 | [programmatic-seo](programmatic-seo-scan.md) | skills.sh | Yes | 0 | SAFE |
| 578 | [property-based-testing](plugins-property-based-testing-skills-property-based-testing-scan.md) | trailofbits | Yes | 0 | SAFE |
| 579 | [pydantic-models-py](github-skills-pydantic-models-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 580 | [react-email](react-email-skills-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 581 | [react-flow-node-ts](github-skills-react-flow-node-ts-scan.md) | microsoft | Yes | 0 | SAFE |
| 582 | [react-native-best-practices](react-native-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 583 | [remotion-best-practices](remotion-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 584 | [sarif-parsing](plugins-static-analysis-skills-sarif-parsing-scan.md) | trailofbits | Yes | 0 | SAFE |
| 585 | [secure-workflow-guide](plugins-building-secure-contracts-skills-secure-workflow-guide-scan.md) | trailofbits | Yes | 0 | SAFE |
| 586 | [semgrep](plugins-static-analysis-skills-semgrep-scan.md) | trailofbits | Yes | 0 | SAFE |
| 587 | [semgrep-rule-creator](plugins-semgrep-rule-creator-skills-semgrep-rule-creator-scan.md) | trailofbits | Yes | 0 | SAFE |
| 588 | [semgrep-rule-variant-creator](plugins-semgrep-rule-variant-creator-skills-semgrep-rule-variant-creator-scan.md) | trailofbits | Yes | 0 | SAFE |
| 589 | [sharp-edges](plugins-sharp-edges-skills-sharp-edges-scan.md) | trailofbits | Yes | 0 | SAFE |
| 590 | [skill-creator](github-skills-skill-creator-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 591 | [skill-creator](jash-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 592 | [skill-creator](skill-creator-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 593 | [skill-creator](skills-skill-creator-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 594 | [skill-scanner](ai-skillner-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 595 | [slack-gif-creator](skills-slack-gif-creator-scan.md) | skills.sh | Yes | 0 | SAFE |
| 596 | [slack-gif-creator](slack-gif-creator-scan.md) | skills.sh | Yes | 0 | SAFE |
| 597 | [social-content](social-content-scan.md) | skills.sh | Yes | 0 | SAFE |
| 598 | [solana-vulnerability-scanner](plugins-building-secure-contracts-skills-solana-vulnerabilityner-scan.md) | trailofbits | Yes | 0 | SAFE |
| 599 | [substrate-vulnerability-scanner](plugins-building-secure-contracts-skills-substrate-vulnerabilityner-scan.md) | trailofbits | Yes | 0 | SAFE |
| 600 | [supabase-postgres-best-practices](supabase-postgres-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 601 | [systematic-debugging](systematic-debugging-scan.md) | skills.sh | Yes | 0 | SAFE |
| 602 | [template-skill](template-scan.md) | skills.sh | Yes | 0 | SAFE |
| 603 | [test-driven-development](test-driven-development-scan.md) | skills.sh | Yes | 0 | SAFE |
| 604 | [theme-factory](skills-theme-factory-scan.md) | anthropic | Yes | 0 | SAFE |
| 605 | [theme-factory](theme-factory-scan.md) | anthropic | Yes | 0 | SAFE |
| 606 | [token-integration-analyzer](plugins-building-secure-contracts-skills-token-integration-analyzer-scan.md) | trailofbits | Yes | 0 | SAFE |
| 607 | [ton-vulnerability-scanner](plugins-building-secure-contracts-skills-ton-vulnerabilityner-scan.md) | trailofbits | Yes | 0 | SAFE |
| 608 | [upgrading-expo](upgrading-expo-scan.md) | skills.sh | Yes | 0 | SAFE |
| 609 | [use-dom](use-dom-scan.md) | skills.sh | Yes | 0 | SAFE |
| 610 | [vercel-composition-patterns](vercel-composition-patterns-scan.md) | skills.sh | Yes | 0 | SAFE |
| 611 | [vercel-react-best-practices](vercel-react-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 612 | [vercel-react-native-skills](vercel-react-native-skills-scan.md) | skills.sh | Yes | 0 | SAFE |
| 613 | [vue-best-practices](vue-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 614 | [web-artifacts-builder](skills-web-artifacts-builder-scan.md) | skills.sh | Yes | 0 | SAFE |
| 615 | [web-artifacts-builder](web-artifacts-builder-scan.md) | skills.sh | Yes | 0 | SAFE |
| 616 | [whisper](whisper-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 617 | [x-trends](x-trends-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 618 | [xlsx](skills-xlsx-scan.md) | anthropic | Yes | 0 | SAFE |
| 619 | [xlsx](xlsx-scan.md) | anthropic | Yes | 0 | SAFE |
| 620 | [youtube-api](youtube-api-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 621 | [youtube-music-cast](youtube-music-cast-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 622 | [youtube-search](youtube-search-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 623 | [youtube-voice-summarizer](youtube-podcast-summarizer-via-elevenlabs-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 624 | [zustand-store-ts](github-skills-zustand-store-ts-scan.md) | microsoft | Yes | 0 | SAFE |

---

## Top Risks (Critical/High Severity)

### 1. [CRITICAL] azure-eventhub-java - command_injection

**Rule:** YARA_sql_injection
**Location:** None

Detects SQL injection attack patterns including keywords, tautologies, and database functions: sleep(

### 2. [HIGH] azure-mgmt-fabric-py - unauthorized_tool_use

**Rule:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** None

The skill provides full Azure Fabric capacity management capabilities including create, update, suspend, and delete operations without any safety guardrails, confirmation prompts, or cost warnings. Creating or scaling Azure Fabric capacities can incur significant costs (F2, F4 SKUs are expensive). The skill could be triggered to create costly resources without explicit user awareness.

### 3. [CRITICAL] 2captcha - command_injection

**Rule:** LLM_COMMAND_INJECTION
**Location:** None

The installation instructions direct users to download and execute a bash script from GitHub without any integrity verification (no checksum, signature, or hash validation). The script is immediately made executable and placed in a system directory (/usr/local/bin/). An attacker who compromises the GitHub repository or performs a man-in-the-middle attack could inject malicious code that would be executed with the user's privileges. This represents arbitrary code execution with no security controls.

### 4. [HIGH] 2captcha - data_exfiltration

**Rule:** LLM_DATA_EXFILTRATION
**Location:** None

The skill instructs users to store their 2Captcha API key in plaintext in ~/.config/2captcha/api-key without any encryption or access controls. API keys are sensitive credentials that provide access to paid services and should be protected. Storing them in plaintext makes them vulnerable to theft by malware, other users on shared systems, or accidental exposure through backups/logs. The skill also suggests using environment variables, but the primary instruction is plaintext file storage.

### 5. [HIGH] 2captcha - social_engineering

**Rule:** LLM_SOCIAL_ENGINEERING
**Location:** None

The skill's stated purpose is to 'bypass captchas during web automation, account creation, or form submission.' CAPTCHAs exist as security controls to prevent automated abuse, bot attacks, spam, and fraudulent account creation. This skill explicitly facilitates circumventing these security measures. While there may be legitimate accessibility or testing use cases, the skill provides no ethical guidelines, warnings about terms of service violations, or restrictions on use. The workflow section specifically describes browser automation to inject CAPTCHA tokens, which is commonly used for malicious purposes including credential stuffing, spam, scraping protected content, and mass account creation for fraud.

### 6. [CRITICAL] ABM Outbound - data_exfiltration

**Rule:** LLM_DATA_EXFILTRATION
**Location:** None

The skill requires users to export sensitive API keys (APIFY_API_KEY, APOLLO_API_KEY, SCRIBELESS_API_KEY) as environment variables. This creates multiple security risks: (1) API keys stored in shell history files, (2) Keys accessible to all processes running under the user account, (3) No secure credential management, (4) Keys may be logged or exposed in process listings. The skill provides no guidance on secure credential storage or rotation.

### 7. [CRITICAL] ABM Outbound - data_exfiltration

**Rule:** LLM_DATA_EXFILTRATION
**Location:** None

The skill orchestrates a comprehensive personal data collection pipeline that scrapes LinkedIn profiles, enriches with contact information (emails, phone numbers), obtains physical mailing addresses via skip tracing, and transmits all data to multiple third-party services (Apify, Apollo, Scribeless). This creates severe privacy and data protection risks: (1) Bulk collection of personal identifiable information (PII) without explicit consent, (2) Cross-service data sharing with multiple vendors, (3) Physical address lookup via skip tracing services, (4) No data retention or deletion policies, (5) Potential violations of GDPR, CCPA, and other privacy regulations, (6) No user consent mechanisms for data subjects.

### 8. [HIGH] ABM Outbound - social_engineering

**Rule:** LLM_SOCIAL_ENGINEERING
**Location:** None

The skill description presents the tool as a 'secret weapon for standing out in crowded inboxes' without disclosing the significant privacy, legal, and ethical risks involved in mass personal data collection, skip tracing, and unsolicited multi-channel outreach. The description fails to mention: (1) Potential violations of privacy laws (GDPR, CCPA), (2) Anti-spam regulations (CAN-SPAM, CASL), (3) Telephone Consumer Protection Act (TCPA) compliance for phone outreach, (4) Ethical concerns with skip tracing and physical mail to home addresses, (5) LinkedIn Terms of Service violations for scraping. This constitutes social engineering by omission, misleading users about the true nature and risks of the tool.

### 9. [HIGH] ABM Outbound - unauthorized_tool_use

**Rule:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** None

The skill integrates with multiple third-party services (Apify, Apollo, Scribeless, Instantly) and transmits user data to these services without adequate disclosure of: (1) Data sharing agreements, (2) Third-party data retention policies, (3) Vendor security practices, (4) Data processor agreements required under GDPR, (5) Liability for third-party data breaches. Users are instructed to sign up for these services and provide API keys without understanding the full data sharing implications.

### 10. [CRITICAL] activecampaign - data_exfiltration

**Rule:** LLM_DATA_EXFILTRATION
**Location:** None

The skill instructs users to store API credentials in plaintext files (~/.config/activecampaign/url and ~/.config/activecampaign/api_key) without encryption or secure storage mechanisms. This creates a critical data exposure risk where credentials could be accessed by malicious processes, other users, or inadvertently committed to version control.

---

## Known False Positives

The following skills were flagged by the scanner but have been manually reviewed and determined to be false positives.

| Skill | Findings | Reason |
|-------|----------|--------|
| [clawdefender](clawdefender-openclaw-security-prompt-injection%2C-rogue-skills-etc-scan.md) | 0 | Security defense tool whose detection signatures (prompt injection patterns, dangerous command strings, ANSI codes) trigger the same rules they are designed to detect. All 37 findings are pattern arrays and documentation examples, not malicious code. |

---

## Clean Skills (No Findings)

- Content ID Guide
- ab-test-setup
- academic-deep-research
- actual-budget
- address-sanitizer
- agent-browser
- agent-builder
- agent-framework-azure-ai-py
- agent-md-refactor
- agenticflow-skills
- airc
- algorand-vulnerability-scanner
- algorithmic-art
- analytics-tracking
- answeroverflow
- anterior-cingulate-memory
- api-designer
- artifacts-builder
- ask-questions-if-underspecified
- audit-context-building
- audit-website
- auto-animate
- aws-cost-operations
- aws-mcp-setup
- aws-serverless-eda
- azd-deployment
- azure-ai-agents-persistent-dotnet
- azure-ai-agents-persistent-java
- azure-ai-anomalydetector-java
- azure-ai-contentsafety-java
- azure-ai-contentsafety-py
- azure-ai-formrecognizer-java
- azure-ai-ml-py
- azure-ai-openai-dotnet
- azure-ai-projects-dotnet
- azure-ai-projects-java
- azure-ai-projects-py
- azure-ai-textanalytics-py
- azure-ai-transcription-py
- azure-ai-translation-document-py
- azure-ai-translation-text-py
- azure-ai-vision-imageanalysis-java
- azure-ai-vision-imageanalysis-py
- azure-ai-voicelive-java
- azure-ai-voicelive-py
- azure-appconfiguration-java
- azure-appconfiguration-py
- azure-communication-callingserver-java
- azure-communication-common-java
- azure-communication-sms-java
- azure-compute-batch-java
- azure-cosmos-db-py
- azure-cosmos-java
- azure-cosmos-py
- azure-data-tables-java
- azure-data-tables-py
- azure-eventgrid-dotnet
- azure-eventgrid-java
- azure-eventgrid-py
- azure-eventhub-dotnet
- azure-eventhub-py
- azure-identity-dotnet
- azure-identity-java
- azure-identity-py
- azure-keyvault-py
- azure-maps-search-dotnet
- azure-messaging-webpubsub-java
- azure-messaging-webpubsubservice-py
- azure-mgmt-apicenter-dotnet
- azure-mgmt-apimanagement-py
- azure-mgmt-applicationinsights-dotnet
- azure-mgmt-arizeaiobservabilityeval-dotnet
- azure-mgmt-botservice-dotnet
- azure-mgmt-botservice-py
- azure-mgmt-fabric-dotnet
- azure-mgmt-mongodbatlas-dotnet
- azure-mgmt-weightsandbiases-dotnet
- azure-microsoft-playwright-testing-ts
- azure-monitor-ingestion-java
- azure-monitor-ingestion-py
- azure-monitor-opentelemetry-exporter-java
- azure-monitor-opentelemetry-py
- azure-monitor-query-java
- azure-monitor-query-py
- azure-postgres-ts
- azure-resource-manager-cosmosdb-dotnet
- azure-resource-manager-durabletask-dotnet
- azure-resource-manager-mysql-dotnet
- azure-resource-manager-playwright-dotnet
- azure-resource-manager-postgresql-dotnet
- azure-resource-manager-redis-dotnet
- azure-resource-manager-sql-dotnet
- azure-search-documents-dotnet
- azure-search-documents-py
- azure-security-keyvault-keys-dotnet
- azure-servicebus-dotnet
- azure-servicebus-py
- azure-speech-to-text-rest-py
- azure-storage-blob-py
- azure-storage-file-datalake-py
- azure-storage-file-share-py
- azure-storage-queue-py
- basal-ganglia-memory
- bat-cat
- brainstorming
- brand-guidelines
- brand-guidelines
- building-native-ui
- burpsuite-project-parser
- cairo-vulnerability-scanner
- chirp
- claude-in-chrome-troubleshooting
- clawdbot-cost-tracker
- clawdbot-self-security-audit
- clawdefender
- clawdex
- code-maturity-assessor
- codeql
- coding-agent
- commit-work
- competitor-alternatives
- constant-time-analysis
- copy-editing
- copywriting
- cosmos-vulnerability-scanner
- create-auth-skill
- create-auth-skill
- cron-mastery
- daily-meeting-update
- decision-trees
- differential-review
- discord-chat
- dispatching-parallel-agents
- dont-hack-me
- dotnet-expert
- dwarf-expert
- email-best-practices
- email-sequence
- entry-point-analyzer
- error-guard
- exa-web-search-free
- executing-plans
- expo-api-routes
- expo-deployment
- expo-dev-client
- expo-tailwind-setup
- ez-cronjob
- fastapi-router-py
- faster-whisper
- feast
- find-skills
- finishing-a-development-branch
- fix-review
- form-cro
- foundry-iq-py
- free-tool-strategy
- frontend-design
- frontend-design
- gemini-nano-banana-pro-portraits
- github-issue-creator
- gitlab-cli-skills
- google-gemini-media
- google-imagen-3-hyperrealistic-landscape
- guidelines-advisor
- hackernews
- hf-mcp
- hosted-agents-v2-py
- humanize
- humanize-ai
- hybrid-memory
- insecure-defaults
- insula-memory
- internal-comms
- internal-comms
- interpreting-culture-index
- juicebox-v5
- language-learning
- lobster
- local-falcon
- logseq
- m365-agents-dotnet
- marketing-ideas
- mcp-builder
- mcp-builder
- mcp-builder
- memory-setup
- mermaid-diagrams
- microsoft-azure-webjobs-extensions-authentication-events-dotnet
- modern-python
- molt-identity
- moltbot-best-practices
- native-data-fetching
- next-best-practices
- nextjs-expert
- nuxt
- obsidian-tasks
- onboarding-cro
- openclaw
- opencode-controller
- page-cro
- paid-ads
- paywall-upgrade-cro
- pdd
- pdf
- pdf
- podcast-generation
- pptx
- pptx
- pricing-strategy
- programmatic-seo
- property-based-testing
- pydantic-models-py
- react-email
- react-flow-node-ts
- react-native-best-practices
- remotion-best-practices
- sarif-parsing
- secure-workflow-guide
- semgrep
- semgrep-rule-creator
- semgrep-rule-variant-creator
- sharp-edges
- skill-creator
- skill-creator
- skill-creator
- skill-creator
- skill-scanner
- slack-gif-creator
- slack-gif-creator
- social-content
- solana-vulnerability-scanner
- substrate-vulnerability-scanner
- supabase-postgres-best-practices
- systematic-debugging
- template-skill
- test-driven-development
- theme-factory
- theme-factory
- token-integration-analyzer
- ton-vulnerability-scanner
- upgrading-expo
- use-dom
- vercel-composition-patterns
- vercel-react-best-practices
- vercel-react-native-skills
- vue-best-practices
- web-artifacts-builder
- web-artifacts-builder
- whisper
- x-trends
- xlsx
- xlsx
- youtube-api
- youtube-music-cast
- youtube-search
- youtube-voice-summarizer
- zustand-store-ts

---

## Methodology

- **Scanner:** cisco-ai-skill-scanner
- **Analyzers:** behavioral_analyzer, llm_analyzer, meta_analyzer, static_analyzer, trigger_analyzer
- **Scan Date:** 2026-02-07T14:20:40.984939

### Limitations

- VirusTotal binary scanning not used (requires API key)
- No runtime verification - static and semantic analysis only
