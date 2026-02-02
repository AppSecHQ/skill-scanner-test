# Agent Skill Security Scan Report

**Skill:** agent-task-manager
**Directory:** ./skills/clawhub-agent-task-manager
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.54s
**Timestamp:** 2026-02-02T03:07:37.529662

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] User input used in command substitution - potential injection risk

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** COMMAND_INJECTION_USER_INPUT
**Location:** scripts/cooldown.sh:40

**Description:** Pattern detected: eval "$

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
