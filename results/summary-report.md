# AI Agent Skills Security Scan Report

**Generated:** 2026-10-22T14:35:50.937456
**Scanner:** cisco-ai-skill-scanner 2.3.1
**Analyzers:** behavioral, bytecode, correlation, llm, meta, pipeline, static, trigger

---

## Executive Summary

| Metric | Count |
|--------|-------|
| Total Skills Scanned | 1303 |
| Safe Skills | 1092 (84%) |
| Skills with Issues | 211 (16%) |
| Scan Errors | 0 |

### Severity Breakdown

| Severity | Count |
|----------|-------|
| CRITICAL | 378 |
| HIGH | 325 |
| MEDIUM | 1049 |
| LOW | 869 |
| **Total Findings** | **3058** |

### Findings by Category

| Category | Count |
|----------|-------|
| data_exfiltration | 745 |
| obfuscation | 582 |
| policy_violation | 530 |
| command_injection | 397 |
| unauthorized_tool_use | 212 |
| social_engineering | 208 |
| transitive_trust_abuse | 151 |
| resource_abuse | 91 |
| prompt_injection | 65 |
| tool_chaining_abuse | 30 |
| hardcoded_secrets | 23 |
| supply_chain_attack | 17 |
| skill_discovery_abuse | 6 |
| autonomy_abuse | 1 |

---

## Results by Skill

