"""Tests for scripts/fetch_skills.py"""

import json
from pathlib import Path

import pytest

from fetch_skills import save_inventory, load_inventory, VALID_SOURCES


class TestValidSources:
    def test_contains_skillssh(self):
        assert "skills.sh" in VALID_SOURCES

    def test_contains_clawhub(self):
        assert "clawhub" in VALID_SOURCES


class TestInventoryRoundTrip:
    def test_save_and_load(self, tmp_path, sample_skill_list):
        path = tmp_path / "inventory.json"
        save_inventory(sample_skill_list, path)

        loaded = load_inventory(path)
        assert len(loaded) == len(sample_skill_list)
        assert loaded[0]["name"] == "skill-alpha"

    def test_save_creates_parent_dirs(self, tmp_path, sample_skill_list):
        path = tmp_path / "sub" / "dir" / "inventory.json"
        save_inventory(sample_skill_list, path)
        assert path.exists()

    def test_load_preserves_all_fields(self, tmp_path, sample_skill_list):
        path = tmp_path / "inventory.json"
        save_inventory(sample_skill_list, path)
        loaded = load_inventory(path)

        for original, loaded_item in zip(sample_skill_list, loaded):
            assert original["rank"] == loaded_item["rank"]
            assert original["name"] == loaded_item["name"]
            assert original["installs"] == loaded_item["installs"]
            assert original["source"] == loaded_item["source"]


# skills.sh rankings now come from the LinklyAI/best-skills CSV mirror.
from unittest.mock import MagicMock, patch  # noqa: E402
import fetch_skills  # noqa: E402


CSV = """view,rank,source,name,installs,is_official,installs_yesterday,change,weekly_installs
all-time,1,vercel-labs/skills,find-skills,3977808,true,,,1|2
all-time,2,mattpocock/skills,grill-me,1408491,false,,,1|2
all-time,3,vercel-labs/agent-browser,agent-browser,1206479,false,,,1|2
weekly,1,someone/else,ignored,99,false,,,1
"""


def _session(text):
    resp = MagicMock(text=text)
    resp.raise_for_status = MagicMock()
    sess = MagicMock()
    sess.get.return_value = resp
    return sess


def test_top_n_from_csv():
    with patch("fetch_skills.get_session", return_value=_session(CSV)):
        got = fetch_skills.fetch_top_skills(2)
    assert [g["name"] for g in got] == ["find-skills", "grill-me"]
    assert got[0] == {"rank": 1, "name": "find-skills", "id": "vercel-labs/skills/find-skills",
                      "repo": "vercel-labs/skills", "installs": 3977808, "source": "skills.sh"}


def test_offset_and_reverse():
    with patch("fetch_skills.get_session", return_value=_session(CSV)):
        off = fetch_skills.fetch_top_skills(5, offset=1)
        rev = fetch_skills.fetch_top_skills(1, reverse=True)
    assert [g["rank"] for g in off] == [2, 3] and off[0]["name"] == "grill-me"
    assert rev[0]["name"] == "agent-browser"  # weekly rows are excluded, so the least-installed all-time row wins


def test_requests_best_skills_mirror():
    sess = _session(CSV)
    with patch("fetch_skills.get_session", return_value=sess):
        fetch_skills.fetch_top_skills(1)
    url = sess.get.call_args.args[0]
    assert url.startswith(fetch_skills.BEST_SKILLS_BASE) and url.endswith("raw/skills-sh.csv")
