# Agent Skill Security Scan Report

**Skill:** hugging-face-evaluation
**Directory:** /workspace/skills/huggingface-skills/skills/hugging-face-evaluation
**Status:** [FAIL] ISSUES FOUND
**Max Severity:** CRITICAL
**Scan Duration:** 9.32s
**Timestamp:** 2026-02-06T07:48:00.580719

## Summary

- **Total Findings:** 113
- **Critical:** 8
- **High:** 7
- **Medium:** 97
- **Low:** 1
- **Info:** 0

## Findings

### CRITICAL Severity

#### [CRITICAL] Environment variable access with network calls detected

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_ENV_VAR_EXFILTRATION
**Location:** skills/huggingface-skills/skills/hugging-face-evaluation/examples/artificial_analysis_to_hub.py

**Description:** Script accesses environment variables and makes network calls in skills/huggingface-skills/skills/hugging-face-evaluation/examples/artificial_analysis_to_hub.py

#### [CRITICAL] Environment variable access with network calls detected

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_ENV_VAR_EXFILTRATION
**Location:** skills/huggingface-skills/skills/hugging-face-evaluation/scripts/evaluation_manager.py

**Description:** Script accesses environment variables and makes network calls in skills/huggingface-skills/skills/hugging-face-evaluation/scripts/evaluation_manager.py

#### [CRITICAL] eval/exec combined with subprocess detected

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** BEHAVIOR_EVAL_SUBPROCESS
**Location:** skills/huggingface-skills/skills/hugging-face-evaluation/scripts/run_eval_job.py

**Description:** Dangerous combination of code execution and system commands in skills/huggingface-skills/skills/hugging-face-evaluation/scripts/run_eval_job.py

#### [CRITICAL] eval/exec combined with subprocess detected

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** BEHAVIOR_EVAL_SUBPROCESS
**Location:** skills/huggingface-skills/skills/hugging-face-evaluation/scripts/inspect_eval_uv.py

**Description:** Dangerous combination of code execution and system commands in skills/huggingface-skills/skills/hugging-face-evaluation/scripts/inspect_eval_uv.py

#### [CRITICAL] eval/exec combined with subprocess detected

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** BEHAVIOR_EVAL_SUBPROCESS
**Location:** skills/huggingface-skills/skills/hugging-face-evaluation/scripts/lighteval_vllm_uv.py

**Description:** Dangerous combination of code execution and system commands in skills/huggingface-skills/skills/hugging-face-evaluation/scripts/lighteval_vllm_uv.py

#### [CRITICAL] eval/exec combined with subprocess detected

**Severity:** CRITICAL
**Category:** command_injection
**Rule ID:** BEHAVIOR_EVAL_SUBPROCESS
**Location:** skills/huggingface-skills/skills/hugging-face-evaluation/scripts/run_vllm_eval_job.py

**Description:** Dangerous combination of code execution and system commands in skills/huggingface-skills/skills/hugging-face-evaluation/scripts/run_vllm_eval_job.py

#### [CRITICAL] Cross-file exfiltration chain: 7 files

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_CROSSFILE_EXFILTRATION_CHAIN

**Description:** Multi-file exfiltration chain detected: examples/artificial_analysis_to_hub.py, scripts/evaluation_manager.py, scripts/run_eval_job.py, scripts/inspect_vllm_uv.py, scripts/inspect_eval_uv.py, scripts/lighteval_vllm_uv.py, scripts/run_vllm_eval_job.py collect data → encode → examples/artificial_analysis_to_hub.py, scripts/evaluation_manager.py transmit to network

#### [CRITICAL] Cross-file env var exfiltration: 7 files

**Severity:** CRITICAL
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_CROSSFILE_ENV_VAR_EXFILTRATION

**Description:** Environment variable access with network calls in examples/artificial_analysis_to_hub.py, scripts/evaluation_manager.py, scripts/run_eval_job.py, scripts/inspect_vllm_uv.py, scripts/inspect_eval_uv.py, scripts/lighteval_vllm_uv.py, scripts/run_vllm_eval_job.py

### HIGH Severity

#### [HIGH] Suspicious URL detected: https://artificialanalysis.ai

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/huggingface-skills/skills/hugging-face-evaluation/examples/artificial_analysis_to_hub.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

#### [HIGH] Suspicious URL detected: https://artificialanalysis.ai/api/v2/data/llms/models

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/huggingface-skills/skills/hugging-face-evaluation/examples/artificial_analysis_to_hub.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

