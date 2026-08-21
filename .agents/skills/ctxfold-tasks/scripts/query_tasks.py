#!/usr/bin/env python3
# Copyright 2026-present The context-fold Authors
# SPDX-License-Identifier: Apache-2.0

"""Discover context-fold task packages across a repository and its registered worktrees.

Reads task frontmatter directly; it is not a cache and never writes anything. The frontmatter
contract mirrors decision 0037 (`status`/`objective`, strict LF frontmatter, folded objective) so
that this script and the repository's own convention checks can never quietly disagree about what
counts as a valid task package.

Usage: query_tasks.py [unfinished|archive|all]

Prints one JSON object to stdout: {"tasks": [...], "diagnostics": [...]}. Exit code is 0 whenever
the query ran, even when diagnostics are present; a non-zero exit means the query could not run at
all (for example, invoked outside a context-fold repository).
"""

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

TASK_FRONTMATTER = re.compile(
    r"\A---\n"
    r"status: (?P<status>planned|active|completed|cancelled)\n"
    r"objective: >-\n"
    r"(?P<objective>(?:  \S(?:[^\n]*\S)?\n)+)"
    r"---\n\n"
    r"# (?P<title>\S(?:[^\n]*\S)?)\n"
)
ARCHIVE_DIR = re.compile(r"^(?P<ts>\d{4}-\d{2}-\d{2}-\d{4})-(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)$")

RANK = {"planned": 0, "active": 1, "completed": 2, "cancelled": 2}
TERMINAL_RANK = 2
VIEWS = {
    "unfinished": {"planned", "active"},
    "archive": {"completed", "cancelled"},
    "all": {"planned", "active", "completed", "cancelled"},
}


@dataclass(frozen=True)
class Observation:
    slug: str
    status: str
    objective: str
    title: str
    path: str  # forward-slash, relative to the invoking repository root
    archive_ts: str | None  # set only for archived observations


def find_repo_root(start: Path) -> Path:
    """Nearest ancestor of `start` that owns a `.agents/tasks` directory."""
    for candidate in (start, *start.parents):
        if (candidate / ".agents" / "tasks").is_dir():
            return candidate
    raise SystemExit("not inside a context-fold repository (no .agents/tasks found)")


def decode_task_md(text: str) -> tuple[str, str, str]:
    """Strict task frontmatter plus title: mirrors decision 0037's `status`/`objective` contract.

    Returns (status, objective, title); raises ValueError on anything noncanonical. Only the
    frontmatter-and-title prefix matters here — this is a discovery tool, not the certification
    `tests/test_conventions.py` already owns for the repository's accepted task packages.
    """
    match = TASK_FRONTMATTER.match(text)
    if not match:
        raise ValueError("task.md does not start with exact status/objective frontmatter")

    objective = " ".join(line[2:] for line in match.group("objective").splitlines())
    return match.group("status"), objective, match.group("title")


def parse_task(task_dir: Path, invoking_root: Path, archive_ts: str | None) -> Observation:
    task_md = task_dir / "task.md"
    if not task_md.is_file():
        raise ValueError("missing task.md")

    status, objective, title = decode_task_md(task_md.read_text(encoding="utf-8"))
    rel_path = task_dir.relative_to(invoking_root).as_posix()
    return Observation(
        slug=task_dir.name if archive_ts is None else task_dir.name[len(archive_ts) + 1 :],
        status=status,
        objective=objective,
        title=title,
        path=rel_path,
        archive_ts=archive_ts,
    )


def gather(tasks_root: Path, invoking_root: Path) -> tuple[list[Observation], list[dict]]:
    """Scan one `.agents/tasks` directory (unfinished children plus `archive/`)."""
    observations: list[Observation] = []
    diagnostics: list[dict] = []

    if not tasks_root.is_dir():
        return observations, diagnostics

    for child in sorted(p for p in tasks_root.iterdir() if p.is_dir() and p.name != "archive"):
        try:
            observations.append(parse_task(child, invoking_root, archive_ts=None))
        except ValueError as exc:
            diagnostics.append(
                {
                    "type": "malformed_task",
                    "path": child.relative_to(invoking_root).as_posix(),
                    "detail": str(exc),
                }
            )

    archive_root = tasks_root / "archive"
    if archive_root.is_dir():
        for child in sorted(p for p in archive_root.iterdir() if p.is_dir()):
            archive_match = ARCHIVE_DIR.match(child.name)
            ts = archive_match.group("ts") if archive_match else None
            try:
                observations.append(parse_task(child, invoking_root, archive_ts=ts))
            except ValueError as exc:
                diagnostics.append(
                    {
                        "type": "malformed_task",
                        "path": child.relative_to(invoking_root).as_posix(),
                        "detail": str(exc),
                    }
                )

    return observations, diagnostics


