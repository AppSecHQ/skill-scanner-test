# Agent Skill Security Scan Report

**Skill:** durable-objects
**Directory:** /workspace/skills/cloudflare-skills/skills/durable-objects
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 0.23s
**Timestamp:** 2026-02-06T07:47:20.706919

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 0
- **Medium:** 2
- **Low:** 1
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** SKILL.md:67

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): exec(`
        CREATE TABLE IF NOT EXISTS items (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
  

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** SKILL.md:131

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): exec("INSERT INTO t (c)

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
