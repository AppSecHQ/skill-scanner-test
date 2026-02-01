# Agent Skill Security Scan Report

**Skill:** health-tracker
**Directory:** ./skills/clawhub-healthcheck
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 33.15s
**Timestamp:** 2026-02-01T18:21:31.957952

## Summary

- **Total Findings:** 5
- **Critical:** 0
- **High:** 0
- **Medium:** 1
- **Low:** 4
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Unbounded Autonomy with Auto-Logging Without User Consent

**Severity:** MEDIUM
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** SKILL.md

**Description:** The skill implements an 'auto-log' feature that automatically records water intake entries (with 0 cups) if the user does not respond within 15 minutes of a reminder. This creates an unbounded autonomous behavior where the system makes persistent modifications to user data without explicit consent. The auto-log entries are marked as automatic but still pollute the data history and could interfere with accurate habit tracking and statistics.

### LOW Severity

#### [LOW] Skill does not specify a license

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

#### [LOW] Undeclared Tool Usage and Missing Tool Restrictions

**Severity:** LOW
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** SKILL.md

**Description:** The skill declares three tools (log_water, log_sleep, view_stats) in its documentation but does not specify 'allowed-tools' in the YAML manifest. While this field is optional, the skill's behavior suggests it requires Write access (to modify health-data.json), Read access (to retrieve statistics), and potentially scheduling capabilities (node-cron for reminders). The absence of declared tool restrictions means there's no validation that the skill operates within expected boundaries.

#### [LOW] Missing Critical Metadata Fields

**Severity:** LOW
**Category:** social_engineering
**Rule ID:** LLM_SOCIAL_ENGINEERING
**Location:** SKILL.md

**Description:** The skill's YAML manifest is missing several important metadata fields including 'license' and 'compatibility'. While 'author' and 'version' are present in additional metadata, the lack of license information makes it unclear under what terms the skill can be used or modified. The missing compatibility field doesn't inform users which agent environments support this skill's features (especially the scheduling/reminder functionality).

#### [LOW] External Dependency Without Provenance Verification

**Severity:** LOW
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill requires installation of 'node-cron' package via npm but provides no version pinning, integrity verification, or provenance information. This creates a minor supply chain risk where the skill could pull an unexpected version of the dependency or a compromised package. However, node-cron is a well-known legitimate package, reducing the actual risk.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
