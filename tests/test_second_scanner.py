"""SkillSpector runner, target scanner naming, well-known fetcher, and the
Cisco-vs-SkillSpector comparison."""
import json
import subprocess
import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

import compare_scanners  # noqa: E402
import fetch_wellknown  # noqa: E402
import run_skillspector  # noqa: E402
import scan_targets  # noqa: E402


class TestResolveLocalSkillPath:
    def test_ci_workspace_path_maps_to_local_skills_dir(self, tmp_path):
        (tmp_path / "skills" / "owner-repo" / "skills" / "x").mkdir(parents=True)
        got = run_skillspector.resolve_local_skill_path("/workspace/skills/owner-repo/skills/x", tmp_path / "skills")
        assert got == tmp_path / "skills" / "owner-repo" / "skills" / "x"

    def test_github_runner_path_with_dotdot(self, tmp_path):
        (tmp_path / "skills" / "K-Dense-AI-scientific-agent-skills" / "skills" / "gget").mkdir(parents=True)
        p = "/home/runner/work/skill-scanner-test/skill-scanner-test/scripts/../skills/K-Dense-AI-scientific-agent-skills/skills/gget"
        assert run_skillspector.resolve_local_skill_path(p, tmp_path / "skills") is not None

    def test_missing_returns_none(self, tmp_path):
        assert run_skillspector.resolve_local_skill_path("/workspace/skills/nope/x", tmp_path / "skills") is None
        assert run_skillspector.resolve_local_skill_path("", tmp_path / "skills") is None


class TestScanOne:
    def _fake(self, report, rc=0):
        def fake(cmd, **kw):
            Path(cmd[cmd.index("--output") + 1]).write_text(json.dumps(report))
            assert "--no-llm" in cmd and cmd[cmd.index("--format") + 1] == "json"
            return subprocess.CompletedProcess(cmd, rc, "", "")
        return fake

    def test_writes_report_with_meta_and_keeps_exit_1_as_result(self, tmp_path):
        report = {"risk_assessment": {"score": 77, "severity": "HIGH", "recommendation": "DO_NOT_INSTALL"}, "issues": [{"id": "X"}]}
        out = tmp_path / "ss" / "a-skillspector.json"
        with patch("run_skillspector.subprocess.run", side_effect=self._fake(report, rc=1)):
            row = run_skillspector.scan_one("skillspector", tmp_path, out, tmp_path / "a-scan.json")
        assert row == {"name": "a-skillspector", "score": 77, "severity": "HIGH", "recommendation": "DO_NOT_INSTALL", "issues": 1}
        saved = json.loads(out.read_text())
        assert saved["_meta"]["cisco_result"] == "a-scan.json" and saved["_meta"]["exit_code"] == 1

    def test_exit_2_is_error(self, tmp_path):
        with patch("run_skillspector.subprocess.run", return_value=subprocess.CompletedProcess([], 2, "", "bad input")):
            row = run_skillspector.scan_one("skillspector", tmp_path, tmp_path / "x.json", tmp_path / "a-scan.json")
        assert row["error"] == "bad input"

    def test_timeout_is_error(self, tmp_path):
        with patch("run_skillspector.subprocess.run", side_effect=subprocess.TimeoutExpired("x", 1)):
            row = run_skillspector.scan_one("skillspector", tmp_path, tmp_path / "x.json", tmp_path / "a-scan.json")
        assert row["error"] == "timeout"


class TestScanTargets:
    def test_names_are_prefixed_with_target_dir(self, tmp_path):
        repo = tmp_path / "skills" / "a-repo"
        for rel in ("skills/tdd", "skills/eng/review", "."):
            (repo / rel).mkdir(parents=True, exist_ok=True)
            (repo / rel / "SKILL.md").write_text("x")
        (repo / "node_modules" / "pkg").mkdir(parents=True)
        (repo / "node_modules" / "pkg" / "SKILL.md").write_text("x")
        names = scan_targets.skill_names(repo)
        assert set(names.values()) == {"a-repo", "a-repo-skills-tdd", "a-repo-skills-eng-review"}

    def test_two_repos_with_same_skill_do_not_collide(self, tmp_path):
        stems = []
        for r in ("101-skills-superpowers", "obra-superpowers"):
            repo = tmp_path / r
            (repo / "skills" / "tdd").mkdir(parents=True)
            (repo / "skills" / "tdd" / "SKILL.md").write_text("x")
            stems += list(scan_targets.skill_names(repo).values())
        assert len(set(stems)) == 2

    def test_target_forms(self, tmp_path):
        d, o = scan_targets.target_to_dir_and_origin("owner/repo", tmp_path)
        assert d == tmp_path / "owner-repo" and o == {"source": "owner", "repo_url": "https://github.com/owner/repo"}
        d, o = scan_targets.target_to_dir_and_origin("https://github.com/owner/repo/", tmp_path)
        assert d == tmp_path / "owner-repo"
        d, o = scan_targets.target_to_dir_and_origin("site:uizze.sh", tmp_path)
        assert d == tmp_path / "site-uizze.sh" and o["source"] == "uizze.sh"

    def test_scan_target_passes_origin_to_batch(self, tmp_path):
        repo = tmp_path / "owner-repo"
        (repo / "SKILL.md").parent.mkdir(parents=True)
        (repo / "SKILL.md").write_text("x")
        with patch("scan_targets.run_batch_scan", return_value={"owner-repo": {"is_safe": True}}) as m:
            got = scan_targets.scan_target("owner/repo", tmp_path, tmp_path / "out", "skill-scanner")
        assert got == {"owner-repo": {"is_safe": True}}
        assert m.call_args.kwargs["origin"]["repo_url"] == "https://github.com/owner/repo"
        assert m.call_args.kwargs["names"] == {repo: "owner-repo"}


