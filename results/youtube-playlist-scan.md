# Agent Skill Security Scan Report

**Skill:** youtube-playlist
**Directory:** ./skills/clawhub-youtube-playlist
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 26.67s
**Timestamp:** 2026-02-01T07:14:34.425574

## Summary

- **Total Findings:** 6
- **Critical:** 1
- **High:** 0
- **Medium:** 2
- **Low:** 3
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:9

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export TRANSCRIPT_API_KEY

### MEDIUM Severity

#### [MEDIUM] Hardcoded API Key Required in Environment Variable

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires users to store a third-party API key (TRANSCRIPT_API_KEY) in their shell environment. While the instructions show proper storage in ~/.zshenv, this creates a persistent credential that could be exposed if the environment is compromised. The API key is transmitted in Authorization headers to transcriptapi.com for all requests.

#### [MEDIUM] Data Transmission to Third-Party Service

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill sends YouTube playlist and video data to an external third-party API (transcriptapi.com) that is not operated by YouTube/Google. Users may not be aware that their playlist browsing activity and video transcript requests are being routed through this intermediary service, which could log or retain this data.

### LOW Severity

#### [LOW] Skill does not specify a license

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

#### [LOW] Missing Referenced Files Without Explanation

**Severity:** LOW
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING

**Description:** The skill references two files (URL.py and a.py) in its instructions that are not included in the package and are marked as 'not found'. These appear to be documentation artifacts or incomplete references that could confuse users or indicate incomplete skill packaging.

#### [LOW] Missing Optional Metadata Fields

**Severity:** LOW
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill manifest is missing optional but recommended metadata fields: license, compatibility, and allowed-tools. While not required, these fields help users understand the skill's constraints and usage context. The absence of allowed-tools means there are no declared restrictions on which agent tools can be used.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
