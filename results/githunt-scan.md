# Agent Skill Security Scan Report

**Skill:** githunt
**Directory:** /workspace/skills/clawhub-githunt
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 29.73s
**Timestamp:** 2026-02-06T02:21:19.906211

## Summary

- **Total Findings:** 5
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 4
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] External API Communication Without User Awareness

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** scripts/githunt-search.sh

**Description:** The skill makes network requests to an external API (api.githunt.ai) to retrieve GitHub developer data. While the API endpoint is clearly documented and the service appears legitimate, users may not be fully aware that their search queries (location, skills, role) are being transmitted to a third-party service. This creates a potential privacy concern as search parameters could reveal hiring intentions or organizational interests.

### LOW Severity

#### [LOW] Skill does not specify a license

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

#### [LOW] Missing Optional Metadata Fields

**Severity:** LOW
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill manifest is missing optional metadata fields including 'license', 'compatibility', and 'allowed-tools'. While these fields are optional per the agent skills specification, their absence reduces transparency about the skill's behavior and tool usage. The skill does specify 'version' and 'author' which is good practice.

#### [LOW] Command Injection Risk in Bash Script Variable Handling

**Severity:** LOW
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** scripts/githunt-search.sh

**Description:** The bash scripts use user-provided input (location, role, skills) directly in JSON payload construction without proper escaping or validation. While the current implementation uses double quotes and basic string manipulation, special characters in user input could potentially break JSON structure or cause unexpected behavior. The risk is mitigated by the fact that the payload is sent via curl to an external API rather than executed locally, but improper JSON construction could still cause issues.

#### [LOW] No Timeout or Rate Limiting on API Calls

**Severity:** LOW
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** scripts/githunt-search.sh

**Description:** The bash scripts make curl requests to the external GitHunt API without specifying timeouts or implementing rate limiting. The streaming endpoint could potentially hang indefinitely if the API becomes unresponsive. Additionally, there's no protection against rapid repeated calls that could exhaust API quotas or cause resource issues.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
