# Agent Skill Security Scan Report

**Skill:** glm-coding-agent
**Directory:** /workspace/skills/clawhub-glm-coding-agent
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 31.72s
**Timestamp:** 2026-02-06T02:28:04.574565

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Credential Exposure via OpenClaw Config File Access

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill reads API keys from the OpenClaw configuration file (~/.openclaw/openclaw.json on Unix, %USERPROFILE%\.openclaw\openclaw.json on Windows) and exports them as environment variables (ANTHROPIC_AUTH_TOKEN). While this is the intended design for accessing Z.AI API credentials, it creates a potential attack surface if the skill is modified or if the config file contains sensitive credentials that could be exposed through command execution or logging.

#### [MEDIUM] Command Injection Risk via Unvalidated User Input

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The skill accepts user-provided task descriptions as command-line arguments that are passed directly to the claude CLI tool without validation or sanitization. While the scripts use proper quoting in examples, malicious input could potentially be crafted to inject commands if the wrapper scripts don't properly handle special characters or if the claude CLI has vulnerabilities in argument parsing.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
