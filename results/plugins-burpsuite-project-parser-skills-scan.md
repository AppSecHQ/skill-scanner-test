# Agent Skill Security Scan Report

**Skill:** burpsuite-project-parser
**Directory:** /workspace/skills/trailofbits-skills/plugins/burpsuite-project-parser/skills
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 21.92s
**Timestamp:** 2026-02-06T06:57:05.065782

## Summary

- **Total Findings:** 1
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Undeclared Python Tool Usage Despite allowed-tools Restriction

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill declares 'allowed-tools: [Bash, Read]' in its manifest, restricting usage to Bash scripts and file reading. However, the instructions extensively reference Python files (proxy.py, headers.py, Burp.py) that are missing from the package. While these files are not present (reducing immediate risk), the instructions suggest Python tool usage which violates the declared tool restrictions. This represents a tool restriction violation and potential tool poisoning if the missing Python files were to be added later.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
