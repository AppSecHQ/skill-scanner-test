# Agent Skill Security Scan Report

**Skill:** social-content
**Directory:** ./skills/coreyhaines31-marketingskills/skills/social-content
**Status:** [OK] SAFE
**Max Severity:** LOW
**Scan Duration:** 28.03s
**Timestamp:** 2026-02-01T10:18:36.888980

## Summary

- **Total Findings:** 5
- **Critical:** 0
- **High:** 0
- **Medium:** 0
- **Low:** 5
- **Info:** 0

## Findings

### LOW Severity

#### [LOW] Skill does not specify a license

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

#### [LOW] Optional Product Marketing Context File Reference

**Severity:** LOW
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** SKILL.md

**Description:** The skill instructions reference an optional file '.claude/product-marketing-context.md' that may exist outside the skill package. While the instruction to 'read it before asking questions' could theoretically be exploited if an attacker controls this file, this is a low-severity concern because: (1) the file is optional and the skill functions without it, (2) it's intended as user-provided context within the user's own workspace, (3) there's no evidence of malicious intent, and (4) the skill doesn't blindly execute instructions from this file but rather uses it as informational context.

#### [LOW] Missing License and Compatibility Metadata

**Severity:** LOW
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill package is missing optional metadata fields 'license' and 'compatibility' in the YAML frontmatter. While these fields are not required by the agent skills specification, including them improves transparency and helps users understand licensing terms and platform compatibility.

#### [LOW] Missing allowed-tools Declaration

**Severity:** LOW
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill does not declare an 'allowed-tools' field in the YAML frontmatter. While this field is optional per the agent skills specification, including it would provide clarity about which agent tools the skill intends to use and enable better security validation.

#### [LOW] Multiple Missing Internal Reference Files

**Severity:** LOW
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill references several internal files that are not found in the package: 'assets/platforms.md', 'templates/platforms.md', 'templates/post-templates.md', 'target.py', 'templates/reverse-engineering.md', 'assets/reverse-engineering.md', and 'assets/post-templates.md'. While some reference files exist (references/platforms.md, references/post-templates.md, references/reverse-engineering.md), the missing files could cause the skill to function incorrectly or provide incomplete guidance. The presence of 'target.py' in the references list is unusual for a content creation skill and warrants investigation.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
