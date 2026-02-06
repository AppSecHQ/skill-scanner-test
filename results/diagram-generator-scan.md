# Agent Skill Security Scan Report

**Skill:** diagram-gen
**Directory:** /workspace/skills/clawhub-diagram-gen
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 44.41s
**Timestamp:** 2026-02-06T00:07:50.229202

## Summary

- **Total Findings:** 4
- **Critical:** 1
- **High:** 2
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Hardcoded External API Key Requirement with Unclear Data Transmission

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION

**Description:** The skill requires an OPENAI_API_KEY environment variable but provides no transparency about what data is sent to OpenAI's servers. The tool reads the user's entire codebase and processes it, but there is no disclosure about whether source code is transmitted externally to OpenAI's API for diagram generation. This creates a critical data exfiltration risk where proprietary source code could be sent to third-party servers without explicit user consent or awareness.

### HIGH Severity

#### [HIGH] Tool Shadowing via NPX with Unverified Package

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE

**Description:** The skill instructs the agent to execute 'npx ai-diagram' which downloads and runs arbitrary JavaScript code from npm registries without any package verification, version pinning, or provenance checking. This creates a tool shadowing risk where a malicious package could replace legitimate functionality. The package name 'ai-diagram' is not verified to be from LXGIC Studios, and npx will execute whatever package matches that name in the npm registry.

#### [HIGH] Unbounded Codebase Processing Without Resource Limits

**Severity:** HIGH
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE

**Description:** The skill instructs processing entire source directories ('npx ai-diagram ./src/') without any resource limits, file size restrictions, or scope boundaries. This could lead to resource exhaustion when processing large codebases, potentially causing denial of service through excessive CPU, memory, or API quota consumption. The instruction 'don't diagram everything' in best practices contradicts the actual usage examples that target entire directories.

### MEDIUM Severity

#### [MEDIUM] Misleading Zero-Config Claims with Hidden API Key Requirement

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING

**Description:** The skill markets itself as 'Zero config. Just works' and 'No install needed. Just run with npx' but actually requires OPENAI_API_KEY environment variable configuration. This is deceptive social engineering that misleads users about the actual setup requirements and external dependencies. Users may unknowingly expose their OpenAI API keys or be surprised by API usage costs.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
