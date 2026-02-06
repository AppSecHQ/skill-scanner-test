# Agent Skill Security Scan Report

**Skill:** gaussian-process-mlp-hybrid
**Directory:** /workspace/skills/clawhub-gaussian-process-mlp-hybrid
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 24.66s
**Timestamp:** 2026-02-05T18:51:46.789376

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Misleading Skill Description and Purpose

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill's YAML description claims it is for 'Discussion on Gaussian Process and MLP hybrid models for uncertainty estimation' and suggests use 'when exploring machine learning model architectures.' However, the actual instruction body contains a Reddit post asking questions about GP+MLP drawbacks, not providing discussion capabilities or ML architecture exploration. The skill appears to be auto-generated content from a Reddit post rather than a functional skill, creating a mismatch between stated purpose and actual content.

### LOW Severity

#### [LOW] Missing Referenced File

**Severity:** LOW
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE

**Description:** The instruction body references 'screening.py' but this file is not found in the skill package. This creates a broken reference that could cause confusion or errors if the skill attempts to use this file. While not a direct security threat, it indicates incomplete skill packaging.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
