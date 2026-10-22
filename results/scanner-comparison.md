# Scanner comparison: Cisco skill-scanner vs NVIDIA SkillSpector (static)

Skills compared: 1302. Both scanners ran without an LLM.

### Loose tier: Cisco any finding vs SkillSpector CAUTION or DO_NOT_INSTALL

| | SkillSpector flagged | SkillSpector not flagged |
|---|---|---|
| Cisco flagged | 189 | 22 |
| Cisco not flagged | 795 | 296 |

Agreement 37.2%, Cohen's kappa 0.07

### Strict tier: Cisco HIGH/CRITICAL vs SkillSpector DO_NOT_INSTALL

| | SkillSpector flagged | SkillSpector not flagged |
|---|---|---|
| Cisco flagged | 82 | 129 |
| Cisco not flagged | 135 | 956 |

Agreement 79.7%, Cohen's kappa 0.26

## By source (loose tier)

| Source | Skills | Both | Cisco only | SkillSpector only | Neither |
|---|---|---|---|---|---|
| clawhub.ai | 325 | 103 | 19 | 140 | 63 |
| K-Dense-AI | 177 | 25 | 0 | 152 | 0 |
| unknown | 107 | 2 | 0 | 89 | 16 |
| microsoft | 93 | 13 | 0 | 80 | 0 |
| 101-skills | 86 | 6 | 0 | 28 | 52 |
| magentosh | 86 | 6 | 0 | 28 | 52 |
| qu-skills | 86 | 6 | 0 | 28 | 52 |
| skills.sh | 75 | 4 | 1 | 62 | 8 |
| trailofbits | 58 | 6 | 0 | 48 | 4 |
| mattpocock | 38 | 0 | 1 | 21 | 16 |
| anthropic | 29 | 1 | 0 | 21 | 7 |
| juliusbrussee | 28 | 2 | 0 | 6 | 20 |
| open.feishu.cn | 28 | 0 | 0 | 28 | 0 |
| heygen-com | 26 | 8 | 0 | 18 | 0 |
| hoodini | 26 | 1 | 1 | 21 | 3 |
| huggingface | 9 | 2 | 0 | 6 | 1 |
| cloudflare | 6 | 0 | 0 | 6 | 0 |
| zxkane | 5 | 0 | 0 | 4 | 1 |
| kepano | 3 | 0 | 0 | 3 | 0 |
| uizze.sh | 2 | 0 | 0 | 2 | 0 |
| stripe | 2 | 1 | 0 | 0 | 1 |
| designed-by-ai | 1 | 0 | 0 | 1 | 0 |
| jthack | 1 | 0 | 0 | 1 | 0 |
| flowkit-labs | 1 | 1 | 0 | 0 | 0 |
| leonxlnx | 1 | 1 | 0 | 0 | 0 |
| moltbook.com | 1 | 1 | 0 | 0 | 0 |
| sawyerhood | 1 | 0 | 0 | 1 | 0 |
| lackeyjb | 1 | 0 | 0 | 1 | 0 |

## Cisco finding categories

| Category | Skills |
|---|---|
| policy_violation | 485 |
| data_exfiltration | 302 |
| social_engineering | 173 |
| unauthorized_tool_use | 167 |
| command_injection | 163 |
| resource_abuse | 86 |
| prompt_injection | 53 |
| obfuscation | 41 |
| transitive_trust_abuse | 8 |
| skill_discovery_abuse | 6 |
| hardcoded_secrets | 5 |
| tool_chaining_abuse | 4 |
| supply_chain_attack | 3 |
| autonomy_abuse | 1 |

## SkillSpector finding categories

| Category | Skills |
|---|---|
| MCP Rug Pull | 389 |
| MCP Least Privilege | 230 |
| Data Exfiltration | 209 |
| Privilege Escalation | 209 |
| Excessive Agency | 194 |
| analysis-evasion | 172 |
| Tool Misuse | 139 |
| Rogue Agent | 101 |
| Supply Chain | 99 |
| Dangerous Code Execution | 75 |
| Prompt Injection | 41 |
| Memory Poisoning | 40 |
| Anti-Refusal | 34 |
| YARA Match | 31 |
| Data Flow | 31 |
| Output Handling | 25 |
| System Prompt Leakage | 24 |
| Agent Snooping | 20 |
| Trigger Abuse | 7 |
| Server-Side Request Forgery | 2 |

## Largest disagreements

Skills one scanner rates most severely while the other calls safe.

