# Skill Scanner

An exploration project using automated security scanning of AI agent skills and plugins across public skill directories.

AI agent skills, installable packages that extend what coding assistants and AI agents can do, are a growing attack surface. Skills can contain prompt injection, data exfiltration, command injection, and other vulnerabilities, whether introduced intentionally or by accident. This project aims to systematically scan popular skills and publish the results.

## Status

This is early-stage and evolving. The current implementation:

- **Scanner:** [Cisco AI Defense skill-scanner](https://github.com/cisco-ai-defense/skill-scanner) (static + behavioral + trigger analysis)
- **Target directory:** [skills.sh](https://skills.sh/) (top skills by install count)
- **Coverage:** 10 skills scanned so far

This could be expanded along both axes -- adding more scanners and targeting more skill directories.

- Additional scanners (custom rules, alternative tools)
- Additional skill directories (e.g., [CHub](https://clawhub.ai/), others as they emerge)
- Broader coverage of existing directories
- Automation for continuous scanning

## Scan Results

Results are in the [`results/`](results/) directory. Each scanned skill has a JSON file (machine-readable) and a Markdown file (human-readable). The [summary report](results/summary-report.md) consolidates all findings.

Latest scan highlights (10 skills from skills.sh):

- 5 skills clean, 5 with findings
- 1 skill flagged unsafe (command injection + tool permission issues)
- Most common finding: missing license metadata

## Project Structure

```
results/
  summary-report.md           # Consolidated findings across all skills
  <skill-name>-scan.json      # Raw scan output per skill
  <skill-name>-scan.md        # Readable scan report per skill
```

Cloned skill repositories are kept in `skills/` locally but excluded from version control via `.gitignore`.

## Running Scans

```bash
# Install the Cisco scanner
pip install cisco-ai-skill-scanner

# Clone a skill
git clone https://github.com/<owner>/<repo> skills/<skill-name>

# Scan it
skill-scanner scan skills/<skill-name> --output-format json --output results/<skill-name>-scan.json
skill-scanner scan skills/<skill-name> --output-format markdown --output results/<skill-name>-scan.md
```

Requires Python 3.10+.

## Known Limitations

- Only static analysis so far -- no runtime verification
- LLM-based semantic analysis unavailable without API keys
- Limited to skills with public source repos
- Scanner coverage depends on the rule sets of the underlying tools

## Links

- [Cisco AI Defense skill-scanner](https://github.com/cisco-ai-defense/skill-scanner)
- [skills.sh](https://skills.sh/)
- 
