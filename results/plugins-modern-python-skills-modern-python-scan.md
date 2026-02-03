# Agent Skill Security Scan Report

**Skill:** modern-python
**Directory:** ./skills/trailofbits-skills/plugins/modern-python/skills/modern-python
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.44s
**Timestamp:** 2026-02-03T14:13:54.518040

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:98

**Description:** Detects skills that delegate trust to untrusted external content: Run code

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
