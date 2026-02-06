# Agent Skill Security Scan Report

**Skill:** deps-analyzer
**Directory:** /workspace/skills/clawhub-deps-checker
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 34.07s
**Timestamp:** 2026-02-06T00:04:10.566724

## Summary

- **Total Findings:** 7
- **Critical:** 1
- **High:** 2
- **Medium:** 2
- **Low:** 2
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Hardcoded External API Dependency with Required API Key

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires an OPENAI_API_KEY environment variable to function, which means it will access and potentially transmit project dependency data to OpenAI's external servers. This creates a data exfiltration risk where sensitive information about the user's project structure, dependency names, versions, and potentially proprietary package information is sent to a third-party service without explicit user consent or warning in the description.

### HIGH Severity

#### [HIGH] Deceptive Description - Omits External API Dependency

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill description ('Find unused and outdated dependencies. Use when your package.json is a mess.') presents this as a simple local analysis tool, but fails to disclose that it sends project data to OpenAI's API. This is social engineering through omission - users expect a local dependency analyzer but get a tool that transmits their project information to external servers.

#### [HIGH] Unauthorized External Tool Execution via npx

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill instructs execution of 'npx ai-deps' which downloads and runs arbitrary code from npm registry without any verification, version pinning, or security checks. This creates a supply chain attack vector where a compromised or malicious 'ai-deps' package could execute arbitrary code on the user's machine with full access to their project and environment variables (including the OPENAI_API_KEY).

### MEDIUM Severity

#### [MEDIUM] Environment Variable Credential Exposure Risk

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires access to OPENAI_API_KEY environment variable, which could be inadvertently exposed through error messages, logs, or debugging output. If the external tool or its dependencies have vulnerabilities, this API key could be leaked or stolen.

#### [MEDIUM] Auto-Fix Feature Without Adequate Safety Warnings

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The '--fix' flag automatically removes dependencies from package.json without sufficient warnings about potential risks. The skill mentions 'some deps are used dynamically' but the auto-fix feature could break applications by removing legitimately used dependencies that aren't detected by static analysis.

### LOW Severity

#### [LOW] Skill does not specify a license

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

#### [LOW] Missing Metadata Fields - No Provenance Information

**Severity:** LOW
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill manifest is missing critical metadata fields including license, compatibility, and allowed-tools. While the body mentions 'MIT' license, it's not in the YAML frontmatter. This lack of structured metadata makes it harder to assess the skill's trustworthiness and intended usage scope.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
