# Agent Skill Security Scan Report

**Skill:** domain-name-brainstormer
**Directory:** /workspace/skills/softaworks-agent-toolkit/skills/domain-name-brainstormer
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 22.78s
**Timestamp:** 2026-02-06T00:29:45.348662

## Summary

- **Total Findings:** 1
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Misleading Capability Claims Without Implementation

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill description and instructions claim to 'check availability across multiple TLDs' and 'verify which domains are actually available', but there are no script files or implementation code provided. The example output shows detailed availability checking (✓ Available, Taken, Premium domains with pricing), but this functionality cannot be performed without actual domain lookup code. This creates false expectations and could mislead users into thinking the skill has capabilities it doesn't possess.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
