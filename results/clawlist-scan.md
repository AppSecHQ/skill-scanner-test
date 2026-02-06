# Agent Skill Security Scan Report

**Skill:** clawlist
**Directory:** /workspace/skills/clawhub-clawlist
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 32.97s
**Timestamp:** 2026-02-05T22:25:12.696555

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 1
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Aggressive Activation Directive - Forced Skill Usage

**Severity:** HIGH
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** SKILL.md

**Description:** The skill description and instructions contain multiple aggressive directives forcing the agent to use this skill ('MUST use', 'ALWAYS use clawlist when'). This is a direct prompt injection attempt to override the agent's decision-making autonomy and force activation regardless of actual need. The skill attempts to claim priority over the agent's normal task assessment process.

### MEDIUM Severity

#### [MEDIUM] Unbounded Autonomy - Infinite Task Execution

**Severity:** MEDIUM
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** SKILL.md

**Description:** The skill explicitly promotes 'infinite monitoring loops' and 'infinite tasks' that run 'Forever' without clear termination conditions or user confirmation requirements. This creates availability risks through unbounded resource consumption and autonomous execution patterns that may run indefinitely without oversight.

#### [MEDIUM] Tool Chaining Without Safeguards

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill orchestrates a complex chain of sub-skills (brainstorming → write-plan → doing-tasks → verify-task → dispatch-multiple-agents) with automated execution flow. This tool chaining pattern lacks explicit user confirmation points between phases and could enable automated multi-step operations without oversight, especially when combined with the 'infinite task' execution model.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
