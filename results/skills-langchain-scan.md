# Agent Skill Security Scan Report

**Skill:** langchain
**Directory:** /home/runner/work/skill-scanner-test/skill-scanner-test/scripts/../skills/hoodini-ai-agents-skills/skills/langchain
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 0.26s
**Timestamp:** 2026-04-18T19:20:54.895456+00:00

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 1
- **Medium:** 0
- **Low:** 0
- **Info:** 1

## Findings

### HIGH Severity

#### [HIGH] Python code block uses eval/exec

**Severity:** HIGH
**Category:** command_injection
**Rule ID:** MDBLOCK_PYTHON_EVAL_EXEC
**Location:** SKILL.md:95

**Description:** Code block in SKILL.md at line 95 contains potentially dangerous Python code.

### INFO Severity

#### [INFO] Skill does not specify a license

**Severity:** INFO
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

## Analyzers

The following analyzers were used:

- static_analyzer
- bytecode
- pipeline
- behavioral_analyzer
- trigger_analyzer
