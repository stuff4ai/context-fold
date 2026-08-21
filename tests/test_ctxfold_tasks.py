# Copyright 2026-present The context-fold Authors
# SPDX-License-Identifier: Apache-2.0

"""Behavioral tests for the bundled `ctxfold-tasks` query helper.

`tests/test_conventions.py` checks that this repository's task packages are well-formed; this
file checks that `skills/ctxfold-tasks/query_tasks.py` discovers, groups, and reports on task
packages correctly, including packages this repository does not currently have (a conflict, a
terminal-status tie, a malformed package, a missing worktree).
"""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

from test_conventions import task_metadata

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "skills" / "ctxfold-tasks" / "query_tasks.py"

_dont_write_bytecode = sys.dont_write_bytecode
sys.dont_write_bytecode = True  # importing from skills/ must not leave __pycache__ behind there
try:
    spec = importlib.util.spec_from_file_location("query_tasks", SCRIPT)
    query_tasks = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = query_tasks
    spec.loader.exec_module(query_tasks)
finally:
    sys.dont_write_bytecode = _dont_write_bytecode


def _write_task(root: Path, slug: str, status: str, objective: str = "Do the thing.", title: str | None = None) -> Path:
    task_dir = root / ".agents" / "tasks" / slug
    task_dir.mkdir(parents=True)
    (task_dir / "task.md").write_text(
        f"---\nstatus: {status}\nobjective: >-\n  {objective}\n---\n\n# {title or slug}\n",
        encoding="utf-8",
    )
    (task_dir / "context.md").write_text("# Context\n", encoding="utf-8")
    return task_dir


def _write_archived_task(
    root: Path, archive_dir_name: str, status: str, objective: str = "Done.", title: str | None = None
) -> Path:
    task_dir = root / ".agents" / "tasks" / "archive" / archive_dir_name
    task_dir.mkdir(parents=True)
    slug = archive_dir_name[16:]
    (task_dir / "task.md").write_text(
        f"---\nstatus: {status}\nobjective: >-\n  {objective}\n---\n\n# {title or slug}\n",
        encoding="utf-8",
    )
    return task_dir


# --- Frontmatter decoding stays in lockstep with tests/test_conventions.py ------------


@pytest.mark.parametrize(
    "text",
    [
        "---\nstatus: active\nobjective: >-\n  Work.\n---\n\n# Case\n",
        "preamble\n---\nstatus: active\nobjective: >-\n  Work.\n---\n\n# Case\n",
        "---\nobjective: >-\n  Work.\nstatus: active\n---\n\n# Case\n",
        "---\nstatus: unknown\nobjective: >-\n  Work.\n---\n\n# Case\n",
        "---\nstatus: active\nobjective: >-\n---\n\n# Case\n",
        "---\r\nstatus: active\r\nobjective: >-\r\n  Work.\r\n---\r\n\r\n# Case\r\n",
        "---\nstatus: active\nobjective: >-\n  Work.\n---\n# Case\n",
        "---\nstatus: active\nobjective: >-\n  Work.\n---\n\nCase\n",
        "---\nstatus: active\nobjective: >-\n  Work.\n---\n\n# Case\n\n## Status\n\nactive\n",
    ],
)
def test_decode_task_md_matches_task_metadata_acceptance(text: str) -> None:
    """query_tasks.decode_task_md accepts and rejects the same inputs as task_metadata."""
    try:
        expected_status, expected_objective = task_metadata(text)
        expected_ok = True
    except ValueError:
        expected_ok = False

    try:
        status, objective, _title = query_tasks.decode_task_md(text)
        actual_ok = True
    except ValueError:
        actual_ok = False

    assert actual_ok == expected_ok, f"acceptance diverged for: {text!r}"
    if expected_ok:
        assert (status, objective) == (expected_status, expected_objective)


def test_decode_task_md_extracts_title() -> None:
    text = "---\nstatus: active\nobjective: >-\n  Work.\n---\n\n# A title line\n"
    assert query_tasks.decode_task_md(text) == ("active", "Work.", "A title line")


# --- Discovery and grouping -------------------------------------------------------------


def test_unfinished_view_returns_only_planned_and_active(tmp_path: Path) -> None:
    _write_task(tmp_path, "one", "planned")
    _write_task(tmp_path, "two", "active")
    _write_archived_task(tmp_path, "2026-01-01-0000-three", "completed")
    (tmp_path / ".git").mkdir()

    result = query_tasks.run(tmp_path, "unfinished")

    slugs = {t["slug"] for t in result["tasks"]}
    assert slugs == {"one", "two"}
    assert result["diagnostics"] == []


def test_archive_view_returns_only_terminal_statuses(tmp_path: Path) -> None:
    _write_task(tmp_path, "one", "planned")
    _write_archived_task(tmp_path, "2026-01-01-0000-two", "completed")
    _write_archived_task(tmp_path, "2026-01-02-0000-three", "cancelled")

    result = query_tasks.run(tmp_path, "archive")

    slugs = {t["slug"] for t in result["tasks"]}
    assert slugs == {"two", "three"}


