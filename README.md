# Skill Scanner: Security Assessment of Popular AI Agent Skills

Security scan results for the top 10 most-installed AI agent skills from [skills.sh](https://skills.sh/), analyzed using Cisco's open-source [skill-scanner](https://github.com/cisco-ai-defense/skill-scanner).

## Key Findings

| Metric | Value |
|--------|-------|
| Skills scanned | 10 |
| Clean (no findings) | 5 |
| Marked unsafe | 1 |
| Total findings | 12 |

**Severity breakdown:** 0 Critical, 1 High, 6 Medium, 5 Low

- **90%** of the top 10 skills passed all security checks
- **1 skill** ([agent-browser](results/agent-browser-scan.md)) flagged with a HIGH-severity tool permission mismatch and 6 MEDIUM-severity command injection findings
- **50%** of skills are missing license metadata in their manifests (LOW severity)

See the full [summary report](results/summary-report.md) for details.

## Skills Scanned

| Skill | Repo | Installs | Findings |
|-------|------|----------|----------|
| vercel-react-best-practices | vercel-labs/agent-skills | 73,182 | 0 |
| find-skills | vercel-labs/skills | 40,505 | 1 LOW |
| web-design-guidelines | vercel-labs/agent-skills | 30,817 | 1 LOW |
| remotion-best-practices | remotion-dev/skills | 29,152 | 1 LOW |
| frontend-design | anthropics/skills | 27,292 | 0 |
| agent-browser | vercel-labs/agent-browser | 15,968 | 1 HIGH, 6 MED, 1 LOW |
| skill-creator | anthropics/skills | 13,525 | 0 |
| vercel-composition-patterns | vercel-labs/agent-skills | 11,340 | 0 |
| vercel-react-native-skills | vercel-labs/agent-skills | 8,611 | 0 |
| seo-audit | coreyhaines31/marketingskills | 7,236 | 1 LOW |

## Repository Structure

```
results/
  summary-report.md           # Consolidated findings report
  <skill-name>-scan.json      # Raw JSON scan output per skill
  <skill-name>-scan.md        # Human-readable scan report per skill
```

Each skill has both a JSON file (machine-readable) and a Markdown file (human-readable) in `results/`.

## Methodology

Scans were run on 2026-01-30 using `cisco-ai-skill-scanner` v1.0.1.

**Analyzers used:**

| Analyzer | Description |
|----------|-------------|
| static_analyzer | Pattern-based detection using YAML + YARA rules (80+ patterns, 12+ threat categories) |
| behavioral_analyzer | Static dataflow analysis via AST + taint tracking |
| trigger_analyzer | Detects overly generic descriptions and trigger hijacking risks |

**Analyzers not available** (require API keys): llm_analyzer, meta_analyzer, virustotal_analyzer, aidefense_analyzer.

### Limitations

- No LLM-based semantic analysis -- may miss context-dependent vulnerabilities
- No binary file scanning (VirusTotal unavailable)
- Static analysis only; no runtime behavior verification
- Sample limited to 10 skills; may not represent the broader ecosystem

## Reproducing the Scans

```bash
# Install the scanner
pip install cisco-ai-skill-scanner

# Clone a skill
git clone https://github.com/<owner>/<repo> skills/<skill-name>

# Run a scan (JSON output)
skill-scanner scan skills/<skill-name> --output-format json --output results/<skill-name>-scan.json

# Run a scan (Markdown output)
skill-scanner scan skills/<skill-name> --output-format markdown --output results/<skill-name>-scan.md
```

Requires Python 3.10+ and Git.

## References

- [Cisco AI Defense skill-scanner](https://github.com/cisco-ai-defense/skill-scanner)
- [skills.sh](https://skills.sh/) -- AI agent skills directory
