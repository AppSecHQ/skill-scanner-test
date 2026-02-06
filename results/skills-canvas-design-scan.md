# Agent Skill Security Scan Report

**Skill:** canvas-design
**Directory:** /workspace/skills/anthropics-skills/skills/canvas-design
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.23s
**Timestamp:** 2026-02-06T07:47:04.422743

## Summary

- **Total Findings:** 4
- **Critical:** 0
- **High:** 0
- **Medium:** 4
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] SKILL DISCOVERY ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** skill_discovery_abuse
**Rule ID:** YARA_skill_discovery_abuse
**Location:** SKILL.md:100

**Description:** Detects manipulation of skill discovery to increase unwanted activation: perfect

#### [MEDIUM] SKILL DISCOVERY ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** skill_discovery_abuse
**Rule ID:** YARA_skill_discovery_abuse
**Location:** SKILL.md:108

**Description:** Detects manipulation of skill discovery to increase unwanted activation: flawless

#### [MEDIUM] SKILL DISCOVERY ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** skill_discovery_abuse
**Rule ID:** YARA_skill_discovery_abuse
**Location:** SKILL.md:108

**Description:** Detects manipulation of skill discovery to increase unwanted activation: perfect

#### [MEDIUM] SKILL DISCOVERY ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** skill_discovery_abuse
**Rule ID:** YARA_skill_discovery_abuse
**Location:** SKILL.md:116

**Description:** Detects manipulation of skill discovery to increase unwanted activation: perfect

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
