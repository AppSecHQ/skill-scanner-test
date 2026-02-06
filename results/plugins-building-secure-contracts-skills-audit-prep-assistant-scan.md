# Agent Skill Security Scan Report

**Skill:** audit-prep-assistant
**Directory:** /workspace/skills/trailofbits-skills/plugins/building-secure-contracts/skills/audit-prep-assistant
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 36.14s
**Timestamp:** 2026-02-06T06:42:51.135654

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 0
- **Medium:** 3
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Unrestricted Command Execution Without Safety Validation

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The skill instructs the agent to execute multiple static analysis tools (slither, dylint, golangci-lint, CodeQL, Semgrep) directly via bash commands without any validation, sandboxing, or output sanitization. These commands are executed with whatever permissions the agent has, potentially allowing command injection if tool outputs or file paths contain malicious content. The skill provides no guidance on validating tool installation, checking tool integrity, or handling potentially malicious output from these security tools.

#### [MEDIUM] Unbounded Autonomous Operations Without User Confirmation

**Severity:** MEDIUM
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** SKILL.md

**Description:** The skill describes autonomous multi-step workflows that could consume significant resources without user oversight: 'Run full test suite', 'Analyze current coverage', 'Find unused functions/variables', 'List all files in scope', 'Test on fresh environment'. These operations could traverse entire codebases, run extensive test suites, or perform resource-intensive analysis without checkpoints or user confirmation. No guidance is provided on limiting scope, setting timeouts, or requesting confirmation before expensive operations.

#### [MEDIUM] Excessive Data Collection Without Scope Boundaries

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs collection of comprehensive codebase information without defined boundaries: 'List all files in scope', 'Identify all actors', 'Map primary workflows', 'Document all dependencies', 'Find unused functions/variables'. This over-collection pattern could lead to processing sensitive files (credentials, private keys, environment files) that should be excluded from security review preparation. No guidance is provided on excluding sensitive files or limiting data collection scope.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
