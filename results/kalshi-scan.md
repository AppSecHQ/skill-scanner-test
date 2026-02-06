# Agent Skill Security Scan Report

**Skill:** kalshi
**Directory:** /workspace/skills/clawhub-kalshi
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 23.50s
**Timestamp:** 2026-02-06T03:44:41.214989

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Undeclared network usage

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** TOOL_ABUSE_UNDECLARED_NETWORK

**Description:** Skill code uses network libraries but doesn't declare network requirement

#### [MEDIUM] Credential Storage in User Home Directory

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill stores API credentials (API key ID and private key) in ~/.kalshi/ directory with JSON configuration file. While this is a common pattern, it creates a persistent credential store that could be accessed by other processes or malicious skills. The private key file is set to 600 permissions, which is good, but the credentials.json file permissions are not explicitly restricted.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
