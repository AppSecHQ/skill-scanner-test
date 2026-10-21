# AI Agent Skills Security Scan Report

**Generated:** 2026-10-21T21:38:07.738370
**Scanner:** cisco-ai-skill-scanner 2.3.1
**Analyzers:** behavioral, bytecode, correlation, llm, meta, pipeline, static, trigger

---

## Executive Summary

| Metric | Count |
|--------|-------|
| Total Skills Scanned | 827 |
| Safe Skills | 660 (80%) |
| Skills with Issues | 167 (20%) |
| Scan Errors | 0 |

### Severity Breakdown

| Severity | Count |
|----------|-------|
| CRITICAL | 245 |
| HIGH | 280 |
| MEDIUM | 792 |
| LOW | 205 |
| **Total Findings** | **1553** |

### Findings by Category

| Category | Count |
|----------|-------|
| data_exfiltration | 504 |
| command_injection | 252 |
| social_engineering | 172 |
| unauthorized_tool_use | 168 |
| transitive_trust_abuse | 151 |
| policy_violation | 97 |
| resource_abuse | 91 |
| prompt_injection | 54 |
| tool_chaining_abuse | 30 |
| hardcoded_secrets | 23 |
| skill_discovery_abuse | 6 |
| obfuscation | 3 |
| autonomy_abuse | 1 |
| supply_chain_attack | 1 |

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
| 15 | [autoskill](skills-autoskill-scan.md) | K | **No** | 11 | **CRITICAL** |
| 16 | [imap-smtp-email](imap-smtp-email-scan.md) | clawhub.ai | **No** | 11 | **HIGH** |
| 17 | [simmer](simmer-scan.md) | clawhub.ai | **No** | 10 | **CRITICAL** |
| 18 | [capability-evolver](capability-evolver-scan.md) | clawhub.ai | **No** | 9 | **CRITICAL** |
| 19 | [scientific-slides](skills-scientific-slides-scan.md) | K | **No** | 9 | **CRITICAL** |
| 20 | [session-handoff](session-handoff-scan.md) | skills.sh | **No** | 9 | **HIGH** |
| 21 | [citation-management](skills-citation-management-scan.md) | K | **No** | 8 | **CRITICAL** |
| 22 | [hugging-face-jobs](skills-hugging-face-jobs-scan.md) | huggingface | Yes | 8 | MEDIUM |
| 23 | [libafl](plugins-testing-handbook-skills-skills-libafl-scan.md) | trailofbits | **No** | 8 | **CRITICAL** |
| 24 | [modal](skills-modal-scan.md) | K | **No** | 8 | **HIGH** |
| 25 | [ontology-term-resolution](skills-ontology-term-resolution-scan.md) | K | Yes | 8 | MEDIUM |
| 26 | [ruzzy](plugins-testing-handbook-skills-skills-ruzzy-scan.md) | trailofbits | Yes | 8 | MEDIUM |
| 27 | [x402](x402-scan.md) | clawhub.ai | **No** | 8 | **CRITICAL** |
| 28 | [ClawDoro](clawdoro-scan.md) | clawhub.ai | Yes | 7 | MEDIUM |
| 29 | [auto-updater](auto-updater-skill-scan.md) | clawhub.ai | **No** | 7 | **CRITICAL** |
| 30 | [browse](browserbase-scan.md) | clawhub.ai | Yes | 7 | MEDIUM |
| 31 | [dev-browser](skills-dev-browser-scan.md) | sawyerhood | Yes | 7 | MEDIUM |
| 32 | [foundry](foundry-scan.md) | clawhub.ai | **No** | 7 | **CRITICAL** |
| 33 | [infographics](skills-infographics-scan.md) | K | **No** | 7 | **CRITICAL** |
| 34 | [latex-posters](skills-latex-posters-scan.md) | K | **No** | 7 | **CRITICAL** |
| 35 | [literature-review](skills-literature-review-scan.md) | K | **No** | 7 | **CRITICAL** |
| 36 | [open-notebook](skills-open-notebook-scan.md) | K | **No** | 7 | **CRITICAL** |
| 37 | [paper-lookup](skills-paper-lookup-scan.md) | K | Yes | 7 | MEDIUM |
| 38 | [telegram-pairing-customization](%E6%80%BB%E6%98%AF%E5%93%8D%E5%BA%94%E6%9C%AA%E9%85%8D%E5%AF%B9%E7%94%A8%E6%88%B7%E7%9A%84-start-%E6%B6%88%E6%81%AF-always-respond-to-start-messages-from-unpaired-users-scan.md) | clawhub.ai | **No** | 7 | **CRITICAL** |
| 39 | [vestaboard](vestaboard-scan.md) | clawhub.ai | Yes | 7 | MEDIUM |
| 40 | [ABM Outbound](abm-outbound-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 41 | [agent-task-manager](agent-task-manager-scan.md) | clawhub.ai | Yes | 6 | MEDIUM |
| 42 | [biopython](skills-biopython-scan.md) | K | Yes | 6 | MEDIUM |
| 43 | [browser-agent](browser-agent-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 44 | [bybit-trading](bybit-trading-agent-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 45 | [clawhub](clawhub-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 46 | [coding-agent](coding-agent-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 47 | [excel](excel-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 48 | [google](google-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 49 | [omni-stories](omni-stories-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 50 | [openwork](openwork-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 51 | [pathogen-variant-surveillance](skills-pathogen-variant-surveillance-scan.md) | K | Yes | 6 | MEDIUM |
| 52 | [phone-agent](phone-voice-agent-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 53 | [taskr](taskr-remote-task-tracking-for-ai-agents-scan.md) | clawhub.ai | Yes | 6 | MEDIUM |
| 54 | [using-git-worktrees](using-git-worktrees-scan.md) | skills.sh | Yes | 6 | MEDIUM |
| 55 | [wallet-tracker](wallet-tracker-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 56 | [whisper](whisper-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 57 | [Agent Browser](browser-automation-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 58 | [ClawGateSecure](claw-gate-secure-scan.md) | clawhub.ai | Yes | 5 | MEDIUM |
| 59 | [azure-eventhub-java](github-skills-azure-eventhub-java-scan.md) | microsoft | **No** | 5 | **CRITICAL** |
| 60 | [azure-storage-blob-java](github-skills-azure-storage-blob-java-scan.md) | microsoft | Yes | 5 | LOW |
| 61 | [base-trading-agent](base-trading-agent-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 62 | [browser-use](browser-use-scan.md) | skills.sh | **No** | 5 | **HIGH** |
| 63 | [clawdhub](clawdhub-cli-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 64 | [clawflows](clawflows-scan.md) | clawhub.ai | **No** | 5 | **HIGH** |
| 65 | [compound-engineering](compound-interest-calculator-scan.md) | clawhub.ai | **No** | 5 | **HIGH** |
| 66 | [cryptocurrency-trader](cryptocurrency-trader-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 67 | [ffuf-web-fuzzing](ffuf-skill-scan.md) | jthack | Yes | 5 | MEDIUM |
| 68 | [gitclaw](gitclaw-scan.md) | clawhub.ai | **No** | 5 | **HIGH** |
| 69 | [health-tracker](healthcheck-scan.md) | clawhub.ai | Yes | 5 | MEDIUM |
| 70 | [hugging-face-cli](skills-hugging-face-cli-scan.md) | huggingface | Yes | 5 | LOW |
| 71 | [hugging-science](skills-hugging-science-scan.md) | K | **No** | 5 | **HIGH** |
| 72 | [job-auto-apply](job-auto-apply-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 73 | [linear-autopilot](linear-autopilot-scan.md) | clawhub.ai | **No** | 5 | **HIGH** |
| 74 | [linkedin](linkedin-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 75 | [mersal](mersal-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 76 | [moltbook](moltbook-scan.md) | moltbook.com | **No** | 5 | **CRITICAL** |
| 77 | [nano-banana-pro](nano-banana-pro-image-generation-%26-editing-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 78 | [ncats-arax](skills-ncats-arax-scan.md) | K | Yes | 5 | MEDIUM |
| 79 | [openclaw-optimizer](startclaw-optimizer-scan.md) | clawhub.ai | **No** | 5 | **HIGH** |
| 80 | [polymarket](polymarket-better-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 81 | [research-lookup](skills-research-lookup-scan.md) | K | **No** | 5 | **CRITICAL** |
| 82 | [scientific-schematics](skills-scientific-schematics-scan.md) | K | **No** | 5 | **CRITICAL** |
| 83 | [sendclaw](sendclaw-email-without-human-permission-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 84 | [solana](solana-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 85 | [stealthy-auto-browse](stealthy-auto-browse-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 86 | [subagent-driven-development](subagent-driven-development-scan.md) | skills.sh | Yes | 5 | MEDIUM |
| 87 | [taskmaster](taskmaster-ai-cost-optimizer-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 88 | [tokenguard](tokenguard-scan.md) | clawhub.ai | **No** | 5 | **HIGH** |
| 89 | [using-superpowers](using-superpowers-scan.md) | skills.sh | **No** | 5 | **HIGH** |
| 90 | [voice-agent](voice-agent-scan.md) | clawhub.ai | **No** | 5 | **HIGH** |
| 91 | [windows-control](windows-control-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 92 | [yahoo-finance](yahoo-finance-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 93 | [youtube-watcher](youtube-watcher-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 94 | [MoltMedia](moltmedia-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 95 | [adguard](adguard-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 96 | [apewisdom](apewisdom-reddit-scanner-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 97 | [bags](sagb-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 98 | [binance-pay](binance-pay-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 99 | [channel](wechat-oa-channel-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 100 | [ci-gen](ci-cd-pipeline-generator-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 101 | [claude-chrome](claude-chrome-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 102 | [clawmail](clawmail-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 103 | [compound-engineering](compound-engineering-scan.md) | clawhub.ai | Yes | 4 | MEDIUM |
| 104 | [ctxly](mymemory.bot-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 105 | [discord-voice](discord-voice-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 106 | [docx](skills-docx-scan.md) | anthropic | **No** | 4 | **HIGH** |
| 107 | [esm](skills-esm-scan.md) | K | **No** | 4 | **HIGH** |
| 108 | [ethereum-gas-tracker](ethereum-gas-tracker-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 109 | [firebase-apk-scanner](plugins-firebase-apk-scanner-skills-firebase-apk-scanner-scan.md) | trailofbits | **No** | 4 | **CRITICAL** |
| 110 | [firebase-apk-scanner](plugins-firebase-apkner-skills-firebase-apkner-scan.md) | trailofbits | **No** | 4 | **HIGH** |
| 111 | [fuzzing-dictionary](plugins-testing-handbook-skills-skills-fuzzing-dictionary-scan.md) | trailofbits | **No** | 4 | **CRITICAL** |
| 112 | [glycoengineering](skills-glycoengineering-scan.md) | K | Yes | 4 | MEDIUM |
| 113 | [google-workspace](google-workspace-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 114 | [hyperliquid](hyperliquid-cli-with-hip3-support-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 115 | [insider-wallets-finder](insider-wallets-finder-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 116 | [lightning](lightning-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 117 | [nano-pdf](nano-pdf-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 118 | [notebooklm](notebooklm-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 119 | [phantom](phantom-wallet-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 120 | [redis](redis-scan.md) | clawhub.ai | Yes | 4 | MEDIUM |
| 121 | [slack](slack-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 122 | [sora-2-nature-documentary](sora-2-%E8%87%AA%E7%84%B6%E7%BA%AA%E5%BD%95%E7%89%87-scan.md) | clawhub.ai | Yes | 4 | LOW |
| 123 | [stripe-best-practices](skills-stripe-best-practices-scan.md) | stripe | Yes | 4 | MEDIUM |
| 124 | [supermemory](supermemory-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 125 | [tencent-map](%E8%85%BE%E8%AE%AF%E5%9C%B0%E5%9B%BEapi%E8%B0%83%E7%94%A8%E6%8A%80%E8%83%BD-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 126 | [tinyfish](tinyfish-web-agent-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 127 | [torch-geometric](skills-torch-geometric-scan.md) | K | **No** | 4 | **HIGH** |
| 128 | [torchdrug](skills-torchdrug-scan.md) | K | **No** | 4 | **HIGH** |
| 129 | [x-trends](x-twitter-trends-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 130 | [youtube-summarize](youtube-video-summarizer-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 131 | [2captcha](2captcha-cli-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 132 | [Docker Pro Diagnostic](docker-diag-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 133 | [MockAPI - Instant REST API from JSON](mockapi-instant-rest-api-from-json-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 134 | [YT Meta - YouTube Metadata Extractor](yt-meta-youtube-metadata-extractor-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 135 | [activecampaign](activecampaign-crm-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 136 | [activecampaign](baby-connect-logger-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 137 | [agentarcade](agent-arcade-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 138 | [agnxi-search](agent-skills-search-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 139 | [alby-bitcoin-payments-cli-skill](alby-bitcoin-payments-cli-skill-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 140 | [algorithmic-art](algorithmic-art-scan.md) | anthropic | Yes | 3 | MEDIUM |
| 141 | [amap](amap-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 142 | [api-docs-gen](api-docs-generator-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 143 | [api-gateway](api-gateway-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 144 | [atxp](atxp-scan.md) | skills.sh | Yes | 3 | MEDIUM |
| 145 | [azure-mgmt-fabric-py](github-skills-azure-mgmt-fabric-py-scan.md) | microsoft | **No** | 3 | **HIGH** |
| 146 | [baidu-map](%E8%B0%83%E7%94%A8%E7%99%BE%E5%BA%A6%E5%9C%B0%E5%9B%BEapi%E5%8A%9F%E8%83%BD-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 147 | [botcoin-miner](botcoin-miner-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 148 | [clawlist](clawlist-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 149 | [clickup](clickup-skill-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 150 | [codemod-gen](codemod-generator-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 151 | [crypto-gold-monitor](%E5%8A%A0%E5%AF%86%E8%B4%A7%E5%B8%81%E4%B8%8E%E8%B4%B5%E9%87%91%E5%B1%9E%E7%9B%91%E6%8E%A7-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 152 | [crypto-wallet](crypto-wallet-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 153 | [defi](defi-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 154 | [diagram-gen](diagram-generator-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 155 | [diff-summary](git-diff-summarizer-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 156 | [error-handler-gen](error-handler-generator-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 157 | [etf-assistant](etf%E6%8A%95%E8%B5%84%E5%8A%A9%E7%90%86-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 158 | [gcloud](google-cloud-platform-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 159 | [generate-image](skills-generate-image-scan.md) | K | Yes | 3 | MEDIUM |
| 160 | [genomic-intelligence](skills-genomic-intelligence-scan.md) | K | **No** | 3 | **HIGH** |
| 161 | [geomaster](skills-geomaster-scan.md) | K | **No** | 3 | **HIGH** |
| 162 | [giphy-gif](giphy-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 163 | [github-action-gen](github-action-generator-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 164 | [home-assistant](home-assistant-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 165 | [lighthouse-fixer](lighthouse-score-fixer-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 166 | [local-llm-router](skills-local-llm-router-scan.md) | hoodini | Yes | 3 | MEDIUM |
| 167 | [mageck](skills-mageck-scan.md) | K | Yes | 3 | MEDIUM |
| 168 | [mcps](mcps-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 169 | [nextflow](skills-nextflow-scan.md) | K | **No** | 3 | **CRITICAL** |
| 170 | [obsidian-sync](obsidian-sync-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 171 | [openclaw-checkpoint](openclaw-checkpoint-personal-ai-assistant-backup-%26-recovery-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 172 | [ossfuzz](plugins-testing-handbook-skills-skills-ossfuzz-scan.md) | trailofbits | Yes | 3 | LOW |
| 173 | [protocolsio-integration](skills-protocolsio-integration-scan.md) | K | Yes | 3 | MEDIUM |
| 174 | [reposit](reposit-collective-intelligence-for-ai-agents-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 175 | [save-money](save-money-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 176 | [skill-scanner](skill-scanner-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 177 | [stealth-browser](stealth-browser-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 178 | [swarmmarket](swarmmarket-skill%2C-make-money-with-your-agents-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 179 | [talent-de-cv](digital-identity%2C-cv-%26-resume-creator-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 180 | [technews](techmeme-news-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 181 | [telegram-auto-topic](telegram-auto-topic-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 182 | [testing-handbook-generator](plugins-testing-handbook-skills-skills-testing-handbook-generator-scan.md) | trailofbits | Yes | 3 | MEDIUM |
| 183 | [trade-signal](trade-singal-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 184 | [trading-coach](trading-coach-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 185 | [undetectable-ai](undetectable-ai-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 186 | [web-design-guidelines](web-design-guidelines-scan.md) | skills.sh | **No** | 3 | **HIGH** |
| 187 | [youtube-voice-summarizer](youtube-podcast-summarizer-via-elevenlabs-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 188 | [1inch](1inch-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 189 | [Agent Wallet](agent-wallet-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 190 | [Job Search MCP](job-search-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 191 | [adaptyv](skills-adaptyv-scan.md) | K | **No** | 2 | **HIGH** |
| 192 | [aegis-security](aegis-security-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 193 | [agent-money-tracker](intelligent-budget-tracker-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 194 | [ai-pdf-builder](ai-pdf-builder-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 195 | [aifs](aifs-http-file-system-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 196 | [antigravity-image-gen](antigravity-image-generator-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 197 | [apewisdom](apewisdom-redditner-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 198 | [aws-agentic-ai](plugins-aws-agentic-ai-skills-aws-agentic-ai-scan.md) | zxkane | Yes | 2 | MEDIUM |
| 199 | [aws-cdk-development](plugins-aws-cdk-skills-aws-cdk-development-scan.md) | zxkane | Yes | 2 | MEDIUM |
| 200 | [aws-infra](aws-infra-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 201 | [azure-ai-contentunderstanding-py](github-skills-azure-ai-contentunderstanding-py-scan.md) | microsoft | Yes | 2 | MEDIUM |
| 202 | [azure-ai-document-intelligence-dotnet](github-skills-azure-ai-document-intelligence-dotnet-scan.md) | microsoft | Yes | 2 | MEDIUM |
| 203 | [azure-ai-evaluation-py](github-skills-azure-ai-evaluation-py-scan.md) | microsoft | Yes | 2 | MEDIUM |
| 204 | [azure-monitor-opentelemetry-exporter-py](github-skills-azure-monitor-opentelemetry-exporter-py-scan.md) | microsoft | Yes | 2 | MEDIUM |
| 205 | [bids](skills-bids-scan.md) | K | Yes | 2 | MEDIUM |
| 206 | [bun](skills-bun-scan.md) | hoodini | Yes | 2 | LOW |
| 207 | [canvas-design](canvas-design-scan.md) | anthropic | Yes | 2 | MEDIUM |
| 208 | [canvas-design](skills-canvas-design-scan.md) | anthropic | Yes | 2 | MEDIUM |
| 209 | [chart-image](chart-image-generator-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 210 | [clawbridge](clawbridge-find-your-connections-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 211 | [clawbrowser](clawbrowser-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 212 | [clawkey](clawkey-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 213 | [clawops](clawops-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 214 | [code-explain](code-explainer-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 215 | [codex](codex-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 216 | [cold-email](machfive-cold-email-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 217 | [context-manager](smart-context-manager-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 218 | [core-vitals-fixer](core-web-vitals-optimizer-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 219 | [dependency-updater](dependency-updater-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 220 | [deps-analyzer](deps-checker-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 221 | [doc-coauthoring](skills-doc-coauthoring-scan.md) | anthropic | Yes | 2 | MEDIUM |
| 222 | [dockerfile-gen](dockerfile-generator-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 223 | [earnings-calendar](earnings-calendar-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 224 | [email](email-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 225 | [explorer](github-projects-explorer-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 226 | [expo-cicd-workflows](expo-cicd-workflows-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 227 | [ez-google](ez-google-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 228 | [feishu-api-docs](feishu-api-docs-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 229 | [feishu-bridge](feishu-bridge-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 230 | [finance](finance-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 231 | [gemini](gemini-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 232 | [gitclassic](gitclassic-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 233 | [githunt](githunt-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 234 | [gitlab-manager](gitlab-manager-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 235 | [gold_price_mcp](gold-price-mcp-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 236 | [google-calendar](google-calendar-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 237 | [habitica](habitica-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 238 | [humanize-ai-text](humanize-ai-text-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 239 | [humanizer](humanizer-scan.md) | clawhub.ai | Yes | 2 | LOW |
| 240 | [instagram](instagram-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 241 | [intodns](intodns-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 242 | [kimi-integration](kimi-integration-scan.md) | clawhub.ai | Yes | 2 | LOW |
| 243 | [landing-gen](landing-page-generator-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 244 | [langchain](skills-langchain-scan.md) | hoodini | **No** | 2 | **HIGH** |
| 245 | [launch-strategy](launch-strategy-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 246 | [llm](llm-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 247 | [local-pandoc](md-to-office-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 248 | [mailgun](mailgun-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 249 | [memory-hygiene](memory-hygiene-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 250 | [moltbot-ha](moltbot-home-assistant-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 251 | [multi-llm](multi-llm-fallback-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 252 | [n8n-api](n8n-api-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 253 | [near-email](near-email-skill-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 254 | [openocean](openocean-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 255 | [openpet](openpet-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 256 | [paperclip](skills-paperclip-scan.md) | K | Yes | 2 | MEDIUM |
| 257 | [payment](payment-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 258 | [pi-agent](skills-pi-agent-scan.md) | K | **No** | 2 | **CRITICAL** |
| 259 | [primer-x402](primer-x402-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 260 | [querit-search](querit-search-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 261 | [ralph-loop](ralph-loop-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 262 | [react-email](react-email-skills-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 263 | [rei](rei-clawd-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 264 | [search-reddit](search-reddit-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 265 | [searxng](searxng-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 266 | [send-email](send-email-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 267 | [smtp-send](smtp-send-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 268 | [spec-to-code-compliance](plugins-spec-to-code-compliance-skills-spec-to-code-compliance-scan.md) | trailofbits | Yes | 2 | MEDIUM |
| 269 | [stock-evaluator-v3](stock-evaluator-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 270 | [subtitles](subtitles-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 271 | [tg](telegram-cli-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 272 | [timesfm-forecasting](skills-timesfm-forecasting-scan.md) | K | Yes | 2 | LOW |
| 273 | [twitter](twitter-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 274 | [twitter-openclaw](x-twitter-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 275 | [ui-test](ui-test-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 276 | [upgrade-stripe](skills-upgrade-stripe-scan.md) | stripe | **No** | 2 | **CRITICAL** |
| 277 | [use-dom](use-dom-scan.md) | skills.sh | Yes | 2 | LOW |
| 278 | [veo3-video-gen](veo-3-video-gen-gemini-api-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 279 | [video-transcript](video-transcript-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 280 | [waypoint-bio](skills-waypoint-bio-scan.md) | K | **No** | 2 | **HIGH** |
| 281 | [webhook-gen](webhook-generator-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 282 | [writing-skills](writing-skills-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 283 | [x-api](x-api-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 284 | [youtube-playlist](youtube-playlist-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 285 | [Better Polymarket](polymarket-trading-skill-scan.md) | clawhub.ai | **No** | 1 | **HIGH** |
| 286 | [Meta Tags - SEO Tag Generator](meta-tags-seo-tag-generator-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 287 | [aflpp](plugins-testing-handbook-skills-skills-aflpp-scan.md) | trailofbits | Yes | 1 | MEDIUM |
| 288 | [algorand-vulnerability-scanner](plugins-building-secure-contracts-skills-algorand-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 289 | [alphagenome](skills-alphagenome-scan.md) | K | Yes | 1 | LOW |
| 290 | [analytics-metrics](skills-analytics-metrics-scan.md) | hoodini | Yes | 1 | INFO |
| 291 | [ansible](ansible-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 292 | [audit-prep-assistant](plugins-building-secure-contracts-skills-audit-prep-assistant-scan.md) | trailofbits | Yes | 1 | MEDIUM |
| 293 | [aws-account-management](skills-aws-account-management-scan.md) | hoodini | Yes | 1 | INFO |
| 294 | [aws-agentcore](skills-aws-agentcore-scan.md) | hoodini | Yes | 1 | INFO |
| 295 | [aws-strands](skills-aws-strands-scan.md) | hoodini | Yes | 1 | INFO |
| 296 | [azure-ai-voicelive-dotnet](github-skills-azure-ai-voicelive-dotnet-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 297 | [azure-communication-callautomation-java](github-skills-azure-communication-callautomation-java-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 298 | [azure-communication-chat-java](github-skills-azure-communication-chat-java-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 299 | [azure-containerregistry-py](github-skills-azure-containerregistry-py-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 300 | [azure-mgmt-apicenter-py](github-skills-azure-mgmt-apicenter-py-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 301 | [azure-mgmt-apimanagement-dotnet](github-skills-azure-mgmt-apimanagement-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 302 | [azure-security-keyvault-keys-java](github-skills-azure-security-keyvault-keys-java-scan.md) | microsoft | Yes | 1 | LOW |
| 303 | [azure-security-keyvault-secrets-java](github-skills-azure-security-keyvault-secrets-java-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 304 | [birthday-reminder](Birthday%20Reminder-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 305 | [cairo-vulnerability-scanner](plugins-building-secure-contracts-skills-cairo-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 306 | [calendar](calendar-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 307 | [captions](captions-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 308 | [chromadb-memory](chromadb-memory-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 309 | [clawdbot-security](clawdbot-security-audit-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 310 | [cloudflare](skills-cloudflare-scan.md) | hoodini | Yes | 1 | INFO |
| 311 | [codeql](plugins-testing-handbook-skills-skills-codeql-scan.md) | trailofbits | Yes | 1 | LOW |
| 312 | [copilot-docs](skills-copilot-docs-scan.md) | hoodini | Yes | 1 | INFO |
| 313 | [copilot-sdk](skills-copilot-sdk-scan.md) | hoodini | Yes | 1 | INFO |
| 314 | [cosmos-vulnerability-scanner](plugins-building-secure-contracts-skills-cosmos-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 315 | [daily-ai-news](daily-ai-news-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 316 | [database](database-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 317 | [dnanexus-integration](skills-dnanexus-integration-scan.md) | K | Yes | 1 | MEDIUM |
| 318 | [doc-coauthoring](doc-coauthoring-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 319 | [docx](docx-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 320 | [domain-name-brainstormer](domain-name-brainstormer-scan.md) | skills.sh | Yes | 1 | MEDIUM |
| 321 | [dwlf](a-clawdbot-skill-that-gives-your-agent-native-access-to-dwlf-%E2%80%94-a-market-analysis-platform-for-crypto-and-stocks.-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 322 | [eslint-gen](eslint-config-generator-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 323 | [fal-ai](skills-fal-ai-scan.md) | hoodini | Yes | 1 | INFO |
| 324 | [figma](skills-figma-scan.md) | hoodini | Yes | 1 | INFO |
| 325 | [frontend-ui-dark-ts](github-skills-frontend-ui-dark-ts-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 326 | [gaussian-process-mlp-hybrid](ai-%E7%BC%96%E7%A0%81-prompt-skill-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 327 | [genomic-coordinates](skills-genomic-coordinates-scan.md) | K | Yes | 1 | LOW |
| 328 | [gget](skills-gget-scan.md) | K | Yes | 1 | LOW |
| 329 | [github-trending](skills-github-trending-scan.md) | hoodini | Yes | 1 | INFO |
| 330 | [glm-coding-agent](glm-coding-agent-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 331 | [google-workspace-cli](skills-google-workspace-cli-scan.md) | hoodini | Yes | 1 | INFO |
| 332 | [honest-agent](skills-honest-agent-scan.md) | hoodini | Yes | 1 | INFO |
| 333 | [imaging-data-commons](skills-imaging-data-commons-scan.md) | K | Yes | 1 | MEDIUM |
| 334 | [iso-standards-readiness](skills-iso-standards-readiness-scan.md) | K | Yes | 1 | LOW |
| 335 | [kalshi](kalshi-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 336 | [liteparse](skills-liteparse-scan.md) | K | Yes | 1 | LOW |
| 337 | [m365-agents-py](github-skills-m365-agents-py-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 338 | [marketing-psychology](marketing-psychology-scan.md) | skills.sh | Yes | 1 | MEDIUM |
| 339 | [memory-system-v2](memory-system-v2-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 340 | [mermaid-diagrams](skills-mermaid-diagrams-scan.md) | hoodini | Yes | 1 | INFO |
| 341 | [mobile-responsiveness](skills-mobile-responsiveness-scan.md) | hoodini | Yes | 1 | INFO |
| 342 | [mongodb](skills-mongodb-scan.md) | hoodini | Yes | 1 | INFO |
| 343 | [nano-banana-pro](skills-nano-banana-pro-scan.md) | hoodini | Yes | 1 | INFO |
| 344 | [notion](notion-api-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 345 | [notion](notion-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 346 | [npkill](npkill-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 347 | [omero-integration](skills-omero-integration-scan.md) | K | **No** | 1 | **CRITICAL** |
| 348 | [owasp-security](skills-owasp-security-scan.md) | hoodini | Yes | 1 | INFO |
| 349 | [para-second-brain](para-second-brain-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 350 | [paypal](paypal-scan.md) | clawhub.ai | **No** | 1 | **HIGH** |
| 351 | [perf-auditor](performance-auditor-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 352 | [pipedrive](pipedrive-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 353 | [playwright-skill](skills-playwright-skill-scan.md) | lackeyjb | Yes | 1 | MEDIUM |
| 354 | [popup-cro](popup-cro-scan.md) | skills.sh | Yes | 1 | MEDIUM |
| 355 | [pptx-posters](skills-pptx-posters-scan.md) | K | Yes | 1 | LOW |
| 356 | [pyhealth](skills-pyhealth-scan.md) | K | Yes | 1 | INFO |
| 357 | [pytorch-lightning](skills-pytorch-lightning-scan.md) | K | **No** | 1 | **HIGH** |
| 358 | [qiime2-amplicon](skills-qiime2-amplicon-scan.md) | K | **No** | 1 | **HIGH** |
| 359 | [qmd](qmd-external-knowledge-base-search-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 360 | [railway](skills-railway-scan.md) | hoodini | Yes | 1 | INFO |
| 361 | [reddit](reddit-scraper-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 362 | [seo-audit](seo-audit-scan.md) | skills.sh | Yes | 1 | LOW |
| 363 | [shabbat-times](skills-shabbat-times-scan.md) | hoodini | Yes | 1 | INFO |
| 364 | [shorten](url-shortener-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 365 | [skill-name](templates-skill-template-scan.md) | hoodini | Yes | 1 | INFO |
| 366 | [solana-vulnerability-scanner](plugins-building-secure-contracts-skills-solana-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 367 | [sql-assistant](sql-assistant-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 368 | [statistical-power](skills-statistical-power-scan.md) | K | **No** | 1 | **HIGH** |
| 369 | [streme-launcher](streme-token-launcher-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 370 | [substrate-vulnerability-scanner](plugins-building-secure-contracts-skills-substrate-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 371 | [tellurium](skills-tellurium-scan.md) | K | Yes | 1 | LOW |
| 372 | [ton-vulnerability-scanner](plugins-building-secure-contracts-skills-ton-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 373 | [transformers](skills-transformers-scan.md) | K | **No** | 1 | **HIGH** |
| 374 | [ux-design-systems](skills-ux-design-systems-scan.md) | hoodini | Yes | 1 | INFO |
| 375 | [variant-analysis](plugins-variant-analysis-skills-variant-analysis-scan.md) | trailofbits | Yes | 1 | LOW |
| 376 | [vercel](skills-vercel-scan.md) | hoodini | Yes | 1 | INFO |
| 377 | [video-agent](video-agent-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 378 | [watch-my-money](watch-my-money-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 379 | [web-accessibility](skills-web-accessibility-scan.md) | hoodini | Yes | 1 | INFO |
| 380 | [webapp-testing](webapp-testing-scan.md) | anthropic | Yes | 1 | MEDIUM |
| 381 | [writing-clearly-and-concisely](writing-clearly-and-concisely-scan.md) | skills.sh | Yes | 1 | LOW |
| 382 | [writing-plans](writing-plans-scan.md) | skills.sh | Yes | 1 | LOW |
| 383 | [youtube-channels](youtube-channels-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 384 | [youtube-data](youtube-data-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 385 | [youtube-full](youtube-full-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 386 | [youtube-transcript](youtube-transcript-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 387 | [10-of-my-most-popular-text-to-image-series-prompts-78b0897e](test-skill-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 388 | [13c-metabolic-flux](skills-13c-metabolic-flux-scan.md) | K | Yes | 0 | SAFE |
| 389 | [Content ID Guide](content-id-guide-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 390 | [Search Realtime Information](realtime-web-search-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 391 | [ab-test-setup](ab-test-setup-scan.md) | skills.sh | Yes | 0 | SAFE |
| 392 | [academic-deep-research](academic-deep-research-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 393 | [actual-budget](actual-budget-cli-to-interact-with-the-actual-budget-api-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 394 | [address-sanitizer](plugins-testing-handbook-skills-skills-address-sanitizer-scan.md) | trailofbits | Yes | 0 | SAFE |
| 395 | [aeon](skills-aeon-scan.md) | K | Yes | 0 | SAFE |
| 396 | [agent-browser](agent-browser-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 397 | [agent-builder](agent-builder-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 398 | [agent-framework-azure-ai-py](github-skills-agent-framework-azure-ai-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 399 | [agent-md-refactor](agent-md-refactor-scan.md) | skills.sh | Yes | 0 | SAFE |
| 400 | [agenticflow-skills](agenticflow-skills-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 401 | [agents-sdk](skills-agents-sdk-scan.md) | cloudflare | Yes | 0 | SAFE |
| 402 | [airc](airc-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 403 | [algorand-vulnerability-scanner](plugins-building-secure-contracts-skills-algorand-vulnerabilityner-scan.md) | trailofbits | Yes | 0 | SAFE |
| 404 | [algorithmic-art](skills-algorithmic-art-scan.md) | anthropic | Yes | 0 | SAFE |
| 405 | [analytical-method-validation](skills-analytical-method-validation-scan.md) | K | Yes | 0 | SAFE |
| 406 | [analytics-tracking](analytics-tracking-scan.md) | skills.sh | Yes | 0 | SAFE |
| 407 | [anndata](skills-anndata-scan.md) | K | Yes | 0 | SAFE |
| 408 | [answeroverflow](answer-overflow-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 409 | [anterior-cingulate-memory](anterior-cingulate-memory-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 410 | [api-designer](api-designer-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 411 | [arbor](skills-arbor-scan.md) | K | Yes | 0 | SAFE |
| 412 | [arboreto](skills-arboreto-scan.md) | K | Yes | 0 | SAFE |
| 413 | [artifacts-builder](artifacts-builder-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 414 | [ask-questions-if-underspecified](plugins-ask-questions-if-underspecified-skills-ask-questions-if-underspecified-scan.md) | trailofbits | Yes | 0 | SAFE |
| 415 | [astropy](skills-astropy-scan.md) | K | Yes | 0 | SAFE |
| 416 | [atheris](plugins-testing-handbook-skills-skills-atheris-scan.md) | trailofbits | Yes | 0 | SAFE |
| 417 | [audit-context-building](plugins-audit-context-building-skills-audit-context-building-scan.md) | trailofbits | Yes | 0 | SAFE |
| 418 | [audit-website](audit-website-scan.md) | skills.sh | Yes | 0 | SAFE |
| 419 | [auto-animate](auto-animate-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 420 | [aws-cost-operations](plugins-aws-cost-ops-skills-aws-cost-operations-scan.md) | zxkane | Yes | 0 | SAFE |
| 421 | [aws-mcp-setup](plugins-aws-common-skills-aws-mcp-setup-scan.md) | zxkane | Yes | 0 | SAFE |
| 422 | [aws-serverless-eda](plugins-serverless-eda-skills-aws-serverless-eda-scan.md) | zxkane | Yes | 0 | SAFE |
| 423 | [azd-deployment](github-skills-azd-deployment-scan.md) | microsoft | Yes | 0 | SAFE |
| 424 | [azure-ai-agents-persistent-dotnet](github-skills-azure-ai-agents-persistent-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 425 | [azure-ai-agents-persistent-java](github-skills-azure-ai-agents-persistent-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 426 | [azure-ai-anomalydetector-java](github-skills-azure-ai-anomalydetector-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 427 | [azure-ai-contentsafety-java](github-skills-azure-ai-contentsafety-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 428 | [azure-ai-contentsafety-py](github-skills-azure-ai-contentsafety-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 429 | [azure-ai-formrecognizer-java](github-skills-azure-ai-formrecognizer-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 430 | [azure-ai-ml-py](github-skills-azure-ai-ml-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 431 | [azure-ai-openai-dotnet](github-skills-azure-ai-openai-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 432 | [azure-ai-projects-dotnet](github-skills-azure-ai-projects-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 433 | [azure-ai-projects-java](github-skills-azure-ai-projects-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 434 | [azure-ai-projects-py](github-skills-azure-ai-projects-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 435 | [azure-ai-textanalytics-py](github-skills-azure-ai-textanalytics-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 436 | [azure-ai-transcription-py](github-skills-azure-ai-transcription-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 437 | [azure-ai-translation-document-py](github-skills-azure-ai-translation-document-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 438 | [azure-ai-translation-text-py](github-skills-azure-ai-translation-text-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 439 | [azure-ai-vision-imageanalysis-java](github-skills-azure-ai-vision-imageanalysis-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 440 | [azure-ai-vision-imageanalysis-py](github-skills-azure-ai-vision-imageanalysis-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 441 | [azure-ai-voicelive-java](github-skills-azure-ai-voicelive-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 442 | [azure-ai-voicelive-py](github-skills-azure-ai-voicelive-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 443 | [azure-appconfiguration-java](github-skills-azure-appconfiguration-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 444 | [azure-appconfiguration-py](github-skills-azure-appconfiguration-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 445 | [azure-communication-callingserver-java](github-skills-azure-communication-callingserver-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 446 | [azure-communication-common-java](github-skills-azure-communication-common-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 447 | [azure-communication-sms-java](github-skills-azure-communication-sms-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 448 | [azure-compute-batch-java](github-skills-azure-compute-batch-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 449 | [azure-cosmos-db-py](github-skills-azure-cosmos-db-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 450 | [azure-cosmos-java](github-skills-azure-cosmos-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 451 | [azure-cosmos-py](github-skills-azure-cosmos-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 452 | [azure-data-tables-java](github-skills-azure-data-tables-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 453 | [azure-data-tables-py](github-skills-azure-data-tables-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 454 | [azure-eventgrid-dotnet](github-skills-azure-eventgrid-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 455 | [azure-eventgrid-java](github-skills-azure-eventgrid-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 456 | [azure-eventgrid-py](github-skills-azure-eventgrid-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 457 | [azure-eventhub-dotnet](github-skills-azure-eventhub-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 458 | [azure-eventhub-py](github-skills-azure-eventhub-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 459 | [azure-identity-dotnet](github-skills-azure-identity-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 460 | [azure-identity-java](github-skills-azure-identity-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 461 | [azure-identity-py](github-skills-azure-identity-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 462 | [azure-keyvault-py](github-skills-azure-keyvault-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 463 | [azure-maps-search-dotnet](github-skills-azure-maps-search-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 464 | [azure-messaging-webpubsub-java](github-skills-azure-messaging-webpubsub-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 465 | [azure-messaging-webpubsubservice-py](github-skills-azure-messaging-webpubsubservice-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 466 | [azure-mgmt-apicenter-dotnet](github-skills-azure-mgmt-apicenter-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 467 | [azure-mgmt-apimanagement-py](github-skills-azure-mgmt-apimanagement-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 468 | [azure-mgmt-applicationinsights-dotnet](github-skills-azure-mgmt-applicationinsights-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 469 | [azure-mgmt-arizeaiobservabilityeval-dotnet](github-skills-azure-mgmt-arizeaiobservabilityeval-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 470 | [azure-mgmt-botservice-dotnet](github-skills-azure-mgmt-botservice-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 471 | [azure-mgmt-botservice-py](github-skills-azure-mgmt-botservice-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 472 | [azure-mgmt-fabric-dotnet](github-skills-azure-mgmt-fabric-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 473 | [azure-mgmt-mongodbatlas-dotnet](github-skills-azure-mgmt-mongodbatlas-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 474 | [azure-mgmt-weightsandbiases-dotnet](github-skills-azure-mgmt-weightsandbiases-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 475 | [azure-microsoft-playwright-testing-ts](github-skills-azure-microsoft-playwright-testing-ts-scan.md) | microsoft | Yes | 0 | SAFE |
| 476 | [azure-monitor-ingestion-java](github-skills-azure-monitor-ingestion-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 477 | [azure-monitor-ingestion-py](github-skills-azure-monitor-ingestion-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 478 | [azure-monitor-opentelemetry-exporter-java](github-skills-azure-monitor-opentelemetry-exporter-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 479 | [azure-monitor-opentelemetry-py](github-skills-azure-monitor-opentelemetry-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 480 | [azure-monitor-query-java](github-skills-azure-monitor-query-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 481 | [azure-monitor-query-py](github-skills-azure-monitor-query-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 482 | [azure-postgres-ts](github-skills-azure-postgres-ts-scan.md) | microsoft | Yes | 0 | SAFE |
| 483 | [azure-resource-manager-cosmosdb-dotnet](github-skills-azure-resource-manager-cosmosdb-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 484 | [azure-resource-manager-durabletask-dotnet](github-skills-azure-resource-manager-durabletask-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 485 | [azure-resource-manager-mysql-dotnet](github-skills-azure-resource-manager-mysql-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 486 | [azure-resource-manager-playwright-dotnet](github-skills-azure-resource-manager-playwright-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 487 | [azure-resource-manager-postgresql-dotnet](github-skills-azure-resource-manager-postgresql-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 488 | [azure-resource-manager-redis-dotnet](github-skills-azure-resource-manager-redis-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 489 | [azure-resource-manager-sql-dotnet](github-skills-azure-resource-manager-sql-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 490 | [azure-search-documents-dotnet](github-skills-azure-search-documents-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 491 | [azure-search-documents-py](github-skills-azure-search-documents-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 492 | [azure-security-keyvault-keys-dotnet](github-skills-azure-security-keyvault-keys-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 493 | [azure-servicebus-dotnet](github-skills-azure-servicebus-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 494 | [azure-servicebus-py](github-skills-azure-servicebus-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 495 | [azure-speech-to-text-rest-py](github-skills-azure-speech-to-text-rest-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 496 | [azure-storage-blob-py](github-skills-azure-storage-blob-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 497 | [azure-storage-file-datalake-py](github-skills-azure-storage-file-datalake-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 498 | [azure-storage-file-share-py](github-skills-azure-storage-file-share-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 499 | [azure-storage-queue-py](github-skills-azure-storage-queue-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 500 | [basal-ganglia-memory](basal-ganglia-memory-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 501 | [bat-cat](bat-cat-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 502 | [benchling-integration](skills-benchling-integration-scan.md) | K | Yes | 0 | SAFE |
| 503 | [bgpt-paper-search](skills-bgpt-paper-search-scan.md) | K | Yes | 0 | SAFE |
| 504 | [bioservices](skills-bioservices-scan.md) | K | Yes | 0 | SAFE |
| 505 | [brainstorming](brainstorming-scan.md) | skills.sh | Yes | 0 | SAFE |
| 506 | [brand-guidelines](brand-guidelines-scan.md) | anthropic | Yes | 0 | SAFE |
| 507 | [brand-guidelines](skills-brand-guidelines-scan.md) | anthropic | Yes | 0 | SAFE |
| 508 | [building-ai-agent-on-cloudflare](skills-building-ai-agent-on-cloudflare-scan.md) | cloudflare | Yes | 0 | SAFE |
| 509 | [building-mcp-server-on-cloudflare](skills-building-mcp-server-on-cloudflare-scan.md) | cloudflare | Yes | 0 | SAFE |
| 510 | [building-native-ui](building-native-ui-scan.md) | skills.sh | Yes | 0 | SAFE |
| 511 | [bulk-rnaseq](skills-bulk-rnaseq-scan.md) | K | Yes | 0 | SAFE |
| 512 | [burpsuite-project-parser](plugins-burpsuite-project-parser-skills-scan.md) | trailofbits | Yes | 0 | SAFE |
| 513 | [cairo-vulnerability-scanner](plugins-building-secure-contracts-skills-cairo-vulnerabilityner-scan.md) | trailofbits | Yes | 0 | SAFE |
| 514 | [cantera](skills-cantera-scan.md) | K | Yes | 0 | SAFE |
| 515 | [cargo-fuzz](plugins-testing-handbook-skills-skills-cargo-fuzz-scan.md) | trailofbits | Yes | 0 | SAFE |
| 516 | [cellprofiler](skills-cellprofiler-scan.md) | K | Yes | 0 | SAFE |
| 517 | [cellxgene-census](skills-cellxgene-census-scan.md) | K | Yes | 0 | SAFE |
| 518 | [chirp](chirp-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 519 | [cirq](skills-cirq-scan.md) | K | Yes | 0 | SAFE |
| 520 | [claude-in-chrome-troubleshooting](plugins-claude-in-chrome-troubleshooting-skills-claude-in-chrome-troubleshooting-scan.md) | trailofbits | Yes | 0 | SAFE |
| 521 | [clawdbot-cost-tracker](cost-tracking-for-models-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 522 | [clawdbot-self-security-audit](clawdbot-security-check-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 523 | [clawdefender](clawdefender-openclaw-security-prompt-injection%2C-rogue-skills-etc-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 524 | [clawdex](clawdex-by-koi-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 525 | [clinical-decision-support](skills-clinical-decision-support-scan.md) | K | Yes | 0 | SAFE |
| 526 | [clinical-reports](skills-clinical-reports-scan.md) | K | Yes | 0 | SAFE |
| 527 | [cobrapy](skills-cobrapy-scan.md) | K | Yes | 0 | SAFE |
| 528 | [code-maturity-assessor](plugins-building-secure-contracts-skills-code-maturity-assessor-scan.md) | trailofbits | Yes | 0 | SAFE |
| 529 | [codeql](plugins-static-analysis-skills-codeql-scan.md) | trailofbits | Yes | 0 | SAFE |
| 530 | [coding-agent](multi-coding-agent-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 531 | [commit-work](commit-work-scan.md) | skills.sh | Yes | 0 | SAFE |
| 532 | [competitor-alternatives](competitor-alternatives-scan.md) | skills.sh | Yes | 0 | SAFE |
| 533 | [consciousness-council](skills-consciousness-council-scan.md) | K | Yes | 0 | SAFE |
| 534 | [constant-time-analysis](plugins-constant-time-analysis-skills-constant-time-analysis-scan.md) | trailofbits | Yes | 0 | SAFE |
| 535 | [copy-editing](copy-editing-scan.md) | skills.sh | Yes | 0 | SAFE |
| 536 | [copywriting](copywriting-scan.md) | skills.sh | Yes | 0 | SAFE |
| 537 | [cosmos-vulnerability-scanner](plugins-building-secure-contracts-skills-cosmos-vulnerabilityner-scan.md) | trailofbits | Yes | 0 | SAFE |
| 538 | [coverage-analysis](plugins-testing-handbook-skills-skills-coverage-analysis-scan.md) | trailofbits | Yes | 0 | SAFE |
| 539 | [create-auth-skill](better-auth-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 540 | [create-auth-skill](create-auth-skill-scan.md) | skills.sh | Yes | 0 | SAFE |
| 541 | [cron-mastery](cron-mastery-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 542 | [daily-meeting-update](daily-meeting-update-scan.md) | skills.sh | Yes | 0 | SAFE |
| 543 | [dask](skills-dask-scan.md) | K | Yes | 0 | SAFE |
| 544 | [database-lookup](skills-database-lookup-scan.md) | K | Yes | 0 | SAFE |
| 545 | [datalad](skills-datalad-scan.md) | K | Yes | 0 | SAFE |
| 546 | [datamol](skills-datamol-scan.md) | K | Yes | 0 | SAFE |
| 547 | [decision-trees](decision-trees-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 548 | [deepchem](skills-deepchem-scan.md) | K | Yes | 0 | SAFE |
| 549 | [deepspot-m](skills-deepspot-m-scan.md) | K | Yes | 0 | SAFE |
| 550 | [deeptools](skills-deeptools-scan.md) | K | Yes | 0 | SAFE |
| 551 | [depmap](skills-depmap-scan.md) | K | Yes | 0 | SAFE |
| 552 | [dhdna-profiler](skills-dhdna-profiler-scan.md) | K | Yes | 0 | SAFE |
| 553 | [diffdock](skills-diffdock-scan.md) | K | Yes | 0 | SAFE |
| 554 | [differential-review](plugins-differential-review-skills-differential-review-scan.md) | trailofbits | Yes | 0 | SAFE |
| 555 | [discord-chat](discord-chat-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 556 | [dispatching-parallel-agents](dispatching-parallel-agents-scan.md) | skills.sh | Yes | 0 | SAFE |
| 557 | [dont-hack-me](dont-hack-me-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 558 | [dotnet-expert](dotnet-expert-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 559 | [durable-objects](skills-durable-objects-scan.md) | cloudflare | Yes | 0 | SAFE |
| 560 | [dwarf-expert](plugins-dwarf-expert-skills-dwarf-expert-scan.md) | trailofbits | Yes | 0 | SAFE |
| 561 | [email-best-practices](email-best-practices-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 562 | [email-sequence](email-sequence-scan.md) | skills.sh | Yes | 0 | SAFE |
| 563 | [entry-point-analyzer](plugins-entry-point-analyzer-skills-entry-point-analyzer-scan.md) | trailofbits | Yes | 0 | SAFE |
| 564 | [error-guard](error-guard-%E2%80%94-control%E2%80%91plane-safety-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 565 | [etetoolkit](skills-etetoolkit-scan.md) | K | Yes | 0 | SAFE |
| 566 | [exa-search](skills-exa-search-scan.md) | K | Yes | 0 | SAFE |
| 567 | [exa-web-search-free](exa-web-search-free-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 568 | [executing-plans](executing-plans-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 569 | [experimental-design](skills-experimental-design-scan.md) | K | Yes | 0 | SAFE |
| 570 | [exploratory-data-analysis](skills-exploratory-data-analysis-scan.md) | K | Yes | 0 | SAFE |
| 571 | [expo-api-routes](expo-api-routes-scan.md) | skills.sh | Yes | 0 | SAFE |
| 572 | [expo-deployment](expo-deployment-scan.md) | skills.sh | Yes | 0 | SAFE |
| 573 | [expo-dev-client](expo-dev-client-scan.md) | skills.sh | Yes | 0 | SAFE |
| 574 | [expo-tailwind-setup](expo-tailwind-setup-scan.md) | skills.sh | Yes | 0 | SAFE |
| 575 | [ez-cronjob](ez-cronjob-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 576 | [fastapi-router-py](github-skills-fastapi-router-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 577 | [faster-whisper](faster-whisper-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 578 | [feast](feast-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 579 | [fictiv](skills-fictiv-scan.md) | K | Yes | 0 | SAFE |
| 580 | [find-skills](find-skills-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 581 | [finishing-a-development-branch](finishing-a-development-branch-scan.md) | skills.sh | Yes | 0 | SAFE |
| 582 | [fix-review](plugins-fix-review-skills-fix-review-scan.md) | trailofbits | Yes | 0 | SAFE |
| 583 | [flowio](skills-flowio-scan.md) | K | Yes | 0 | SAFE |
| 584 | [flowkit](skills-flowkit-scan.md) | K | Yes | 0 | SAFE |
| 585 | [fluidsim](skills-fluidsim-scan.md) | K | Yes | 0 | SAFE |
| 586 | [folklore-variant-evidence](skills-folklore-variant-evidence-scan.md) | K | Yes | 0 | SAFE |
| 587 | [form-cro](form-cro-scan.md) | skills.sh | Yes | 0 | SAFE |
| 588 | [foundry-iq-py](github-skills-foundry-iq-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 589 | [free-tool-strategy](free-tool-strategy-scan.md) | skills.sh | Yes | 0 | SAFE |
| 590 | [frontend-design](frontend-design-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 591 | [frontend-design](skills-frontend-design-scan.md) | anthropic | Yes | 0 | SAFE |
| 592 | [fuzzing-obstacles](plugins-testing-handbook-skills-skills-fuzzing-obstacles-scan.md) | trailofbits | Yes | 0 | SAFE |
| 593 | [gemini-nano-banana-pro-portraits](gemini-nano-banana-pro-portraits-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 594 | [geniml](skills-geniml-scan.md) | K | Yes | 0 | SAFE |
| 595 | [geopandas](skills-geopandas-scan.md) | K | Yes | 0 | SAFE |
| 596 | [get-available-resources](skills-get-available-resources-scan.md) | K | Yes | 0 | SAFE |
| 597 | [ginkgo-cloud-lab](skills-ginkgo-cloud-lab-scan.md) | K | Yes | 0 | SAFE |
| 598 | [github-issue-creator](github-skills-github-issue-creator-scan.md) | microsoft | Yes | 0 | SAFE |
| 599 | [gitlab-cli-skills](gitlab-cli-skills-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 600 | [google-gemini-media](google-gemini-media-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 601 | [google-imagen-3-hyperrealistic-landscape](google-imagen-3-%E8%B6%85%E5%86%99%E5%AE%9E%E9%A3%8E%E6%99%AF-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 602 | [gtars](skills-gtars-scan.md) | K | Yes | 0 | SAFE |
| 603 | [guidelines-advisor](plugins-building-secure-contracts-skills-guidelines-advisor-scan.md) | trailofbits | Yes | 0 | SAFE |
| 604 | [hackernews](hacker-news-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 605 | [harness-writing](plugins-testing-handbook-skills-skills-harness-writing-scan.md) | trailofbits | Yes | 0 | SAFE |
| 606 | [hf-mcp](hf-mcp-skills-hf-mcp-scan.md) | huggingface | Yes | 0 | SAFE |
| 607 | [histolab](skills-histolab-scan.md) | K | Yes | 0 | SAFE |
| 608 | [hosted-agents-v2-py](github-skills-hosted-agents-v2-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 609 | [hugging-face-trackio](skills-hugging-face-trackio-scan.md) | huggingface | Yes | 0 | SAFE |
| 610 | [humanize](humanize-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 611 | [humanize-ai](humanize-ai-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 612 | [hybrid-memory](hybrid-memory-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 613 | [hypogenic](skills-hypogenic-scan.md) | K | Yes | 0 | SAFE |
| 614 | [hypothesis-generation](skills-hypothesis-generation-scan.md) | K | Yes | 0 | SAFE |
| 615 | [insecure-defaults](plugins-insecure-defaults-skills-insecure-defaults-scan.md) | trailofbits | Yes | 0 | SAFE |
| 616 | [insula-memory](insula-memory-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 617 | [internal-comms](internal-comms-scan.md) | anthropic | Yes | 0 | SAFE |
| 618 | [internal-comms](skills-internal-comms-scan.md) | anthropic | Yes | 0 | SAFE |
| 619 | [interpreting-culture-index](plugins-culture-index-skills-interpreting-culture-index-scan.md) | trailofbits | Yes | 0 | SAFE |
| 620 | [json-canvas](skills-json-canvas-scan.md) | kepano | Yes | 0 | SAFE |
| 621 | [juicebox-v5](juicy-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 622 | [lab-hardware-cad](skills-lab-hardware-cad-scan.md) | K | Yes | 0 | SAFE |
| 623 | [labarchive-integration](skills-labarchive-integration-scan.md) | K | Yes | 0 | SAFE |
| 624 | [lamindb](skills-lamindb-scan.md) | K | Yes | 0 | SAFE |
| 625 | [language-learning](language-learning-tutor-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 626 | [latchbio-integration](skills-latchbio-integration-scan.md) | K | Yes | 0 | SAFE |
| 627 | [libfuzzer](plugins-testing-handbook-skills-skills-libfuzzer-scan.md) | trailofbits | Yes | 0 | SAFE |
| 628 | [lobster](lobster-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 629 | [local-falcon](local-falcon-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 630 | [logseq](logseq-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 631 | [m365-agents-dotnet](github-skills-m365-agents-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 632 | [marine-carbonate-chemistry](skills-marine-carbonate-chemistry-scan.md) | K | Yes | 0 | SAFE |
| 633 | [markdown-mermaid-writing](skills-markdown-mermaid-writing-scan.md) | K | Yes | 0 | SAFE |
| 634 | [market-research-reports](skills-market-research-reports-scan.md) | K | Yes | 0 | SAFE |
| 635 | [marketing-ideas](marketing-ideas-scan.md) | skills.sh | Yes | 0 | SAFE |
| 636 | [markitdown](skills-markitdown-scan.md) | K | Yes | 0 | SAFE |
| 637 | [matchms](skills-matchms-scan.md) | K | Yes | 0 | SAFE |
| 638 | [matlab](skills-matlab-scan.md) | K | Yes | 0 | SAFE |
| 639 | [matplotlib](skills-matplotlib-scan.md) | K | Yes | 0 | SAFE |
| 640 | [mcp-builder](github-skills-mcp-builder-scan.md) | microsoft | Yes | 0 | SAFE |
| 641 | [mcp-builder](mcp-builder-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 642 | [mcp-builder](skills-mcp-builder-scan.md) | anthropic | Yes | 0 | SAFE |
| 643 | [medchem](skills-medchem-scan.md) | K | Yes | 0 | SAFE |
| 644 | [memory-setup](memory-setup-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 645 | [mermaid-diagrams](mermaid-diagrams-scan.md) | skills.sh | Yes | 0 | SAFE |
| 646 | [microsoft-azure-webjobs-extensions-authentication-events-dotnet](github-skills-microsoft-azure-webjobs-extensions-authentication-events-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 647 | [modern-python](plugins-modern-python-skills-modern-python-scan.md) | trailofbits | Yes | 0 | SAFE |
| 648 | [molecular-dynamics](skills-molecular-dynamics-scan.md) | K | Yes | 0 | SAFE |
| 649 | [molfeat](skills-molfeat-scan.md) | K | Yes | 0 | SAFE |
| 650 | [molt-identity](molt-identity-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 651 | [moltbot-best-practices](moltbot-best-practices-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 652 | [native-data-fetching](native-data-fetching-scan.md) | skills.sh | Yes | 0 | SAFE |
| 653 | [networkx](skills-networkx-scan.md) | K | Yes | 0 | SAFE |
| 654 | [neurokit2](skills-neurokit2-scan.md) | K | Yes | 0 | SAFE |
| 655 | [neuropixels-analysis](skills-neuropixels-analysis-scan.md) | K | Yes | 0 | SAFE |
| 656 | [next-best-practices](next-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 657 | [nextjs-expert](nextjs-expert-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 658 | [nmrglue](skills-nmrglue-scan.md) | K | Yes | 0 | SAFE |
| 659 | [nuxt](nuxt-scan.md) | skills.sh | Yes | 0 | SAFE |
| 660 | [nwb-conversion](skills-nwb-conversion-scan.md) | K | Yes | 0 | SAFE |
| 661 | [obsidian-bases](skills-obsidian-bases-scan.md) | kepano | Yes | 0 | SAFE |
| 662 | [obsidian-markdown](skills-obsidian-markdown-scan.md) | kepano | Yes | 0 | SAFE |
| 663 | [obsidian-tasks](obsidian-tasks-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 664 | [onboarding-cro](onboarding-cro-scan.md) | skills.sh | Yes | 0 | SAFE |
| 665 | [onekgpd](skills-onekgpd-scan.md) | K | Yes | 0 | SAFE |
| 666 | [openclaw](comprehensive-skill-for-installing%2C-configuring%2C-and-managing-the-openclaw-ecosystem-gateway%2C-channels%2C-models%2C-automation%2C-nodes%2C-and-deployment-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 667 | [opencode-controller](opencode-controller-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 668 | [openpiv](skills-openpiv-scan.md) | K | Yes | 0 | SAFE |
| 669 | [opentrons-integration](skills-opentrons-integration-scan.md) | K | Yes | 0 | SAFE |
| 670 | [optimize-for-gpu](skills-optimize-for-gpu-scan.md) | K | Yes | 0 | SAFE |
| 671 | [pacsomatic](skills-pacsomatic-scan.md) | K | Yes | 0 | SAFE |
| 672 | [page-cro](page-cro-scan.md) | skills.sh | Yes | 0 | SAFE |
| 673 | [paid-ads](paid-ads-scan.md) | skills.sh | Yes | 0 | SAFE |
| 674 | [paperzilla](skills-paperzilla-scan.md) | K | Yes | 0 | SAFE |
| 675 | [parallel-web](skills-parallel-web-scan.md) | K | Yes | 0 | SAFE |
| 676 | [pathml](skills-pathml-scan.md) | K | Yes | 0 | SAFE |
| 677 | [pathway-enrichment](skills-pathway-enrichment-scan.md) | K | Yes | 0 | SAFE |
| 678 | [paywall-upgrade-cro](paywall-upgrade-cro-scan.md) | skills.sh | Yes | 0 | SAFE |
| 679 | [pdd](pdd-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 680 | [pdf](pdf-scan.md) | anthropic | Yes | 0 | SAFE |
| 681 | [pdf](skills-pdf-scan.md) | anthropic | Yes | 0 | SAFE |
| 682 | [peer-review](skills-peer-review-scan.md) | K | Yes | 0 | SAFE |
| 683 | [pennylane](skills-pennylane-scan.md) | K | Yes | 0 | SAFE |
| 684 | [phylogenetics](skills-phylogenetics-scan.md) | K | Yes | 0 | SAFE |
| 685 | [pkpd-modeling](skills-pkpd-modeling-scan.md) | K | Yes | 0 | SAFE |
| 686 | [podcast-generation](github-skills-podcast-generation-scan.md) | microsoft | Yes | 0 | SAFE |
| 687 | [polars](skills-polars-scan.md) | K | Yes | 0 | SAFE |
| 688 | [polars-bio](skills-polars-bio-scan.md) | K | Yes | 0 | SAFE |
| 689 | [pptx](pptx-scan.md) | anthropic | Yes | 0 | SAFE |
| 690 | [pptx](skills-pptx-scan.md) | anthropic | Yes | 0 | SAFE |
| 691 | [preview-markdown](preview-markdown-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 692 | [pricing-strategy](pricing-strategy-scan.md) | skills.sh | Yes | 0 | SAFE |
| 693 | [primekg](skills-primekg-scan.md) | K | Yes | 0 | SAFE |
| 694 | [primer-design](skills-primer-design-scan.md) | K | Yes | 0 | SAFE |
| 695 | [programmatic-seo](programmatic-seo-scan.md) | skills.sh | Yes | 0 | SAFE |
| 696 | [property-based-testing](plugins-property-based-testing-skills-property-based-testing-scan.md) | trailofbits | Yes | 0 | SAFE |
| 697 | [pufferlib](skills-pufferlib-scan.md) | K | Yes | 0 | SAFE |
| 698 | [pybamm](skills-pybamm-scan.md) | K | Yes | 0 | SAFE |
| 699 | [pycalphad](skills-pycalphad-scan.md) | K | Yes | 0 | SAFE |
| 700 | [pydantic-models-py](github-skills-pydantic-models-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 701 | [pydeseq2](skills-pydeseq2-scan.md) | K | Yes | 0 | SAFE |
| 702 | [pydicom](skills-pydicom-scan.md) | K | Yes | 0 | SAFE |
| 703 | [pylabrobot](skills-pylabrobot-scan.md) | K | Yes | 0 | SAFE |
| 704 | [pymatgen](skills-pymatgen-scan.md) | K | Yes | 0 | SAFE |
| 705 | [pymc](skills-pymc-scan.md) | K | Yes | 0 | SAFE |
| 706 | [pymoo](skills-pymoo-scan.md) | K | Yes | 0 | SAFE |
| 707 | [pyopenms](skills-pyopenms-scan.md) | K | Yes | 0 | SAFE |
| 708 | [pysam](skills-pysam-scan.md) | K | Yes | 0 | SAFE |
| 709 | [pytdc](skills-pytdc-scan.md) | K | Yes | 0 | SAFE |
| 710 | [pyzotero](skills-pyzotero-scan.md) | K | Yes | 0 | SAFE |
| 711 | [qiskit](skills-qiskit-scan.md) | K | Yes | 0 | SAFE |
| 712 | [qutip](skills-qutip-scan.md) | K | Yes | 0 | SAFE |
| 713 | [railway](railway-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 714 | [rdkit](skills-rdkit-scan.md) | K | Yes | 0 | SAFE |
| 715 | [react-expert](react-expert-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 716 | [react-flow-node-ts](github-skills-react-flow-node-ts-scan.md) | microsoft | Yes | 0 | SAFE |
| 717 | [react-native-best-practices](react-native-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 718 | [readwise-mcp](readwise-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 719 | [receiving-code-review](receiving-code-review-scan.md) | skills.sh | Yes | 0 | SAFE |
| 720 | [referral-program](referral-program-scan.md) | skills.sh | Yes | 0 | SAFE |
| 721 | [relion](skills-relion-scan.md) | K | Yes | 0 | SAFE |
| 722 | [relsa-severity-assessment](skills-relsa-severity-assessment-scan.md) | K | Yes | 0 | SAFE |
| 723 | [remotion-best-practices](remotion-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 724 | [remotion-video-toolkit](remotion-video-toolkit-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 725 | [requesting-code-review](requesting-code-review-scan.md) | skills.sh | Yes | 0 | SAFE |
| 726 | [research-grants](skills-research-grants-scan.md) | K | Yes | 0 | SAFE |
| 727 | [research-paper-writer](research-paper-writer-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 728 | [resume-builder](resume-builder-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 729 | [rowan](skills-rowan-scan.md) | K | Yes | 0 | SAFE |
| 730 | [rssaurus-cli](rssaurus-agent-friendly-rss-feed-reader-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 731 | [sarif-parsing](plugins-static-analysis-skills-sarif-parsing-scan.md) | trailofbits | Yes | 0 | SAFE |
| 732 | [scanpy](skills-scanpy-scan.md) | K | Yes | 0 | SAFE |
| 733 | [schema-markup](schema-markup-scan.md) | skills.sh | Yes | 0 | SAFE |
| 734 | [scholar-evaluation](skills-scholar-evaluation-scan.md) | K | Yes | 0 | SAFE |
| 735 | [scientific-brainstorming](skills-scientific-brainstorming-scan.md) | K | Yes | 0 | SAFE |
| 736 | [scientific-critical-thinking](skills-scientific-critical-thinking-scan.md) | K | Yes | 0 | SAFE |
| 737 | [scientific-visualization](skills-scientific-visualization-scan.md) | K | Yes | 0 | SAFE |
| 738 | [scientific-writing](skills-scientific-writing-scan.md) | K | Yes | 0 | SAFE |
| 739 | [scikit-bio](skills-scikit-bio-scan.md) | K | Yes | 0 | SAFE |
| 740 | [scikit-learn](skills-scikit-learn-scan.md) | K | Yes | 0 | SAFE |
| 741 | [scikit-survival](skills-scikit-survival-scan.md) | K | Yes | 0 | SAFE |
| 742 | [scvelo](skills-scvelo-scan.md) | K | Yes | 0 | SAFE |
| 743 | [scvi-tools](skills-scvi-tools-scan.md) | K | Yes | 0 | SAFE |
| 744 | [seaborn](skills-seaborn-scan.md) | K | Yes | 0 | SAFE |
| 745 | [secure-workflow-guide](plugins-building-secure-contracts-skills-secure-workflow-guide-scan.md) | trailofbits | Yes | 0 | SAFE |
| 746 | [security-auditor](security-auditor-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 747 | [semgrep](plugins-static-analysis-skills-semgrep-scan.md) | trailofbits | Yes | 0 | SAFE |
| 748 | [semgrep](plugins-testing-handbook-skills-skills-semgrep-scan.md) | trailofbits | Yes | 0 | SAFE |
| 749 | [semgrep-rule-creator](plugins-semgrep-rule-creator-skills-semgrep-rule-creator-scan.md) | trailofbits | Yes | 0 | SAFE |
| 750 | [semgrep-rule-variant-creator](plugins-semgrep-rule-variant-creator-skills-semgrep-rule-variant-creator-scan.md) | trailofbits | Yes | 0 | SAFE |
| 751 | [senior-architect](senior-architect-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 752 | [senior-devops](senior-devops-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 753 | [shap](skills-shap-scan.md) | K | Yes | 0 | SAFE |
| 754 | [sharp-edges](plugins-sharp-edges-skills-sharp-edges-scan.md) | trailofbits | Yes | 0 | SAFE |
| 755 | [ship-learn-next](ship-learn-next-scan.md) | skills.sh | Yes | 0 | SAFE |
| 756 | [signup-flow-cro](signup-flow-cro-scan.md) | skills.sh | Yes | 0 | SAFE |
| 757 | [simpy](skills-simpy-scan.md) | K | Yes | 0 | SAFE |
| 758 | [skill-creator](github-skills-skill-creator-scan.md) | microsoft | Yes | 0 | SAFE |
| 759 | [skill-creator](jash-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 760 | [skill-creator](skill-creator-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 761 | [skill-creator](skills-skill-creator-scan.md) | anthropic | Yes | 0 | SAFE |
| 762 | [skill-scanner](ai-skillner-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 763 | [skill-scanner](skillner-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 764 | [slack-gif-creator](skills-slack-gif-creator-scan.md) | anthropic | Yes | 0 | SAFE |
| 765 | [slack-gif-creator](slack-gif-creator-scan.md) | anthropic | Yes | 0 | SAFE |
| 766 | [social-content](social-content-scan.md) | skills.sh | Yes | 0 | SAFE |
| 767 | [solana-vulnerability-scanner](plugins-building-secure-contracts-skills-solana-vulnerabilityner-scan.md) | trailofbits | Yes | 0 | SAFE |
| 768 | [soulcraft](soulcraft-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 769 | [spring-boot-engineer](spring-boot-engineer-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 770 | [sql-pro](sql-pro-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 771 | [ssh-essentials](ssh-essentials-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 772 | [stable-baselines3](skills-stable-baselines3-scan.md) | K | Yes | 0 | SAFE |
| 773 | [statistical-analysis](skills-statistical-analysis-scan.md) | K | Yes | 0 | SAFE |
| 774 | [statsmodels](skills-statsmodels-scan.md) | K | Yes | 0 | SAFE |
| 775 | [stock-market-pro](stock-market-pro-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 776 | [substrate-vulnerability-scanner](plugins-building-secure-contracts-skills-substrate-vulnerabilityner-scan.md) | trailofbits | Yes | 0 | SAFE |
| 777 | [supabase-postgres-best-practices](supabase-postgres-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 778 | [swift-expert](swift-expert-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 779 | [sympy](skills-sympy-scan.md) | K | Yes | 0 | SAFE |
| 780 | [system_monitor](system-monitor-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 781 | [systematic-debugging](systematic-debugging-scan.md) | skills.sh | Yes | 0 | SAFE |
| 782 | [tailwind-design-system](tailwind-design-system-scan.md) | skills.sh | Yes | 0 | SAFE |
| 783 | [tamarind](skills-tamarind-scan.md) | K | Yes | 0 | SAFE |
| 784 | [template-skill](template-scan.md) | anthropic | Yes | 0 | SAFE |
| 785 | [template-skill](template-skill-scan.md) | anthropic | Yes | 0 | SAFE |
| 786 | [test-driven-development](test-driven-development-scan.md) | skills.sh | Yes | 0 | SAFE |
| 787 | [test-specialist](test-specialist-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 788 | [theme-factory](skills-theme-factory-scan.md) | anthropic | Yes | 0 | SAFE |
| 789 | [theme-factory](theme-factory-scan.md) | anthropic | Yes | 0 | SAFE |
| 790 | [tiledbvcf](skills-tiledbvcf-scan.md) | K | Yes | 0 | SAFE |
| 791 | [token-integration-analyzer](plugins-building-secure-contracts-skills-token-integration-analyzer-scan.md) | trailofbits | Yes | 0 | SAFE |
| 792 | [ton-vulnerability-scanner](plugins-building-secure-contracts-skills-ton-vulnerabilityner-scan.md) | trailofbits | Yes | 0 | SAFE |
| 793 | [transcribe](transcribe-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 794 | [treatment-plans](skills-treatment-plans-scan.md) | K | Yes | 0 | SAFE |
| 795 | [trmnl](trmnl-display-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 796 | [turborepo](turborepo-scan.md) | skills.sh | Yes | 0 | SAFE |
| 797 | [ui-ux-pro-max](ui-ux-pro-max-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 798 | [umap-learn](skills-umap-learn-scan.md) | K | Yes | 0 | SAFE |
| 799 | [uncertainty-and-units](skills-uncertainty-and-units-scan.md) | K | Yes | 0 | SAFE |
| 800 | [upgrading-expo](upgrading-expo-scan.md) | skills.sh | Yes | 0 | SAFE |
| 801 | [usfiscaldata](skills-usfiscaldata-scan.md) | K | Yes | 0 | SAFE |
| 802 | [vaex](skills-vaex-scan.md) | K | Yes | 0 | SAFE |
| 803 | [venue-templates](skills-venue-templates-scan.md) | K | Yes | 0 | SAFE |
| 804 | [vercel-composition-patterns](vercel-composition-patterns-scan.md) | skills.sh | Yes | 0 | SAFE |
| 805 | [vercel-react-best-practices](vercel-react-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 806 | [vercel-react-native-skills](vercel-react-native-skills-scan.md) | skills.sh | Yes | 0 | SAFE |
| 807 | [verification-before-completion](verification-before-completion-scan.md) | skills.sh | Yes | 0 | SAFE |
| 808 | [vue](vue-scan.md) | skills.sh | Yes | 0 | SAFE |
| 809 | [vue-best-practices](vue-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 810 | [web-artifacts-builder](skills-web-artifacts-builder-scan.md) | anthropic | Yes | 0 | SAFE |
| 811 | [web-artifacts-builder](web-artifacts-builder-scan.md) | anthropic | Yes | 0 | SAFE |
| 812 | [web-perf](skills-web-perf-scan.md) | cloudflare | Yes | 0 | SAFE |
| 813 | [webapp-testing](skills-webapp-testing-scan.md) | anthropic | Yes | 0 | SAFE |
| 814 | [what-if-oracle](skills-what-if-oracle-scan.md) | K | Yes | 0 | SAFE |
| 815 | [wordpress-pro](wordpress-pro-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 816 | [wrangler](skills-wrangler-scan.md) | cloudflare | Yes | 0 | SAFE |
| 817 | [wycheproof](plugins-testing-handbook-skills-skills-wycheproof-scan.md) | trailofbits | Yes | 0 | SAFE |
| 818 | [x-trends](x-trends-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 819 | [xlsx](skills-xlsx-scan.md) | anthropic | Yes | 0 | SAFE |
| 820 | [xlsx](xlsx-scan.md) | anthropic | Yes | 0 | SAFE |
| 821 | [youtube-api](youtube-api-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 822 | [youtube-music-cast](youtube-music-cast-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 823 | [youtube-search](youtube-search-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 824 | [yt-video-downloader](youtube-video-downloader-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 825 | [zarr-python](skills-zarr-python-scan.md) | K | Yes | 0 | SAFE |
| 826 | [zotero](zotero-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 827 | [zustand-store-ts](github-skills-zustand-store-ts-scan.md) | microsoft | Yes | 0 | SAFE |

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
- 13c-metabolic-flux
- Content ID Guide
- Search Realtime Information
- ab-test-setup
- academic-deep-research
- actual-budget
- address-sanitizer
- aeon
- agent-browser
- agent-builder
- agent-framework-azure-ai-py
- agent-md-refactor
- agenticflow-skills
- agents-sdk
- airc
- algorand-vulnerability-scanner
- algorithmic-art
- analytical-method-validation
- analytics-tracking
- anndata
- answeroverflow
- anterior-cingulate-memory
- api-designer
- arbor
- arboreto
- artifacts-builder
- ask-questions-if-underspecified
- astropy
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
- benchling-integration
- bgpt-paper-search
- bioservices
- brainstorming
- brand-guidelines
- brand-guidelines
- building-ai-agent-on-cloudflare
- building-mcp-server-on-cloudflare
- building-native-ui
- bulk-rnaseq
- burpsuite-project-parser
- cairo-vulnerability-scanner
- cantera
- cargo-fuzz
- cellprofiler
- cellxgene-census
- chirp
- cirq
- claude-in-chrome-troubleshooting
- clawdbot-cost-tracker
- clawdbot-self-security-audit
- clawdefender
- clawdex
- clinical-decision-support
- clinical-reports
- cobrapy
- code-maturity-assessor
- codeql
- coding-agent
- commit-work
- competitor-alternatives
- consciousness-council
- constant-time-analysis
- copy-editing
- copywriting
- cosmos-vulnerability-scanner
- coverage-analysis
- create-auth-skill
- create-auth-skill
- cron-mastery
- daily-meeting-update
- dask
- database-lookup
- datalad
- datamol
- decision-trees
- deepchem
- deepspot-m
- deeptools
- depmap
- dhdna-profiler
- diffdock
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
- etetoolkit
- exa-search
- exa-web-search-free
- executing-plans
- experimental-design
- exploratory-data-analysis
- expo-api-routes
- expo-deployment
- expo-dev-client
- expo-tailwind-setup
- ez-cronjob
- fastapi-router-py
- faster-whisper
- feast
- fictiv
- find-skills
- finishing-a-development-branch
- fix-review
- flowio
- flowkit
- fluidsim
- folklore-variant-evidence
- form-cro
- foundry-iq-py
- free-tool-strategy
- frontend-design
- frontend-design
- fuzzing-obstacles
- gemini-nano-banana-pro-portraits
- geniml
- geopandas
- get-available-resources
- ginkgo-cloud-lab
- github-issue-creator
- gitlab-cli-skills
- google-gemini-media
- google-imagen-3-hyperrealistic-landscape
- gtars
- guidelines-advisor
- hackernews
- harness-writing
- hf-mcp
- histolab
- hosted-agents-v2-py
- hugging-face-trackio
- humanize
- humanize-ai
- hybrid-memory
- hypogenic
- hypothesis-generation
- insecure-defaults
- insula-memory
- internal-comms
- internal-comms
- interpreting-culture-index
- json-canvas
- juicebox-v5
- lab-hardware-cad
- labarchive-integration
- lamindb
- language-learning
- latchbio-integration
- libfuzzer
- lobster
- local-falcon
- logseq
- m365-agents-dotnet
- marine-carbonate-chemistry
- markdown-mermaid-writing
- market-research-reports
- marketing-ideas
- markitdown
- matchms
- matlab
- matplotlib
- mcp-builder
- mcp-builder
- mcp-builder
- medchem
- memory-setup
- mermaid-diagrams
- microsoft-azure-webjobs-extensions-authentication-events-dotnet
- modern-python
- molecular-dynamics
- molfeat
- molt-identity
- moltbot-best-practices
- native-data-fetching
- networkx
- neurokit2
- neuropixels-analysis
- next-best-practices
- nextjs-expert
- nmrglue
- nuxt
- nwb-conversion
- obsidian-bases
- obsidian-markdown
- obsidian-tasks
- onboarding-cro
- onekgpd
- openclaw
- opencode-controller
- openpiv
- opentrons-integration
- optimize-for-gpu
- pacsomatic
- page-cro
- paid-ads
- paperzilla
- parallel-web
- pathml
- pathway-enrichment
- paywall-upgrade-cro
- pdd
- pdf
- pdf
- peer-review
- pennylane
- phylogenetics
- pkpd-modeling
- podcast-generation
- polars
- polars-bio
- pptx
- pptx
- preview-markdown
- pricing-strategy
- primekg
- primer-design
- programmatic-seo
- property-based-testing
- pufferlib
- pybamm
- pycalphad
- pydantic-models-py
- pydeseq2
- pydicom
- pylabrobot
- pymatgen
- pymc
- pymoo
- pyopenms
- pysam
- pytdc
- pyzotero
- qiskit
- qutip
- railway
- rdkit
- react-expert
- react-flow-node-ts
- react-native-best-practices
- readwise-mcp
- receiving-code-review
- referral-program
- relion
- relsa-severity-assessment
- remotion-best-practices
- remotion-video-toolkit
- requesting-code-review
- research-grants
- research-paper-writer
- resume-builder
- rowan
- rssaurus-cli
- sarif-parsing
- scanpy
- schema-markup
- scholar-evaluation
- scientific-brainstorming
- scientific-critical-thinking
- scientific-visualization
- scientific-writing
- scikit-bio
- scikit-learn
- scikit-survival
- scvelo
- scvi-tools
- seaborn
- secure-workflow-guide
- security-auditor
- semgrep
- semgrep
- semgrep-rule-creator
- semgrep-rule-variant-creator
- senior-architect
- senior-devops
- shap
- sharp-edges
- ship-learn-next
- signup-flow-cro
- simpy
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
- stable-baselines3
- statistical-analysis
- statsmodels
- stock-market-pro
- substrate-vulnerability-scanner
- supabase-postgres-best-practices
- swift-expert
- sympy
- system_monitor
- systematic-debugging
- tailwind-design-system
- tamarind
- template-skill
- template-skill
- test-driven-development
- test-specialist
- theme-factory
- theme-factory
- tiledbvcf
- token-integration-analyzer
- ton-vulnerability-scanner
- transcribe
- treatment-plans
- trmnl
- turborepo
- ui-ux-pro-max
- umap-learn
- uncertainty-and-units
- upgrading-expo
- usfiscaldata
- vaex
- venue-templates
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
- what-if-oracle
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
- zarr-python
- zotero
- zustand-store-ts

---

## Methodology

- **Scanner:** cisco-ai-skill-scanner 2.3.1
- **Analyzers:** behavioral_analyzer, bytecode, correlation, llm_analyzer, meta_analyzer, pipeline, static_analyzer, trigger_analyzer
- **Scan Date:** 2026-10-21T21:38:07.738370

### Limitations

- VirusTotal binary scanning not used (requires API key)
- No runtime verification - static and semantic analysis only
