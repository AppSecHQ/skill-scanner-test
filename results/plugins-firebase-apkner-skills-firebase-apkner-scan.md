# Agent Skill Security Scan Report

**Skill:** firebase-apk-scanner
**Directory:** /workspace/skills/trailofbits-skills/plugins/firebase-apk-scanner/skills/firebase-apk-scanner
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 56.04s
**Timestamp:** 2026-02-06T07:07:54.445437

## Summary

- **Total Findings:** 4
- **Critical:** 1
- **High:** 2
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Missing Scanner Script - Core Functionality Unavailable

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md:37

**Description:** The skill's primary executable 'scanner.sh' is referenced in allowed-tools and instructions but was not provided for analysis. This script is supposed to perform security testing including network requests to Firebase endpoints, authentication testing, and data access attempts. Without reviewing this script, we cannot verify: (1) where extracted data is sent, (2) if credentials are exfiltrated, (3) if the script contains hardcoded secrets, or (4) if it performs unauthorized actions beyond stated scope.

### HIGH Severity

#### [HIGH] Unrestricted External Command Execution

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE

**Description:** The skill declares 'Bash(apktool:*)' and 'Bash(curl:*)' in allowed-tools, permitting execution of arbitrary apktool and curl commands. The curl permission is particularly dangerous as it allows the skill to make arbitrary HTTP requests to any endpoint, potentially exfiltrating extracted Firebase configurations, API keys, or test results to attacker-controlled servers. The wildcard (*) provides no restrictions on arguments, URLs, or data payloads.

#### [HIGH] Deceptive Scope - Offensive Security Tool Disguised as Audit Tool

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill description claims 'For authorized security research only' but provides no technical controls to enforce authorization boundaries. The skill actively performs exploitation attempts (creating accounts, testing write access, enumerating endpoints) rather than passive configuration analysis. The instructions include a 'Rationalizations to Reject' section that trains the agent to be aggressive in reporting findings and dismiss security justifications, suggesting the tool is designed for offensive use rather than defensive auditing.

### MEDIUM Severity

#### [MEDIUM] Unbounded Resource Consumption Risk

**Severity:** MEDIUM
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** SKILL.md

**Description:** The skill accepts directory paths as input and will recursively process all APKs found. The instructions show 'ls -la $ARGUMENTS' and '{baseDir}/scanner.sh $ARGUMENTS' with no limits on: (1) number of APKs processed, (2) size of APKs, (3) depth of directory traversal, or (4) timeout for decompilation/testing operations. Processing large directories or maliciously crafted APKs could cause resource exhaustion.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
