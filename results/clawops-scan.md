# Agent Skill Security Scan Report

**Skill:** clawops
**Directory:** /workspace/skills/clawhub-clawops
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 30.88s
**Timestamp:** 2026-02-05T22:34:14.599234

## Summary

- **Total Findings:** 1
- **Critical:** 0
- **High:** 1
- **Medium:** 0
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Skill Orchestration Without Implementation or Safeguards

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md:1

**Description:** ClawOps claims to be a 'central brain' that manages all installed skills, resolves dependencies, schedules actions, and coordinates workflows across multiple skills. However, there are no script files implementing these capabilities. This creates a dangerous scenario where the skill's description promises powerful orchestration capabilities (discovering skills, executing actions, managing secrets, restarting processes) without any visible implementation or security controls. If implemented later, such broad system-level control without proper authorization checks could enable unauthorized tool use, tool shadowing, or manipulation of other skills' behavior.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
