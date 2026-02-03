# Agent Skill Security Scan Report

**Skill:** browse
**Directory:** ./skills/clawhub-browse
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.68s
**Timestamp:** 2026-02-03T16:17:05.595571

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** SKILL.md:246

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): eval(selector, els =>
    els.map(el => el.textContent)

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
