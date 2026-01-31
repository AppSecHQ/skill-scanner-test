# Automation Plan: Skill Scanner Pipeline

## Goal

Create a deterministic, scriptable pipeline to:
1. Fetch top N skills from skills.sh
2. Clone repositories
3. Run security scans
4. Generate summary reports

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     scan-skills.py                          │
│  (Main orchestrator - single entry point)                   │
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│  fetch_skills │    │  run_scans    │    │ generate_report│
│  (Module 1)   │    │  (Module 2)   │    │  (Module 3)    │
└───────────────┘    └───────────────┘    └───────────────┘
```

---

## Module 1: Fetch Skills

### Option A: API (Preferred if available)

Check if skills.sh has an API endpoint:
```bash
curl -s "https://skills.sh/api/skills?sort=installs&limit=25"
```

### Option B: Scrape HTML

If no API, scrape the page with a deterministic parser:

```python
# fetch_skills.py
import requests
from bs4 import BeautifulSoup
import json

def fetch_top_skills(n: int = 25) -> list[dict]:
    """Fetch top N skills from skills.sh"""
    url = "https://skills.sh/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    skills = []
    # Parse skill cards (adjust selectors based on actual HTML)
    for card in soup.select('.skill-card')[:n]:
        skills.append({
            'name': card.select_one('.skill-name').text,
            'repo': card.select_one('.repo-link')['href'],
            'installs': parse_installs(card.select_one('.install-count').text),
            'description': card.select_one('.description').text
        })

    return skills

def save_inventory(skills: list[dict], output_path: str):
    """Save skills to JSON for downstream processing"""
    with open(output_path, 'w') as f:
        json.dump(skills, f, indent=2)
```

### Output Format

```json
// skills/skill-inventory.json
[
  {
    "rank": 1,
    "name": "vercel-react-best-practices",
    "repo": "vercel-labs/agent-skills",
    "skill_path": "skills/react-best-practices",
    "installs": 73182,
    "description": "React best practices guidelines"
  }
]
```

---

## Module 2: Clone & Scan

### Challenges to Solve

1. **Monorepos**: Multiple skills in one repo (e.g., vercel-labs/agent-skills)
2. **Skill path detection**: Finding the actual skill directory within a repo
3. **Idempotency**: Don't re-clone or re-scan if already done

### Implementation

```python
# run_scans.py
import subprocess
import json
from pathlib import Path

def clone_repo(repo: str, dest: Path) -> bool:
    """Clone repo if not already present"""
    if dest.exists():
        return True  # Already cloned

    url = f"https://github.com/{repo}.git"
    result = subprocess.run(
        ["git", "clone", "--depth=1", url, str(dest)],
        capture_output=True
    )
    return result.returncode == 0

def find_skill_path(repo_dir: Path, skill_name: str) -> Path | None:
    """Locate skill directory within repo"""
    # Common patterns:
    # 1. repo/skills/{skill_name}/
    # 2. repo/{skill_name}/
    # 3. repo/ (skill is the entire repo)

    candidates = [
        repo_dir / "skills" / skill_name,
        repo_dir / "skills" / skill_name.replace("vercel-", ""),
        repo_dir / skill_name,
        repo_dir,  # Fallback: entire repo is the skill
    ]

    for path in candidates:
        if (path / "SKILL.md").exists():
            return path

    return None

def run_scan(skill_path: Path, output_dir: Path, skill_name: str) -> dict:
    """Run skill-scanner and return results"""
    json_output = output_dir / f"{skill_name}-scan.json"
    md_output = output_dir / f"{skill_name}-scan.md"

    # Run scan
    subprocess.run([
        "skill-scanner", "scan", str(skill_path),
        "--use-behavioral", "--use-trigger",
        "--format", "json",
        "-o", str(json_output)
    ])

    subprocess.run([
        "skill-scanner", "scan", str(skill_path),
        "--use-behavioral", "--use-trigger",
        "--format", "markdown",
        "-o", str(md_output)
    ])

    # Load and return results
    with open(json_output) as f:
        return json.load(f)
