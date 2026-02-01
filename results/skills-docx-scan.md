# Agent Skill Security Scan Report

**Skill:** docx
**Directory:** ./skills/anthropics-skills/skills/docx
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.85s
**Timestamp:** 2026-02-01T23:22:45.639824

## Summary

- **Total Findings:** 1
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:128

**Description:** Detects skills that delegate trust to untrusted external content: run script

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
