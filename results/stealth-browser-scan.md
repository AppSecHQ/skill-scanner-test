# Agent Skill Security Scan Report

**Skill:** stealth-browser
**Directory:** /workspace/skills/clawhub-kesslerio-stealth-browser
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 1.51s
**Timestamp:** 2026-02-06T07:50:08.016055

## Summary

- **Total Findings:** 6
- **Critical:** 1
- **High:** 0
- **Medium:** 4
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] HTTP POST request that may send data externally

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_HTTP_POST
**Location:** scripts/curl-api.py:73

**Description:** Pattern detected: requests.post(

### MEDIUM Severity

#### [MEDIUM] Attempting to install system packages with elevated privileges

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** TOOL_ABUSE_SYSTEM_PACKAGE_INSTALL
**Location:** scripts/setup.sh:30

**Description:** Pattern detected: sudo dnf install

#### [MEDIUM] HTTP client library imports that enable external communication

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_NETWORK_REQUESTS
**Location:** scripts/curl-api.py:23

**Description:** Pattern detected: import requests

#### [MEDIUM] Undeclared network usage

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** TOOL_ABUSE_UNDECLARED_NETWORK

**Description:** Skill code uses network libraries but doesn't declare network requirement

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** scripts/curl-api.py:11

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: GET, POST

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