```

### Repo Deduplication

```python
def get_unique_repos(skills: list[dict]) -> dict[str, list[dict]]:
    """Group skills by repo to avoid duplicate clones"""
    repos = {}
    for skill in skills:
        repo = skill['repo']
        if repo not in repos:
            repos[repo] = []
        repos[repo].append(skill)
    return repos

# Example output:
# {
#   "vercel-labs/agent-skills": [skill1, skill3, skill8, skill9],
#   "vercel-labs/skills": [skill2],
#   ...
# }
```

---

## Module 3: Generate Report

```python
# generate_report.py
import json
from pathlib import Path
from datetime import datetime

def aggregate_results(results_dir: Path) -> dict:
    """Aggregate all scan results"""
    findings = {
        'total_skills': 0,
        'safe_skills': 0,
        'unsafe_skills': 0,
        'severity_counts': {'CRITICAL': 0, 'HIGH': 0, 'MEDIUM': 0, 'LOW': 0},
        'skills': []
    }

    for json_file in results_dir.glob('*-scan.json'):
        with open(json_file) as f:
            result = json.load(f)

        findings['total_skills'] += 1
        if result['is_safe']:
            findings['safe_skills'] += 1
        else:
            findings['unsafe_skills'] += 1

        # Count severities
        for finding in result.get('findings', []):
            sev = finding.get('severity', 'LOW')
            findings['severity_counts'][sev] += 1

        findings['skills'].append({
            'name': result['skill_name'],
            'is_safe': result['is_safe'],
            'findings_count': result['findings_count'],
            'max_severity': result['max_severity']
        })

    return findings

def generate_markdown_report(findings: dict, output_path: Path):
    """Generate summary report"""
    report = f"""# AI Agent Skills Security Scan Report

**Generated:** {datetime.now().isoformat()}
**Scanner:** cisco-ai-skill-scanner
**Analyzers:** static, behavioral, trigger

## Executive Summary

| Metric | Count |
|--------|-------|
| Total Skills Scanned | {findings['total_skills']} |
| Safe Skills | {findings['safe_skills']} |
| Unsafe Skills | {findings['unsafe_skills']} |

### Severity Breakdown

| Severity | Count |
|----------|-------|
| CRITICAL | {findings['severity_counts']['CRITICAL']} |
| HIGH | {findings['severity_counts']['HIGH']} |
| MEDIUM | {findings['severity_counts']['MEDIUM']} |
| LOW | {findings['severity_counts']['LOW']} |

## Results by Skill

| Skill | Safe | Findings | Max Severity |
|-------|------|----------|--------------|
"""
    for skill in findings['skills']:
        safe = "Yes" if skill['is_safe'] else "**No**"
        report += f"| {skill['name']} | {safe} | {skill['findings_count']} | {skill['max_severity']} |\n"

    with open(output_path, 'w') as f:
        f.write(report)
```

---

## Main Orchestrator

```python
#!/usr/bin/env python3
# scan-skills.py

import argparse
import sys
from pathlib import Path

from fetch_skills import fetch_top_skills, save_inventory
from run_scans import clone_repo, find_skill_path, run_scan, get_unique_repos
from generate_report import aggregate_results, generate_markdown_report