#### [HIGH] Suspicious URL detected: https://huggingface.co/

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/huggingface-skills/skills/hugging-face-evaluation/scripts/evaluation_manager.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

#### [HIGH] Suspicious URL detected: https://huggingface.co/api/models/

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/huggingface-skills/skills/hugging-face-evaluation/scripts/evaluation_manager.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

#### [HIGH] Suspicious URL detected: https://artificialanalysis.ai/api/v2/data/llms/models

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/huggingface-skills/skills/hugging-face-evaluation/scripts/evaluation_manager.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

#### [HIGH] Suspicious URL detected: https://artificialanalysis.ai

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/huggingface-skills/skills/hugging-face-evaluation/scripts/evaluation_manager.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

#### [HIGH] Suspicious URL detected: https://huggingface.co/test/model

**Severity:** HIGH
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_SUSPICIOUS_URL
**Location:** skills/huggingface-skills/skills/hugging-face-evaluation/scripts/test_extraction.py

**Description:** Script contains suspicious URL that may be used for data exfiltration

### MEDIUM Severity

#### [MEDIUM] HTTP client library imports that enable external communication

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_NETWORK_REQUESTS
**Location:** examples/artificial_analysis_to_hub.py:36

**Description:** Pattern detected: import requests

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** examples/artificial_analysis_to_hub.py:42

