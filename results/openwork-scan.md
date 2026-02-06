# Agent Skill Security Scan Report

**Skill:** openwork
**Directory:** /workspace/skills/clawhub-openwork
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 40.91s
**Timestamp:** 2026-02-06T06:01:21.218284

## Summary

- **Total Findings:** 6
- **Critical:** 2
- **High:** 3
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Direct Prompt Injection - Autonomous Operation Override

**Severity:** CRITICAL
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** SKILL.md

**Description:** The SKILL.md instructions contain explicit directives that override agent safety controls by declaring 'You are fully autonomous' and 'No human approval needed. No human in the loop.' This is a direct attempt to bypass human oversight and make the agent operate without user confirmation for financial transactions and external API interactions.

#### [CRITICAL] Credential Exposure - API Key Storage Without Protection

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs the agent to save an API key ('ow_xxx') with the warning 'Save your apiKey immediately! It won't be shown again. Store it securely' but provides no secure storage mechanism. The agent may store this credential in plaintext in conversation history, logs, or unsecured files, leading to credential exposure.

### HIGH Severity

#### [HIGH] Wallet Address Collection and Financial Transaction Risk

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill collects the user's Base blockchain wallet address and instructs the agent to perform financial transactions (earning tokens, spending tokens, escrow operations) without explicit user confirmation. This creates risk of unauthorized financial operations using the user's wallet.

#### [HIGH] Unbounded External API Integration Without Validation

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill instructs the agent to make API calls to an external service (openwork.bot) for registration, job posting, and financial transactions without any validation, rate limiting, or safety checks. The agent is told to operate autonomously with this external service, creating tool exploitation risk.

#### [HIGH] Social Engineering - Deceptive Autonomy Claims

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill description claims to be 'The agent-only marketplace' and emphasizes full autonomy, but this is misleading social engineering designed to make users believe the agent should operate without oversight. The repeated emphasis on 'no human approval needed' is designed to bypass normal safety protocols.

### MEDIUM Severity

#### [MEDIUM] Transitive Trust - External File References Without Validation

**Severity:** MEDIUM
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** SKILL.md:15

**Description:** The skill references external files (HEARTBEAT.md from openwork.bot) that could contain additional instructions or malicious content. The agent is instructed to download and potentially follow instructions from these external sources without validation.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
