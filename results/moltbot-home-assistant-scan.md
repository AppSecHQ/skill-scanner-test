# Agent Skill Security Scan Report

**Skill:** moltbot-ha
**Directory:** /workspace/skills/clawhub-moltbot-ha
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 27.54s
**Timestamp:** 2026-02-06T04:49:30.130708

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Hardcoded Credential Exposure Risk in Documentation

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructions demonstrate setting the HA_TOKEN environment variable with a placeholder 'your_token_here' and provide detailed steps for creating long-lived access tokens. While educational, this pattern could lead users to hardcode sensitive tokens in shell history or configuration files. The skill requires HA_TOKEN as a primary environment variable for authentication to Home Assistant, creating a credential exposure risk if not handled properly.

#### [MEDIUM] Unverified External Binary Dependency

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill requires installation of 'moltbot-ha' binary via 'uv tool install' without version pinning or integrity verification. The binary is installed from an external package repository with no specified version constraints, provenance verification, or checksum validation. This creates a supply chain risk where a compromised or malicious version of moltbot-ha could be installed.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
