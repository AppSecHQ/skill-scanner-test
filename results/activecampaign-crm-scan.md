# Agent Skill Security Scan Report

**Skill:** activecampaign
**Directory:** /workspace/skills/clawhub-activecampaign
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 30.27s
**Timestamp:** 2026-02-05T17:52:53.503052

## Summary

- **Total Findings:** 3
- **Critical:** 1
- **High:** 2
- **Medium:** 0
- **Low:** 0
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Hardcoded Credentials in Configuration Files

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill instructs users to store API credentials in plaintext files (~/.config/activecampaign/url and ~/.config/activecampaign/api_key) without encryption or secure storage mechanisms. This creates a critical data exposure risk where credentials can be easily accessed by malicious actors or other processes on the system.

### HIGH Severity

#### [HIGH] Missing Binary Dependency Without Verification

**Severity:** HIGH
**Category:** unauthorized_tool_use
**Rule ID:** LLM_UNAUTHORIZED_TOOL_USE
**Location:** YAML frontmatter

**Description:** The skill requires an 'activecampaign' binary (specified in openclaw.requires.bins) but provides no information about where to obtain it, how to verify its authenticity, or its provenance. This creates a supply chain risk where users might install malicious binaries from untrusted sources.

#### [HIGH] Missing Referenced Configuration Files

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill references critical configuration files (config.py, sample.py) that are not found in the package. These files are mentioned in instructions for field configuration and initialization but are absent, creating uncertainty about what code would actually execute and potential for malicious file substitution.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
