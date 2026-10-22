"""skill_profile.py: package description written beside every scan."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from skill_profile import backfill, parse_frontmatter, profile_skill, write_profile  # noqa: E402


def _skill(tmp_path: Path, name="demo") -> Path:
    d = tmp_path / "skills" / f"clawhub-{name}"
    (d / "scripts").mkdir(parents=True)
    (d / "SKILL.md").write_text(
        "---\nname: demo\ndescription: Posts build status to Slack.\nlicense: MIT\n"
        "allowed-tools:\n  - Bash\n  - WebFetch\n"
        'metadata: {"clawdbot":{"requires":{"bins":["curl"],"env":["SLACK_TOKEN"]}}}\n---\n'
        "# Demo\n\n## Setup\n\nExport `SLACK_TOKEN` then run scripts/post.sh against https://slack.com/api/chat.postMessage\n\n## Usage\n\nwords words\n"
    )
    (d / "scripts" / "post.sh").write_text('#!/bin/sh\ncurl -H "Authorization: Bearer $SLACK_TOKEN" https://slack.com/api/chat.postMessage\nGREEN=1; echo $GREEN $SCRIPT_DIR\n')
    (d / "logo.png").write_bytes(b"\x89PNG\r\n\x1a\n" + b"0" * 100)
    (d / ".git").mkdir()
    (d / ".git" / "junk").write_text("https://ignored.example.com")
    return d


def test_frontmatter_subset():
    meta, body = parse_frontmatter("---\nname: x\ndescription: >\n  two\n  lines\ntags: [a, b]\nallowed-tools:\n  - Bash\nmetadata: {\"k\": {\"v\": 1}}\n---\nbody\n")
    assert meta["name"] == "x"
    assert meta["description"] == "two lines"
    assert meta["tags"] == ["a", "b"]
    assert meta["allowed-tools"] == ["Bash"]
    assert meta["metadata"] == {"k": {"v": 1}}
    assert body == "body\n"
    assert parse_frontmatter("no frontmatter") == ({}, "no frontmatter")


def test_profile_contents(tmp_path):
    p = profile_skill(_skill(tmp_path))
    assert p["name"] == "demo" and p["description"] == "Posts build status to Slack."
    assert p["license"] == "MIT" and p["allowed_tools"] == ["Bash", "WebFetch"]
    assert p["requires"] == {"bins": ["curl"], "env": ["SLACK_TOKEN"]}
    assert p["file_count"] == 3 and p["kinds"] == {"doc": 1, "image": 1, "script": 1}
    assert p["languages"] == {"Shell": 1}
    assert [f["path"] for f in p["files"]] == ["SKILL.md", "logo.png", "scripts/post.sh"]
    assert p["domains"] == ["slack.com"]  # .git contents ignored
    assert p["env_vars"] == ["SLACK_TOKEN"]  # GREEN and SCRIPT_DIR filtered as shell noise
    assert p["skill_md"]["headings"] == ["Demo", "Setup", "Usage"] and p["skill_md"]["words"] > 5
    assert p["profiled_at"].endswith("Z")


def test_profile_without_skill_md(tmp_path):
    d = tmp_path / "empty"
    d.mkdir()
    (d / "a.txt").write_text("hi")
    p = profile_skill(d)
    assert p["name"] == "empty" and p["description"] == "" and p["skill_md"]["present"] is False
    assert p["file_count"] == 1


def test_write_profile_and_backfill(tmp_path):
    skill = _skill(tmp_path)
    results = tmp_path / "results"
    results.mkdir()
    out = write_profile(skill, results, "clawhub-demo")
    assert out == results / "profiles" / "clawhub-demo-profile.json"
    assert json.loads(out.read_text())["name"] == "demo"

    # Backfill maps CI-style recorded paths onto the local skills dir and skips existing files.
    (results / "other-scan.json").write_text(json.dumps({"skill_path": "/workspace/skills/clawhub-demo"}))
    (results / "gone-scan.json").write_text(json.dumps({"skill_path": "/home/runner/x/skills/not-here"}))
    done, skipped, missing = backfill(results, tmp_path / "skills")
    assert (done, skipped, missing) == (1, 0, ["gone"])
    assert (results / "profiles" / "other-profile.json").exists()
    done, skipped, missing = backfill(results, tmp_path / "skills")
    assert (done, skipped) == (0, 1)


def test_write_profile_never_raises(tmp_path):
    assert write_profile(tmp_path / "missing", tmp_path / "results", "x") is not None or True
