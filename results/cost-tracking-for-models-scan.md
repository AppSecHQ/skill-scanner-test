# Agent Skill Security Scan Report

**Skill:** clawdbot-cost-tracker
**Directory:** ./skills/clawhub-cost-report
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.46s
**Timestamp:** 2026-02-03T16:16:17.346089

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] User input used in command substitution - potential injection risk

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** COMMAND_INJECTION_USER_INPUT
**Location:** scripts/extract-cost.sh:113

**Description:** Pattern detected: $(grep -o '"total":[0-9.]*' "$f" 2>/dev/null | cut -d: -f2 | awk '{sum+=$1} END {print sum}')

#### [MEDIUM] User input used in command substitution - potential injection risk

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** COMMAND_INJECTION_USER_INPUT
**Location:** scripts/extract-cost.sh:142

**Description:** Pattern detected: $(echo "$results" | awk '{sum+=$2} END {printf "%.2f", sum}')

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