def gather_worktrees(root: Path) -> tuple[list[Observation], list[dict]]:
    """Scan every `.agents/worktrees/*` directory as a registered nested checkout."""
    observations: list[Observation] = []
    diagnostics: list[dict] = []

    worktrees_root = root / ".agents" / "worktrees"
    if not worktrees_root.is_dir():
        return observations, diagnostics

    for child in sorted(p for p in worktrees_root.iterdir() if p.is_dir()):
        nested_tasks = child / ".agents" / "tasks"
        if not nested_tasks.is_dir():
            diagnostics.append(
                {
                    "type": "missing_worktree",
                    "path": child.relative_to(root).as_posix(),
                    "detail": "no .agents/tasks in this registered worktree",
                }
            )
            continue
        obs, diags = gather(nested_tasks, root)
        observations.extend(obs)
        diagnostics.extend(diags)

    return observations, diagnostics


def build_entries(observations: list[Observation]) -> tuple[list[dict], list[dict]]:
    by_slug: dict[str, list[Observation]] = {}
    for obs in observations:
        by_slug.setdefault(obs.slug, []).append(obs)

    entries: list[dict] = []
    diagnostics: list[dict] = []

    for slug in sorted(by_slug):
        obs_list = by_slug[slug]
        max_rank = max(RANK[o.status] for o in obs_list)
        winners = [o for o in obs_list if RANK[o.status] == max_rank]

        tie_broken = False
        if max_rank == TERMINAL_RANK and len(winners) > 1:
            winners_by_ts = sorted(winners, key=lambda o: (o.archive_ts or "", o.path), reverse=True)
            selected = winners_by_ts[0]
            if len({(o.status, o.objective, o.title) for o in winners}) > 1:
                tie_broken = True
                diagnostics.append(
                    {
                        "type": "terminal_tie",
                        "slug": slug,
                        "selected": selected.path,
                        "candidates": sorted(o.path for o in winners),
                    }
                )
        else:
            selected = sorted(winners, key=lambda o: o.path)[0]

        conflict = len({(o.status, o.objective, o.title) for o in winners}) > 1
        if conflict:
            diagnostics.append(
                {
                    "type": "conflict",
                    "slug": slug,
                    "paths": sorted(o.path for o in winners),
                }
            )

        entry = {
            "slug": slug,
            "status": selected.status,
            "objective": selected.objective,
            "title": selected.title,
            "sources": sorted(o.path for o in obs_list),
            "conflict": conflict,
            "tie_broken": tie_broken,
        }
        if conflict:
            entry["observations"] = [
                {"path": o.path, "status": o.status, "objective": o.objective, "title": o.title}
                for o in sorted(winners, key=lambda o: o.path)
            ]
        entries.append(entry)

    return entries, diagnostics


def run(root: Path, view: str) -> dict:
    observations, diagnostics = gather(root / ".agents" / "tasks", root)
    wt_observations, wt_diagnostics = gather_worktrees(root)
    observations += wt_observations
    diagnostics += wt_diagnostics

    entries, grouping_diagnostics = build_entries(observations)
    diagnostics += grouping_diagnostics

    allowed = VIEWS[view]
    tasks = [e for e in entries if e["status"] in allowed]
    tasks.sort(key=lambda e: e["slug"])
    diagnostics.sort(key=lambda d: (d["type"], d.get("slug", ""), d.get("path", "")))

    return {"tasks": tasks, "diagnostics": diagnostics}


def main(argv: list[str]) -> int:
    view = argv[0] if argv else "unfinished"
    if view not in VIEWS:
        print(json.dumps({"error": f"unknown view {view!r}; expected one of {sorted(VIEWS)}"}))
        return 1

    try:
        root = find_repo_root(Path.cwd())
    except SystemExit as exc:
        print(json.dumps({"error": str(exc)}))
        return 1

    print(json.dumps(run(root, view), indent=2, sort_keys=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
