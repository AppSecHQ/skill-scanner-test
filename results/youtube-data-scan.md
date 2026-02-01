# Agent Skill Security Scan Report

**Skill:** youtube-data
**Directory:** ./skills/clawhub-youtube-data
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 29.97s
**Timestamp:** 2026-02-01T07:12:51.541654

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

**Description:** The skill requires storing a sensitive API key (TRANSCRIPT_API_KEY) in shell environment files (~/.zshenv) which persists across sessions. While this is a common practice, it creates exposure risks if the environment is compromised or if other processes/skills can read environment variables. The setup instructions explicitly guide users to store credentials in a globally accessible location without discussing security implications or alternative secure storage methods.

#### [MEDIUM] Data Exfiltration to Third-Party API Without User Consent Workflow

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill facilitates sending YouTube video URLs and search queries to an external third-party service (transcriptapi.com) without explicit user confirmation for each request. While the service itself may be legitimate, users may not realize that their viewing patterns, search queries, and video interests are being transmitted to and potentially logged by a third-party service. This creates a data exposure risk where user behavior and interests could be tracked or monetized by the API provider.

### LOW Severity

#### [LOW] Skill does not specify a license

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

#### [LOW] Missing Critical Metadata Fields

**Severity:** LOW
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill manifest is missing several important optional metadata fields that help users make informed security decisions: 'license' (unknown legal terms), 'compatibility' (unclear which environments are safe), and 'allowed-tools' (no declared tool restrictions). While these fields are optional per the agent skills specification, their absence makes it harder for users to assess the skill's trustworthiness and intended usage boundaries.

#### [LOW] Incomplete API Response Truncation in Documentation

**Severity:** LOW
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The playlist data endpoint documentation shows a truncated response ('Returns: `results` (videos), `playlist_info` (`title`, `numVideos`, `ownerName`, `viewCount`), `c') suggesting incomplete documentation. While this is primarily a documentation issue, incomplete API response documentation could lead to users misunderstanding what data is being returned, potentially missing sensitive fields that are included in responses.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
