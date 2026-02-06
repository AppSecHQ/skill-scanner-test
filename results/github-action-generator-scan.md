# Agent Skill Security Scan Report

**Skill:** github-action-gen
**Directory:** /workspace/skills/clawhub-github-action-gen
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 39.51s
**Timestamp:** 2026-02-06T02:15:04.095336

## Summary

- **Total Findings:** 3
- **Critical:** 1
- **High:** 2
- **Medium:** 0
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Hardcoded External API Dependency with User API Key Requirement

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md:45

**Description:** The skill requires users to provide their OPENAI_API_KEY environment variable to function. This creates a critical security risk as the skill executes an external NPM package (npx ai-github-action) that will have access to the user's OpenAI API key. The skill provides no transparency about how this key is used, where data is sent, or what the external package does with the credentials. Users may unknowingly expose their API keys to untrusted third-party code.

### HIGH Severity

#### [HIGH] Tool Shadowing via External NPM Package Execution

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill instructs users to execute an external NPM package (npx ai-github-action) without providing any source code, verification mechanism, or transparency about what the package does. This is a form of tool shadowing where the skill delegates its core functionality to an unverified external tool. The package could be malicious, compromised, or modified at any time without the user's knowledge. No allowed-tools are declared, and no Python/Bash scripts are provided for inspection.

#### [HIGH] Deceptive Skill Description - External Dependency Not Disclosed

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill description claims to 'Generate GitHub Actions workflows from plain English' but fails to disclose that it actually delegates all functionality to an external NPM package. The description creates the false impression that this is a self-contained skill when it's actually a wrapper around an external tool. Users cannot inspect the actual code that generates workflows, assess its security, or understand what data is transmitted. The marketing language ('Just works', 'Zero config') obscures the security implications of running external code with API key access.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
