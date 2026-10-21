"""Tests for the single-process batch scan path (run_scans.run_batch_scan and
community_scan.run_community_scan's use of it)."""
import json
import subprocess
import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from community_scan import run_community_scan  # noqa: E402
from run_scans import run_batch_scan, write_markdown_summary  # noqa: E402


def _result(path: Path, name: str, findings=None):
    findings = findings or []
    return {
        "skill_name": name, "skill_path": str(path), "is_safe": not findings,
        "max_severity": findings[0]["severity"] if findings else "SAFE",
        "findings_count": len(findings), "findings": findings,
        "analyzers_used": ["static_analyzer"], "timestamp": "2026-10-21T20:00:00+00:00",
    }


def _fake_scan_all(results):
    """subprocess.run replacement that writes the combined JSON to the -o path."""
    def fake(cmd, **kwargs):
        assert cmd[1] == "scan-all" and "--recursive" in cmd
        out = Path(cmd[cmd.index("-o") + 1])
        out.write_text(json.dumps({"summary": {}, "results": results}))
        return subprocess.CompletedProcess(cmd, 0, stdout="", stderr="")
    return fake


class TestRunBatchScan:
    def test_splits_combined_output_into_per_skill_files(self, tmp_path):
        repo = tmp_path / "repo"
        a, b = repo / "skills" / "a", repo / "skills" / "b"
        for d in (a, b):
            d.mkdir(parents=True)
            (d / "SKILL.md").write_text("x")
        out = tmp_path / "results"
        finding = {"severity": "HIGH", "category": "command_injection", "title": "Pipe | to shell", "file_path": "run.sh", "line_number": 4}
        results = [_result(a, "a"), _result(b, "b", [finding])]
        with patch("run_scans.subprocess.run", side_effect=_fake_scan_all(results)), \
             patch("run_scans.get_scanner_version", return_value="2.3.1"):
            got = run_batch_scan(repo, out, {a: "skills-a", b: "skills-b"})

        assert set(got) == {"skills-a", "skills-b"}
        saved = json.loads((out / "skills-b-scan.json").read_text())
        assert saved["scanner_version"] == "2.3.1" and saved["findings_count"] == 1
        md = (out / "skills-b-scan.md").read_text()
        assert "ISSUES FOUND" in md and "Pipe \\| to shell" in md and "run.sh:4" in md
        assert "SAFE" in (out / "skills-a-scan.md").read_text()
        assert not (out / ".scan-all-combined.json").exists()

    def test_missing_skill_is_reported_not_invented(self, tmp_path):
        repo = tmp_path / "repo"
        a, b = repo / "a", repo / "b"
        for d in (a, b):
            d.mkdir(parents=True)
        with patch("run_scans.subprocess.run", side_effect=_fake_scan_all([_result(a, "a")])), \
             patch("run_scans.get_scanner_version", return_value="x"):
            got = run_batch_scan(repo, tmp_path / "out", {a: "a", b: "b"})
        assert set(got) == {"a"}

    def test_unexpected_path_is_skipped(self, tmp_path):
        repo = tmp_path / "repo"
        a = repo / "a"
        a.mkdir(parents=True)
        stray = _result(tmp_path / "elsewhere", "stray")
        with patch("run_scans.subprocess.run", side_effect=_fake_scan_all([stray])), \
             patch("run_scans.get_scanner_version", return_value="x"):
            got = run_batch_scan(repo, tmp_path / "out", {a: "a"})
        assert got == {}

    def test_nonzero_exit_returns_none(self, tmp_path):
        with patch("run_scans.subprocess.run", return_value=subprocess.CompletedProcess([], 2, "", "boom")):
            assert run_batch_scan(tmp_path, tmp_path / "out", {tmp_path / "a": "a"}) is None

    def test_timeout_returns_none(self, tmp_path):
        with patch("run_scans.subprocess.run", side_effect=subprocess.TimeoutExpired("x", 1)):
            assert run_batch_scan(tmp_path, tmp_path / "out", {tmp_path / "a": "a"}) is None

    def test_missing_scanner_returns_none(self, tmp_path):
        with patch("run_scans.subprocess.run", side_effect=FileNotFoundError):
            assert run_batch_scan(tmp_path, tmp_path / "out", {tmp_path / "a": "a"}) is None


def test_write_markdown_summary_no_findings(tmp_path):
    md = tmp_path / "x.md"
    write_markdown_summary({"skill_name": "s", "is_safe": True, "findings_count": 0, "analyzers_used": []}, md)
    text = md.read_text()
    assert "# Scan: s" in text and "SAFE" in text and "## Findings" not in text


