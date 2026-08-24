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
DECISIONS = ROOT / "decisions"
DECISIONS_INDEX = DECISIONS / "README.md"

# Files carrying the portable managed blocks in this installation (0005, 0011, 0035, 0041).
PORTABLE = [
    ROOT / ".agents" / "AGENTS.md",
    TASKS / "AGENTS.md",
    ARCHIVE / "AGENTS.md",
    ROOT / ".agents" / "skills" / "AGENTS.md",
    ROOT / ".agents" / "worktrees" / "AGENTS.md",
]

ARCHIVE_DIR = re.compile(r"^\d{4}-\d{2}-\d{2}-\d{4}-[a-z0-9]+(?:-[a-z0-9]+)*$")
RECORD_FILE = re.compile(r"^(\d{4})-[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
RFC_FRONTMATTER = re.compile(r"\A---\nstatus: (draft|resolved)\n---\n")
TASK_FRONTMATTER = re.compile(
    r"\A---\n"
    r"status: (?P<status>planned|active|completed|cancelled)\n"
    r"objective: >-\n"
    r"(?P<objective>(?:  \S(?:[^\n]*\S)?\n)+)"
    r"---\n\n"
    r"(?=# \S(?:[^\n]*\S)?\n)"
)
MANAGED_BEGIN = b"<!-- agent-layer:begin -->\n"
MANAGED_END = b"<!-- agent-layer:end -->\n"
MANAGED_MARKER_PREFIX = b"<!-- agent-layer:"
SUBLAYER_CONTRACT_FIELDS = (
    "purpose and routing; authority and source-of-truth boundary; contract ownership; "
    "content ownership; lifecycle and deletion behavior; customization-suffix boundary; "
    "and treatment of unknown extensions"
)

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
    paths = (ROOT / name for name in out.stdout.split("\0") if name)
    return sorted(path for path in paths if path.is_file())


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
    """The decision records. Not their README index or the hidden template."""
    return sorted(
        p
        for p in DECISIONS.glob("*.md")
        if p.name != "README.md" and not p.name.startswith(".")
    )


def section(text: str, heading: str) -> str | None:
    """Body of a level-2 section, or None when it is absent."""
    match = re.search(rf"^## {re.escape(heading)}\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    return match.group(1).strip() if match else None


def task_metadata(text: str) -> tuple[str, str]:
    """Strict task frontmatter: two ordered keys and no legacy metadata headings."""
    if "\r" in text:
        raise ValueError("task.md must use LF line endings")
    if re.search(r"^## (?:Status|Objective)\s*$", text, re.M):
        raise ValueError("task.md contains a legacy metadata heading")

    frontmatter = TASK_FRONTMATTER.match(text)
    if not frontmatter:
        raise ValueError("task.md does not start with exact status/objective frontmatter")

    objective = " ".join(
        line[2:] for line in frontmatter.group("objective").splitlines()
    )
    return frontmatter.group("status"), objective


def status_of(task: Path) -> str:
    text = (task / "task.md").read_bytes().decode("utf-8")
    return task_metadata(text)[0]


def rfc_lifecycle_errors(task: Path) -> list[str]:
    """0033: report structural contradictions in an optional task RFC."""
    rfc = task / "rfc.md"
    if not rfc.is_file():
        return []

    text = rfc.read_text(encoding="utf-8")
    frontmatter = RFC_FRONTMATTER.match(text)
    if not frontmatter:
        return ["rfc.md does not start with the exact draft/resolved frontmatter block"]

    rfc_status = frontmatter.group(1)
    task_status = status_of(task)
    resolution_headings = len(re.findall(r"^## Resolution\s*$", text, re.M))
    resolution = section(text, "Resolution")
    plan_exists = (task / "plan.md").is_file()
    errors = []

    if rfc_status == "draft":
        if resolution_headings:
            errors.append("a draft RFC has a Resolution")
        if plan_exists:
            errors.append("a draft RFC has a plan")
    else:
        if resolution_headings != 1 or not resolution:
            errors.append("a resolved RFC does not have exactly one non-empty Resolution")

    if task_status == "planned" and rfc_status == "resolved":
        errors.append("a planned task has a resolved RFC")
    if task_status == "completed" and rfc_status != "resolved":
        errors.append("a completed task has a draft RFC")

    return errors


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


DECISION_REFERENCE = re.compile(r"\bdecision\s+\d{4}\b", re.IGNORECASE)
DECISION_FILENAME = re.compile(r"\b\d{4}-[a-z0-9-]+\.md\b")
TEST_FILENAME = re.compile(r"\btest_[a-z0-9_]+\.py\b")


def skill_portability_slugs() -> set[str]:
    """Every concrete task slug or package identity this repository's own artifacts carry.

    Same construction as `test_portable_rules_carry_no_project_detail`: the archived slug is
    the part of the archive directory name after its timestamp, and active tasks are named by
    slug directly.
    """
    return {p.name.split("-", 4)[-1] for p in archived_tasks()} | {p.name for p in active_tasks()}


def skill_portability_offenders(text: str, slugs: set[str]) -> list[str]:
    """Repository-specific references a shipped skill file must not carry.

    Lexical only: it matches shapes and substrings, not meaning, so a paraphrase of the same
    fact would slip through. It intentionally does not flag `context-fold` or generic
    adopter-layer paths such as `.agents/tasks/` or `.agents/worktrees/` — those describe any
    installation, not this source repository.
    """
    offenders = []
    if DECISION_REFERENCE.search(text):
        offenders.append("a bare numbered decision reference")
    if DECISION_FILENAME.search(text):
        offenders.append("a decision record filename")
    if "decisions/" in text:
        offenders.append("a path into this repository's decisions")
    if "tests/" in text:
        offenders.append("a path into this repository's tests")
    if TEST_FILENAME.search(text):
        offenders.append("a test_*.py filename")
    for slug in slugs:
        if slug in text:
            offenders.append(f"the task slug or package identity {slug!r}")
    return offenders


@pytest.mark.parametrize("skill", skills(), ids=lambda p: p.name)
def test_shipped_skill_carries_no_project_detail(skill: Path) -> None:
    """0040: a shipped skill is copied into a repository with none of this one's evidence.

    Every regular file under the skill package that decodes as UTF-8 is scanned; a file that
    raises `UnicodeDecodeError` is skipped, which is the check's documented false-negative
    boundary — binary or otherwise non-UTF-8 content is out of scope, and a paraphrase of a
    forbidden reference can still slip past a lexical match. The matching is broad on purpose,
    which is also its false-positive risk: a future legitimate use of one of these shapes would
    be flagged too, and this first version has no allowlist to silence it.
    """
    slugs = skill_portability_slugs()
    offenders: list[str] = []
    for path in sorted(p for p in skill.rglob("*") if p.is_file()):
        try:
            text = path.read_bytes().decode("utf-8")
        except UnicodeDecodeError:
            continue
        for category in skill_portability_offenders(text, slugs):
            offenders.append(f"{path.relative_to(skill)}: {category}")
    assert not offenders, f"{skill.name} ships repository-specific content: {offenders}"


@pytest.mark.parametrize(
    "text,expected",
    [
        ("this references decision 0037 directly", "a bare numbered decision reference"),
        ("see DECISION 0037 for background", "a bare numbered decision reference"),
        (
            "0037-replace-task-index-with-frontmatter.md has the detail",
            "a decision record filename",
        ),
        ("read decisions/0037-replace-task-index-with-frontmatter.md", "a path into this repository's decisions"),
        ("run tests/test_conventions.py to check", "a path into this repository's tests"),
        ("see tests/test_conventions.py", "a test_*.py filename"),
        ("guard-skill-portability is the task slug", "the task slug or package identity"),
    ],
)
def test_skill_portability_offenders_flags_each_prohibited_category(text: str, expected: str) -> None:
    """Regression fixtures for the exact incident: `decision 0037` and the test file it named."""
    offenders = skill_portability_offenders(text, {"guard-skill-portability"})
    assert any(expected in o for o in offenders), f"{text!r} did not flag {expected!r}: {offenders}"


@pytest.mark.parametrize(
    "text",
    [
        "context-fold is the name of the methodology",
        "installs into .agents/tasks/ in the adopting repository",
        "work happens in .agents/worktrees/ during development",
    ],
)
def test_skill_portability_offenders_permits_product_and_generic_paths(text: str) -> None:
    """The product name and generic adopter-layer paths are not repository evidence."""
    offenders = skill_portability_offenders(text, {"guard-skill-portability"})
    assert not offenders, f"{text!r} was wrongly flagged: {offenders}"


# --- Dogfooding -----------------------------------------------------------------------


def managed_rule_parts(data: bytes) -> tuple[bytes, bytes] | None:
    """0035: split a valid managed rule block from its installation-owned suffix.

    No marker is the legacy whole-file case handled by the adoption procedure. Once any
    `agent-layer` marker appears, the complete shape must be unambiguous before an update can
    write any target.
    """
    marker_lines = [
        line for line in data.splitlines(keepends=True) if line.startswith(MANAGED_MARKER_PREFIX)
    ]
    if not marker_lines:
        return None
    if marker_lines != [MANAGED_BEGIN, MANAGED_END] or not data.startswith(MANAGED_BEGIN):
        raise ValueError("managed rule markers are malformed")

    end = data.index(MANAGED_END, len(MANAGED_BEGIN)) + len(MANAGED_END)
    return data[:end], data[end:]


def installed_rule_files() -> list[tuple[Path, Path, Path]]:
    """Each source template, installed-skill template, and active installation.

    The two skill packages remain identical as wholes. Their templates and the active rule file
    share a byte-identical managed block, while only the active file may carry a project suffix.
    """
    return [
        (
            t,
            ROOT / ".agents" / "skills" / "ctxfold-init" / "templates" / "agents"
            / t.relative_to(AGENT_TEMPLATES),
            ROOT / ".agents" / t.relative_to(AGENT_TEMPLATES),
        )
        for t in sorted(p for p in AGENT_TEMPLATES.rglob("*") if p.is_file())
    ]


@pytest.mark.parametrize(
    "template",
    sorted(p for p in AGENT_TEMPLATES.rglob("*") if p.is_file()),
    ids=lambda p: str(p.relative_to(ROOT)),
)
def test_managed_rule_notice_is_source_only(template: Path) -> None:
    """0035: ownership metadata stays in source rather than rendered instructions."""
    block, suffix = managed_rule_parts(template.read_bytes()) or (b"", b"")
    notice = (
        b"<!--\n"
        b"Managed rule block. Updates replace everything between the agent-layer markers.\n"
        b"Do not edit this block. Add only non-conflicting project instructions after the end "
        b"marker.\n"
        b"-->\n"
    )
    assert block.startswith(MANAGED_BEGIN + b"\n" + notice + b"\n# AGENTS.md")
    assert not suffix


@pytest.mark.parametrize(
    "template,installed_template,installed",
    installed_rule_files(),
    ids=lambda p: str(p.relative_to(ROOT)) if isinstance(p, Path) else str(p),
)
def test_installation_matches_the_distribution(
    template: Path, installed_template: Path, installed: Path
) -> None:
    """This repository runs what it ships.

    `0035`: all three copies expose the same managed block. The source and installed-skill
    templates end with that block; the active installation may append project instructions.
    """
    for path in (template, installed_template, installed):
        assert path.is_file(), f"{path.relative_to(ROOT)} is missing"

    template_parts = managed_rule_parts(template.read_bytes())
    installed_template_parts = managed_rule_parts(installed_template.read_bytes())
    installed_parts = managed_rule_parts(installed.read_bytes())
    assert template_parts is not None, f"{template.relative_to(ROOT)} has no managed block"
    assert installed_template_parts is not None, (
        f"{installed_template.relative_to(ROOT)} has no managed block"
    )
    assert installed_parts is not None, f"{installed.relative_to(ROOT)} has no managed block"

    template_block, template_suffix = template_parts
    installed_template_block, installed_template_suffix = installed_template_parts
    installed_block, _ = installed_parts
    assert not template_suffix, f"{template.relative_to(ROOT)} has content outside its block"
    assert not installed_template_suffix, (
        f"{installed_template.relative_to(ROOT)} has content outside its block"
    )
    assert template_block == installed_template_block == installed_block, (
        f"managed block drift for {installed.relative_to(ROOT)}"
    )


@pytest.mark.parametrize(
    "data",
    [
        b"preamble\n<!-- agent-layer:begin -->\nrules\n<!-- agent-layer:end -->\n",
        b"<!-- agent-layer:end -->\nrules\n<!-- agent-layer:begin -->\n",
        b"<!-- agent-layer:begin -->\nrules\n<!-- agent-layer:begin -->\n<!-- agent-layer:end -->\n",
        b"<!-- agent-layer:begin -->\nrules\n",
        b"<!-- agent-layer:begin -->\nrules\n<!-- agent-layer:end -->",
        b"<!-- agent-layer:begin -->\nrules\n<!-- agent-layer:other -->\n<!-- agent-layer:end -->\n",
    ],
    ids=["displaced", "reversed", "duplicate", "missing-mate", "missing-lf", "stray"],
)
def test_managed_rule_parts_rejects_ambiguous_markers(data: bytes) -> None:
    with pytest.raises(ValueError, match="malformed"):
        managed_rule_parts(data)


def test_managed_rule_parts_distinguishes_legacy_and_preserves_suffix() -> None:
    assert managed_rule_parts(b"legacy whole file\n") is None

    block = MANAGED_BEGIN + b"# Rules\n" + MANAGED_END
    suffix = b"\n## Project additions\n\nKeep this byte-for-byte.\n"
    assert managed_rule_parts(block) == (block, b"")
    assert managed_rule_parts(block + suffix) == (block, suffix)


def installed_layer_files() -> set[Path]:
    """Files carrying layer-owned blocks, which are not the whole of `.agents/`.

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

    # Other recognized sublayers may hold package-owned or disposable nested `AGENTS.md` files.
    # Derive their direct contracts from the distribution instead of adding a hand-written case
    # for every sublayer; never recurse into their independently owned contents.
    for template in sorted(AGENT_TEMPLATES.glob("*/AGENTS.md")):
        installed = agents / template.relative_to(AGENT_TEMPLATES)
        if installed.is_file():
            found.add(installed.relative_to(agents))

    return found


@pytest.mark.parametrize(
    "document",
    [
        ROOT / "README.md",
        ROOT / ".agents" / "AGENTS.md",
        ARCHIVE / "2026-08-24-2124-define-agent-sublayer-model" / "rfc.md",
        DECISIONS / "0041-define-governed-agent-sublayers.md",
    ],
    ids=lambda path: str(path.relative_to(ROOT)),
)
def test_sublayer_contract_fields_do_not_drift(document: Path) -> None:
    """0041: every normative restatement uses the decision's canonical field vocabulary."""
    prose = " ".join(document.read_text(encoding="utf-8").split())
    assert SUBLAYER_CONTRACT_FIELDS in prose, (
        f"{document.relative_to(ROOT)} drifts from the recognized-sublayer contract fields"
    )


def test_distribution_is_complete() -> None:
    """Every contract shipped by the distribution is active in this installation.

    Compares `AGENTS.md` files only. Direct sublayer contracts are derived from the shipped
    templates; the installation also holds task packages, which it produced rather than received.
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


def test_task_index_is_absent() -> None:
    """0037: neither this installation nor either skill copy carries a task index."""
    paths = [
        TASKS / "INDEX.md",
        TEMPLATES / "INDEX.md",
        ROOT / ".agents" / "skills" / "ctxfold-init" / "templates" / "INDEX.md",
    ]
    assert not (existing := [path.relative_to(ROOT) for path in paths if path.exists()]), (
        f"task index still exists: {existing}"
    )


# --- Task packages (0006) -------------------------------------------------------------


@pytest.mark.parametrize("task", archived_tasks() + active_tasks(), ids=lambda p: p.name)
def test_task_package_has_required_files(task: Path) -> None:
    """0006: a package is task.md and context.md; plan.md is optional."""
    for required in ("task.md", "context.md"):
        assert (task / required).is_file(), f"{task.name} is missing {required}"


@pytest.mark.parametrize("task", archived_tasks() + active_tasks(), ids=lambda p: p.name)
def test_task_metadata_is_canonical(task: Path) -> None:
    """0037: task status and objective use the one supported frontmatter format."""
    text = (task / "task.md").read_bytes().decode("utf-8")
    status, objective = task_metadata(text)
    assert status in {"planned", "active", "completed", "cancelled"}
    assert objective


def test_task_metadata_decodes_folded_objective() -> None:
    text = (
        "---\nstatus: active\nobjective: >-\n"
        "  Make task metadata canonical and\n"
        "  remove its duplicated view.\n"
        "---\n\n# Case\n"
    )
    assert task_metadata(text) == (
        "active",
        "Make task metadata canonical and remove its duplicated view.",
    )


@pytest.mark.parametrize(
    "text",
    [
        "preamble\n---\nstatus: active\nobjective: >-\n  Work.\n---\n\n# Case\n",
        "---\nobjective: >-\n  Work.\nstatus: active\n---\n\n# Case\n",
        "---\nstatus: unknown\nobjective: >-\n  Work.\n---\n\n# Case\n",
        "---\nstatus: active\nowner: agent\nobjective: >-\n  Work.\n---\n\n# Case\n",
        "---\nstatus: active\nstatus: active\nobjective: >-\n  Work.\n---\n\n# Case\n",
        "---\nstatus: active\nobjective: >-\n---\n\n# Case\n",
        "---\nstatus: active\nobjective: >-\n  Work.\n  \n---\n\n# Case\n",
        "---\nstatus: active\nobjective: >-\n Work.\n---\n\n# Case\n",
        "---\nstatus: active\nobjective: >-\n   Work.\n---\n\n# Case\n",
        "---\nstatus: active\nobjective: >-\n  Work. \n---\n\n# Case\n",
        "---\r\nstatus: active\r\nobjective: >-\r\n  Work.\r\n---\r\n\r\n# Case\r\n",
        "---\nstatus: active\nobjective: >-\n  Work.\n---\n# Case\n",
        "---\nstatus: active\nobjective: >-\n  Work.\n---\n\nCase\n",
        (
            "---\nstatus: active\nobjective: >-\n  Work.\n---\n\n# Case\n\n"
            "## Status\n\nactive\n"
        ),
        (
            "---\nstatus: active\nobjective: >-\n  Work.\n---\n\n# Case\n\n"
            "## Objective\n\nLegacy.\n"
        ),
    ],
    ids=[
        "preamble",
        "wrong-order",
        "unknown-status",
        "unknown-key",
        "duplicate-key",
        "empty-objective",
        "blank-objective-line",
        "one-space-indent",
        "three-space-indent",
        "trailing-whitespace",
        "crlf",
        "missing-blank-line",
        "missing-title",
        "legacy-status-heading",
        "legacy-objective-heading",
    ],
)
def test_task_metadata_rejects_noncanonical_format(text: str) -> None:
    with pytest.raises(ValueError):
        task_metadata(text)


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


@pytest.mark.parametrize("task", archived_tasks() + active_tasks(), ids=lambda p: p.name)
def test_task_rfc_lifecycle_is_consistent(task: Path) -> None:
    """0033: an optional RFC and plan agree with the task's lifecycle state."""
    assert not (errors := rfc_lifecycle_errors(task)), f"{task.name}: {errors}"


def _rfc_case(
    root: Path,
    task_status: str,
    rfc_status: str | None,
    *,
    plan: bool = False,
) -> Path:
    task = root / "case"
    task.mkdir()
    (task / "task.md").write_text(
        f"---\nstatus: {task_status}\nobjective: >-\n  Exercise RFC state.\n---\n\n# Case\n",
        encoding="utf-8",
    )
    if rfc_status:
        resolution = "\n## Resolution\n\nSelected direction.\n" if rfc_status == "resolved" else ""
        (task / "rfc.md").write_text(
            f"---\nstatus: {rfc_status}\n---\n\n# RFC\n{resolution}",
            encoding="utf-8",
        )
    if plan:
        (task / "plan.md").write_text("# Plan\n", encoding="utf-8")
    return task


@pytest.mark.parametrize(
    "task_status,rfc_status,plan",
    [
        ("planned", None, False),
        ("planned", "draft", False),
        ("active", None, False),
        ("active", "draft", False),
        ("active", "resolved", False),
        ("active", "resolved", True),
        ("completed", None, False),
        ("completed", "resolved", False),
        ("completed", "resolved", True),
        ("cancelled", None, False),
        ("cancelled", "draft", False),
        ("cancelled", "resolved", False),
        ("cancelled", "resolved", True),
    ],
    ids=[
        "planned-without-rfc",
        "planned-draft",
        "active-without-rfc",
        "active-draft",
        "active-resolved",
        "active-resolved-with-plan",
        "completed-without-rfc",
        "completed-resolved",
        "completed-resolved-with-plan",
        "cancelled-without-rfc",
        "cancelled-draft",
        "cancelled-resolved",
        "cancelled-resolved-with-plan",
    ],
)
def test_task_rfc_lifecycle_accepts_supported_matrix_row(
    tmp_path: Path,
    task_status: str,
    rfc_status: str | None,
    plan: bool,
) -> None:
    task = _rfc_case(tmp_path, task_status, rfc_status, plan=plan)
    assert not rfc_lifecycle_errors(task)


@pytest.mark.parametrize(
    "case,task_status,rfc_text,plan",
    [
        (
            "malformed-frontmatter",
            "active",
            "---\nstatus: draft\nowner: agent\n---\n\n# RFC\n",
            False,
        ),
        ("unknown-status", "active", "---\nstatus: withdrawn\n---\n\n# RFC\n", False),
        (
            "planned-resolved",
            "planned",
            "---\nstatus: resolved\n---\n\n# RFC\n\n## Resolution\n\nSelected.\n",
            False,
        ),
        (
            "draft-with-resolution",
            "active",
            "---\nstatus: draft\n---\n\n# RFC\n\n## Resolution\n\nStale.\n",
            False,
        ),
        ("draft-with-plan", "active", "---\nstatus: draft\n---\n\n# RFC\n", True),
        ("resolved-without-resolution", "active", "---\nstatus: resolved\n---\n\n# RFC\n", False),
        (
            "resolved-with-empty-resolution",
            "active",
            "---\nstatus: resolved\n---\n\n# RFC\n\n## Resolution\n",
            False,
        ),
        (
            "resolved-with-duplicate-resolution",
            "active",
            "---\nstatus: resolved\n---\n\n# RFC\n\n## Resolution\n\nOne.\n\n"
            "## Resolution\n\nTwo.\n",
            False,
        ),
        ("completed-draft", "completed", "---\nstatus: draft\n---\n\n# RFC\n", False),
    ],
    ids=[
        "malformed-frontmatter",
        "unknown-status",
        "planned-resolved",
        "draft-with-resolution",
        "draft-with-plan",
        "resolved-without-resolution",
        "resolved-with-empty-resolution",
        "resolved-with-duplicate-resolution",
        "completed-draft",
    ],
)
def test_task_rfc_lifecycle_rejects_forbidden_case(
    tmp_path: Path,
    case: str,
    task_status: str,
    rfc_text: str,
    plan: bool,
) -> None:
    task = _rfc_case(tmp_path, task_status, None, plan=plan)
    (task / "rfc.md").write_text(rfc_text, encoding="utf-8")
    assert rfc_lifecycle_errors(task), case


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
    "Ideas",
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
    """0005, 0011, 0018, 0035, 0041: managed blocks carry no project detail.

    A record number, a path to this repository's documents, or one of its task slugs
    would be wrong in any other repository — and would read correctly here, which is
    why this is checked rather than reviewed.

    The project name is excluded too. The rules describe the layer, and a set of rules
    naming its vendor is wrong for anyone who forks and maintains them. Where the layer
    came from is metadata, and metadata is not built yet.
    """
    parts = managed_rule_parts(rules.read_bytes())
    assert parts is not None, f"{rules.relative_to(ROOT)} has no managed block"
    block, _ = parts
    text = block.decode("utf-8")
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
