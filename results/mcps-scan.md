# Agent Skill Security Scan Report

**Skill:** mcps
**Directory:** /workspace/skills/clawhub-mcps-skill
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 33.88s
**Timestamp:** 2026-02-06T04:24:25.369253

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Environment Variable Exposure Risk in Configuration Examples

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill's configuration examples demonstrate storing sensitive credentials in environment variables (POSTGRES_CONNECTION_STRING, GITLAB_PERSONAL_ACCESS_TOKEN) that are passed to external MCP servers. While using environment variables is better than hardcoding, the skill provides no guidance on secure credential management, validation of server trustworthiness, or warnings about credential exposure risks when adding untrusted MCP servers.

#### [MEDIUM] Unrestricted External Command Execution via MCP Servers

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill allows users to add arbitrary MCP servers that execute external commands (uvx, npx, custom binaries) without any validation, sandboxing, or security warnings. Users can configure servers that run untrusted code with full system access. The examples show adding servers via package managers (npx, uvx) that could download and execute malicious code. No guidance is provided on vetting servers or understanding security implications.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
