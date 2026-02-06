# Agent Skill Security Scan Report

**Skill:** swarmmarket
**Directory:** /workspace/skills/clawhub-swarmmarket
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 0.25s
**Timestamp:** 2026-02-06T07:50:34.113920

## Summary

- **Total Findings:** 10
- **Critical:** 9
- **High:** 0
- **Medium:** 0
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:72

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl https://api.swarmmarket.ai/api/v1/agents/me

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:76

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl https://api.swarmmarket.ai/api/v1/agents/me

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:89

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl https://api.swarmmarket.ai/api/v1/agents/me

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:122

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl https://api.swarmmarket.ai/api/v1/agents/AGENT_ID

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:129

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl https://api.swarmmarket.ai/api/v1/agents/AGENT_ID/reputation

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:352

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl https://api.swarmmarket.ai/api/v1/wallet/balance

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:453

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl https://api.swarmmarket.ai/health

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:580

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl https://api.swarmmarket.ai/api/v1/agents/{agent_id}/trust

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:608

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl https://api.swarmmarket.ai/api/v1/agents/{agent_id}/trust/history

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
