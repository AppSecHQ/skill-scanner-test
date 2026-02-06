# Agent Skill Security Scan Report

**Skill:** instagram
**Directory:** /workspace/skills/clawhub-instagram
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 27.80s
**Timestamp:** 2026-02-06T03:26:00.937919

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Hardcoded Access Token in Environment Variable Without Validation

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires INSTAGRAM_ACCESS_TOKEN to be set as an environment variable but provides no validation, rotation guidance, or security warnings. The setup instructions encourage users to export a long-lived access token directly into their shell environment, which could be exposed through shell history, process listings, or accidental commits to version control. Instagram access tokens grant significant permissions including posting content, accessing analytics, and managing follower interactions.

### LOW Severity

#### [LOW] Missing Tool Declarations and Implementation Details

**Severity:** LOW
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill declares 'always: True' in metadata (suggesting automatic activation) and requires external binaries (curl, jq) but does not specify allowed-tools in the manifest. There are no script files provided to examine actual implementation, making it impossible to verify what operations are performed with the Instagram API. The combination of automatic activation, required external tools, and missing implementation creates opacity around actual behavior and potential tool exploitation risks.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
