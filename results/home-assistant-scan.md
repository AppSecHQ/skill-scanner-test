# Agent Skill Security Scan Report

**Skill:** home-assistant
**Directory:** /workspace/skills/clawhub-home-assistant
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 35.49s
**Timestamp:** 2026-02-06T03:02:36.174070

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 1
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Hardcoded Credential Storage in User Home Directory

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs users to store Home Assistant credentials (long-lived access tokens) in plaintext configuration files at ~/.config/home-assistant/config.json or as environment variables. Long-lived access tokens provide full API access to Home Assistant, which controls physical smart home devices. Storing these in plaintext creates a significant credential exposure risk if the user's system is compromised.

### MEDIUM Severity

#### [MEDIUM] Command Injection Risk in Shell Script

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** scripts/ha.sh

**Description:** The bash script ha.sh uses user-provided entity_id values directly in curl commands and string interpolation without proper validation or sanitization. While the script uses proper quoting in most places, the entity_id is used in URL construction and JSON payloads where special characters could potentially cause issues. An attacker who can control entity_id input could potentially inject malicious commands or manipulate API calls.

#### [MEDIUM] Unrestricted Network Access Without Tool Declaration

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill makes extensive network calls to external Home Assistant instances via curl but does not declare any allowed-tools restrictions in the manifest. While the skill's purpose legitimately requires network access, the absence of tool declarations means there are no documented restrictions on what the skill can do. The skill could potentially be modified to make unauthorized network calls without detection.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
