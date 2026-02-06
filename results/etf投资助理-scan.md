# Agent Skill Security Scan Report

**Skill:** etf-assistant
**Directory:** /workspace/skills/clawhub-etf-assistant
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 29.63s
**Timestamp:** 2026-02-06T00:53:41.449945

## Summary

- **Total Findings:** 11
- **Critical:** 5
- **High:** 0
- **Medium:** 1
- **Low:** 5
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** etf-assistant.sh:11

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0;31m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** etf-assistant.sh:12

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0;32m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** etf-assistant.sh:13

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[1;33m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** etf-assistant.sh:15

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0;34m

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_script_injection
**Location:** etf-assistant.sh:15

**Description:** Detects embedded scripting payloads (JS, VBScript, etc.) in MCP tool descriptions: \033[0m

### MEDIUM Severity

#### [MEDIUM] Unvalidated External Network Calls to Yahoo Finance

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** etf-assistant.sh

**Description:** The skill makes HTTP requests to Yahoo Finance API (query1.finance.yahoo.com) without any validation of response content or error handling for malicious responses. While Yahoo Finance is a legitimate service, the skill blindly trusts and processes external data without sanitization. The curl commands use '-s' (silent) flag which suppresses errors, and responses are directly parsed and displayed to users without validation.

### LOW Severity

#### [LOW] Skill does not specify a license

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

#### [LOW] Missing Optional Metadata Fields

**Severity:** LOW
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill's YAML manifest is missing several optional but recommended fields: 'license' (not specified), 'compatibility' (not specified), and 'allowed-tools' (not specified). While these fields are optional per the agent skills specification, their absence makes it harder for users to understand the skill's requirements and restrictions. The skill uses Bash extensively but doesn't declare this in allowed-tools.

#### [LOW] Potential Resource Exhaustion in Retry Logic

**Severity:** LOW
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** etf-assistant.sh

**Description:** The cmd_price function implements a retry mechanism with sleep delays (sleep 2) but lacks maximum retry limits or timeout controls. If the Yahoo Finance API is unresponsive, this could lead to extended blocking or resource consumption. The retry logic uses 'continue' in a loop without bounds checking.

#### [LOW] Investment Advice Disclaimer Insufficient

**Severity:** LOW
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** While the skill includes disclaimers in Chinese and English ('Investment involves risk', 'For reference only, not investment advice'), these warnings appear only in the documentation. The actual command outputs (price quotes, DCA calculations, hot ETF recommendations) do not include inline disclaimers, which could mislead users into treating the information as actionable investment advice.

#### [LOW] Skill description is too short

**Severity:** LOW
**Category:** social_engineering
**Rule ID:** TRIGGER_DESCRIPTION_TOO_SHORT
**Location:** SKILL.md

**Description:** Description has only 3 words. Short descriptions may not provide enough context for the agent to determine when this skill should be used.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
