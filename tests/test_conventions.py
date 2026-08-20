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
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent

SKILLS = ROOT / "skills"
INIT_SKILL = SKILLS / "ctxfold-init"
TEMPLATES = INIT_SKILL / "templates"
AGENT_TEMPLATES = TEMPLATES / "agents"

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
    ROOT / ".agents" / "worktrees" / "AGENTS.md",
]

ARCHIVE_DIR = re.compile(r"^\d{4}-\d{2}-\d{2}-\d{4}-[a-z0-9]+(?:-[a-z0-9]+)*$")
RECORD_FILE = re.compile(r"^(\d{4})-[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

# [text](target) — not images, not autolinks.
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")

# Fenced blocks hold examples. A link inside one is a shape to copy, not a link to follow.
FENCE = re.compile(r"^```.*?^```", re.M | re.S)

# Inline code is quoted syntax, not a reference — writing *about* a link is not making one.
CODE_SPAN = re.compile(r"`[^`\n]*`")


def _visible_markdown() -> list[Path]:
    """Every Markdown file Git would consider part of the repository.

    Tracked files plus untracked ones Git does not ignore. Asking Git rather than
    keeping a list here means the suite and the linter agree about what the
    repository contains — the linter already runs with `--respect-gitignore`. It
    also keeps parallel checkouts under `.agents/worktrees/` out of the suite,
    which would otherwise read a second copy of every record as though it were
    this one.
    """
    out = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z", "*.md"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    return sorted(ROOT / name for name in out.stdout.split("\0") if name)


def markdown_files() -> list[Path]:
    """Every document in the repository.

    Hidden files are skipped: `.adr-template.md` is a skeleton whose headings are
    placeholders and whose links point at names that do not exist. Checking it would be
    checking the shape of a form. Hidden *directories* are still walked — `.agents/` is
    where half the repository lives.
    """
    return [p for p in _visible_markdown() if not p.name.startswith(".")]


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


# --- Shipped skills -------------------------------------------------------------------


def skills() -> list[Path]:
    return sorted(p for p in SKILLS.iterdir() if p.is_dir()) if SKILLS.is_dir() else []


@pytest.mark.parametrize("skill", skills(), ids=lambda p: p.name)
def test_skill_has_usable_frontmatter(skill: Path) -> None:
    """A skill without loadable frontmatter is not a skill, it is a document."""
    text = (skill / "SKILL.md").read_text(encoding="utf-8")
    front = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    assert front, f"{skill.name}/SKILL.md has no frontmatter block"

    name = re.search(r"^name:\s*(\S+)\s*$", front.group(1), re.M)
    assert name, f"{skill.name}/SKILL.md declares no name"
    assert name.group(1) == skill.name, (
        f"{skill.name}/SKILL.md is named {name.group(1)!r}; it would install under one name "
        "and answer to another"
    )
    assert re.search(r"^description:", front.group(1), re.M), (
        f"{skill.name}/SKILL.md has no description, so nothing can tell when to invoke it"
    )


@pytest.mark.parametrize("skill", skills(), ids=lambda p: p.name)
def test_skill_ships_no_stray_files(skill: Path) -> None:
    """Everything in the directory ships, including whatever was left there by accident.

    A backup or editor artifact reaches every installation and nothing else notices — the
    other checks only read the files they expect to find.
    """
    junk = [
        p.relative_to(skill)
        for p in skill.rglob("*")
        if p.is_file()
        and (
            p.suffix in {".bak", ".orig", ".rej", ".tmp", ".swp"}
            or p.name.endswith("~")
            or "__pycache__" in p.parts
        )
    ]
    assert not junk, f"{skill.name} would ship: {junk}"


@pytest.mark.parametrize("skill", skills(), ids=lambda p: p.name)
def test_skill_is_self_contained(skill: Path) -> None:
    """A skill directory is what an installer copies. Anything it points outside is lost.

    This is the portability check for shipped skills: a reference that resolves here and
    nowhere else reads correctly until the moment it matters.
    """
    escaping = []
    for doc in sorted(skill.rglob("*.md")):
        for target in LINK.findall(CODE_SPAN.sub("", FENCE.sub("", doc.read_text(encoding="utf-8")))):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            resolved = (doc.parent / target.split("#", 1)[0]).resolve()
            if not resolved.is_relative_to(skill.resolve()):
                escaping.append(f"{doc.relative_to(skill)} → {target}")
            elif not resolved.exists():
                escaping.append(f"{doc.relative_to(skill)} → {target} (missing)")
    assert not escaping, f"{skill.name} references outside its own directory: {escaping}"


def installed_skills() -> list[tuple[Path, Path]]:
    """Shipped skills that this repository has also installed for its own use."""
    return [
        (s, ROOT / ".agents" / "skills" / s.name)
        for s in skills()
        if (ROOT / ".agents" / "skills" / s.name).is_dir()
    ]


@pytest.mark.parametrize("shipped,installed", installed_skills(), ids=lambda p: p.name)
def test_installed_skill_matches_the_shipped_one(shipped: Path, installed: Path) -> None:
    """A skill this repository uses is the skill it distributes.

    The same rule as the layer, one directory over: an installation that drifts from its
    distribution is a claim to dogfood that has quietly stopped being true.
    """
    ship = {p.relative_to(shipped) for p in shipped.rglob("*") if p.is_file()}
    inst = {p.relative_to(installed) for p in installed.rglob("*") if p.is_file()}
    assert ship == inst, (
        f"{shipped.name}: installed but not shipped {sorted(inst - ship)}; "
        f"shipped but not installed {sorted(ship - inst)}"
    )
    differing = [f for f in sorted(ship) if (shipped / f).read_bytes() != (installed / f).read_bytes()]
    assert not differing, f"{shipped.name}: installed copy differs in {differing}"


# --- Dogfooding -----------------------------------------------------------------------


def installed_rule_files() -> list[tuple[Path, Path]]:
    """Everything in `templates/agents/`, paired with where it installs to.

    The directory holds only files that must stay byte-identical forever, so there is
    nothing to exclude. `INDEX.md` lives outside it precisely because it is copied once
    and then diverges.
    """
    return [
        (t, ROOT / ".agents" / t.relative_to(AGENT_TEMPLATES))
        for t in sorted(p for p in AGENT_TEMPLATES.rglob("*") if p.is_file())
    ]


@pytest.mark.parametrize(
    "template,installed",
    installed_rule_files(),
    ids=lambda p: str(p.relative_to(ROOT)) if isinstance(p, Path) else str(p),
)
def test_installation_matches_the_distribution(template: Path, installed: Path) -> None:
    """This repository runs what it ships.

    `templates/agents/` is the distribution; `.agents/` is one installation of it. If they
    differ, either the shipped rules were edited in place — which is what the layer tells
    adopters never to do — or a change was made to the distribution and not installed.
    """
    assert installed.is_file(), f"{installed.relative_to(ROOT)} is not installed"
    assert installed.read_bytes() == template.read_bytes(), (
        f"{installed.relative_to(ROOT)} differs from {template.relative_to(ROOT)}"
    )


def installed_layer_files() -> set[Path]:
    """Rule files belonging to the layer, which is not the whole of `.agents/`.

    `0018`: the layer is what was installed, and `.agents/` is only where it lives. Other
    tools write there — including a skill installer placing this project's own skill, whose
    bundled templates contain `AGENTS.md` files that are not part of any installation.
    """
    agents = ROOT / ".agents"
    found: set[Path] = set()
    for name in ("AGENTS.md", "tasks"):
        path = agents / name
        if path.is_file():
            found.add(path.relative_to(agents))
        elif path.is_dir():
            found |= {p.relative_to(agents) for p in path.rglob("AGENTS.md")}

    # `worktrees/` cannot use the `tasks`-style recursive glob: it also holds live worktree
    # checkouts (0025), each a full nested copy of this repository with its own nested
    # `AGENTS.md` files. `rglob` would descend into whichever happen to be checked out and
    # break the set comparison depending on what work is in progress when the suite runs.
    worktrees_agents = agents / "worktrees" / "AGENTS.md"
    if worktrees_agents.is_file():
        found.add(worktrees_agents.relative_to(agents))

    return found


def test_distribution_is_complete() -> None:
    """A rule file installed but not shipped would reach no other repository.

    Compares `AGENTS.md` files only. The installation also holds an index and task
    packages, which it produced rather than received.
    """
    shipped = {p.relative_to(AGENT_TEMPLATES) for p in AGENT_TEMPLATES.rglob("AGENTS.md")}
    installed = installed_layer_files()
    assert installed == shipped, (
        f"installed but not shipped: {sorted(installed - shipped)}; "
        f"shipped but not installed: {sorted(shipped - installed)}"
    )


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
    assert skills(), "no shipped skills found"
    assert installed_rule_files(), "the distribution shipped no rule files"


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


# --- Leftover scaffolding in a task package (0031) ------------------------------------


TASK_OPTIONAL_HEADINGS = ("Blocked by", "Approval")
CONTEXT_OPTIONAL_HEADINGS = (
    "Assumptions",
    "Open questions",
    "Context conflicts",
    "Base state",
    "Not relevant",
)


@pytest.mark.parametrize("task", archived_tasks(), ids=lambda p: p.name)
def test_archived_task_has_no_empty_optional_heading(task: Path) -> None:
    """0031: `## Assumptions` survived the `etu-forms` template run empty, because nothing
    marks an unfilled optional heading wrong on its own — only whether it was ever going to
    be filled, which archival settles. An optional heading still empty once the task is done
    was declared and never used; drop it rather than ship it hollow.

    Only archived tasks are checked: an active task may legitimately carry an optional
    heading it intends to fill before it is done.

    A duplicated heading is the other structural defect in the same `etu-forms` evidence, but
    it needs no check here: `.pymarkdown.json` already enables MD024 (`siblings_only`), which
    flags a heading repeated among its siblings in the same file — checked by the lint step
    0016 already runs in CI, not duplicated by this suite.
    """
    empty = []
    for name, optional in (
        ("task.md", TASK_OPTIONAL_HEADINGS),
        ("context.md", CONTEXT_OPTIONAL_HEADINGS),
    ):
        path = task / name
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for heading in optional:
            body = section(text, heading)
            if body is not None and not body.strip():
                empty.append(f"{name}#{heading}")
    assert not empty, f"{task.name} archived with empty optional heading(s): {empty}"


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
    """0005, 0011, 0018: these files are identical in every installation.

    A record number, a path to this repository's documents, or one of its task slugs
    would be wrong in any other repository — and would read correctly here, which is
    why this is checked rather than reviewed.

    The project name is excluded too. The rules describe the layer, and a set of rules
    naming its vendor is wrong for anyone who forks and maintains them. Where the layer
    came from is metadata, and metadata is not built yet.
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
    if "context-fold" in text:
        offenders.append("the name of the project that ships it")
    for slug in slugs:
        if slug in text:
            offenders.append(f"the task slug {slug!r}")
    assert not offenders, f"{rules.name} contains {', '.join(offenders)}"


# --- Links ----------------------------------------------------------------------------


@pytest.mark.parametrize("doc", markdown_files(), ids=lambda p: str(p.relative_to(ROOT)))
def test_relative_links_resolve(doc: Path) -> None:
    """External URLs are not checked: they are few, stable, and flaky in CI.

    Fenced blocks are stripped first. Documents that show the shape of a file contain
    links to placeholder paths, and those are examples rather than references.
    """
    broken = []
    for target in LINK.findall(CODE_SPAN.sub("", FENCE.sub("", doc.read_text(encoding="utf-8")))):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        path = (doc.parent / target.split("#", 1)[0]).resolve()
        if not path.exists():
            broken.append(target)
    assert not broken, f"{doc.relative_to(ROOT)} links to missing: {broken}"