**Description:** Pattern detected: os.getenv("AA_API_KEY

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** examples/artificial_analysis_to_hub.py:43

**Description:** Pattern detected: os.getenv("HF_TOKEN

#### [MEDIUM] HTTP client library imports that enable external communication

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_NETWORK_REQUESTS
**Location:** scripts/evaluation_manager.py:62

**Description:** Pattern detected: import requests

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/evaluation_manager.py:515

**Description:** Pattern detected: os.getenv("HF_TOKEN

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/evaluation_manager.py:725

**Description:** Pattern detected: os.getenv("HF_TOKEN

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/evaluation_manager.py:865

**Description:** Pattern detected: os.getenv("AA_API_KEY

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/evaluation_manager.py:994

**Description:** Pattern detected: os.getenv("HF_TOKEN

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/evaluation_manager.py:1057

**Description:** Pattern detected: os.getenv("HF_TOKEN

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/evaluation_manager.py:1105

**Description:** Pattern detected: os.getenv("HF_TOKEN

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/run_eval_job.py:42

**Description:** Pattern detected: os.getenv("HF_TOKEN

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/inspect_vllm_uv.py:43

**Description:** Pattern detected: os.getenv("HF_TOKEN

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/inspect_eval_uv.py:61

**Description:** Pattern detected: os.getenv("HF_TOKEN

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/lighteval_vllm_uv.py:39

**Description:** Pattern detected: os.getenv("HF_TOKEN

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/run_vllm_eval_job.py:91

**Description:** Pattern detected: os.getenv("HF_TOKEN

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/run_vllm_eval_job.py:147

**Description:** Pattern detected: os.getenv("HF_TOKEN

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

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/lighteval_vllm_uv.py:39

**Description:** Pattern detected: os.getenv("HF_TOKEN

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/inspect_vllm_uv.py:43

**Description:** Pattern detected: os.getenv("HF_TOKEN

#### [MEDIUM] HTTP client library imports that enable external communication

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_NETWORK_REQUESTS
**Location:** scripts/evaluation_manager.py:62

**Description:** Pattern detected: import requests

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/evaluation_manager.py:515

**Description:** Pattern detected: os.getenv("HF_TOKEN

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/evaluation_manager.py:725

**Description:** Pattern detected: os.getenv("HF_TOKEN

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/evaluation_manager.py:865

**Description:** Pattern detected: os.getenv("AA_API_KEY

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/evaluation_manager.py:994

**Description:** Pattern detected: os.getenv("HF_TOKEN

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/evaluation_manager.py:1057

**Description:** Pattern detected: os.getenv("HF_TOKEN

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/evaluation_manager.py:1105

**Description:** Pattern detected: os.getenv("HF_TOKEN

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/inspect_eval_uv.py:61

**Description:** Pattern detected: os.getenv("HF_TOKEN

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/run_vllm_eval_job.py:91

**Description:** Pattern detected: os.getenv("HF_TOKEN

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/run_vllm_eval_job.py:147

**Description:** Pattern detected: os.getenv("HF_TOKEN

#### [MEDIUM] Reading environment variables that may contain secrets

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** DATA_EXFIL_ENV_VARS
**Location:** scripts/run_eval_job.py:42

**Description:** Pattern detected: os.getenv("HF_TOKEN

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:50

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:71

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:72

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
**Location:** SKILL.md:115

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:127

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:152

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:155

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
**Location:** SKILL.md:167

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:184

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:197

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:205

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:238

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:265

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:270

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:275

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:281

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:289

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:327

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:332

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:338

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:346

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:368

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:374

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:382

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:401

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:402

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:407

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:412

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:424

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
**Location:** SKILL.md:434

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:439

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:445

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
**Location:** SKILL.md:464

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:471

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:478

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:557

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:565

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:569

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:582

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** SKILL.md:586

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] CODE EXECUTION detected by YARA

**Severity:** MEDIUM
**Category:** command_injection
**Rule ID:** YARA_code_execution
**Location:** SKILL.md:636

**Description:** Detects dangerous code execution patterns in agent skills (Python/Bash): subprocess.run(

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** scripts/evaluation_manager.py:556

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** scripts/evaluation_manager.py:775

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** scripts/evaluation_manager.py:1157

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** scripts/evaluation_manager.py:1165

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** scripts/evaluation_manager.py:1167

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** scripts/evaluation_manager.py:1169

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** scripts/evaluation_manager.py:1171

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** scripts/evaluation_manager.py:1194

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** scripts/evaluation_manager.py:1195

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** scripts/evaluation_manager.py:1196

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** scripts/evaluation_manager.py:1197

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** scripts/evaluation_manager.py:1228

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** scripts/evaluation_manager.py:1229

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] TRANSITIVE TRUST ABUSE detected by YARA

**Severity:** MEDIUM
**Category:** transitive_trust_abuse
**Rule ID:** YARA_transitive_trust_abuse
**Location:** scripts/evaluation_manager.py:1284

**Description:** Detects skills that delegate trust to untrusted external content: run scripts

#### [MEDIUM] Environment variable harvesting detected

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_ENV_VAR_HARVESTING
**Location:** skills/huggingface-skills/skills/hugging-face-evaluation/examples/artificial_analysis_to_hub.py

**Description:** Script iterates through environment variables in skills/huggingface-skills/skills/hugging-face-evaluation/examples/artificial_analysis_to_hub.py

#### [MEDIUM] Environment variable harvesting detected

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_ENV_VAR_HARVESTING
**Location:** skills/huggingface-skills/skills/hugging-face-evaluation/scripts/evaluation_manager.py

**Description:** Script iterates through environment variables in skills/huggingface-skills/skills/hugging-face-evaluation/scripts/evaluation_manager.py

#### [MEDIUM] Environment variable harvesting detected

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_ENV_VAR_HARVESTING
**Location:** skills/huggingface-skills/skills/hugging-face-evaluation/scripts/run_eval_job.py

**Description:** Script iterates through environment variables in skills/huggingface-skills/skills/hugging-face-evaluation/scripts/run_eval_job.py

#### [MEDIUM] Environment variable harvesting detected

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_ENV_VAR_HARVESTING
**Location:** skills/huggingface-skills/skills/hugging-face-evaluation/scripts/inspect_vllm_uv.py

**Description:** Script iterates through environment variables in skills/huggingface-skills/skills/hugging-face-evaluation/scripts/inspect_vllm_uv.py

#### [MEDIUM] Environment variable harvesting detected

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_ENV_VAR_HARVESTING
**Location:** skills/huggingface-skills/skills/hugging-face-evaluation/scripts/inspect_eval_uv.py

**Description:** Script iterates through environment variables in skills/huggingface-skills/skills/hugging-face-evaluation/scripts/inspect_eval_uv.py

#### [MEDIUM] Environment variable harvesting detected

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_ENV_VAR_HARVESTING
**Location:** skills/huggingface-skills/skills/hugging-face-evaluation/scripts/lighteval_vllm_uv.py

**Description:** Script iterates through environment variables in skills/huggingface-skills/skills/hugging-face-evaluation/scripts/lighteval_vllm_uv.py

#### [MEDIUM] Environment variable harvesting detected

**Severity:** MEDIUM
**Category:** data_exfiltration
**Rule ID:** BEHAVIOR_ENV_VAR_HARVESTING
**Location:** skills/huggingface-skills/skills/hugging-face-evaluation/scripts/run_vllm_eval_job.py

**Description:** Script iterates through environment variables in skills/huggingface-skills/skills/hugging-face-evaluation/scripts/run_vllm_eval_job.py

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
