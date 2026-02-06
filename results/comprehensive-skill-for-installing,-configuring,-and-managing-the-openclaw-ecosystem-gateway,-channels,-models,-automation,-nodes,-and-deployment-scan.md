# Agent Skill Security Scan Report

**Skill:** openclaw
**Directory:** /workspace/skills/clawhub-openclaw-anything
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 53.19s
**Timestamp:** 2026-02-05T23:10:31.430026

## Summary

- **Total Findings:** 7
- **Critical:** 0
- **High:** 2
- **Medium:** 3
- **Low:** 2
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Hardcoded Gateway Token in Configuration Schema

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** references/config-schema.md:7

**Description:** The configuration schema documentation reveals that gateway authentication uses a token stored in plaintext in ~/.openclaw/openclaw.json. The example shows 'your-gateway-token' as a placeholder, but this pattern encourages storing sensitive authentication credentials in unencrypted configuration files. If the gateway binds to 0.0.0.0 or a public IP with this token, it becomes a critical authentication secret that could be exposed through file system access.

#### [HIGH] Unrestricted Shell Command Execution via Exec Tool

**Severity:** HIGH
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** references/advanced-tools.md:7

**Description:** The skill enables an 'exec' tool that allows agents to run arbitrary shell commands. While mentioned as 'controlled by tools.policy', the documentation does not specify what restrictions are enforced by default. The bash wrapper script passes commands directly to the openclaw CLI without visible sanitization or validation, creating command injection risks if user input flows into these commands.

### MEDIUM Severity

#### [MEDIUM] Elevated Privilege Mode Without Clear Authorization Flow

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** references/advanced-tools.md:14

**Description:** The skill describes an 'Elevated Mode' that grants temporary high-privilege permissions to agents. The authorization mechanism relies on user approval via 'Control UI or CLI', but the documentation does not specify timeout limits, scope restrictions, or audit logging for elevated operations. This creates risk of privilege escalation if the approval mechanism is bypassed or if elevated permissions persist longer than necessary.

#### [MEDIUM] Unbounded Browser Control Without Resource Limits

**Severity:** MEDIUM
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** scripts/openclaw.sh:42

**Description:** The skill provides Playwright-powered browser control capabilities without documented resource limits or timeout constraints. The browser tool can be started and controlled by agents, but there are no visible safeguards against resource exhaustion from opening multiple browser instances, infinite page loads, or memory leaks.

#### [MEDIUM] Plugin System Without Signature Verification

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** references/advanced-tools.md:38

**Description:** The skill supports a plugin system where users can install plugins from paths, but the documentation does not mention signature verification, sandboxing, or security vetting of plugins. Malicious plugins could execute arbitrary code with the same privileges as the OpenClaw gateway.

### LOW Severity

#### [LOW] Public IP Binding Without Strong Authentication Warning

**Severity:** LOW
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** references/deployment.md:52

**Description:** The documentation mentions binding the gateway to 0.0.0.0 for remote access but does not prominently warn about the security implications. While it mentions using a token, there is insufficient emphasis on the critical importance of strong authentication when exposing the gateway publicly.

#### [LOW] Cron Jobs Without Execution Limits

**Severity:** LOW
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** references/nodes-platforms.md:31

**Description:** The skill supports scheduled cron jobs that can send messages and potentially execute other actions, but there are no documented limits on job frequency, execution time, or resource usage. Misconfigured cron jobs could cause resource exhaustion or spam.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
