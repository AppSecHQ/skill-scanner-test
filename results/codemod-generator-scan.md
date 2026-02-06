# Agent Skill Security Scan Report

**Skill:** codemod-gen
**Directory:** /workspace/skills/clawhub-ai-codemod
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 37.60s
**Timestamp:** 2026-02-05T22:40:21.138114

## Summary

- **Total Findings:** 4
- **Critical:** 0
- **High:** 2
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Hardcoded External API Key Requirement

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires users to set an OPENAI_API_KEY environment variable to function. This creates a credential exposure risk as the skill executes external npx commands that will have access to this API key. The skill does not disclose how this key is used, transmitted, or protected during codemod generation. Users may unknowingly expose their OpenAI API keys to third-party code execution.

#### [HIGH] Unverified External Package Execution

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill instructs users to execute 'npx ai-codemod' which downloads and runs code from npm registry without any verification, version pinning, or provenance checking. This creates a supply chain attack vector where malicious code could be executed with full access to the user's codebase and environment variables (including OPENAI_API_KEY). The package source is not verified against the claimed GitHub repository.

### MEDIUM Severity

#### [MEDIUM] Arbitrary Code Generation and Execution

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The skill generates and executes AST transformation code (jscodeshift codemods) based on plain English descriptions. This creates a code injection risk where malicious or poorly formed prompts could generate codemods that perform unintended operations on the user's codebase. The generated code runs with full filesystem access and could modify, delete, or exfiltrate code.

#### [MEDIUM] Misleading Scope and Risk Disclosure

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill description emphasizes ease of use ('One command. Zero config. Just works.') while downplaying significant security risks. It encourages running transformations across entire codebases ('500 files') without adequate warnings about the risks of automated code modification, credential exposure, or supply chain attacks. The 'Best Practices' section mentions testing but does not emphasize security review.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
