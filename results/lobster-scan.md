# Agent Skill Security Scan Report

**Skill:** lobster
**Directory:** /workspace/skills/clawhub-lobster
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 27.86s
**Timestamp:** 2026-02-06T04:13:39.614119

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Arbitrary Shell Command Execution via exec Command

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The skill provides an 'exec' command that allows execution of arbitrary shell commands through the Lobster CLI. While this is the intended functionality, it creates a command injection risk if user input is not properly sanitized before being passed to shell commands. The examples show direct shell execution patterns like 'exec --json --shell "gh pr list"' which could be exploited if malicious input is incorporated into command strings.

#### [MEDIUM] Unbounded Tool Autonomy Without Explicit Safeguards

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill enables automated workflow execution with approval gates, but the approval mechanism can be bypassed or automated via 'lobster resume --approve yes'. The workflow system allows chaining multiple operations (fetch, filter, process) without clear boundaries on what operations require human oversight. The 'tool mode' is designed for programmatic integration, which could enable autonomous execution of sensitive operations.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
