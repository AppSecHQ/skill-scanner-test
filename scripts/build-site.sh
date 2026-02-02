#!/usr/bin/env bash
# Copy scan result JSON into docs/data/ for the static site
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Source and destination
RESULTS_DIR="${PROJECT_ROOT}/results"
DATA_DIR="${PROJECT_ROOT}/docs/data"
SCANS_DIR="${DATA_DIR}/scans"

# Create directories
mkdir -p "$SCANS_DIR"

# Copy summary
cp "$RESULTS_DIR/summary-report.json" "$DATA_DIR/summary.json"

# Copy individual scan files
cp "$RESULTS_DIR"/*-scan.json "$SCANS_DIR/"

# Enrich summary.json with repo URLs from inventory files + path heuristics
python3 -c "
import json, os, glob, re

summary_path = '${DATA_DIR}/summary.json'
inventory_dir = '${PROJECT_ROOT}/skills'

# Load all inventory files and build lookups by id
url_map = {}
for inv_file in glob.glob(os.path.join(inventory_dir, 'skill-inventory*.json')):
    with open(inv_file) as f:
        for entry in json.load(f):
            sid = entry.get('id', '')
            source = entry.get('source', '')
            repo = entry.get('repo')
            if source == 'skills.sh' and repo:
                url_map[sid] = 'https://github.com/' + repo
            elif source == 'clawhub':
                url_map[sid] = 'https://clawhub.ai/skills/' + sid

# Patch summary
with open(summary_path) as f:
    summary = json.load(f)

for skill in summary.get('skills', []):
    name_lower = skill['name'].lower().replace(' ', '-')
    # Try inventory lookup first
    url = url_map.get(name_lower, url_map.get(skill['name'], ''))

    # Fallback: derive from clone path
    if not url and skill.get('path'):
        path = skill['path']
        # Normalize absolute /workspace/skills/ paths to ./skills/
        path = re.sub(r'^/workspace/skills/', './skills/', path)
        # moltbook.com: standalone skill
        if skill.get('source') == 'moltbook.com':
            url = 'https://www.moltbook.com'
        # anthropic skills: path like ./skills/anthropics-skills/skills/<name>
        elif skill.get('source') == 'anthropic':
            m = re.match(r'^\./skills/anthropics-skills/skills/(.+)$', path)
            if m:
                url = 'https://github.com/anthropics/skills/tree/main/skills/' + m.group(1)
        # clawhub.ai skills: path like ./skills/clawhub-<name>
        elif skill.get('source') == 'clawhub.ai':
            m = re.match(r'^\./skills/clawhub-(.+)$', path)
            if m:
                url = 'https://clawhub.ai/skills/' + m.group(1)
        # skills.sh: path like ./skills/<owner>-<repo>/... -> github.com/<owner>/<repo>
        elif skill.get('source') == 'skills.sh':
            # Extract the top-level clone dir
            parts = path.replace('./skills/', '').split('/')
            if parts:
                clone_dir = parts[0]
                # Known repo mappings from clone dir patterns
                known = {
                    'vercel-labs-agent-browser': 'vercel-labs/agent-browser',
                    'vercel-labs-skills': 'vercel-labs/skills',
                    'vercel-labs-next-skills': 'vercel-labs/next-skills',
                    'anthropics-skills': 'anthropics/skills',
                    'expo-skills': 'expo/skills',
                    'remotion-dev-skills': 'remotion-dev/skills',
                    'squirrelscan-skills': 'squirrelscan/skills',
                    'obra-superpowers': 'obra/superpowers',
                    'coreyhaines31-marketingskills': 'coreyhaines31/marketingskills',
                    'browser-use-browser-use': 'browser-use/browser-use',
                    'nextlevelbuilder-ui-ux-pro-max-skill': 'nextlevelbuilder/ui-ux-pro-max-skill',
                    'supabase-agent-skills': 'supabase/agent-skills',
                    'better-auth-skills': 'better-auth/skills',
                    'hyf0-vue-skills': 'hyf0/vue-skills',
                    'callstackincubator-agent-skills': 'callstackincubator/agent-skills',
                }
                # Non-GitHub skills with direct URLs
                direct_urls = {
                    'moltbook': 'https://www.moltbook.com',
                }
                if clone_dir in direct_urls:
                    url = direct_urls[clone_dir]
                elif clone_dir in known:
                    url = 'https://github.com/' + known[clone_dir]
                else:
                    # Generic: try splitting on first hyphen as owner-repo
                    parts2 = clone_dir.split('-', 1)
                    if len(parts2) == 2:
                        url = 'https://github.com/' + parts2[0] + '/' + parts2[1]

    skill['repo_url'] = url

with open(summary_path, 'w') as f:
    json.dump(summary, f, indent=2)

patched = sum(1 for s in summary['skills'] if s.get('repo_url'))
missing = [s['name'] for s in summary['skills'] if not s.get('repo_url')]
print(f'Enriched {patched}/{len(summary[\"skills\"])} skills with repo URLs')
if missing:
    print(f'Still missing: {missing}')
"

echo "Copied summary + $(ls "$SCANS_DIR"/*.json | wc -l | tr -d ' ') scan files to $DATA_DIR"
