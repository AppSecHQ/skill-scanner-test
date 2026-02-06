# Agent Skill Security Scan Report

**Skill:** zotero
**Directory:** /workspace/skills/clawhub-zotero
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 30.24s
**Timestamp:** 2026-02-06T07:56:00.177656

## Summary

- **Total Findings:** 19
- **Critical:** 1
- **High:** 11
- **Medium:** 6
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] CREDENTIAL HARVESTING detected by YARA

**Severity:** CRITICAL
**Category:** hardcoded_secrets
**Rule ID:** YARA_credential_harvesting
**Location:** SKILL.md:92

**Description:** Detects potential exposure of sensitive information like API keys, passwords, tokens, and certificates: export --format csljson --collection COLLKEY

### HIGH Severity

#### [HIGH] Accessing sensitive system or credential files

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_SENSITIVE_FILES
**Location:** scripts/zotero.py:1049

**Description:** Pattern detected: open(filepath

#### [HIGH] Suspicious URL detected: https://translate.zotero.org/web

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/clawhub-zotero/scripts/zotero.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

#### [HIGH] Suspicious URL detected: https://doi.org/

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/clawhub-zotero/scripts/zotero.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

#### [HIGH] Suspicious URL detected: https://www.worldcat.org/isbn/

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/clawhub-zotero/scripts/zotero.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

#### [HIGH] Suspicious URL detected: https://pubmed.ncbi.nlm.nih.gov/

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/clawhub-zotero/scripts/zotero.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

#### [HIGH] Suspicious URL detected: https://api.crossref.org/works/

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/clawhub-zotero/scripts/zotero.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

#### [HIGH] Suspicious URL detected: https://api.crossref.org/works?

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/clawhub-zotero/scripts/zotero.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

#### [HIGH] Suspicious URL detected: https://api.unpaywall.org/v2/

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/clawhub-zotero/scripts/zotero.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

#### [HIGH] Suspicious URL detected: https://api.semanticscholar.org/graph/v1/paper/DOI:

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/clawhub-zotero/scripts/zotero.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

#### [HIGH] Suspicious URL detected: https://doi.org/

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/clawhub-zotero/scripts/zotero.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

#### [HIGH] Suspicious URL detected: https://api.zotero.org

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/clawhub-zotero/scripts/zotero.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

### MEDIUM Severity

#### [MEDIUM] HTTP client library imports that enable external communication

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_NETWORK_REQUESTS
**Location:** scripts/zotero.py:40

**Description:** Pattern detected: import urllib.request

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/zotero.py:46

**Description:** Pattern detected: os.environ.get("ZOTERO_API_KEY

#### [MEDIUM] Undeclared network usage

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** TOOL_ABUSE_UNDECLARED_NETWORK

**Description:** Skill code uses network libraries but doesn't declare network requirement

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** SKILL.md:151

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: fetch-pdfs --upload

#### [MEDIUM] TOOL CHAINING ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** tool_chaining_abuse
**Rule ID:** YARA_tool_chaining_abuse
**Location:** scripts/zotero.py:1051

**Description:** Detects suspicious tool chaining patterns that could lead to data exfiltration: Get upload

#### [MEDIUM] Environment variable harvesting detected

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_ENV_VAR_HARVESTING
**Location:** skills/clawhub-zotero/scripts/zotero.py

**Description:** Script iterates through environment variables in skills/clawhub-zotero/scripts/zotero.py

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
