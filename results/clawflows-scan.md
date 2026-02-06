# Agent Skill Security Scan Report

**Skill:** clawflows
**Directory:** /workspace/skills/clawhub-clawflows
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 56.90s
**Timestamp:** 2026-02-05T22:12:55.054221

## Summary

- **Total Findings:** 6
- **Critical:** 1
- **High:** 3
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Arbitrary Code Execution via Untrusted Remote Automations

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill downloads and executes automation YAML files from clawflows.com without any security validation, code signing, or sandboxing. The 'clawflows install' and 'clawflows run' commands fetch remote workflow definitions that can execute arbitrary bash scripts and Python code on the user's machine. There is no mention of signature verification, content validation, or security review of these automations before execution.

### HIGH Severity

#### [HIGH] Transitive Trust Abuse - Delegating Execution to Untrusted External Content

**Severity:** HIGH
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** SKILL.md

**Description:** The skill establishes a transitive trust relationship where the agent blindly follows instructions embedded in remotely-fetched YAML automation files from clawflows.com. The automation files define multi-step workflows with logic, conditions, and data flow that the agent will execute without validation. This is indirect prompt injection - the skill delegates trust to external content that could contain malicious instructions.

#### [HIGH] Tool Chaining for Data Exfiltration via Capability System

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The automation system explicitly supports multi-step tool chaining with data flow between steps (capture and variable substitution). Example workflows show reading data (youtube-data capability), storing it (database capability), and the system supports arbitrary capability combinations. This enables data exfiltration patterns like: read sensitive data → send to external API, collect files → upload to remote server, etc. There are no restrictions on capability chaining or data flow validation.

#### [HIGH] Command Injection Risk via Unvalidated Automation Parameters

**Severity:** HIGH
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The CAPABILITY.md example shows bash script execution with parameter substitution from automation YAML files: './scripts/my-script.sh --param1 "${param1}"'. If automation files from clawflows.com contain malicious parameter values, this could lead to command injection. There is no mention of input validation, sanitization, or escaping of parameters before shell execution.

### MEDIUM Severity

#### [MEDIUM] Deceptive Scope - Automation Registry Presents as Curated but Lacks Security Guarantees

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill presents clawflows.com as a registry of automations with a 'publish via PR' process, implying curation and review. However, there is no mention of security review, malware scanning, or vetting process for published automations. Users may trust automations from the registry assuming they are safe, but the skill provides no security guarantees. The 'clawflows check' command only verifies capability requirements, not security.

#### [MEDIUM] Unbounded Automation Execution Without Resource Limits

**Severity:** MEDIUM
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** SKILL.md

**Description:** The skill supports scheduled automation execution ('clawflows enable' with cron) and multi-step workflows with logic and conditions, but there is no mention of resource limits, timeouts, or execution bounds. Malicious or buggy automations could run indefinitely, consume excessive resources, or create infinite loops. The '--dry-run' flag exists but doesn't prevent resource abuse in actual execution.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
