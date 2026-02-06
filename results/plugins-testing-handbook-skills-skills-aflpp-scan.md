# Agent Skill Security Scan Report

**Skill:** aflpp
**Directory:** /workspace/skills/trailofbits-skills/plugins/testing-handbook-skills/skills/aflpp
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 59.59s
**Timestamp:** 2026-02-06T07:33:24.094615

## Summary

- **Total Findings:** 9
- **Critical:** 4
- **High:** 0
- **Medium:** 2
- **Low:** 3
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:495

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl -O 

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:538

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl -O 

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:546

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl -o 

#### [CRITICAL] INJECTION ATTACK detected by YARA

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** YARA_command_injection
**Location:** SKILL.md:547

**Description:** Detects command injection patterns in agent skills: shell operators, system commands, and network tools: curl -O 

### MEDIUM Severity

#### [MEDIUM] Arbitrary Command Execution via Wrapper Script

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The skill instructs users to create a wrapper script that executes arbitrary bash commands with 'bash -c "$*"' without any input validation or sanitization. This pattern allows command injection if the wrapper is called with untrusted input, as the shell will interpret special characters, command substitution, and other shell metacharacters.

#### [MEDIUM] Docker Container Execution Without Resource Limits

**Severity:** MEDIUM
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** SKILL.md

**Description:** The skill's Docker wrapper script runs AFL++ containers without specifying resource limits (CPU, memory, process limits). AFL++ is designed for intensive multi-core fuzzing which can consume significant system resources. Without proper resource constraints, a fuzzing campaign could exhaust system resources, leading to denial of service conditions on the host system.

### LOW Severity

#### [LOW] Skill does not specify a license

**Severity:** LOW
**Category:** policy_violation
**Rule ID:** MANIFEST_MISSING_LICENSE
**Location:** SKILL.md

**Description:** Skill manifest does not include a 'license' field. Specifying a license helps users understand usage terms.

#### [LOW] Missing Optional Metadata Fields

**Severity:** LOW
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill manifest is missing optional but recommended metadata fields: 'license', 'compatibility', and 'allowed-tools'. While these fields are not required, their absence makes it harder to assess the skill's intended usage constraints and compatibility requirements. The skill involves compiling and executing code, which would benefit from explicit tool declarations.

#### [LOW] Incomplete Wrapper Script in Documentation

**Severity:** LOW
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The SKILL.md instructions show a truncated wrapper script that ends abruptly without showing the complete Docker case statement or script termination. This incomplete documentation could lead users to create a malformed wrapper script that behaves unexpectedly or fails to handle all execution modes properly.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
