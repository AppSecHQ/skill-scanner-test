# Agent Skill Security Scan Report

**Skill:** local-llm-router
**Directory:** /home/runner/work/skill-scanner-test/skill-scanner-test/scripts/../skills/hoodini-ai-agents-skills/skills/local-llm-router
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.31s
**Timestamp:** 2026-04-18T19:19:45.235289+00:00

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 1
- **Info:** 1

## Findings

### MEDIUM Severity

#### [MEDIUM] Python code block executes shell commands

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** MDBLOCK_PYTHON_SUBPROCESS
**Location:** SKILL.md:99

**Description:** Code block in SKILL.md at line 99 contains potentially dangerous Python code.

### LOW Severity

#### [LOW] Dangerous data flow in command pipeline

**Severity:** LOW
**Category:** command_injection
**Rule ID:** PIPELINE_TAINT_FLOW
**Location:** references/model-matrix.md:2

**Description:** Pipeline downloads data from the network and executes it: `curl -fsSL https://ollama.ai/install.sh | sh`. This is a remote code execution pattern. (Note: found in documentation file - may be instructional rather than executable.)

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
