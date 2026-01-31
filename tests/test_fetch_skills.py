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
