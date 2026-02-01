# Agent Skill Security Scan Report

**Skill:** youtube-search
**Directory:** ./skills/clawhub-youtube-search
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 17.88s
**Timestamp:** 2026-02-01T08:53:03.967884

## Summary

- **Total Findings:** 1
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] API Key Exposure Risk via Environment Variable

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires users to store the TRANSCRIPT_API_KEY in ~/.zshenv, which is a shell configuration file that may be readable by other processes or inadvertently committed to version control. While environment variables are a common practice, the instructions do not warn users about protecting this credential or the risks of exposure. The API key provides access to a paid service (100 free credits) and could be abused if exposed.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