| Skill | Source | Cisco | SkillSpector |
|---|---|---|---|
| earnings-calendar | clawhub.ai | MEDIUM (2) | DO_NOT_INSTALL 100 (7) |
| azure-prepare | microsoft | MEDIUM (5) | DO_NOT_INSTALL 100 (69) |
| azure-upgrade | microsoft | MEDIUM (3) | DO_NOT_INSTALL 100 (15) |
| foundry-iq | microsoft | MEDIUM (2) | DO_NOT_INSTALL 100 (50) |
| azure-prepare | microsoft | MEDIUM (5) | DO_NOT_INSTALL 100 (69) |
| azure-upgrade | microsoft | MEDIUM (3) | DO_NOT_INSTALL 100 (15) |
| testing-handbook-generator | trailofbits | MEDIUM (3) | DO_NOT_INSTALL 100 (14) |
| searxng | clawhub.ai | MEDIUM (2) | DO_NOT_INSTALL 100 (11) |
| dev-browser | sawyerhood | MEDIUM (7) | DO_NOT_INSTALL 100 (41) |
| hugging-face-evaluation | huggingface | MEDIUM (96) | DO_NOT_INSTALL 100 (35) |
| hugging-face-model-trainer | huggingface | MEDIUM (14) | DO_NOT_INSTALL 100 (26) |
| paper-lookup | K-Dense-AI | MEDIUM (7) | DO_NOT_INSTALL 100 (57) |
| paperclip | K-Dense-AI | MEDIUM (2) | DO_NOT_INSTALL 100 (13) |
| protocolsio-integration | K-Dense-AI | MEDIUM (3) | DO_NOT_INSTALL 100 (24) |
| video-agent | clawhub.ai | MEDIUM (1) | DO_NOT_INSTALL 100 (6) |
| writing-skills | skills.sh | MEDIUM (2) | DO_NOT_INSTALL 100 (21) |
| glm-coding-agent | clawhub.ai | MEDIUM (1) | DO_NOT_INSTALL 99 (18) |
| querit-search | clawhub.ai | MEDIUM (2) | DO_NOT_INSTALL 99 (14) |
| azure-cloud-migrate | microsoft | MEDIUM (8) | DO_NOT_INSTALL 95 (11) |
| azure-cloud-migrate | microsoft | MEDIUM (8) | DO_NOT_INSTALL 95 (11) |
| azure-ai-evaluation-py | None | MEDIUM (2) | DO_NOT_INSTALL 92 (6) |
| codex | skills.sh | MEDIUM (2) | DO_NOT_INSTALL 90 (6) |
| azure-validate | microsoft | MEDIUM (5) | DO_NOT_INSTALL 89 (22) |
| azure-validate | microsoft | MEDIUM (5) | DO_NOT_INSTALL 89 (22) |
| aks-troubleshooting | microsoft | MEDIUM (3) | DO_NOT_INSTALL 88 (8) |
| aws-agentic-ai | zxkane | MEDIUM (2) | DO_NOT_INSTALL 82 (16) |
| deploy | microsoft | LOW (2) | DO_NOT_INSTALL 100 (12) |
| deploy | microsoft | LOW (2) | DO_NOT_INSTALL 100 (12) |
| hugging-face-cli | huggingface | LOW (5) | DO_NOT_INSTALL 100 (19) |
| browse | clawhub.ai | MEDIUM (7) | DO_NOT_INSTALL 77 (22) |
| generate-image | K-Dense-AI | MEDIUM (3) | DO_NOT_INSTALL 76 (8) |
| hyperframes-cli | heygen-com | MEDIUM (6) | DO_NOT_INSTALL 74 (224) |
| azure-diagnostics | microsoft | MEDIUM (2) | DO_NOT_INSTALL 74 (6) |
| azure-diagnostics | microsoft | MEDIUM (2) | DO_NOT_INSTALL 74 (6) |
| dnanexus-integration | K-Dense-AI | MEDIUM (1) | DO_NOT_INSTALL 72 (10) |
| clawdbot-security | clawhub.ai | MEDIUM (1) | DO_NOT_INSTALL 71 (12) |
| remotion-to-hyperframes | heygen-com | MEDIUM (17) | DO_NOT_INSTALL 71 (41) |
| streme-launcher | clawhub.ai | MEDIUM (1) | DO_NOT_INSTALL 71 (18) |
| playwright-skill | lackeyjb | MEDIUM (1) | DO_NOT_INSTALL 70 (20) |
| algorand-vulnerability-scanner | trailofbits | LOW (1) | DO_NOT_INSTALL 87 (9) |
