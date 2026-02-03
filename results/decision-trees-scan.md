# Agent Skill Security Scan Report

**Skill:** decision-trees
**Directory:** ./skills/clawhub-decision-trees
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 0.97s
**Timestamp:** 2026-02-03T15:59:05.324146

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 1
- **Medium:** 1
- **Low:** 1
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Accessing sensitive system or credential files

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_SENSITIVE_FILES
**Location:** scripts/decision_tree.py:119

**Description:** Pattern detected: open(filename

### MEDIUM Severity

#### [MEDIUM] SKILL DISCOVERY ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** skill_discovery_abuse
**Rule ID:** YARA_skill_discovery_abuse
**Location:** SKILL.md:74

**Description:** Detects manipulation of skill discovery to increase unwanted activation: perfect

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
