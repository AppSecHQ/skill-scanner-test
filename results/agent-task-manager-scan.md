# Agent Skill Security Scan Report

**Skill:** agent-task-manager
**Directory:** /workspace/skills/clawhub-agent-task-manager
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 35.19s
**Timestamp:** 2026-02-05T18:43:21.917968

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 0
- **Medium:** 3
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] User input used in command substitution - potential injection risk

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** COMMAND_INJECTION_USER_INPUT
**Location:** scripts/cooldown.sh:40

**Description:** Pattern detected: eval "$

#### [MEDIUM] Command Injection via eval() in cooldown.sh

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** scripts/cooldown.sh:40

**Description:** The cooldown.sh script uses 'eval "$COMMAND"' to execute arbitrary commands passed as arguments. This creates a command injection vulnerability where malicious input in the COMMAND parameter could execute unintended shell commands. While this is within a local skill package, it allows arbitrary code execution if the orchestrator or task parser constructs malicious commands.

#### [MEDIUM] Unbounded Workflow Execution Without User Confirmation

**Severity:** MEDIUM
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** scripts/orchestrator.py

**Description:** The orchestrator.py implements automated multi-step workflows that execute sequentially without requiring user confirmation between steps. The run_task_from_human.py interface accepts natural language requests and automatically executes complex workflows including financial analysis and external notifications. This creates risk of unintended automated actions, especially when combined with rate-limiting that enables continuous background execution.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
