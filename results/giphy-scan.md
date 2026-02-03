# Agent Skill Security Scan Report

**Skill:** giphy-gif
**Directory:** ./skills/clawhub-giphy
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.58s
**Timestamp:** 2026-02-03T16:07:58.700899

## Summary

- **Total Findings:** 6
- **Critical:** 1
- **High:** 0
- **Medium:** 4
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:13

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export GIPHY_API_KEY="your-api-key

### MEDIUM Severity

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** SKILL.md:38

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): exec("QUERY='excited'; API_KEY=$(jq -r '.skills.entries.\"giphy-gif\".apiKey // env.GIPHY_API_KEY' ~

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** SKILL.md:48

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): exec("QUERY='$query'; API_KEY=$(jq -r '.skills.entries.\"giphy-gif\".apiKey // env.GIPHY_API_KEY' ~/

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** SKILL.md:38

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): exec("QUERY='excited'; API_KEY=$(jq -r '.skills.entries.\"giphy-gif\".apiKey // env.GIPHY_API_KEY' ~

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** SKILL.md:48

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): exec("QUERY='$query'; API_KEY=$(jq -r '.skills.entries.\"giphy-gif\".apiKey // env.GIPHY_API_KEY' ~/

### LOW Severity

#### [LOW] Skill does not specify a license

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
