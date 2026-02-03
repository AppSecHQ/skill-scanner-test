# Agent Skill Security Scan Report

**Skill:** veo3-video-gen
**Directory:** ./skills/clawhub-veo3-video-gen
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 2.16s
**Timestamp:** 2026-02-03T15:55:23.359420

## Summary

- **Total Findings:** 5
- **Critical:** 1
- **High:** 0
- **Medium:** 3
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Shell command execution with string formatting (potential injection)

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** COMMAND_INJECTION_OS_SYSTEM
**Location:** scripts/generate_video.py:49

**Description:** Pattern detected: subprocess.run(["bash", "-lc", f"command -v {shlex.quote(name)}

### MEDIUM Severity

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/generate_video.py:45

**Description:** Pattern detected: os.environ.get("GEMINI_API_KEY

#### [MEDIUM] AUTONOMY ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** autonomy_abuse
**Rule ID:** YARA_autonomy_abuse
**Location:** scripts/generate_video.py:117

**Description:** Detects unbounded autonomy patterns that could lead to runaway behavior: keep trying

#### [MEDIUM] Environment variable harvesting detected

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_ENV_VAR_HARVESTING
**Location:** skills/clawhub-veo3-video-gen/scripts/generate_video.py

**Description:** Script iterates through environment variables in skills/clawhub-veo3-video-gen/scripts/generate_video.py

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
