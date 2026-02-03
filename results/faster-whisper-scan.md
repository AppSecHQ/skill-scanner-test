# Agent Skill Security Scan Report

**Skill:** faster-whisper
**Directory:** ./skills/clawhub-faster-whisper
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.69s
**Timestamp:** 2026-02-03T15:59:39.166198

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Attempting to install system packages with elevated privileges

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** TOOL_ABUSE_SYSTEM_PACKAGE_INSTALL
**Location:** setup.sh:50

**Description:** Pattern detected: sudo dnf install

#### [MEDIUM] Attempting to install system packages with elevated privileges

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** TOOL_ABUSE_SYSTEM_PACKAGE_INSTALL
**Location:** setup.sh:51

**Description:** Pattern detected: sudo pacman -S

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
