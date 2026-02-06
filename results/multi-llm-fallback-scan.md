# Agent Skill Security Scan Report

**Skill:** multi-llm
**Directory:** /workspace/skills/clawhub-mlti-llm-fallback
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 29.87s
**Timestamp:** 2026-02-06T04:58:02.982759

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Command Injection Risk via Unvalidated User Input in Model Selection

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** scripts/select-model.sh

**Description:** The scripts use user input directly in shell commands and curl requests without proper validation or sanitization. The user-provided task description is passed to grep patterns and used in API calls, which could allow command injection if malicious input contains shell metacharacters or escape sequences.

#### [MEDIUM] Potential Resource Exhaustion via Unbounded Model Fallback Attempts

**Severity:** MEDIUM
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** scripts/select-model.sh

**Description:** The fallback mechanism attempts multiple models sequentially without timeout limits or maximum retry bounds. If all models in the fallback chain are unavailable or slow to respond, this could cause extended delays or resource exhaustion. The scripts make multiple curl requests without overall timeout constraints.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
