# Agent Skill Security Scan Report

**Skill:** webapp-testing
**Directory:** /workspace/skills/anthropics-skills/skills/webapp-testing
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.42s
**Timestamp:** 2026-02-06T07:49:14.354130

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
**Location:** SKILL.md:8

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
