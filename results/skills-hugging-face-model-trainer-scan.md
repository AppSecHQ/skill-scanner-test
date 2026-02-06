# Agent Skill Security Scan Report

**Skill:** hugging-face-model-trainer
**Directory:** /workspace/skills/huggingface-skills/skills/hugging-face-model-trainer
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 3.58s
**Timestamp:** 2026-02-06T07:48:20.672203

## Summary

- **Total Findings:** 16
- **Critical:** 0
- **High:** 2
- **Medium:** 14
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Suspicious URL detected: https://datasets-server.huggingface.co/splits?dataset=

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/huggingface-skills/skills/hugging-face-model-trainer/scripts/dataset_inspector.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

#### [HIGH] Suspicious URL detected: https://datasets-server.huggingface.co/rows?dataset=

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/huggingface-skills/skills/hugging-face-model-trainer/scripts/dataset_inspector.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

### MEDIUM Severity

#### [MEDIUM] Attempting to install system packages with elevated privileges

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** TOOL_ABUSE_SYSTEM_PACKAGE_INSTALL
**Location:** scripts/convert_to_gguf.py:27

**Description:** Pattern detected: sudo apt-get install

#### [MEDIUM] Attempting to install system packages with elevated privileges

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** TOOL_ABUSE_SYSTEM_PACKAGE_INSTALL
**Location:** scripts/convert_to_gguf.py:28

**Description:** Pattern detected: sudo yum install

#### [MEDIUM] Attempting to install system packages with elevated privileges

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** TOOL_ABUSE_SYSTEM_PACKAGE_INSTALL
**Location:** scripts/convert_to_gguf.py:57

**Description:** Pattern detected: sudo apt-get install

#### [MEDIUM] Attempting to install system packages with elevated privileges

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** TOOL_ABUSE_SYSTEM_PACKAGE_INSTALL
**Location:** scripts/convert_to_gguf.py:58

**Description:** Pattern detected: sudo yum install

#### [MEDIUM] Attempting to install system packages with elevated privileges

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** TOOL_ABUSE_SYSTEM_PACKAGE_INSTALL
**Location:** scripts/convert_to_gguf.py:68

**Description:** Pattern detected: sudo apt-get install

#### [MEDIUM] Attempting to install system packages with elevated privileges

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** TOOL_ABUSE_SYSTEM_PACKAGE_INSTALL
**Location:** scripts/convert_to_gguf.py:69

**Description:** Pattern detected: sudo yum install

#### [MEDIUM] HTTP client library imports that enable external communication

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_NETWORK_REQUESTS
**Location:** scripts/dataset_inspector.py:24

**Description:** Pattern detected: import urllib.request

#### [MEDIUM] Undeclared network usage

**Severity:** MEDIUM
**Category:** unauthorized_tool_use
**Rule ID:** TOOL_ABUSE_UNDECLARED_NETWORK

**Description:** Skill code uses network libraries but doesn't declare network requirement

#### [MEDIUM] Potential description-behavior mismatch

**Severity:** MEDIUM
**Category:** social_engineering
**Rule ID:** SOCIAL_ENG_MISLEADING_DESC
**Location:** SKILL.md

**Description:** Skill performs actions not reflected in its description

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:47

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:416

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** scripts/convert_to_gguf.py:63

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): subprocess.run(

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** scripts/convert_to_gguf.py:64

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): subprocess.run(

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** scripts/convert_to_gguf.py:81

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): subprocess.run(

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
