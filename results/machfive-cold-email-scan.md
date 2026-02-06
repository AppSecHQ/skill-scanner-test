# Agent Skill Security Scan Report

**Skill:** cold-email
**Directory:** /workspace/skills/clawhub-cold-email
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 31.93s
**Timestamp:** 2026-02-06T04:16:51.735117

## Summary

- **Total Findings:** 2
- **Critical:** 0
- **High:** 1
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Hardcoded API Key Requirement with External Data Transmission

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION

**Description:** The skill requires MACHFIVE_API_KEY environment variable and transmits potentially sensitive lead data (names, emails, LinkedIn URLs, company information) to external third-party API (app.machfive.io). This creates risk of credential theft if the environment variable is compromised, and data exfiltration of user's lead/contact databases to an external service without explicit security controls or data handling guarantees.

### MEDIUM Severity

#### [MEDIUM] Long-Running Synchronous Operations Without Timeout Warnings

**Severity:** MEDIUM
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** SKILL.md

**Description:** The single lead generation endpoint is documented to take 3-5 minutes with recommended timeout of 5-10 minutes. This creates availability risk if multiple requests are made concurrently or if the external API becomes unresponsive, potentially causing agent hangs or resource exhaustion.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
