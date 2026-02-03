# Agent Skill Security Scan Report

**Skill:** Better Polymarket
**Directory:** ./skills/clawhub-polymarket-all-in-one
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 2.11s
**Timestamp:** 2026-02-03T16:11:23.928097

## Summary

- **Total Findings:** 6
- **Critical:** 0
- **High:** 2
- **Medium:** 2
- **Low:** 2
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Shell command execution with shell=True enabled

**Severity:** HIGH
**Category:** command_injection
**Rule ID:** COMMAND_INJECTION_SHELL_TRUE
**Location:** scripts/polymarket.py:179

**Description:** Pattern detected: os.system(

#### [HIGH] Suspicious URL detected: https://gamma-api.polymarket.com

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/clawhub-polymarket-all-in-one/scripts/polymarket.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

### MEDIUM Severity

#### [MEDIUM] HTTP client library imports that enable external communication

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_NETWORK_REQUESTS
**Location:** scripts/polymarket.py:16

**Description:** Pattern detected: import requests

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

**Description:** Skill name 'Better Polymarket' is invalid. Agent skills require lowercase letters, numbers, and hyphens only, with a maximum length of 64 characters.

#### [LOW] Skill does not specify a license

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