def test_malformed_task_becomes_a_diagnostic_and_is_excluded(tmp_path: Path) -> None:
    good = _write_task(tmp_path, "good", "planned")
    bad_dir = tmp_path / ".agents" / "tasks" / "bad"
    bad_dir.mkdir(parents=True)
    (bad_dir / "task.md").write_text("not frontmatter at all\n", encoding="utf-8")

    result = query_tasks.run(tmp_path, "all")

    slugs = {t["slug"] for t in result["tasks"]}
    assert slugs == {"good"}
    assert good.exists()
    malformed = [d for d in result["diagnostics"] if d["type"] == "malformed_task"]
    assert len(malformed) == 1
    assert malformed[0]["path"] == ".agents/tasks/bad"


def test_worktree_is_scanned_and_merges_matching_sources(tmp_path: Path) -> None:
    _write_task(tmp_path, "shared", "planned")
    wt_root = tmp_path / ".agents" / "worktrees" / "wt"
    _write_task(wt_root, "shared", "planned")

    result = query_tasks.run(tmp_path, "unfinished")

    entries = [t for t in result["tasks"] if t["slug"] == "shared"]
    assert len(entries) == 1
    assert entries[0]["conflict"] is False
    assert sorted(entries[0]["sources"]) == [
        ".agents/tasks/shared",
        ".agents/worktrees/wt/.agents/tasks/shared",
    ]


def test_missing_worktree_becomes_a_diagnostic(tmp_path: Path) -> None:
    (tmp_path / ".agents" / "tasks").mkdir(parents=True)
    (tmp_path / ".agents" / "worktrees" / "empty").mkdir(parents=True)

    result = query_tasks.run(tmp_path, "all")

    diags = [d for d in result["diagnostics"] if d["type"] == "missing_worktree"]
    assert diags == [
        {
            "type": "missing_worktree",
            "path": ".agents/worktrees/empty",
            "detail": "no .agents/tasks in this registered worktree",
        }
    ]


def test_same_status_conflict_keeps_every_observation(tmp_path: Path) -> None:
    _write_task(tmp_path, "disputed", "active", objective="Root version.")
    wt_root = tmp_path / ".agents" / "worktrees" / "wt"
    _write_task(wt_root, "disputed", "active", objective="Worktree version.")

    result = query_tasks.run(tmp_path, "unfinished")

    entry = next(t for t in result["tasks"] if t["slug"] == "disputed")
    assert entry["conflict"] is True
    assert entry["tie_broken"] is False
    observed_objectives = {o["objective"] for o in entry["observations"]}
    assert observed_objectives == {"Root version.", "Worktree version."}
    assert any(d["type"] == "conflict" and d["slug"] == "disputed" for d in result["diagnostics"])


def test_more_advanced_status_wins_without_conflict(tmp_path: Path) -> None:
    _write_task(tmp_path, "graduated", "planned", objective="Stale planned copy.")
    wt_root = tmp_path / ".agents" / "worktrees" / "wt"
    _write_archived_task(wt_root, "2026-01-01-0000-graduated", "completed", objective="Actually done.")

    result = query_tasks.run(tmp_path, "all")

    entry = next(t for t in result["tasks"] if t["slug"] == "graduated")
    assert entry["status"] == "completed"
    assert entry["conflict"] is False


def test_terminal_tie_is_broken_by_later_archive_timestamp(tmp_path: Path) -> None:
    _write_archived_task(tmp_path, "2026-01-01-0000-tied", "completed", objective="Earlier.")
    wt_root = tmp_path / ".agents" / "worktrees" / "wt"
    _write_archived_task(wt_root, "2026-06-01-0000-tied", "completed", objective="Later.")

    result = query_tasks.run(tmp_path, "archive")

    entry = next(t for t in result["tasks"] if t["slug"] == "tied")
    assert entry["tie_broken"] is True
    assert entry["objective"] == "Later."
    assert any(d["type"] == "terminal_tie" and d["slug"] == "tied" for d in result["diagnostics"])


# --- CLI surface -------------------------------------------------------------------------


def test_cli_reports_json_and_exits_zero(tmp_path: Path) -> None:
    _write_task(tmp_path, "one", "planned")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), "unfinished"],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0
    payload = json.loads(proc.stdout)
    assert [t["slug"] for t in payload["tasks"]] == ["one"]


def test_cli_outside_a_repository_exits_nonzero_with_json_error(tmp_path: Path) -> None:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode != 0
    payload = json.loads(proc.stdout)
    assert "error" in payload


def test_cli_rejects_unknown_view(tmp_path: Path) -> None:
    (tmp_path / ".agents" / "tasks").mkdir(parents=True)
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), "bogus"],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode != 0
    payload = json.loads(proc.stdout)
    assert "error" in payload