class TestWellKnown:
    def test_rejects_path_traversal(self):
        assert fetch_wellknown._safe_relative("../etc/passwd") is None
        assert fetch_wellknown._safe_relative("/abs") is None
        assert str(fetch_wellknown._safe_relative("references/a.md")) == "references/a.md"

    def test_download_skill_fetches_files_under_agent_skills(self, tmp_path):
        calls = []

        class Resp:
            status_code = 200
            content = b"# skill"

        class Sess:
            def get(self, url, timeout):
                calls.append(url)
                return Resp()

        with patch("fetch_wellknown.get_session", return_value=Sess()):
            dest = fetch_wellknown.download_skill("uizze.sh", {"name": "ui-taste", "files": ["reference/a.md"]}, tmp_path)
        assert dest == tmp_path / "ui-taste"
        assert (dest / "SKILL.md").exists() and (dest / "reference" / "a.md").exists()
        assert calls == ["https://uizze.sh/.well-known/agent-skills/ui-taste/SKILL.md",
                         "https://uizze.sh/.well-known/agent-skills/ui-taste/reference/a.md"]
        assert json.loads((dest / ".wellknown-origin.json").read_text())["host"] == "uizze.sh"

    def test_unsafe_skill_name_skipped(self, tmp_path):
        with patch("fetch_wellknown.get_session"):
            assert fetch_wellknown.download_skill("h", {"name": "../x"}, tmp_path) is None


class TestCompare:
    def _pair(self, cisco_safe, cisco_sev, rec):
        return {"name": "n", "skill_name": "n", "source": "s",
                "cisco": {"flagged": not cisco_safe, "flagged_strict": cisco_sev in ("HIGH", "CRITICAL"),
                          "max_severity": cisco_sev, "findings": 0, "categories": []},
                "skillspector": {"flagged": rec != "SAFE", "flagged_strict": rec == "DO_NOT_INSTALL",
                                 "recommendation": rec, "score": 0, "severity": "LOW", "findings": 0, "categories": []}}

    def test_contingency_and_kappa(self):
        pairs = [self._pair(False, "HIGH", "DO_NOT_INSTALL"), self._pair(True, "SAFE", "SAFE"),
                 self._pair(False, "MEDIUM", "SAFE"), self._pair(True, "SAFE", "CAUTION")]
        loose = compare_scanners.summarize(pairs)
        assert (loose["flagged_by_both"], loose["cisco_only"], loose["skillspector_only"], loose["flagged_by_neither"]) == (1, 1, 1, 1)
        assert loose["agreement_rate"] == 0.5 and loose["cohens_kappa"] == 0.0
        strict = compare_scanners.summarize(pairs, "flagged_strict")
        assert strict["flagged_by_both"] == 1 and strict["flagged_by_neither"] == 3 and strict["cohens_kappa"] == 1.0

    def test_load_pairs_uses_summary_for_source_and_skips_failed(self, tmp_path):
        results = tmp_path / "results"
        (results / "skillspector").mkdir(parents=True)
        (tmp_path / "docs" / "data").mkdir(parents=True)
        (tmp_path / "docs" / "data" / "summary.json").write_text(json.dumps([{"scan_file": "a-scan.md", "source": "obra"}]))
        (results / "a-scan.json").write_text(json.dumps({"skill_name": "a", "is_safe": False, "max_severity": "HIGH", "findings_count": 1,
                                                          "findings": [{"category": "command_injection"}]}))
        (results / "skillspector" / "a-skillspector.json").write_text(json.dumps({"risk_assessment": {"score": 60, "recommendation": "DO_NOT_INSTALL", "severity": "HIGH"},
                                                                                   "issues": [{"category": "Tool Misuse"}], "metadata": {"skillspector_version": "2.12.0"}}))
        (results / "b-scan.json").write_text(json.dumps({"skill_name": "b", "is_safe": None, "error": "Scan failed"}))
        (results / "skillspector" / "b-skillspector.json").write_text(json.dumps({"risk_assessment": {}, "issues": []}))
        pairs = compare_scanners.load_pairs(results)
        assert len(pairs) == 1 and pairs[0]["source"] == "obra"
        assert pairs[0]["cisco"]["flagged_strict"] and pairs[0]["skillspector"]["flagged_strict"]
        assert pairs[0]["skillspector"]["categories"] == ["Tool Misuse"]
