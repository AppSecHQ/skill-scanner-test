# Agent Skill Security Scan Report

**Skill:** tokenguard
**Directory:** ./skills/clawhub-tokenguard
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 2.33s
**Timestamp:** 2026-02-02T03:05:34.990456

## Summary

- **Total Findings:** 7
- **Critical:** 0
- **High:** 1
- **Medium:** 6
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Accessing sensitive system or credential files

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_SENSITIVE_FILES
**Location:** scripts/tokenguard.py:25

**Description:** Pattern detected: Path(os.env

### MEDIUM Severity

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/tokenguard.py:25

**Description:** Pattern detected: os.environ.get("TOKEN

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/tokenguard.py:31

**Description:** Pattern detected: os.environ.get("TOKEN

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/tokenguard.py:32

**Description:** Pattern detected: os.environ.get("TOKEN

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** SKILL.md:116

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): subprocess.run(

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** SKILL.md:125

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): subprocess.run(

#### [MEDIUM] Environment variable harvesting detected

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_ENV_VAR_HARVESTING
**Location:** skills/clawhub-tokenguard/scripts/tokenguard.py

**Description:** Script iterates through environment variables in skills/clawhub-tokenguard/scripts/tokenguard.py

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
