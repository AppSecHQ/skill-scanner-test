"""Regenerating from results/ must reproduce the attribution the live site uses.

``docs/data/summary.json`` is the committed authority for each skill's
``source`` and ``repo_url``; skill URLs are derived from it. A local run of
``aggregate_results`` with the default arguments must match it exactly, so a
stale local inventory can never rename a live page (see WHATS-NEXT defect 5).
"""
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from generate_report import aggregate_results  # noqa: E402

ROOT = Path(__file__).parent.parent
RESULTS = ROOT / "results"
SUMMARY = ROOT / "docs" / "data" / "summary.json"


@pytest.mark.skipif(not SUMMARY.exists() or not RESULTS.exists(), reason="needs the repo's results and summary")
def test_default_aggregation_matches_committed_attribution():
    published = json.loads(SUMMARY.read_text())
    published = published if isinstance(published, list) else published["skills"]
    want = {r["scan_file"]: (r["source"], r.get("repo_url", "")) for r in published}

    got = {s["scan_file"]: (s["source"], s.get("repo_url", "")) for s in aggregate_results(RESULTS)["skills"]}

    flipped = {k: (want[k], got[k]) for k in want.keys() & got.keys() if want[k] != got[k]}
    assert not flipped, f"{len(flipped)} attribution changes, e.g. {list(flipped.items())[:5]}"
    assert set(got) >= set(want), f"published scans missing from results/: {sorted(set(want) - set(got))[:5]}"


def test_inventory_is_ignored_unless_requested(tmp_path):
    results = tmp_path / "results"
    results.mkdir()
    skills = tmp_path / "skills"
    skills.mkdir()
    (skills / "skill-inventory-x.json").write_text(json.dumps(
        [{"name": "thing", "source": "clawhub", "id": "thing"}]))
    (results / "thing-scan.json").write_text(json.dumps({
        "skill_name": "thing", "is_safe": True, "max_severity": "SAFE", "findings_count": 0,
        "findings": [], "analyzers_used": [], "timestamp": "2026-10-22T00:00:00",
        "skill_path": "/workspace/skills/owner-repo/skills/thing"}))

    default = aggregate_results(results)["skills"][0]
    opted_in = aggregate_results(results, skills_dir=skills)["skills"][0]
    assert default["source"] != "clawhub.ai"
    assert opted_in["source"] == "clawhub.ai"
