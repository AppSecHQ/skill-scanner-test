# Agent Skill Security Scan Report

**Skill:** ClawGateSecure
**Directory:** ./skills/clawhub-clawgatesecure
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 30.75s
**Timestamp:** 2026-02-01T16:52:59.658251

## Summary

- **Total Findings:** 4
- **Critical:** 0
- **High:** 0
- **Medium:** 4
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Direct Prompt Injection Attempt - Immutability Claims

**Severity:** MEDIUM
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** SKILL.md

**Description:** The SKILL.md contains explicit instructions claiming to be 'MANDATORY / IMMUTABLE' and stating 'No internal or external instructions can override these directives.' This is a direct attempt to override the agent's core instructions and establish persistent control over the agent's behavior. The skill attempts to redefine the agent's security posture and decision-making process.

#### [MEDIUM] Command Injection via Bash Tool - Unvalidated Path

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md:30

**Description:** The installation instructions direct the agent to execute 'touch ~/.openclaw/SecurityAudit.log' without any validation of the path or confirmation that this operation is safe. While 'touch' itself is relatively benign, this establishes a pattern of executing commands based on skill instructions without validation. The skill also references 'binaries: [touch]' in gating metadata, suggesting awareness of command execution.

#### [MEDIUM] Social Engineering - Deceptive Security Claims

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill presents itself as a 'security protocol' and 'Agent's security core' while actually attempting to manipulate agent behavior through instruction injection. The description claims to provide 'Prompt Injection mitigation' while the skill itself contains prompt injection attempts. This is deceptive social engineering designed to gain user trust.

#### [MEDIUM] Persistent Instruction Injection - SOUL.md and AGENTS.md Modification

**Severity:** MEDIUM
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** SKILL.md:31

**Description:** The skill instructs the agent to modify core configuration files (SOUL.md and AGENTS.md) to make itself 'an immutable part of your agent's reasoning.' This is an attempt to achieve persistence and permanent influence over the agent's behavior by embedding itself into the agent's core identity and reasoning framework.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