def main():
    parser = argparse.ArgumentParser(description='Scan top AI agent skills for security issues')
    parser.add_argument('-n', '--count', type=int, default=25, help='Number of top skills to scan')
    parser.add_argument('-o', '--output', type=Path, default=Path('results'), help='Output directory')
    parser.add_argument('--skills-dir', type=Path, default=Path('skills'), help='Directory for cloned repos')
    parser.add_argument('--skip-fetch', action='store_true', help='Skip fetching skills (use existing inventory)')
    parser.add_argument('--skip-clone', action='store_true', help='Skip cloning repos')
    parser.add_argument('--use-llm', action='store_true', help='Enable LLM analyzer (requires API key)')
    args = parser.parse_args()

    # Setup directories
    args.output.mkdir(exist_ok=True)
    args.skills_dir.mkdir(exist_ok=True)

    inventory_path = args.skills_dir / 'skill-inventory.json'

    # Step 1: Fetch skills
    if not args.skip_fetch:
        print(f"Fetching top {args.count} skills from skills.sh...")
        skills = fetch_top_skills(args.count)
        save_inventory(skills, inventory_path)
    else:
        with open(inventory_path) as f:
            skills = json.load(f)

    print(f"Loaded {len(skills)} skills")

    # Step 2: Clone repos (deduplicated)
    if not args.skip_clone:
        repos = get_unique_repos(skills)
        print(f"Cloning {len(repos)} unique repositories...")
        for repo in repos:
            repo_dir = args.skills_dir / repo.replace('/', '-')
            clone_repo(repo, repo_dir)

    # Step 3: Run scans
    print("Running security scans...")
    results = []
    for skill in skills:
        repo_dir = args.skills_dir / skill['repo'].replace('/', '-')
        skill_path = find_skill_path(repo_dir, skill['name'])

        if skill_path is None:
            print(f"  Warning: Could not find skill path for {skill['name']}")
            continue

        print(f"  Scanning {skill['name']}...")
        result = run_scan(skill_path, args.output, skill['name'])
        results.append(result)

    # Step 4: Generate report
    print("Generating summary report...")
    findings = aggregate_results(args.output)
    generate_markdown_report(findings, args.output / 'summary-report.md')

    print(f"\nDone! Results saved to {args.output}/")
    print(f"  - {findings['total_skills']} skills scanned")
    print(f"  - {findings['unsafe_skills']} skills with issues")

if __name__ == '__main__':
    main()
```

---

## Usage

```bash
# Install dependencies
pip install cisco-ai-skill-scanner beautifulsoup4 requests

# Run full pipeline (top 25 skills)
python scan-skills.py -n 25

# Run with LLM analyzer
export SKILL_SCANNER_LLM_API_KEY="your-key"
python scan-skills.py -n 25 --use-llm

# Skip fetching (use existing inventory)
python scan-skills.py --skip-fetch

# Custom output directory
python scan-skills.py -n 10 -o ./my-results
```

---

## Directory Structure (After Running)

```
skill-scanner/
├── scan-skills.py              # Main orchestrator
├── fetch_skills.py             # Module 1
├── run_scans.py                # Module 2
├── generate_report.py          # Module 3
├── skills/
│   ├── skill-inventory.json    # Fetched skill metadata
│   ├── vercel-labs-agent-skills/
│   ├── vercel-labs-skills/
│   └── ...
└── results/
    ├── *-scan.json             # Raw scan results
    ├── *-scan.md               # Readable scan results
    └── summary-report.md       # Aggregated report
```

---

## Error Handling

```python
# Add to run_scans.py

class ScanError(Exception):
    pass

def run_scan_safe(skill_path: Path, output_dir: Path, skill_name: str) -> dict | None:
    """Run scan with error handling"""
    try:
        return run_scan(skill_path, output_dir, skill_name)
    except subprocess.CalledProcessError as e:
        print(f"  Error scanning {skill_name}: {e}")
        return {
            'skill_name': skill_name,
            'is_safe': None,
            'error': str(e),
            'findings_count': 0,
            'max_severity': 'ERROR'
        }
    except FileNotFoundError:
        print(f"  Error: skill-scanner not found. Is it installed?")
        sys.exit(1)
```

---

## CI/CD Integration

```yaml
# .github/workflows/scan-skills.yml
name: Weekly Skill Scan

on:
  schedule:
    - cron: '0 0 * * 0'  # Weekly on Sunday
  workflow_dispatch:      # Manual trigger

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install cisco-ai-skill-scanner beautifulsoup4 requests

      - name: Run scan
        run: python scan-skills.py -n 25

      - name: Upload results
        uses: actions/upload-artifact@v4
        with:
          name: scan-results
          path: results/

      - name: Check for critical findings
        run: |
          if grep -q '"max_severity": "CRITICAL"' results/*-scan.json; then
            echo "::error::Critical security findings detected!"
            exit 1
          fi
```

---

## Next Steps

1. **Investigate skills.sh structure** - Check for API or determine HTML selectors
2. **Create the Python modules** - Implement fetch, scan, report modules
3. **Test on small N** - Verify with 3-5 skills first
4. **Add caching** - Skip already-scanned skills
5. **Add parallel scanning** - Use multiprocessing for faster scans
