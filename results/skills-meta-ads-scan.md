# Agent Skill Security Scan Report

**Skill:** meta-ads
**Directory:** /home/runner/work/skill-scanner-test/skill-scanner-test/scripts/../skills/hoodini-ai-agents-skills/skills/meta-ads
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 17.84s
**Timestamp:** 2026-05-09T01:44:26.549690+00:00

## Summary

- **Total Findings:** 13
- **Critical:** 5
- **High:** 0
- **Medium:** 7
- **Low:** 0
- **Info:** 1

## Findings

### CRITICAL Severity

#### [CRITICAL] Cross-file env var exfiltration: 3 files

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_CROSSFILE_ENV_VAR_EXFILTRATION

**Description:** Environment variable access with network calls in scripts/exchange_token.py, scripts/meta_client.py

#### [CRITICAL] Cross-file exfiltration chain: 3 files

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_CROSSFILE_EXFILTRATION_CHAIN

**Description:** Multi-file exfiltration chain detected: scripts/exchange_token.py, scripts/meta_client.py collect data → encode → scripts/exchange_token.py, scripts/meta_client.py, scripts/create_campaign.py transmit to network

#### [CRITICAL] Environment variable access with network calls detected

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_ENV_VAR_EXFILTRATION
**Location:** ../skills/hoodini-ai-agents-skills/skills/meta-ads/scripts/exchange_token.py

**Description:** Script accesses environment variables and makes network calls in ../skills/hoodini-ai-agents-skills/skills/meta-ads/scripts/exchange_token.py

#### [CRITICAL] Environment variable access with network calls detected

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_ENV_VAR_EXFILTRATION
**Location:** ../skills/hoodini-ai-agents-skills/skills/meta-ads/scripts/meta_client.py

**Description:** Script accesses environment variables and makes network calls in ../skills/hoodini-ai-agents-skills/skills/meta-ads/scripts/meta_client.py

#### [CRITICAL] PROMPT INJECTION detected by YARA

**Severity:** CRITICAL
**Category:** prompt_injection
**Rule ID:** YARA_coercive_injection_generic
**Location:** scripts/exchange_token.py:76

**Description:** Detects coercive prompt injections in tool description fields: hidden input

### MEDIUM Severity

#### [MEDIUM] Undeclared network usage

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** TOOL_ABUSE_UNDECLARED_NETWORK
**Location:** ../skills/hoodini-ai-agents-skills/skills/meta-ads/SKILL.md

**Description:** Skill code uses network libraries but doesn't declare network requirement

#### [MEDIUM] Environment variable harvesting detected

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_ENV_VAR_HARVESTING
**Location:** ../skills/hoodini-ai-agents-skills/skills/meta-ads/scripts/exchange_token.py

**Description:** Script iterates through environment variables in ../skills/hoodini-ai-agents-skills/skills/meta-ads/scripts/exchange_token.py

#### [MEDIUM] Environment variable harvesting detected

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_ENV_VAR_HARVESTING
**Location:** ../skills/hoodini-ai-agents-skills/skills/meta-ads/scripts/meta_client.py

**Description:** Script iterates through environment variables in ../skills/hoodini-ai-agents-skills/skills/meta-ads/scripts/meta_client.py

#### [MEDIUM] Outbound network request primitives that can transmit data externally

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_NETWORK_REQUESTS
**Location:** scripts/create_campaign.py:108

**Description:** Pattern detected: requests.post(

#### [MEDIUM] Outbound network request primitives that can transmit data externally

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_NETWORK_REQUESTS
**Location:** scripts/exchange_token.py:47

**Description:** Pattern detected: requests.get(

#### [MEDIUM] Outbound network request primitives that can transmit data externally

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_NETWORK_REQUESTS
**Location:** scripts/meta_client.py:129

**Description:** Pattern detected: requests.request(

#### [MEDIUM] Outbound network request primitives that can transmit data externally

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_NETWORK_REQUESTS
**Location:** scripts/meta_client.py:189

**Description:** Pattern detected: requests.get(

### INFO Severity

#### [INFO] Skill does not specify a license

**Severity:** INFO
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

## Analyzers

The following analyzers were used:

- static_analyzer
- bytecode
- pipeline
- behavioral_analyzer
- trigger_analyzer
