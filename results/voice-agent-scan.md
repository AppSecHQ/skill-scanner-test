# Agent Skill Security Scan Report

**Skill:** voice-agent
**Directory:** /workspace/skills/clawhub-voice-agent
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 0.22s
**Timestamp:** 2026-02-06T07:53:00.578079

## Summary

- **Total Findings:** 5
- **Critical:** 0
- **High:** 2
- **Medium:** 2
- **Low:** 1
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Accessing sensitive system or credential files

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_SENSITIVE_FILES
**Location:** scripts/client.py:57

**Description:** Pattern detected: open(filename

#### [HIGH] Accessing sensitive system or credential files

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_SENSITIVE_FILES
**Location:** scripts/client.py:70

**Description:** Pattern detected: open(filename

### MEDIUM Severity

#### [MEDIUM] HTTP client library imports that enable external communication

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_NETWORK_REQUESTS
**Location:** scripts/client.py:6

**Description:** Pattern detected: import urllib.request

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
