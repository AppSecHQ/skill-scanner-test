# Agent Skill Security Scan Report

**Skill:** windows-control
**Directory:** /workspace/skills/clawhub-windows-control
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 4.71s
**Timestamp:** 2026-02-06T07:53:38.929449

## Summary

- **Total Findings:** 3
- **Critical:** 2
- **High:** 0
- **Medium:** 0
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Base64 encoding (often used before data exfiltration)

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_BASE64_AND_NETWORK
**Location:** scripts/screenshot.py:17

**Description:** Pattern detected: base64.b64encode

#### [CRITICAL] Base64 encoding (often used before data exfiltration)

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_BASE64_AND_NETWORK
**Location:** screenshot.py:17

**Description:** Pattern detected: base64.b64encode

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
