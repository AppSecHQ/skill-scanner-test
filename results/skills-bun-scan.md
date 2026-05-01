# Agent Skill Security Scan Report

**Skill:** bun
**Directory:** /home/runner/work/skill-scanner-test/skill-scanner-test/scripts/../skills/hoodini-ai-agents-skills/skills/bun
**Status:** [OK] SAFE
**Max Severity:** LOW
**Scan Duration:** 0.26s
**Timestamp:** 2026-04-18T19:19:21.570884+00:00

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 0
- **Low:** 1
- **Info:** 1

## Findings

### LOW Severity

#### [LOW] Dangerous data flow in command pipeline

**Severity:** LOW
**Category:** command_injection
**Rule ID:** PIPELINE_TAINT_FLOW
**Location:** SKILL.md:2

**Description:** Pipeline downloads data from the network and executes it: `curl -fsSL https://bun.sh/install | bash`. This is a remote code execution pattern. (Note: uses a well-known installer URL - likely a standard installation command.)

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
