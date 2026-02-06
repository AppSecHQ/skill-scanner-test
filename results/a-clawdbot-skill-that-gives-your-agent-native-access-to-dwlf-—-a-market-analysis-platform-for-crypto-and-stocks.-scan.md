# Agent Skill Security Scan Report

**Skill:** dwlf
**Directory:** /workspace/skills/clawhub-dwlf
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 33.77s
**Timestamp:** 2026-02-05T17:39:55.560704

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 1
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] API Key Extraction from TOOLS.md File

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** scripts/dwlf-api.sh

**Description:** The bash script attempts to extract an API key from a file named TOOLS.md by searching for 'Jenna's own key' and parsing the API Key value. This creates a security risk as it accesses credentials from an external file that may contain sensitive information. The script specifically looks for a pattern 'Jenna's own key' followed by 'API Key:', which suggests it's designed to extract a specific user's credentials.

### MEDIUM Severity

#### [MEDIUM] Command Injection Risk via Unsanitized PATH_AND_QUERY Parameter

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** scripts/dwlf-api.sh

**Description:** The script accepts a PATH_AND_QUERY parameter that is directly interpolated into a curl URL without sanitization. While the script uses proper quoting in most places, the parameter could contain shell metacharacters or malicious payloads that might be interpreted by the shell or curl. An attacker could potentially inject additional curl arguments or manipulate the request.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
