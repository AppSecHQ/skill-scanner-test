# Agent Skill Security Scan Report

**Skill:** clickup
**Directory:** /workspace/skills/clawhub-clickup-skill
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 37.58s
**Timestamp:** 2026-02-01T20:19:28.958637

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 1
- **Medium:** 1
- **Low:** 1
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Hardcoded API Token Exposure Risk

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** scripts/clickup_client.py

**Description:** The skill requires users to set CLICKUP_API_TOKEN as an environment variable, which could lead to credential exposure if not properly managed. The token is passed directly in Authorization headers and could be logged, cached, or exposed through error messages. Additionally, there's no validation or sanitization of the token value, and no guidance on secure token storage or rotation.

### MEDIUM Severity

#### [MEDIUM] Potential Command Injection via Unvalidated User Input

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** scripts/clickup_client.py

**Description:** The script accepts command-line arguments and JSON parameters that are passed directly to API methods without validation or sanitization. While the requests library handles URL encoding, there's no input validation for special characters, path traversal attempts, or malicious payloads in task names, descriptions, or other fields. An attacker could potentially inject malicious content that gets stored and later executed in other contexts.

### LOW Severity

#### [LOW] No Rate Limiting Protection in Client

**Severity:** LOW
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** scripts/clickup_client.py

**Description:** While the API reference mentions ClickUp's rate limits (100 requests/minute per token), the client implementation does not include any rate limiting protection, retry logic with backoff, or request throttling. This could lead to API quota exhaustion, service disruption, or temporary account suspension if the skill is used intensively.

## Analyzers

The following analyzers were used:

- static_analyzer
- llm_analyzer
- meta_analyzer
