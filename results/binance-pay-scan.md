# Agent Skill Security Scan Report

**Skill:** binance-pay
**Directory:** /workspace/skills/clawhub-binance-pay
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 41.71s
**Timestamp:** 2026-02-05T20:31:40.837333

## Summary

- **Total Findings:** 7
- **Critical:** 0
- **High:** 1
- **Medium:** 3
- **Low:** 3
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Hardcoded API Credentials Exposure Risk

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires sensitive Binance Pay API credentials (BINANCE_PAY_API_KEY, BINANCE_PAY_SECRET, BINANCE_PAY_MERCHANT_ID) to be stored as environment variables. While environment variables are better than hardcoding, the instructions demonstrate direct usage of these credentials in bash commands without any validation, sanitization, or secure handling guidance. If an agent executes these commands with user-controlled input, credentials could be exposed through command injection or logging.

### MEDIUM Severity

#### [MEDIUM] Command Injection Risk in Signature Generation

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The generate_signature() function uses echo with user-controlled payload data without proper sanitization. The payload variable is constructed from user input (order amounts, product names, merchant trade numbers) and directly interpolated into shell commands. An attacker could inject malicious commands through specially crafted input fields like 'goodsName' or 'merchantTradeNo' that could break out of the echo command or the openssl pipeline.

#### [MEDIUM] JSON Injection via Unvalidated User Input

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The skill constructs JSON payloads using shell string interpolation with user-controlled values (merchantTradeNo, orderAmount, goodsName, etc.) without proper JSON escaping or validation. An attacker could inject malicious JSON by providing input like '"}, "maliciousField": "value' in fields like goodsName, potentially manipulating the API request structure or injecting additional parameters.

#### [MEDIUM] Unrestricted Bash Tool Usage Without allowed-tools Declaration

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill provides extensive bash command examples that make network requests, handle sensitive credentials, and perform cryptographic operations, but does not declare 'allowed-tools' in the manifest. While this field is optional, its absence means there are no documented restrictions on what tools the agent can use when executing this skill. The skill requires 'curl' and 'jq' binaries but doesn't validate their presence or versions before use.

### LOW Severity

#### [LOW] Skill does not specify a license

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

#### [LOW] Missing Metadata Fields in Manifest

**Severity:** LOW
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill manifest is missing several optional but recommended metadata fields including 'license', 'compatibility', and 'allowed-tools'. While not a direct security threat, missing metadata reduces transparency about the skill's intended usage, licensing terms, and compatibility requirements. The absence of 'allowed-tools' means users cannot verify intended tool restrictions.

#### [LOW] No Rate Limiting or Error Handling Guidance

**Severity:** LOW
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** SKILL.md

**Description:** The skill provides API integration examples without any guidance on rate limiting, retry logic, or error handling. The Binance Pay API likely has rate limits, but the skill doesn't document them or provide safeguards against excessive API calls. This could lead to API throttling, account suspension, or denial of service if the agent makes unbounded requests.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
