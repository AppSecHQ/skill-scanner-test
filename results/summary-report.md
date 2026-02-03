# AI Agent Skills Security Scan Report

**Generated:** 2026-02-03T14:44:33.718555
**Scanner:** cisco-ai-skill-scanner
**Analyzers:** behavioral, llm, meta, static, trigger

---

## Executive Summary

| Metric | Count |
|--------|-------|
| Total Skills Scanned | 372 |
| Safe Skills | 307 (83%) |
| Skills with Issues | 65 (17%) |
| Scan Errors | 0 |

### Severity Breakdown

| Severity | Count |
|----------|-------|
| CRITICAL | 208 |
| HIGH | 96 |
| MEDIUM | 364 |
| LOW | 278 |
| **Total Findings** | **946** |

### Findings by Category

| Category | Count |
|----------|-------|
| policy_violation | 270 |
| command_injection | 199 |
| transitive_trust_abuse | 163 |
| data_exfiltration | 150 |
| unauthorized_tool_use | 51 |
| hardcoded_secrets | 27 |
| prompt_injection | 24 |
| skill_discovery_abuse | 21 |
| social_engineering | 14 |
| tool_chaining_abuse | 13 |
| resource_abuse | 8 |
| autonomy_abuse | 3 |
| obfuscation | 3 |

---

## Results by Skill

