# Agent Skill Security Scan Report

**Skill:** ABM Outbound
**Directory:** /workspace/skills/clawhub-abm-outbound
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 58.93s
**Timestamp:** 2026-02-05T17:46:28.254163

## Summary

- **Total Findings:** 7
- **Critical:** 1
- **High:** 2
- **Medium:** 3
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Hardcoded API Keys Required in Environment Variables

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires users to export sensitive API keys (APIFY_API_KEY, APOLLO_API_KEY, SCRIBELESS_API_KEY) as environment variables. The instructions explicitly show 'export APIFY_API_KEY="your_key"' commands. If users follow these instructions literally or store keys insecurely, this creates a credential exposure risk. Additionally, there's no guidance on secure credential management, key rotation, or using credential managers.

### HIGH Severity

#### [HIGH] Personal Data Collection and Transmission Without Consent Framework

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill orchestrates collection and transmission of highly sensitive personal data (names, emails, phone numbers, physical mailing addresses) across multiple third-party services (Apify, Apollo, Scribeless) without any documented consent verification, data protection measures, or privacy safeguards. This creates significant privacy and compliance risks under GDPR, CCPA, and other data protection regulations.

#### [HIGH] Deceptive Skill Description Masks Aggressive Data Harvesting

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill description presents this as a 'secret weapon for standing out in crowded inboxes' and 'multi-channel ABM automation', but obscures the aggressive nature of the data collection: scraping LinkedIn profiles without authorization, purchasing personal phone numbers and physical addresses via skip tracing services, and sending unsolicited physical mail. The description doesn't clearly communicate that this is a cold outreach tool that collects personal data from multiple sources.

### MEDIUM Severity

#### [MEDIUM] No Rate Limiting or Resource Controls on API Calls

**Severity:** MEDIUM
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** SKILL.md

**Description:** The skill provides curl commands for bulk API operations (bulk_match, run-sync-get-dataset-items) without any rate limiting, retry logic, or resource consumption controls. Users could inadvertently trigger excessive API calls, exhaust API quotas, incur unexpected costs, or trigger rate limit bans from third-party services.

#### [MEDIUM] Potential Violation of LinkedIn Terms of Service

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill instructs users to scrape LinkedIn profiles using third-party services (Apify's LinkedIn scraper), which likely violates LinkedIn's Terms of Service and User Agreement. LinkedIn explicitly prohibits scraping, automated data collection, and use of bots. This could expose users to legal action from LinkedIn and account termination.

#### [MEDIUM] Skip Trace Service Enables Stalking and Privacy Invasion

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill integrates skip tracing services to obtain physical mailing addresses of prospects. Skip tracing is typically used for debt collection and can enable stalking, harassment, or unwanted contact. The skill provides no ethical guidelines, consent requirements, or warnings about misuse of this capability.

### LOW Severity

#### [LOW] Unauthorized Multi-Service Tool Chaining for Data Exfiltration

**Severity:** LOW
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill implements an automated pipeline that chains multiple external API services (Apify → Apollo → Apify Skip Trace → Scribeless) to collect, enrich, and transmit personal data without user confirmation at each step. This tool chaining pattern enables automated data exfiltration across service boundaries. The 'allowed-tools' field is not specified, providing no restrictions on what the agent can execute.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
