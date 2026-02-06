# Agent Skill Security Scan Report

**Skill:** clawbridge
**Directory:** /workspace/skills/clawhub-clawbridge-skill-latest
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** HIGH
**Scan Duration:** 45.00s
**Timestamp:** 2026-02-05T21:52:53.377215

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 2
- **Medium:** 1
- **Low:** 0
- **Info:** 0

## Findings

### HIGH Severity

#### [HIGH] Arbitrary Command Execution via Unvalidated User Input

**Severity:** HIGH
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** SKILL.md

**Description:** The skill executes 'clawbridge run' with user-provided arguments (e.g., '--profile myprofile') without any input validation or sanitization. This allows command injection attacks where malicious users could inject arbitrary shell commands through the profile parameter or other arguments. For example, '/clawbridge --profile "myprofile; rm -rf /"' could execute destructive commands.

#### [HIGH] Execution of Untrusted Remote Code via Install Script

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** SKILL.md

**Description:** The skill's installation instructions direct users to execute a remote shell script directly from the internet using 'curl | bash' pattern ('curl -fsSL https://clawbridge.cloud/install | bash'). This is a critical security anti-pattern that executes arbitrary code without inspection. If the domain is compromised or performs a man-in-the-middle attack, malicious code would execute with the user's privileges. The metadata also includes this dangerous installation method as the 'recommended' approach.

### MEDIUM Severity

#### [MEDIUM] Unbounded External Process Execution

**Severity:** MEDIUM
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE
**Location:** SKILL.md

**Description:** The skill executes an external binary ('clawbridge run') with no documented timeouts, resource limits, or error handling. The runner performs 'discovery workflow' which could involve network calls, file operations, and API interactions. There are no safeguards against the process hanging indefinitely, consuming excessive resources, or entering infinite loops. This could lead to denial of service or resource exhaustion on the user's machine.

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
