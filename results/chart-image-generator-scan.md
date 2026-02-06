# Agent Skill Security Scan Report

**Skill:** chart-image
**Directory:** /workspace/skills/clawhub-chart-image
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 25.46s
**Timestamp:** 2026-02-05T21:38:12.732295

## Summary

- **Total Findings:** 1
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Hardcoded Absolute Path Exposes System Structure

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill uses hardcoded absolute paths (/data/clawd/skills/chart-image/scripts) throughout the instructions. This reveals the internal directory structure of the deployment environment and could aid attackers in understanding the system layout. Additionally, this makes the skill non-portable and assumes a specific installation location that may not exist on all systems.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
