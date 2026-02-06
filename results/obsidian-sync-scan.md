# Agent Skill Security Scan Report

**Skill:** obsidian-sync
**Directory:** /workspace/skills/clawhub-obsidian-sync
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 37.24s
**Timestamp:** 2026-02-06T05:29:48.755680

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 1
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Hardcoded Authentication Token in Service Configuration

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The systemd service configuration example includes a hardcoded placeholder token 'your-token-here' in the Environment variable. Users may deploy this without changing it, or may store sensitive tokens in plaintext systemd files that could be exposed through misconfiguration or system compromise.

### MEDIUM Severity

#### [MEDIUM] Network Service Exposure Without Explicit Security Warnings

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs users to expose a local sync server via Tailscale without prominent warnings about authentication requirements, token security, or the risks of exposing file system access over the network. While authentication is mentioned, the ease of exposure via 'tailscale serve' may lead users to deploy without fully understanding security implications.

#### [MEDIUM] Missing Script File Creates Tool Execution Risk

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The instructions reference 'Obsidian.py' but this file is not found in the skill package. Additionally, the systemd service and quick start examples reference 'sync-server.mjs' which is also not provided. Users cannot verify the actual behavior of the sync server code, creating a trust gap where malicious code could be substituted or the missing files could contain vulnerabilities.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
