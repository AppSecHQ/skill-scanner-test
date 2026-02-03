# Agent Skill Security Scan Report

**Skill:** aws-agentic-ai
**Directory:** ./skills/zxkane-aws-skills/plugins/aws-agentic-ai/skills/aws-agentic-ai
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.38s
**Timestamp:** 2026-02-03T14:28:40.079706

## Summary

- **Total Findings:** 15
- **Critical:** 11
- **High:** 1
- **Medium:** 1
- **Low:** 2
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** services/gateway/deploy-template.sh:3

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: Template

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** services/gateway/deploy-template.sh:8

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0;31m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** services/gateway/deploy-template.sh:9

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0;32m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** services/gateway/deploy-template.sh:10

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[1;33m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** services/gateway/deploy-template.sh:11

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0m

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** services/gateway/deploy-template.sh:45

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export $(cat $ENV_FILE

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** services/gateway/validate-deployment.sh:8

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0;31m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** services/gateway/validate-deployment.sh:9

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0;32m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** services/gateway/validate-deployment.sh:10

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[1;33m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** services/gateway/validate-deployment.sh:11

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0;34m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** services/gateway/validate-deployment.sh:12

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0m

### HIGH Severity

#### [HIGH] Code executes bash but Bash tool not in allowed-tools

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** ALLOWED_TOOLS_BASH_VIOLATION

**Description:** Skill restricts tools to ['mcp__aws-mcp__*', 'mcp__awsdocs__*', 'Bash(aws bedrock-agentcore-control *)', 'Bash(aws bedrock-agentcore-runtime *)', 'Bash(aws bedrock *)', 'Bash(aws s3 cp *)', 'Bash(aws s3 ls *)', 'Bash(aws secretsmanager *)', 'Bash(aws sts get-caller-identity)'] but code executes bash commands

### MEDIUM Severity

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:30

**Description:** Detects skills that delegate trust to untrusted external content: execute code

### LOW Severity

#### [LOW] Skill does not specify a license

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

#### [LOW] Code uses search/grep patterns but Grep tool not in allowed-tools

**Severity:** LOW
**Category:** unauthorized_tool_use
**Rule ID:** ALLOWED_TOOLS_GREP_VIOLATION

**Description:** Skill restricts tools to ['mcp__aws-mcp__*', 'mcp__awsdocs__*', 'Bash(aws bedrock-agentcore-control *)', 'Bash(aws bedrock-agentcore-runtime *)', 'Bash(aws bedrock *)', 'Bash(aws s3 cp *)', 'Bash(aws s3 ls *)', 'Bash(aws secretsmanager *)', 'Bash(aws sts get-caller-identity)'] but code uses regex search patterns

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
