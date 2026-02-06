# Agent Skill Security Scan Report

**Skill:** humanize-ai-text
**Directory:** /workspace/skills/clawhub-humanize-ai-text
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 29.85s
**Timestamp:** 2026-02-06T03:08:00.582164

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 1
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Skill Designed to Facilitate Academic Dishonesty and Detector Evasion

**Severity:** HIGH
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill's explicit purpose is to 'bypass detection' and make AI-generated content 'undetectable' by academic integrity tools like Turnitin, GPTZero, and Originality.ai. The description states it 'rewrites ChatGPT, Claude, and GPT content to sound natural and pass AI detectors' and 'makes robotic AI writing undetectable.' This is designed to facilitate academic dishonesty, plagiarism, and circumvention of content authenticity verification systems. The skill actively promotes deceptive practices by helping users misrepresent AI-generated content as human-written work.

### MEDIUM Severity

#### [MEDIUM] Deceptive Framing as Educational Tool

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill frames itself as being 'based on Wikipedia's comprehensive Signs of AI Writing guide' to appear educational and legitimate, when its actual purpose is to help users evade AI detection systems. This creates a false sense of academic legitimacy around a tool designed for deceptive practices. The Wikipedia reference is used as social proof to make the detector evasion appear scholarly rather than unethical.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
