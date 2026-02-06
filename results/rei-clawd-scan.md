# Agent Skill Security Scan Report

**Skill:** rei
**Directory:** /workspace/skills/clawhub-rei
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.23s
**Timestamp:** 2026-02-06T07:35:47.267217

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Attempting to install system packages with elevated privileges

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** TOOL_ABUSE_SYSTEM_PACKAGE_INSTALL
**Location:** scripts/setup.sh:28

**Description:** Pattern detected: sudo dnf install

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
