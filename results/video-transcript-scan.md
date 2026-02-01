# Agent Skill Security Scan Report

**Skill:** video-transcript
**Directory:** ./skills/clawhub-video-transcript
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 28.25s
**Timestamp:** 2026-02-01T07:17:05.883626

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

#### [MEDIUM] API Key Exposure Risk via Environment Variable

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires TRANSCRIPT_API_KEY to be stored in ~/.zshenv as an environment variable. While environment variables are a common practice, the instructions guide users to permanently export sensitive credentials in shell configuration files. If the user's system is compromised or if other processes can read environment variables, the API key could be exposed. Additionally, the skill makes external API calls to transcriptapi.com with this credential, creating a data flow path where video URLs and potentially sensitive content are transmitted to a third-party service.

#### [MEDIUM] Missing Critical Metadata Fields

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill manifest is missing several important metadata fields that help users make informed security decisions: 'license' (not specified), 'compatibility' (not specified), and 'allowed-tools' (not specified). The absence of 'allowed-tools' means users cannot verify which agent capabilities this skill will use. Based on the instructions, the skill will use Bash tool to execute curl commands for external API calls, but this is not declared in the manifest.

### LOW Severity

#### [LOW] Skill does not specify a license

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

#### [LOW] Referenced File Not Found in Package

**Severity:** LOW
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION

**Description:** The instructions reference a file 'videos.py' that is not included in the skill package. This creates an incomplete package where documented functionality may not work as expected. While not an active security threat, missing referenced files can indicate incomplete packaging, abandoned development, or potential supply chain issues if users are expected to obtain the file from elsewhere.

#### [LOW] Third-Party API Dependency Without Provenance

**Severity:** LOW
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill relies entirely on an external third-party service (transcriptapi.com) for its core functionality. While the service appears legitimate, there is no information about the service's security practices, data retention policies, or privacy guarantees. Users transmitting video URLs and receiving transcripts have no visibility into how transcriptapi.com handles this data, whether it's logged, stored, or shared.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
