# Agent Skill Security Scan Report

**Skill:** docx
**Directory:** ./skills/clawhub-docx
**Status:** [OK] SAFE
**Max Severity:** MEDIUM
**Scan Duration:** 44.68s
**Timestamp:** 2026-02-01T16:45:09.772847

## Summary

- **Total Findings:** 3
- **Critical:** 0
- **High:** 0
- **Medium:** 3
- **Low:** 0
- **Info:** 0

## Findings

### MEDIUM Severity

#### [MEDIUM] Command Injection Risk - Subprocess Execution with User-Controlled Paths

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** LLM_COMMAND_INJECTION
**Location:** ooxml/scripts/pack.py

**Description:** The pack.py script uses subprocess.run() to execute external commands (xmllint) with file paths that could be influenced by user input. While the script uses shell=False which provides some protection, the validation logic can be bypassed with --force flag, and file paths are not sanitized before being passed to subprocess commands. This creates potential for command injection if an attacker can control directory or file names.

#### [MEDIUM] Potential Data Exposure - Unpacking Office Files Without Validation

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** LLM_DATA_EXFILTRATION
**Location:** ooxml/scripts/unpack.py

**Description:** The unpack.py script extracts ZIP archives (Office files) without validating their contents, size limits, or structure. This could lead to zip bomb attacks, path traversal via malicious filenames in the archive, or exposure of sensitive data if a malicious Office file is processed. The script uses zipfile.ZipFile().extractall() which is known to be vulnerable to path traversal attacks.

#### [MEDIUM] Resource Exhaustion Risk - Unbounded XML Processing

**Severity:** MEDIUM
**Category:** resource_abuse
**Rule ID:** LLM_RESOURCE_ABUSE

**Description:** Multiple scripts process XML files without size limits or resource constraints. The validation scripts (docx.py, pptx.py, base.py) parse XML using lxml.etree without memory limits, and the utilities.py XMLEditor loads entire XML files into memory. Processing maliciously crafted or extremely large XML files could cause memory exhaustion or CPU exhaustion (XML entity expansion attacks, deeply nested structures).

## Analyzers

The following analyzers were used:

- static_analyzer
- behavioral_analyzer
- llm_analyzer
- trigger_analyzer
- meta_analyzer
