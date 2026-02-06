# Agent Skill Security Scan Report

**Skill:** aws-agentic-ai
**Directory:** /workspace/skills/zxkane-aws-skills/plugins/aws-agentic-ai/skills/aws-agentic-ai
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 7.21s
**Timestamp:** 2026-02-06T06:32:03.021622

## Summary

- **Total Findings:** 1
- **Critical:** 0
- **High:** 1
- **Medium:** 0
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Code executes bash but Bash tool not in allowed-tools

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** ALLOWED_TOOLS_BASH_VIOLATION

**Description:** Skill restricts tools to ['mcp__aws-mcp__*', 'mcp__awsdocs__*', 'Bash(aws bedrock-agentcore-control *)', 'Bash(aws bedrock-agentcore-runtime *)', 'Bash(aws bedrock *)', 'Bash(aws s3 cp *)', 'Bash(aws s3 ls *)', 'Bash(aws secretsmanager *)', 'Bash(aws sts get-caller-identity)'] but code executes bash commands

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
