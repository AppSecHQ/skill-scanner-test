# Agent Skill Security Scan Report

**Skill:** gold_price_mcp
**Directory:** ./skills/clawhub-gold-price-mcp
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 0.36s
**Timestamp:** 2026-02-03T15:59:33.954686

## Summary

- **Total Findings:** 9
- **Critical:** 0
- **High:** 1
- **Medium:** 5
- **Low:** 3
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Suspicious URL detected: https://api.chnwt.dev/thai-gold-api/latest

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/clawhub-gold-price-mcp/gold-price-mcp.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

### MEDIUM Severity

#### [MEDIUM] User input used in command substitution - potential injection risk

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** COMMAND_INJECTION_USER_INPUT
**Location:** run.sh:4

**Description:** Pattern detected: $(dirname "$0")

#### [MEDIUM] User input used in command substitution - potential injection risk

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** COMMAND_INJECTION_USER_INPUT
**Location:** run.sh:7

**Description:** Pattern detected: $(dirname "$0")

#### [MEDIUM] HTTP client library imports that enable external communication

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_NETWORK_REQUESTS
**Location:** gold-price-mcp.py:11

**Description:** Pattern detected: import httpx

#### [MEDIUM] HTTP client library imports that enable external communication

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_NETWORK_REQUESTS
**Location:** test_api.py:8

**Description:** Pattern detected: import httpx

#### [MEDIUM] Undeclared network usage

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** TOOL_ABUSE_UNDECLARED_NETWORK

**Description:** Skill code uses network libraries but doesn't declare network requirement

### LOW Severity

#### [LOW] Skill name does not follow agent skills naming rules

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_INVALID_NAME
**Location:** SKILL.md

**Description:** Skill name 'gold_price_mcp' is invalid. Agent skills require lowercase letters, numbers, and hyphens only, with a maximum length of 64 characters.

#### [LOW] Skill does not specify a license

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

#### [LOW] Skill description is too short

**Severity:** LOW
**Category:** social_engineering
**Rule ID:** TRIGGER_DESCRIPTION_TOO_SHORT
**Location:** SKILL.md

**Description:** Description has only 1 words. Short descriptions may not provide enough context for the agent to determine when this skill should be used.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
