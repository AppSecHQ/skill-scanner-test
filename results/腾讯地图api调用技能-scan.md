# Agent Skill Security Scan Report

**Skill:** tencent-map
**Directory:** ./skills/clawhub-qqmap
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 37.48s
**Timestamp:** 2026-02-01T17:40:00.116647

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 2
- **Medium:** 0
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Command Injection via Unvalidated User Input in URL Construction

**Severity:** HIGH
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** scripts/tencent_map.sh

**Description:** The script constructs URLs by directly interpolating user-provided parameters (keyword, region, addresses) into curl commands without proper sanitization or URL encoding. An attacker could inject shell metacharacters or malicious payloads through these parameters, potentially leading to command injection. For example, a keyword containing backticks, semicolons, or other shell special characters could execute arbitrary commands.

#### [HIGH] Unrestricted External Network Calls to Third-Party API

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** scripts/tencent_map.sh:38

**Description:** The skill makes unrestricted HTTP requests to apis.map.qq.com (Tencent Maps API) with user-controlled parameters. While this is the intended functionality, there are no safeguards against data exfiltration through these API calls. An attacker could potentially use the search, geocode, or route functions to encode and exfiltrate sensitive data by embedding it in search queries or addresses that get sent to the external API.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
