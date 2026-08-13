# Copyright 2026-present The context-fold Authors
# SPDX-License-Identifier: Apache-2.0

"""Checks for the repository conventions.

Every check here encodes a decision record. When a decision changes, the check that
encodes it changes with it — the record is the specification, this file is not.

A passing suite proves the structure holds. It says nothing about whether the prose
is correct, consistent with what is already decided, or worth reading.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent

TASKS = ROOT / ".agents" / "tasks"
ARCHIVE = TASKS / "archive"
INDEX = TASKS / "INDEX.md"
DECISIONS = ROOT / "decisions"
DECISIONS_INDEX = DECISIONS / "README.md"

# The rule files shipped to every project using context-fold (0005, 0011).
PORTABLE = [
    ROOT / ".agents" / "AGENTS.md",
    TASKS / "AGENTS.md",
    ARCHIVE / "AGENTS.md",
]

ARCHIVE_DIR = re.compile(r"^\d{4}-\d{2}-\d{2}-\d{4}-[a-z0-9]+(?:-[a-z0-9]+)*$")
RECORD_FILE = re.compile(r"^(\d{4})-[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

# [text](target) — not images, not autolinks.
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


IGNORED_DIRS = {".git", ".venv", ".idea", ".vscode"}


def markdown_files() -> list[Path]:
    """Every document in the repository.

    Hidden files are skipped: `.adr-template.md` is a skeleton whose headings are
    placeholders and whose links point at names that do not exist. Checking it would be
    checking the shape of a form. Hidden *directories* are still walked — `.agents/` is
    where half the repository lives.
    """
    return sorted(
        p
        for p in ROOT.rglob("*.md")
        if not IGNORED_DIRS.intersection(p.parts) and not p.name.startswith(".")
    )


def archived_tasks() -> list[Path]:
    return sorted(p for p in ARCHIVE.iterdir() if p.is_dir())


def active_tasks() -> list[Path]:
    return sorted(p for p in TASKS.iterdir() if p.is_dir() and p.name != "archive")


def records() -> list[Path]:
    """The decision records. Not the index, and not the template."""
    return sorted(
        p
        for p in DECISIONS.glob("*.md")
        if p.name != "README.md" and not p.name.startswith(".")
    )


def section(text: str, heading: str) -> str | None:
    """Body of a level-2 section, or None when it is absent."""
    match = re.search(rf"^## {re.escape(heading)}\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    return match.group(1).strip() if match else None


def status_of(task: Path) -> str | None:
    return section((task / "task.md").read_text(encoding="utf-8"), "Status")


# --- Discovery ------------------------------------------------------------------------


def test_discovery_finds_content() -> None:
    """A helper returning nothing makes its checks vanish rather than fail.

    Parametrizing over an empty list skips silently, so a broken finder reads as green.
    Active tasks are legitimately empty between tasks and are not asserted here.
    """
    assert records(), "no decision records found"
    assert archived_tasks(), "no archived tasks found"
    assert len(markdown_files()) > 20, "markdown discovery found suspiciously little"
    assert all(p.is_file() for p in PORTABLE), "a portable rule file is missing"


# --- Task packages (0006) -------------------------------------------------------------


@pytest.mark.parametrize("task", archived_tasks() + active_tasks(), ids=lambda p: p.name)
def test_task_package_has_required_files(task: Path) -> None:
    """0006: a package is task.md and context.md; plan.md is optional."""
    for required in ("task.md", "context.md"):
        assert (task / required).is_file(), f"{task.name} is missing {required}"


@pytest.mark.parametrize("task", archived_tasks(), ids=lambda p: p.name)
def test_archived_task_is_finished(task: Path) -> None:
    """0006, 0007: archival requires a final status and an outcome."""
    status = status_of(task)
    assert status in {"completed", "cancelled"}, (
        f"{task.name} is archived with status {status!r}; "
        "archived tasks are completed or cancelled"
    )
    text = (task / "task.md").read_text(encoding="utf-8")
    assert section(text, "Outcome"), f"{task.name} is archived without an Outcome section"


@pytest.mark.parametrize("task", active_tasks(), ids=lambda p: p.name)
def test_active_task_is_unfinished(task: Path) -> None:
    """0006: an outcome is written at archival, so active tasks do not have one."""
    status = status_of(task)
    assert status in {"planned", "active"}, (
        f"{task.name} is not archived but has status {status!r}"
    )
    text = (task / "task.md").read_text(encoding="utf-8")
    assert not section(text, "Outcome"), (
        f"{task.name} has an Outcome but is still in the active directory"
    )


@pytest.mark.parametrize("task", archived_tasks(), ids=lambda p: p.name)
def test_archive_directory_is_named_correctly(task: Path) -> None:
    """0007, 0009: {YYYY-MM-DD-HHMM}-{slug}, so the sort orders by recency."""
    assert ARCHIVE_DIR.match(task.name), (
        f"{task.name} does not match {{YYYY-MM-DD-HHMM}}-{{slug}}"
    )


@pytest.mark.parametrize("task", active_tasks(), ids=lambda p: p.name)
def test_active_directory_is_a_bare_slug(task: Path) -> None:
    """0006: the slug is stable identity; the timestamp is added at archival."""
    assert SLUG.match(task.name), f"{task.name} is not a lowercase hyphenated slug"


# --- Task index (0009) ----------------------------------------------------------------


def index_rows(heading: str) -> list[str]:
    """Task directory names linked from one section of the index, in order."""
    body = section(INDEX.read_text(encoding="utf-8"), heading) or ""
    return [m.group(1) for m in re.finditer(r"\]\((?:archive/)?([^/)]+)/task\.md\)", body)]


def test_index_archive_matches_disk() -> None:
    """0009: newest first, which is directory name descending."""
    assert index_rows("Archive") == [p.name for p in sorted(archived_tasks(), reverse=True)]


def test_index_active_matches_disk() -> None:
    """0009: active tasks sort by slug ascending; the order carries no meaning."""
    assert index_rows("Active") == [p.name for p in active_tasks()]


# --- Decision records (0000) ----------------------------------------------------------


@pytest.mark.parametrize("record", records(), ids=lambda p: p.name)
def test_record_has_required_sections(record: Path) -> None:
    """0000: the Nygard template."""
    text = record.read_text(encoding="utf-8")
    for heading in ("Status", "Context", "Decision", "Consequences"):
        assert section(text, heading), f"{record.name} has no {heading} section"


@pytest.mark.parametrize("record", records(), ids=lambda p: p.name)
def test_record_filename_is_well_formed(record: Path) -> None:
    assert RECORD_FILE.match(record.name), (
        f"{record.name} does not match NNNN-slug.md"
    )


def test_record_numbering_is_contiguous_and_unique() -> None:
    """0000: four-digit prefixes, never renumbered, so gaps mean a lost record."""
    numbers = [int(RECORD_FILE.match(p.name).group(1)) for p in records()]
    assert numbers == sorted(numbers)
    assert len(set(numbers)) == len(numbers), "duplicate record numbers"
    assert numbers == list(range(len(numbers))), f"gap in record numbering: {numbers}"


def test_decision_index_lists_every_record() -> None:
    """0000: the index is how records are found; an unlisted record is invisible."""
    listed = set(re.findall(r"\]\((\d{4}-[a-z0-9-]+\.md)\)", DECISIONS_INDEX.read_text("utf-8")))
    on_disk = {p.name for p in records()}
    assert listed == on_disk, (
        f"unlisted: {sorted(on_disk - listed)}; listed but absent: {sorted(listed - on_disk)}"
    )


# --- Portability (0005, 0011) ---------------------------------------------------------


@pytest.mark.parametrize("rules", PORTABLE, ids=lambda p: str(p.relative_to(ROOT)))
def test_portable_rules_carry_no_project_detail(rules: Path) -> None:
    """0005, 0011: these files are identical in every project using context-fold.

    A record number, a path to this repository's documents, or one of its task slugs
    would be wrong in any other repository — and would read correctly here, which is
    why this is checked rather than reviewed.
    """
    text = rules.read_text(encoding="utf-8")
    slugs = {p.name.split("-", 4)[-1] for p in archived_tasks()} | {
        p.name for p in active_tasks()
    }
    offenders = []
    if re.search(r"\b\d{4}-[a-z0-9-]+\.md\b", text):
        offenders.append("a decision record filename")
    if "decisions/" in text:
        offenders.append("a path into this repository's decisions")
    for slug in slugs:
        if slug in text:
            offenders.append(f"the task slug {slug!r}")
    assert not offenders, f"{rules.name} contains {', '.join(offenders)}"


# --- Links ----------------------------------------------------------------------------


@pytest.mark.parametrize("doc", markdown_files(), ids=lambda p: str(p.relative_to(ROOT)))
def test_relative_links_resolve(doc: Path) -> None:
    """External URLs are not checked: they are few, stable, and flaky in CI."""
    broken = []
    for target in LINK.findall(doc.read_text(encoding="utf-8")):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        path = (doc.parent / target.split("#", 1)[0]).resolve()
        if not path.exists():
            broken.append(target)
    assert not broken, f"{doc.relative_to(ROOT)} links to missing: {broken}"
