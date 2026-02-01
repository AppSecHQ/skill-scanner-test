# Agent Skill Security Scan Report

**Skill:** youtube-api
**Directory:** ./skills/clawhub-youtube-api
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 25.24s
**Timestamp:** 2026-02-01T07:13:43.148391

## Summary

- **Total Findings:** 4
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 3
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Third-Party API Dependency with Credential Requirement

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION

**Description:** The skill requires users to register with a third-party service (TranscriptAPI.com) and store API credentials in their environment. While the service appears legitimate, this creates a dependency on an external commercial service that could potentially log or access all YouTube data requests made by users. The skill does not disclose data handling practices of the third-party service or provide alternatives.

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

**Description:** The skill manifest is missing several important optional fields that help users make informed security decisions: 'license' (unknown legal terms), 'compatibility' (unclear where it works), and 'allowed-tools' (no declared tool restrictions). While these fields are optional per the spec, their absence reduces transparency about the skill's behavior and constraints.

#### [LOW] Environment Variable Persistence Instruction

**Severity:** LOW
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION

**Description:** The setup instructions recommend persisting the API key in ~/.zshenv, which makes the credential available to all shell sessions and processes. While this is a common practice, it increases the exposure window if the system is compromised. The instruction also assumes zsh shell, which may not apply to all users.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