| # | Skill | Source | Safe | Findings | Max Severity |
|---|-------|--------|------|----------|--------------|
| 1 | [hugging-face-evaluation](skills-hugging-face-evaluation-scan.md) | huggingface | **No** | 113 | **CRITICAL** |
| 2 | [hugging-face-datasets](skills-hugging-face-datasets-scan.md) | huggingface | **No** | 77 | **CRITICAL** |
| 3 | [hugging-face-paper-publisher](skills-hugging-face-paper-publisher-scan.md) | huggingface | **No** | 65 | **CRITICAL** |
| 4 | [clawdefender](clawdefender-openclaw-security-prompt-injection%2C-rogue-skills-etc-scan.md) | clawhub.ai | **No** | 37 | **CRITICAL** |
| 5 | [aws-cdk-development](plugins-aws-cdk-skills-aws-cdk-development-scan.md) | zxkane | **No** | 31 | **CRITICAL** |
| 6 | [qa-test-planner](qa-test-planner-scan.md) | skills.sh | **No** | 19 | **CRITICAL** |
| 7 | [yara-rule-authoring](plugins-yara-authoring-skills-yara-rule-authoring-scan.md) | trailofbits | **No** | 19 | **CRITICAL** |
| 8 | [hugging-face-model-trainer](skills-hugging-face-model-trainer-scan.md) | huggingface | **No** | 16 | **HIGH** |
| 9 | [aws-agentic-ai](plugins-aws-agentic-ai-skills-aws-agentic-ai-scan.md) | zxkane | **No** | 15 | **CRITICAL** |
| 10 | [hugging-face-tool-builder](skills-hugging-face-tool-builder-scan.md) | huggingface | **No** | 13 | **CRITICAL** |
| 11 | [clawmail](clawmail-scan.md) | clawhub.ai | **No** | 10 | **CRITICAL** |
| 12 | [constant-time-testing](plugins-testing-handbook-skills-skills-constant-time-testing-scan.md) | trailofbits | **No** | 10 | **CRITICAL** |
| 13 | [semgrep](plugins-static-analysis-skills-semgrep-scan.md) | trailofbits | Yes | 10 | MEDIUM |
| 14 | [swarmmarket](swarmmarket-skill%2C-make-money-with-your-agents-scan.md) | clawhub.ai | **No** | 10 | **CRITICAL** |
| 15 | [browser-use](browser-use-scan.md) | skills.sh | **No** | 8 | **HIGH** |
| 16 | [foundry-iq-py](.github-skills-foundry-iq-py-scan.md) | microsoft | **No** | 8 | **HIGH** |
| 17 | [atheris](plugins-testing-handbook-skills-skills-atheris-scan.md) | trailofbits | **No** | 7 | **CRITICAL** |
| 18 | [azure-ai-evaluation-py](.github-skills-azure-ai-evaluation-py-scan.md) | microsoft | **No** | 7 | **HIGH** |
| 19 | [hugging-face-jobs](skills-hugging-face-jobs-scan.md) | huggingface | **No** | 7 | **HIGH** |
| 20 | [tokenguard](tokenguard-scan.md) | clawhub.ai | **No** | 7 | **HIGH** |
| 21 | [semgrep-rule-creator](plugins-semgrep-rule-creator-skills-semgrep-rule-creator-scan.md) | trailofbits | Yes | 6 | MEDIUM |
| 22 | [wallet-tracker](wallet-tracker-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 23 | [ClawGateSecure](claw-gate-secure-scan.md) | clawhub.ai | Yes | 5 | MEDIUM |
| 24 | [aflpp](plugins-testing-handbook-skills-skills-aflpp-scan.md) | trailofbits | **No** | 5 | **CRITICAL** |
| 25 | [constant-time-analysis](plugins-constant-time-analysis-skills-constant-time-analysis-scan.md) | trailofbits | **No** | 5 | **CRITICAL** |
| 26 | [kalshi](kalshi-scan.md) | clawhub.ai | **No** | 5 | **HIGH** |
| 27 | [libafl](plugins-testing-handbook-skills-skills-libafl-scan.md) | trailofbits | **No** | 5 | **CRITICAL** |
| 28 | [mersal](mersal-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 29 | [solana](solana-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 30 | [azure-cosmos-db-py](.github-skills-azure-cosmos-db-py-scan.md) | microsoft | **No** | 4 | **HIGH** |
| 31 | [canvas-design](skills-canvas-design-scan.md) | anthropic | Yes | 4 | MEDIUM |
| 32 | [domain-name-brainstormer](domain-name-brainstormer-scan.md) | skills.sh | Yes | 4 | MEDIUM |
| 33 | [ethereum-gas-tracker](ethereum-gas-tracker-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 34 | [finance](finance-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 35 | [firebase-apk-scanner](plugins-firebase-apk-scanner-skills-firebase-apk-scanner-scan.md) | trailofbits | **No** | 4 | **CRITICAL** |
| 36 | [humanize-ai](humanize-ai-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 37 | [humanizer](humanizer-scan.md) | clawhub.ai | Yes | 4 | MEDIUM |
| 38 | [insider-wallets-finder](insider-wallets-finder-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 39 | [libfuzzer](plugins-testing-handbook-skills-skills-libfuzzer-scan.md) | trailofbits | **No** | 4 | **CRITICAL** |
| 40 | [phantom](phantom-wallet-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 41 | [sarif-parsing](plugins-static-analysis-skills-sarif-parsing-scan.md) | trailofbits | **No** | 4 | **HIGH** |
| 42 | [session-handoff](session-handoff-scan.md) | skills.sh | **No** | 4 | **HIGH** |
| 43 | [tencent-map](%E8%85%BE%E8%AE%AF%E5%9C%B0%E5%9B%BEapi%E8%B0%83%E7%94%A8%E6%8A%80%E8%83%BD-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 44 | [youtube-summarize](youtube-video-summarizer-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 45 | [MockAPI - Instant REST API from JSON](mockapi-instant-rest-api-from-json-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 46 | [azure-cosmos-py](.github-skills-azure-cosmos-py-scan.md) | microsoft | Yes | 3 | MEDIUM |
| 47 | [azure-eventgrid-dotnet](.github-skills-azure-eventgrid-dotnet-scan.md) | microsoft | **No** | 3 | **CRITICAL** |
| 48 | [azure-postgres-ts](.github-skills-azure-postgres-ts-scan.md) | microsoft | **No** | 3 | **HIGH** |
| 49 | [baidu-map](%E8%B0%83%E7%94%A8%E7%99%BE%E5%BA%A6%E5%9C%B0%E5%9B%BEapi%E5%8A%9F%E8%83%BD-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 50 | [clickup](clickup-skill-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 51 | [cloudflare](skills-cloudflare-scan.md) | cloudflare | Yes | 3 | MEDIUM |
| 52 | [durable-objects](skills-durable-objects-scan.md) | cloudflare | Yes | 3 | MEDIUM |
| 53 | [gemini](gemini-scan.md) | skills.sh | **No** | 3 | **HIGH** |
| 54 | [gemini-nano-banana-pro-portraits](gemini-nano-banana-pro-portraits-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 55 | [google-workspace](google-workspace-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 56 | [moltbook](moltbook-scan.md) | moltbook.com | **No** | 3 | **HIGH** |
| 57 | [playwright-skill](skills-playwright-skill-scan.md) | lackeyjb | Yes | 3 | MEDIUM |
| 58 | [testing-handbook-generator](plugins-testing-handbook-skills-skills-testing-handbook-generator-scan.md) | trailofbits | Yes | 3 | MEDIUM |
| 59 | [web-design-guidelines](web-design-guidelines-scan.md) | skills.sh | **No** | 3 | **HIGH** |
| 60 | [windows-control](windows-control-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 61 | [wrangler](skills-wrangler-scan.md) | cloudflare | **No** | 3 | **CRITICAL** |
| 62 | [Agent Wallet](agent-wallet-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 63 | [agent-browser](agent-browser-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 64 | [agent-framework-azure-ai-py](.github-skills-agent-framework-azure-ai-py-scan.md) | microsoft | Yes | 2 | MEDIUM |
| 65 | [agent-task-manager](agent-task-manager-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 66 | [atxp](atxp-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 67 | [azure-ai-agents-persistent-dotnet](.github-skills-azure-ai-agents-persistent-dotnet-scan.md) | microsoft | Yes | 2 | MEDIUM |
| 68 | [azure-ai-agents-persistent-java](.github-skills-azure-ai-agents-persistent-java-scan.md) | microsoft | **No** | 2 | **CRITICAL** |
| 69 | [azure-ai-projects-py](.github-skills-azure-ai-projects-py-scan.md) | microsoft | Yes | 2 | MEDIUM |
| 70 | [azure-communication-chat-java](.github-skills-azure-communication-chat-java-scan.md) | microsoft | Yes | 2 | MEDIUM |
| 71 | [azure-eventhub-dotnet](.github-skills-azure-eventhub-dotnet-scan.md) | microsoft | Yes | 2 | MEDIUM |
| 72 | [azure-eventhub-java](.github-skills-azure-eventhub-java-scan.md) | microsoft | **No** | 2 | **CRITICAL** |
| 73 | [azure-monitor-ingestion-py](.github-skills-azure-monitor-ingestion-py-scan.md) | microsoft | Yes | 2 | MEDIUM |
| 74 | [azure-security-keyvault-keys-dotnet](.github-skills-azure-security-keyvault-keys-dotnet-scan.md) | microsoft | **No** | 2 | **CRITICAL** |
| 75 | [azure-security-keyvault-keys-java](.github-skills-azure-security-keyvault-keys-java-scan.md) | microsoft | **No** | 2 | **CRITICAL** |
| 76 | [building-ai-agent-on-cloudflare](skills-building-ai-agent-on-cloudflare-scan.md) | cloudflare | **No** | 2 | **CRITICAL** |
| 77 | [building-mcp-server-on-cloudflare](skills-building-mcp-server-on-cloudflare-scan.md) | cloudflare | **No** | 2 | **CRITICAL** |
| 78 | [canvas-design](canvas-design-scan.md) | anthropic | Yes | 2 | MEDIUM |
| 79 | [cargo-fuzz](plugins-testing-handbook-skills-skills-cargo-fuzz-scan.md) | trailofbits | **No** | 2 | **CRITICAL** |
| 80 | [create-auth-skill](create-auth-skill-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 81 | [daily-meeting-update](daily-meeting-update-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 82 | [dependency-updater](dependency-updater-scan.md) | skills.sh | **No** | 2 | **HIGH** |
| 83 | [dev-browser](skills-dev-browser-scan.md) | sawyerhood | Yes | 2 | MEDIUM |
| 84 | [doc-coauthoring](doc-coauthoring-scan.md) | anthropic | Yes | 2 | MEDIUM |
| 85 | [doc-coauthoring](skills-doc-coauthoring-scan.md) | anthropic | Yes | 2 | MEDIUM |
| 86 | [expo-api-routes](expo-api-routes-scan.md) | skills.sh | **No** | 2 | **CRITICAL** |
| 87 | [ez-google](ez-google-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 88 | [ffuf-web-fuzzing](ffuf-skill-scan.md) | jthack | Yes | 2 | MEDIUM |
| 89 | [free-tool-strategy](free-tool-strategy-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 90 | [fuzzing-dictionary](plugins-testing-handbook-skills-skills-fuzzing-dictionary-scan.md) | trailofbits | **No** | 2 | **CRITICAL** |
| 91 | [google-imagen-3-hyperrealistic-landscape](google-imagen-3-%E8%B6%85%E5%86%99%E5%AE%9E%E9%A3%8E%E6%99%AF-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 92 | [hf-mcp](hf-mcp-skills-hf-mcp-scan.md) | huggingface | Yes | 2 | MEDIUM |
| 93 | [insecure-defaults](plugins-insecure-defaults-skills-insecure-defaults-scan.md) | trailofbits | **No** | 2 | **HIGH** |
| 94 | [interpreting-culture-index](plugins-culture-index-skills-interpreting-culture-index-scan.md) | trailofbits | Yes | 2 | MEDIUM |
| 95 | [launch-strategy](launch-strategy-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 96 | [marketing-psychology](marketing-psychology-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 97 | [memory-system-v2](memory-system-v2-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 98 | [modern-python](plugins-modern-python-skills-modern-python-scan.md) | trailofbits | Yes | 2 | MEDIUM |
| 99 | [n8n-api](n8n-api-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 100 | [near-email](near-email-skill-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 101 | [primer-x402](primer-x402-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 102 | [reposit](reposit-collective-intelligence-for-ai-agents-scan.md) | clawhub.ai | **No** | 2 | **CRITICAL** |
| 103 | [semgrep-rule-variant-creator](plugins-semgrep-rule-variant-creator-skills-semgrep-rule-variant-creator-scan.md) | trailofbits | **No** | 2 | **CRITICAL** |
| 104 | [ship-learn-next](ship-learn-next-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 105 | [subtitles](subtitles-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 106 | [taskmaster](taskmaster-ai-cost-optimizer-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 107 | [upgrade-stripe](skills-upgrade-stripe-scan.md) | stripe | **No** | 2 | **CRITICAL** |
| 108 | [verification-before-completion](verification-before-completion-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 109 | [video-transcript](video-transcript-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 110 | [writing-skills](writing-skills-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 111 | [wycheproof](plugins-testing-handbook-skills-skills-wycheproof-scan.md) | trailofbits | **No** | 2 | **CRITICAL** |
| 112 | [youtube-playlist](youtube-playlist-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 113 | [10-of-my-most-popular-text-to-image-series-prompts-78b0897e](test-skill-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 114 | [ab-test-setup](ab-test-setup-scan.md) | skills.sh | Yes | 1 | LOW |
| 115 | [address-sanitizer](plugins-testing-handbook-skills-skills-address-sanitizer-scan.md) | trailofbits | Yes | 1 | LOW |
| 116 | [agentarcade](agent-arcade-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 117 | [agents-sdk](skills-agents-sdk-scan.md) | cloudflare | Yes | 1 | LOW |
| 118 | [airc](airc-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 119 | [algorand-vulnerability-scanner](plugins-building-secure-contracts-skills-algorand-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 120 | [algorithmic-art](algorithmic-art-scan.md) | skills.sh | Yes | 1 | MEDIUM |
| 121 | [ask-questions-if-underspecified](plugins-ask-questions-if-underspecified-skills-ask-questions-if-underspecified-scan.md) | trailofbits | Yes | 1 | LOW |
| 122 | [audit-context-building](plugins-audit-context-building-skills-audit-context-building-scan.md) | trailofbits | Yes | 1 | LOW |
| 123 | [audit-prep-assistant](plugins-building-secure-contracts-skills-audit-prep-assistant-scan.md) | trailofbits | Yes | 1 | LOW |
| 124 | [auto-updater](auto-updater-skill-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 125 | [aws-cost-operations](plugins-aws-cost-ops-skills-aws-cost-operations-scan.md) | zxkane | Yes | 1 | LOW |
| 126 | [aws-mcp-setup](plugins-aws-common-skills-aws-mcp-setup-scan.md) | zxkane | Yes | 1 | LOW |
| 127 | [aws-serverless-eda](plugins-serverless-eda-skills-aws-serverless-eda-scan.md) | zxkane | Yes | 1 | LOW |
| 128 | [azd-deployment](.github-skills-azd-deployment-scan.md) | microsoft | Yes | 1 | LOW |
| 129 | [azure-ai-anomalydetector-java](.github-skills-azure-ai-anomalydetector-java-scan.md) | microsoft | Yes | 1 | LOW |
| 130 | [azure-ai-contentsafety-java](.github-skills-azure-ai-contentsafety-java-scan.md) | microsoft | Yes | 1 | LOW |
| 131 | [azure-ai-contentsafety-py](.github-skills-azure-ai-contentsafety-py-scan.md) | microsoft | Yes | 1 | LOW |
| 132 | [azure-ai-contentunderstanding-py](.github-skills-azure-ai-contentunderstanding-py-scan.md) | microsoft | Yes | 1 | LOW |
| 133 | [azure-ai-document-intelligence-dotnet](.github-skills-azure-ai-document-intelligence-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 134 | [azure-ai-formrecognizer-java](.github-skills-azure-ai-formrecognizer-java-scan.md) | microsoft | Yes | 1 | LOW |
| 135 | [azure-ai-ml-py](.github-skills-azure-ai-ml-py-scan.md) | microsoft | Yes | 1 | LOW |
| 136 | [azure-ai-openai-dotnet](.github-skills-azure-ai-openai-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 137 | [azure-ai-projects-dotnet](.github-skills-azure-ai-projects-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 138 | [azure-ai-projects-java](.github-skills-azure-ai-projects-java-scan.md) | microsoft | Yes | 1 | LOW |
| 139 | [azure-ai-textanalytics-py](.github-skills-azure-ai-textanalytics-py-scan.md) | microsoft | Yes | 1 | LOW |
| 140 | [azure-ai-transcription-py](.github-skills-azure-ai-transcription-py-scan.md) | microsoft | Yes | 1 | LOW |
| 141 | [azure-ai-translation-document-py](.github-skills-azure-ai-translation-document-py-scan.md) | microsoft | Yes | 1 | LOW |
| 142 | [azure-ai-translation-text-py](.github-skills-azure-ai-translation-text-py-scan.md) | microsoft | Yes | 1 | LOW |
| 143 | [azure-ai-vision-imageanalysis-java](.github-skills-azure-ai-vision-imageanalysis-java-scan.md) | microsoft | Yes | 1 | LOW |
| 144 | [azure-ai-vision-imageanalysis-py](.github-skills-azure-ai-vision-imageanalysis-py-scan.md) | microsoft | Yes | 1 | LOW |
| 145 | [azure-ai-voicelive-dotnet](.github-skills-azure-ai-voicelive-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 146 | [azure-ai-voicelive-java](.github-skills-azure-ai-voicelive-java-scan.md) | microsoft | Yes | 1 | LOW |
| 147 | [azure-ai-voicelive-py](.github-skills-azure-ai-voicelive-py-scan.md) | microsoft | Yes | 1 | LOW |
| 148 | [azure-appconfiguration-java](.github-skills-azure-appconfiguration-java-scan.md) | microsoft | Yes | 1 | LOW |
| 149 | [azure-appconfiguration-py](.github-skills-azure-appconfiguration-py-scan.md) | microsoft | Yes | 1 | LOW |
| 150 | [azure-communication-callautomation-java](.github-skills-azure-communication-callautomation-java-scan.md) | microsoft | Yes | 1 | LOW |
| 151 | [azure-communication-callingserver-java](.github-skills-azure-communication-callingserver-java-scan.md) | microsoft | Yes | 1 | LOW |
| 152 | [azure-communication-common-java](.github-skills-azure-communication-common-java-scan.md) | microsoft | Yes | 1 | LOW |
| 153 | [azure-communication-sms-java](.github-skills-azure-communication-sms-java-scan.md) | microsoft | Yes | 1 | LOW |
| 154 | [azure-compute-batch-java](.github-skills-azure-compute-batch-java-scan.md) | microsoft | Yes | 1 | LOW |
| 155 | [azure-containerregistry-py](.github-skills-azure-containerregistry-py-scan.md) | microsoft | Yes | 1 | LOW |
| 156 | [azure-cosmos-java](.github-skills-azure-cosmos-java-scan.md) | microsoft | Yes | 1 | LOW |
| 157 | [azure-data-tables-java](.github-skills-azure-data-tables-java-scan.md) | microsoft | Yes | 1 | LOW |
| 158 | [azure-data-tables-py](.github-skills-azure-data-tables-py-scan.md) | microsoft | Yes | 1 | LOW |
| 159 | [azure-eventgrid-java](.github-skills-azure-eventgrid-java-scan.md) | microsoft | Yes | 1 | LOW |
| 160 | [azure-eventgrid-py](.github-skills-azure-eventgrid-py-scan.md) | microsoft | Yes | 1 | LOW |
| 161 | [azure-eventhub-py](.github-skills-azure-eventhub-py-scan.md) | microsoft | Yes | 1 | LOW |
| 162 | [azure-identity-dotnet](.github-skills-azure-identity-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 163 | [azure-identity-java](.github-skills-azure-identity-java-scan.md) | microsoft | Yes | 1 | LOW |
| 164 | [azure-identity-py](.github-skills-azure-identity-py-scan.md) | microsoft | Yes | 1 | LOW |
| 165 | [azure-keyvault-py](.github-skills-azure-keyvault-py-scan.md) | microsoft | Yes | 1 | LOW |
| 166 | [azure-maps-search-dotnet](.github-skills-azure-maps-search-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 167 | [azure-messaging-webpubsub-java](.github-skills-azure-messaging-webpubsub-java-scan.md) | microsoft | Yes | 1 | LOW |
| 168 | [azure-messaging-webpubsubservice-py](.github-skills-azure-messaging-webpubsubservice-py-scan.md) | microsoft | Yes | 1 | LOW |
| 169 | [azure-mgmt-apicenter-dotnet](.github-skills-azure-mgmt-apicenter-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 170 | [azure-mgmt-apicenter-py](.github-skills-azure-mgmt-apicenter-py-scan.md) | microsoft | Yes | 1 | LOW |
| 171 | [azure-mgmt-apimanagement-dotnet](.github-skills-azure-mgmt-apimanagement-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 172 | [azure-mgmt-apimanagement-py](.github-skills-azure-mgmt-apimanagement-py-scan.md) | microsoft | Yes | 1 | LOW |
| 173 | [azure-mgmt-applicationinsights-dotnet](.github-skills-azure-mgmt-applicationinsights-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 174 | [azure-mgmt-arizeaiobservabilityeval-dotnet](.github-skills-azure-mgmt-arizeaiobservabilityeval-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 175 | [azure-mgmt-botservice-dotnet](.github-skills-azure-mgmt-botservice-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 176 | [azure-mgmt-botservice-py](.github-skills-azure-mgmt-botservice-py-scan.md) | microsoft | Yes | 1 | LOW |
| 177 | [azure-mgmt-fabric-dotnet](.github-skills-azure-mgmt-fabric-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 178 | [azure-mgmt-fabric-py](.github-skills-azure-mgmt-fabric-py-scan.md) | microsoft | Yes | 1 | LOW |
| 179 | [azure-mgmt-mongodbatlas-dotnet](.github-skills-azure-mgmt-mongodbatlas-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 180 | [azure-mgmt-weightsandbiases-dotnet](.github-skills-azure-mgmt-weightsandbiases-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 181 | [azure-microsoft-playwright-testing-ts](.github-skills-azure-microsoft-playwright-testing-ts-scan.md) | microsoft | Yes | 1 | LOW |
| 182 | [azure-monitor-ingestion-java](.github-skills-azure-monitor-ingestion-java-scan.md) | microsoft | Yes | 1 | LOW |
| 183 | [azure-monitor-opentelemetry-exporter-java](.github-skills-azure-monitor-opentelemetry-exporter-java-scan.md) | microsoft | Yes | 1 | LOW |
| 184 | [azure-monitor-opentelemetry-exporter-py](.github-skills-azure-monitor-opentelemetry-exporter-py-scan.md) | microsoft | Yes | 1 | LOW |
| 185 | [azure-monitor-opentelemetry-py](.github-skills-azure-monitor-opentelemetry-py-scan.md) | microsoft | Yes | 1 | LOW |
| 186 | [azure-monitor-query-java](.github-skills-azure-monitor-query-java-scan.md) | microsoft | Yes | 1 | LOW |
| 187 | [azure-monitor-query-py](.github-skills-azure-monitor-query-py-scan.md) | microsoft | Yes | 1 | LOW |
| 188 | [azure-resource-manager-cosmosdb-dotnet](.github-skills-azure-resource-manager-cosmosdb-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 189 | [azure-resource-manager-durabletask-dotnet](.github-skills-azure-resource-manager-durabletask-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 190 | [azure-resource-manager-mysql-dotnet](.github-skills-azure-resource-manager-mysql-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 191 | [azure-resource-manager-playwright-dotnet](.github-skills-azure-resource-manager-playwright-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 192 | [azure-resource-manager-postgresql-dotnet](.github-skills-azure-resource-manager-postgresql-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 193 | [azure-resource-manager-redis-dotnet](.github-skills-azure-resource-manager-redis-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 194 | [azure-resource-manager-sql-dotnet](.github-skills-azure-resource-manager-sql-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 195 | [azure-search-documents-dotnet](.github-skills-azure-search-documents-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 196 | [azure-search-documents-py](.github-skills-azure-search-documents-py-scan.md) | microsoft | Yes | 1 | LOW |
| 197 | [azure-security-keyvault-secrets-java](.github-skills-azure-security-keyvault-secrets-java-scan.md) | microsoft | Yes | 1 | LOW |
| 198 | [azure-servicebus-dotnet](.github-skills-azure-servicebus-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 199 | [azure-servicebus-py](.github-skills-azure-servicebus-py-scan.md) | microsoft | Yes | 1 | LOW |
| 200 | [azure-speech-to-text-rest-py](.github-skills-azure-speech-to-text-rest-py-scan.md) | microsoft | Yes | 1 | LOW |
| 201 | [azure-storage-blob-java](.github-skills-azure-storage-blob-java-scan.md) | microsoft | Yes | 1 | LOW |
| 202 | [azure-storage-blob-py](.github-skills-azure-storage-blob-py-scan.md) | microsoft | Yes | 1 | LOW |
| 203 | [azure-storage-file-datalake-py](.github-skills-azure-storage-file-datalake-py-scan.md) | microsoft | Yes | 1 | LOW |
| 204 | [azure-storage-file-share-py](.github-skills-azure-storage-file-share-py-scan.md) | microsoft | Yes | 1 | LOW |
| 205 | [azure-storage-queue-py](.github-skills-azure-storage-queue-py-scan.md) | microsoft | Yes | 1 | LOW |
| 206 | [bags](sagb-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 207 | [birthday-reminder](Birthday%20Reminder-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 208 | [burpsuite-project-parser](plugins-burpsuite-project-parser-skills-scan.md) | trailofbits | Yes | 1 | LOW |
| 209 | [cairo-vulnerability-scanner](plugins-building-secure-contracts-skills-cairo-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 210 | [captions](captions-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 211 | [claude-in-chrome-troubleshooting](plugins-claude-in-chrome-troubleshooting-skills-claude-in-chrome-troubleshooting-scan.md) | trailofbits | Yes | 1 | LOW |
| 212 | [clawhub](clawhub-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 213 | [code-maturity-assessor](plugins-building-secure-contracts-skills-code-maturity-assessor-scan.md) | trailofbits | Yes | 1 | LOW |
| 214 | [codeql](plugins-static-analysis-skills-codeql-scan.md) | trailofbits | Yes | 1 | LOW |
| 215 | [codeql](plugins-testing-handbook-skills-skills-codeql-scan.md) | trailofbits | Yes | 1 | LOW |
| 216 | [codex](codex-scan.md) | skills.sh | Yes | 1 | LOW |
| 217 | [commit-work](commit-work-scan.md) | skills.sh | Yes | 1 | LOW |
| 218 | [competitor-alternatives](competitor-alternatives-scan.md) | skills.sh | Yes | 1 | LOW |
| 219 | [cosmos-vulnerability-scanner](plugins-building-secure-contracts-skills-cosmos-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 220 | [coverage-analysis](plugins-testing-handbook-skills-skills-coverage-analysis-scan.md) | trailofbits | Yes | 1 | LOW |
| 221 | [differential-review](plugins-differential-review-skills-differential-review-scan.md) | trailofbits | Yes | 1 | LOW |
| 222 | [dispatching-parallel-agents](dispatching-parallel-agents-scan.md) | skills.sh | Yes | 1 | LOW |
| 223 | [docx](docx-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 224 | [docx](skills-docx-scan.md) | anthropic | Yes | 1 | MEDIUM |
| 225 | [dwarf-expert](plugins-dwarf-expert-skills-dwarf-expert-scan.md) | trailofbits | Yes | 1 | LOW |
| 226 | [dwlf](a-clawdbot-skill-that-gives-your-agent-native-access-to-dwlf-%E2%80%94-a-market-analysis-platform-for-crypto-and-stocks.-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 227 | [email-sequence](email-sequence-scan.md) | skills.sh | Yes | 1 | LOW |
| 228 | [entry-point-analyzer](plugins-entry-point-analyzer-skills-entry-point-analyzer-scan.md) | trailofbits | Yes | 1 | LOW |
| 229 | [executing-plans](executing-plans-scan.md) | skills.sh | Yes | 1 | LOW |
| 230 | [fastapi-router-py](.github-skills-fastapi-router-py-scan.md) | microsoft | Yes | 1 | LOW |
| 231 | [feast](feast-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 232 | [feishu-api-docs](feishu-api-docs-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 233 | [finishing-a-development-branch](finishing-a-development-branch-scan.md) | skills.sh | Yes | 1 | LOW |
| 234 | [fix-review](plugins-fix-review-skills-fix-review-scan.md) | trailofbits | Yes | 1 | LOW |
| 235 | [form-cro](form-cro-scan.md) | skills.sh | Yes | 1 | LOW |
| 236 | [frontend-ui-dark-ts](.github-skills-frontend-ui-dark-ts-scan.md) | microsoft | Yes | 1 | LOW |
| 237 | [fuzzing-obstacles](plugins-testing-handbook-skills-skills-fuzzing-obstacles-scan.md) | trailofbits | Yes | 1 | LOW |
| 238 | [github-issue-creator](.github-skills-github-issue-creator-scan.md) | microsoft | Yes | 1 | LOW |
| 239 | [gitlab-manager](gitlab-manager-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 240 | [guidelines-advisor](plugins-building-secure-contracts-skills-guidelines-advisor-scan.md) | trailofbits | Yes | 1 | LOW |
| 241 | [harness-writing](plugins-testing-handbook-skills-skills-harness-writing-scan.md) | trailofbits | Yes | 1 | LOW |
| 242 | [hosted-agents-v2-py](.github-skills-hosted-agents-v2-py-scan.md) | microsoft | Yes | 1 | LOW |
| 243 | [hugging-face-cli](skills-hugging-face-cli-scan.md) | huggingface | Yes | 1 | LOW |
| 244 | [hugging-face-trackio](skills-hugging-face-trackio-scan.md) | huggingface | Yes | 1 | LOW |
| 245 | [json-canvas](skills-json-canvas-scan.md) | kepano | Yes | 1 | LOW |
| 246 | [m365-agents-dotnet](.github-skills-m365-agents-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 247 | [m365-agents-py](.github-skills-m365-agents-py-scan.md) | microsoft | Yes | 1 | LOW |
| 248 | [mcp-builder](.github-skills-mcp-builder-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 249 | [mermaid-diagrams](mermaid-diagrams-scan.md) | skills.sh | Yes | 1 | LOW |
| 250 | [microsoft-azure-webjobs-extensions-authentication-events-dotnet](.github-skills-microsoft-azure-webjobs-extensions-authentication-events-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 251 | [next-best-practices](next-best-practices-scan.md) | skills.sh | Yes | 1 | LOW |
| 252 | [notion](notion-api-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 253 | [nuxt](nuxt-scan.md) | skills.sh | Yes | 1 | LOW |
| 254 | [obsidian-bases](skills-obsidian-bases-scan.md) | kepano | Yes | 1 | LOW |
| 255 | [obsidian-markdown](skills-obsidian-markdown-scan.md) | kepano | Yes | 1 | LOW |
| 256 | [obsidian-sync](obsidian-sync-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 257 | [onboarding-cro](onboarding-cro-scan.md) | skills.sh | Yes | 1 | LOW |
| 258 | [openpet](openpet-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 259 | [ossfuzz](plugins-testing-handbook-skills-skills-ossfuzz-scan.md) | trailofbits | Yes | 1 | LOW |
| 260 | [paid-ads](paid-ads-scan.md) | skills.sh | Yes | 1 | LOW |
| 261 | [paywall-upgrade-cro](paywall-upgrade-cro-scan.md) | skills.sh | Yes | 1 | LOW |
| 262 | [podcast-generation](.github-skills-podcast-generation-scan.md) | microsoft | Yes | 1 | LOW |
| 263 | [polymarket](polymarket-trading-skill-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 264 | [popup-cro](popup-cro-scan.md) | skills.sh | Yes | 1 | LOW |
| 265 | [property-based-testing](plugins-property-based-testing-skills-property-based-testing-scan.md) | trailofbits | Yes | 1 | LOW |
| 266 | [pydantic-models-py](.github-skills-pydantic-models-py-scan.md) | microsoft | Yes | 1 | LOW |
| 267 | [react-flow-node-ts](.github-skills-react-flow-node-ts-scan.md) | microsoft | Yes | 1 | LOW |
| 268 | [readwise-mcp](readwise-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 269 | [receiving-code-review](receiving-code-review-scan.md) | skills.sh | Yes | 1 | LOW |
| 270 | [referral-program](referral-program-scan.md) | skills.sh | Yes | 1 | LOW |
| 271 | [requesting-code-review](requesting-code-review-scan.md) | skills.sh | Yes | 1 | LOW |
| 272 | [ruzzy](plugins-testing-handbook-skills-skills-ruzzy-scan.md) | trailofbits | Yes | 1 | LOW |
| 273 | [schema-markup](schema-markup-scan.md) | skills.sh | Yes | 1 | LOW |
| 274 | [secure-workflow-guide](plugins-building-secure-contracts-skills-secure-workflow-guide-scan.md) | trailofbits | Yes | 1 | LOW |
| 275 | [semgrep](plugins-testing-handbook-skills-skills-semgrep-scan.md) | trailofbits | Yes | 1 | LOW |
| 276 | [seo-audit](seo-audit-scan.md) | skills.sh | Yes | 1 | LOW |
| 277 | [sharp-edges](plugins-sharp-edges-skills-sharp-edges-scan.md) | trailofbits | Yes | 1 | LOW |
| 278 | [signup-flow-cro](signup-flow-cro-scan.md) | skills.sh | Yes | 1 | LOW |
| 279 | [skill-creator](.github-skills-skill-creator-scan.md) | microsoft | Yes | 1 | LOW |
| 280 | [solana-vulnerability-scanner](plugins-building-secure-contracts-skills-solana-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 281 | [sora-2-nature-documentary](sora-2-%E8%87%AA%E7%84%B6%E7%BA%AA%E5%BD%95%E7%89%87-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 282 | [spec-to-code-compliance](plugins-spec-to-code-compliance-skills-spec-to-code-compliance-scan.md) | trailofbits | Yes | 1 | LOW |
| 283 | [stealthy-auto-browse](stealthy-auto-browse-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 284 | [streme-launcher](streme-token-launcher-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 285 | [stripe-best-practices](skills-stripe-best-practices-scan.md) | stripe | Yes | 1 | LOW |
| 286 | [subagent-driven-development](subagent-driven-development-scan.md) | skills.sh | Yes | 1 | LOW |
| 287 | [substrate-vulnerability-scanner](plugins-building-secure-contracts-skills-substrate-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 288 | [tailwind-design-system](tailwind-design-system-scan.md) | skills.sh | Yes | 1 | LOW |
| 289 | [template-skill](template-skill-scan.md) | skills.sh | Yes | 1 | LOW |
| 290 | [token-integration-analyzer](plugins-building-secure-contracts-skills-token-integration-analyzer-scan.md) | trailofbits | Yes | 1 | LOW |
| 291 | [ton-vulnerability-scanner](plugins-building-secure-contracts-skills-ton-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 292 | [turborepo](turborepo-scan.md) | skills.sh | Yes | 1 | LOW |
| 293 | [undetectable-ai](undetectable-ai-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 294 | [using-git-worktrees](using-git-worktrees-scan.md) | skills.sh | Yes | 1 | LOW |
| 295 | [using-superpowers](using-superpowers-scan.md) | skills.sh | Yes | 1 | LOW |
| 296 | [variant-analysis](plugins-variant-analysis-skills-variant-analysis-scan.md) | trailofbits | Yes | 1 | LOW |
| 297 | [vestaboard](vestaboard-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 298 | [vue](vue-scan.md) | skills.sh | Yes | 1 | LOW |
| 299 | [web-perf](skills-web-perf-scan.md) | cloudflare | Yes | 1 | LOW |
| 300 | [webapp-testing](skills-webapp-testing-scan.md) | anthropic | Yes | 1 | MEDIUM |
| 301 | [webapp-testing](webapp-testing-scan.md) | anthropic | Yes | 1 | MEDIUM |
| 302 | [writing-clearly-and-concisely](writing-clearly-and-concisely-scan.md) | skills.sh | Yes | 1 | LOW |
| 303 | [writing-plans](writing-plans-scan.md) | skills.sh | Yes | 1 | LOW |
| 304 | [x-trends](x-twitter-trends-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 305 | [yahoo-finance](yahoo-finance-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 306 | [youtube-channels](youtube-channels-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 307 | [youtube-data](youtube-data-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 308 | [youtube-full](youtube-full-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 309 | [zustand-store-ts](.github-skills-zustand-store-ts-scan.md) | microsoft | Yes | 1 | LOW |
| 310 | [agent-md-refactor](agent-md-refactor-scan.md) | skills.sh | Yes | 0 | SAFE |
| 311 | [algorithmic-art](skills-algorithmic-art-scan.md) | skills.sh | Yes | 0 | SAFE |
| 312 | [analytics-tracking](analytics-tracking-scan.md) | skills.sh | Yes | 0 | SAFE |
| 313 | [artifacts-builder](artifacts-builder-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 314 | [audit-website](audit-website-scan.md) | skills.sh | Yes | 0 | SAFE |
| 315 | [brainstorming](brainstorming-scan.md) | skills.sh | Yes | 0 | SAFE |
| 316 | [brand-guidelines](brand-guidelines-scan.md) | skills.sh | Yes | 0 | SAFE |
| 317 | [brand-guidelines](skills-brand-guidelines-scan.md) | skills.sh | Yes | 0 | SAFE |
| 318 | [building-native-ui](building-native-ui-scan.md) | skills.sh | Yes | 0 | SAFE |
| 319 | [clawdex](clawdex-by-koi-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 320 | [copy-editing](copy-editing-scan.md) | skills.sh | Yes | 0 | SAFE |
| 321 | [copywriting](copywriting-scan.md) | skills.sh | Yes | 0 | SAFE |
| 322 | [create-auth-skill](better-auth-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 323 | [expo-cicd-workflows](expo-cicd-workflows-scan.md) | skills.sh | Yes | 0 | SAFE |
| 324 | [expo-deployment](expo-deployment-scan.md) | skills.sh | Yes | 0 | SAFE |
| 325 | [expo-dev-client](expo-dev-client-scan.md) | skills.sh | Yes | 0 | SAFE |
| 326 | [expo-tailwind-setup](expo-tailwind-setup-scan.md) | skills.sh | Yes | 0 | SAFE |
| 327 | [find-skills](find-skills-scan.md) | skills.sh | Yes | 0 | SAFE |
| 328 | [frontend-design](frontend-design-scan.md) | anthropic | Yes | 0 | SAFE |
| 329 | [frontend-design](skills-frontend-design-scan.md) | anthropic | Yes | 0 | SAFE |
| 330 | [health-tracker](healthcheck-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 331 | [internal-comms](internal-comms-scan.md) | skills.sh | Yes | 0 | SAFE |
| 332 | [internal-comms](skills-internal-comms-scan.md) | skills.sh | Yes | 0 | SAFE |
| 333 | [logseq](logseq-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 334 | [marketing-ideas](marketing-ideas-scan.md) | skills.sh | Yes | 0 | SAFE |
| 335 | [mcp-builder](mcp-builder-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 336 | [mcp-builder](skills-mcp-builder-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 337 | [native-data-fetching](native-data-fetching-scan.md) | skills.sh | Yes | 0 | SAFE |
| 338 | [page-cro](page-cro-scan.md) | skills.sh | Yes | 0 | SAFE |
| 339 | [pdf](pdf-scan.md) | anthropic | Yes | 0 | SAFE |
| 340 | [pdf](skills-pdf-scan.md) | anthropic | Yes | 0 | SAFE |
| 341 | [pptx](pptx-scan.md) | anthropic | Yes | 0 | SAFE |
| 342 | [pptx](skills-pptx-scan.md) | anthropic | Yes | 0 | SAFE |
| 343 | [pricing-strategy](pricing-strategy-scan.md) | skills.sh | Yes | 0 | SAFE |
| 344 | [programmatic-seo](programmatic-seo-scan.md) | skills.sh | Yes | 0 | SAFE |
| 345 | [react-native-best-practices](react-native-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 346 | [remotion-best-practices](remotion-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 347 | [skill-creator](skill-creator-scan.md) | anthropic | Yes | 0 | SAFE |
| 348 | [skill-creator](skills-skill-creator-scan.md) | anthropic | Yes | 0 | SAFE |
| 349 | [slack-gif-creator](skills-slack-gif-creator-scan.md) | skills.sh | Yes | 0 | SAFE |
| 350 | [slack-gif-creator](slack-gif-creator-scan.md) | skills.sh | Yes | 0 | SAFE |
| 351 | [social-content](social-content-scan.md) | skills.sh | Yes | 0 | SAFE |
| 352 | [supabase-postgres-best-practices](supabase-postgres-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 353 | [systematic-debugging](systematic-debugging-scan.md) | skills.sh | Yes | 0 | SAFE |
| 354 | [template-skill](template-scan.md) | skills.sh | Yes | 0 | SAFE |
| 355 | [test-driven-development](test-driven-development-scan.md) | skills.sh | Yes | 0 | SAFE |
| 356 | [theme-factory](skills-theme-factory-scan.md) | anthropic | Yes | 0 | SAFE |
| 357 | [theme-factory](theme-factory-scan.md) | anthropic | Yes | 0 | SAFE |
| 358 | [ui-ux-pro-max](ui-ux-pro-max-scan.md) | skills.sh | Yes | 0 | SAFE |
| 359 | [upgrading-expo](upgrading-expo-scan.md) | skills.sh | Yes | 0 | SAFE |
| 360 | [use-dom](use-dom-scan.md) | skills.sh | Yes | 0 | SAFE |
| 361 | [vercel-composition-patterns](vercel-composition-patterns-scan.md) | skills.sh | Yes | 0 | SAFE |
| 362 | [vercel-react-best-practices](vercel-react-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 363 | [vercel-react-native-skills](vercel-react-native-skills-scan.md) | skills.sh | Yes | 0 | SAFE |
| 364 | [vue-best-practices](vue-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 365 | [web-artifacts-builder](skills-web-artifacts-builder-scan.md) | skills.sh | Yes | 0 | SAFE |
| 366 | [web-artifacts-builder](web-artifacts-builder-scan.md) | skills.sh | Yes | 0 | SAFE |
| 367 | [xlsx](skills-xlsx-scan.md) | anthropic | Yes | 0 | SAFE |
| 368 | [xlsx](xlsx-scan.md) | anthropic | Yes | 0 | SAFE |
| 369 | [youtube-api](youtube-api-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 370 | [youtube-music-cast](youtube-music-cast-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 371 | [youtube-search](youtube-search-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 372 | [youtube-voice-summarizer](youtube-podcast-summarizer-via-elevenlabs-scan.md) | clawhub.ai | Yes | 0 | SAFE |

---

## Top Risks (Critical/High Severity)

### 1. [CRITICAL] azure-ai-agents-persistent-java - command_injection

**Rule:** YARA_sql_injection
**Location:** None

Detects SQL injection attack patterns including keywords, tautologies, and database functions: sleep(

### 2. [HIGH] azure-ai-evaluation-py - prompt_injection

**Rule:** PROMPT_INJECTION_IGNORE_INSTRUCTIONS
**Location:** None

Pattern detected: ignore previous instructions

### 3. [HIGH] azure-ai-evaluation-py - prompt_injection

**Rule:** ASSET_PROMPT_INJECTION
**Location:** None

Pattern 'ignore previous instructions...' detected in asset file

### 4. [HIGH] azure-ai-evaluation-py - prompt_injection

**Rule:** ASSET_PROMPT_INJECTION
**Location:** None

Pattern 'ignore previous instructions...' detected in asset file

### 5. [HIGH] azure-cosmos-db-py - resource_abuse

**Rule:** RESOURCE_ABUSE_INFINITE_LOOP
**Location:** None

Pattern detected: while True:

### 6. [HIGH] azure-cosmos-db-py - resource_abuse

**Rule:** RESOURCE_ABUSE_INFINITE_LOOP
**Location:** None

Pattern detected: while True:

### 7. [HIGH] azure-cosmos-db-py - resource_abuse

**Rule:** RESOURCE_ABUSE_INFINITE_LOOP
**Location:** None

Pattern detected: while True:

### 8. [CRITICAL] azure-eventgrid-dotnet - command_injection

**Rule:** YARA_script_injection
**Location:** None

Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: # 

### 9. [CRITICAL] azure-eventgrid-dotnet - command_injection

**Rule:** YARA_script_injection
**Location:** None

Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: Function(

### 10. [CRITICAL] azure-eventhub-java - command_injection

**Rule:** YARA_sql_injection
**Location:** None

Detects SQL injection attack patterns including keywords, tautologies, and database functions: sleep(

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
- **Scan Date:** 2026-02-03T14:44:33.718555

### Limitations

- VirusTotal binary scanning not used (requires API key)
- No runtime verification - static and semantic analysis only
