# Agent Skill Security Scan Report

**Skill:** ci-gen
**Directory:** /workspace/skills/clawhub-ai-ci
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 46.91s
**Timestamp:** 2026-02-05T21:45:14.053708

## Summary

- **Total Findings:** 5
- **Critical:** 1
- **High:** 2
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Hardcoded External API Key Requirement

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md:45

**Description:** The skill requires users to set OPENAI_API_KEY environment variable to function. This creates a critical data exfiltration risk as the skill executes an external NPX package (ai-ci) that has full access to this API key. The external package could transmit the API key to arbitrary servers, use it for unauthorized API calls, or log it. Users are instructed to expose their OpenAI credentials to untrusted third-party code without any security warnings.

### HIGH Severity

#### [HIGH] Unauthorized External Package Execution

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md:11

**Description:** The skill instructs the agent to execute an external NPX package (ai-ci) that is not included in the skill package itself. This is tool exploitation through external code execution. The agent has no visibility into what this package does, creating risks of: arbitrary code execution on user's machine, file system access beyond skill scope, network calls to unknown endpoints, and potential malware. The package is fetched from NPM registry at runtime without version pinning or integrity verification.

#### [HIGH] Arbitrary Command Execution Without Validation

**Severity:** HIGH
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The skill allows arbitrary command-line arguments to be passed to the external NPX package without any validation or sanitization. Arguments like '--deploy', '--preview' are passed directly to the external executable. This creates command injection risks if user input is incorporated into these commands, and allows the external package to perform arbitrary operations (deploy to AWS, Docker, etc.) without user confirmation or security boundaries.

### MEDIUM Severity

#### [MEDIUM] Misleading Skill Packaging

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill presents itself as a self-contained CI generator tool but actually functions as a wrapper that executes external, unvetted code. The description 'Generate GitHub Actions workflows from your project' implies the skill contains the generation logic, but it merely invokes an external NPX package. This is social engineering through deceptive packaging - users expect to review skill code before use, but the actual functionality is hidden in an external package.

#### [MEDIUM] Unrestricted File System Access

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md:55

**Description:** The skill description states it 'Scans your project to detect language and framework' and 'Analyzes your package.json, config files, and project structure'. This indicates the external package will read arbitrary files from the user's project directory without any declared restrictions. Combined with network access (NPX package can make HTTP calls), this creates a data exfiltration pathway where project files, configuration, and potentially secrets could be transmitted externally.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
