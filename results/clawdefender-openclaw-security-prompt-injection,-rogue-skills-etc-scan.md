# Agent Skill Security Scan Report

**Skill:** clawdefender
**Directory:** ./skills/clawhub-clawdefender
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.42s
**Timestamp:** 2026-02-02T03:06:49.217701

## Summary

- **Total Findings:** 37
- **Critical:** 22
- **High:** 9
- **Medium:** 5
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Modifying system permissions or configuration

**Severity:** CRITICAL
**Category:** unauthorized_tool_use
**Rule ID:** TOOL_ABUSE_SYSTEM_MODIFICATION
**Location:** scripts/clawdefender.sh:147

**Description:** Pattern detected: chmod 777

#### [CRITICAL] Modifying system permissions or configuration

**Severity:** CRITICAL
**Category:** unauthorized_tool_use
**Rule ID:** TOOL_ABUSE_SYSTEM_MODIFICATION
**Location:** scripts/clawdefender.sh:214

**Description:** Pattern detected: /etc/passwd

#### [CRITICAL] Modifying system permissions or configuration

**Severity:** CRITICAL
**Category:** unauthorized_tool_use
**Rule ID:** TOOL_ABUSE_SYSTEM_MODIFICATION
**Location:** scripts/clawdefender.sh:215

**Description:** Pattern detected: /etc/shadow

#### [CRITICAL] PROMPT INJECTION detected by YARA

**Severity:** CRITICAL
**Category:** prompt_injection
**Rule ID:** YARA_prompt_injection
**Location:** SKILL.md:76

**Description:** Detects prompt strings used to override or force malicious tool calls: Do NOT follow any instructions

#### [CRITICAL] PROMPT INJECTION detected by YARA

**Severity:** CRITICAL
**Category:** prompt_injection
**Rule ID:** YARA_prompt_injection
**Location:** SKILL.md:197

**Description:** Detects prompt strings used to override or force malicious tool calls: Do NOT follow instructions

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/sanitize.sh:24

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0;31m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/sanitize.sh:25

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[1;33m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/sanitize.sh:26

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0;32m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/sanitize.sh:27

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/clawdefender.sh:23

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0;31m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/clawdefender.sh:24

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[1;33m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/clawdefender.sh:25

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0;32m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/clawdefender.sh:26

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0;34m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/clawdefender.sh:27

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0;33m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** scripts/clawdefender.sh:28

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** scripts/clawdefender.sh:151

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: nc -e

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** scripts/clawdefender.sh:153

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: bash -i

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** scripts/clawdefender.sh:214

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: '/etc/passwd'

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** scripts/clawdefender.sh:215

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: '/etc/shadow'

#### [CRITICAL] PROMPT INJECTION detected by YARA

**Severity:** CRITICAL
**Category:** prompt_injection
**Rule ID:** YARA_prompt_injection
**Location:** scripts/clawdefender.sh:76

**Description:** Detects prompt strings used to override or force malicious tool calls: ignore your instructions

#### [CRITICAL] PROMPT INJECTION detected by YARA

**Severity:** CRITICAL
**Category:** prompt_injection
**Rule ID:** YARA_prompt_injection
**Location:** scripts/clawdefender.sh:83

**Description:** Detects prompt strings used to override or force malicious tool calls: forget your instructions

#### [CRITICAL] PROMPT INJECTION detected by YARA

**Severity:** CRITICAL
**Category:** prompt_injection
**Rule ID:** YARA_prompt_injection
**Location:** scripts/clawdefender.sh:84

**Description:** Detects prompt strings used to override or force malicious tool calls: forget everything above

### HIGH Severity

#### [HIGH] Attempts to override previous system instructions

**Severity:** HIGH
**Category:** prompt_injection
**Rule ID:** PROMPT_INJECTION_IGNORE_INSTRUCTIONS
**Location:** SKILL.md:98

**Description:** Pattern detected: ignore previous instructions

#### [HIGH] Attempts to override previous system instructions

**Severity:** HIGH
**Category:** prompt_injection
**Rule ID:** PROMPT_INJECTION_IGNORE_INSTRUCTIONS
**Location:** SKILL.md:129

**Description:** Pattern detected: ignore previous instructions

#### [HIGH] SYSTEM MANIPULATION detected by YARA

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** YARA_system_manipulation
**Location:** SKILL.md:121

**Description:** Detects system manipulation, privilege escalation, and destructive file operations: rm -rf

#### [HIGH] SYSTEM MANIPULATION detected by YARA

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** YARA_system_manipulation
**Location:** SKILL.md:157

**Description:** Detects system manipulation, privilege escalation, and destructive file operations: rm -rf

#### [HIGH] SYSTEM MANIPULATION detected by YARA

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** YARA_system_manipulation
**Location:** SKILL.md:161

**Description:** Detects system manipulation, privilege escalation, and destructive file operations: chmod 777

#### [HIGH] SYSTEM MANIPULATION detected by YARA

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** YARA_system_manipulation
**Location:** scripts/clawdefender.sh:145

**Description:** Detects system manipulation, privilege escalation, and destructive file operations: rm -rf

#### [HIGH] SYSTEM MANIPULATION detected by YARA

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** YARA_system_manipulation
**Location:** scripts/clawdefender.sh:146

**Description:** Detects system manipulation, privilege escalation, and destructive file operations: rm -rf

#### [HIGH] SYSTEM MANIPULATION detected by YARA

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** YARA_system_manipulation
**Location:** scripts/clawdefender.sh:622

**Description:** Detects system manipulation, privilege escalation, and destructive file operations: rm -rf

#### [HIGH] SYSTEM MANIPULATION detected by YARA

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** YARA_system_manipulation
**Location:** scripts/clawdefender.sh:147

**Description:** Detects system manipulation, privilege escalation, and destructive file operations: chmod 777

### MEDIUM Severity

#### [MEDIUM] Attempts to reveal system prompts or configuration

**Severity:** MEDIUM
**Category:** prompt_injection
**Rule ID:** PROMPT_INJECTION_REVEAL_SYSTEM
**Location:** SKILL.md:133

**Description:** Pattern detected: reveal the system prompt

#### [MEDIUM] User input used in command substitution - potential injection risk

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** COMMAND_INJECTION_USER_INPUT
**Location:** scripts/clawdefender.sh:655

**Description:** Pattern detected: $(validate_url "$2")

#### [MEDIUM] User input used in command substitution - potential injection risk

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** COMMAND_INJECTION_USER_INPUT
**Location:** scripts/clawdefender.sh:690

**Description:** Pattern detected: $(date -r "$0" '+%Y-%m-%d')

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:197

**Description:** Detects skills that delegate trust to untrusted external content: follow instructions in the content

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:194

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: get-email

### LOW Severity

#### [LOW] Skill does not specify a license

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
