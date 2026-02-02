# Agent Skill Security Scan Report

**Skill:** algorithmic-art
**Directory:** ./skills/anthropics-skills/skills/algorithmic-art
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.34s
**Timestamp:** 2026-02-02T02:54:27.349246

## Summary

- **Total Findings:** 1
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] SKILL DISCOVERY ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** skill_discovery_abuse
**Rule ID:** YARA_skill_discovery_abuse
**Location:** SKILL.md:60

**Description:** Detects manipulation of skill discovery to increase unwanted activation: perfect

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
