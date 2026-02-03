# Agent Skill Security Scan Report

**Skill:** obsidian-tasks
**Directory:** ./skills/clawhub-openclaw-obsidian-tasks
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.53s
**Timestamp:** 2026-02-03T16:01:40.505592

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
**Location:** scripts/publish_clawhub.sh:12

**Description:** Pattern detected: ${1:?"Usage: $0 <version> [changelog]"}

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
