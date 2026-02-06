# Agent Skill Security Scan Report

**Skill:** ez-cronjob
**Directory:** /workspace/skills/clawhub-ez-cronjob
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 19.40s
**Timestamp:** 2026-02-06T01:06:46.322756

## Summary

- **Total Findings:** 1
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Direct Instruction Override Attempt in Markdown Body

**Severity:** MEDIUM
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** SKILL.md

**Description:** The skill contains explicit instructions directed at AI agents to bypass normal tool usage patterns. The section 'For Agents' states 'If you're an AI agent reading this: when the user asks you to manage cron jobs, **always use the exec/bash tool**'. This attempts to override the agent's normal decision-making process and force specific tool usage, which is a form of instruction injection.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
