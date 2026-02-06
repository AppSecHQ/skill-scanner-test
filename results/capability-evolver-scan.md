# Agent Skill Security Scan Report

**Skill:** capability-evolver
**Directory:** /workspace/skills/clawhub-evolver
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 150.30s
**Timestamp:** 2026-02-05T21:26:38.233674

## Summary

- **Total Findings:** 9
- **Critical:** 2
- **High:** 3
- **Medium:** 2
- **Low:** 2
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Direct Prompt Injection: Identity Override and Forced Behavior Modification

**Severity:** CRITICAL
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** SKILL.md

**Description:** The skill explicitly instructs the agent to adopt a new identity ('You are a Recursive Self-Improving System') and forces specific behaviors through mutation directives. The instruction 'Evolution is not optional. Adapt or die' combined with 'Forced Optimization (Refactor/Innovate)' when stable constitutes a direct attempt to override the agent's normal operational constraints and safety guidelines. This is a jailbreak attempt disguised as a feature.

#### [CRITICAL] Autonomous Code Modification Without User Consent

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The skill is designed to autonomously write new code and update agent memory without explicit user approval in 'Mad Dog Mode' (default behavior). The documentation states 'executes changes immediately' and 'assumes fully automated mode' when no flags are provided. This allows the skill to inject arbitrary code modifications into the agent's runtime environment, effectively enabling arbitrary code execution through self-modification.

### HIGH Severity

#### [HIGH] Infinite Loop Mode Enables Resource Exhaustion

**Severity:** HIGH
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** SKILL.md

**Description:** The skill explicitly supports continuous loop execution via '--loop' flag or cron jobs, combined with autonomous code modification capabilities. This creates a risk of runaway processes that continuously modify code, consume resources, and potentially create cascading failures. The 'Infinite Recursion' mitigation mentioned is vague and unverified.

#### [HIGH] Tool Behavior Manipulation via Environment Variables

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill allows runtime modification of tool behavior through environment variables (EVOLVE_REPORT_TOOL) and automatic detection of local skills to 'upgrade its behavior accordingly'. This creates a tool shadowing risk where the skill can redirect standard agent tools to alternative implementations without user awareness, potentially bypassing security controls.

#### [HIGH] Unrestricted Access to Runtime History and Memory

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill claims to 'automatically scans memory and history files' and 'inspect their own runtime history' without any specified access controls or scope limitations. This provides unrestricted read access to potentially sensitive agent memory, conversation history, credentials, and runtime state that may contain user data or system secrets.

### MEDIUM Severity

#### [MEDIUM] Deceptive Framing as 'Evolution' Masks Dangerous Capabilities

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill uses evolutionary biology metaphors ('Evolution is not optional. Adapt or die', 'Genetic Mutation', 'Capability Evolver') to frame what is essentially autonomous code injection and system modification. This social engineering technique makes dangerous capabilities sound natural and beneficial, potentially misleading users about the actual security implications.

#### [MEDIUM] Misleading Safety Claims and Inadequate Risk Disclosure

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The 'Safety & Risk Protocol' section provides false assurance by listing mitigations that are either unverified ('Strict single-process logic') or inadequate (git-sync as primary safety mechanism). The skill downplays the inherent risks of autonomous self-modification and presents dangerous features as safe with minimal controls.

### LOW Severity

#### [LOW] Skill does not specify a license

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

#### [LOW] Missing Manifest Metadata Reduces Transparency

**Severity:** LOW
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill manifest is missing critical metadata fields: license (listed as 'Not specified'), compatibility, and allowed-tools. This reduces transparency about the skill's requirements, restrictions, and intended operating environment. Given the dangerous nature of this skill, complete metadata is especially important for security assessment.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
