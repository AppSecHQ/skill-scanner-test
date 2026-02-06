# Agent Skill Security Scan Report

**Skill:** memory-system-v2
**Directory:** /workspace/skills/clawhub-memory-system-v2
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 24.94s
**Timestamp:** 2026-02-06T04:33:04.349439

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Hardcoded Home Directory Path Without User Consent

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** memory-cli.sh

**Description:** The skill hardcodes MEMORY_DIR to $HOME/clawd/memory and automatically creates directories in the user's home directory without explicit consent or configuration options. This creates persistent storage in a fixed location that users may not be aware of, potentially exposing sensitive memory data.

#### [MEDIUM] Unbounded Memory Growth Without Cleanup Mechanism

**Severity:** MEDIUM
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** memory-cli.sh

**Description:** The skill continuously appends memories to daily logs and maintains a growing JSON index without any documented cleanup, archival, or size limit mechanisms. Over time, this could lead to excessive disk usage and performance degradation as the index grows unbounded.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
