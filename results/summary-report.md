# AI Agent Skills Security Scan Report

**Generated:** 2026-05-09T01:44:52.079973
**Scanner:** cisco-ai-skill-scanner
**Analyzers:** behavioral, bytecode, llm, meta, pipeline, static, trigger

---

## Executive Summary

| Metric | Count |
|--------|-------|
| Total Skills Scanned | 650 |
| Safe Skills | 508 (78%) |
| Skills with Issues | 142 (22%) |
| Scan Errors | 0 |

### Severity Breakdown

| Severity | Count |
|----------|-------|
| CRITICAL | 209 |
| HIGH | 251 |
| MEDIUM | 714 |
| LOW | 180 |
| **Total Findings** | **1381** |

### Findings by Category

| Category | Count |
|----------|-------|
| data_exfiltration | 423 |
| command_injection | 211 |
| social_engineering | 168 |
| transitive_trust_abuse | 151 |
| unauthorized_tool_use | 133 |
| policy_violation | 91 |
| resource_abuse | 88 |
| prompt_injection | 53 |
| tool_chaining_abuse | 30 |
| hardcoded_secrets | 23 |
| skill_discovery_abuse | 6 |
| obfuscation | 3 |
| autonomy_abuse | 1 |

---

## Results by Skill

| # | Skill | Source | Safe | Findings | Max Severity |
|---|-------|--------|------|----------|--------------|
| 1 | [hugging-face-evaluation](skills-hugging-face-evaluation-scan.md) | huggingface | Yes | 96 | MEDIUM |
| 2 | [hugging-face-datasets](skills-hugging-face-datasets-scan.md) | huggingface | **No** | 78 | **CRITICAL** |
| 3 | [hugging-face-paper-publisher](skills-hugging-face-paper-publisher-scan.md) | huggingface | Yes | 54 | MEDIUM |
| 4 | [zoho-email](zoho-email-integration-scan.md) | clawhub.ai | **No** | 53 | **CRITICAL** |
| 5 | [finance-news](finance-news-briefings-scan.md) | clawhub.ai | **No** | 33 | **HIGH** |
| 6 | [qa-test-planner](qa-test-planner-scan.md) | skills.sh | **No** | 22 | **CRITICAL** |
| 7 | [skill-scanner](ai-skill-scanner-scan.md) | clawhub.ai | **No** | 19 | **CRITICAL** |
| 8 | [yara-rule-authoring](plugins-yara-authoring-skills-yara-rule-authoring-scan.md) | trailofbits | **No** | 19 | **CRITICAL** |
| 9 | [update-plus](update-plus-scan.md) | clawhub.ai | **No** | 15 | **CRITICAL** |
| 10 | [hugging-face-model-trainer](skills-hugging-face-model-trainer-scan.md) | huggingface | Yes | 14 | MEDIUM |
| 11 | [meta-ads](skills-meta-ads-scan.md) | hoodini | **No** | 13 | **CRITICAL** |
| 12 | [base-trader](base-trader-scan.md) | clawhub.ai | **No** | 12 | **CRITICAL** |
| 13 | [constant-time-testing](plugins-testing-handbook-skills-skills-constant-time-testing-scan.md) | trailofbits | **No** | 12 | **CRITICAL** |
| 14 | [hugging-face-tool-builder](skills-hugging-face-tool-builder-scan.md) | huggingface | **No** | 12 | **CRITICAL** |
| 15 | [imap-smtp-email](imap-smtp-email-scan.md) | clawhub.ai | **No** | 11 | **HIGH** |
| 16 | [simmer](simmer-scan.md) | clawhub.ai | **No** | 10 | **CRITICAL** |
| 17 | [capability-evolver](capability-evolver-scan.md) | clawhub.ai | **No** | 9 | **CRITICAL** |
| 18 | [session-handoff](session-handoff-scan.md) | skills.sh | **No** | 9 | **HIGH** |
| 19 | [hugging-face-jobs](skills-hugging-face-jobs-scan.md) | huggingface | Yes | 8 | MEDIUM |
| 20 | [libafl](plugins-testing-handbook-skills-skills-libafl-scan.md) | trailofbits | **No** | 8 | **CRITICAL** |
| 21 | [ruzzy](plugins-testing-handbook-skills-skills-ruzzy-scan.md) | trailofbits | Yes | 8 | MEDIUM |
| 22 | [x402](x402-scan.md) | clawhub.ai | **No** | 8 | **CRITICAL** |
| 23 | [ClawDoro](clawdoro-scan.md) | clawhub.ai | Yes | 7 | MEDIUM |
| 24 | [auto-updater](auto-updater-skill-scan.md) | clawhub.ai | **No** | 7 | **CRITICAL** |
| 25 | [browse](browserbase-scan.md) | clawhub.ai | Yes | 7 | MEDIUM |
| 26 | [dev-browser](skills-dev-browser-scan.md) | sawyerhood | Yes | 7 | MEDIUM |
| 27 | [foundry](foundry-scan.md) | clawhub.ai | **No** | 7 | **CRITICAL** |
| 28 | [telegram-pairing-customization](%E6%80%BB%E6%98%AF%E5%93%8D%E5%BA%94%E6%9C%AA%E9%85%8D%E5%AF%B9%E7%94%A8%E6%88%B7%E7%9A%84-start-%E6%B6%88%E6%81%AF-always-respond-to-start-messages-from-unpaired-users-scan.md) | clawhub.ai | **No** | 7 | **CRITICAL** |
| 29 | [vestaboard](vestaboard-scan.md) | clawhub.ai | Yes | 7 | MEDIUM |
| 30 | [ABM Outbound](abm-outbound-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 31 | [agent-task-manager](agent-task-manager-scan.md) | clawhub.ai | Yes | 6 | MEDIUM |
| 32 | [browser-agent](browser-agent-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 33 | [bybit-trading](bybit-trading-agent-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 34 | [clawhub](clawhub-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 35 | [coding-agent](coding-agent-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 36 | [excel](excel-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 37 | [google](google-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 38 | [omni-stories](omni-stories-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 39 | [openwork](openwork-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 40 | [phone-agent](phone-voice-agent-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 41 | [taskr](taskr-remote-task-tracking-for-ai-agents-scan.md) | clawhub.ai | Yes | 6 | MEDIUM |
| 42 | [using-git-worktrees](using-git-worktrees-scan.md) | skills.sh | Yes | 6 | MEDIUM |
| 43 | [wallet-tracker](wallet-tracker-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 44 | [whisper](whisper-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 45 | [Agent Browser](browser-automation-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 46 | [ClawGateSecure](claw-gate-secure-scan.md) | clawhub.ai | Yes | 5 | MEDIUM |
| 47 | [azure-eventhub-java](github-skills-azure-eventhub-java-scan.md) | microsoft | **No** | 5 | **CRITICAL** |
| 48 | [azure-storage-blob-java](github-skills-azure-storage-blob-java-scan.md) | microsoft | Yes | 5 | LOW |
| 49 | [base-trading-agent](base-trading-agent-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 50 | [browser-use](browser-use-scan.md) | skills.sh | **No** | 5 | **HIGH** |
| 51 | [clawdhub](clawdhub-cli-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 52 | [clawflows](clawflows-scan.md) | clawhub.ai | **No** | 5 | **HIGH** |
| 53 | [compound-engineering](compound-interest-calculator-scan.md) | clawhub.ai | **No** | 5 | **HIGH** |
| 54 | [cryptocurrency-trader](cryptocurrency-trader-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 55 | [ffuf-web-fuzzing](ffuf-skill-scan.md) | jthack | Yes | 5 | MEDIUM |
| 56 | [gitclaw](gitclaw-scan.md) | clawhub.ai | **No** | 5 | **HIGH** |
| 57 | [health-tracker](healthcheck-scan.md) | clawhub.ai | Yes | 5 | MEDIUM |
| 58 | [hugging-face-cli](skills-hugging-face-cli-scan.md) | huggingface | Yes | 5 | LOW |
| 59 | [job-auto-apply](job-auto-apply-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 60 | [linear-autopilot](linear-autopilot-scan.md) | clawhub.ai | **No** | 5 | **HIGH** |
| 61 | [linkedin](linkedin-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 62 | [mersal](mersal-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 63 | [moltbook](moltbook-scan.md) | moltbook.com | **No** | 5 | **CRITICAL** |
| 64 | [nano-banana-pro](nano-banana-pro-image-generation-%26-editing-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 65 | [openclaw-optimizer](startclaw-optimizer-scan.md) | clawhub.ai | **No** | 5 | **HIGH** |
| 66 | [polymarket](polymarket-better-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 67 | [sendclaw](sendclaw-email-without-human-permission-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 68 | [solana](solana-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 69 | [stealthy-auto-browse](stealthy-auto-browse-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 70 | [subagent-driven-development](subagent-driven-development-scan.md) | skills.sh | Yes | 5 | MEDIUM |
| 71 | [taskmaster](taskmaster-ai-cost-optimizer-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 72 | [tokenguard](tokenguard-scan.md) | clawhub.ai | **No** | 5 | **HIGH** |
| 73 | [using-superpowers](using-superpowers-scan.md) | skills.sh | **No** | 5 | **HIGH** |
| 74 | [voice-agent](voice-agent-scan.md) | clawhub.ai | **No** | 5 | **HIGH** |
| 75 | [windows-control](windows-control-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 76 | [yahoo-finance](yahoo-finance-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 77 | [youtube-watcher](youtube-watcher-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 78 | [MoltMedia](moltmedia-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 79 | [adguard](adguard-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 80 | [apewisdom](apewisdom-reddit-scanner-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 81 | [bags](sagb-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 82 | [binance-pay](binance-pay-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 83 | [channel](wechat-oa-channel-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 84 | [ci-gen](ci-cd-pipeline-generator-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 85 | [claude-chrome](claude-chrome-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 86 | [clawmail](clawmail-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 87 | [compound-engineering](compound-engineering-scan.md) | clawhub.ai | Yes | 4 | MEDIUM |
| 88 | [ctxly](mymemory.bot-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 89 | [discord-voice](discord-voice-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 90 | [docx](skills-docx-scan.md) | anthropic | **No** | 4 | **HIGH** |
| 91 | [ethereum-gas-tracker](ethereum-gas-tracker-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 92 | [firebase-apk-scanner](plugins-firebase-apk-scanner-skills-firebase-apk-scanner-scan.md) | trailofbits | **No** | 4 | **CRITICAL** |
| 93 | [firebase-apk-scanner](plugins-firebase-apkner-skills-firebase-apkner-scan.md) | trailofbits | **No** | 4 | **HIGH** |
| 94 | [fuzzing-dictionary](plugins-testing-handbook-skills-skills-fuzzing-dictionary-scan.md) | trailofbits | **No** | 4 | **CRITICAL** |
| 95 | [google-workspace](google-workspace-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 96 | [hyperliquid](hyperliquid-cli-with-hip3-support-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 97 | [insider-wallets-finder](insider-wallets-finder-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 98 | [lightning](lightning-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 99 | [nano-pdf](nano-pdf-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 100 | [notebooklm](notebooklm-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 101 | [phantom](phantom-wallet-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 102 | [redis](redis-scan.md) | clawhub.ai | Yes | 4 | MEDIUM |
| 103 | [slack](slack-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 104 | [sora-2-nature-documentary](sora-2-%E8%87%AA%E7%84%B6%E7%BA%AA%E5%BD%95%E7%89%87-scan.md) | clawhub.ai | Yes | 4 | LOW |
| 105 | [stripe-best-practices](skills-stripe-best-practices-scan.md) | stripe | Yes | 4 | MEDIUM |
| 106 | [supermemory](supermemory-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 107 | [tencent-map](%E8%85%BE%E8%AE%AF%E5%9C%B0%E5%9B%BEapi%E8%B0%83%E7%94%A8%E6%8A%80%E8%83%BD-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 108 | [tinyfish](tinyfish-web-agent-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 109 | [x-trends](x-twitter-trends-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 110 | [youtube-summarize](youtube-video-summarizer-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 111 | [2captcha](2captcha-cli-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 112 | [Docker Pro Diagnostic](docker-diag-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 113 | [MockAPI - Instant REST API from JSON](mockapi-instant-rest-api-from-json-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 114 | [YT Meta - YouTube Metadata Extractor](yt-meta-youtube-metadata-extractor-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 115 | [activecampaign](activecampaign-crm-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 116 | [activecampaign](baby-connect-logger-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 117 | [agentarcade](agent-arcade-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 118 | [agnxi-search](agent-skills-search-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 119 | [alby-bitcoin-payments-cli-skill](alby-bitcoin-payments-cli-skill-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 120 | [algorithmic-art](algorithmic-art-scan.md) | anthropic | Yes | 3 | MEDIUM |
| 121 | [amap](amap-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 122 | [api-docs-gen](api-docs-generator-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 123 | [api-gateway](api-gateway-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 124 | [atxp](atxp-scan.md) | skills.sh | Yes | 3 | MEDIUM |
| 125 | [azure-mgmt-fabric-py](github-skills-azure-mgmt-fabric-py-scan.md) | microsoft | **No** | 3 | **HIGH** |
| 126 | [baidu-map](%E8%B0%83%E7%94%A8%E7%99%BE%E5%BA%A6%E5%9C%B0%E5%9B%BEapi%E5%8A%9F%E8%83%BD-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 127 | [botcoin-miner](botcoin-miner-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 128 | [clawlist](clawlist-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 129 | [clickup](clickup-skill-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 130 | [codemod-gen](codemod-generator-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 131 | [crypto-gold-monitor](%E5%8A%A0%E5%AF%86%E8%B4%A7%E5%B8%81%E4%B8%8E%E8%B4%B5%E9%87%91%E5%B1%9E%E7%9B%91%E6%8E%A7-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 132 | [crypto-wallet](crypto-wallet-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 133 | [defi](defi-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 134 | [diagram-gen](diagram-generator-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 135 | [diff-summary](git-diff-summarizer-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 136 | [error-handler-gen](error-handler-generator-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 137 | [etf-assistant](etf%E6%8A%95%E8%B5%84%E5%8A%A9%E7%90%86-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 138 | [gcloud](google-cloud-platform-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 139 | [giphy-gif](giphy-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 140 | [github-action-gen](github-action-generator-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 141 | [home-assistant](home-assistant-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 142 | [lighthouse-fixer](lighthouse-score-fixer-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 143 | [local-llm-router](skills-local-llm-router-scan.md) | hoodini | Yes | 3 | MEDIUM |
| 144 | [mcps](mcps-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 145 | [obsidian-sync](obsidian-sync-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 146 | [openclaw-checkpoint](openclaw-checkpoint-personal-ai-assistant-backup-%26-recovery-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 147 | [ossfuzz](plugins-testing-handbook-skills-skills-ossfuzz-scan.md) | trailofbits | Yes | 3 | LOW |
| 148 | [reposit](reposit-collective-intelligence-for-ai-agents-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 149 | [save-money](save-money-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 150 | [skill-scanner](skill-scanner-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 151 | [stealth-browser](stealth-browser-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 152 | [swarmmarket](swarmmarket-skill%2C-make-money-with-your-agents-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 153 | [talent-de-cv](digital-identity%2C-cv-%26-resume-creator-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 154 | [technews](techmeme-news-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 155 | [telegram-auto-topic](telegram-auto-topic-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 156 | [testing-handbook-generator](plugins-testing-handbook-skills-skills-testing-handbook-generator-scan.md) | trailofbits | Yes | 3 | MEDIUM |
| 157 | [trade-signal](trade-singal-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 158 | [trading-coach](trading-coach-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 159 | [undetectable-ai](undetectable-ai-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 160 | [web-design-guidelines](web-design-guidelines-scan.md) | skills.sh | **No** | 3 | **HIGH** |
| 161 | [youtube-voice-summarizer](youtube-podcast-summarizer-via-elevenlabs-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 162 | [1inch](1inch-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 163 | [Agent Wallet](agent-wallet-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 164 | [Job Search MCP](job-search-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 165 | [aegis-security](aegis-security-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 166 | [agent-money-tracker](intelligent-budget-tracker-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 167 | [ai-pdf-builder](ai-pdf-builder-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 168 | [aifs](aifs-http-file-system-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 169 | [antigravity-image-gen](antigravity-image-generator-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 170 | [apewisdom](apewisdom-redditner-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 171 | [aws-agentic-ai](plugins-aws-agentic-ai-skills-aws-agentic-ai-scan.md) | zxkane | Yes | 2 | MEDIUM |
| 172 | [aws-cdk-development](plugins-aws-cdk-skills-aws-cdk-development-scan.md) | zxkane | Yes | 2 | MEDIUM |
| 173 | [aws-infra](aws-infra-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 174 | [azure-ai-contentunderstanding-py](github-skills-azure-ai-contentunderstanding-py-scan.md) | microsoft | Yes | 2 | MEDIUM |
| 175 | [azure-ai-document-intelligence-dotnet](github-skills-azure-ai-document-intelligence-dotnet-scan.md) | microsoft | Yes | 2 | MEDIUM |
| 176 | [azure-ai-evaluation-py](github-skills-azure-ai-evaluation-py-scan.md) | microsoft | Yes | 2 | MEDIUM |
| 177 | [azure-monitor-opentelemetry-exporter-py](github-skills-azure-monitor-opentelemetry-exporter-py-scan.md) | microsoft | Yes | 2 | MEDIUM |
| 178 | [bun](skills-bun-scan.md) | hoodini | Yes | 2 | LOW |
| 179 | [canvas-design](canvas-design-scan.md) | anthropic | Yes | 2 | MEDIUM |
| 180 | [canvas-design](skills-canvas-design-scan.md) | anthropic | Yes | 2 | MEDIUM |
| 181 | [chart-image](chart-image-generator-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 182 | [clawbridge](clawbridge-find-your-connections-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 183 | [clawbrowser](clawbrowser-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 184 | [clawkey](clawkey-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 185 | [clawops](clawops-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 186 | [code-explain](code-explainer-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 187 | [codex](codex-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 188 | [cold-email](machfive-cold-email-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 189 | [context-manager](smart-context-manager-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 190 | [core-vitals-fixer](core-web-vitals-optimizer-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 191 | [dependency-updater](dependency-updater-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 192 | [deps-analyzer](deps-checker-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 193 | [doc-coauthoring](skills-doc-coauthoring-scan.md) | anthropic | Yes | 2 | MEDIUM |
| 194 | [dockerfile-gen](dockerfile-generator-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 195 | [earnings-calendar](earnings-calendar-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 196 | [email](email-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 197 | [explorer](github-projects-explorer-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 198 | [expo-cicd-workflows](expo-cicd-workflows-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 199 | [ez-google](ez-google-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 200 | [feishu-api-docs](feishu-api-docs-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 201 | [feishu-bridge](feishu-bridge-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 202 | [finance](finance-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 203 | [gemini](gemini-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 204 | [gitclassic](gitclassic-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 205 | [githunt](githunt-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 206 | [gitlab-manager](gitlab-manager-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 207 | [gold_price_mcp](gold-price-mcp-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 208 | [google-calendar](google-calendar-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 209 | [habitica](habitica-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 210 | [humanize-ai-text](humanize-ai-text-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 211 | [humanizer](humanizer-scan.md) | clawhub.ai | Yes | 2 | LOW |
| 212 | [instagram](instagram-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 213 | [intodns](intodns-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 214 | [kimi-integration](kimi-integration-scan.md) | clawhub.ai | Yes | 2 | LOW |
| 215 | [landing-gen](landing-page-generator-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 216 | [langchain](skills-langchain-scan.md) | hoodini | **No** | 2 | **HIGH** |
| 217 | [launch-strategy](launch-strategy-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 218 | [llm](llm-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 219 | [local-pandoc](md-to-office-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 220 | [mailgun](mailgun-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 221 | [memory-hygiene](memory-hygiene-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 222 | [moltbot-ha](moltbot-home-assistant-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 223 | [multi-llm](multi-llm-fallback-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 224 | [n8n-api](n8n-api-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 225 | [near-email](near-email-skill-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 226 | [openocean](openocean-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 227 | [openpet](openpet-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 228 | [payment](payment-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 229 | [primer-x402](primer-x402-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 230 | [querit-search](querit-search-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 231 | [ralph-loop](ralph-loop-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 232 | [react-email](react-email-skills-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 233 | [rei](rei-clawd-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 234 | [search-reddit](search-reddit-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 235 | [searxng](searxng-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 236 | [send-email](send-email-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 237 | [smtp-send](smtp-send-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 238 | [spec-to-code-compliance](plugins-spec-to-code-compliance-skills-spec-to-code-compliance-scan.md) | trailofbits | Yes | 2 | MEDIUM |
| 239 | [stock-evaluator-v3](stock-evaluator-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 240 | [subtitles](subtitles-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 241 | [tg](telegram-cli-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 242 | [twitter](twitter-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 243 | [twitter-openclaw](x-twitter-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 244 | [ui-test](ui-test-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 245 | [upgrade-stripe](skills-upgrade-stripe-scan.md) | stripe | **No** | 2 | **CRITICAL** |
| 246 | [use-dom](use-dom-scan.md) | skills.sh | Yes | 2 | LOW |
| 247 | [veo3-video-gen](veo-3-video-gen-gemini-api-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 248 | [video-transcript](video-transcript-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 249 | [webhook-gen](webhook-generator-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 250 | [writing-skills](writing-skills-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 251 | [x-api](x-api-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 252 | [youtube-playlist](youtube-playlist-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 253 | [Better Polymarket](polymarket-trading-skill-scan.md) | clawhub.ai | **No** | 1 | **HIGH** |
| 254 | [Meta Tags - SEO Tag Generator](meta-tags-seo-tag-generator-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 255 | [aflpp](plugins-testing-handbook-skills-skills-aflpp-scan.md) | trailofbits | Yes | 1 | MEDIUM |
| 256 | [algorand-vulnerability-scanner](plugins-building-secure-contracts-skills-algorand-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 257 | [analytics-metrics](skills-analytics-metrics-scan.md) | hoodini | Yes | 1 | INFO |
| 258 | [ansible](ansible-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 259 | [audit-prep-assistant](plugins-building-secure-contracts-skills-audit-prep-assistant-scan.md) | trailofbits | Yes | 1 | MEDIUM |
| 260 | [aws-account-management](skills-aws-account-management-scan.md) | hoodini | Yes | 1 | INFO |
| 261 | [aws-agentcore](skills-aws-agentcore-scan.md) | hoodini | Yes | 1 | INFO |
| 262 | [aws-strands](skills-aws-strands-scan.md) | hoodini | Yes | 1 | INFO |
| 263 | [azure-ai-voicelive-dotnet](github-skills-azure-ai-voicelive-dotnet-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 264 | [azure-communication-callautomation-java](github-skills-azure-communication-callautomation-java-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 265 | [azure-communication-chat-java](github-skills-azure-communication-chat-java-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 266 | [azure-containerregistry-py](github-skills-azure-containerregistry-py-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 267 | [azure-mgmt-apicenter-py](github-skills-azure-mgmt-apicenter-py-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 268 | [azure-mgmt-apimanagement-dotnet](github-skills-azure-mgmt-apimanagement-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 269 | [azure-security-keyvault-keys-java](github-skills-azure-security-keyvault-keys-java-scan.md) | microsoft | Yes | 1 | LOW |
| 270 | [azure-security-keyvault-secrets-java](github-skills-azure-security-keyvault-secrets-java-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 271 | [birthday-reminder](Birthday%20Reminder-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 272 | [cairo-vulnerability-scanner](plugins-building-secure-contracts-skills-cairo-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 273 | [calendar](calendar-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 274 | [captions](captions-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 275 | [chromadb-memory](chromadb-memory-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 276 | [clawdbot-security](clawdbot-security-audit-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 277 | [cloudflare](skills-cloudflare-scan.md) | hoodini | Yes | 1 | INFO |
| 278 | [codeql](plugins-testing-handbook-skills-skills-codeql-scan.md) | trailofbits | Yes | 1 | LOW |
| 279 | [copilot-docs](skills-copilot-docs-scan.md) | hoodini | Yes | 1 | INFO |
| 280 | [copilot-sdk](skills-copilot-sdk-scan.md) | hoodini | Yes | 1 | INFO |
| 281 | [cosmos-vulnerability-scanner](plugins-building-secure-contracts-skills-cosmos-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 282 | [daily-ai-news](daily-ai-news-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 283 | [database](database-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 284 | [doc-coauthoring](doc-coauthoring-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 285 | [docx](docx-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 286 | [domain-name-brainstormer](domain-name-brainstormer-scan.md) | skills.sh | Yes | 1 | MEDIUM |
| 287 | [dwlf](a-clawdbot-skill-that-gives-your-agent-native-access-to-dwlf-%E2%80%94-a-market-analysis-platform-for-crypto-and-stocks.-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 288 | [eslint-gen](eslint-config-generator-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 289 | [fal-ai](skills-fal-ai-scan.md) | hoodini | Yes | 1 | INFO |
| 290 | [figma](skills-figma-scan.md) | hoodini | Yes | 1 | INFO |
| 291 | [frontend-ui-dark-ts](github-skills-frontend-ui-dark-ts-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 292 | [gaussian-process-mlp-hybrid](ai-%E7%BC%96%E7%A0%81-prompt-skill-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 293 | [github-trending](skills-github-trending-scan.md) | hoodini | Yes | 1 | INFO |
| 294 | [glm-coding-agent](glm-coding-agent-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 295 | [google-workspace-cli](skills-google-workspace-cli-scan.md) | hoodini | Yes | 1 | INFO |
| 296 | [honest-agent](skills-honest-agent-scan.md) | hoodini | Yes | 1 | INFO |
| 297 | [kalshi](kalshi-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 298 | [m365-agents-py](github-skills-m365-agents-py-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 299 | [marketing-psychology](marketing-psychology-scan.md) | skills.sh | Yes | 1 | MEDIUM |
| 300 | [memory-system-v2](memory-system-v2-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 301 | [mermaid-diagrams](skills-mermaid-diagrams-scan.md) | hoodini | Yes | 1 | INFO |
| 302 | [mobile-responsiveness](skills-mobile-responsiveness-scan.md) | hoodini | Yes | 1 | INFO |
| 303 | [mongodb](skills-mongodb-scan.md) | hoodini | Yes | 1 | INFO |
| 304 | [nano-banana-pro](skills-nano-banana-pro-scan.md) | hoodini | Yes | 1 | INFO |
| 305 | [notion](notion-api-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 306 | [notion](notion-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 307 | [npkill](npkill-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 308 | [owasp-security](skills-owasp-security-scan.md) | hoodini | Yes | 1 | INFO |
| 309 | [para-second-brain](para-second-brain-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 310 | [paypal](paypal-scan.md) | clawhub.ai | **No** | 1 | **HIGH** |
| 311 | [perf-auditor](performance-auditor-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 312 | [pipedrive](pipedrive-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 313 | [playwright-skill](skills-playwright-skill-scan.md) | lackeyjb | Yes | 1 | MEDIUM |
| 314 | [popup-cro](popup-cro-scan.md) | skills.sh | Yes | 1 | MEDIUM |
| 315 | [qmd](qmd-external-knowledge-base-search-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 316 | [railway](skills-railway-scan.md) | hoodini | Yes | 1 | INFO |
| 317 | [reddit](reddit-scraper-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 318 | [seo-audit](seo-audit-scan.md) | skills.sh | Yes | 1 | LOW |
| 319 | [shabbat-times](skills-shabbat-times-scan.md) | hoodini | Yes | 1 | INFO |
| 320 | [shorten](url-shortener-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 321 | [skill-name](templates-skill-template-scan.md) | hoodini | Yes | 1 | INFO |
| 322 | [solana-vulnerability-scanner](plugins-building-secure-contracts-skills-solana-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 323 | [sql-assistant](sql-assistant-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 324 | [streme-launcher](streme-token-launcher-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 325 | [substrate-vulnerability-scanner](plugins-building-secure-contracts-skills-substrate-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 326 | [ton-vulnerability-scanner](plugins-building-secure-contracts-skills-ton-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 327 | [ux-design-systems](skills-ux-design-systems-scan.md) | hoodini | Yes | 1 | INFO |
| 328 | [variant-analysis](plugins-variant-analysis-skills-variant-analysis-scan.md) | trailofbits | Yes | 1 | LOW |
| 329 | [vercel](skills-vercel-scan.md) | hoodini | Yes | 1 | INFO |
| 330 | [video-agent](video-agent-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 331 | [watch-my-money](watch-my-money-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 332 | [web-accessibility](skills-web-accessibility-scan.md) | hoodini | Yes | 1 | INFO |
| 333 | [webapp-testing](webapp-testing-scan.md) | anthropic | Yes | 1 | MEDIUM |
| 334 | [writing-clearly-and-concisely](writing-clearly-and-concisely-scan.md) | skills.sh | Yes | 1 | LOW |
| 335 | [writing-plans](writing-plans-scan.md) | skills.sh | Yes | 1 | LOW |
| 336 | [youtube-channels](youtube-channels-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 337 | [youtube-data](youtube-data-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 338 | [youtube-full](youtube-full-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 339 | [youtube-transcript](youtube-transcript-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 340 | [10-of-my-most-popular-text-to-image-series-prompts-78b0897e](test-skill-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 341 | [Content ID Guide](content-id-guide-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 342 | [Search Realtime Information](realtime-web-search-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 343 | [ab-test-setup](ab-test-setup-scan.md) | skills.sh | Yes | 0 | SAFE |
| 344 | [academic-deep-research](academic-deep-research-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 345 | [actual-budget](actual-budget-cli-to-interact-with-the-actual-budget-api-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 346 | [address-sanitizer](plugins-testing-handbook-skills-skills-address-sanitizer-scan.md) | trailofbits | Yes | 0 | SAFE |
| 347 | [agent-browser](agent-browser-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 348 | [agent-builder](agent-builder-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 349 | [agent-framework-azure-ai-py](github-skills-agent-framework-azure-ai-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 350 | [agent-md-refactor](agent-md-refactor-scan.md) | skills.sh | Yes | 0 | SAFE |
| 351 | [agenticflow-skills](agenticflow-skills-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 352 | [agents-sdk](skills-agents-sdk-scan.md) | cloudflare | Yes | 0 | SAFE |
| 353 | [airc](airc-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 354 | [algorand-vulnerability-scanner](plugins-building-secure-contracts-skills-algorand-vulnerabilityner-scan.md) | trailofbits | Yes | 0 | SAFE |
| 355 | [algorithmic-art](skills-algorithmic-art-scan.md) | anthropic | Yes | 0 | SAFE |
| 356 | [analytics-tracking](analytics-tracking-scan.md) | skills.sh | Yes | 0 | SAFE |
| 357 | [answeroverflow](answer-overflow-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 358 | [anterior-cingulate-memory](anterior-cingulate-memory-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 359 | [api-designer](api-designer-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 360 | [artifacts-builder](artifacts-builder-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 361 | [ask-questions-if-underspecified](plugins-ask-questions-if-underspecified-skills-ask-questions-if-underspecified-scan.md) | trailofbits | Yes | 0 | SAFE |
| 362 | [atheris](plugins-testing-handbook-skills-skills-atheris-scan.md) | trailofbits | Yes | 0 | SAFE |
| 363 | [audit-context-building](plugins-audit-context-building-skills-audit-context-building-scan.md) | trailofbits | Yes | 0 | SAFE |
| 364 | [audit-website](audit-website-scan.md) | skills.sh | Yes | 0 | SAFE |
| 365 | [auto-animate](auto-animate-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 366 | [aws-cost-operations](plugins-aws-cost-ops-skills-aws-cost-operations-scan.md) | zxkane | Yes | 0 | SAFE |
| 367 | [aws-mcp-setup](plugins-aws-common-skills-aws-mcp-setup-scan.md) | zxkane | Yes | 0 | SAFE |
| 368 | [aws-serverless-eda](plugins-serverless-eda-skills-aws-serverless-eda-scan.md) | zxkane | Yes | 0 | SAFE |
| 369 | [azd-deployment](github-skills-azd-deployment-scan.md) | microsoft | Yes | 0 | SAFE |
| 370 | [azure-ai-agents-persistent-dotnet](github-skills-azure-ai-agents-persistent-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 371 | [azure-ai-agents-persistent-java](github-skills-azure-ai-agents-persistent-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 372 | [azure-ai-anomalydetector-java](github-skills-azure-ai-anomalydetector-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 373 | [azure-ai-contentsafety-java](github-skills-azure-ai-contentsafety-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 374 | [azure-ai-contentsafety-py](github-skills-azure-ai-contentsafety-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 375 | [azure-ai-formrecognizer-java](github-skills-azure-ai-formrecognizer-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 376 | [azure-ai-ml-py](github-skills-azure-ai-ml-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 377 | [azure-ai-openai-dotnet](github-skills-azure-ai-openai-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 378 | [azure-ai-projects-dotnet](github-skills-azure-ai-projects-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 379 | [azure-ai-projects-java](github-skills-azure-ai-projects-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 380 | [azure-ai-projects-py](github-skills-azure-ai-projects-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 381 | [azure-ai-textanalytics-py](github-skills-azure-ai-textanalytics-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 382 | [azure-ai-transcription-py](github-skills-azure-ai-transcription-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 383 | [azure-ai-translation-document-py](github-skills-azure-ai-translation-document-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 384 | [azure-ai-translation-text-py](github-skills-azure-ai-translation-text-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 385 | [azure-ai-vision-imageanalysis-java](github-skills-azure-ai-vision-imageanalysis-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 386 | [azure-ai-vision-imageanalysis-py](github-skills-azure-ai-vision-imageanalysis-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 387 | [azure-ai-voicelive-java](github-skills-azure-ai-voicelive-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 388 | [azure-ai-voicelive-py](github-skills-azure-ai-voicelive-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 389 | [azure-appconfiguration-java](github-skills-azure-appconfiguration-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 390 | [azure-appconfiguration-py](github-skills-azure-appconfiguration-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 391 | [azure-communication-callingserver-java](github-skills-azure-communication-callingserver-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 392 | [azure-communication-common-java](github-skills-azure-communication-common-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 393 | [azure-communication-sms-java](github-skills-azure-communication-sms-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 394 | [azure-compute-batch-java](github-skills-azure-compute-batch-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 395 | [azure-cosmos-db-py](github-skills-azure-cosmos-db-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 396 | [azure-cosmos-java](github-skills-azure-cosmos-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 397 | [azure-cosmos-py](github-skills-azure-cosmos-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 398 | [azure-data-tables-java](github-skills-azure-data-tables-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 399 | [azure-data-tables-py](github-skills-azure-data-tables-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 400 | [azure-eventgrid-dotnet](github-skills-azure-eventgrid-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 401 | [azure-eventgrid-java](github-skills-azure-eventgrid-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 402 | [azure-eventgrid-py](github-skills-azure-eventgrid-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 403 | [azure-eventhub-dotnet](github-skills-azure-eventhub-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 404 | [azure-eventhub-py](github-skills-azure-eventhub-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 405 | [azure-identity-dotnet](github-skills-azure-identity-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 406 | [azure-identity-java](github-skills-azure-identity-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 407 | [azure-identity-py](github-skills-azure-identity-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 408 | [azure-keyvault-py](github-skills-azure-keyvault-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 409 | [azure-maps-search-dotnet](github-skills-azure-maps-search-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 410 | [azure-messaging-webpubsub-java](github-skills-azure-messaging-webpubsub-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 411 | [azure-messaging-webpubsubservice-py](github-skills-azure-messaging-webpubsubservice-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 412 | [azure-mgmt-apicenter-dotnet](github-skills-azure-mgmt-apicenter-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 413 | [azure-mgmt-apimanagement-py](github-skills-azure-mgmt-apimanagement-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 414 | [azure-mgmt-applicationinsights-dotnet](github-skills-azure-mgmt-applicationinsights-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 415 | [azure-mgmt-arizeaiobservabilityeval-dotnet](github-skills-azure-mgmt-arizeaiobservabilityeval-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 416 | [azure-mgmt-botservice-dotnet](github-skills-azure-mgmt-botservice-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 417 | [azure-mgmt-botservice-py](github-skills-azure-mgmt-botservice-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 418 | [azure-mgmt-fabric-dotnet](github-skills-azure-mgmt-fabric-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 419 | [azure-mgmt-mongodbatlas-dotnet](github-skills-azure-mgmt-mongodbatlas-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 420 | [azure-mgmt-weightsandbiases-dotnet](github-skills-azure-mgmt-weightsandbiases-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 421 | [azure-microsoft-playwright-testing-ts](github-skills-azure-microsoft-playwright-testing-ts-scan.md) | microsoft | Yes | 0 | SAFE |
| 422 | [azure-monitor-ingestion-java](github-skills-azure-monitor-ingestion-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 423 | [azure-monitor-ingestion-py](github-skills-azure-monitor-ingestion-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 424 | [azure-monitor-opentelemetry-exporter-java](github-skills-azure-monitor-opentelemetry-exporter-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 425 | [azure-monitor-opentelemetry-py](github-skills-azure-monitor-opentelemetry-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 426 | [azure-monitor-query-java](github-skills-azure-monitor-query-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 427 | [azure-monitor-query-py](github-skills-azure-monitor-query-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 428 | [azure-postgres-ts](github-skills-azure-postgres-ts-scan.md) | microsoft | Yes | 0 | SAFE |
| 429 | [azure-resource-manager-cosmosdb-dotnet](github-skills-azure-resource-manager-cosmosdb-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 430 | [azure-resource-manager-durabletask-dotnet](github-skills-azure-resource-manager-durabletask-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 431 | [azure-resource-manager-mysql-dotnet](github-skills-azure-resource-manager-mysql-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 432 | [azure-resource-manager-playwright-dotnet](github-skills-azure-resource-manager-playwright-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 433 | [azure-resource-manager-postgresql-dotnet](github-skills-azure-resource-manager-postgresql-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 434 | [azure-resource-manager-redis-dotnet](github-skills-azure-resource-manager-redis-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 435 | [azure-resource-manager-sql-dotnet](github-skills-azure-resource-manager-sql-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 436 | [azure-search-documents-dotnet](github-skills-azure-search-documents-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 437 | [azure-search-documents-py](github-skills-azure-search-documents-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 438 | [azure-security-keyvault-keys-dotnet](github-skills-azure-security-keyvault-keys-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 439 | [azure-servicebus-dotnet](github-skills-azure-servicebus-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 440 | [azure-servicebus-py](github-skills-azure-servicebus-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 441 | [azure-speech-to-text-rest-py](github-skills-azure-speech-to-text-rest-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 442 | [azure-storage-blob-py](github-skills-azure-storage-blob-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 443 | [azure-storage-file-datalake-py](github-skills-azure-storage-file-datalake-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 444 | [azure-storage-file-share-py](github-skills-azure-storage-file-share-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 445 | [azure-storage-queue-py](github-skills-azure-storage-queue-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 446 | [basal-ganglia-memory](basal-ganglia-memory-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 447 | [bat-cat](bat-cat-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 448 | [brainstorming](brainstorming-scan.md) | skills.sh | Yes | 0 | SAFE |
| 449 | [brand-guidelines](brand-guidelines-scan.md) | anthropic | Yes | 0 | SAFE |
| 450 | [brand-guidelines](skills-brand-guidelines-scan.md) | anthropic | Yes | 0 | SAFE |
| 451 | [building-ai-agent-on-cloudflare](skills-building-ai-agent-on-cloudflare-scan.md) | cloudflare | Yes | 0 | SAFE |
| 452 | [building-mcp-server-on-cloudflare](skills-building-mcp-server-on-cloudflare-scan.md) | cloudflare | Yes | 0 | SAFE |
| 453 | [building-native-ui](building-native-ui-scan.md) | skills.sh | Yes | 0 | SAFE |
| 454 | [burpsuite-project-parser](plugins-burpsuite-project-parser-skills-scan.md) | trailofbits | Yes | 0 | SAFE |
| 455 | [cairo-vulnerability-scanner](plugins-building-secure-contracts-skills-cairo-vulnerabilityner-scan.md) | trailofbits | Yes | 0 | SAFE |
| 456 | [cargo-fuzz](plugins-testing-handbook-skills-skills-cargo-fuzz-scan.md) | trailofbits | Yes | 0 | SAFE |
| 457 | [chirp](chirp-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 458 | [claude-in-chrome-troubleshooting](plugins-claude-in-chrome-troubleshooting-skills-claude-in-chrome-troubleshooting-scan.md) | trailofbits | Yes | 0 | SAFE |
| 459 | [clawdbot-cost-tracker](cost-tracking-for-models-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 460 | [clawdbot-self-security-audit](clawdbot-security-check-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 461 | [clawdefender](clawdefender-openclaw-security-prompt-injection%2C-rogue-skills-etc-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 462 | [clawdex](clawdex-by-koi-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 463 | [code-maturity-assessor](plugins-building-secure-contracts-skills-code-maturity-assessor-scan.md) | trailofbits | Yes | 0 | SAFE |
| 464 | [codeql](plugins-static-analysis-skills-codeql-scan.md) | trailofbits | Yes | 0 | SAFE |
| 465 | [coding-agent](multi-coding-agent-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 466 | [commit-work](commit-work-scan.md) | skills.sh | Yes | 0 | SAFE |
| 467 | [competitor-alternatives](competitor-alternatives-scan.md) | skills.sh | Yes | 0 | SAFE |
| 468 | [constant-time-analysis](plugins-constant-time-analysis-skills-constant-time-analysis-scan.md) | trailofbits | Yes | 0 | SAFE |
| 469 | [copy-editing](copy-editing-scan.md) | skills.sh | Yes | 0 | SAFE |
| 470 | [copywriting](copywriting-scan.md) | skills.sh | Yes | 0 | SAFE |
| 471 | [cosmos-vulnerability-scanner](plugins-building-secure-contracts-skills-cosmos-vulnerabilityner-scan.md) | trailofbits | Yes | 0 | SAFE |
| 472 | [coverage-analysis](plugins-testing-handbook-skills-skills-coverage-analysis-scan.md) | trailofbits | Yes | 0 | SAFE |
| 473 | [create-auth-skill](better-auth-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 474 | [create-auth-skill](create-auth-skill-scan.md) | skills.sh | Yes | 0 | SAFE |
| 475 | [cron-mastery](cron-mastery-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 476 | [daily-meeting-update](daily-meeting-update-scan.md) | skills.sh | Yes | 0 | SAFE |
| 477 | [decision-trees](decision-trees-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 478 | [differential-review](plugins-differential-review-skills-differential-review-scan.md) | trailofbits | Yes | 0 | SAFE |
| 479 | [discord-chat](discord-chat-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 480 | [dispatching-parallel-agents](dispatching-parallel-agents-scan.md) | skills.sh | Yes | 0 | SAFE |
| 481 | [dont-hack-me](dont-hack-me-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 482 | [dotnet-expert](dotnet-expert-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 483 | [durable-objects](skills-durable-objects-scan.md) | cloudflare | Yes | 0 | SAFE |
| 484 | [dwarf-expert](plugins-dwarf-expert-skills-dwarf-expert-scan.md) | trailofbits | Yes | 0 | SAFE |
| 485 | [email-best-practices](email-best-practices-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 486 | [email-sequence](email-sequence-scan.md) | skills.sh | Yes | 0 | SAFE |
| 487 | [entry-point-analyzer](plugins-entry-point-analyzer-skills-entry-point-analyzer-scan.md) | trailofbits | Yes | 0 | SAFE |
| 488 | [error-guard](error-guard-%E2%80%94-control%E2%80%91plane-safety-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 489 | [exa-web-search-free](exa-web-search-free-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 490 | [executing-plans](executing-plans-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 491 | [expo-api-routes](expo-api-routes-scan.md) | skills.sh | Yes | 0 | SAFE |
| 492 | [expo-deployment](expo-deployment-scan.md) | skills.sh | Yes | 0 | SAFE |
| 493 | [expo-dev-client](expo-dev-client-scan.md) | skills.sh | Yes | 0 | SAFE |
| 494 | [expo-tailwind-setup](expo-tailwind-setup-scan.md) | skills.sh | Yes | 0 | SAFE |
| 495 | [ez-cronjob](ez-cronjob-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 496 | [fastapi-router-py](github-skills-fastapi-router-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 497 | [faster-whisper](faster-whisper-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 498 | [feast](feast-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 499 | [find-skills](find-skills-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 500 | [finishing-a-development-branch](finishing-a-development-branch-scan.md) | skills.sh | Yes | 0 | SAFE |
| 501 | [fix-review](plugins-fix-review-skills-fix-review-scan.md) | trailofbits | Yes | 0 | SAFE |
| 502 | [form-cro](form-cro-scan.md) | skills.sh | Yes | 0 | SAFE |
| 503 | [foundry-iq-py](github-skills-foundry-iq-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 504 | [free-tool-strategy](free-tool-strategy-scan.md) | skills.sh | Yes | 0 | SAFE |
| 505 | [frontend-design](frontend-design-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 506 | [frontend-design](skills-frontend-design-scan.md) | anthropic | Yes | 0 | SAFE |
| 507 | [fuzzing-obstacles](plugins-testing-handbook-skills-skills-fuzzing-obstacles-scan.md) | trailofbits | Yes | 0 | SAFE |
| 508 | [gemini-nano-banana-pro-portraits](gemini-nano-banana-pro-portraits-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 509 | [github-issue-creator](github-skills-github-issue-creator-scan.md) | microsoft | Yes | 0 | SAFE |
| 510 | [gitlab-cli-skills](gitlab-cli-skills-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 511 | [google-gemini-media](google-gemini-media-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 512 | [google-imagen-3-hyperrealistic-landscape](google-imagen-3-%E8%B6%85%E5%86%99%E5%AE%9E%E9%A3%8E%E6%99%AF-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 513 | [guidelines-advisor](plugins-building-secure-contracts-skills-guidelines-advisor-scan.md) | trailofbits | Yes | 0 | SAFE |
| 514 | [hackernews](hacker-news-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 515 | [harness-writing](plugins-testing-handbook-skills-skills-harness-writing-scan.md) | trailofbits | Yes | 0 | SAFE |
| 516 | [hf-mcp](hf-mcp-skills-hf-mcp-scan.md) | huggingface | Yes | 0 | SAFE |
| 517 | [hosted-agents-v2-py](github-skills-hosted-agents-v2-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 518 | [hugging-face-trackio](skills-hugging-face-trackio-scan.md) | huggingface | Yes | 0 | SAFE |
| 519 | [humanize](humanize-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 520 | [humanize-ai](humanize-ai-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 521 | [hybrid-memory](hybrid-memory-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 522 | [insecure-defaults](plugins-insecure-defaults-skills-insecure-defaults-scan.md) | trailofbits | Yes | 0 | SAFE |
| 523 | [insula-memory](insula-memory-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 524 | [internal-comms](internal-comms-scan.md) | anthropic | Yes | 0 | SAFE |
| 525 | [internal-comms](skills-internal-comms-scan.md) | anthropic | Yes | 0 | SAFE |
| 526 | [interpreting-culture-index](plugins-culture-index-skills-interpreting-culture-index-scan.md) | trailofbits | Yes | 0 | SAFE |
| 527 | [json-canvas](skills-json-canvas-scan.md) | kepano | Yes | 0 | SAFE |
| 528 | [juicebox-v5](juicy-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 529 | [language-learning](language-learning-tutor-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 530 | [libfuzzer](plugins-testing-handbook-skills-skills-libfuzzer-scan.md) | trailofbits | Yes | 0 | SAFE |
| 531 | [lobster](lobster-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 532 | [local-falcon](local-falcon-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 533 | [logseq](logseq-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 534 | [m365-agents-dotnet](github-skills-m365-agents-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 535 | [marketing-ideas](marketing-ideas-scan.md) | skills.sh | Yes | 0 | SAFE |
| 536 | [mcp-builder](github-skills-mcp-builder-scan.md) | microsoft | Yes | 0 | SAFE |
| 537 | [mcp-builder](mcp-builder-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 538 | [mcp-builder](skills-mcp-builder-scan.md) | anthropic | Yes | 0 | SAFE |
| 539 | [memory-setup](memory-setup-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 540 | [mermaid-diagrams](mermaid-diagrams-scan.md) | skills.sh | Yes | 0 | SAFE |
| 541 | [microsoft-azure-webjobs-extensions-authentication-events-dotnet](github-skills-microsoft-azure-webjobs-extensions-authentication-events-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 542 | [modern-python](plugins-modern-python-skills-modern-python-scan.md) | trailofbits | Yes | 0 | SAFE |
| 543 | [molt-identity](molt-identity-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 544 | [moltbot-best-practices](moltbot-best-practices-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 545 | [native-data-fetching](native-data-fetching-scan.md) | skills.sh | Yes | 0 | SAFE |
| 546 | [next-best-practices](next-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 547 | [nextjs-expert](nextjs-expert-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 548 | [nuxt](nuxt-scan.md) | skills.sh | Yes | 0 | SAFE |
| 549 | [obsidian-bases](skills-obsidian-bases-scan.md) | kepano | Yes | 0 | SAFE |
| 550 | [obsidian-markdown](skills-obsidian-markdown-scan.md) | kepano | Yes | 0 | SAFE |
| 551 | [obsidian-tasks](obsidian-tasks-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 552 | [onboarding-cro](onboarding-cro-scan.md) | skills.sh | Yes | 0 | SAFE |
| 553 | [openclaw](comprehensive-skill-for-installing%2C-configuring%2C-and-managing-the-openclaw-ecosystem-gateway%2C-channels%2C-models%2C-automation%2C-nodes%2C-and-deployment-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 554 | [opencode-controller](opencode-controller-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 555 | [page-cro](page-cro-scan.md) | skills.sh | Yes | 0 | SAFE |
| 556 | [paid-ads](paid-ads-scan.md) | skills.sh | Yes | 0 | SAFE |
| 557 | [paywall-upgrade-cro](paywall-upgrade-cro-scan.md) | skills.sh | Yes | 0 | SAFE |
| 558 | [pdd](pdd-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 559 | [pdf](pdf-scan.md) | anthropic | Yes | 0 | SAFE |
| 560 | [pdf](skills-pdf-scan.md) | anthropic | Yes | 0 | SAFE |
| 561 | [podcast-generation](github-skills-podcast-generation-scan.md) | microsoft | Yes | 0 | SAFE |
| 562 | [pptx](pptx-scan.md) | anthropic | Yes | 0 | SAFE |
| 563 | [pptx](skills-pptx-scan.md) | anthropic | Yes | 0 | SAFE |
| 564 | [preview-markdown](preview-markdown-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 565 | [pricing-strategy](pricing-strategy-scan.md) | skills.sh | Yes | 0 | SAFE |
| 566 | [programmatic-seo](programmatic-seo-scan.md) | skills.sh | Yes | 0 | SAFE |
| 567 | [property-based-testing](plugins-property-based-testing-skills-property-based-testing-scan.md) | trailofbits | Yes | 0 | SAFE |
| 568 | [pydantic-models-py](github-skills-pydantic-models-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 569 | [railway](railway-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 570 | [react-expert](react-expert-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 571 | [react-flow-node-ts](github-skills-react-flow-node-ts-scan.md) | microsoft | Yes | 0 | SAFE |
| 572 | [react-native-best-practices](react-native-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 573 | [readwise-mcp](readwise-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 574 | [receiving-code-review](receiving-code-review-scan.md) | skills.sh | Yes | 0 | SAFE |
| 575 | [referral-program](referral-program-scan.md) | skills.sh | Yes | 0 | SAFE |
| 576 | [remotion-best-practices](remotion-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 577 | [remotion-video-toolkit](remotion-video-toolkit-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 578 | [requesting-code-review](requesting-code-review-scan.md) | skills.sh | Yes | 0 | SAFE |
| 579 | [research-paper-writer](research-paper-writer-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 580 | [resume-builder](resume-builder-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 581 | [rssaurus-cli](rssaurus-agent-friendly-rss-feed-reader-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 582 | [sarif-parsing](plugins-static-analysis-skills-sarif-parsing-scan.md) | trailofbits | Yes | 0 | SAFE |
| 583 | [schema-markup](schema-markup-scan.md) | skills.sh | Yes | 0 | SAFE |
| 584 | [secure-workflow-guide](plugins-building-secure-contracts-skills-secure-workflow-guide-scan.md) | trailofbits | Yes | 0 | SAFE |
| 585 | [security-auditor](security-auditor-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 586 | [semgrep](plugins-static-analysis-skills-semgrep-scan.md) | trailofbits | Yes | 0 | SAFE |
| 587 | [semgrep](plugins-testing-handbook-skills-skills-semgrep-scan.md) | trailofbits | Yes | 0 | SAFE |
| 588 | [semgrep-rule-creator](plugins-semgrep-rule-creator-skills-semgrep-rule-creator-scan.md) | trailofbits | Yes | 0 | SAFE |
| 589 | [semgrep-rule-variant-creator](plugins-semgrep-rule-variant-creator-skills-semgrep-rule-variant-creator-scan.md) | trailofbits | Yes | 0 | SAFE |
| 590 | [senior-architect](senior-architect-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 591 | [senior-devops](senior-devops-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 592 | [sharp-edges](plugins-sharp-edges-skills-sharp-edges-scan.md) | trailofbits | Yes | 0 | SAFE |
| 593 | [ship-learn-next](ship-learn-next-scan.md) | skills.sh | Yes | 0 | SAFE |
| 594 | [signup-flow-cro](signup-flow-cro-scan.md) | skills.sh | Yes | 0 | SAFE |
| 595 | [skill-creator](github-skills-skill-creator-scan.md) | microsoft | Yes | 0 | SAFE |
| 596 | [skill-creator](jash-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 597 | [skill-creator](skill-creator-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 598 | [skill-creator](skills-skill-creator-scan.md) | anthropic | Yes | 0 | SAFE |
| 599 | [skill-scanner](ai-skillner-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 600 | [skill-scanner](skillner-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 601 | [slack-gif-creator](skills-slack-gif-creator-scan.md) | anthropic | Yes | 0 | SAFE |
| 602 | [slack-gif-creator](slack-gif-creator-scan.md) | anthropic | Yes | 0 | SAFE |
| 603 | [social-content](social-content-scan.md) | skills.sh | Yes | 0 | SAFE |
| 604 | [solana-vulnerability-scanner](plugins-building-secure-contracts-skills-solana-vulnerabilityner-scan.md) | trailofbits | Yes | 0 | SAFE |
| 605 | [soulcraft](soulcraft-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 606 | [spring-boot-engineer](spring-boot-engineer-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 607 | [sql-pro](sql-pro-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 608 | [ssh-essentials](ssh-essentials-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 609 | [stock-market-pro](stock-market-pro-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 610 | [substrate-vulnerability-scanner](plugins-building-secure-contracts-skills-substrate-vulnerabilityner-scan.md) | trailofbits | Yes | 0 | SAFE |
| 611 | [supabase-postgres-best-practices](supabase-postgres-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 612 | [swift-expert](swift-expert-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 613 | [system_monitor](system-monitor-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 614 | [systematic-debugging](systematic-debugging-scan.md) | skills.sh | Yes | 0 | SAFE |
| 615 | [tailwind-design-system](tailwind-design-system-scan.md) | skills.sh | Yes | 0 | SAFE |
| 616 | [template-skill](template-scan.md) | anthropic | Yes | 0 | SAFE |
| 617 | [template-skill](template-skill-scan.md) | anthropic | Yes | 0 | SAFE |
| 618 | [test-driven-development](test-driven-development-scan.md) | skills.sh | Yes | 0 | SAFE |
| 619 | [test-specialist](test-specialist-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 620 | [theme-factory](skills-theme-factory-scan.md) | anthropic | Yes | 0 | SAFE |
| 621 | [theme-factory](theme-factory-scan.md) | anthropic | Yes | 0 | SAFE |
| 622 | [token-integration-analyzer](plugins-building-secure-contracts-skills-token-integration-analyzer-scan.md) | trailofbits | Yes | 0 | SAFE |
| 623 | [ton-vulnerability-scanner](plugins-building-secure-contracts-skills-ton-vulnerabilityner-scan.md) | trailofbits | Yes | 0 | SAFE |
| 624 | [transcribe](transcribe-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 625 | [trmnl](trmnl-display-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 626 | [turborepo](turborepo-scan.md) | skills.sh | Yes | 0 | SAFE |
| 627 | [ui-ux-pro-max](ui-ux-pro-max-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 628 | [upgrading-expo](upgrading-expo-scan.md) | skills.sh | Yes | 0 | SAFE |
| 629 | [vercel-composition-patterns](vercel-composition-patterns-scan.md) | skills.sh | Yes | 0 | SAFE |
| 630 | [vercel-react-best-practices](vercel-react-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 631 | [vercel-react-native-skills](vercel-react-native-skills-scan.md) | skills.sh | Yes | 0 | SAFE |
| 632 | [verification-before-completion](verification-before-completion-scan.md) | skills.sh | Yes | 0 | SAFE |
| 633 | [vue](vue-scan.md) | skills.sh | Yes | 0 | SAFE |
| 634 | [vue-best-practices](vue-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 635 | [web-artifacts-builder](skills-web-artifacts-builder-scan.md) | anthropic | Yes | 0 | SAFE |
| 636 | [web-artifacts-builder](web-artifacts-builder-scan.md) | anthropic | Yes | 0 | SAFE |
| 637 | [web-perf](skills-web-perf-scan.md) | cloudflare | Yes | 0 | SAFE |
| 638 | [webapp-testing](skills-webapp-testing-scan.md) | anthropic | Yes | 0 | SAFE |
| 639 | [wordpress-pro](wordpress-pro-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 640 | [wrangler](skills-wrangler-scan.md) | cloudflare | Yes | 0 | SAFE |
| 641 | [wycheproof](plugins-testing-handbook-skills-skills-wycheproof-scan.md) | trailofbits | Yes | 0 | SAFE |
| 642 | [x-trends](x-trends-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 643 | [xlsx](skills-xlsx-scan.md) | anthropic | Yes | 0 | SAFE |
| 644 | [xlsx](xlsx-scan.md) | anthropic | Yes | 0 | SAFE |
| 645 | [youtube-api](youtube-api-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 646 | [youtube-music-cast](youtube-music-cast-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 647 | [youtube-search](youtube-search-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 648 | [yt-video-downloader](youtube-video-downloader-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 649 | [zotero](zotero-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 650 | [zustand-store-ts](github-skills-zustand-store-ts-scan.md) | microsoft | Yes | 0 | SAFE |

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

- 10-of-my-most-popular-text-to-image-series-prompts-78b0897e
- Content ID Guide
- Search Realtime Information
- ab-test-setup
- academic-deep-research
- actual-budget
- address-sanitizer
- agent-browser
- agent-builder
- agent-framework-azure-ai-py
- agent-md-refactor
- agenticflow-skills
- agents-sdk
- airc
- algorand-vulnerability-scanner
- algorithmic-art
- analytics-tracking
- answeroverflow
- anterior-cingulate-memory
- api-designer
- artifacts-builder
- ask-questions-if-underspecified
- atheris
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
- building-ai-agent-on-cloudflare
- building-mcp-server-on-cloudflare
- building-native-ui
- burpsuite-project-parser
- cairo-vulnerability-scanner
- cargo-fuzz
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
- coverage-analysis
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
- durable-objects
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
- fuzzing-obstacles
- gemini-nano-banana-pro-portraits
- github-issue-creator
- gitlab-cli-skills
- google-gemini-media
- google-imagen-3-hyperrealistic-landscape
- guidelines-advisor
- hackernews
- harness-writing
- hf-mcp
- hosted-agents-v2-py
- hugging-face-trackio
- humanize
- humanize-ai
- hybrid-memory
- insecure-defaults
- insula-memory
- internal-comms
- internal-comms
- interpreting-culture-index
- json-canvas
- juicebox-v5
- language-learning
- libfuzzer
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
- obsidian-bases
- obsidian-markdown
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
- preview-markdown
- pricing-strategy
- programmatic-seo
- property-based-testing
- pydantic-models-py
- railway
- react-expert
- react-flow-node-ts
- react-native-best-practices
- readwise-mcp
- receiving-code-review
- referral-program
- remotion-best-practices
- remotion-video-toolkit
- requesting-code-review
- research-paper-writer
- resume-builder
- rssaurus-cli
- sarif-parsing
- schema-markup
- secure-workflow-guide
- security-auditor
- semgrep
- semgrep
- semgrep-rule-creator
- semgrep-rule-variant-creator
- senior-architect
- senior-devops
- sharp-edges
- ship-learn-next
- signup-flow-cro
- skill-creator
- skill-creator
- skill-creator
- skill-creator
- skill-scanner
- skill-scanner
- slack-gif-creator
- slack-gif-creator
- social-content
- solana-vulnerability-scanner
- soulcraft
- spring-boot-engineer
- sql-pro
- ssh-essentials
- stock-market-pro
- substrate-vulnerability-scanner
- supabase-postgres-best-practices
- swift-expert
- system_monitor
- systematic-debugging
- tailwind-design-system
- template-skill
- template-skill
- test-driven-development
- test-specialist
- theme-factory
- theme-factory
- token-integration-analyzer
- ton-vulnerability-scanner
- transcribe
- trmnl
- turborepo
- ui-ux-pro-max
- upgrading-expo
- vercel-composition-patterns
- vercel-react-best-practices
- vercel-react-native-skills
- verification-before-completion
- vue
- vue-best-practices
- web-artifacts-builder
- web-artifacts-builder
- web-perf
- webapp-testing
- wordpress-pro
- wrangler
- wycheproof
- x-trends
- xlsx
- xlsx
- youtube-api
- youtube-music-cast
- youtube-search
- yt-video-downloader
- zotero
- zustand-store-ts

---

## Methodology

- **Scanner:** cisco-ai-skill-scanner
- **Analyzers:** behavioral_analyzer, bytecode, llm_analyzer, meta_analyzer, pipeline, static_analyzer, trigger_analyzer
- **Scan Date:** 2026-05-09T01:44:52.079973

### Limitations

- VirusTotal binary scanning not used (requires API key)
- No runtime verification - static and semantic analysis only
