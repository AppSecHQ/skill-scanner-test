# Agent Skill Security Scan Report

**Skill:** hugging-face-datasets
**Directory:** ./skills/huggingface-skills/skills/hugging-face-datasets
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 4.12s
**Timestamp:** 2026-02-03T14:18:20.098069

## Summary

- **Total Findings:** 77
- **Critical:** 27
- **High:** 1
- **Medium:** 48
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] SQL query with string formatting (SQL injection risk)

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** SQL_INJECTION_STRING_FORMAT
**Location:** scripts/sql_manager.py:262

**Description:** Pattern detected: f"SELECT * FROM '{hf_path}' USING SAMPLE {n} (RESERVOIR, {seed}

#### [CRITICAL] SQL query with string formatting (SQL injection risk)

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** SQL_INJECTION_STRING_FORMAT
**Location:** scripts/sql_manager.py:264

**Description:** Pattern detected: f"SELECT * FROM '{hf_path}' USING SAMPLE {n}

#### [CRITICAL] SQL query with string formatting (SQL injection risk)

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** SQL_INJECTION_STRING_FORMAT
**Location:** scripts/sql_manager.py:285

**Description:** Pattern detected: f"SELECT COUNT(*) FROM '{hf_path}

#### [CRITICAL] SQL query with string formatting (SQL injection risk)

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** SQL_INJECTION_STRING_FORMAT
**Location:** scripts/sql_manager.py:287

**Description:** Pattern detected: f" WHERE {where}

#### [CRITICAL] SQL query with string formatting (SQL injection risk)

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** SQL_INJECTION_STRING_FORMAT
**Location:** scripts/sql_manager.py:310

**Description:** Pattern detected: f"SELECT DISTINCT {column} FROM '{hf_path}' LIMIT {limit}

#### [CRITICAL] SQL query with string formatting (SQL injection risk)

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** SQL_INJECTION_STRING_FORMAT
**Location:** scripts/sql_manager.py:383

**Description:** Pattern detected: f"SELECT {select}", f"FROM '{hf_path}

#### [CRITICAL] SQL query with string formatting (SQL injection risk)

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** SQL_INJECTION_STRING_FORMAT
**Location:** scripts/sql_manager.py:386

**Description:** Pattern detected: f"WHERE {where}

#### [CRITICAL] SQL query with string formatting (SQL injection risk)

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** SQL_INJECTION_STRING_FORMAT
**Location:** scripts/sql_manager.py:471

**Description:** Pattern detected: f"SELECT * FROM '{hf_path}

#### [CRITICAL] SQL query with string formatting (SQL injection risk)

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** SQL_INJECTION_STRING_FORMAT
**Location:** scripts/sql_manager.py:781

**Description:** Pattern detected: f" WHERE {args.where}

#### [CRITICAL] SQL query with string formatting (SQL injection risk)

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** SQL_INJECTION_STRING_FORMAT
**Location:** sql_manager.py:262

**Description:** Pattern detected: f"SELECT * FROM '{hf_path}' USING SAMPLE {n} (RESERVOIR, {seed}

#### [CRITICAL] SQL query with string formatting (SQL injection risk)

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** SQL_INJECTION_STRING_FORMAT
**Location:** sql_manager.py:264

**Description:** Pattern detected: f"SELECT * FROM '{hf_path}' USING SAMPLE {n}

#### [CRITICAL] SQL query with string formatting (SQL injection risk)

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** SQL_INJECTION_STRING_FORMAT
**Location:** sql_manager.py:285

**Description:** Pattern detected: f"SELECT COUNT(*) FROM '{hf_path}

#### [CRITICAL] SQL query with string formatting (SQL injection risk)

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** SQL_INJECTION_STRING_FORMAT
**Location:** sql_manager.py:287

**Description:** Pattern detected: f" WHERE {where}

#### [CRITICAL] SQL query with string formatting (SQL injection risk)

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** SQL_INJECTION_STRING_FORMAT
**Location:** sql_manager.py:310

**Description:** Pattern detected: f"SELECT DISTINCT {column} FROM '{hf_path}' LIMIT {limit}

#### [CRITICAL] SQL query with string formatting (SQL injection risk)

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** SQL_INJECTION_STRING_FORMAT
**Location:** sql_manager.py:383

**Description:** Pattern detected: f"SELECT {select}", f"FROM '{hf_path}

#### [CRITICAL] SQL query with string formatting (SQL injection risk)

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** SQL_INJECTION_STRING_FORMAT
**Location:** sql_manager.py:386

**Description:** Pattern detected: f"WHERE {where}

