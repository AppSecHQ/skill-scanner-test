# Agent Skill Security Scan Report

**Skill:** hugging-face-jobs
**Directory:** /workspace/skills/huggingface-skills/skills/hugging-face-jobs
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 3.06s
**Timestamp:** 2026-02-06T07:48:10.239612

## Summary

- **Total Findings:** 7
- **Critical:** 0
- **High:** 1
- **Medium:** 6
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Suspicious URL detected: https://huggingface.co/datasets/

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/huggingface-skills/skills/hugging-face-jobs/scripts/finepdfs-stats.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

### MEDIUM Severity

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/generate-responses.py:228

**Description:** Pattern detected: os.environ.get("HF_TOKEN

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/cot-self-instruct.py:572

**Description:** Pattern detected: os.environ.get("HF_TOKEN

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/finepdfs-stats.py:470

**Description:** Pattern detected: os.environ.get("HF_TOKEN

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:1024

**Description:** Detects skills that delegate trust to untrusted external content: run script

#### [MEDIUM] Environment variable harvesting detected

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_ENV_VAR_HARVESTING
**Location:** skills/huggingface-skills/skills/hugging-face-jobs/scripts/cot-self-instruct.py

**Description:** Script iterates through environment variables in skills/huggingface-skills/skills/hugging-face-jobs/scripts/cot-self-instruct.py

#### [MEDIUM] Environment variable harvesting detected

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_ENV_VAR_HARVESTING
**Location:** skills/huggingface-skills/skills/hugging-face-jobs/scripts/finepdfs-stats.py

**Description:** Script iterates through environment variables in skills/huggingface-skills/skills/hugging-face-jobs/scripts/finepdfs-stats.py

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
