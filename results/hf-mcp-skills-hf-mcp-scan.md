# Agent Skill Security Scan Report

**Skill:** hf-mcp
**Directory:** /workspace/skills/huggingface-skills/hf-mcp/skills/hf-mcp
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 41.06s
**Timestamp:** 2026-02-06T02:58:51.870276

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 0
- **Medium:** 3
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] MCP Server Dependency Without Provenance or Security Validation

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill relies entirely on an external MCP (Model Context Protocol) server for all functionality but provides no validation, authentication requirements, or security guidance. The skill instructions assume the HF MCP server is trustworthy and properly configured, creating a transitive trust relationship. If a malicious or compromised MCP server is connected, all operations (model search, data access, job execution, API calls) would be routed through the attacker-controlled server. The skill provides no mechanism to verify server authenticity or validate responses.

#### [MEDIUM] Arbitrary Code Execution via hf_jobs Without Safety Constraints

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The skill enables execution of arbitrary Python scripts and shell commands on remote GPU infrastructure through hf_jobs operations. Examples show direct execution of user-provided code ('Run this Python script on a GPU') and shell commands with no input validation, sandboxing, or safety checks. The 'uv' operation accepts raw Python scripts, and 'run' operation accepts arbitrary Docker images and shell commands. This creates command injection risks if user input is incorporated into scripts or commands without sanitization.

#### [MEDIUM] Dynamic Tool Invocation Without Parameter Validation

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The dynamic_space operation allows invocation of arbitrary Gradio Spaces with user-provided parameters without validation. The skill demonstrates calling external AI tools (e.g., background removal, image generation) by passing parameters directly to unknown endpoints. If a malicious Space is invoked or parameters are crafted maliciously, this could lead to tool exploitation, data exfiltration through tool parameters, or execution of unintended operations.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
