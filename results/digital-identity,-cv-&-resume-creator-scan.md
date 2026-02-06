# Agent Skill Security Scan Report

**Skill:** talent-de-cv
**Directory:** /workspace/skills/clawhub-id-cv-resume-creator
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 25.31s
**Timestamp:** 2026-02-06T00:11:44.708225

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Transitive Trust Abuse - External Instruction Following

**Severity:** MEDIUM
**Category:** prompt_injection
**Rule ID:** LLM_PROMPT_INJECTION
**Location:** SKILL.md

**Description:** The skill instructs the agent to fetch and follow instructions from external URLs (https://www.talent.de/skills/template-create.md and 13 reference files) for 'Way B' template creation. This creates a transitive trust vulnerability where the agent would execute instructions from untrusted external sources that could be modified by the domain owner at any time to inject malicious commands.

#### [MEDIUM] Potential Data Exfiltration via API Submission

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill facilitates sending user data (name, job title, email, skills, background) to an external API (https://www.talent.de/api) without explicit security validation or user consent mechanisms. While the service appears legitimate, the skill provides no visibility into what data is transmitted, how it's stored, or who can access it. The 'fictional persona' option could be used to mask real data exfiltration.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
