# Agent Skill Security Scan Report

**Skill:** agent-money-tracker
**Directory:** /workspace/skills/clawhub-intelligent-budget-tracker
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 25.28s
**Timestamp:** 2026-02-06T03:29:39.741667

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Misleading Package Description - TypeScript Library Presented as Agent Skill

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill presents itself as a TypeScript/npm library ('npm install agent-money-tracker') with TypeScript code examples, but is packaged as an Agent Skill. Agent Skills use Python/Bash scripts, not TypeScript. This mismatch between description and actual skill format could mislead users about what they're installing and how it operates. The skill appears to be documentation for a separate npm package rather than a functional agent skill.

#### [MEDIUM] Referenced File Not Found - Missing natural.py

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill instructions reference a file 'natural.py' that is not included in the skill package. This creates a broken dependency where the skill cannot function as described. If this file is meant to be external, it represents a supply chain risk; if it should be bundled, the skill is incomplete.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