| # | Skill | Source | Safe | Findings | Max Severity |
|---|-------|--------|------|----------|--------------|
| 1 | [media-use](heygen-com-hyperframes-skills-media-use-scan.md) | heygen-com | **No** | 116 | **CRITICAL** |
| 2 | [hugging-face-evaluation](skills-hugging-face-evaluation-scan.md) | huggingface | Yes | 96 | MEDIUM |
| 3 | [hugging-face-datasets](skills-hugging-face-datasets-scan.md) | huggingface | **No** | 78 | **CRITICAL** |
| 4 | [lark-drive](site-open.feishu.cn-lark-drive-scan.md) | open.feishu.cn | Yes | 64 | LOW |
| 5 | [lark-im](site-open.feishu.cn-lark-im-scan.md) | open.feishu.cn | Yes | 64 | LOW |
| 6 | [hugging-face-paper-publisher](skills-hugging-face-paper-publisher-scan.md) | huggingface | Yes | 54 | MEDIUM |
| 7 | [lark-slides](site-open.feishu.cn-lark-slides-scan.md) | open.feishu.cn | Yes | 53 | MEDIUM |
| 8 | [zoho-email](zoho-email-integration-scan.md) | clawhub.ai | **No** | 53 | **CRITICAL** |
| 9 | [lark-apps](site-open.feishu.cn-lark-apps-scan.md) | open.feishu.cn | Yes | 51 | MEDIUM |
| 10 | [lark-doc](site-open.feishu.cn-lark-doc-scan.md) | open.feishu.cn | Yes | 47 | LOW |
| 11 | [design-taste-frontend](leonxlnx-taste-skill-skills-taste-skill-scan.md) | leonxlnx | **No** | 39 | **CRITICAL** |
| 12 | [lark-mail](site-open.feishu.cn-lark-mail-scan.md) | open.feishu.cn | Yes | 34 | LOW |
| 13 | [lark-whiteboard](site-open.feishu.cn-lark-whiteboard-scan.md) | open.feishu.cn | Yes | 34 | LOW |
| 14 | [finance-news](finance-news-briefings-scan.md) | clawhub.ai | **No** | 33 | **HIGH** |
| 15 | [lark-meeting](site-open.feishu.cn-lark-meeting-scan.md) | open.feishu.cn | Yes | 33 | LOW |
| 16 | [lark-sheets](site-open.feishu.cn-lark-sheets-scan.md) | open.feishu.cn | Yes | 33 | MEDIUM |
| 17 | [lark-base](site-open.feishu.cn-lark-base-scan.md) | open.feishu.cn | Yes | 30 | LOW |
| 18 | [lark-okr](site-open.feishu.cn-lark-okr-scan.md) | open.feishu.cn | Yes | 29 | LOW |
| 19 | [microsoft-foundry](microsoft-azure-skills-github-plugins-azure-skills-skills-microsoft-foundry-scan.md) | microsoft | **No** | 29 | **CRITICAL** |
| 20 | [microsoft-foundry](microsoft-azure-skills-skills-microsoft-foundry-scan.md) | microsoft | **No** | 29 | **CRITICAL** |
| 21 | [lark-task](site-open.feishu.cn-lark-task-scan.md) | open.feishu.cn | Yes | 22 | LOW |
| 22 | [qa-test-planner](qa-test-planner-scan.md) | skills.sh | **No** | 22 | **CRITICAL** |
| 23 | [lark-approval](site-open.feishu.cn-lark-approval-scan.md) | open.feishu.cn | Yes | 20 | LOW |
| 24 | [skill-scanner](ai-skill-scanner-scan.md) | clawhub.ai | **No** | 19 | **CRITICAL** |
| 25 | [yara-rule-authoring](plugins-yara-authoring-skills-yara-rule-authoring-scan.md) | trailofbits | **No** | 19 | **CRITICAL** |
| 26 | [lark-calendar](site-open.feishu.cn-lark-calendar-scan.md) | open.feishu.cn | Yes | 18 | LOW |
| 27 | [lark-wiki](site-open.feishu.cn-lark-wiki-scan.md) | open.feishu.cn | Yes | 17 | LOW |
| 28 | [remotion-to-hyperframes](heygen-com-hyperframes-skills-remotion-to-hyperframes-scan.md) | heygen-com | Yes | 17 | MEDIUM |
| 29 | [hyperframes](heygen-com-hyperframes-skills-hyperframes-scan.md) | heygen-com | **No** | 15 | **CRITICAL** |
| 30 | [update-plus](update-plus-scan.md) | clawhub.ai | **No** | 15 | **CRITICAL** |
| 31 | [hugging-face-model-trainer](skills-hugging-face-model-trainer-scan.md) | huggingface | Yes | 14 | MEDIUM |
| 32 | [frost-sequence-camera-orbit](heygen-com-hyperframes-registry-blocks-frost-sequence-camera-orbit-scan.md) | heygen-com | **No** | 13 | **CRITICAL** |
| 33 | [meta-ads](skills-meta-ads-scan.md) | hoodini | **No** | 13 | **CRITICAL** |
| 34 | [base-trader](base-trader-scan.md) | clawhub.ai | **No** | 12 | **CRITICAL** |
| 35 | [constant-time-testing](plugins-testing-handbook-skills-skills-constant-time-testing-scan.md) | trailofbits | **No** | 12 | **CRITICAL** |
| 36 | [hugging-face-tool-builder](skills-hugging-face-tool-builder-scan.md) | huggingface | **No** | 12 | **CRITICAL** |
| 37 | [autoskill](skills-autoskill-scan.md) | K-Dense-AI | **No** | 11 | **CRITICAL** |
| 38 | [finetuning](microsoft-azure-skills-github-plugins-azure-skills-skills-microsoft-foundry-finetuning-scan.md) | microsoft | **No** | 11 | **CRITICAL** |
| 39 | [finetuning](microsoft-azure-skills-skills-microsoft-foundry-finetuning-scan.md) | microsoft | **No** | 11 | **CRITICAL** |
| 40 | [imap-smtp-email](imap-smtp-email-scan.md) | clawhub.ai | **No** | 11 | **HIGH** |
| 41 | [lark-event](site-open.feishu.cn-lark-event-scan.md) | open.feishu.cn | Yes | 11 | LOW |
| 42 | [agent-browser](101-skills-superpowers-tools-utilities-agent-browser-scan.md) | 101-skills | **No** | 10 | **HIGH** |
| 43 | [agent-browser](magentosh-superpowers-tools-utilities-agent-browser-scan.md) | magentosh | **No** | 10 | **HIGH** |
| 44 | [agent-browser](qu-skills-superpowers-tools-utilities-agent-browser-scan.md) | qu-skills | **No** | 10 | **HIGH** |
| 45 | [entra-agent-id](microsoft-azure-skills-github-plugins-azure-skills-skills-entra-agent-id-scan.md) | microsoft | **No** | 10 | **HIGH** |
| 46 | [entra-agent-id](microsoft-azure-skills-skills-entra-agent-id-scan.md) | microsoft | **No** | 10 | **HIGH** |
| 47 | [lark-shared](site-open.feishu.cn-lark-shared-scan.md) | open.feishu.cn | Yes | 10 | LOW |
| 48 | [simmer](simmer-scan.md) | clawhub.ai | **No** | 10 | **CRITICAL** |
| 49 | [capability-evolver](capability-evolver-scan.md) | clawhub.ai | **No** | 9 | **CRITICAL** |
| 50 | [lark-markdown](site-open.feishu.cn-lark-markdown-scan.md) | open.feishu.cn | Yes | 9 | LOW |
| 51 | [scientific-slides](skills-scientific-slides-scan.md) | K-Dense-AI | **No** | 9 | **CRITICAL** |
| 52 | [session-handoff](session-handoff-scan.md) | skills.sh | **No** | 9 | **HIGH** |
| 53 | [azure-cloud-migrate](microsoft-azure-skills-github-plugins-azure-skills-skills-azure-cloud-migrate-scan.md) | microsoft | Yes | 8 | MEDIUM |
| 54 | [azure-cloud-migrate](microsoft-azure-skills-skills-azure-cloud-migrate-scan.md) | microsoft | Yes | 8 | MEDIUM |
| 55 | [building-inferencesh-apps](101-skills-superpowers-sdk-building-apps-scan.md) | 101-skills | **No** | 8 | **HIGH** |
| 56 | [building-inferencesh-apps](magentosh-superpowers-sdk-building-apps-scan.md) | magentosh | **No** | 8 | **HIGH** |
| 57 | [building-inferencesh-apps](qu-skills-superpowers-sdk-building-apps-scan.md) | qu-skills | **No** | 8 | **HIGH** |
| 58 | [citation-management](skills-citation-management-scan.md) | K-Dense-AI | **No** | 8 | **CRITICAL** |
| 59 | [code-slice-hero](heygen-com-hyperframes-registry-blocks-code-slice-hero-scan.md) | heygen-com | **No** | 8 | **CRITICAL** |
| 60 | [hugging-face-jobs](skills-hugging-face-jobs-scan.md) | huggingface | Yes | 8 | MEDIUM |
| 61 | [libafl](plugins-testing-handbook-skills-skills-libafl-scan.md) | trailofbits | **No** | 8 | **CRITICAL** |
| 62 | [modal](skills-modal-scan.md) | K-Dense-AI | **No** | 8 | **HIGH** |
| 63 | [ontology-term-resolution](skills-ontology-term-resolution-scan.md) | K-Dense-AI | Yes | 8 | MEDIUM |
| 64 | [ruzzy](plugins-testing-handbook-skills-skills-ruzzy-scan.md) | trailofbits | Yes | 8 | MEDIUM |
| 65 | [x402](x402-scan.md) | clawhub.ai | **No** | 8 | **CRITICAL** |
| 66 | [ClawDoro](clawdoro-scan.md) | clawhub.ai | Yes | 7 | MEDIUM |
| 67 | [auto-updater](auto-updater-skill-scan.md) | clawhub.ai | **No** | 7 | **CRITICAL** |
| 68 | [browse](browserbase-scan.md) | clawhub.ai | Yes | 7 | MEDIUM |
| 69 | [caveman-compress](juliusbrussee-caveman-plugins-caveman-skills-caveman-compress-scan.md) | juliusbrussee | **No** | 7 | **HIGH** |
| 70 | [caveman-compress](juliusbrussee-caveman-skills-caveman-compress-scan.md) | juliusbrussee | **No** | 7 | **HIGH** |
| 71 | [cuboid-carousel](heygen-com-hyperframes-registry-blocks-cuboid-carousel-scan.md) | heygen-com | Yes | 7 | MEDIUM |
| 72 | [dev-browser](skills-dev-browser-scan.md) | sawyerhood | Yes | 7 | MEDIUM |
| 73 | [foundry](foundry-scan.md) | clawhub.ai | **No** | 7 | **CRITICAL** |
| 74 | [infographics](skills-infographics-scan.md) | K-Dense-AI | **No** | 7 | **CRITICAL** |
| 75 | [lark-contact](site-open.feishu.cn-lark-contact-scan.md) | open.feishu.cn | Yes | 7 | LOW |
| 76 | [latex-posters](skills-latex-posters-scan.md) | K-Dense-AI | **No** | 7 | **CRITICAL** |
| 77 | [literature-review](skills-literature-review-scan.md) | K-Dense-AI | **No** | 7 | **CRITICAL** |
| 78 | [open-notebook](skills-open-notebook-scan.md) | K-Dense-AI | **No** | 7 | **CRITICAL** |
| 79 | [orbit-card](heygen-com-hyperframes-registry-blocks-orbit-card-scan.md) | heygen-com | Yes | 7 | MEDIUM |
| 80 | [paper-lookup](skills-paper-lookup-scan.md) | K-Dense-AI | Yes | 7 | MEDIUM |
| 81 | [telegram-pairing-customization](%E6%80%BB%E6%98%AF%E5%93%8D%E5%BA%94%E6%9C%AA%E9%85%8D%E5%AF%B9%E7%94%A8%E6%88%B7%E7%9A%84-start-%E6%B6%88%E6%81%AF-always-respond-to-start-messages-from-unpaired-users-scan.md) | clawhub.ai | **No** | 7 | **CRITICAL** |
| 82 | [vestaboard](vestaboard-scan.md) | clawhub.ai | Yes | 7 | MEDIUM |
| 83 | [ABM Outbound](abm-outbound-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 84 | [agent-task-manager](agent-task-manager-scan.md) | clawhub.ai | Yes | 6 | MEDIUM |
| 85 | [azure-deploy](microsoft-azure-skills-github-plugins-azure-skills-skills-azure-deploy-scan.md) | microsoft | **No** | 6 | **CRITICAL** |
| 86 | [azure-deploy](microsoft-azure-skills-skills-azure-deploy-scan.md) | microsoft | **No** | 6 | **CRITICAL** |
| 87 | [biopython](skills-biopython-scan.md) | K-Dense-AI | Yes | 6 | MEDIUM |
| 88 | [browser-agent](browser-agent-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 89 | [bybit-trading](bybit-trading-agent-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 90 | [clawhub](clawhub-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 91 | [coding-agent](coding-agent-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 92 | [excel](excel-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 93 | [glass-shard-title](heygen-com-hyperframes-registry-blocks-glass-shard-title-scan.md) | heygen-com | **No** | 6 | **CRITICAL** |
| 94 | [google](google-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 95 | [hyperframes-cli](heygen-com-hyperframes-skills-hyperframes-cli-scan.md) | heygen-com | Yes | 6 | MEDIUM |
| 96 | [omni-stories](omni-stories-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 97 | [openwork](openwork-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 98 | [pathogen-variant-surveillance](skills-pathogen-variant-surveillance-scan.md) | K-Dense-AI | Yes | 6 | MEDIUM |
| 99 | [phone-agent](phone-voice-agent-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 100 | [taskr](taskr-remote-task-tracking-for-ai-agents-scan.md) | clawhub.ai | Yes | 6 | MEDIUM |
| 101 | [using-git-worktrees](using-git-worktrees-scan.md) | skills.sh | Yes | 6 | MEDIUM |
| 102 | [wallet-tracker](wallet-tracker-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 103 | [whisper](whisper-scan.md) | clawhub.ai | **No** | 6 | **CRITICAL** |
| 104 | [Agent Browser](browser-automation-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 105 | [ClawGateSecure](claw-gate-secure-scan.md) | clawhub.ai | Yes | 5 | MEDIUM |
| 106 | [agent-tools](101-skills-superpowers-tools-agent-tools-scan.md) | 101-skills | **No** | 5 | **HIGH** |
| 107 | [agent-tools](magentosh-superpowers-tools-agent-tools-scan.md) | magentosh | **No** | 5 | **HIGH** |
| 108 | [agent-tools](qu-skills-superpowers-tools-agent-tools-scan.md) | qu-skills | **No** | 5 | **HIGH** |
| 109 | [azure-eventhub-java](github-skills-azure-eventhub-java-scan.md) | microsoft | **No** | 5 | **CRITICAL** |
| 110 | [azure-prepare](microsoft-azure-skills-github-plugins-azure-skills-skills-azure-prepare-scan.md) | microsoft | Yes | 5 | MEDIUM |
| 111 | [azure-prepare](microsoft-azure-skills-skills-azure-prepare-scan.md) | microsoft | Yes | 5 | MEDIUM |
| 112 | [azure-storage-blob-java](github-skills-azure-storage-blob-java-scan.md) | microsoft | Yes | 5 | LOW |
| 113 | [azure-validate](microsoft-azure-skills-github-plugins-azure-skills-skills-azure-validate-scan.md) | microsoft | Yes | 5 | MEDIUM |
| 114 | [azure-validate](microsoft-azure-skills-skills-azure-validate-scan.md) | microsoft | Yes | 5 | MEDIUM |
| 115 | [base-trading-agent](base-trading-agent-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 116 | [browser-use](browser-use-scan.md) | skills.sh | **No** | 5 | **HIGH** |
| 117 | [clawdhub](clawdhub-cli-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 118 | [clawflows](clawflows-scan.md) | clawhub.ai | **No** | 5 | **HIGH** |
| 119 | [compound-engineering](compound-interest-calculator-scan.md) | clawhub.ai | **No** | 5 | **HIGH** |
| 120 | [cryptocurrency-trader](cryptocurrency-trader-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 121 | [ffuf-web-fuzzing](ffuf-skill-scan.md) | jthack | Yes | 5 | MEDIUM |
| 122 | [gitclaw](gitclaw-scan.md) | clawhub.ai | **No** | 5 | **HIGH** |
| 123 | [health-tracker](healthcheck-scan.md) | clawhub.ai | Yes | 5 | MEDIUM |
| 124 | [hugging-face-cli](skills-hugging-face-cli-scan.md) | huggingface | Yes | 5 | LOW |
| 125 | [hugging-science](skills-hugging-science-scan.md) | K-Dense-AI | **No** | 5 | **HIGH** |
| 126 | [infsh-cli](101-skills-superpowers-tools-infsh-cli-scan.md) | 101-skills | **No** | 5 | **HIGH** |
| 127 | [infsh-cli](magentosh-superpowers-tools-infsh-cli-scan.md) | magentosh | **No** | 5 | **HIGH** |
| 128 | [infsh-cli](qu-skills-superpowers-tools-infsh-cli-scan.md) | qu-skills | **No** | 5 | **HIGH** |
| 129 | [job-auto-apply](job-auto-apply-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 130 | [linear-autopilot](linear-autopilot-scan.md) | clawhub.ai | **No** | 5 | **HIGH** |
| 131 | [linkedin](linkedin-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 132 | [mersal](mersal-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 133 | [moltbook](moltbook-scan.md) | moltbook.com | **No** | 5 | **CRITICAL** |
| 134 | [nano-banana-pro](nano-banana-pro-image-generation-%26-editing-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 135 | [ncats-arax](skills-ncats-arax-scan.md) | K-Dense-AI | Yes | 5 | MEDIUM |
| 136 | [openclaw-optimizer](startclaw-optimizer-scan.md) | clawhub.ai | **No** | 5 | **HIGH** |
| 137 | [polymarket](polymarket-better-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 138 | [research-lookup](skills-research-lookup-scan.md) | K-Dense-AI | **No** | 5 | **CRITICAL** |
| 139 | [scientific-schematics](skills-scientific-schematics-scan.md) | K-Dense-AI | **No** | 5 | **CRITICAL** |
| 140 | [sendclaw](sendclaw-email-without-human-permission-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 141 | [solana](solana-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 142 | [stealthy-auto-browse](stealthy-auto-browse-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 143 | [subagent-driven-development](subagent-driven-development-scan.md) | skills.sh | Yes | 5 | MEDIUM |
| 144 | [taskmaster](taskmaster-ai-cost-optimizer-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 145 | [tokenguard](tokenguard-scan.md) | clawhub.ai | **No** | 5 | **HIGH** |
| 146 | [using-superpowers](using-superpowers-scan.md) | skills.sh | **No** | 5 | **HIGH** |
| 147 | [voice-agent](voice-agent-scan.md) | clawhub.ai | **No** | 5 | **HIGH** |
| 148 | [windows-control](windows-control-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 149 | [yahoo-finance](yahoo-finance-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 150 | [youtube-watcher](youtube-watcher-scan.md) | clawhub.ai | **No** | 5 | **CRITICAL** |
| 151 | [MoltMedia](moltmedia-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 152 | [adguard](adguard-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 153 | [apewisdom](apewisdom-reddit-scanner-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 154 | [bags](sagb-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 155 | [binance-pay](binance-pay-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 156 | [channel](wechat-oa-channel-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 157 | [ci-gen](ci-cd-pipeline-generator-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 158 | [claude-chrome](claude-chrome-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 159 | [clawmail](clawmail-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 160 | [compound-engineering](compound-engineering-scan.md) | clawhub.ai | Yes | 4 | MEDIUM |
| 161 | [ctxly](mymemory.bot-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 162 | [discord-voice](discord-voice-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 163 | [docx](skills-docx-scan.md) | anthropic | **No** | 4 | **HIGH** |
| 164 | [esm](skills-esm-scan.md) | K-Dense-AI | **No** | 4 | **HIGH** |
| 165 | [ethereum-gas-tracker](ethereum-gas-tracker-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 166 | [firebase-apk-scanner](plugins-firebase-apk-scanner-skills-firebase-apk-scanner-scan.md) | trailofbits | **No** | 4 | **CRITICAL** |
| 167 | [firebase-apk-scanner](plugins-firebase-apkner-skills-firebase-apkner-scan.md) | trailofbits | **No** | 4 | **HIGH** |
| 168 | [fuzzing-dictionary](plugins-testing-handbook-skills-skills-fuzzing-dictionary-scan.md) | trailofbits | **No** | 4 | **CRITICAL** |
| 169 | [glycoengineering](skills-glycoengineering-scan.md) | K-Dense-AI | Yes | 4 | MEDIUM |
| 170 | [google-workspace](google-workspace-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 171 | [hyperliquid](hyperliquid-cli-with-hip3-support-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 172 | [insider-wallets-finder](insider-wallets-finder-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 173 | [lark-attendance](site-open.feishu.cn-lark-attendance-scan.md) | open.feishu.cn | Yes | 4 | LOW |
| 174 | [lark-minutes](site-open.feishu.cn-lark-minutes-scan.md) | open.feishu.cn | Yes | 4 | LOW |
| 175 | [lark-note](site-open.feishu.cn-lark-note-scan.md) | open.feishu.cn | Yes | 4 | LOW |
| 176 | [lark-openapi-explorer](site-open.feishu.cn-lark-openapi-explorer-scan.md) | open.feishu.cn | Yes | 4 | LOW |
| 177 | [lark-skill-maker](site-open.feishu.cn-lark-skill-maker-scan.md) | open.feishu.cn | Yes | 4 | LOW |
| 178 | [lark-vc](site-open.feishu.cn-lark-vc-scan.md) | open.feishu.cn | Yes | 4 | LOW |
| 179 | [lark-vc-agent](site-open.feishu.cn-lark-vc-agent-scan.md) | open.feishu.cn | Yes | 4 | LOW |
| 180 | [lark-workflow-meeting-summary](site-open.feishu.cn-lark-workflow-meeting-summary-scan.md) | open.feishu.cn | Yes | 4 | LOW |
| 181 | [lark-workflow-standup-report](site-open.feishu.cn-lark-workflow-standup-report-scan.md) | open.feishu.cn | Yes | 4 | LOW |
| 182 | [lightning](lightning-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 183 | [motion-doctrine](heygen-com-hyperframes-agents-skills-motion-doctrine-scan.md) | heygen-com | **No** | 4 | **CRITICAL** |
| 184 | [motion-doctrine](heygen-com-hyperframes-claude-skills-motion-doctrine-scan.md) | heygen-com | **No** | 4 | **CRITICAL** |
| 185 | [nano-pdf](nano-pdf-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 186 | [notebooklm](notebooklm-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 187 | [phantom](phantom-wallet-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 188 | [redis](redis-scan.md) | clawhub.ai | Yes | 4 | MEDIUM |
| 189 | [scaffold](microsoft-azure-skills-github-plugins-azure-skills-skills-azure-app-onboard-scaffold-scan.md) | microsoft | **No** | 4 | **CRITICAL** |
| 190 | [scaffold](microsoft-azure-skills-skills-azure-app-onboard-scaffold-scan.md) | microsoft | **No** | 4 | **CRITICAL** |
| 191 | [slack](slack-scan.md) | clawhub.ai | **No** | 4 | **HIGH** |
| 192 | [sora-2-nature-documentary](sora-2-%E8%87%AA%E7%84%B6%E7%BA%AA%E5%BD%95%E7%89%87-scan.md) | clawhub.ai | Yes | 4 | LOW |
| 193 | [stripe-best-practices](skills-stripe-best-practices-scan.md) | stripe | Yes | 4 | MEDIUM |
| 194 | [supermemory](supermemory-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 195 | [tencent-map](%E8%85%BE%E8%AE%AF%E5%9C%B0%E5%9B%BEapi%E8%B0%83%E7%94%A8%E6%8A%80%E8%83%BD-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 196 | [tinyfish](tinyfish-web-agent-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 197 | [torch-geometric](skills-torch-geometric-scan.md) | K-Dense-AI | **No** | 4 | **HIGH** |
| 198 | [torchdrug](skills-torchdrug-scan.md) | K-Dense-AI | **No** | 4 | **HIGH** |
| 199 | [x-trends](x-twitter-trends-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 200 | [youtube-summarize](youtube-video-summarizer-scan.md) | clawhub.ai | **No** | 4 | **CRITICAL** |
| 201 | [2captcha](2captcha-cli-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 202 | [Docker Pro Diagnostic](docker-diag-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 203 | [MockAPI - Instant REST API from JSON](mockapi-instant-rest-api-from-json-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 204 | [YT Meta - YouTube Metadata Extractor](yt-meta-youtube-metadata-extractor-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 205 | [activecampaign](activecampaign-crm-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 206 | [activecampaign](baby-connect-logger-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 207 | [agentarcade](agent-arcade-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 208 | [agnxi-search](agent-skills-search-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 209 | [ai-automation-workflows](101-skills-superpowers-guides-content-ai-automation-workflows-scan.md) | 101-skills | **No** | 3 | **HIGH** |
| 210 | [ai-automation-workflows](magentosh-superpowers-guides-content-ai-automation-workflows-scan.md) | magentosh | **No** | 3 | **HIGH** |
| 211 | [ai-automation-workflows](qu-skills-superpowers-guides-content-ai-automation-workflows-scan.md) | qu-skills | **No** | 3 | **HIGH** |
| 212 | [aks-troubleshooting](microsoft-azure-skills-github-plugins-aks-skills-skills-aks-troubleshooting-scan.md) | microsoft | Yes | 3 | MEDIUM |
| 213 | [alby-bitcoin-payments-cli-skill](alby-bitcoin-payments-cli-skill-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 214 | [algorithmic-art](algorithmic-art-scan.md) | anthropic | Yes | 3 | MEDIUM |
| 215 | [amap](amap-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 216 | [api-docs-gen](api-docs-generator-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 217 | [api-gateway](api-gateway-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 218 | [atxp](atxp-scan.md) | skills.sh | Yes | 3 | MEDIUM |
| 219 | [azure-mgmt-fabric-py](github-skills-azure-mgmt-fabric-py-scan.md) | microsoft | **No** | 3 | **HIGH** |
| 220 | [azure-upgrade](microsoft-azure-skills-github-plugins-azure-skills-skills-azure-upgrade-scan.md) | microsoft | Yes | 3 | MEDIUM |
| 221 | [azure-upgrade](microsoft-azure-skills-skills-azure-upgrade-scan.md) | microsoft | Yes | 3 | MEDIUM |
| 222 | [baidu-map](%E8%B0%83%E7%94%A8%E7%99%BE%E5%BA%A6%E5%9C%B0%E5%9B%BEapi%E5%8A%9F%E8%83%BD-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 223 | [botcoin-miner](botcoin-miner-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 224 | [clawlist](clawlist-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 225 | [clickup](clickup-skill-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 226 | [codemod-gen](codemod-generator-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 227 | [crypto-gold-monitor](%E5%8A%A0%E5%AF%86%E8%B4%A7%E5%B8%81%E4%B8%8E%E8%B4%B5%E9%87%91%E5%B1%9E%E7%9B%91%E6%8E%A7-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 228 | [crypto-wallet](crypto-wallet-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 229 | [defi](defi-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 230 | [diagram-gen](diagram-generator-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 231 | [diff-summary](git-diff-summarizer-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 232 | [error-handler-gen](error-handler-generator-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 233 | [etf-assistant](etf%E6%8A%95%E8%B5%84%E5%8A%A9%E7%90%86-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 234 | [figma](heygen-com-hyperframes-skills-figma-scan.md) | heygen-com | **No** | 3 | **CRITICAL** |
| 235 | [gcloud](google-cloud-platform-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 236 | [generate-image](skills-generate-image-scan.md) | K-Dense-AI | Yes | 3 | MEDIUM |
| 237 | [genomic-intelligence](skills-genomic-intelligence-scan.md) | K-Dense-AI | **No** | 3 | **HIGH** |
| 238 | [geomaster](skills-geomaster-scan.md) | K-Dense-AI | **No** | 3 | **HIGH** |
| 239 | [giphy-gif](giphy-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 240 | [github-action-gen](github-action-generator-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 241 | [home-assistant](home-assistant-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 242 | [lighthouse-fixer](lighthouse-score-fixer-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 243 | [local-llm-router](skills-local-llm-router-scan.md) | hoodini | Yes | 3 | MEDIUM |
| 244 | [mageck](skills-mageck-scan.md) | K-Dense-AI | Yes | 3 | MEDIUM |
| 245 | [mcps](mcps-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 246 | [nextflow](skills-nextflow-scan.md) | K-Dense-AI | **No** | 3 | **CRITICAL** |
| 247 | [obsidian-sync](obsidian-sync-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 248 | [openclaw-checkpoint](openclaw-checkpoint-personal-ai-assistant-backup-%26-recovery-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 249 | [ossfuzz](plugins-testing-handbook-skills-skills-ossfuzz-scan.md) | trailofbits | Yes | 3 | LOW |
| 250 | [protocolsio-integration](skills-protocolsio-integration-scan.md) | K-Dense-AI | Yes | 3 | MEDIUM |
| 251 | [python-sdk](101-skills-superpowers-sdk-python-sdk-scan.md) | 101-skills | **No** | 3 | **HIGH** |
| 252 | [python-sdk](magentosh-superpowers-sdk-python-sdk-scan.md) | magentosh | **No** | 3 | **HIGH** |
| 253 | [python-sdk](qu-skills-superpowers-sdk-python-sdk-scan.md) | qu-skills | **No** | 3 | **HIGH** |
| 254 | [reposit](reposit-collective-intelligence-for-ai-agents-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 255 | [save-money](save-money-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 256 | [skill-scanner](skill-scanner-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 257 | [stealth-browser](stealth-browser-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 258 | [swarmmarket](swarmmarket-skill%2C-make-money-with-your-agents-scan.md) | clawhub.ai | **No** | 3 | **CRITICAL** |
| 259 | [talent-de-cv](digital-identity%2C-cv-%26-resume-creator-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 260 | [technews](techmeme-news-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 261 | [telegram-auto-topic](telegram-auto-topic-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 262 | [testing-handbook-generator](plugins-testing-handbook-skills-skills-testing-handbook-generator-scan.md) | trailofbits | Yes | 3 | MEDIUM |
| 263 | [trade-signal](trade-singal-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 264 | [trading-coach](trading-coach-scan.md) | clawhub.ai | Yes | 3 | MEDIUM |
| 265 | [undetectable-ai](undetectable-ai-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 266 | [web-design-guidelines](web-design-guidelines-scan.md) | skills.sh | **No** | 3 | **HIGH** |
| 267 | [youtube-voice-summarizer](youtube-podcast-summarizer-via-elevenlabs-scan.md) | clawhub.ai | **No** | 3 | **HIGH** |
| 268 | [1inch](1inch-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 269 | [Agent Wallet](agent-wallet-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 270 | [Job Search MCP](job-search-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 271 | [adaptyv](skills-adaptyv-scan.md) | K-Dense-AI | **No** | 2 | **HIGH** |
| 272 | [aegis-security](aegis-security-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 273 | [agent-money-tracker](intelligent-budget-tracker-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 274 | [ai-pdf-builder](ai-pdf-builder-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 275 | [aifs](aifs-http-file-system-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 276 | [antigravity-image-gen](antigravity-image-generator-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 277 | [apewisdom](apewisdom-redditner-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 278 | [aws-agentic-ai](plugins-aws-agentic-ai-skills-aws-agentic-ai-scan.md) | zxkane | Yes | 2 | MEDIUM |
| 279 | [aws-cdk-development](plugins-aws-cdk-skills-aws-cdk-development-scan.md) | zxkane | Yes | 2 | MEDIUM |
| 280 | [aws-infra](aws-infra-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 281 | [azure-ai-contentunderstanding-py](github-skills-azure-ai-contentunderstanding-py-scan.md) | microsoft | Yes | 2 | MEDIUM |
| 282 | [azure-ai-document-intelligence-dotnet](github-skills-azure-ai-document-intelligence-dotnet-scan.md) | microsoft | Yes | 2 | MEDIUM |
| 283 | [azure-ai-evaluation-py](github-skills-azure-ai-evaluation-py-scan.md) | microsoft | Yes | 2 | MEDIUM |
| 284 | [azure-diagnostics](microsoft-azure-skills-github-plugins-azure-skills-skills-azure-diagnostics-scan.md) | microsoft | Yes | 2 | MEDIUM |
| 285 | [azure-diagnostics](microsoft-azure-skills-skills-azure-diagnostics-scan.md) | microsoft | Yes | 2 | MEDIUM |
| 286 | [azure-monitor-opentelemetry-exporter-py](github-skills-azure-monitor-opentelemetry-exporter-py-scan.md) | microsoft | Yes | 2 | MEDIUM |
| 287 | [bids](skills-bids-scan.md) | K-Dense-AI | Yes | 2 | MEDIUM |
| 288 | [bun](skills-bun-scan.md) | hoodini | Yes | 2 | LOW |
| 289 | [canvas-design](canvas-design-scan.md) | anthropic | Yes | 2 | MEDIUM |
| 290 | [canvas-design](skills-canvas-design-scan.md) | anthropic | Yes | 2 | MEDIUM |
| 291 | [changelog-video](heygen-com-hyperframes-agents-skills-changelog-video-scan.md) | heygen-com | Yes | 2 | MEDIUM |
| 292 | [changelog-video](heygen-com-hyperframes-claude-skills-changelog-video-scan.md) | heygen-com | Yes | 2 | MEDIUM |
| 293 | [chart-image](chart-image-generator-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 294 | [clawbridge](clawbridge-find-your-connections-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 295 | [clawbrowser](clawbrowser-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 296 | [clawkey](clawkey-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 297 | [clawops](clawops-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 298 | [code-explain](code-explainer-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 299 | [codex](codex-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 300 | [cold-email](machfive-cold-email-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 301 | [context-manager](smart-context-manager-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 302 | [core-vitals-fixer](core-web-vitals-optimizer-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 303 | [dependency-updater](dependency-updater-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 304 | [deploy](microsoft-azure-skills-github-plugins-azure-skills-skills-azure-app-onboard-deploy-scan.md) | microsoft | Yes | 2 | LOW |
| 305 | [deploy](microsoft-azure-skills-skills-azure-app-onboard-deploy-scan.md) | microsoft | Yes | 2 | LOW |
| 306 | [deploy-model](microsoft-azure-skills-github-plugins-azure-skills-skills-microsoft-foundry-models-deploy-model-scan.md) | microsoft | Yes | 2 | MEDIUM |
| 307 | [deploy-model](microsoft-azure-skills-skills-microsoft-foundry-models-deploy-model-scan.md) | microsoft | Yes | 2 | MEDIUM |
| 308 | [deps-analyzer](deps-checker-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 309 | [doc-coauthoring](skills-doc-coauthoring-scan.md) | anthropic | Yes | 2 | MEDIUM |
| 310 | [dockerfile-gen](dockerfile-generator-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 311 | [earnings-calendar](earnings-calendar-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 312 | [email](email-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 313 | [explorer](github-projects-explorer-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 314 | [expo-cicd-workflows](expo-cicd-workflows-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 315 | [ez-google](ez-google-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 316 | [feishu-api-docs](feishu-api-docs-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 317 | [feishu-bridge](feishu-bridge-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 318 | [finance](finance-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 319 | [foundry-iq](microsoft-azure-skills-github-plugins-foundry-iq-skills-skills-foundry-iq-scan.md) | microsoft | Yes | 2 | MEDIUM |
| 320 | [gemini](gemini-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 321 | [gitclassic](gitclassic-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 322 | [githunt](githunt-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 323 | [gitlab-manager](gitlab-manager-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 324 | [gold_price_mcp](gold-price-mcp-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 325 | [google-calendar](google-calendar-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 326 | [habitica](habitica-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 327 | [humanize-ai-text](humanize-ai-text-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 328 | [humanizer](humanizer-scan.md) | clawhub.ai | Yes | 2 | LOW |
| 329 | [implement](mattpocock-skills-skills-engineering-implement-scan.md) | mattpocock | **No** | 2 | **HIGH** |
| 330 | [instagram](instagram-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 331 | [intodns](intodns-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 332 | [kimi-integration](kimi-integration-scan.md) | clawhub.ai | Yes | 2 | LOW |
| 333 | [landing-gen](landing-page-generator-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 334 | [langchain](skills-langchain-scan.md) | hoodini | **No** | 2 | **HIGH** |
| 335 | [launch-strategy](launch-strategy-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 336 | [llm](llm-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 337 | [local-pandoc](md-to-office-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 338 | [mailgun](mailgun-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 339 | [memory-hygiene](memory-hygiene-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 340 | [moltbot-ha](moltbot-home-assistant-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 341 | [multi-llm](multi-llm-fallback-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 342 | [n8n-api](n8n-api-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 343 | [near-email](near-email-skill-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 344 | [openocean](openocean-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 345 | [openpet](openpet-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 346 | [paperclip](skills-paperclip-scan.md) | K-Dense-AI | Yes | 2 | MEDIUM |
| 347 | [payment](payment-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 348 | [pi-agent](skills-pi-agent-scan.md) | K-Dense-AI | **No** | 2 | **CRITICAL** |
| 349 | [prepare](microsoft-azure-skills-github-plugins-azure-skills-skills-azure-app-onboard-prepare-scan.md) | microsoft | Yes | 2 | LOW |
| 350 | [prepare](microsoft-azure-skills-skills-azure-app-onboard-prepare-scan.md) | microsoft | Yes | 2 | LOW |
| 351 | [primer-x402](primer-x402-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 352 | [querit-search](querit-search-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 353 | [ralph-loop](ralph-loop-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 354 | [react-email](react-email-skills-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 355 | [rei](rei-clawd-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 356 | [search-reddit](search-reddit-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 357 | [searxng](searxng-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 358 | [send-email](send-email-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 359 | [smtp-send](smtp-send-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 360 | [spec-to-code-compliance](plugins-spec-to-code-compliance-skills-spec-to-code-compliance-scan.md) | trailofbits | Yes | 2 | MEDIUM |
| 361 | [stock-evaluator-v3](stock-evaluator-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 362 | [subtitles](subtitles-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 363 | [tg](telegram-cli-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 364 | [timesfm-forecasting](skills-timesfm-forecasting-scan.md) | K-Dense-AI | Yes | 2 | LOW |
| 365 | [twitter](twitter-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 366 | [twitter-openclaw](x-twitter-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 367 | [ui-test](ui-test-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 368 | [upgrade-stripe](skills-upgrade-stripe-scan.md) | stripe | **No** | 2 | **CRITICAL** |
| 369 | [use-dom](use-dom-scan.md) | skills.sh | Yes | 2 | LOW |
| 370 | [veo3-video-gen](veo-3-video-gen-gemini-api-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 371 | [video-transcript](video-transcript-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 372 | [waypoint-bio](skills-waypoint-bio-scan.md) | K-Dense-AI | **No** | 2 | **HIGH** |
| 373 | [webhook-gen](webhook-generator-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 374 | [wizard](mattpocock-skills-skills-engineering-wizard-scan.md) | mattpocock | Yes | 2 | LOW |
| 375 | [writing-skills](writing-skills-scan.md) | skills.sh | Yes | 2 | MEDIUM |
| 376 | [x-api](x-api-scan.md) | clawhub.ai | **No** | 2 | **HIGH** |
| 377 | [youtube-playlist](youtube-playlist-scan.md) | clawhub.ai | Yes | 2 | MEDIUM |
| 378 | [Better Polymarket](polymarket-trading-skill-scan.md) | clawhub.ai | **No** | 1 | **HIGH** |
| 379 | [Meta Tags - SEO Tag Generator](meta-tags-seo-tag-generator-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 380 | [affirmations](101-skills-superpowers-guides-agent-affirmations-scan.md) | 101-skills | Yes | 1 | INFO |
| 381 | [affirmations](magentosh-superpowers-guides-agent-affirmations-scan.md) | magentosh | Yes | 1 | INFO |
| 382 | [affirmations](qu-skills-superpowers-guides-agent-affirmations-scan.md) | qu-skills | Yes | 1 | INFO |
| 383 | [aflpp](plugins-testing-handbook-skills-skills-aflpp-scan.md) | trailofbits | Yes | 1 | MEDIUM |
| 384 | [agent-ui](101-skills-superpowers-ui-agent-ui-scan.md) | 101-skills | Yes | 1 | INFO |
| 385 | [agent-ui](magentosh-superpowers-ui-agent-ui-scan.md) | magentosh | Yes | 1 | INFO |
| 386 | [agent-ui](qu-skills-superpowers-ui-agent-ui-scan.md) | qu-skills | Yes | 1 | INFO |
| 387 | [ai-avatar-video](101-skills-superpowers-tools-video-ai-avatar-video-scan.md) | 101-skills | Yes | 1 | INFO |
| 388 | [ai-avatar-video](magentosh-superpowers-tools-video-ai-avatar-video-scan.md) | magentosh | Yes | 1 | INFO |
| 389 | [ai-avatar-video](qu-skills-superpowers-tools-video-ai-avatar-video-scan.md) | qu-skills | Yes | 1 | INFO |
| 390 | [ai-content-pipeline](101-skills-superpowers-guides-content-ai-content-pipeline-scan.md) | 101-skills | Yes | 1 | INFO |
| 391 | [ai-content-pipeline](magentosh-superpowers-guides-content-ai-content-pipeline-scan.md) | magentosh | Yes | 1 | INFO |
| 392 | [ai-content-pipeline](qu-skills-superpowers-guides-content-ai-content-pipeline-scan.md) | qu-skills | Yes | 1 | INFO |
| 393 | [ai-image-generation](101-skills-superpowers-tools-image-ai-image-generation-scan.md) | 101-skills | Yes | 1 | INFO |
| 394 | [ai-image-generation](magentosh-superpowers-tools-image-ai-image-generation-scan.md) | magentosh | Yes | 1 | INFO |
| 395 | [ai-image-generation](qu-skills-superpowers-tools-image-ai-image-generation-scan.md) | qu-skills | Yes | 1 | INFO |
| 396 | [ai-marketing-videos](101-skills-superpowers-guides-video-ai-marketing-videos-scan.md) | 101-skills | Yes | 1 | INFO |
| 397 | [ai-marketing-videos](magentosh-superpowers-guides-video-ai-marketing-videos-scan.md) | magentosh | Yes | 1 | INFO |
| 398 | [ai-marketing-videos](qu-skills-superpowers-guides-video-ai-marketing-videos-scan.md) | qu-skills | Yes | 1 | INFO |
| 399 | [ai-music-generation](101-skills-superpowers-tools-audio-ai-music-generation-scan.md) | 101-skills | Yes | 1 | INFO |
| 400 | [ai-music-generation](magentosh-superpowers-tools-audio-ai-music-generation-scan.md) | magentosh | Yes | 1 | INFO |
| 401 | [ai-music-generation](qu-skills-superpowers-tools-audio-ai-music-generation-scan.md) | qu-skills | Yes | 1 | INFO |
| 402 | [ai-podcast](101-skills-superpowers-guides-content-ai-podcast-scan.md) | 101-skills | Yes | 1 | INFO |
| 403 | [ai-podcast](magentosh-superpowers-guides-content-ai-podcast-scan.md) | magentosh | Yes | 1 | INFO |
| 404 | [ai-podcast](qu-skills-superpowers-guides-content-ai-podcast-scan.md) | qu-skills | Yes | 1 | INFO |
| 405 | [ai-podcast-creation](101-skills-superpowers-guides-content-ai-podcast-creation-scan.md) | 101-skills | Yes | 1 | INFO |
| 406 | [ai-podcast-creation](magentosh-superpowers-guides-content-ai-podcast-creation-scan.md) | magentosh | Yes | 1 | INFO |
| 407 | [ai-podcast-creation](qu-skills-superpowers-guides-content-ai-podcast-creation-scan.md) | qu-skills | Yes | 1 | INFO |
| 408 | [ai-product-photography](101-skills-superpowers-guides-photo-ai-product-photography-scan.md) | 101-skills | Yes | 1 | INFO |
| 409 | [ai-product-photography](magentosh-superpowers-guides-photo-ai-product-photography-scan.md) | magentosh | Yes | 1 | INFO |
| 410 | [ai-product-photography](qu-skills-superpowers-guides-photo-ai-product-photography-scan.md) | qu-skills | Yes | 1 | INFO |
| 411 | [ai-rag-pipeline](101-skills-superpowers-tools-llm-ai-rag-pipeline-scan.md) | 101-skills | Yes | 1 | INFO |
| 412 | [ai-rag-pipeline](magentosh-superpowers-tools-llm-ai-rag-pipeline-scan.md) | magentosh | Yes | 1 | INFO |
| 413 | [ai-rag-pipeline](qu-skills-superpowers-tools-llm-ai-rag-pipeline-scan.md) | qu-skills | Yes | 1 | INFO |
| 414 | [ai-social-media-content](101-skills-superpowers-guides-social-ai-social-media-content-scan.md) | 101-skills | Yes | 1 | INFO |
| 415 | [ai-social-media-content](magentosh-superpowers-guides-social-ai-social-media-content-scan.md) | magentosh | Yes | 1 | INFO |
| 416 | [ai-social-media-content](qu-skills-superpowers-guides-social-ai-social-media-content-scan.md) | qu-skills | Yes | 1 | INFO |
| 417 | [ai-video-generation](101-skills-superpowers-tools-video-ai-video-generation-scan.md) | 101-skills | Yes | 1 | INFO |
| 418 | [ai-video-generation](magentosh-superpowers-tools-video-ai-video-generation-scan.md) | magentosh | Yes | 1 | INFO |
| 419 | [ai-video-generation](qu-skills-superpowers-tools-video-ai-video-generation-scan.md) | qu-skills | Yes | 1 | INFO |
| 420 | [ai-voice-cloning](101-skills-superpowers-tools-audio-ai-voice-cloning-scan.md) | 101-skills | Yes | 1 | INFO |
| 421 | [ai-voice-cloning](magentosh-superpowers-tools-audio-ai-voice-cloning-scan.md) | magentosh | Yes | 1 | INFO |
| 422 | [ai-voice-cloning](qu-skills-superpowers-tools-audio-ai-voice-cloning-scan.md) | qu-skills | Yes | 1 | INFO |
| 423 | [airunway-aks-setup](microsoft-azure-skills-github-plugins-azure-skills-skills-airunway-aks-setup-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 424 | [airunway-aks-setup](microsoft-azure-skills-skills-airunway-aks-setup-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 425 | [aks-network-capture](microsoft-azure-skills-github-plugins-aks-skills-skills-aks-network-capture-scan.md) | microsoft | **No** | 1 | **CRITICAL** |
| 426 | [algorand-vulnerability-scanner](plugins-building-secure-contracts-skills-algorand-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 427 | [alphagenome](skills-alphagenome-scan.md) | K-Dense-AI | Yes | 1 | LOW |
| 428 | [analytics-metrics](skills-analytics-metrics-scan.md) | hoodini | Yes | 1 | INFO |
| 429 | [ansible](ansible-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 430 | [app-store-screenshots](101-skills-superpowers-guides-design-app-store-screenshots-scan.md) | 101-skills | Yes | 1 | INFO |
| 431 | [app-store-screenshots](magentosh-superpowers-guides-design-app-store-screenshots-scan.md) | magentosh | Yes | 1 | INFO |
| 432 | [app-store-screenshots](qu-skills-superpowers-guides-design-app-store-screenshots-scan.md) | qu-skills | Yes | 1 | INFO |
| 433 | [ask-matt](mattpocock-skills-skills-engineering-ask-matt-scan.md) | mattpocock | Yes | 1 | INFO |
| 434 | [audit-prep-assistant](plugins-building-secure-contracts-skills-audit-prep-assistant-scan.md) | trailofbits | Yes | 1 | MEDIUM |
| 435 | [aws-account-management](skills-aws-account-management-scan.md) | hoodini | Yes | 1 | INFO |
| 436 | [aws-agentcore](skills-aws-agentcore-scan.md) | hoodini | Yes | 1 | INFO |
| 437 | [aws-strands](skills-aws-strands-scan.md) | hoodini | Yes | 1 | INFO |
| 438 | [azure-ai-voicelive-dotnet](github-skills-azure-ai-voicelive-dotnet-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 439 | [azure-aigateway](microsoft-azure-skills-github-plugins-azure-skills-skills-azure-aigateway-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 440 | [azure-aigateway](microsoft-azure-skills-skills-azure-aigateway-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 441 | [azure-app-onboard](microsoft-azure-skills-github-plugins-azure-skills-skills-azure-app-onboard-scan.md) | microsoft | **No** | 1 | **CRITICAL** |
| 442 | [azure-app-onboard](microsoft-azure-skills-skills-azure-app-onboard-scan.md) | microsoft | **No** | 1 | **CRITICAL** |
| 443 | [azure-communication-callautomation-java](github-skills-azure-communication-callautomation-java-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 444 | [azure-communication-chat-java](github-skills-azure-communication-chat-java-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 445 | [azure-containerregistry-py](github-skills-azure-containerregistry-py-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 446 | [azure-mgmt-apicenter-py](github-skills-azure-mgmt-apicenter-py-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 447 | [azure-mgmt-apimanagement-dotnet](github-skills-azure-mgmt-apimanagement-dotnet-scan.md) | microsoft | Yes | 1 | LOW |
| 448 | [azure-quotas](microsoft-azure-skills-github-plugins-azure-skills-skills-azure-quotas-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 449 | [azure-quotas](microsoft-azure-skills-skills-azure-quotas-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 450 | [azure-reliability](microsoft-azure-skills-github-plugins-azure-skills-skills-azure-reliability-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 451 | [azure-reliability](microsoft-azure-skills-skills-azure-reliability-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 452 | [azure-security-keyvault-keys-java](github-skills-azure-security-keyvault-keys-java-scan.md) | microsoft | Yes | 1 | LOW |
| 453 | [azure-security-keyvault-secrets-java](github-skills-azure-security-keyvault-secrets-java-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 454 | [background-removal](101-skills-superpowers-tools-image-background-removal-scan.md) | 101-skills | Yes | 1 | INFO |
| 455 | [background-removal](magentosh-superpowers-tools-image-background-removal-scan.md) | magentosh | Yes | 1 | INFO |
| 456 | [background-removal](qu-skills-superpowers-tools-image-background-removal-scan.md) | qu-skills | Yes | 1 | INFO |
| 457 | [birthday-reminder](Birthday%20Reminder-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 458 | [book-cover-design](101-skills-superpowers-guides-design-book-cover-design-scan.md) | 101-skills | Yes | 1 | INFO |
| 459 | [book-cover-design](magentosh-superpowers-guides-design-book-cover-design-scan.md) | magentosh | Yes | 1 | INFO |
| 460 | [book-cover-design](qu-skills-superpowers-guides-design-book-cover-design-scan.md) | qu-skills | Yes | 1 | INFO |
| 461 | [cairo-vulnerability-scanner](plugins-building-secure-contracts-skills-cairo-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 462 | [calendar](calendar-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 463 | [canopy-part-title](heygen-com-hyperframes-registry-blocks-canopy-part-title-scan.md) | heygen-com | Yes | 1 | INFO |
| 464 | [captions](captions-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 465 | [captions-overlay](heygen-com-hyperframes-agents-skills-captions-overlay-scan.md) | heygen-com | Yes | 1 | INFO |
| 466 | [captions-overlay](heygen-com-hyperframes-claude-skills-captions-overlay-scan.md) | heygen-com | Yes | 1 | INFO |
| 467 | [case-study-writing](101-skills-superpowers-guides-writing-case-study-writing-scan.md) | 101-skills | Yes | 1 | INFO |
| 468 | [case-study-writing](magentosh-superpowers-guides-writing-case-study-writing-scan.md) | magentosh | Yes | 1 | INFO |
| 469 | [case-study-writing](qu-skills-superpowers-guides-writing-case-study-writing-scan.md) | qu-skills | Yes | 1 | INFO |
| 470 | [cavecrew](juliusbrussee-caveman-plugins-caveman-skills-cavecrew-scan.md) | juliusbrussee | Yes | 1 | INFO |
| 471 | [cavecrew](juliusbrussee-caveman-skills-cavecrew-scan.md) | juliusbrussee | Yes | 1 | INFO |
| 472 | [caveman](juliusbrussee-caveman-plugins-caveman-skills-caveman-scan.md) | juliusbrussee | Yes | 1 | INFO |
| 473 | [caveman](juliusbrussee-caveman-skills-caveman-scan.md) | juliusbrussee | Yes | 1 | INFO |
| 474 | [caveman-commit](juliusbrussee-caveman-skills-caveman-commit-scan.md) | juliusbrussee | Yes | 1 | INFO |
| 475 | [caveman-discover](juliusbrussee-caveman-skills-caveman-discover-scan.md) | juliusbrussee | Yes | 1 | INFO |
| 476 | [caveman-evidence-review](juliusbrussee-caveman-skills-caveman-evidence-review-scan.md) | juliusbrussee | Yes | 1 | INFO |
| 477 | [caveman-explore](juliusbrussee-caveman-skills-caveman-explore-scan.md) | juliusbrussee | Yes | 1 | INFO |
| 478 | [caveman-help](juliusbrussee-caveman-skills-caveman-help-scan.md) | juliusbrussee | Yes | 1 | INFO |
| 479 | [caveman-learn](juliusbrussee-caveman-skills-caveman-learn-scan.md) | juliusbrussee | Yes | 1 | INFO |
| 480 | [caveman-manage](juliusbrussee-caveman-skills-caveman-manage-scan.md) | juliusbrussee | Yes | 1 | INFO |
| 481 | [caveman-optimize](juliusbrussee-caveman-skills-caveman-optimize-scan.md) | juliusbrussee | Yes | 1 | INFO |
| 482 | [caveman-review](juliusbrussee-caveman-skills-caveman-review-scan.md) | juliusbrussee | Yes | 1 | INFO |
| 483 | [caveman-setup](juliusbrussee-caveman-skills-caveman-setup-scan.md) | juliusbrussee | Yes | 1 | INFO |
| 484 | [caveman-stats](juliusbrussee-caveman-plugins-caveman-skills-caveman-stats-scan.md) | juliusbrussee | Yes | 1 | INFO |
| 485 | [caveman-stats](juliusbrussee-caveman-skills-caveman-stats-scan.md) | juliusbrussee | Yes | 1 | INFO |
| 486 | [character-design-sheet](101-skills-superpowers-guides-design-character-design-sheet-scan.md) | 101-skills | Yes | 1 | INFO |
| 487 | [character-design-sheet](magentosh-superpowers-guides-design-character-design-sheet-scan.md) | magentosh | Yes | 1 | INFO |
| 488 | [character-design-sheet](qu-skills-superpowers-guides-design-character-design-sheet-scan.md) | qu-skills | Yes | 1 | INFO |
| 489 | [chat-ui](101-skills-superpowers-ui-chat-ui-scan.md) | 101-skills | Yes | 1 | INFO |
| 490 | [chat-ui](magentosh-superpowers-ui-chat-ui-scan.md) | magentosh | Yes | 1 | INFO |
| 491 | [chat-ui](qu-skills-superpowers-ui-chat-ui-scan.md) | qu-skills | Yes | 1 | INFO |
| 492 | [chief-of-staff](mattpocock-skills-skills-in-progress-chief-of-staff-scan.md) | mattpocock | Yes | 1 | INFO |
| 493 | [chromadb-memory](chromadb-memory-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 494 | [claude-handoff](mattpocock-skills-skills-in-progress-claude-handoff-scan.md) | mattpocock | Yes | 1 | INFO |
| 495 | [clawdbot-security](clawdbot-security-audit-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 496 | [cloudflare](skills-cloudflare-scan.md) | hoodini | Yes | 1 | INFO |
| 497 | [code-review](mattpocock-skills-skills-engineering-code-review-scan.md) | mattpocock | Yes | 1 | INFO |
| 498 | [codebase-design](mattpocock-skills-skills-engineering-codebase-design-scan.md) | mattpocock | Yes | 1 | INFO |
| 499 | [codeql](plugins-testing-handbook-skills-skills-codeql-scan.md) | trailofbits | Yes | 1 | LOW |
| 500 | [competitor-teardown](101-skills-superpowers-guides-product-competitor-teardown-scan.md) | 101-skills | Yes | 1 | INFO |
| 501 | [competitor-teardown](magentosh-superpowers-guides-product-competitor-teardown-scan.md) | magentosh | Yes | 1 | INFO |
| 502 | [competitor-teardown](qu-skills-superpowers-guides-product-competitor-teardown-scan.md) | qu-skills | Yes | 1 | INFO |
| 503 | [content-repurposing](101-skills-superpowers-guides-content-content-repurposing-scan.md) | 101-skills | Yes | 1 | INFO |
| 504 | [content-repurposing](magentosh-superpowers-guides-content-content-repurposing-scan.md) | magentosh | Yes | 1 | INFO |
| 505 | [content-repurposing](qu-skills-superpowers-guides-content-content-repurposing-scan.md) | qu-skills | Yes | 1 | INFO |
| 506 | [copilot-docs](skills-copilot-docs-scan.md) | hoodini | Yes | 1 | INFO |
| 507 | [copilot-sdk](skills-copilot-sdk-scan.md) | hoodini | Yes | 1 | INFO |
| 508 | [cosmos-vulnerability-scanner](plugins-building-secure-contracts-skills-cosmos-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 509 | [customer-persona](101-skills-superpowers-guides-product-customer-persona-scan.md) | 101-skills | Yes | 1 | INFO |
| 510 | [customer-persona](magentosh-superpowers-guides-product-customer-persona-scan.md) | magentosh | Yes | 1 | INFO |
| 511 | [customer-persona](qu-skills-superpowers-guides-product-customer-persona-scan.md) | qu-skills | Yes | 1 | INFO |
| 512 | [cut-the-curve](heygen-com-hyperframes-agents-skills-cut-the-curve-scan.md) | heygen-com | Yes | 1 | INFO |
| 513 | [cut-the-curve](heygen-com-hyperframes-claude-skills-cut-the-curve-scan.md) | heygen-com | Yes | 1 | INFO |
| 514 | [daily-ai-news](daily-ai-news-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 515 | [data-visualization](101-skills-superpowers-guides-design-data-visualization-scan.md) | 101-skills | Yes | 1 | INFO |
| 516 | [data-visualization](magentosh-superpowers-guides-design-data-visualization-scan.md) | magentosh | Yes | 1 | INFO |
| 517 | [data-visualization](qu-skills-superpowers-guides-design-data-visualization-scan.md) | qu-skills | Yes | 1 | INFO |
| 518 | [database](database-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 519 | [design-mobile-apps](designed-by-ai-skills-skills-design-mobile-apps-scan.md) | designed-by-ai | Yes | 1 | INFO |
| 520 | [diagnosing-bugs](mattpocock-skills-skills-engineering-diagnosing-bugs-scan.md) | mattpocock | Yes | 1 | INFO |
| 521 | [dialogue-audio](101-skills-superpowers-tools-audio-dialogue-audio-scan.md) | 101-skills | Yes | 1 | INFO |
| 522 | [dialogue-audio](magentosh-superpowers-tools-audio-dialogue-audio-scan.md) | magentosh | Yes | 1 | INFO |
| 523 | [dialogue-audio](qu-skills-superpowers-tools-audio-dialogue-audio-scan.md) | qu-skills | Yes | 1 | INFO |
| 524 | [dnanexus-integration](skills-dnanexus-integration-scan.md) | K-Dense-AI | Yes | 1 | MEDIUM |
| 525 | [doc-coauthoring](doc-coauthoring-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 526 | [docx](docx-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 527 | [domain-modeling](mattpocock-skills-skills-engineering-domain-modeling-scan.md) | mattpocock | Yes | 1 | INFO |
| 528 | [domain-name-brainstormer](domain-name-brainstormer-scan.md) | skills.sh | Yes | 1 | MEDIUM |
| 529 | [dwlf](a-clawdbot-skill-that-gives-your-agent-native-access-to-dwlf-%E2%80%94-a-market-analysis-platform-for-crypto-and-stocks.-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 530 | [elevenlabs-dialogue](101-skills-superpowers-tools-audio-elevenlabs-dialogue-scan.md) | 101-skills | Yes | 1 | INFO |
| 531 | [elevenlabs-dialogue](magentosh-superpowers-tools-audio-elevenlabs-dialogue-scan.md) | magentosh | Yes | 1 | INFO |
| 532 | [elevenlabs-dialogue](qu-skills-superpowers-tools-audio-elevenlabs-dialogue-scan.md) | qu-skills | Yes | 1 | INFO |
| 533 | [elevenlabs-dubbing](101-skills-superpowers-tools-audio-elevenlabs-dubbing-scan.md) | 101-skills | Yes | 1 | INFO |
| 534 | [elevenlabs-dubbing](magentosh-superpowers-tools-audio-elevenlabs-dubbing-scan.md) | magentosh | Yes | 1 | INFO |
| 535 | [elevenlabs-dubbing](qu-skills-superpowers-tools-audio-elevenlabs-dubbing-scan.md) | qu-skills | Yes | 1 | INFO |
| 536 | [elevenlabs-music](101-skills-superpowers-tools-audio-elevenlabs-music-scan.md) | 101-skills | Yes | 1 | INFO |
| 537 | [elevenlabs-music](magentosh-superpowers-tools-audio-elevenlabs-music-scan.md) | magentosh | Yes | 1 | INFO |
| 538 | [elevenlabs-music](qu-skills-superpowers-tools-audio-elevenlabs-music-scan.md) | qu-skills | Yes | 1 | INFO |
| 539 | [elevenlabs-sound-effects](101-skills-superpowers-tools-audio-elevenlabs-sound-effects-scan.md) | 101-skills | Yes | 1 | INFO |
| 540 | [elevenlabs-sound-effects](magentosh-superpowers-tools-audio-elevenlabs-sound-effects-scan.md) | magentosh | Yes | 1 | INFO |
| 541 | [elevenlabs-sound-effects](qu-skills-superpowers-tools-audio-elevenlabs-sound-effects-scan.md) | qu-skills | Yes | 1 | INFO |
| 542 | [elevenlabs-stt](101-skills-superpowers-tools-audio-elevenlabs-stt-scan.md) | 101-skills | Yes | 1 | INFO |
| 543 | [elevenlabs-stt](magentosh-superpowers-tools-audio-elevenlabs-stt-scan.md) | magentosh | Yes | 1 | INFO |
| 544 | [elevenlabs-stt](qu-skills-superpowers-tools-audio-elevenlabs-stt-scan.md) | qu-skills | Yes | 1 | INFO |
| 545 | [elevenlabs-tts](101-skills-superpowers-tools-audio-elevenlabs-tts-scan.md) | 101-skills | Yes | 1 | INFO |
| 546 | [elevenlabs-tts](magentosh-superpowers-tools-audio-elevenlabs-tts-scan.md) | magentosh | Yes | 1 | INFO |
| 547 | [elevenlabs-tts](qu-skills-superpowers-tools-audio-elevenlabs-tts-scan.md) | qu-skills | Yes | 1 | INFO |
| 548 | [elevenlabs-voice-changer](101-skills-superpowers-tools-audio-elevenlabs-voice-changer-scan.md) | 101-skills | Yes | 1 | INFO |
| 549 | [elevenlabs-voice-changer](magentosh-superpowers-tools-audio-elevenlabs-voice-changer-scan.md) | magentosh | Yes | 1 | INFO |
| 550 | [elevenlabs-voice-changer](qu-skills-superpowers-tools-audio-elevenlabs-voice-changer-scan.md) | qu-skills | Yes | 1 | INFO |
| 551 | [elevenlabs-voice-isolator](101-skills-superpowers-tools-audio-elevenlabs-voice-isolator-scan.md) | 101-skills | Yes | 1 | INFO |
| 552 | [elevenlabs-voice-isolator](magentosh-superpowers-tools-audio-elevenlabs-voice-isolator-scan.md) | magentosh | Yes | 1 | INFO |
| 553 | [elevenlabs-voice-isolator](qu-skills-superpowers-tools-audio-elevenlabs-voice-isolator-scan.md) | qu-skills | Yes | 1 | INFO |
| 554 | [email-design](101-skills-superpowers-guides-design-email-design-scan.md) | 101-skills | Yes | 1 | INFO |
| 555 | [email-design](magentosh-superpowers-guides-design-email-design-scan.md) | magentosh | Yes | 1 | INFO |
| 556 | [email-design](qu-skills-superpowers-guides-design-email-design-scan.md) | qu-skills | Yes | 1 | INFO |
| 557 | [eslint-gen](eslint-config-generator-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 558 | [explainer-video-guide](101-skills-superpowers-guides-video-explainer-video-guide-scan.md) | 101-skills | Yes | 1 | INFO |
| 559 | [explainer-video-guide](magentosh-superpowers-guides-video-explainer-video-guide-scan.md) | magentosh | Yes | 1 | INFO |
| 560 | [explainer-video-guide](qu-skills-superpowers-guides-video-explainer-video-guide-scan.md) | qu-skills | Yes | 1 | INFO |
| 561 | [fal-ai](skills-fal-ai-scan.md) | hoodini | Yes | 1 | INFO |
| 562 | [figma](skills-figma-scan.md) | hoodini | Yes | 1 | INFO |
| 563 | [flux-image](101-skills-superpowers-tools-image-flux-image-scan.md) | 101-skills | Yes | 1 | INFO |
| 564 | [flux-image](magentosh-superpowers-tools-image-flux-image-scan.md) | magentosh | Yes | 1 | INFO |
| 565 | [flux-image](qu-skills-superpowers-tools-image-flux-image-scan.md) | qu-skills | Yes | 1 | INFO |
| 566 | [frontend-ui-dark-ts](github-skills-frontend-ui-dark-ts-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 567 | [gaussian-process-mlp-hybrid](ai-%E7%BC%96%E7%A0%81-prompt-skill-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 568 | [genomic-coordinates](skills-genomic-coordinates-scan.md) | K-Dense-AI | Yes | 1 | LOW |
| 569 | [gget](skills-gget-scan.md) | K-Dense-AI | Yes | 1 | LOW |
| 570 | [git-guardrails-claude-code](mattpocock-skills-skills-misc-git-guardrails-claude-code-scan.md) | mattpocock | Yes | 1 | INFO |
| 571 | [github-trending](skills-github-trending-scan.md) | hoodini | Yes | 1 | INFO |
| 572 | [glm-coding-agent](glm-coding-agent-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 573 | [google-veo](101-skills-superpowers-tools-video-google-veo-scan.md) | 101-skills | Yes | 1 | INFO |
| 574 | [google-veo](magentosh-superpowers-tools-video-google-veo-scan.md) | magentosh | Yes | 1 | INFO |
| 575 | [google-veo](qu-skills-superpowers-tools-video-google-veo-scan.md) | qu-skills | Yes | 1 | INFO |
| 576 | [google-workspace-cli](skills-google-workspace-cli-scan.md) | hoodini | Yes | 1 | INFO |
| 577 | [gpt-image](101-skills-superpowers-tools-image-gpt-image-scan.md) | 101-skills | Yes | 1 | INFO |
| 578 | [gpt-image](magentosh-superpowers-tools-image-gpt-image-scan.md) | magentosh | Yes | 1 | INFO |
| 579 | [gpt-image](qu-skills-superpowers-tools-image-gpt-image-scan.md) | qu-skills | Yes | 1 | INFO |
| 580 | [grill-me](mattpocock-skills-skills-productivity-grill-me-scan.md) | mattpocock | Yes | 1 | INFO |
| 581 | [grill-with-docs](mattpocock-skills-skills-engineering-grill-with-docs-scan.md) | mattpocock | Yes | 1 | INFO |
| 582 | [grilling](mattpocock-skills-skills-productivity-grilling-scan.md) | mattpocock | Yes | 1 | INFO |
| 583 | [handoff](mattpocock-skills-skills-productivity-handoff-scan.md) | mattpocock | Yes | 1 | INFO |
| 584 | [happyhorse](101-skills-superpowers-tools-video-happyhorse-scan.md) | 101-skills | Yes | 1 | INFO |
| 585 | [happyhorse](magentosh-superpowers-tools-video-happyhorse-scan.md) | magentosh | Yes | 1 | INFO |
| 586 | [happyhorse](qu-skills-superpowers-tools-video-happyhorse-scan.md) | qu-skills | Yes | 1 | INFO |
| 587 | [honest-agent](skills-honest-agent-scan.md) | hoodini | Yes | 1 | INFO |
| 588 | [hyperframes-registry](heygen-com-hyperframes-skills-hyperframes-registry-scan.md) | heygen-com | Yes | 1 | INFO |
| 589 | [image-to-video](101-skills-superpowers-tools-video-image-to-video-scan.md) | 101-skills | Yes | 1 | INFO |
| 590 | [image-to-video](magentosh-superpowers-tools-video-image-to-video-scan.md) | magentosh | Yes | 1 | INFO |
| 591 | [image-to-video](qu-skills-superpowers-tools-video-image-to-video-scan.md) | qu-skills | Yes | 1 | INFO |
| 592 | [image-upscaling](101-skills-superpowers-tools-image-image-upscaling-scan.md) | 101-skills | Yes | 1 | INFO |
| 593 | [image-upscaling](magentosh-superpowers-tools-image-image-upscaling-scan.md) | magentosh | Yes | 1 | INFO |
| 594 | [image-upscaling](qu-skills-superpowers-tools-image-image-upscaling-scan.md) | qu-skills | Yes | 1 | INFO |
| 595 | [imaging-data-commons](skills-imaging-data-commons-scan.md) | K-Dense-AI | Yes | 1 | MEDIUM |
| 596 | [implement-spec](mattpocock-skills-skills-engineering-implement-spec-scan.md) | mattpocock | Yes | 1 | INFO |
| 597 | [improve-codebase-architecture](mattpocock-skills-skills-engineering-improve-codebase-architecture-scan.md) | mattpocock | Yes | 1 | INFO |
| 598 | [investigate-first](juliusbrussee-caveman-skills-investigate-first-scan.md) | juliusbrussee | Yes | 1 | INFO |
| 599 | [ios-design](site-uizze.sh-ios-design-scan.md) | uizze.sh | Yes | 1 | LOW |
| 600 | [iso-standards-readiness](skills-iso-standards-readiness-scan.md) | K-Dense-AI | Yes | 1 | LOW |
| 601 | [javascript-sdk](101-skills-superpowers-sdk-javascript-sdk-scan.md) | 101-skills | Yes | 1 | INFO |
| 602 | [javascript-sdk](magentosh-superpowers-sdk-javascript-sdk-scan.md) | magentosh | Yes | 1 | INFO |
| 603 | [javascript-sdk](qu-skills-superpowers-sdk-javascript-sdk-scan.md) | qu-skills | Yes | 1 | INFO |
| 604 | [kalshi](kalshi-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 605 | [landing-page-design](101-skills-superpowers-guides-design-landing-page-design-scan.md) | 101-skills | Yes | 1 | INFO |
| 606 | [landing-page-design](magentosh-superpowers-guides-design-landing-page-design-scan.md) | magentosh | Yes | 1 | INFO |
| 607 | [landing-page-design](qu-skills-superpowers-guides-design-landing-page-design-scan.md) | qu-skills | Yes | 1 | INFO |
| 608 | [lean-build](juliusbrussee-caveman-skills-lean-build-scan.md) | juliusbrussee | Yes | 1 | INFO |
| 609 | [linkedin-content](101-skills-superpowers-guides-social-linkedin-content-scan.md) | 101-skills | Yes | 1 | INFO |
| 610 | [linkedin-content](magentosh-superpowers-guides-social-linkedin-content-scan.md) | magentosh | Yes | 1 | INFO |
| 611 | [linkedin-content](qu-skills-superpowers-guides-social-linkedin-content-scan.md) | qu-skills | Yes | 1 | INFO |
| 612 | [liteparse](skills-liteparse-scan.md) | K-Dense-AI | Yes | 1 | LOW |
| 613 | [llm-models](101-skills-superpowers-tools-llm-llm-models-scan.md) | 101-skills | Yes | 1 | INFO |
| 614 | [llm-models](magentosh-superpowers-tools-llm-llm-models-scan.md) | magentosh | Yes | 1 | INFO |
| 615 | [llm-models](qu-skills-superpowers-tools-llm-llm-models-scan.md) | qu-skills | Yes | 1 | INFO |
| 616 | [logo-design-guide](101-skills-superpowers-guides-design-logo-design-guide-scan.md) | 101-skills | Yes | 1 | INFO |
| 617 | [logo-design-guide](magentosh-superpowers-guides-design-logo-design-guide-scan.md) | magentosh | Yes | 1 | INFO |
| 618 | [logo-design-guide](qu-skills-superpowers-guides-design-logo-design-guide-scan.md) | qu-skills | Yes | 1 | INFO |
| 619 | [loop-me](mattpocock-skills-skills-in-progress-loop-me-scan.md) | mattpocock | Yes | 1 | INFO |
| 620 | [m365-agents-py](github-skills-m365-agents-py-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 621 | [marketing-psychology](marketing-psychology-scan.md) | skills.sh | Yes | 1 | MEDIUM |
| 622 | [megacave](juliusbrussee-caveman-plugins-caveman-skills-megacave-scan.md) | juliusbrussee | Yes | 1 | INFO |
| 623 | [megacave](juliusbrussee-caveman-skills-megacave-scan.md) | juliusbrussee | Yes | 1 | INFO |
| 624 | [memory-system-v2](memory-system-v2-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 625 | [mermaid-diagrams](skills-mermaid-diagrams-scan.md) | hoodini | Yes | 1 | INFO |
| 626 | [migrate-to-shoehorn](mattpocock-skills-skills-misc-migrate-to-shoehorn-scan.md) | mattpocock | Yes | 1 | INFO |
| 627 | [migration](juliusbrussee-caveman-skills-migration-scan.md) | juliusbrussee | Yes | 1 | INFO |
| 628 | [mobile-responsiveness](skills-mobile-responsiveness-scan.md) | hoodini | Yes | 1 | INFO |
| 629 | [mongodb](skills-mongodb-scan.md) | hoodini | Yes | 1 | INFO |
| 630 | [nano-banana](101-skills-superpowers-tools-image-nano-banana-scan.md) | 101-skills | Yes | 1 | INFO |
| 631 | [nano-banana](magentosh-superpowers-tools-image-nano-banana-scan.md) | magentosh | Yes | 1 | INFO |
| 632 | [nano-banana](qu-skills-superpowers-tools-image-nano-banana-scan.md) | qu-skills | Yes | 1 | INFO |
| 633 | [nano-banana-2](101-skills-superpowers-tools-image-nano-banana-2-scan.md) | 101-skills | Yes | 1 | INFO |
| 634 | [nano-banana-2](magentosh-superpowers-tools-image-nano-banana-2-scan.md) | magentosh | Yes | 1 | INFO |
| 635 | [nano-banana-2](qu-skills-superpowers-tools-image-nano-banana-2-scan.md) | qu-skills | Yes | 1 | INFO |
| 636 | [nano-banana-pro](skills-nano-banana-pro-scan.md) | hoodini | Yes | 1 | INFO |
| 637 | [newsletter-curation](101-skills-superpowers-guides-writing-newsletter-curation-scan.md) | 101-skills | Yes | 1 | INFO |
| 638 | [newsletter-curation](magentosh-superpowers-guides-writing-newsletter-curation-scan.md) | magentosh | Yes | 1 | INFO |
| 639 | [newsletter-curation](qu-skills-superpowers-guides-writing-newsletter-curation-scan.md) | qu-skills | Yes | 1 | INFO |
| 640 | [notion](notion-api-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 641 | [notion](notion-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 642 | [npkill](npkill-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 643 | [og-image-design](101-skills-superpowers-guides-design-og-image-design-scan.md) | 101-skills | Yes | 1 | INFO |
| 644 | [og-image-design](magentosh-superpowers-guides-design-og-image-design-scan.md) | magentosh | Yes | 1 | INFO |
| 645 | [og-image-design](qu-skills-superpowers-guides-design-og-image-design-scan.md) | qu-skills | Yes | 1 | INFO |
| 646 | [omero-integration](skills-omero-integration-scan.md) | K-Dense-AI | **No** | 1 | **CRITICAL** |
| 647 | [oversized-cursor](heygen-com-hyperframes-agents-skills-oversized-cursor-scan.md) | heygen-com | Yes | 1 | INFO |
| 648 | [oversized-cursor](heygen-com-hyperframes-claude-skills-oversized-cursor-scan.md) | heygen-com | Yes | 1 | INFO |
| 649 | [owasp-security](skills-owasp-security-scan.md) | hoodini | Yes | 1 | INFO |
| 650 | [p-image](101-skills-superpowers-tools-image-p-image-scan.md) | 101-skills | Yes | 1 | INFO |
| 651 | [p-image](magentosh-superpowers-tools-image-p-image-scan.md) | magentosh | Yes | 1 | INFO |
| 652 | [p-image](qu-skills-superpowers-tools-image-p-image-scan.md) | qu-skills | Yes | 1 | INFO |
| 653 | [p-video](101-skills-superpowers-tools-video-p-video-scan.md) | 101-skills | Yes | 1 | INFO |
| 654 | [p-video](magentosh-superpowers-tools-video-p-video-scan.md) | magentosh | Yes | 1 | INFO |
| 655 | [p-video](qu-skills-superpowers-tools-video-p-video-scan.md) | qu-skills | Yes | 1 | INFO |
| 656 | [p-video-avatar](101-skills-superpowers-tools-video-p-video-avatar-scan.md) | 101-skills | Yes | 1 | INFO |
| 657 | [p-video-avatar](magentosh-superpowers-tools-video-p-video-avatar-scan.md) | magentosh | Yes | 1 | INFO |
| 658 | [p-video-avatar](qu-skills-superpowers-tools-video-p-video-avatar-scan.md) | qu-skills | Yes | 1 | INFO |
| 659 | [para-second-brain](para-second-brain-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 660 | [paypal](paypal-scan.md) | clawhub.ai | **No** | 1 | **HIGH** |
| 661 | [perf-auditor](performance-auditor-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 662 | [pipedrive](pipedrive-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 663 | [pitch-deck-visuals](101-skills-superpowers-guides-design-pitch-deck-visuals-scan.md) | 101-skills | Yes | 1 | INFO |
| 664 | [pitch-deck-visuals](magentosh-superpowers-guides-design-pitch-deck-visuals-scan.md) | magentosh | Yes | 1 | INFO |
| 665 | [pitch-deck-visuals](qu-skills-superpowers-guides-design-pitch-deck-visuals-scan.md) | qu-skills | Yes | 1 | INFO |
| 666 | [playwright-skill](skills-playwright-skill-scan.md) | lackeyjb | Yes | 1 | MEDIUM |
| 667 | [popup-cro](popup-cro-scan.md) | skills.sh | Yes | 1 | MEDIUM |
| 668 | [pptx-posters](skills-pptx-posters-scan.md) | K-Dense-AI | Yes | 1 | LOW |
| 669 | [pr](mattpocock-skills-skills-engineering-pr-scan.md) | mattpocock | Yes | 1 | INFO |
| 670 | [preset](microsoft-azure-skills-github-plugins-azure-skills-skills-microsoft-foundry-models-deploy-model-preset-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 671 | [preset](microsoft-azure-skills-skills-microsoft-foundry-models-deploy-model-preset-scan.md) | microsoft | Yes | 1 | MEDIUM |
| 672 | [press-release-writing](101-skills-superpowers-guides-writing-press-release-writing-scan.md) | 101-skills | Yes | 1 | INFO |
| 673 | [press-release-writing](magentosh-superpowers-guides-writing-press-release-writing-scan.md) | magentosh | Yes | 1 | INFO |
| 674 | [press-release-writing](qu-skills-superpowers-guides-writing-press-release-writing-scan.md) | qu-skills | Yes | 1 | INFO |
| 675 | [product-changelog](101-skills-superpowers-guides-product-product-changelog-scan.md) | 101-skills | Yes | 1 | INFO |
| 676 | [product-changelog](magentosh-superpowers-guides-product-product-changelog-scan.md) | magentosh | Yes | 1 | INFO |
| 677 | [product-changelog](qu-skills-superpowers-guides-product-product-changelog-scan.md) | qu-skills | Yes | 1 | INFO |
| 678 | [product-hunt-launch](101-skills-superpowers-guides-product-product-hunt-launch-scan.md) | 101-skills | Yes | 1 | INFO |
| 679 | [product-hunt-launch](magentosh-superpowers-guides-product-product-hunt-launch-scan.md) | magentosh | Yes | 1 | INFO |
| 680 | [product-hunt-launch](qu-skills-superpowers-guides-product-product-hunt-launch-scan.md) | qu-skills | Yes | 1 | INFO |
| 681 | [product-photography](101-skills-superpowers-guides-photo-product-photography-scan.md) | 101-skills | Yes | 1 | INFO |
| 682 | [product-photography](magentosh-superpowers-guides-photo-product-photography-scan.md) | magentosh | Yes | 1 | INFO |
| 683 | [product-photography](qu-skills-superpowers-guides-photo-product-photography-scan.md) | qu-skills | Yes | 1 | INFO |
| 684 | [prompt-engineering](101-skills-superpowers-guides-prompting-prompt-engineering-scan.md) | 101-skills | Yes | 1 | INFO |
| 685 | [prompt-engineering](magentosh-superpowers-guides-prompting-prompt-engineering-scan.md) | magentosh | Yes | 1 | INFO |
| 686 | [prompt-engineering](qu-skills-superpowers-guides-prompting-prompt-engineering-scan.md) | qu-skills | Yes | 1 | INFO |
| 687 | [prototype](mattpocock-skills-skills-engineering-prototype-scan.md) | mattpocock | Yes | 1 | INFO |
| 688 | [pyhealth](skills-pyhealth-scan.md) | K-Dense-AI | Yes | 1 | INFO |
| 689 | [python-executor](101-skills-superpowers-tools-utilities-python-executor-scan.md) | 101-skills | Yes | 1 | INFO |
| 690 | [python-executor](magentosh-superpowers-tools-utilities-python-executor-scan.md) | magentosh | Yes | 1 | INFO |
| 691 | [python-executor](qu-skills-superpowers-tools-utilities-python-executor-scan.md) | qu-skills | Yes | 1 | INFO |
| 692 | [pytorch-lightning](skills-pytorch-lightning-scan.md) | K-Dense-AI | **No** | 1 | **HIGH** |
| 693 | [qiime2-amplicon](skills-qiime2-amplicon-scan.md) | K-Dense-AI | **No** | 1 | **HIGH** |
| 694 | [qmd](qmd-external-knowledge-base-search-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 695 | [qwen-image-2](101-skills-superpowers-tools-image-qwen-image-2-scan.md) | 101-skills | Yes | 1 | INFO |
| 696 | [qwen-image-2](magentosh-superpowers-tools-image-qwen-image-2-scan.md) | magentosh | Yes | 1 | INFO |
| 697 | [qwen-image-2](qu-skills-superpowers-tools-image-qwen-image-2-scan.md) | qu-skills | Yes | 1 | INFO |
| 698 | [qwen-image-2-pro](101-skills-superpowers-tools-image-qwen-image-2-pro-scan.md) | 101-skills | Yes | 1 | INFO |
| 699 | [qwen-image-2-pro](magentosh-superpowers-tools-image-qwen-image-2-pro-scan.md) | magentosh | Yes | 1 | INFO |
| 700 | [qwen-image-2-pro](qu-skills-superpowers-tools-image-qwen-image-2-pro-scan.md) | qu-skills | Yes | 1 | INFO |
| 701 | [railway](skills-railway-scan.md) | hoodini | Yes | 1 | INFO |
| 702 | [reddit](reddit-scraper-scan.md) | clawhub.ai | Yes | 1 | LOW |
| 703 | [reddit-automation](flowkit-labs-skills-reddit-automation-scan.md) | flowkit-labs | **No** | 1 | **CRITICAL** |
| 704 | [related-skill](101-skills-superpowers-tools-utilities-related-skill-scan.md) | 101-skills | Yes | 1 | INFO |
| 705 | [related-skill](magentosh-superpowers-tools-utilities-related-skill-scan.md) | magentosh | Yes | 1 | INFO |
| 706 | [related-skill](qu-skills-superpowers-tools-utilities-related-skill-scan.md) | qu-skills | Yes | 1 | INFO |
| 707 | [remotion-render](101-skills-superpowers-tools-video-remotion-render-scan.md) | 101-skills | Yes | 1 | INFO |
| 708 | [remotion-render](magentosh-superpowers-tools-video-remotion-render-scan.md) | magentosh | Yes | 1 | INFO |
| 709 | [remotion-render](qu-skills-superpowers-tools-video-remotion-render-scan.md) | qu-skills | Yes | 1 | INFO |
| 710 | [research](mattpocock-skills-skills-engineering-research-scan.md) | mattpocock | Yes | 1 | INFO |
| 711 | [retro](mattpocock-skills-skills-engineering-retro-scan.md) | mattpocock | Yes | 1 | INFO |
| 712 | [safe-refactor](juliusbrussee-caveman-skills-safe-refactor-scan.md) | juliusbrussee | Yes | 1 | INFO |
| 713 | [scaffold-exercises](mattpocock-skills-skills-misc-scaffold-exercises-scan.md) | mattpocock | Yes | 1 | INFO |
| 714 | [seam-craft](heygen-com-hyperframes-agents-skills-seam-craft-scan.md) | heygen-com | Yes | 1 | INFO |
| 715 | [seam-craft](heygen-com-hyperframes-claude-skills-seam-craft-scan.md) | heygen-com | Yes | 1 | INFO |
| 716 | [seedance](101-skills-superpowers-tools-video-seedance-scan.md) | 101-skills | Yes | 1 | INFO |
| 717 | [seedance](magentosh-superpowers-tools-video-seedance-scan.md) | magentosh | Yes | 1 | INFO |
| 718 | [seedance](qu-skills-superpowers-tools-video-seedance-scan.md) | qu-skills | Yes | 1 | INFO |
| 719 | [seo-audit](seo-audit-scan.md) | skills.sh | Yes | 1 | LOW |
| 720 | [seo-content-brief](101-skills-superpowers-guides-writing-seo-content-brief-scan.md) | 101-skills | Yes | 1 | INFO |
| 721 | [seo-content-brief](magentosh-superpowers-guides-writing-seo-content-brief-scan.md) | magentosh | Yes | 1 | INFO |
| 722 | [seo-content-brief](qu-skills-superpowers-guides-writing-seo-content-brief-scan.md) | qu-skills | Yes | 1 | INFO |
| 723 | [setup-matt-pocock-skills](mattpocock-skills-skills-engineering-setup-matt-pocock-skills-scan.md) | mattpocock | Yes | 1 | INFO |
| 724 | [setup-pre-commit](mattpocock-skills-skills-misc-setup-pre-commit-scan.md) | mattpocock | Yes | 1 | INFO |
| 725 | [setup-ts-deep-modules](mattpocock-skills-skills-in-progress-setup-ts-deep-modules-scan.md) | mattpocock | Yes | 1 | INFO |
| 726 | [shabbat-times](skills-shabbat-times-scan.md) | hoodini | Yes | 1 | INFO |
| 727 | [shorten](url-shortener-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 728 | [skill-name](templates-skill-template-scan.md) | hoodini | Yes | 1 | INFO |
| 729 | [slideshow](heygen-com-hyperframes-skills-slideshow-scan.md) | heygen-com | Yes | 1 | INFO |
| 730 | [social-media-carousel](101-skills-superpowers-guides-social-social-media-carousel-scan.md) | 101-skills | Yes | 1 | INFO |
| 731 | [social-media-carousel](magentosh-superpowers-guides-social-social-media-carousel-scan.md) | magentosh | Yes | 1 | INFO |
| 732 | [social-media-carousel](qu-skills-superpowers-guides-social-social-media-carousel-scan.md) | qu-skills | Yes | 1 | INFO |
| 733 | [solana-vulnerability-scanner](plugins-building-secure-contracts-skills-solana-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 734 | [speech-to-text](101-skills-superpowers-tools-audio-speech-to-text-scan.md) | 101-skills | Yes | 1 | INFO |
| 735 | [speech-to-text](magentosh-superpowers-tools-audio-speech-to-text-scan.md) | magentosh | Yes | 1 | INFO |
| 736 | [speech-to-text](qu-skills-superpowers-tools-audio-speech-to-text-scan.md) | qu-skills | Yes | 1 | INFO |
| 737 | [sql-assistant](sql-assistant-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 738 | [statistical-power](skills-statistical-power-scan.md) | K-Dense-AI | **No** | 1 | **HIGH** |
| 739 | [storyboard-creation](101-skills-superpowers-guides-video-storyboard-creation-scan.md) | 101-skills | Yes | 1 | INFO |
| 740 | [storyboard-creation](magentosh-superpowers-guides-video-storyboard-creation-scan.md) | magentosh | Yes | 1 | INFO |
| 741 | [storyboard-creation](qu-skills-superpowers-guides-video-storyboard-creation-scan.md) | qu-skills | Yes | 1 | INFO |
| 742 | [streme-launcher](streme-token-launcher-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 743 | [substrate-vulnerability-scanner](plugins-building-secure-contracts-skills-substrate-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 744 | [surgical-patch](juliusbrussee-caveman-skills-surgical-patch-scan.md) | juliusbrussee | Yes | 1 | INFO |
| 745 | [talking-head-production](101-skills-superpowers-guides-video-talking-head-production-scan.md) | 101-skills | Yes | 1 | INFO |
| 746 | [talking-head-production](magentosh-superpowers-guides-video-talking-head-production-scan.md) | magentosh | Yes | 1 | INFO |
| 747 | [talking-head-production](qu-skills-superpowers-guides-video-talking-head-production-scan.md) | qu-skills | Yes | 1 | INFO |
| 748 | [tdd](mattpocock-skills-skills-engineering-tdd-scan.md) | mattpocock | Yes | 1 | INFO |
| 749 | [teach](mattpocock-skills-skills-productivity-teach-scan.md) | mattpocock | Yes | 1 | INFO |
| 750 | [technical-blog-writing](101-skills-superpowers-guides-writing-technical-blog-writing-scan.md) | 101-skills | Yes | 1 | INFO |
| 751 | [technical-blog-writing](magentosh-superpowers-guides-writing-technical-blog-writing-scan.md) | magentosh | Yes | 1 | INFO |
| 752 | [technical-blog-writing](qu-skills-superpowers-guides-writing-technical-blog-writing-scan.md) | qu-skills | Yes | 1 | INFO |
| 753 | [tellurium](skills-tellurium-scan.md) | K-Dense-AI | Yes | 1 | LOW |
| 754 | [text-to-speech](101-skills-superpowers-tools-audio-text-to-speech-scan.md) | 101-skills | Yes | 1 | INFO |
| 755 | [text-to-speech](magentosh-superpowers-tools-audio-text-to-speech-scan.md) | magentosh | Yes | 1 | INFO |
| 756 | [text-to-speech](qu-skills-superpowers-tools-audio-text-to-speech-scan.md) | qu-skills | Yes | 1 | INFO |
| 757 | [to-questionnaire](mattpocock-skills-skills-productivity-to-questionnaire-scan.md) | mattpocock | Yes | 1 | INFO |
| 758 | [to-spec](mattpocock-skills-skills-engineering-to-spec-scan.md) | mattpocock | Yes | 1 | INFO |
| 759 | [to-tickets](mattpocock-skills-skills-engineering-to-tickets-scan.md) | mattpocock | Yes | 1 | INFO |
| 760 | [ton-vulnerability-scanner](plugins-building-secure-contracts-skills-ton-vulnerability-scanner-scan.md) | trailofbits | Yes | 1 | LOW |
| 761 | [tools-ui](101-skills-superpowers-ui-tools-ui-scan.md) | 101-skills | Yes | 1 | INFO |
| 762 | [tools-ui](magentosh-superpowers-ui-tools-ui-scan.md) | magentosh | Yes | 1 | INFO |
| 763 | [tools-ui](qu-skills-superpowers-ui-tools-ui-scan.md) | qu-skills | Yes | 1 | INFO |
| 764 | [transformers](skills-transformers-scan.md) | K-Dense-AI | **No** | 1 | **HIGH** |
| 765 | [triage](mattpocock-skills-skills-engineering-triage-scan.md) | mattpocock | Yes | 1 | INFO |
| 766 | [twitter-automation](101-skills-superpowers-tools-social-twitter-automation-scan.md) | 101-skills | Yes | 1 | INFO |
| 767 | [twitter-automation](magentosh-superpowers-tools-social-twitter-automation-scan.md) | magentosh | Yes | 1 | INFO |
| 768 | [twitter-automation](qu-skills-superpowers-tools-social-twitter-automation-scan.md) | qu-skills | Yes | 1 | INFO |
| 769 | [twitter-thread-creation](101-skills-superpowers-guides-social-twitter-thread-creation-scan.md) | 101-skills | Yes | 1 | INFO |
| 770 | [twitter-thread-creation](magentosh-superpowers-guides-social-twitter-thread-creation-scan.md) | magentosh | Yes | 1 | INFO |
| 771 | [twitter-thread-creation](qu-skills-superpowers-guides-social-twitter-thread-creation-scan.md) | qu-skills | Yes | 1 | INFO |
| 772 | [ui-taste](site-uizze.sh-ui-taste-scan.md) | uizze.sh | Yes | 1 | LOW |
| 773 | [ultracave](juliusbrussee-caveman-plugins-caveman-skills-ultracave-scan.md) | juliusbrussee | Yes | 1 | INFO |
| 774 | [ultracave](juliusbrussee-caveman-skills-ultracave-scan.md) | juliusbrussee | Yes | 1 | INFO |
| 775 | [ux-design-systems](skills-ux-design-systems-scan.md) | hoodini | Yes | 1 | INFO |
| 776 | [variant-analysis](plugins-variant-analysis-skills-variant-analysis-scan.md) | trailofbits | Yes | 1 | LOW |
| 777 | [vercel](skills-vercel-scan.md) | hoodini | Yes | 1 | INFO |
| 778 | [verify-and-stop](juliusbrussee-caveman-skills-verify-and-stop-scan.md) | juliusbrussee | Yes | 1 | INFO |
| 779 | [video-ad-specs](101-skills-superpowers-guides-video-video-ad-specs-scan.md) | 101-skills | Yes | 1 | INFO |
| 780 | [video-ad-specs](magentosh-superpowers-guides-video-video-ad-specs-scan.md) | magentosh | Yes | 1 | INFO |
| 781 | [video-ad-specs](qu-skills-superpowers-guides-video-video-ad-specs-scan.md) | qu-skills | Yes | 1 | INFO |
| 782 | [video-agent](video-agent-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 783 | [video-prompting-guide](101-skills-superpowers-guides-prompting-video-prompting-guide-scan.md) | 101-skills | Yes | 1 | INFO |
| 784 | [video-prompting-guide](magentosh-superpowers-guides-prompting-video-prompting-guide-scan.md) | magentosh | Yes | 1 | INFO |
| 785 | [video-prompting-guide](qu-skills-superpowers-guides-prompting-video-prompting-guide-scan.md) | qu-skills | Yes | 1 | INFO |
| 786 | [wait-what](mattpocock-skills-skills-productivity-wait-what-scan.md) | mattpocock | Yes | 1 | INFO |
| 787 | [watch-my-money](watch-my-money-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 788 | [wayfinder](mattpocock-skills-skills-engineering-wayfinder-scan.md) | mattpocock | Yes | 1 | INFO |
| 789 | [web-accessibility](skills-web-accessibility-scan.md) | hoodini | Yes | 1 | INFO |
| 790 | [web-search](101-skills-superpowers-tools-llm-web-search-scan.md) | 101-skills | Yes | 1 | INFO |
| 791 | [web-search](magentosh-superpowers-tools-llm-web-search-scan.md) | magentosh | Yes | 1 | INFO |
| 792 | [web-search](qu-skills-superpowers-tools-llm-web-search-scan.md) | qu-skills | Yes | 1 | INFO |
| 793 | [webapp-testing](webapp-testing-scan.md) | anthropic | Yes | 1 | MEDIUM |
| 794 | [widgets-ui](101-skills-superpowers-ui-widgets-ui-scan.md) | 101-skills | Yes | 1 | INFO |
| 795 | [widgets-ui](magentosh-superpowers-ui-widgets-ui-scan.md) | magentosh | Yes | 1 | INFO |
| 796 | [widgets-ui](qu-skills-superpowers-ui-widgets-ui-scan.md) | qu-skills | Yes | 1 | INFO |
| 797 | [wireframe-portal-title](heygen-com-hyperframes-registry-blocks-wireframe-portal-title-scan.md) | heygen-com | Yes | 1 | INFO |
| 798 | [writing-beats](mattpocock-skills-skills-in-progress-writing-beats-scan.md) | mattpocock | Yes | 1 | INFO |
| 799 | [writing-clearly-and-concisely](writing-clearly-and-concisely-scan.md) | skills.sh | Yes | 1 | LOW |
| 800 | [writing-for-agents](mattpocock-skills-skills-productivity-writing-for-agents-scan.md) | mattpocock | Yes | 1 | INFO |
| 801 | [writing-fragments](mattpocock-skills-skills-in-progress-writing-fragments-scan.md) | mattpocock | Yes | 1 | INFO |
| 802 | [writing-plans](writing-plans-scan.md) | skills.sh | Yes | 1 | LOW |
| 803 | [writing-shape](mattpocock-skills-skills-in-progress-writing-shape-scan.md) | mattpocock | Yes | 1 | INFO |
| 804 | [youtube-channels](youtube-channels-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 805 | [youtube-data](youtube-data-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 806 | [youtube-full](youtube-full-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 807 | [youtube-thumbnail-design](101-skills-superpowers-guides-design-youtube-thumbnail-design-scan.md) | 101-skills | Yes | 1 | INFO |
| 808 | [youtube-thumbnail-design](magentosh-superpowers-guides-design-youtube-thumbnail-design-scan.md) | magentosh | Yes | 1 | INFO |
| 809 | [youtube-thumbnail-design](qu-skills-superpowers-guides-design-youtube-thumbnail-design-scan.md) | qu-skills | Yes | 1 | INFO |
| 810 | [youtube-transcript](youtube-transcript-scan.md) | clawhub.ai | Yes | 1 | MEDIUM |
| 811 | [10-of-my-most-popular-text-to-image-series-prompts-78b0897e](test-skill-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 812 | [13c-metabolic-flux](skills-13c-metabolic-flux-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 813 | [Content ID Guide](content-id-guide-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 814 | [Search Realtime Information](realtime-web-search-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 815 | [ab-test-setup](ab-test-setup-scan.md) | skills.sh | Yes | 0 | SAFE |
| 816 | [academic-deep-research](academic-deep-research-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 817 | [actual-budget](actual-budget-cli-to-interact-with-the-actual-budget-api-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 818 | [address-sanitizer](plugins-testing-handbook-skills-skills-address-sanitizer-scan.md) | trailofbits | Yes | 0 | SAFE |
| 819 | [aeon](skills-aeon-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 820 | [agent-browser](agent-browser-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 821 | [agent-builder](agent-builder-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 822 | [agent-framework-azure-ai-py](github-skills-agent-framework-azure-ai-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 823 | [agent-md-refactor](agent-md-refactor-scan.md) | skills.sh | Yes | 0 | SAFE |
| 824 | [agenticflow-skills](agenticflow-skills-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 825 | [agents-sdk](skills-agents-sdk-scan.md) | cloudflare | Yes | 0 | SAFE |
| 826 | [airc](airc-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 827 | [aks-gpu-inference](microsoft-azure-skills-github-plugins-aks-skills-skills-aks-gpu-inference-scan.md) | microsoft | Yes | 0 | SAFE |
| 828 | [aks-known-issues](microsoft-azure-skills-github-plugins-aks-skills-skills-aks-known-issues-scan.md) | microsoft | Yes | 0 | SAFE |
| 829 | [algorand-vulnerability-scanner](plugins-building-secure-contracts-skills-algorand-vulnerabilityner-scan.md) | trailofbits | Yes | 0 | SAFE |
| 830 | [algorithmic-art](skills-algorithmic-art-scan.md) | anthropic | Yes | 0 | SAFE |
| 831 | [analytical-method-validation](skills-analytical-method-validation-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 832 | [analytics-tracking](analytics-tracking-scan.md) | skills.sh | Yes | 0 | SAFE |
| 833 | [anndata](skills-anndata-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 834 | [answeroverflow](answer-overflow-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 835 | [anterior-cingulate-memory](anterior-cingulate-memory-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 836 | [api-designer](api-designer-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 837 | [appinsights-instrumentation](microsoft-azure-skills-github-plugins-azure-skills-skills-appinsights-instrumentation-scan.md) | microsoft | Yes | 0 | SAFE |
| 838 | [appinsights-instrumentation](microsoft-azure-skills-skills-appinsights-instrumentation-scan.md) | microsoft | Yes | 0 | SAFE |
| 839 | [arbor](skills-arbor-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 840 | [arboreto](skills-arboreto-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 841 | [artifacts-builder](artifacts-builder-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 842 | [ask-questions-if-underspecified](plugins-ask-questions-if-underspecified-skills-ask-questions-if-underspecified-scan.md) | trailofbits | Yes | 0 | SAFE |
| 843 | [astropy](skills-astropy-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 844 | [atheris](plugins-testing-handbook-skills-skills-atheris-scan.md) | trailofbits | Yes | 0 | SAFE |
| 845 | [audit-context-building](plugins-audit-context-building-skills-audit-context-building-scan.md) | trailofbits | Yes | 0 | SAFE |
| 846 | [audit-website](audit-website-scan.md) | skills.sh | Yes | 0 | SAFE |
| 847 | [auto-animate](auto-animate-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 848 | [aws-cost-operations](plugins-aws-cost-ops-skills-aws-cost-operations-scan.md) | zxkane | Yes | 0 | SAFE |
| 849 | [aws-mcp-setup](plugins-aws-common-skills-aws-mcp-setup-scan.md) | zxkane | Yes | 0 | SAFE |
| 850 | [aws-serverless-eda](plugins-serverless-eda-skills-aws-serverless-eda-scan.md) | zxkane | Yes | 0 | SAFE |
| 851 | [azd-deployment](github-skills-azd-deployment-scan.md) | microsoft | Yes | 0 | SAFE |
| 852 | [azure-advisor](microsoft-azure-skills-github-plugins-azure-advisor-skills-azure-advisor-scan.md) | microsoft | Yes | 0 | SAFE |
| 853 | [azure-advisor-actionability](microsoft-azure-skills-github-plugins-azure-advisor-skills-azure-advisor-actionability-scan.md) | microsoft | Yes | 0 | SAFE |
| 854 | [azure-ai](microsoft-azure-skills-github-plugins-azure-skills-skills-azure-ai-scan.md) | microsoft | Yes | 0 | SAFE |
| 855 | [azure-ai](microsoft-azure-skills-skills-azure-ai-scan.md) | microsoft | Yes | 0 | SAFE |
| 856 | [azure-ai-agents-persistent-dotnet](github-skills-azure-ai-agents-persistent-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 857 | [azure-ai-agents-persistent-java](github-skills-azure-ai-agents-persistent-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 858 | [azure-ai-anomalydetector-java](github-skills-azure-ai-anomalydetector-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 859 | [azure-ai-contentsafety-java](github-skills-azure-ai-contentsafety-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 860 | [azure-ai-contentsafety-py](github-skills-azure-ai-contentsafety-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 861 | [azure-ai-formrecognizer-java](github-skills-azure-ai-formrecognizer-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 862 | [azure-ai-ml-py](github-skills-azure-ai-ml-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 863 | [azure-ai-openai-dotnet](github-skills-azure-ai-openai-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 864 | [azure-ai-projects-dotnet](github-skills-azure-ai-projects-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 865 | [azure-ai-projects-java](github-skills-azure-ai-projects-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 866 | [azure-ai-projects-py](github-skills-azure-ai-projects-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 867 | [azure-ai-textanalytics-py](github-skills-azure-ai-textanalytics-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 868 | [azure-ai-transcription-py](github-skills-azure-ai-transcription-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 869 | [azure-ai-translation-document-py](github-skills-azure-ai-translation-document-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 870 | [azure-ai-translation-text-py](github-skills-azure-ai-translation-text-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 871 | [azure-ai-vision-imageanalysis-java](github-skills-azure-ai-vision-imageanalysis-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 872 | [azure-ai-vision-imageanalysis-py](github-skills-azure-ai-vision-imageanalysis-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 873 | [azure-ai-voicelive-java](github-skills-azure-ai-voicelive-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 874 | [azure-ai-voicelive-py](github-skills-azure-ai-voicelive-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 875 | [azure-app-onboard-prereq](microsoft-azure-skills-github-plugins-azure-skills-skills-azure-app-onboard-prereq-scan.md) | microsoft | Yes | 0 | SAFE |
| 876 | [azure-app-onboard-prereq](microsoft-azure-skills-skills-azure-app-onboard-prereq-scan.md) | microsoft | Yes | 0 | SAFE |
| 877 | [azure-appconfiguration-java](github-skills-azure-appconfiguration-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 878 | [azure-appconfiguration-py](github-skills-azure-appconfiguration-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 879 | [azure-communication-callingserver-java](github-skills-azure-communication-callingserver-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 880 | [azure-communication-common-java](github-skills-azure-communication-common-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 881 | [azure-communication-sms-java](github-skills-azure-communication-sms-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 882 | [azure-compliance](microsoft-azure-skills-github-plugins-azure-skills-skills-azure-compliance-scan.md) | microsoft | Yes | 0 | SAFE |
| 883 | [azure-compliance](microsoft-azure-skills-skills-azure-compliance-scan.md) | microsoft | Yes | 0 | SAFE |
| 884 | [azure-compute](microsoft-azure-skills-github-plugins-azure-skills-skills-azure-compute-scan.md) | microsoft | Yes | 0 | SAFE |
| 885 | [azure-compute](microsoft-azure-skills-skills-azure-compute-scan.md) | microsoft | Yes | 0 | SAFE |
| 886 | [azure-compute-batch-java](github-skills-azure-compute-batch-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 887 | [azure-cosmos-db-py](github-skills-azure-cosmos-db-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 888 | [azure-cosmos-java](github-skills-azure-cosmos-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 889 | [azure-cosmos-py](github-skills-azure-cosmos-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 890 | [azure-data-tables-java](github-skills-azure-data-tables-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 891 | [azure-data-tables-py](github-skills-azure-data-tables-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 892 | [azure-enterprise-infra-planner](microsoft-azure-skills-github-plugins-azure-skills-skills-azure-enterprise-infra-planner-scan.md) | microsoft | Yes | 0 | SAFE |
| 893 | [azure-enterprise-infra-planner](microsoft-azure-skills-skills-azure-enterprise-infra-planner-scan.md) | microsoft | Yes | 0 | SAFE |
| 894 | [azure-eventgrid-dotnet](github-skills-azure-eventgrid-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 895 | [azure-eventgrid-java](github-skills-azure-eventgrid-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 896 | [azure-eventgrid-py](github-skills-azure-eventgrid-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 897 | [azure-eventhub-dotnet](github-skills-azure-eventhub-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 898 | [azure-eventhub-py](github-skills-azure-eventhub-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 899 | [azure-identity-dotnet](github-skills-azure-identity-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 900 | [azure-identity-java](github-skills-azure-identity-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 901 | [azure-identity-py](github-skills-azure-identity-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 902 | [azure-keyvault-py](github-skills-azure-keyvault-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 903 | [azure-kubernetes](microsoft-azure-skills-github-plugins-azure-skills-skills-azure-kubernetes-scan.md) | microsoft | Yes | 0 | SAFE |
| 904 | [azure-kubernetes](microsoft-azure-skills-skills-azure-kubernetes-scan.md) | microsoft | Yes | 0 | SAFE |
| 905 | [azure-kubernetes-app-deploy](microsoft-azure-skills-github-plugins-azure-skills-skills-azure-kubernetes-azure-kubernetes-app-deploy-scan.md) | microsoft | Yes | 0 | SAFE |
| 906 | [azure-kubernetes-app-deploy](microsoft-azure-skills-skills-azure-kubernetes-azure-kubernetes-app-deploy-scan.md) | microsoft | Yes | 0 | SAFE |
| 907 | [azure-kubernetes-automatic-readiness](microsoft-azure-skills-github-plugins-azure-skills-skills-azure-kubernetes-azure-kubernetes-automatic-readiness-scan.md) | microsoft | Yes | 0 | SAFE |
| 908 | [azure-kubernetes-automatic-readiness](microsoft-azure-skills-skills-azure-kubernetes-azure-kubernetes-automatic-readiness-scan.md) | microsoft | Yes | 0 | SAFE |
| 909 | [azure-kusto](microsoft-azure-skills-github-plugins-azure-skills-skills-azure-kusto-scan.md) | microsoft | Yes | 0 | SAFE |
| 910 | [azure-kusto](microsoft-azure-skills-skills-azure-kusto-scan.md) | microsoft | Yes | 0 | SAFE |
| 911 | [azure-kusto-graph](microsoft-azure-skills-github-plugins-azure-kusto-graph-skills-skills-azure-kusto-graph-scan.md) | microsoft | Yes | 0 | SAFE |
| 912 | [azure-kusto-irql](microsoft-azure-skills-github-plugins-azure-kusto-graph-skills-skills-azure-kusto-irql-scan.md) | microsoft | Yes | 0 | SAFE |
| 913 | [azure-kusto-irql-graph](microsoft-azure-skills-github-plugins-azure-kusto-graph-skills-skills-azure-kusto-irql-graph-scan.md) | microsoft | Yes | 0 | SAFE |
| 914 | [azure-local](microsoft-azure-skills-github-plugins-azure-local-skills-skills-azure-local-scan.md) | microsoft | Yes | 0 | SAFE |
| 915 | [azure-local-multi-rack](microsoft-azure-skills-github-plugins-azure-local-skills-skills-azure-local-multi-rack-scan.md) | microsoft | Yes | 0 | SAFE |
| 916 | [azure-maps-search-dotnet](github-skills-azure-maps-search-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 917 | [azure-messaging](microsoft-azure-skills-github-plugins-azure-skills-skills-azure-messaging-scan.md) | microsoft | Yes | 0 | SAFE |
| 918 | [azure-messaging](microsoft-azure-skills-skills-azure-messaging-scan.md) | microsoft | Yes | 0 | SAFE |
| 919 | [azure-messaging-webpubsub-java](github-skills-azure-messaging-webpubsub-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 920 | [azure-messaging-webpubsubservice-py](github-skills-azure-messaging-webpubsubservice-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 921 | [azure-mgmt-apicenter-dotnet](github-skills-azure-mgmt-apicenter-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 922 | [azure-mgmt-apimanagement-py](github-skills-azure-mgmt-apimanagement-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 923 | [azure-mgmt-applicationinsights-dotnet](github-skills-azure-mgmt-applicationinsights-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 924 | [azure-mgmt-arizeaiobservabilityeval-dotnet](github-skills-azure-mgmt-arizeaiobservabilityeval-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 925 | [azure-mgmt-botservice-dotnet](github-skills-azure-mgmt-botservice-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 926 | [azure-mgmt-botservice-py](github-skills-azure-mgmt-botservice-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 927 | [azure-mgmt-fabric-dotnet](github-skills-azure-mgmt-fabric-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 928 | [azure-mgmt-mongodbatlas-dotnet](github-skills-azure-mgmt-mongodbatlas-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 929 | [azure-mgmt-weightsandbiases-dotnet](github-skills-azure-mgmt-weightsandbiases-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 930 | [azure-microsoft-playwright-testing-ts](github-skills-azure-microsoft-playwright-testing-ts-scan.md) | microsoft | Yes | 0 | SAFE |
| 931 | [azure-monitor-ingestion-java](github-skills-azure-monitor-ingestion-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 932 | [azure-monitor-ingestion-py](github-skills-azure-monitor-ingestion-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 933 | [azure-monitor-opentelemetry-exporter-java](github-skills-azure-monitor-opentelemetry-exporter-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 934 | [azure-monitor-opentelemetry-py](github-skills-azure-monitor-opentelemetry-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 935 | [azure-monitor-query-java](github-skills-azure-monitor-query-java-scan.md) | microsoft | Yes | 0 | SAFE |
| 936 | [azure-monitor-query-py](github-skills-azure-monitor-query-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 937 | [azure-postgres-ts](github-skills-azure-postgres-ts-scan.md) | microsoft | Yes | 0 | SAFE |
| 938 | [azure-resource-lookup](microsoft-azure-skills-github-plugins-azure-skills-skills-azure-resource-lookup-scan.md) | microsoft | Yes | 0 | SAFE |
| 939 | [azure-resource-lookup](microsoft-azure-skills-skills-azure-resource-lookup-scan.md) | microsoft | Yes | 0 | SAFE |
| 940 | [azure-resource-manager-cosmosdb-dotnet](github-skills-azure-resource-manager-cosmosdb-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 941 | [azure-resource-manager-durabletask-dotnet](github-skills-azure-resource-manager-durabletask-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 942 | [azure-resource-manager-mysql-dotnet](github-skills-azure-resource-manager-mysql-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 943 | [azure-resource-manager-playwright-dotnet](github-skills-azure-resource-manager-playwright-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 944 | [azure-resource-manager-postgresql-dotnet](github-skills-azure-resource-manager-postgresql-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 945 | [azure-resource-manager-redis-dotnet](github-skills-azure-resource-manager-redis-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 946 | [azure-resource-manager-sql-dotnet](github-skills-azure-resource-manager-sql-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 947 | [azure-resource-visualizer](microsoft-azure-skills-github-plugins-azure-skills-skills-azure-resource-visualizer-scan.md) | microsoft | Yes | 0 | SAFE |
| 948 | [azure-resource-visualizer](microsoft-azure-skills-skills-azure-resource-visualizer-scan.md) | microsoft | Yes | 0 | SAFE |
| 949 | [azure-search-documents-dotnet](github-skills-azure-search-documents-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 950 | [azure-search-documents-py](github-skills-azure-search-documents-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 951 | [azure-search-nav](microsoft-azure-skills-github-plugins-aks-skills-skills-azure-search-nav-scan.md) | microsoft | Yes | 0 | SAFE |
| 952 | [azure-security-keyvault-keys-dotnet](github-skills-azure-security-keyvault-keys-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 953 | [azure-servicebus-dotnet](github-skills-azure-servicebus-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 954 | [azure-servicebus-py](github-skills-azure-servicebus-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 955 | [azure-speech-to-text-rest-py](github-skills-azure-speech-to-text-rest-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 956 | [azure-storage](microsoft-azure-skills-github-plugins-azure-skills-skills-azure-storage-scan.md) | microsoft | Yes | 0 | SAFE |
| 957 | [azure-storage](microsoft-azure-skills-skills-azure-storage-scan.md) | microsoft | Yes | 0 | SAFE |
| 958 | [azure-storage-blob-py](github-skills-azure-storage-blob-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 959 | [azure-storage-file-datalake-py](github-skills-azure-storage-file-datalake-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 960 | [azure-storage-file-share-py](github-skills-azure-storage-file-share-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 961 | [azure-storage-queue-py](github-skills-azure-storage-queue-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 962 | [basal-ganglia-memory](basal-ganglia-memory-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 963 | [bat-cat](bat-cat-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 964 | [benchling-integration](skills-benchling-integration-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 965 | [bgpt-paper-search](skills-bgpt-paper-search-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 966 | [bioservices](skills-bioservices-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 967 | [brainstorming](brainstorming-scan.md) | skills.sh | Yes | 0 | SAFE |
| 968 | [brand-guidelines](brand-guidelines-scan.md) | anthropic | Yes | 0 | SAFE |
| 969 | [brand-guidelines](skills-brand-guidelines-scan.md) | anthropic | Yes | 0 | SAFE |
| 970 | [building-ai-agent-on-cloudflare](skills-building-ai-agent-on-cloudflare-scan.md) | cloudflare | Yes | 0 | SAFE |
| 971 | [building-mcp-server-on-cloudflare](skills-building-mcp-server-on-cloudflare-scan.md) | cloudflare | Yes | 0 | SAFE |
| 972 | [building-native-ui](building-native-ui-scan.md) | skills.sh | Yes | 0 | SAFE |
| 973 | [bulk-rnaseq](skills-bulk-rnaseq-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 974 | [burpsuite-project-parser](plugins-burpsuite-project-parser-skills-scan.md) | trailofbits | Yes | 0 | SAFE |
| 975 | [cairo-vulnerability-scanner](plugins-building-secure-contracts-skills-cairo-vulnerabilityner-scan.md) | trailofbits | Yes | 0 | SAFE |
| 976 | [cantera](skills-cantera-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 977 | [capacity](microsoft-azure-skills-github-plugins-azure-skills-skills-microsoft-foundry-models-deploy-model-capacity-scan.md) | microsoft | Yes | 0 | SAFE |
| 978 | [capacity](microsoft-azure-skills-skills-microsoft-foundry-models-deploy-model-capacity-scan.md) | microsoft | Yes | 0 | SAFE |
| 979 | [cargo-fuzz](plugins-testing-handbook-skills-skills-cargo-fuzz-scan.md) | trailofbits | Yes | 0 | SAFE |
| 980 | [cellprofiler](skills-cellprofiler-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 981 | [cellxgene-census](skills-cellxgene-census-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 982 | [chirp](chirp-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 983 | [cirq](skills-cirq-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 984 | [claude-in-chrome-troubleshooting](plugins-claude-in-chrome-troubleshooting-skills-claude-in-chrome-troubleshooting-scan.md) | trailofbits | Yes | 0 | SAFE |
| 985 | [clawdbot-cost-tracker](cost-tracking-for-models-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 986 | [clawdbot-self-security-audit](clawdbot-security-check-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 987 | [clawdefender](clawdefender-openclaw-security-prompt-injection%2C-rogue-skills-etc-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 988 | [clawdex](clawdex-by-koi-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 989 | [clinical-decision-support](skills-clinical-decision-support-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 990 | [clinical-reports](skills-clinical-reports-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 991 | [cobrapy](skills-cobrapy-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 992 | [code-maturity-assessor](plugins-building-secure-contracts-skills-code-maturity-assessor-scan.md) | trailofbits | Yes | 0 | SAFE |
| 993 | [codeql](plugins-static-analysis-skills-codeql-scan.md) | trailofbits | Yes | 0 | SAFE |
| 994 | [coding-agent](multi-coding-agent-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 995 | [commit-work](commit-work-scan.md) | skills.sh | Yes | 0 | SAFE |
| 996 | [competitor-alternatives](competitor-alternatives-scan.md) | skills.sh | Yes | 0 | SAFE |
| 997 | [consciousness-council](skills-consciousness-council-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 998 | [constant-time-analysis](plugins-constant-time-analysis-skills-constant-time-analysis-scan.md) | trailofbits | Yes | 0 | SAFE |
| 999 | [copy-editing](copy-editing-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1000 | [copywriting](copywriting-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1001 | [cosmos-vulnerability-scanner](plugins-building-secure-contracts-skills-cosmos-vulnerabilityner-scan.md) | trailofbits | Yes | 0 | SAFE |
| 1002 | [cost-analysis](microsoft-azure-skills-github-plugins-azure-cost-skills-cost-analysis-scan.md) | microsoft | Yes | 0 | SAFE |
| 1003 | [cost-estimation](microsoft-azure-skills-github-plugins-azure-cost-skills-cost-estimation-scan.md) | microsoft | Yes | 0 | SAFE |
| 1004 | [cost-governance](microsoft-azure-skills-github-plugins-azure-cost-skills-cost-governance-scan.md) | microsoft | Yes | 0 | SAFE |
| 1005 | [cost-optimization](microsoft-azure-skills-github-plugins-azure-cost-skills-cost-optimization-scan.md) | microsoft | Yes | 0 | SAFE |
| 1006 | [coverage-analysis](plugins-testing-handbook-skills-skills-coverage-analysis-scan.md) | trailofbits | Yes | 0 | SAFE |
| 1007 | [create-auth-skill](better-auth-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1008 | [create-auth-skill](create-auth-skill-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1009 | [cron-mastery](cron-mastery-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1010 | [customize](microsoft-azure-skills-github-plugins-azure-skills-skills-microsoft-foundry-models-deploy-model-customize-scan.md) | microsoft | Yes | 0 | SAFE |
| 1011 | [customize](microsoft-azure-skills-skills-microsoft-foundry-models-deploy-model-customize-scan.md) | microsoft | Yes | 0 | SAFE |
| 1012 | [daily-meeting-update](daily-meeting-update-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1013 | [dask](skills-dask-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1014 | [database-lookup](skills-database-lookup-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1015 | [datalad](skills-datalad-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1016 | [datamol](skills-datamol-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1017 | [decision-trees](decision-trees-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1018 | [deepchem](skills-deepchem-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1019 | [deepspot-m](skills-deepspot-m-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1020 | [deeptools](skills-deeptools-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1021 | [depmap](skills-depmap-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1022 | [dhdna-profiler](skills-dhdna-profiler-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1023 | [diffdock](skills-diffdock-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1024 | [differential-review](plugins-differential-review-skills-differential-review-scan.md) | trailofbits | Yes | 0 | SAFE |
| 1025 | [discord-chat](discord-chat-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1026 | [discover-azure-skills](microsoft-azure-skills-github-plugins-azure-skills-skills-discover-azure-skills-scan.md) | microsoft | Yes | 0 | SAFE |
| 1027 | [discover-azure-skills](microsoft-azure-skills-skills-discover-azure-skills-scan.md) | microsoft | Yes | 0 | SAFE |
| 1028 | [dispatching-parallel-agents](dispatching-parallel-agents-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1029 | [dont-hack-me](dont-hack-me-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1030 | [dotnet-expert](dotnet-expert-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1031 | [durable-objects](skills-durable-objects-scan.md) | cloudflare | Yes | 0 | SAFE |
| 1032 | [dwarf-expert](plugins-dwarf-expert-skills-dwarf-expert-scan.md) | trailofbits | Yes | 0 | SAFE |
| 1033 | [email-best-practices](email-best-practices-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1034 | [email-sequence](email-sequence-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1035 | [entra-app-registration](microsoft-azure-skills-github-plugins-azure-skills-skills-entra-app-registration-scan.md) | microsoft | Yes | 0 | SAFE |
| 1036 | [entra-app-registration](microsoft-azure-skills-skills-entra-app-registration-scan.md) | microsoft | Yes | 0 | SAFE |
| 1037 | [entry-point-analyzer](plugins-entry-point-analyzer-skills-entry-point-analyzer-scan.md) | trailofbits | Yes | 0 | SAFE |
| 1038 | [error-guard](error-guard-%E2%80%94-control%E2%80%91plane-safety-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1039 | [etetoolkit](skills-etetoolkit-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1040 | [exa-search](skills-exa-search-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1041 | [exa-web-search-free](exa-web-search-free-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1042 | [executing-plans](executing-plans-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1043 | [experimental-design](skills-experimental-design-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1044 | [exploratory-data-analysis](skills-exploratory-data-analysis-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1045 | [expo-api-routes](expo-api-routes-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1046 | [expo-deployment](expo-deployment-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1047 | [expo-dev-client](expo-dev-client-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1048 | [expo-tailwind-setup](expo-tailwind-setup-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1049 | [ez-cronjob](ez-cronjob-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1050 | [fastapi-router-py](github-skills-fastapi-router-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 1051 | [faster-whisper](faster-whisper-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1052 | [feast](feast-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1053 | [fictiv](skills-fictiv-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1054 | [find-skills](find-skills-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1055 | [finishing-a-development-branch](finishing-a-development-branch-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1056 | [fix-review](plugins-fix-review-skills-fix-review-scan.md) | trailofbits | Yes | 0 | SAFE |
| 1057 | [flowio](skills-flowio-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1058 | [flowkit](skills-flowkit-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1059 | [fluidsim](skills-fluidsim-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1060 | [folklore-variant-evidence](skills-folklore-variant-evidence-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1061 | [form-cro](form-cro-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1062 | [foundry-iq-py](github-skills-foundry-iq-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 1063 | [free-tool-strategy](free-tool-strategy-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1064 | [frontend-design](frontend-design-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1065 | [frontend-design](skills-frontend-design-scan.md) | anthropic | Yes | 0 | SAFE |
| 1066 | [fuzzing-obstacles](plugins-testing-handbook-skills-skills-fuzzing-obstacles-scan.md) | trailofbits | Yes | 0 | SAFE |
| 1067 | [gemini-nano-banana-pro-portraits](gemini-nano-banana-pro-portraits-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1068 | [geniml](skills-geniml-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1069 | [geopandas](skills-geopandas-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1070 | [get-available-resources](skills-get-available-resources-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1071 | [ginkgo-cloud-lab](skills-ginkgo-cloud-lab-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1072 | [github-issue-creator](github-skills-github-issue-creator-scan.md) | microsoft | Yes | 0 | SAFE |
| 1073 | [gitlab-cli-skills](gitlab-cli-skills-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1074 | [google-gemini-media](google-gemini-media-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1075 | [google-imagen-3-hyperrealistic-landscape](google-imagen-3-%E8%B6%85%E5%86%99%E5%AE%9E%E9%A3%8E%E6%99%AF-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1076 | [gtars](skills-gtars-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1077 | [guidelines-advisor](plugins-building-secure-contracts-skills-guidelines-advisor-scan.md) | trailofbits | Yes | 0 | SAFE |
| 1078 | [hackernews](hacker-news-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1079 | [harness-writing](plugins-testing-handbook-skills-skills-harness-writing-scan.md) | trailofbits | Yes | 0 | SAFE |
| 1080 | [hf-mcp](hf-mcp-skills-hf-mcp-scan.md) | huggingface | Yes | 0 | SAFE |
| 1081 | [histolab](skills-histolab-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1082 | [hosted-agents-v2-py](github-skills-hosted-agents-v2-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 1083 | [hugging-face-trackio](skills-hugging-face-trackio-scan.md) | huggingface | Yes | 0 | SAFE |
| 1084 | [humanize](humanize-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1085 | [humanize-ai](humanize-ai-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1086 | [hybrid-memory](hybrid-memory-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1087 | [hypogenic](skills-hypogenic-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1088 | [hypothesis-generation](skills-hypothesis-generation-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1089 | [insecure-defaults](plugins-insecure-defaults-skills-insecure-defaults-scan.md) | trailofbits | Yes | 0 | SAFE |
| 1090 | [insula-memory](insula-memory-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1091 | [internal-comms](internal-comms-scan.md) | anthropic | Yes | 0 | SAFE |
| 1092 | [internal-comms](skills-internal-comms-scan.md) | anthropic | Yes | 0 | SAFE |
| 1093 | [interpreting-culture-index](plugins-culture-index-skills-interpreting-culture-index-scan.md) | trailofbits | Yes | 0 | SAFE |
| 1094 | [json-canvas](skills-json-canvas-scan.md) | kepano | Yes | 0 | SAFE |
| 1095 | [juicebox-v5](juicy-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1096 | [lab-hardware-cad](skills-lab-hardware-cad-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1097 | [labarchive-integration](skills-labarchive-integration-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1098 | [lamindb](skills-lamindb-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1099 | [language-learning](language-learning-tutor-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1100 | [latchbio-integration](skills-latchbio-integration-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1101 | [libfuzzer](plugins-testing-handbook-skills-skills-libfuzzer-scan.md) | trailofbits | Yes | 0 | SAFE |
| 1102 | [lobster](lobster-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1103 | [local-falcon](local-falcon-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1104 | [logseq](logseq-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1105 | [m365-agents-dotnet](github-skills-m365-agents-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 1106 | [marine-carbonate-chemistry](skills-marine-carbonate-chemistry-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1107 | [markdown-mermaid-writing](skills-markdown-mermaid-writing-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1108 | [market-research-reports](skills-market-research-reports-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1109 | [marketing-ideas](marketing-ideas-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1110 | [markitdown](skills-markitdown-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1111 | [matchms](skills-matchms-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1112 | [matlab](skills-matlab-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1113 | [matplotlib](skills-matplotlib-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1114 | [mcp-builder](github-skills-mcp-builder-scan.md) | microsoft | Yes | 0 | SAFE |
| 1115 | [mcp-builder](mcp-builder-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1116 | [mcp-builder](skills-mcp-builder-scan.md) | anthropic | Yes | 0 | SAFE |
| 1117 | [medchem](skills-medchem-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1118 | [memory-setup](memory-setup-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1119 | [mermaid-diagrams](mermaid-diagrams-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1120 | [microsoft-azure-webjobs-extensions-authentication-events-dotnet](github-skills-microsoft-azure-webjobs-extensions-authentication-events-dotnet-scan.md) | microsoft | Yes | 0 | SAFE |
| 1121 | [modern-python](plugins-modern-python-skills-modern-python-scan.md) | trailofbits | Yes | 0 | SAFE |
| 1122 | [molecular-dynamics](skills-molecular-dynamics-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1123 | [molfeat](skills-molfeat-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1124 | [molt-identity](molt-identity-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1125 | [moltbot-best-practices](moltbot-best-practices-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1126 | [native-data-fetching](native-data-fetching-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1127 | [networkx](skills-networkx-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1128 | [neurokit2](skills-neurokit2-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1129 | [neuropixels-analysis](skills-neuropixels-analysis-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1130 | [next-best-practices](next-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1131 | [nextjs-expert](nextjs-expert-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1132 | [nmrglue](skills-nmrglue-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1133 | [nuxt](nuxt-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1134 | [nwb-conversion](skills-nwb-conversion-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1135 | [obsidian-bases](skills-obsidian-bases-scan.md) | kepano | Yes | 0 | SAFE |
| 1136 | [obsidian-markdown](skills-obsidian-markdown-scan.md) | kepano | Yes | 0 | SAFE |
| 1137 | [obsidian-tasks](obsidian-tasks-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1138 | [onboarding-cro](onboarding-cro-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1139 | [onekgpd](skills-onekgpd-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1140 | [openclaw](comprehensive-skill-for-installing%2C-configuring%2C-and-managing-the-openclaw-ecosystem-gateway%2C-channels%2C-models%2C-automation%2C-nodes%2C-and-deployment-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1141 | [opencode-controller](opencode-controller-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1142 | [openpiv](skills-openpiv-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1143 | [opentrons-integration](skills-opentrons-integration-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1144 | [optimize-for-gpu](skills-optimize-for-gpu-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1145 | [pacsomatic](skills-pacsomatic-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1146 | [page-cro](page-cro-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1147 | [paid-ads](paid-ads-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1148 | [paperzilla](skills-paperzilla-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1149 | [parallel-web](skills-parallel-web-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1150 | [pathml](skills-pathml-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1151 | [pathway-enrichment](skills-pathway-enrichment-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1152 | [paywall-upgrade-cro](paywall-upgrade-cro-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1153 | [pdd](pdd-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1154 | [pdf](pdf-scan.md) | anthropic | Yes | 0 | SAFE |
| 1155 | [pdf](skills-pdf-scan.md) | anthropic | Yes | 0 | SAFE |
| 1156 | [peer-review](skills-peer-review-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1157 | [pennylane](skills-pennylane-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1158 | [phylogenetics](skills-phylogenetics-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1159 | [pkpd-modeling](skills-pkpd-modeling-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1160 | [podcast-generation](github-skills-podcast-generation-scan.md) | microsoft | Yes | 0 | SAFE |
| 1161 | [polars](skills-polars-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1162 | [polars-bio](skills-polars-bio-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1163 | [pptx](pptx-scan.md) | anthropic | Yes | 0 | SAFE |
| 1164 | [pptx](skills-pptx-scan.md) | anthropic | Yes | 0 | SAFE |
| 1165 | [preview-markdown](preview-markdown-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1166 | [pricing-strategy](pricing-strategy-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1167 | [primekg](skills-primekg-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1168 | [primer-design](skills-primer-design-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1169 | [programmatic-seo](programmatic-seo-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1170 | [property-based-testing](plugins-property-based-testing-skills-property-based-testing-scan.md) | trailofbits | Yes | 0 | SAFE |
| 1171 | [pufferlib](skills-pufferlib-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1172 | [pybamm](skills-pybamm-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1173 | [pycalphad](skills-pycalphad-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1174 | [pydantic-models-py](github-skills-pydantic-models-py-scan.md) | microsoft | Yes | 0 | SAFE |
| 1175 | [pydeseq2](skills-pydeseq2-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1176 | [pydicom](skills-pydicom-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1177 | [pylabrobot](skills-pylabrobot-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1178 | [pymatgen](skills-pymatgen-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1179 | [pymc](skills-pymc-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1180 | [pymoo](skills-pymoo-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1181 | [pyopenms](skills-pyopenms-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1182 | [pysam](skills-pysam-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1183 | [pytdc](skills-pytdc-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1184 | [python-appservice-deploy](microsoft-azure-skills-github-plugins-azure-skills-skills-python-appservice-deploy-scan.md) | microsoft | Yes | 0 | SAFE |
| 1185 | [python-appservice-deploy](microsoft-azure-skills-skills-python-appservice-deploy-scan.md) | microsoft | Yes | 0 | SAFE |
| 1186 | [pyzotero](skills-pyzotero-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1187 | [qiskit](skills-qiskit-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1188 | [qutip](skills-qutip-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1189 | [railway](railway-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1190 | [rdkit](skills-rdkit-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1191 | [react-expert](react-expert-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1192 | [react-flow-node-ts](github-skills-react-flow-node-ts-scan.md) | microsoft | Yes | 0 | SAFE |
| 1193 | [react-native-best-practices](react-native-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1194 | [readwise-mcp](readwise-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1195 | [receiving-code-review](receiving-code-review-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1196 | [referral-program](referral-program-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1197 | [relion](skills-relion-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1198 | [relsa-severity-assessment](skills-relsa-severity-assessment-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1199 | [remotion-best-practices](remotion-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1200 | [remotion-video-toolkit](remotion-video-toolkit-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1201 | [requesting-code-review](requesting-code-review-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1202 | [research-grants](skills-research-grants-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1203 | [research-paper-writer](research-paper-writer-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1204 | [resume-builder](resume-builder-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1205 | [rowan](skills-rowan-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1206 | [rssaurus-cli](rssaurus-agent-friendly-rss-feed-reader-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1207 | [sarif-parsing](plugins-static-analysis-skills-sarif-parsing-scan.md) | trailofbits | Yes | 0 | SAFE |
| 1208 | [scanpy](skills-scanpy-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1209 | [schema-markup](schema-markup-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1210 | [scholar-evaluation](skills-scholar-evaluation-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1211 | [scientific-brainstorming](skills-scientific-brainstorming-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1212 | [scientific-critical-thinking](skills-scientific-critical-thinking-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1213 | [scientific-visualization](skills-scientific-visualization-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1214 | [scientific-writing](skills-scientific-writing-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1215 | [scikit-bio](skills-scikit-bio-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1216 | [scikit-learn](skills-scikit-learn-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1217 | [scikit-survival](skills-scikit-survival-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1218 | [scvelo](skills-scvelo-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1219 | [scvi-tools](skills-scvi-tools-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1220 | [seaborn](skills-seaborn-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1221 | [secure-workflow-guide](plugins-building-secure-contracts-skills-secure-workflow-guide-scan.md) | trailofbits | Yes | 0 | SAFE |
| 1222 | [security-auditor](security-auditor-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1223 | [semgrep](plugins-static-analysis-skills-semgrep-scan.md) | trailofbits | Yes | 0 | SAFE |
| 1224 | [semgrep](plugins-testing-handbook-skills-skills-semgrep-scan.md) | trailofbits | Yes | 0 | SAFE |
| 1225 | [semgrep-rule-creator](plugins-semgrep-rule-creator-skills-semgrep-rule-creator-scan.md) | trailofbits | Yes | 0 | SAFE |
| 1226 | [semgrep-rule-variant-creator](plugins-semgrep-rule-variant-creator-skills-semgrep-rule-variant-creator-scan.md) | trailofbits | Yes | 0 | SAFE |
| 1227 | [senior-architect](senior-architect-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1228 | [senior-devops](senior-devops-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1229 | [shap](skills-shap-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1230 | [sharp-edges](plugins-sharp-edges-skills-sharp-edges-scan.md) | trailofbits | Yes | 0 | SAFE |
| 1231 | [ship-learn-next](ship-learn-next-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1232 | [signup-flow-cro](signup-flow-cro-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1233 | [simpy](skills-simpy-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1234 | [skill-creator](github-skills-skill-creator-scan.md) | microsoft | Yes | 0 | SAFE |
| 1235 | [skill-creator](jash-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1236 | [skill-creator](skill-creator-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1237 | [skill-creator](skills-skill-creator-scan.md) | anthropic | Yes | 0 | SAFE |
| 1238 | [skill-scanner](ai-skillner-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1239 | [skill-scanner](skillner-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1240 | [slack-gif-creator](skills-slack-gif-creator-scan.md) | anthropic | Yes | 0 | SAFE |
| 1241 | [slack-gif-creator](slack-gif-creator-scan.md) | anthropic | Yes | 0 | SAFE |
| 1242 | [social-content](social-content-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1243 | [solana-vulnerability-scanner](plugins-building-secure-contracts-skills-solana-vulnerabilityner-scan.md) | trailofbits | Yes | 0 | SAFE |
| 1244 | [soulcraft](soulcraft-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1245 | [spring-boot-engineer](spring-boot-engineer-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1246 | [sql-pro](sql-pro-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1247 | [ssh-essentials](ssh-essentials-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1248 | [stable-baselines3](skills-stable-baselines3-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1249 | [statistical-analysis](skills-statistical-analysis-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1250 | [statsmodels](skills-statsmodels-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1251 | [stock-market-pro](stock-market-pro-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1252 | [substrate-vulnerability-scanner](plugins-building-secure-contracts-skills-substrate-vulnerabilityner-scan.md) | trailofbits | Yes | 0 | SAFE |
| 1253 | [supabase-postgres-best-practices](supabase-postgres-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1254 | [swift-expert](swift-expert-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1255 | [sympy](skills-sympy-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1256 | [system_monitor](system-monitor-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1257 | [systematic-debugging](systematic-debugging-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1258 | [tailwind-design-system](tailwind-design-system-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1259 | [tamarind](skills-tamarind-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1260 | [template-skill](template-scan.md) | anthropic | Yes | 0 | SAFE |
| 1261 | [template-skill](template-skill-scan.md) | anthropic | Yes | 0 | SAFE |
| 1262 | [test-driven-development](test-driven-development-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1263 | [test-specialist](test-specialist-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1264 | [theme-factory](skills-theme-factory-scan.md) | anthropic | Yes | 0 | SAFE |
| 1265 | [theme-factory](theme-factory-scan.md) | anthropic | Yes | 0 | SAFE |
| 1266 | [tiledbvcf](skills-tiledbvcf-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1267 | [token-integration-analyzer](plugins-building-secure-contracts-skills-token-integration-analyzer-scan.md) | trailofbits | Yes | 0 | SAFE |
| 1268 | [ton-vulnerability-scanner](plugins-building-secure-contracts-skills-ton-vulnerabilityner-scan.md) | trailofbits | Yes | 0 | SAFE |
| 1269 | [transcribe](transcribe-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1270 | [treatment-plans](skills-treatment-plans-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1271 | [trmnl](trmnl-display-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1272 | [turborepo](turborepo-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1273 | [ui-ux-pro-max](ui-ux-pro-max-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1274 | [umap-learn](skills-umap-learn-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1275 | [uncertainty-and-units](skills-uncertainty-and-units-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1276 | [upgrading-expo](upgrading-expo-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1277 | [usfiscaldata](skills-usfiscaldata-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1278 | [vaex](skills-vaex-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1279 | [venue-templates](skills-venue-templates-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1280 | [vercel-composition-patterns](vercel-composition-patterns-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1281 | [vercel-react-best-practices](vercel-react-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1282 | [vercel-react-native-skills](vercel-react-native-skills-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1283 | [verification-before-completion](verification-before-completion-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1284 | [vue](vue-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1285 | [vue-best-practices](vue-best-practices-scan.md) | skills.sh | Yes | 0 | SAFE |
| 1286 | [web-artifacts-builder](skills-web-artifacts-builder-scan.md) | anthropic | Yes | 0 | SAFE |
| 1287 | [web-artifacts-builder](web-artifacts-builder-scan.md) | anthropic | Yes | 0 | SAFE |
| 1288 | [web-perf](skills-web-perf-scan.md) | cloudflare | Yes | 0 | SAFE |
| 1289 | [webapp-testing](skills-webapp-testing-scan.md) | anthropic | Yes | 0 | SAFE |
| 1290 | [what-if-oracle](skills-what-if-oracle-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1291 | [wordpress-pro](wordpress-pro-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1292 | [wrangler](skills-wrangler-scan.md) | cloudflare | Yes | 0 | SAFE |
| 1293 | [wycheproof](plugins-testing-handbook-skills-skills-wycheproof-scan.md) | trailofbits | Yes | 0 | SAFE |
| 1294 | [x-trends](x-trends-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1295 | [xlsx](skills-xlsx-scan.md) | anthropic | Yes | 0 | SAFE |
| 1296 | [xlsx](xlsx-scan.md) | anthropic | Yes | 0 | SAFE |
| 1297 | [youtube-api](youtube-api-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1298 | [youtube-music-cast](youtube-music-cast-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1299 | [youtube-search](youtube-search-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1300 | [yt-video-downloader](youtube-video-downloader-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1301 | [zarr-python](skills-zarr-python-scan.md) | K-Dense-AI | Yes | 0 | SAFE |
| 1302 | [zotero](zotero-scan.md) | clawhub.ai | Yes | 0 | SAFE |
| 1303 | [zustand-store-ts](github-skills-zustand-store-ts-scan.md) | microsoft | Yes | 0 | SAFE |

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

### 3. [HIGH] ai-automation-workflows - command_injection

**Rule:** ACTIVE_DYNAMIC_EXECUTION
**Location:** None

SKILL.md contains a syntax-confirmed dynamic code or process execution call in active instructions.

### 4. [HIGH] building-inferencesh-apps - data_exfiltration

**Rule:** PIPELINE_TAINT_FLOW
**Location:** None

Pipeline downloads data from the network and executes it: `curl -fsSL https://cli.inference.sh | sh`. This is a remote code execution pattern.

### 5. [HIGH] building-inferencesh-apps - data_exfiltration

**Rule:** PIPELINE_TAINT_FLOW
**Location:** None

Pipeline downloads data from the network and executes it: `curl -LsSf https://astral.sh/uv/install.sh | sh`. This is a remote code execution pattern. (Note: source host is listed as an installer endpoint, but artifact integrity was not verified.)

### 6. [HIGH] python-sdk - command_injection

**Rule:** MDBLOCK_PYTHON_EVAL_EXEC
**Location:** None

Code block in references/tool-builder.md at line 254 contains potentially dangerous Python code.

### 7. [HIGH] python-sdk - command_injection

**Rule:** MDBLOCK_PYTHON_EVAL_EXEC
**Location:** None

Code block in references/tool-builder.md at line 364 contains potentially dangerous Python code.

### 8. [HIGH] agent-tools - data_exfiltration

**Rule:** PIPELINE_TAINT_FLOW
**Location:** None

Pipeline downloads data from the network and executes it: `curl -fsSL https://cli.inference.sh | sh`. This is a remote code execution pattern.

### 9. [HIGH] infsh-cli - data_exfiltration

**Rule:** PIPELINE_TAINT_FLOW
**Location:** None

Pipeline downloads data from the network and executes it: `curl -fsSL https://cli.inference.sh | sh`. This is a remote code execution pattern.

### 10. [HIGH] agent-browser - unauthorized_tool_use

**Rule:** ALLOWED_TOOLS_BASH_VIOLATION
**Location:** None

Skill restricts tools to ['Bash(belt', '*)'] but code executes bash commands

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
- aks-gpu-inference
- aks-known-issues
- algorand-vulnerability-scanner
- algorithmic-art
- analytical-method-validation
- analytics-tracking
- anndata
- answeroverflow
- anterior-cingulate-memory
- api-designer
- appinsights-instrumentation
- appinsights-instrumentation
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
- azure-advisor
- azure-advisor-actionability
- azure-ai
- azure-ai
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
- azure-app-onboard-prereq
- azure-app-onboard-prereq
- azure-appconfiguration-java
- azure-appconfiguration-py
- azure-communication-callingserver-java
- azure-communication-common-java
- azure-communication-sms-java
- azure-compliance
- azure-compliance
- azure-compute
- azure-compute
- azure-compute-batch-java
- azure-cosmos-db-py
- azure-cosmos-java
- azure-cosmos-py
- azure-data-tables-java
- azure-data-tables-py
- azure-enterprise-infra-planner
- azure-enterprise-infra-planner
- azure-eventgrid-dotnet
- azure-eventgrid-java
- azure-eventgrid-py
- azure-eventhub-dotnet
- azure-eventhub-py
- azure-identity-dotnet
- azure-identity-java
- azure-identity-py
- azure-keyvault-py
- azure-kubernetes
- azure-kubernetes
- azure-kubernetes-app-deploy
- azure-kubernetes-app-deploy
- azure-kubernetes-automatic-readiness
- azure-kubernetes-automatic-readiness
- azure-kusto
- azure-kusto
- azure-kusto-graph
- azure-kusto-irql
- azure-kusto-irql-graph
- azure-local
- azure-local-multi-rack
- azure-maps-search-dotnet
- azure-messaging
- azure-messaging
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
- azure-resource-lookup
- azure-resource-lookup
- azure-resource-manager-cosmosdb-dotnet
- azure-resource-manager-durabletask-dotnet
- azure-resource-manager-mysql-dotnet
- azure-resource-manager-playwright-dotnet
- azure-resource-manager-postgresql-dotnet
- azure-resource-manager-redis-dotnet
- azure-resource-manager-sql-dotnet
- azure-resource-visualizer
- azure-resource-visualizer
- azure-search-documents-dotnet
- azure-search-documents-py
- azure-search-nav
- azure-security-keyvault-keys-dotnet
- azure-servicebus-dotnet
- azure-servicebus-py
- azure-speech-to-text-rest-py
- azure-storage
- azure-storage
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
- capacity
- capacity
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
- cost-analysis
- cost-estimation
- cost-governance
- cost-optimization
- coverage-analysis
- create-auth-skill
- create-auth-skill
- cron-mastery
- customize
- customize
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
- discover-azure-skills
- discover-azure-skills
- dispatching-parallel-agents
- dont-hack-me
- dotnet-expert
- durable-objects
- dwarf-expert
- email-best-practices
- email-sequence
- entra-app-registration
- entra-app-registration
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
- python-appservice-deploy
- python-appservice-deploy
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
- **Scan Date:** 2026-10-22T14:35:50.937456

### Limitations

- VirusTotal binary scanning not used (requires API key)
- No runtime verification - static and semantic analysis only
