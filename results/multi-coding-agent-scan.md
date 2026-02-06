# Agent Skill Security Scan Report

**Skill:** coding-agent
**Directory:** /workspace/skills/clawhub-multi-coding-agent
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 23.33s
**Timestamp:** 2026-02-06T04:55:41.656528

## Summary

- **Total Findings:** 1
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Missing allowed-tools Declaration

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill does not declare 'allowed-tools' in its YAML manifest. While this field is optional per the agent skills spec, it is recommended for skills that execute bash commands and manage background processes. This skill uses bash extensively with PTY mode, background processes, and process management tools, which should be explicitly declared for transparency.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
