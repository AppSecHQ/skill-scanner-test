# Agent Skill Security Scan Report

**Skill:** expo-api-routes
**Directory:** ./skills/expo-skills/plugins/expo-app-design/skills/expo-api-routes
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.31s
**Timestamp:** 2026-02-02T02:53:54.826297

## Summary

- **Total Findings:** 2
- **Critical:** 1
- **High:** 0
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:202

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl http://localhost:8081/api/hello

### MEDIUM Severity

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:161

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: GET, POST

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
