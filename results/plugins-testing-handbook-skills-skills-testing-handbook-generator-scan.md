# Agent Skill Security Scan Report

**Skill:** testing-handbook-generator
**Directory:** /workspace/skills/trailofbits-skills/plugins/testing-handbook-skills/skills/testing-handbook-generator
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.25s
**Timestamp:** 2026-02-06T07:34:15.249846

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:238

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:256

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

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