#### [CRITICAL] SQL query with string formatting (SQL injection risk)

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** SQL_INJECTION_STRING_FORMAT
**Location:** sql_manager.py:471

**Description:** Pattern detected: f"SELECT * FROM '{hf_path}

#### [CRITICAL] SQL query with string formatting (SQL injection risk)

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** SQL_INJECTION_STRING_FORMAT
**Location:** sql_manager.py:781

**Description:** Pattern detected: f" WHERE {args.where}

#### [CRITICAL] SQL query with string formatting (SQL injection risk)

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** SQL_INJECTION_STRING_FORMAT
**Location:** scripts/sql_manager.py:262

**Description:** Pattern detected: f"SELECT * FROM '{hf_path}' USING SAMPLE {n} (RESERVOIR, {seed}

#### [CRITICAL] SQL query with string formatting (SQL injection risk)

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** SQL_INJECTION_STRING_FORMAT
**Location:** scripts/sql_manager.py:264

**Description:** Pattern detected: f"SELECT * FROM '{hf_path}' USING SAMPLE {n}

#### [CRITICAL] SQL query with string formatting (SQL injection risk)

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** SQL_INJECTION_STRING_FORMAT
**Location:** scripts/sql_manager.py:285

**Description:** Pattern detected: f"SELECT COUNT(*) FROM '{hf_path}

#### [CRITICAL] SQL query with string formatting (SQL injection risk)

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** SQL_INJECTION_STRING_FORMAT
**Location:** scripts/sql_manager.py:287

**Description:** Pattern detected: f" WHERE {where}

#### [CRITICAL] SQL query with string formatting (SQL injection risk)

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** SQL_INJECTION_STRING_FORMAT
**Location:** scripts/sql_manager.py:310

**Description:** Pattern detected: f"SELECT DISTINCT {column} FROM '{hf_path}' LIMIT {limit}

#### [CRITICAL] SQL query with string formatting (SQL injection risk)

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** SQL_INJECTION_STRING_FORMAT
**Location:** scripts/sql_manager.py:383

**Description:** Pattern detected: f"SELECT {select}", f"FROM '{hf_path}

#### [CRITICAL] SQL query with string formatting (SQL injection risk)

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** SQL_INJECTION_STRING_FORMAT
**Location:** scripts/sql_manager.py:386

**Description:** Pattern detected: f"WHERE {where}

#### [CRITICAL] SQL query with string formatting (SQL injection risk)

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** SQL_INJECTION_STRING_FORMAT
**Location:** scripts/sql_manager.py:471

**Description:** Pattern detected: f"SELECT * FROM '{hf_path}

#### [CRITICAL] SQL query with string formatting (SQL injection risk)

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** SQL_INJECTION_STRING_FORMAT
**Location:** scripts/sql_manager.py:781

**Description:** Pattern detected: f" WHERE {args.where}

### HIGH Severity

#### [HIGH] Suspicious URL detected: https://huggingface.co/datasets/

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/huggingface-skills/skills/hugging-face-datasets/scripts/sql_manager.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

### MEDIUM Severity

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/sql_manager.py:51

**Description:** Pattern detected: os.environ.get("HF_TOKEN

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/dataset_manager.py:35

**Description:** Pattern detected: os.environ.get("HF_TOKEN

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** sql_manager.py:51

**Description:** Pattern detected: os.environ.get("HF_TOKEN

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/dataset_manager.py:35

**Description:** Pattern detected: os.environ.get("HF_TOKEN

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/sql_manager.py:51

**Description:** Pattern detected: os.environ.get("HF_TOKEN

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:13

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:54

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:73

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:78

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:81

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:84

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:116

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:119

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:122

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:128

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:133

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:144

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:151

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:162

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:169

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:179

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:185

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:191

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:200

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:309

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:312

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:318

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:323

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:425

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:429

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:433

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:441

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:446

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:452

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:455

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:458

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:466

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:482

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:483

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:486

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:496

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:505

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:514

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:523

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:532

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:533

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] Environment variable harvesting detected

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_ENV_VAR_HARVESTING
**Location:** skills/huggingface-skills/skills/hugging-face-datasets/scripts/sql_manager.py

**Description:** Script iterates through environment variables in skills/huggingface-skills/skills/hugging-face-datasets/scripts/sql_manager.py

#### [MEDIUM] Environment variable harvesting detected

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_ENV_VAR_HARVESTING
**Location:** skills/huggingface-skills/skills/hugging-face-datasets/scripts/dataset_manager.py

**Description:** Script iterates through environment variables in skills/huggingface-skills/skills/hugging-face-datasets/scripts/dataset_manager.py

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
