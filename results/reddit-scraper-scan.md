# Agent Skill Security Scan Report

**Skill:** reddit
**Directory:** /workspace/skills/clawhub-reddit-scraper
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 0.82s
**Timestamp:** 2026-02-06T07:35:35.921551

## Summary

- **Total Findings:** 9
- **Critical:** 0
- **High:** 3
- **Medium:** 5
- **Low:** 1
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Suspicious URL detected: https://redd.it/

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/clawhub-reddit-scraper/scripts/reddit_scraper.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

#### [HIGH] Suspicious URL detected: https://reddit.com

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/clawhub-reddit-scraper/scripts/reddit_scraper.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

#### [HIGH] Suspicious URL detected: https://www.reddit.com

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/clawhub-reddit-scraper/scripts/reddit_scraper.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

### MEDIUM Severity

#### [MEDIUM] HTTP client library imports that enable external communication

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_NETWORK_REQUESTS
**Location:** scripts/reddit_scraper.py:13

**Description:** Pattern detected: import requests

#### [MEDIUM] Undeclared network usage

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** TOOL_ABUSE_UNDECLARED_NETWORK

**Description:** Skill code uses network libraries but doesn't declare network requirement

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:80

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: Read-only**: Cannot post

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** scripts/reddit_scraper.py:88

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: get('kind') == 't3':  # t3 = link/post

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** scripts/reddit_scraper.py:157

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: get('score', 0)} ({int(ratio*100)}%) • 💬 {post

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
