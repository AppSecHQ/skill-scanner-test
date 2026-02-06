# Agent Skill Security Scan Report

**Skill:** trmnl
**Directory:** /workspace/skills/clawhub-trmnl
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.28s
**Timestamp:** 2026-02-06T07:51:48.765051

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] SKILL DISCOVERY ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** skill_discovery_abuse
**Rule ID:** YARA_skill_discovery_abuse
**Location:** SKILL.md:167

**Description:** Detects manipulation of skill discovery to increase unwanted activation: perfect

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** scripts/check_payload.py:10

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): ' | python 

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
