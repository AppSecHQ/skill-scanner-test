# Agent Skill Security Scan Report

**Skill:** launch-strategy
**Directory:** ./skills/coreyhaines31-marketingskills/skills/launch-strategy
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 28.15s
**Timestamp:** 2026-02-01T10:50:46.121906

## Summary

- **Total Findings:** 5
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 3
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Transitive Trust Abuse - External Context File Dependency

**Severity:** MEDIUM
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** SKILL.md

**Description:** The skill instructions direct the agent to read and trust content from '.claude/product-marketing-context.md' without validation. This file is external to the skill package and could contain malicious instructions that override the skill's intended behavior. The instruction 'read it before asking questions. Use that context' creates a transitive trust relationship where untrusted external content can influence agent behavior.

#### [MEDIUM] Missing Referenced File - Broken Tool Dependency

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE

**Description:** The skill references 'content.py' in its instructions but this file is not included in the skill package. This creates an incomplete tool dependency that could lead to skill malfunction or could be exploited if an attacker places a malicious 'content.py' file in the expected location. The skill cannot function as intended without this file.

### LOW Severity

#### [LOW] Skill does not specify a license

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

#### [LOW] Incomplete Skill Package Metadata

**Severity:** LOW
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill manifest is missing several optional but recommended metadata fields: 'license', 'compatibility', and 'allowed-tools'. While these fields are optional per the agent skills specification, their absence reduces transparency about the skill's intended usage constraints and compatibility. The 'allowed-tools' field would be particularly useful to declare that this skill only needs Read access (for reading context files).

#### [LOW] Truncated Instruction Content

**Severity:** LOW
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The instruction body appears to be incomplete, ending mid-sentence with 'Tap into someone else's audience to shortcut the hardest par'. This truncation could lead to incomplete or misleading guidance being provided to users. While not a direct security threat, incomplete instructions could cause the agent to behave unpredictably or provide incomplete advice.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