class TestCommunityScanUsesBatch:
    def _repo(self, tmp_path, n):
        skills_dir = tmp_path / "skills"
        repo_dir = skills_dir / "owner-repo"
        paths = []
        for i in range(n):
            d = repo_dir / "skills" / f"s{i}"
            d.mkdir(parents=True)
            (d / "SKILL.md").write_text("x")
            paths.append(d)
        return skills_dir, repo_dir, paths

    @patch("community_scan.run_scan")
    @patch("community_scan.run_batch_scan")
    @patch("community_scan.clone_repo", return_value=True)
    def test_batch_used_and_per_skill_not_called(self, _clone, mock_batch, mock_scan, tmp_path):
        skills_dir, repo_dir, paths = self._repo(tmp_path, 3)
        mock_batch.return_value = {f"skills-s{i}": _result(p, f"s{i}") for i, p in enumerate(paths)}
        results = run_community_scan("owner/repo", skills_dir, tmp_path / "out")
        assert len(results) == 3 and all(r["is_safe"] for r in results)
        mock_scan.assert_not_called()
        names = mock_batch.call_args.kwargs["names"]
        assert set(names.values()) == {"skills-s0", "skills-s1", "skills-s2"}

    @patch("community_scan.run_scan")
    @patch("community_scan.run_batch_scan", return_value=None)
    @patch("community_scan.clone_repo", return_value=True)
    def test_falls_back_to_per_skill_when_batch_fails(self, _clone, _batch, mock_scan, tmp_path):
        skills_dir, repo_dir, paths = self._repo(tmp_path, 2)
        mock_scan.side_effect = [_result(paths[0], "s0"), None]
        results = run_community_scan("owner/repo", skills_dir, tmp_path / "out")
        assert mock_scan.call_count == 2
        assert results[0]["is_safe"] is True
        assert results[1]["is_safe"] is None and results[1]["error"] == "Scan failed"

    @patch("community_scan.run_scan")
    @patch("community_scan.run_batch_scan")
    @patch("community_scan.clone_repo", return_value=True)
    def test_skill_missing_from_batch_is_an_error_row(self, _clone, mock_batch, mock_scan, tmp_path):
        skills_dir, repo_dir, paths = self._repo(tmp_path, 2)
        mock_batch.return_value = {"skills-s0": _result(paths[0], "s0")}
        results = run_community_scan("owner/repo", skills_dir, tmp_path / "out")
        mock_scan.assert_not_called()
        assert [r.get("is_safe") for r in results] == [True, None]


class TestOriginStamping:
    def test_batch_scan_records_origin(self, tmp_path):
        repo = tmp_path / "repo"
        a = repo / "a"
        a.mkdir(parents=True)
        origin = {"source": "K-Dense-AI", "repo_url": "https://github.com/K-Dense-AI/scientific-agent-skills"}
        with patch("run_scans.subprocess.run", side_effect=_fake_scan_all([_result(a, "a")])), \
             patch("run_scans.get_scanner_version", return_value="2.3.1"):
            got = run_batch_scan(repo, tmp_path / "out", {a: "a"}, origin=origin)
        saved = json.loads((tmp_path / "out" / "a-scan.json").read_text())
        assert got["a"]["source"] == "K-Dense-AI"
        assert saved["repo_url"] == origin["repo_url"]

    @patch("community_scan.run_batch_scan")
    @patch("community_scan.clone_repo", return_value=True)
    def test_community_scan_passes_owner_as_origin(self, _clone, mock_batch, tmp_path):
        skills_dir = tmp_path / "skills"
        d = skills_dir / "K-Dense-AI-scientific-agent-skills" / "skills" / "x"
        d.mkdir(parents=True)
        (d / "SKILL.md").write_text("x")
        mock_batch.return_value = {"skills-x": _result(d, "x")}
        run_community_scan("K-Dense-AI/scientific-agent-skills", skills_dir, tmp_path / "out")
        origin = mock_batch.call_args.kwargs["origin"]
        assert origin == {"source": "K-Dense-AI", "repo_url": "https://github.com/K-Dense-AI/scientific-agent-skills"}

    def test_report_prefers_recorded_origin_over_path_heuristic(self, tmp_path):
        from generate_report import aggregate_results
        results = tmp_path / "results"
        results.mkdir()
        base = {"skill_name": "x", "is_safe": True, "max_severity": "SAFE", "findings_count": 0, "findings": [],
                "analyzers_used": [], "timestamp": "2026-10-21T00:00:00",
                "skill_path": "/workspace/skills/K-Dense-AI-scientific-agent-skills/skills/x"}
        (results / "guessed-scan.json").write_text(json.dumps(base))
        (results / "recorded-scan.json").write_text(json.dumps({**base, "skill_name": "y", "source": "K-Dense-AI",
                                                                 "repo_url": "https://github.com/K-Dense-AI/scientific-agent-skills"}))
        skills = {s["name"]: s for s in aggregate_results(results)["skills"]}
        assert skills["x"]["source"] == "K"  # the heuristic, kept for old results
        assert skills["y"]["source"] == "K-Dense-AI"
        assert skills["y"]["repo_url"].endswith("K-Dense-AI/scientific-agent-skills")
