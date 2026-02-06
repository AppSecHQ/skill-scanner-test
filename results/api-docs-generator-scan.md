# Agent Skill Security Scan Report

**Skill:** api-docs-gen
**Directory:** /workspace/skills/clawhub-api-docs-gen
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 254.35s
**Timestamp:** 2026-02-05T19:39:00.460530

## Summary

- **Total Findings:** 7
- **Critical:** 1
- **High:** 2
- **Medium:** 2
- **Low:** 2
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Hardcoded External API Dependency with Required Credentials

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires an OPENAI_API_KEY environment variable to function, which means it will access and potentially transmit user code to OpenAI's external servers. The skill reads user route files (which may contain sensitive business logic, authentication code, or proprietary algorithms) and sends this data to a third-party API without explicit user consent or warning about data transmission.

### HIGH Severity

#### [HIGH] Deceptive Description Omits Critical External Dependency

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill description claims 'One command. Zero config. Just works.' and 'No install needed. Just run with npx.' However, it requires OPENAI_API_KEY environment variable and sends user code to external servers. This critical dependency and data transmission is buried in the requirements section rather than prominently disclosed in the description. Users may unknowingly expose proprietary code to third-party services.

#### [HIGH] Unauthorized Tool Use - External Command Execution

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill instructs the agent to execute 'npx ai-api-docs' commands, which runs external Node.js packages. No allowed-tools are specified in the manifest, and the skill provides no implementation files, meaning it relies entirely on executing external, unvetted code. The agent would be running arbitrary npm packages that could contain malicious code, and there's no way to audit what 'ai-api-docs' actually does since it's not included in the skill package.

### MEDIUM Severity

#### [MEDIUM] Potential Credential Exposure via Environment Variable Access

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires access to OPENAI_API_KEY environment variable. If the agent executes the npx command, it would have access to all environment variables in the user's shell, potentially exposing other sensitive credentials (AWS keys, database passwords, etc.) to the external npm package.

#### [MEDIUM] Unbounded File System Traversal Risk

**Severity:** MEDIUM
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** SKILL.md

**Description:** The skill accepts directory paths as arguments (e.g., './src/routes/') with no documented limits on scope or depth. Instructions suggest scanning 'multiple directories' without bounds checking. If the external tool has bugs or malicious intent, it could traverse and read the entire file system, leading to excessive resource consumption or data exposure.

### LOW Severity

#### [LOW] Skill does not specify a license

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

#### [LOW] Missing Metadata: allowed-tools, license, compatibility

**Severity:** LOW
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The YAML manifest is missing optional but recommended fields: allowed-tools (which tools the agent can use), license (though MIT is mentioned in body), and compatibility (which environments this works in). This makes it harder for users to assess the skill's requirements and security posture at a glance.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
