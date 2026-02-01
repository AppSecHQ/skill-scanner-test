# Skill Scanner Test

An automated security scanning pipeline for AI agent skills and plugins in public skill directories.

AI agent skills -- installable packages that extend what coding assistants and AI agents can do -- are a growing attack surface. Skills can contain prompt injection, data exfiltration, command injection, and other vulnerabilities, whether introduced intentionally or by accident. This project systematically scans public skills using Cisco's open-source [skill-scanner](https://github.com/cisco-ai-defense/skill-scanner) and publishes the results.

## Status

This is early-stage and evolving. The current implementation:

- **Scanner:** [Cisco AI Defense skill-scanner](https://github.com/cisco-ai-defense/skill-scanner) (static + behavioral + trigger + LLM + meta-analysis)
- **Skill registries:** [skills.sh](https://skills.sh/) and [clawhub.ai](https://clawhub.ai/)
- **Coverage:** 86 skills scanned so far
- **Test suite:** 77 tests passing

This could be expanded along both axes -- adding more scanners and targeting more skill directories.

<!-- BEGIN SCAN RESULTS -->
## Scan Results

| Metric | Count |
|--------|-------|
| Total Skills Scanned | 86 |
| Safe Skills | 64 (74%) |
| Skills with Issues | 22 (26%) |
| Total Findings | 143 |

| Severity | Count |
|----------|-------|
| CRITICAL | 30 |
| HIGH | 42 |
| MEDIUM | 52 |
| LOW | 19 |

| Category | Count |
|----------|-------|
| data_exfiltration | 55 |
| social_engineering | 21 |
| command_injection | 20 |
| unauthorized_tool_use | 13 |
| policy_violation | 12 |
| prompt_injection | 10 |
| resource_abuse | 9 |
| tool_chaining_abuse | 2 |
| hardcoded_secrets | 1 |

- See [summary-report.md](results/summary-report.md) for detailed findings by skill, severity breakdowns, and top risks. Per-skill scan results (JSON + Markdown) are in the [`results/`](results/) directory.
<!-- END SCAN RESULTS -->

## Getting Started

Requires Python 3.10+ and Git.

```bash
git clone https://github.com/AppSecHQ/skill-scanner-test.git
cd skill-scanner-test
python -m venv .venv
source .venv/bin/activate
pip install -r scripts/requirements.txt
```

If you're in a container or environment where you don't need a venv, you can skip the venv steps and install directly with `pip install -r scripts/requirements.txt --break-system-packages`.

### Scan top skills from a registry

```bash
# Scan top 25 skills from skills.sh (default)
python scripts/scan-skills.py -n 25

# Scan top 10 from clawhub.ai
python scripts/scan-skills.py --source clawhub -n 10

# Scan skills 11-25 (pagination)
python scripts/scan-skills.py -n 15 --offset 10

# Enable LLM semantic analysis (requires SKILL_SCANNER_LLM_API_KEY)
python scripts/scan-skills.py -n 25 --use-llm

# Enable LLM + meta-analysis for false positive filtering
python scripts/scan-skills.py -n 25 --use-llm --enable-meta
```

### Scan a specific repo

```bash
# Scan a single GitHub repo
python scripts/scan-skills.py --repo owner/repo --repo-only

# Scan a repo alongside top skills
python scripts/scan-skills.py -n 10 --repo owner/repo
```

### Other options

```bash
# List skills without scanning
python scripts/scan-skills.py --list-only -n 25

# Generate report from existing results (skip fetch + scan)
python scripts/scan-skills.py --skip-scan -o results

# Custom report name
python scripts/scan-skills.py -n 25 --report-name top-25

# Verbose logging
python scripts/scan-skills.py -n 10 -v
```

Run `python scripts/scan-skills.py --help` for the full set of options.

### Running tests

```bash
python -m pytest tests/ -v
```

## Project Structure

```
scripts/
  scan-skills.py          # Main orchestrator and CLI
  fetch_skills.py         # API fetching from skills.sh and clawhub.ai
  run_scans.py            # Clone, download, and scan logic
  generate_report.py      # Aggregate results into markdown/JSON reports
  pipeline_utils.py       # Shared utilities: logging, HTTP session management
  requirements.txt        # Dependencies

tests/                    # 77 tests across 4 modules
  conftest.py             # Shared fixtures
  test_run_scans.py       # Clone, download, scan, ZIP security tests
  test_generate_report.py # Report aggregation tests
  test_fetch_skills.py    # API fetching tests
  test_pipeline_utils.py  # Session management and retry tests

results/
  summary-report.md       # Consolidated findings across all skills
  <skill-name>-scan.json  # Raw scan output per skill
  <skill-name>-scan.md    # Readable scan report per skill
```

Cloned skill repositories are kept in `skills/` locally but excluded from version control via `.gitignore`.

## Known Limitations

- No runtime verification -- analysis is static and semantic only
- LLM and meta-analysis require an API key (`SKILL_SCANNER_LLM_API_KEY`); without one, scans fall back to static/behavioral/trigger only
- Limited to skills with public source repos
- Scanner coverage depends on the rule sets of the underlying tools

## Links

- [Cisco AI Defense skill-scanner](https://github.com/cisco-ai-defense/skill-scanner)
- [skills.sh](https://skills.sh/)
- [clawhub.ai](https://clawhub.ai/)
- [Agent Skills in the Wild: An Empirical Study of Security Vulnerabilities at Scale](https://arxiv.org/abs/2601.10338) -- large-scale security analysis of 31k+ skills from skills.rest and skillsmp.com

## License

MIT
