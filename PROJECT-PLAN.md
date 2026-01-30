# AI Agent Skills Security Scan Project

## Objective
Scan the top N most-installed AI agent skills from skills.sh using Cisco's skill-scanner tool to identify security vulnerabilities, prompt injection risks, and malicious patterns. Produce a summary report of findings.

## Background

This project responds to emerging research showing 25%+ of AI agent skills contain vulnerabilities, some intentionally malicious. The Cisco AI Defense team released an open-source scanner to detect these threats.

- **Scanner repo**: https://github.com/cisco-ai-defense/skill-scanner
- **Skills directory**: https://skills.sh/
- **Detection capabilities**: Prompt injection, data exfiltration, malicious code patterns

## Prerequisites
- Python 3.10+
- Git
- Internet access for cloning repos

## Approach 

- Perform an end-to-end test on 1 Skill, before moving on to each of the subsquent top skills. Get Confirmation from user before moving to the top 2 skill. 


## Phase 1: Environment Setup

1. Install the Cisco skill-scanner:
   ```bash
   pip install cisco-ai-skill-scanner
   ```

2. Verify installation:
   ```bash
   skill-scanner --help
   ```

3. Create a working directory:
   ```bash
   mkdir -p ~/skill-scanner-project/{skills,results}
   cd ~/skill-scanner-project
   ```



## Phase 2: Identify Top Skills

1. Visit https://skills.sh/ and extract the top skills by install count
2. For each skill, record:
   - Skill name
   - GitHub repo URL (format: github.com/<owner>/<repo>)
   - Install count
   - Brief description

3. Save this list to `skills/skill-inventory.md`

## Phase 3: Clone Skills

For each of the skills:
```bash
git clone https://github.com/<owner>/<repo> skills/<skill-name>
```

Note: Some skills may be in monorepos (e.g., vercel-labs/agent-skills contains multiple skills). Clone the repo once and scan the relevant subdirectories.

## Phase 4: Run Security Scans

For each skill directory, run:
```bash
skill-scanner scan skills/<skill-name> \
  --output-format json \
  --output results/<skill-name>-scan.json
```

Also generate a human-readable version:
```bash
skill-scanner scan skills/<skill-name> \
  --output-format markdown \
  --output results/<skill-name>-scan.md
```

If scanning a monorepo with multiple skills, use:
```bash
skill-scanner scan-all skills/<repo-name> \
  --output-format json \
  --output results/<repo-name>-all-scans.json
```

## Phase 5: Compile Results

Create a summary report `results/summary-report.md` containing:

### 1. Executive Summary
- Total skills scanned
- Total findings by severity (CRITICAL, HIGH, MEDIUM, LOW)
- Skills with no findings vs. skills with findings

### 2. Findings by Skill
For each skill with findings:
| Skill | Severity | Finding Type | Description |
|-------|----------|--------------|-------------|

### 3. Top Risks
List the top 5 most concerning findings across all skills with:
- Skill name and repo
- Finding details
- Potential impact
- Recommendation

### 4. Patterns Observed
Document any recurring vulnerability patterns across multiple skills, such as:
- Common prompt injection vectors
- Data exfiltration patterns
- Unsafe code execution patterns

### 5. Methodology Notes
- Scanner version used
- Any skills that failed to scan (and why)
- Limitations observed

## Deliverables

1. `skills/skill-inventory.md` - List of skills with metadata
2. `results/<skill-name>-scan.json` - Raw scan results for each skill
3. `results/<skill-name>-scan.md` - Readable scan results for each skill
4. `results/summary-report.md` - Consolidated findings report

## Notes

- If the scanner requires API keys for LLM-based analysis, run with static analysis only using available flags
- Document any rate limiting or access issues encountered
- If a skill repo is private or unavailable, note it and proceed with others
- Focus on actionable findings - the meta-analyzer should filter false positives
