# AI Agent Skills Security Scan Report

**Generated:** 2026-02-05T10:43:55.504449
**Scanner:** cisco-ai-skill-scanner
**Analyzers:** behavioral, llm, meta, static, trigger

---

## Executive Summary

| Metric | Count |
|--------|-------|
| Total Skills Scanned | 614 |
| Safe Skills | 482 (79%) |
| Skills with Issues | 132 (21%) |
| Scan Errors | 0 |

### Severity Breakdown

| Severity | Count |
|----------|-------|
| CRITICAL | 361 |
| HIGH | 181 |
| MEDIUM | 611 |
| LOW | 463 |
| **Total Findings** | **1616** |

### Findings by Category

| Category | Count |
|----------|-------|
| policy_violation | 446 |
| command_injection | 327 |
| data_exfiltration | 317 |
| transitive_trust_abuse | 169 |
| unauthorized_tool_use | 88 |
| tool_chaining_abuse | 86 |
| hardcoded_secrets | 78 |
| skill_discovery_abuse | 37 |
| prompt_injection | 24 |
| social_engineering | 24 |
| resource_abuse | 8 |
| autonomy_abuse | 7 |
| obfuscation | 5 |

---

## Results by Skill

| # | Skill | Source | Safe | Findings | Max Severity |
|---|-------|--------|------|----------|--------------|
| 1 | [hugging-face-evaluation](skills-hugging-face-evaluation-scan.md) | huggingface | **No** | 113 | **CRITICAL** |
| 2 | [hugging-face-datasets](skills-hugging-face-datasets-scan.md) | huggingface | **No** | 77 | **CRITICAL** |
| 3 | [zoho-email](zoho-email-integration-scan.md) | clawhub.ai | **No** | 69 | **CRITICAL** |
| 4 | [hugging-face-paper-publisher](skills-hugging-face-paper-publisher-scan.md) | huggingface | **No** | 65 | **CRITICAL** |
| 5 | [finance-news](finance-news-briefings-scan.md) | clawhub.ai | **No** | 43 | **CRITICAL** |
| 6 | [clawdefender](clawdefender-openclaw-security-prompt-injection%2C-rogue-skills-etc-scan.md) | clawhub.ai | **No** | 37 | **CRITICAL** |
| 7 | [aws-cdk-development](plugins-aws-cdk-skills-aws-cdk-development-scan.md) | zxkane | **No** | 31 | **CRITICAL** |
| 8 | [qa-test-planner](qa-test-planner-scan.md) | skills.sh | **No** | 19 | **CRITICAL** |
| 9 | [skill-scanner](ai-skill-scanner-scan.md) | clawhub.ai | **No** | 19 | **CRITICAL** |
| 10 | [yara-rule-authoring](plugins-yara-authoring-skills-yara-rule-authoring-scan.md) | trailofbits | **No** | 19 | **CRITICAL** |
| 11 | [zotero](zotero-scan.md) | clawhub.ai | **No** | 19 | **CRITICAL** |
| 12 | [notebooklm](notebooklm-scan.md) | clawhub.ai | **No** | 17 | **CRITICAL** |
| 13 | [hugging-face-model-trainer](skills-hugging-face-model-trainer-scan.md) | huggingface | **No** | 16 | **HIGH** |
| 14 | [aws-agentic-ai](plugins-aws-agentic-ai-skills-aws-agentic-ai-scan.md) | zxkane | **No** | 15 | **CRITICAL** |
| 15 | [phone-agent](phone-voice-agent-scan.md) | clawhub.ai | **No** | 15 | **CRITICAL** |
| 16 | [hugging-face-tool-builder](skills-hugging-face-tool-builder-scan.md) | huggingface | **No** | 13 | **CRITICAL** |
| 17 | [slack](slack-scan.md) | clawhub.ai | Yes | 13 | MEDIUM |
| 18 | [multi-llm](multi-llm-fallback-scan.md) | clawhub.ai | **No** | 12 | **CRITICAL** |
| 19 | [openclaw-optimizer](startclaw-optimizer-scan.md) | clawhub.ai | **No** | 12 | **HIGH** |
| 20 | [earnings-calendar](earnings-calendar-scan.md) | clawhub.ai | **No** | 11 | **CRITICAL** |
| 21 | [clawmail](clawmail-scan.md) | clawhub.ai | **No** | 10 | **CRITICAL** |
| 22 | [constant-time-testing](plugins-testing-handbook-skills-skills-constant-time-testing-scan.md) | trailofbits | **No** | 10 | **CRITICAL** |
| 23 | [semgrep](plugins-static-analysis-skills-semgrep-scan.md) | trailofbits | Yes | 10 | MEDIUM |
| 24 | [swarmmarket](swarmmarket-skill%2C-make-money-with-your-agents-scan.md) | clawhub.ai | **No** | 10 | **CRITICAL** |
| 25 | [technews](techmeme-news-scan.md) | clawhub.ai | **No** | 10 | **HIGH** |
| 26 | [video-agent](video-agent-scan.md) | clawhub.ai | **No** | 10 | **HIGH** |
| 27 | [gold_price_mcp](gold-price-mcp-scan.md) | clawhub.ai | **No** | 9 | **HIGH** |
| 28 | [kimi-integration](kimi-integration-scan.md) | clawhub.ai | **No** | 9 | **CRITICAL** |
| 29 | [reddit](reddit-scraper-scan.md) | clawhub.ai | **No** | 9 | **HIGH** |
| 30 | [agent-browser](agent-browser-scan.md) | clawhub.ai | **No** | 8 | **HIGH** |
| 31 | [browser-use](browser-use-scan.md) | skills.sh | **No** | 8 | **HIGH** |
| 32 | [crypto-gold-monitor](%E5%8A%A0%E5%AF%86%E8%B4%A7%E5%B8%81%E4%B8%8E%E8%B4%B5%E9%87%91%E5%B1%9E%E7%9B%91%E6%8E%A7-scan.md) | clawhub.ai | **No** | 8 | **CRITICAL** |
| 33 | [explorer](github-projects-explorer-scan.md) | clawhub.ai | **No** | 8 | **CRITICAL** |
| 34 | [foundry-iq-py](github-skills-foundry-iq-py-scan.md) | microsoft | **No** | 8 | **HIGH** |
| 35 | [preview-markdown](preview-markdown-scan.md) | clawhub.ai | **No** | 8 | **CRITICAL** |
| 36 | [querit-search](querit-search-scan.md) | clawhub.ai | **No** | 8 | **CRITICAL** |
| 37 | [update-plus](update-plus-scan.md) | clawhub.ai | **No** | 8 | **CRITICAL** |
| 38 | [atheris](plugins-testing-handbook-skills-skills-atheris-scan.md) | trailofbits | **No** | 7 | **CRITICAL** |
| 39 | [channel](wechat-oa-channel-scan.md) | clawhub.ai | **No** | 7 | **CRITICAL** |
| 40 | [clawdbot-self-security-audit](clawdbot-security-check-scan.md) | clawhub.ai | **No** | 7 | **CRITICAL** |
| 41 | [cryptocurrency-trader](cryptocurrency-trader-scan.md) | clawhub.ai | **No** | 7 | **HIGH** |
| 42 | [etf-assistant](etf%E6%8A%95%E8%B5%84%E5%8A%A9%E7%90%86-scan.md) | clawhub.ai | **No** | 7 | **CRITICAL** |
| 43 | [hugging-face-jobs](skills-hugging-face-jobs-scan.md) | huggingface | **No** | 7 | **HIGH** |
| 44 | [pipedrive](pipedrive-scan.md) | clawhub.ai | Yes | 7 | MEDIUM |
| 45 | [test-specialist](test-specialist-scan.md) | clawhub.ai | **No** | 7 | **CRITICAL** |
| 46 | [tokenguard](tokenguard-scan.md) | clawhub.ai | **No** | 7 | **HIGH** |
| 47 | [ABM Outbound](abm-outbound-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 48 | [Better Polymarket](polymarket-better-scan.md) | clawhub.ai | **No** | 6 | **HIGH** |
| 49 | [giphy-gif](giphy-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 50 | [home-assistant](home-assistant-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 51 | [semgrep-rule-creator](plugins-semgrep-rule-creator-skills-semgrep-rule-creator-scan.md) | trailofbits | Yes | 6 | MEDIUM |
| 52 | [stealth-browser](stealth-browser-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 53 | [tinyfish](tinyfish-web-agent-scan.md) | clawhub.ai | **No** | 6 | **HIGH** |
| 54 | [wallet-tracker](wallet-tracker-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 55 | [ClawGateSecure](claw-gate-secure-scan.md) | clawhub.ai | Yes | 5 | MEDIUM |
| 56 | [Job Search MCP](job-search-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 57 | [aflpp](plugins-testing-handbook-skills-skills-aflpp-scan.md) | trailofbits | **No** | 5 | **CRITICAL** |
| 58 | [agnxi-search](agent-skills-search-scan.md) | clawhub.ai | **No** | 5 | **HIGH** |
| 59 | [azure-eventhub-java](github-skills-azure-eventhub-java-scan.md) | microsoft | **No** | 5 | **CRITICAL** |
| 60 | [constant-time-analysis](plugins-constant-time-analysis-skills-constant-time-analysis-scan.md) | trailofbits | **No** | 5 | **CRITICAL** |
| 61 | [context-manager](smart-context-manager-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 62 | [gitclassic](gitclassic-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 63 | [kalshi](kalshi-scan.md) | clawhub.ai | **No** | 5 | **HIGH** |
| 64 | [libafl](plugins-testing-handbook-skills-skills-libafl-scan.md) | trailofbits | **No** | 5 | **CRITICAL** |
| 65 | [mersal](mersal-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 66 | [moltbook](moltbook-scan.md) | clawhub.ai | Yes | 5 | MEDIUM |
| 67 | [openwork](openwork-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 68 | [solana](solana-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 69 | [veo3-video-gen](veo-3-video-gen-gemini-api-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 70 | [voice-agent](voice-agent-scan.md) | clawhub.ai | **No** | 5 | **HIGH** |
| 71 | [x-api](x-api-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 72 | [apewisdom](apewisdom-reddit-scanner-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 73 | [api-gateway](api-gateway-scan.md) | clawhub.ai | Yes | 4 | MEDIUM |
| 74 | [canvas-design](skills-canvas-design-scan.md) | anthropic | Yes | 4 | MEDIUM |
| 75 | [domain-name-brainstormer](domain-name-brainstormer-scan.md) | skills.sh | Yes | 4 | MEDIUM |
| 76 | [ethereum-gas-tracker](ethereum-gas-tracker-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 77 | [finance](finance-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 78 | [firebase-apk-scanner](plugins-firebase-apk-scanner-skills-firebase-apk-scanner-scan.md) | trailofbits | **No** | 4 | **CRITICAL** |
| 79 | [glm-coding-agent](glm-coding-agent-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 80 | [humanize-ai](humanize-ai-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 81 | [humanize-ai-text](humanize-ai-text-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 82 | [humanizer](humanizer-scan.md) | skills.sh | Yes | 4 | MEDIUM |
| 83 | [imap-smtp-email](imap-smtp-email-scan.md) | clawhub.ai | Yes | 4 | MEDIUM |
| 84 | [insider-wallets-finder](insider-wallets-finder-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 85 | [libfuzzer](plugins-testing-handbook-skills-skills-libfuzzer-scan.md) | trailofbits | **No** | 4 | **CRITICAL** |
| 86 | [phantom](phantom-wallet-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 87 | [sarif-parsing](plugins-static-analysis-skills-sarif-parsing-scan.md) | trailofbits | **No** | 4 | **HIGH** |
| 88 | [security-auditor](security-auditor-scan.md) | clawhub.ai | Yes | 4 | MEDIUM |
| 89 | [send-email](send-email-scan.md) | clawhub.ai | Yes | 4 | MEDIUM |
| 90 | [session-handoff](session-handoff-scan.md) | skills.sh | **No** | 4 | **HIGH** |
| 91 | [simmer](simmer-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 92 | [smtp-send](smtp-send-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 93 | [supermemory](supermemory-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 94 | [tencent-map](%E8%85%BE%E8%AE%AF%E5%9C%B0%E5%9B%BEapi%E8%B0%83%E7%94%A8%E6%8A%80%E8%83%BD-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 95 | [youtube-summarize](youtube-video-summarizer-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 96 | [youtube-transcript](youtube-transcript-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 97 | [Docker Pro Diagnostic](docker-diag-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 98 | [MockAPI - Instant REST API from JSON](mockapi-instant-rest-api-from-json-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 99 | [ai-pdf-builder](ai-pdf-builder-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 100 | [amap](amap-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 101 | [azure-mgmt-fabric-py](github-skills-azure-mgmt-fabric-py-scan.md) | microsoft | **No** | 3 | **HIGH** |
| 102 | [baidu-map](%E8%B0%83%E7%94%A8%E7%99%BE%E5%BA%A6%E5%9C%B0%E5%9B%BEapi%E5%8A%9F%E8%83%BD-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 103 | [clawdbot-cost-tracker](cost-tracking-for-models-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 104 | [clickup](clickup-skill-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 105 | [cloudflare](skills-cloudflare-scan.md) | cloudflare | Yes | 3 | MEDIUM |
| 106 | [decision-trees](decision-trees-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 107 | [durable-objects](skills-durable-objects-scan.md) | cloudflare | Yes | 3 | MEDIUM |
| 108 | [ez-cronjob](ez-cronjob-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 109 | [faster-whisper](faster-whisper-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 110 | [gemini](gemini-scan.md) | skills.sh | **No** | 3 | **HIGH** |
| 111 | [gemini-nano-banana-pro-portraits](gemini-nano-banana-pro-portraits-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 112 | [google-workspace](google-workspace-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 113 | [hyperliquid](hyperliquid-cli-with-hip3-support-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 114 | [job-auto-apply](job-auto-apply-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 115 | [moltbot-best-practices](moltbot-best-practices-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 116 | [omni-stories](omni-stories-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 117 | [playwright-skill](skills-playwright-skill-scan.md) | lackeyjb | Yes | 3 | MEDIUM |
| 118 | [save-money](save-money-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 119 | [searxng](searxng-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 120 | [skill-scanner](skill-scanner-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 121 | [testing-handbook-generator](plugins-testing-handbook-skills-skills-testing-handbook-generator-scan.md) | trailofbits | Yes | 3 | MEDIUM |
| 122 | [trmnl](trmnl-display-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 123 | [ui-ux-pro-max](ui-ux-pro-max-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 124 | [web-design-guidelines](web-design-guidelines-scan.md) | skills.sh | **No** | 3 | **HIGH** |
| 125 | [windows-control](windows-control-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 126 | [wrangler](skills-wrangler-scan.md) | cloudflare | **No** | 3 | **CRITICAL** |
| 127 | [Agent Browser](browser-automation-scan.md) | clawhub.ai | Yes | 2 | LOW |
| 128 | [Agent Wallet](agent-wallet-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 129 | [ClawDoro](clawdoro-scan.md) | clawhub.ai | Yes | 2 | LOW |
| 130 | [Content ID Guide](content-id-guide-scan.md) | clawhub.ai | Yes | 2 | LOW |
| 131 | [Meta Tags - SEO Tag Generator](meta-tags-seo-tag-generator-scan.md) | clawhub.ai | Yes | 2 | LOW |
| 132 | [MoltMedia](moltmedia-scan.md) | clawhub.ai | Yes | 2 | LOW |
| 133 | [Search Realtime Information](realtime-web-search-scan.md) | clawhub.ai | Yes | 2 | LOW |
| 134 | [YT Meta - YouTube Metadata Extractor](yt-meta-youtube-metadata-extractor-scan.md) | clawhub.ai | Yes | 2 | LOW |
| 135 | [activecampaign](activecampaign-crm-scan.md) | clawhub.ai | **No** | 2 | **CRITICAL** |
| 136 | [activecampaign](baby-connect-logger-scan.md) | clawhub.ai | **No** | 2 | **CRITICAL** |
| 137 | [aegis-security](aegis-security-scan.md) | clawhub.ai | **No** | 2 | **CRITICAL** |
| 138 | [agent-task-manager](agent-task-manager-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 139 | [ansible](ansible-scan.md) | clawhub.ai | **No** | 2 | **CRITICAL** |
| 140 | [answeroverflow](answer-overflow-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 141 | [atxp](atxp-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 142 | [azure-ai-contentunderstanding-py](github-skills-azure-ai-contentunderstanding-py-scan.md) | microsoft | Yes | 2 | MEDIUM |
| 143 | [azure-ai-document-intelligence-dotnet](github-skills-azure-ai-document-intelligence-dotnet-scan.md) | microsoft | Yes | 2 | MEDIUM |
| 144 | [azure-ai-evaluation-py](github-skills-azure-ai-evaluation-py-scan.md) | microsoft | Yes | 2 | MEDIUM |
| 145 | [azure-monitor-opentelemetry-exporter-py](github-skills-azure-monitor-opentelemetry-exporter-py-scan.md) | microsoft | Yes | 2 | MEDIUM |
| 146 | [azure-security-keyvault-keys-dotnet](github-skills-azure-security-keyvault-keys-dotnet-scan.md) | microsoft | **No** | 2 | **CRITICAL** |
| 147 | [azure-security-keyvault-keys-java](github-skills-azure-security-keyvault-keys-java-scan.md) | microsoft | **No** | 2 | **CRITICAL** |
| 148 | [base-trader](base-trader-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 149 | [botcoin-miner](botcoin-miner-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 150 | [browse](browserbase-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 151 | [building-ai-agent-on-cloudflare](skills-building-ai-agent-on-cloudflare-scan.md) | cloudflare | **No** | 2 | **CRITICAL** |
| 152 | [building-mcp-server-on-cloudflare](skills-building-mcp-server-on-cloudflare-scan.md) | cloudflare | **No** | 2 | **CRITICAL** |
| 153 | [canvas-design](canvas-design-scan.md) | anthropic | Yes | 2 | MEDIUM |
| 154 | [cargo-fuzz](plugins-testing-handbook-skills-skills-cargo-fuzz-scan.md) | trailofbits | **No** | 2 | **CRITICAL** |
| 155 | [chart-image](chart-image-generator-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 156 | [clawdbot-security](clawdbot-security-audit-scan.md) | clawhub.ai | **No** | 2 | **CRITICAL** |
| 157 | [clawhub](clawhub-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 158 | [coding-agent](multi-coding-agent-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 159 | [cold-email](machfive-cold-email-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 160 | [create-auth-skill](create-auth-skill-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 161 | [ctxly](mymemory.bot-scan.md) | clawhub.ai | **No** | 2 | **CRITICAL** |
| 162 | [daily-meeting-update](daily-meeting-update-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 163 | [dependency-updater](dependency-updater-scan.md) | skills.sh | **No** | 2 | **HIGH** |
| 164 | [dev-browser](skills-dev-browser-scan.md) | sawyerhood | Yes | 2 | MEDIUM |
| 165 | [diff-summary](git-diff-summarizer-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 166 | [doc-coauthoring](skills-doc-coauthoring-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 167 | [expo-api-routes](expo-api-routes-scan.md) | skills.sh | **No** | 2 | **CRITICAL** |
| 168 | [ez-google](ez-google-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 169 | [ffuf-web-fuzzing](ffuf-skill-scan.md) | jthack | Yes | 2 | MEDIUM |
| 170 | [free-tool-strategy](free-tool-strategy-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 171 | [fuzzing-dictionary](plugins-testing-handbook-skills-skills-fuzzing-dictionary-scan.md) | trailofbits | **No** | 2 | **CRITICAL** |
| 172 | [gcloud](google-cloud-platform-scan.md) | clawhub.ai | **No** | 2 | **CRITICAL** |
| 173 | [google](google-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 174 | [google-imagen-3-hyperrealistic-landscape](google-imagen-3-%E8%B6%85%E5%86%99%E5%AE%9E%E9%A3%8E%E6%99%AF-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 175 | [hf-mcp](hf-mcp-skills-hf-mcp-scan.md) | huggingface | Yes | 2 | MEDIUM |
| 176 | [insecure-defaults](plugins-insecure-defaults-skills-insecure-defaults-scan.md) | trailofbits | **No** | 2 | **HIGH** |
| 177 | [instagram](instagram-scan.md) | clawhub.ai | **No** | 2 | **CRITICAL** |
| 178 | [interpreting-culture-index](plugins-culture-index-skills-interpreting-culture-index-scan.md) | trailofbits | Yes | 2 | MEDIUM |
| 179 | [launch-strategy](launch-strategy-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 180 | [linear-autopilot](linear-autopilot-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 181 | [llm](llm-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 182 | [mailgun](mailgun-scan.md) | clawhub.ai | **No** | 2 | **CRITICAL** |
| 183 | [marketing-psychology](marketing-psychology-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 184 | [memory-hygiene](memory-hygiene-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 185 | [memory-system-v2](memory-system-v2-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 186 | [modern-python](plugins-modern-python-skills-modern-python-scan.md) | trailofbits | Yes | 2 | MEDIUM |
| 187 | [moltbot-ha](moltbot-home-assistant-scan.md) | clawhub.ai | **No** | 2 | **CRITICAL** |
| 188 | [n8n-api](n8n-api-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 189 | [near-email](near-email-skill-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 190 | [nextjs-expert](nextjs-expert-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 191 | [obsidian-tasks](obsidian-tasks-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 192 | [opencode-controller](opencode-controller-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 193 | [paypal](paypal-scan.md) | clawhub.ai | **No** | 2 | **CRITICAL** |
| 194 | [primer-x402](primer-x402-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 195 | [rei](rei-clawd-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 196 | [reposit](reposit-collective-intelligence-for-ai-agents-scan.md) | clawhub.ai | **No** | 2 | **CRITICAL** |
| 197 | [search-reddit](search-reddit-scan.md) | clawhub.ai | **No** | 2 | **CRITICAL** |
| 198 | [semgrep-rule-variant-creator](plugins-semgrep-rule-variant-creator-skills-semgrep-rule-variant-creator-scan.md) | trailofbits | **No** | 2 | **CRITICAL** |
| 199 | [senior-architect](senior-architect-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 200 | [ship-learn-next](ship-learn-next-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 201 | [stock-evaluator-v3](stock-evaluator-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 202 | [subtitles](subtitles-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 203 | [system_monitor](system-monitor-scan.md) | clawhub.ai | Yes | 2 | LOW |
| 204 | [talent-de-cv](digital-identity%2C-cv-%26-resume-creator-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 205 | [taskmaster](taskmaster-ai-cost-optimizer-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 206 | [trading-coach](trading-coach-scan.md) | clawhub.ai | Yes | 2 | LOW |
| 207 | [twitter-openclaw](x-twitter-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 208 | [ui-test](ui-test-scan.md) | clawhub.ai | **No** | 2 | **CRITICAL** |
| 209 | [upgrade-stripe](skills-upgrade-stripe-scan.md) | stripe | **No** | 2 | **CRITICAL** |
| 210 | [verification-before-completion](verification-before-completion-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 211 | [video-transcript](video-transcript-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 212 | [writing-skills](writing-skills-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 213 | [wycheproof](plugins-testing-handbook-skills-skills-wycheproof-scan.md) | trailofbits | **No** | 2 | **CRITICAL** |
| 214 | [x402](x402-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 215 | [youtube-playlist](youtube-playlist-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 216 | [10-of-my-most-popular-text-to-image-series-prompts-78b0897e](test-skill-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 217 | [1inch](1inch-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 218 | [2captcha](2captcha-cli-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 219 | [ab-test-setup](ab-test-setup-scan.md) | skills.sh | Yes | 1 | LOW |
| 220 | [academic-deep-research](academic-deep-research-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 221 | [actual-budget](actual-budget-cli-to-interact-with-the-actual-budget-api-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 222 | [address-sanitizer](plugins-testing-handbook-skills-skills-address-sanitizer-scan.md) | trailofbits | Yes | 1 | LOW |
| 223 | [adguard](adguard-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 224 | [agent-builder](agent-builder-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 225 | [agent-money-tracker](intelligent-budget-tracker-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 226 | [agentarcade](agent-arcade-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 227 | [agents-sdk](skills-agents-sdk-scan.md) | cloudflare | Yes | 1 | LOW |
| 228 | [aifs](aifs-http-file-system-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 229 | [airc](airc-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 230 | [algorand-vulnerability-scanner](plugins-building-secure-contracts-skills-algorand-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 231 | [algorithmic-art](algorithmic-art-scan.md) | skills.sh | Yes | 1 | MEDIUM |
| 232 | [anterior-cingulate-memory](anterior-cingulate-memory-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 233 | [antigravity-image-gen](antigravity-image-generator-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 234 | [api-designer](api-designer-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 235 | [api-docs-gen](api-docs-generator-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 236 | [ask-questions-if-underspecified](plugins-ask-questions-if-underspecified-skills-ask-questions-if-underspecified-scan.md) | trailofbits | Yes | 1 | LOW |
| 237 | [audit-context-building](plugins-audit-context-building-skills-audit-context-building-scan.md) | trailofbits | Yes | 1 | LOW |
| 238 | [audit-prep-assistant](plugins-building-secure-contracts-skills-audit-prep-assistant-scan.md) | trailofbits | Yes | 1 | LOW |
| 239 | [auto-animate](auto-animate-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 240 | [auto-updater](auto-updater-skill-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 241 | [aws-cost-operations](plugins-aws-cost-ops-skills-aws-cost-operations-scan.md) | zxkane | Yes | 1 | LOW |
| 242 | [aws-infra](aws-infra-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 243 | [aws-mcp-setup](plugins-aws-common-skills-aws-mcp-setup-scan.md) | zxkane | Yes | 1 | LOW |
| 244 | [aws-serverless-eda](plugins-serverless-eda-skills-aws-serverless-eda-scan.md) | zxkane | Yes | 1 | LOW |
| 245 | [azure-ai-voicelive-dotnet](github-skills-azure-ai-voicelive-dotnet-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 246 | [azure-communication-callautomation-java](github-skills-azure-communication-callautomation-java-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 247 | [azure-communication-chat-java](github-skills-azure-communication-chat-java-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 248 | [azure-containerregistry-py](github-skills-azure-containerregistry-py-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 249 | [azure-mgmt-apicenter-py](github-skills-azure-mgmt-apicenter-py-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 250 | [azure-mgmt-apimanagement-dotnet](github-skills-azure-mgmt-apimanagement-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 251 | [azure-resource-manager-postgresql-dotnet](github-skills-azure-resource-manager-postgresql-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 252 | [azure-resource-manager-redis-dotnet](github-skills-azure-resource-manager-redis-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 253 | [azure-resource-manager-sql-dotnet](github-skills-azure-resource-manager-sql-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 254 | [azure-search-documents-dotnet](github-skills-azure-search-documents-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 255 | [azure-search-documents-py](github-skills-azure-search-documents-py-scan.md) | microsoft | Yes | 1 | LOW |
| 256 | [azure-security-keyvault-secrets-java](github-skills-azure-security-keyvault-secrets-java-scan.md) | microsoft | Yes | 1 | LOW |
| 257 | [azure-servicebus-dotnet](github-skills-azure-servicebus-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 258 | [azure-servicebus-py](github-skills-azure-servicebus-py-scan.md) | microsoft | Yes | 1 | LOW |
| 259 | [azure-speech-to-text-rest-py](github-skills-azure-speech-to-text-rest-py-scan.md) | microsoft | Yes | 1 | LOW |
| 260 | [azure-storage-blob-java](github-skills-azure-storage-blob-java-scan.md) | microsoft | Yes | 1 | LOW |
| 261 | [azure-storage-blob-py](github-skills-azure-storage-blob-py-scan.md) | microsoft | Yes | 1 | LOW |
| 262 | [azure-storage-file-datalake-py](github-skills-azure-storage-file-datalake-py-scan.md) | microsoft | Yes | 1 | LOW |
| 263 | [azure-storage-file-share-py](github-skills-azure-storage-file-share-py-scan.md) | microsoft | Yes | 1 | LOW |
| 264 | [azure-storage-queue-py](github-skills-azure-storage-queue-py-scan.md) | microsoft | Yes | 1 | LOW |
| 265 | [bags](sagb-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 266 | [basal-ganglia-memory](basal-ganglia-memory-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 267 | [base-trading-agent](base-trading-agent-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 268 | [bat-cat](bat-cat-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 269 | [binance-pay](binance-pay-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 270 | [birthday-reminder](Birthday%20Reminder-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 271 | [browser-agent](browser-agent-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 272 | [burpsuite-project-parser](plugins-burpsuite-project-parser-skills-scan.md) | trailofbits | Yes | 1 | LOW |
| 273 | [bybit-trading](bybit-trading-agent-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 274 | [cairo-vulnerability-scanner](plugins-building-secure-contracts-skills-cairo-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 275 | [calendar](calendar-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 276 | [capability-evolver](capability-evolver-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 277 | [captions](captions-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 278 | [chirp](chirp-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 279 | [chromadb-memory](chromadb-memory-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 280 | [ci-gen](ci-cd-pipeline-generator-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 281 | [claude-chrome](claude-chrome-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 282 | [claude-in-chrome-troubleshooting](plugins-claude-in-chrome-troubleshooting-skills-claude-in-chrome-troubleshooting-scan.md) | trailofbits | Yes | 1 | LOW |
| 283 | [clawbridge](clawbridge-find-your-connections-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 284 | [clawbrowser](clawbrowser-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 285 | [clawdhub](clawdhub-cli-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 286 | [clawflows](clawflows-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 287 | [clawkey](clawkey-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 288 | [clawlist](clawlist-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 289 | [clawops](clawops-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 290 | [code-explain](code-explainer-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 291 | [code-maturity-assessor](plugins-building-secure-contracts-skills-code-maturity-assessor-scan.md) | trailofbits | Yes | 1 | LOW |
| 292 | [codemod-gen](codemod-generator-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 293 | [codeql](plugins-static-analysis-skills-codeql-scan.md) | trailofbits | Yes | 1 | LOW |
| 294 | [codeql](plugins-testing-handbook-skills-skills-codeql-scan.md) | trailofbits | Yes | 1 | LOW |
| 295 | [codex](codex-scan.md) | skills.sh | Yes | 1 | LOW |
| 296 | [coding-agent](coding-agent-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 297 | [commit-work](commit-work-scan.md) | skills.sh | Yes | 1 | LOW |
| 298 | [competitor-alternatives](competitor-alternatives-scan.md) | skills.sh | Yes | 1 | LOW |
| 299 | [compound-engineering](compound-engineering-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 300 | [compound-engineering](compound-interest-calculator-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 301 | [core-vitals-fixer](core-web-vitals-optimizer-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 302 | [cosmos-vulnerability-scanner](plugins-building-secure-contracts-skills-cosmos-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 303 | [coverage-analysis](plugins-testing-handbook-skills-skills-coverage-analysis-scan.md) | trailofbits | Yes | 1 | LOW |
| 304 | [cron-mastery](cron-mastery-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 305 | [crypto-wallet](crypto-wallet-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 306 | [daily-ai-news](daily-ai-news-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 307 | [database](database-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 308 | [defi](defi-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 309 | [deps-analyzer](deps-checker-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 310 | [diagram-gen](diagram-generator-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 311 | [differential-review](plugins-differential-review-skills-differential-review-scan.md) | trailofbits | Yes | 1 | LOW |
| 312 | [discord-chat](discord-chat-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 313 | [discord-voice](discord-voice-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 314 | [dispatching-parallel-agents](dispatching-parallel-agents-scan.md) | skills.sh | Yes | 1 | LOW |
| 315 | [doc-coauthoring](doc-coauthoring-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 316 | [dockerfile-gen](dockerfile-generator-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 317 | [docx](docx-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 318 | [docx](skills-docx-scan.md) | anthropic | Yes | 1 | MEDIUM |
| 319 | [dont-hack-me](dont-hack-me-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 320 | [dotnet-expert](dotnet-expert-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 321 | [dwarf-expert](plugins-dwarf-expert-skills-dwarf-expert-scan.md) | trailofbits | Yes | 1 | LOW |
| 322 | [dwlf](a-clawdbot-skill-that-gives-your-agent-native-access-to-dwlf-%E2%80%94-a-market-analysis-platform-for-crypto-and-stocks.-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 323 | [email](email-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 324 | [email-best-practices](email-best-practices-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 325 | [email-sequence](email-sequence-scan.md) | skills.sh | Yes | 1 | LOW |
| 326 | [entry-point-analyzer](plugins-entry-point-analyzer-skills-entry-point-analyzer-scan.md) | trailofbits | Yes | 1 | LOW |
| 327 | [error-guard](error-guard-%E2%80%94-control%E2%80%91plane-safety-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 328 | [error-handler-gen](error-handler-generator-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 329 | [eslint-gen](eslint-config-generator-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 330 | [exa-web-search-free](exa-web-search-free-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 331 | [excel](excel-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 332 | [executing-plans](executing-plans-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 333 | [fastapi-router-py](github-skills-fastapi-router-py-scan.md) | microsoft | Yes | 1 | LOW |
| 334 | [feast](feast-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 335 | [feishu-api-docs](feishu-api-docs-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 336 | [feishu-bridge](feishu-bridge-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 337 | [find-skills](find-skills-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 338 | [finishing-a-development-branch](finishing-a-development-branch-scan.md) | skills.sh | Yes | 1 | LOW |
| 339 | [fix-review](plugins-fix-review-skills-fix-review-scan.md) | trailofbits | Yes | 1 | LOW |
| 340 | [form-cro](form-cro-scan.md) | skills.sh | Yes | 1 | LOW |
| 341 | [foundry](foundry-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 342 | [frontend-ui-dark-ts](github-skills-frontend-ui-dark-ts-scan.md) | microsoft | Yes | 1 | LOW |
| 343 | [fuzzing-obstacles](plugins-testing-handbook-skills-skills-fuzzing-obstacles-scan.md) | trailofbits | Yes | 1 | LOW |
| 344 | [gaussian-process-mlp-hybrid](ai-%E7%BC%96%E7%A0%81-prompt-skill-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 345 | [gitclaw](gitclaw-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 346 | [github-action-gen](github-action-generator-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 347 | [github-issue-creator](github-skills-github-issue-creator-scan.md) | microsoft | Yes | 1 | LOW |
| 348 | [githunt](githunt-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 349 | [gitlab-cli-skills](gitlab-cli-skills-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 350 | [gitlab-manager](gitlab-manager-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 351 | [google-calendar](google-calendar-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 352 | [guidelines-advisor](plugins-building-secure-contracts-skills-guidelines-advisor-scan.md) | trailofbits | Yes | 1 | LOW |
| 353 | [habitica](habitica-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 354 | [hackernews](hacker-news-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 355 | [harness-writing](plugins-testing-handbook-skills-skills-harness-writing-scan.md) | trailofbits | Yes | 1 | LOW |
| 356 | [health-tracker](healthcheck-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 357 | [hosted-agents-v2-py](github-skills-hosted-agents-v2-py-scan.md) | microsoft | Yes | 1 | LOW |
| 358 | [hugging-face-cli](skills-hugging-face-cli-scan.md) | huggingface | Yes | 1 | LOW |
| 359 | [hugging-face-trackio](skills-hugging-face-trackio-scan.md) | huggingface | Yes | 1 | LOW |
| 360 | [humanize](humanize-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 361 | [hybrid-memory](hybrid-memory-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 362 | [insula-memory](insula-memory-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 363 | [intodns](intodns-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 364 | [json-canvas](skills-json-canvas-scan.md) | kepano | Yes | 1 | LOW |
| 365 | [juicebox-v5](juicy-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 366 | [landing-gen](landing-page-generator-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 367 | [language-learning](language-learning-tutor-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 368 | [lighthouse-fixer](lighthouse-score-fixer-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 369 | [lightning](lightning-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 370 | [linkedin](linkedin-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 371 | [lobster](lobster-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 372 | [local-pandoc](md-to-office-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 373 | [m365-agents-dotnet](github-skills-m365-agents-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 374 | [m365-agents-py](github-skills-m365-agents-py-scan.md) | microsoft | Yes | 1 | LOW |
| 375 | [mcp-builder](github-skills-mcp-builder-scan.md) | microsoft | Yes | 1 | LOW |
| 376 | [mcps](mcps-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 377 | [memory-setup](memory-setup-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 378 | [mermaid-diagrams](mermaid-diagrams-scan.md) | skills.sh | Yes | 1 | LOW |
| 379 | [microsoft-azure-webjobs-extensions-authentication-events-dotnet](github-skills-microsoft-azure-webjobs-extensions-authentication-events-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 380 | [molt-identity](molt-identity-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 381 | [nano-banana-pro](nano-banana-pro-image-generation-%26-editing-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 382 | [nano-pdf](nano-pdf-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 383 | [next-best-practices](next-best-practices-scan.md) | skills.sh | Yes | 1 | LOW |
| 384 | [notion](notion-api-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 385 | [notion](notion-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 386 | [npkill](npkill-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 387 | [nuxt](nuxt-scan.md) | skills.sh | Yes | 1 | LOW |
| 388 | [obsidian-bases](skills-obsidian-bases-scan.md) | kepano | Yes | 1 | LOW |
| 389 | [obsidian-markdown](skills-obsidian-markdown-scan.md) | kepano | Yes | 1 | LOW |
| 390 | [obsidian-sync](obsidian-sync-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 391 | [onboarding-cro](onboarding-cro-scan.md) | skills.sh | Yes | 1 | LOW |
| 392 | [openclaw](comprehensive-skill-for-installing%2C-configuring%2C-and-managing-the-openclaw-ecosystem-gateway%2C-channels%2C-models%2C-automation%2C-nodes%2C-and-deployment-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 393 | [openclaw-checkpoint](openclaw-checkpoint-personal-ai-assistant-backup-%26-recovery-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 394 | [openocean](openocean-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 395 | [openpet](openpet-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 396 | [ossfuzz](plugins-testing-handbook-skills-skills-ossfuzz-scan.md) | trailofbits | Yes | 1 | LOW |
| 397 | [paid-ads](paid-ads-scan.md) | skills.sh | Yes | 1 | LOW |
| 398 | [para-second-brain](para-second-brain-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 399 | [payment](payment-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 400 | [paywall-upgrade-cro](paywall-upgrade-cro-scan.md) | skills.sh | Yes | 1 | LOW |
| 401 | [pdd](pdd-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 402 | [perf-auditor](performance-auditor-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 403 | [podcast-generation](github-skills-podcast-generation-scan.md) | microsoft | Yes | 1 | LOW |
| 404 | [polymarket](polymarket-trading-skill-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 405 | [popup-cro](popup-cro-scan.md) | skills.sh | Yes | 1 | LOW |
| 406 | [property-based-testing](plugins-property-based-testing-skills-property-based-testing-scan.md) | trailofbits | Yes | 1 | LOW |
| 407 | [pydantic-models-py](github-skills-pydantic-models-py-scan.md) | microsoft | Yes | 1 | LOW |
| 408 | [qmd](qmd-external-knowledge-base-search-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 409 | [railway](railway-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 410 | [ralph-loop](ralph-loop-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 411 | [react-expert](react-expert-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 412 | [react-flow-node-ts](github-skills-react-flow-node-ts-scan.md) | microsoft | Yes | 1 | LOW |
| 413 | [readwise-mcp](readwise-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 414 | [receiving-code-review](receiving-code-review-scan.md) | skills.sh | Yes | 1 | LOW |
| 415 | [redis](redis-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 416 | [referral-program](referral-program-scan.md) | skills.sh | Yes | 1 | LOW |
| 417 | [remotion-video-toolkit](remotion-video-toolkit-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 418 | [requesting-code-review](requesting-code-review-scan.md) | skills.sh | Yes | 1 | LOW |
| 419 | [research-paper-writer](research-paper-writer-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 420 | [resume-builder](resume-builder-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 421 | [rssaurus-cli](rssaurus-agent-friendly-rss-feed-reader-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 422 | [ruzzy](plugins-testing-handbook-skills-skills-ruzzy-scan.md) | trailofbits | Yes | 1 | LOW |
| 423 | [schema-markup](schema-markup-scan.md) | skills.sh | Yes | 1 | LOW |
| 424 | [secure-workflow-guide](plugins-building-secure-contracts-skills-secure-workflow-guide-scan.md) | trailofbits | Yes | 1 | LOW |
| 425 | [semgrep](plugins-testing-handbook-skills-skills-semgrep-scan.md) | trailofbits | Yes | 1 | LOW |
| 426 | [sendclaw](sendclaw-email-without-human-permission-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 427 | [senior-devops](senior-devops-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 428 | [seo-audit](seo-audit-scan.md) | skills.sh | Yes | 1 | LOW |
| 429 | [sharp-edges](plugins-sharp-edges-skills-sharp-edges-scan.md) | trailofbits | Yes | 1 | LOW |
| 430 | [shorten](url-shortener-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 431 | [signup-flow-cro](signup-flow-cro-scan.md) | skills.sh | Yes | 1 | LOW |
| 432 | [skill-creator](github-skills-skill-creator-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 433 | [solana-vulnerability-scanner](plugins-building-secure-contracts-skills-solana-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 434 | [sora-2-nature-documentary](sora-2-%E8%87%AA%E7%84%B6%E7%BA%AA%E5%BD%95%E7%89%87-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 435 | [soulcraft](soulcraft-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 436 | [spec-to-code-compliance](plugins-spec-to-code-compliance-skills-spec-to-code-compliance-scan.md) | trailofbits | Yes | 1 | LOW |
| 437 | [spring-boot-engineer](spring-boot-engineer-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 438 | [sql-assistant](sql-assistant-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 439 | [sql-pro](sql-pro-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 440 | [ssh-essentials](ssh-essentials-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 441 | [stealthy-auto-browse](stealthy-auto-browse-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 442 | [stock-market-pro](stock-market-pro-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 443 | [streme-launcher](streme-token-launcher-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 444 | [stripe-best-practices](skills-stripe-best-practices-scan.md) | stripe | Yes | 1 | LOW |
| 445 | [subagent-driven-development](subagent-driven-development-scan.md) | skills.sh | Yes | 1 | LOW |
| 446 | [substrate-vulnerability-scanner](plugins-building-secure-contracts-skills-substrate-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 447 | [swift-expert](swift-expert-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 448 | [tailwind-design-system](tailwind-design-system-scan.md) | skills.sh | Yes | 1 | LOW |
| 449 | [taskr](taskr-remote-task-tracking-for-ai-agents-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 450 | [telegram-auto-topic](telegram-auto-topic-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 451 | [telegram-pairing-customization](%E6%80%BB%E6%98%AF%E5%93%8D%E5%BA%94%E6%9C%AA%E9%85%8D%E5%AF%B9%E7%94%A8%E6%88%B7%E7%9A%84-start-%E6%B6%88%E6%81%AF-always-respond-to-start-messages-from-unpaired-users-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 452 | [template-skill](template-skill-scan.md) | skills.sh | Yes | 1 | LOW |
| 453 | [tg](telegram-cli-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 454 | [token-integration-analyzer](plugins-building-secure-contracts-skills-token-integration-analyzer-scan.md) | trailofbits | Yes | 1 | LOW |
| 455 | [ton-vulnerability-scanner](plugins-building-secure-contracts-skills-ton-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 456 | [trade-signal](trade-singal-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 457 | [transcribe](transcribe-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 458 | [turborepo](turborepo-scan.md) | skills.sh | Yes | 1 | LOW |
| 459 | [twitter](twitter-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 460 | [undetectable-ai](undetectable-ai-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 461 | [using-git-worktrees](using-git-worktrees-scan.md) | skills.sh | Yes | 1 | LOW |
| 462 | [using-superpowers](using-superpowers-scan.md) | skills.sh | Yes | 1 | LOW |
| 463 | [variant-analysis](plugins-variant-analysis-skills-variant-analysis-scan.md) | trailofbits | Yes | 1 | LOW |
| 464 | [vestaboard](vestaboard-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 465 | [vue](vue-scan.md) | skills.sh | Yes | 1 | LOW |
| 466 | [watch-my-money](watch-my-money-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 467 | [web-perf](skills-web-perf-scan.md) | cloudflare | Yes | 1 | LOW |
| 468 | [webapp-testing](skills-webapp-testing-scan.md) | anthropic | Yes | 1 | MEDIUM |
| 469 | [webapp-testing](webapp-testing-scan.md) | anthropic | Yes | 1 | MEDIUM |
| 470 | [webhook-gen](webhook-generator-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 471 | [wordpress-pro](wordpress-pro-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 472 | [writing-clearly-and-concisely](writing-clearly-and-concisely-scan.md) | skills.sh | Yes | 1 | LOW |
| 473 | [writing-plans](writing-plans-scan.md) | skills.sh | Yes | 1 | LOW |
| 474 | [x-trends](x-twitter-trends-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 475 | [yahoo-finance](yahoo-finance-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 476 | [youtube-channels](youtube-channels-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 477 | [youtube-data](youtube-data-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 478 | [youtube-full](youtube-full-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 479 | [youtube-watcher](youtube-watcher-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 480 | [yt-video-downloader](youtube-video-downloader-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 481 | [zustand-store-ts](github-skills-zustand-store-ts-scan.md) | microsoft | Yes | 1 | LOW |
| 482 | [agent-framework-azure-ai-py](github-skills-agent-framework-azure-ai-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 483 | [agent-md-refactor](agent-md-refactor-scan.md) | skills.sh | Yes | 0 | SAFE |
| 484 | [agenticflow-skills](agenticflow-skills-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 485 | [alby-bitcoin-payments-cli-skill](alby-bitcoin-payments-cli-skill-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 486 | [algorithmic-art](skills-algorithmic-art-scan.md) | skills.sh | Yes | 0 | SAFE |
| 487 | [analytics-tracking](analytics-tracking-scan.md) | skills.sh | Yes | 0 | SAFE |
| 488 | [artifacts-builder](artifacts-builder-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 489 | [audit-website](audit-website-scan.md) | skills.sh | Yes | 0 | SAFE |
| 490 | [azd-deployment](github-skills-azd-deployment-scan.md) | microsoft | Yes | 0 | SAFE |
| 491 | [azure-ai-agents-persistent-dotnet](github-skills-azure-ai-agents-persistent-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 492 | [azure-ai-agents-persistent-java](github-skills-azure-ai-agents-persistent-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 493 | [azure-ai-anomalydetector-java](github-skills-azure-ai-anomalydetector-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 494 | [azure-ai-contentsafety-java](github-skills-azure-ai-contentsafety-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 495 | [azure-ai-contentsafety-py](github-skills-azure-ai-contentsafety-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 496 | [azure-ai-formrecognizer-java](github-skills-azure-ai-formrecognizer-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 497 | [azure-ai-ml-py](github-skills-azure-ai-ml-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 498 | [azure-ai-openai-dotnet](github-skills-azure-ai-openai-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 499 | [azure-ai-projects-dotnet](github-skills-azure-ai-projects-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 500 | [azure-ai-projects-java](github-skills-azure-ai-projects-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 501 | [azure-ai-projects-py](github-skills-azure-ai-projects-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 502 | [azure-ai-textanalytics-py](github-skills-azure-ai-textanalytics-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 503 | [azure-ai-transcription-py](github-skills-azure-ai-transcription-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 504 | [azure-ai-translation-document-py](github-skills-azure-ai-translation-document-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 505 | [azure-ai-translation-text-py](github-skills-azure-ai-translation-text-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 506 | [azure-ai-vision-imageanalysis-java](github-skills-azure-ai-vision-imageanalysis-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 507 | [azure-ai-vision-imageanalysis-py](github-skills-azure-ai-vision-imageanalysis-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 508 | [azure-ai-voicelive-java](github-skills-azure-ai-voicelive-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 509 | [azure-ai-voicelive-py](github-skills-azure-ai-voicelive-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 510 | [azure-appconfiguration-java](github-skills-azure-appconfiguration-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 511 | [azure-appconfiguration-py](github-skills-azure-appconfiguration-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 512 | [azure-communication-callingserver-java](github-skills-azure-communication-callingserver-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 513 | [azure-communication-common-java](github-skills-azure-communication-common-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 514 | [azure-communication-sms-java](github-skills-azure-communication-sms-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 515 | [azure-compute-batch-java](github-skills-azure-compute-batch-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 516 | [azure-cosmos-db-py](github-skills-azure-cosmos-db-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 517 | [azure-cosmos-java](github-skills-azure-cosmos-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 518 | [azure-cosmos-py](github-skills-azure-cosmos-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 519 | [azure-data-tables-java](github-skills-azure-data-tables-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 520 | [azure-data-tables-py](github-skills-azure-data-tables-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 521 | [azure-eventgrid-dotnet](github-skills-azure-eventgrid-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 522 | [azure-eventgrid-java](github-skills-azure-eventgrid-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 523 | [azure-eventgrid-py](github-skills-azure-eventgrid-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 524 | [azure-eventhub-dotnet](github-skills-azure-eventhub-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 525 | [azure-eventhub-py](github-skills-azure-eventhub-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 526 | [azure-identity-dotnet](github-skills-azure-identity-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 527 | [azure-identity-java](github-skills-azure-identity-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 528 | [azure-identity-py](github-skills-azure-identity-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 529 | [azure-keyvault-py](github-skills-azure-keyvault-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 530 | [azure-maps-search-dotnet](github-skills-azure-maps-search-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 531 | [azure-messaging-webpubsub-java](github-skills-azure-messaging-webpubsub-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 532 | [azure-messaging-webpubsubservice-py](github-skills-azure-messaging-webpubsubservice-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 533 | [azure-mgmt-apicenter-dotnet](github-skills-azure-mgmt-apicenter-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 534 | [azure-mgmt-apimanagement-py](github-skills-azure-mgmt-apimanagement-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 535 | [azure-mgmt-applicationinsights-dotnet](github-skills-azure-mgmt-applicationinsights-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 536 | [azure-mgmt-arizeaiobservabilityeval-dotnet](github-skills-azure-mgmt-arizeaiobservabilityeval-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 537 | [azure-mgmt-botservice-dotnet](github-skills-azure-mgmt-botservice-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 538 | [azure-mgmt-botservice-py](github-skills-azure-mgmt-botservice-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 539 | [azure-mgmt-fabric-dotnet](github-skills-azure-mgmt-fabric-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 540 | [azure-mgmt-mongodbatlas-dotnet](github-skills-azure-mgmt-mongodbatlas-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 541 | [azure-mgmt-weightsandbiases-dotnet](github-skills-azure-mgmt-weightsandbiases-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 542 | [azure-microsoft-playwright-testing-ts](github-skills-azure-microsoft-playwright-testing-ts-scan.md) | microsoft | Yes | 0 | SAFE |
| 543 | [azure-monitor-ingestion-java](github-skills-azure-monitor-ingestion-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 544 | [azure-monitor-ingestion-py](github-skills-azure-monitor-ingestion-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 545 | [azure-monitor-opentelemetry-exporter-java](github-skills-azure-monitor-opentelemetry-exporter-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 546 | [azure-monitor-opentelemetry-py](github-skills-azure-monitor-opentelemetry-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 547 | [azure-monitor-query-java](github-skills-azure-monitor-query-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 548 | [azure-monitor-query-py](github-skills-azure-monitor-query-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 549 | [azure-postgres-ts](github-skills-azure-postgres-ts-scan.md) | microsoft | Yes | 0 | SAFE |
| 550 | [azure-resource-manager-cosmosdb-dotnet](github-skills-azure-resource-manager-cosmosdb-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 551 | [azure-resource-manager-durabletask-dotnet](github-skills-azure-resource-manager-durabletask-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 552 | [azure-resource-manager-mysql-dotnet](github-skills-azure-resource-manager-mysql-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 553 | [azure-resource-manager-playwright-dotnet](github-skills-azure-resource-manager-playwright-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 554 | [brainstorming](brainstorming-scan.md) | skills.sh | Yes | 0 | SAFE |
| 555 | [brand-guidelines](brand-guidelines-scan.md) | skills.sh | Yes | 0 | SAFE |
| 556 | [brand-guidelines](skills-brand-guidelines-scan.md) | skills.sh | Yes | 0 | SAFE |
| 557 | [building-native-ui](building-native-ui-scan.md) | skills.sh | Yes | 0 | SAFE |
| 558 | [clawdex](clawdex-by-koi-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 559 | [copy-editing](copy-editing-scan.md) | skills.sh | Yes | 0 | SAFE |
| 560 | [copywriting](copywriting-scan.md) | skills.sh | Yes | 0 | SAFE |
| 561 | [create-auth-skill](better-auth-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 562 | [expo-cicd-workflows](expo-cicd-workflows-scan.md) | skills.sh | Yes | 0 | SAFE |
| 563 | [expo-deployment](expo-deployment-scan.md) | skills.sh | Yes | 0 | SAFE |
| 564 | [expo-dev-client](expo-dev-client-scan.md) | skills.sh | Yes | 0 | SAFE |
| 565 | [expo-tailwind-setup](expo-tailwind-setup-scan.md) | skills.sh | Yes | 0 | SAFE |
| 566 | [frontend-design](frontend-design-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 567 | [frontend-design](skills-frontend-design-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 568 | [google-gemini-media](google-gemini-media-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 569 | [internal-comms](internal-comms-scan.md) | skills.sh | Yes | 0 | SAFE |
| 570 | [internal-comms](skills-internal-comms-scan.md) | skills.sh | Yes | 0 | SAFE |
| 571 | [local-falcon](local-falcon-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 572 | [logseq](logseq-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 573 | [marketing-ideas](marketing-ideas-scan.md) | skills.sh | Yes | 0 | SAFE |
| 574 | [mcp-builder](mcp-builder-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 575 | [mcp-builder](skills-mcp-builder-scan.md) | anthropic | Yes | 0 | SAFE |
| 576 | [native-data-fetching](native-data-fetching-scan.md) | skills.sh | Yes | 0 | SAFE |
| 577 | [page-cro](page-cro-scan.md) | skills.sh | Yes | 0 | SAFE |
| 578 | [pdf](pdf-scan.md) | anthropic | Yes | 0 | SAFE |
| 579 | [pdf](skills-pdf-scan.md) | anthropic | Yes | 0 | SAFE |
| 580 | [pptx](pptx-scan.md) | anthropic | Yes | 0 | SAFE |
| 581 | [pptx](skills-pptx-scan.md) | anthropic | Yes | 0 | SAFE |
| 582 | [pricing-strategy](pricing-strategy-scan.md) | skills.sh | Yes | 0 | SAFE |
| 583 | [programmatic-seo](programmatic-seo-scan.md) | skills.sh | Yes | 0 | SAFE |
| 584 | [react-email](react-email-skills-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 585 | [react-native-best-practices](react-native-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 586 | [remotion-best-practices](remotion-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 587 | [skill-creator](jash-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 588 | [skill-creator](skill-creator-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 589 | [skill-creator](skills-skill-creator-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 590 | [slack-gif-creator](skills-slack-gif-creator-scan.md) | skills.sh | Yes | 0 | SAFE |
| 591 | [slack-gif-creator](slack-gif-creator-scan.md) | skills.sh | Yes | 0 | SAFE |
| 592 | [social-content](social-content-scan.md) | skills.sh | Yes | 0 | SAFE |
| 593 | [supabase-postgres-best-practices](supabase-postgres-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 594 | [systematic-debugging](systematic-debugging-scan.md) | skills.sh | Yes | 0 | SAFE |
| 595 | [template-skill](template-scan.md) | skills.sh | Yes | 0 | SAFE |
| 596 | [test-driven-development](test-driven-development-scan.md) | skills.sh | Yes | 0 | SAFE |
| 597 | [theme-factory](skills-theme-factory-scan.md) | anthropic | Yes | 0 | SAFE |
| 598 | [theme-factory](theme-factory-scan.md) | anthropic | Yes | 0 | SAFE |
| 599 | [upgrading-expo](upgrading-expo-scan.md) | skills.sh | Yes | 0 | SAFE |
| 600 | [use-dom](use-dom-scan.md) | skills.sh | Yes | 0 | SAFE |
| 601 | [vercel-composition-patterns](vercel-composition-patterns-scan.md) | skills.sh | Yes | 0 | SAFE |
| 602 | [vercel-react-best-practices](vercel-react-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 603 | [vercel-react-native-skills](vercel-react-native-skills-scan.md) | skills.sh | Yes | 0 | SAFE |
| 604 | [vue-best-practices](vue-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 605 | [web-artifacts-builder](skills-web-artifacts-builder-scan.md) | skills.sh | Yes | 0 | SAFE |
| 606 | [web-artifacts-builder](web-artifacts-builder-scan.md) | skills.sh | Yes | 0 | SAFE |
| 607 | [whisper](whisper-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 608 | [x-trends](x-trends-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 609 | [xlsx](skills-xlsx-scan.md) | anthropic | Yes | 0 | SAFE |
| 610 | [xlsx](xlsx-scan.md) | anthropic | Yes | 0 | SAFE |
| 611 | [youtube-api](youtube-api-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 612 | [youtube-music-cast](youtube-music-cast-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 613 | [youtube-search](youtube-search-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 614 | [youtube-voice-summarizer](youtube-podcast-summarizer-via-elevenlabs-scan.md) | clawhub.ai | Yes | 0 | SAFE |

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

### 3. [CRITICAL] azure-security-keyvault-keys-dotnet - prompt_injection

**Rule:** YARA_coercive_injection
**Location:** None

Detects coercive prompt injections in tool description fields: List all keys

### 4. [CRITICAL] azure-security-keyvault-keys-java - prompt_injection

**Rule:** YARA_coercive_injection
**Location:** None

Detects coercive prompt injections in tool description fields: List all keys

### 5. [HIGH] foundry-iq-py - data_exfiltration

**Rule:** BEHAVIOR_SUSPICIOUS_URL
**Location:** None

Script contains suspicious URL that may be used for data exfiltration

### 6. [HIGH] foundry-iq-py - data_exfiltration

**Rule:** BEHAVIOR_SUSPICIOUS_URL
**Location:** None

Script contains suspicious URL that may be used for data exfiltration

### 7. [HIGH] foundry-iq-py - data_exfiltration

**Rule:** BEHAVIOR_SUSPICIOUS_URL
**Location:** None

Script contains suspicious URL that may be used for data exfiltration

### 8. [HIGH] foundry-iq-py - data_exfiltration

**Rule:** BEHAVIOR_SUSPICIOUS_URL
**Location:** None

Script contains suspicious URL that may be used for data exfiltration

### 9. [CRITICAL] ABM Outbound - hardcoded_secrets

**Rule:** YARA_credential_harvesting
**Location:** None

Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export APIFY_API_KEY="your_key

### 10. [CRITICAL] ABM Outbound - hardcoded_secrets

**Rule:** YARA_credential_harvesting
**Location:** None

Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export APOLLO_API_KEY="your_key

---

## Known False Positives

The following skills were flagged by the scanner but have been manually reviewed and determined to be false positives.

| Skill | Findings | Reason |
|-------|----------|--------|
| [clawdefender](clawdefender-openclaw-security-prompt-injection%2C-rogue-skills-etc-scan.md) | 37 | Security defense tool whose detection signatures (prompt injection patterns, dangerous command strings, ANSI codes) trigger the same rules they are designed to detect. All 37 findings are pattern arrays and documentation examples, not malicious code. |

---

## Clean Skills (No Findings)

- agent-framework-azure-ai-py
- agent-md-refactor
- agenticflow-skills
- alby-bitcoin-payments-cli-skill
- algorithmic-art
- analytics-tracking
- artifacts-builder
- audit-website
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
- frontend-design
- frontend-design
- google-gemini-media
- internal-comms
- internal-comms
- local-falcon
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
- react-email
- react-native-best-practices
- remotion-best-practices
- skill-creator
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

---

## Methodology

- **Scanner:** cisco-ai-skill-scanner
- **Analyzers:** behavioral_analyzer, llm_analyzer, meta_analyzer, static_analyzer, trigger_analyzer
- **Scan Date:** 2026-02-05T10:43:55.504449

### Limitations

- VirusTotal binary scanning not used (requires API key)
- No runtime verification - static and semantic analysis only
