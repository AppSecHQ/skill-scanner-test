# Agent Skill Security Scan Report

**Skill:** gemini
**Directory:** /workspace/skills/softaworks-agent-toolkit/skills/gemini
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 33.29s
**Timestamp:** 2026-02-06T01:57:59.160010

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Unrestricted Tool Approval Mode Enables Arbitrary Command Execution

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill instructions explicitly recommend using '--approval-mode yolo' for automated tasks, which auto-approves ALL tools without user confirmation. This allows the Gemini CLI to execute arbitrary bash commands, file operations, and other tools without oversight. While the skill correctly warns against using 'default' mode in non-interactive contexts, the 'yolo' mode creates a security risk by removing all approval gates. An attacker could craft prompts that cause Gemini to execute malicious commands, modify files, or exfiltrate data, all auto-approved by the yolo mode.

#### [MEDIUM] Transitive Trust to External AI Model Without Input Validation

**Severity:** MEDIUM
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** SKILL.md

**Description:** The skill delegates complete trust to the Gemini CLI and its underlying AI models (Gemini 3 Pro, Flash, etc.) to process user codebases and execute commands. There is no validation, sanitization, or filtering of what the external Gemini model might instruct the agent to do. If the Gemini model is compromised, manipulated via prompt injection, or produces malicious output, the agent will follow those instructions when using 'yolo' or 'auto_edit' modes. This creates an indirect prompt injection vector where untrusted content from Gemini's responses could influence the agent's behavior.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
