# Agent Skill Security Scan Report

**Skill:** apewisdom
**Directory:** ./skills/clawhub-apewisdom
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 0.59s
**Timestamp:** 2026-02-03T16:15:01.463352

## Summary

- **Total Findings:** 4
- **Critical:** 0
- **High:** 1
- **Medium:** 2
- **Low:** 1
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Suspicious URL detected: https://apewisdom.io/api/v1.0/filter

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/clawhub-apewisdom/scripts/scan_reddit.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

### MEDIUM Severity

#### [MEDIUM] HTTP client library imports that enable external communication

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_NETWORK_REQUESTS
**Location:** scripts/scan_reddit.py:2

**Description:** Pattern detected: import requests

#### [MEDIUM] Undeclared network usage

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** TOOL_ABUSE_UNDECLARED_NETWORK

**Description:** Skill code uses network libraries but doesn't declare network requirement

### LOW Severity

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
