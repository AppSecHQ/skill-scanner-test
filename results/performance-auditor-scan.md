# Agent Skill Security Scan Report

**Skill:** perf-auditor
**Directory:** /workspace/skills/clawhub-perf-auditor
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 33.74s
**Timestamp:** 2026-02-06T06:18:41.370041

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 1
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Unverified External Tool Execution with Network Access

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs the agent to execute 'npx ai-lighthouse' which downloads and runs arbitrary code from npm registry without verification. The tool makes network requests to audit URLs and sends performance data to an unspecified AI model endpoint. There is no transparency about what data is transmitted, where it goes, or how it's processed. The skill provides no source code for inspection, only instructions to run an external binary.

### MEDIUM Severity

#### [MEDIUM] Tool Shadowing Risk via npx Execution

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill relies entirely on an external npm package 'ai-lighthouse' that is not included in the skill package. This creates a tool shadowing risk where the external package could be compromised, typosquatted, or replaced with malicious code. The agent has no way to verify the tool's behavior matches the skill's description. The package could perform actions beyond performance auditing without detection.

#### [MEDIUM] Misleading Skill Packaging and Capability Claims

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill presents itself as a self-contained agent skill but actually functions as a wrapper for an external npm tool. The description 'One command. Zero config. Just works.' is misleading because it requires Node.js 18+, npm/npx availability, and network access - none of which are declared in the manifest. The skill claims to be 'part of 110+ free developer tools' but provides no verification of this claim or the legitimacy of the LXGIC Studios organization.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
