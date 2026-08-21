---
status: completed
objective: >-
  Provide agents with a supported way to discover unfinished and archived context-fold tasks
  across the repository and its registered Git worktrees.
---

# Add the ctxfold-tasks query skill

## Why

The task-index migration deliberately removed the private listing helper and did not provide a
human CLI. The follow-up now needs a durable task contract before implementation starts, while
keeping the agent query interface separate from future human tooling.

## Scope

- An agent-only `ctxfold-tasks` skill with a documented invocation and output contract.
- A private helper bundled with the skill, if the selected design still needs one.
- Discovery of task packages in the repository and registered nested worktrees, including
  unfinished and archived packages.
- Deterministic grouping of the same logical task across worktrees, status precedence, timestamp
  tie handling, and ambiguity diagnostics.
- Skill installation, documentation, and convention checks required by the selected design.
- This task's RFC or plan, if design questions need to be settled before implementation.

## Out of scope

- A supported human-facing CLI; that is a later interface.
- Mutating task lifecycle operations such as starting, completing, archiving, or cancelling tasks.
- Reintroducing a repository-wide `INDEX.md` as the query source of truth.
- Copying task contents into a second index or durable project knowledge store.

## Acceptance

1. A resolved design defines the skill's invocation, default view, output schema, source paths, and
   behavior for malformed, duplicated, or ambiguous task packages.
2. The skill discovers tasks from the repository and registered worktrees without treating the
   derived index as authoritative.
3. Cross-worktree grouping and status selection are deterministic and preserve source paths and
   diagnostics when content conflicts.
4. The implementation, installation path, documentation, and checks required by the resolved
   design are complete, while human CLI and mutating lifecycle operations remain separate.
5. The final task outcome records any durable design decision in the project layer before archival.

## Outcome

`rfc.md` resolves the four open design questions (worktree registration scope, conflict
handling, the JSON envelope, malformed-package behavior), and decision
`0038-add-a-task-discovery-skill.md` records that design durably.

`skills/ctxfold-tasks/` follows the [Agent Skills](https://agentskills.io/specification) format:
`SKILL.md` (with `license` and `compatibility` frontmatter alongside the required
`name`/`description`) and a stdlib-only `scripts/query_tasks.py`, installed byte-identically at
`.agents/skills/ctxfold-tasks/` (reachable through the existing `.claude/skills` symlink,
`0034`). The helper scans `.agents/tasks/` (unfinished and archived) plus every registered
`.agents/worktrees/*` checkout, groups observations by slug using status precedence
`planned < active < completed/cancelled`, breaks a terminal-status tie by archive timestamp, and
never drops a disagreeing observation — a same-status content conflict is flagged and every
source is retained. It supports `unfinished` (default), `archive`, and `all` views and prints
`{"tasks": [...], "diagnostics": [...]}`. It decodes only the frontmatter-and-title prefix of
`task.md`; unlike `tests/test_conventions.py`, it does not separately detect the pre-`0037`
legacy heading format, since `0037` already means no accepted task.md can have that shape.

`tests/test_ctxfold_tasks.py` behaviorally tests discovery, grouping, precedence, conflicts,
tie-breaking, diagnostics, and the CLI's JSON/exit-code contract with synthetic fixtures, and
asserts the helper's frontmatter decoding stays in lockstep with `tests/test_conventions.py`'s
`task_metadata`. `OPEN-QUESTIONS.md`'s task-lifecycle entry on finding blocked work at scale is
narrowed to note that general discovery now exists while `## Blocked by` exposure remains open.

No human-facing CLI and no mutating lifecycle operation were added; both stay separate future
work, as scoped.

The full suite (`pytest tests/`, 587 tests) and `pymarkdown --config .pymarkdown.json scan -r
--respect-gitignore .` pass at the finished state.

## Approval

Human.

## Problems

### Importing the skill script for tests wrote `__pycache__` into the shipped skill

`tests/test_ctxfold_tasks.py` loads the skill's script via `importlib.util`. The first run left
a `__pycache__/` directory on disk next to it, which failed `test_skill_ships_no_stray_files` —
a skill directory is what an installer copies, and Python's default bytecode cache is not
something intended to ship. Assumed this only mattered for files an agent might leave behind by
hand; it also happens automatically on ordinary test collection. Fixed by setting
`sys.dont_write_bytecode = True` around the import in the test module.

### The first version carried unneeded legacy-format and layout choices

Review feedback after the PR opened caught two things the initial version got wrong. First,
`query_tasks.py` special-cased the pre-`0037` `## Status`/`## Objective` heading format —
detecting and rejecting it with its own dedicated check — even though `0037` already means no
accepted task.md in this project can have that shape; a discovery tool re-implementing detection
for a format the project does not support was unnecessary weight, and the check was removed
along with `from __future__ import annotations` (itself a mechanism for supporting older Python
than the script actually needs) in favor of an honest `compatibility: Requires Python 3.10+`
frontmatter field. Second, the skill's layout put its bundled script beside `SKILL.md` instead of
under `scripts/`, which does not match the [Agent Skills](https://agentskills.io/specification)
open format this project's skills are meant to follow; the script moved to
`scripts/query_tasks.py`, and `license`/`compatibility` frontmatter fields were added to match
the specification. Assumed the initial structure was a reasonable local convention without
checking it against the format's own specification first.

### A shipped docstring named this repository's own decision number and test file

`scripts/query_tasks.py`'s module and `decode_task_md` docstrings said the frontmatter contract
"mirrors decision 0037" and that certification was "the job `tests/test_conventions.py` already
owns" — true of this repository, but this skill directory is what gets copied into a different
project, which has neither that decision record nor that test file. Assumed a reference the
skill's own home repository would recognize was harmless documentation; it is instead exactly
the kind of repo-specific context a distributed skill must not carry — only the approaches and
instructions built from that experience travel, not the artifacts that produced them. Fixed by
describing the frontmatter contract directly (strict two-key `status`/`objective` frontmatter,
folded objective) instead of pointing at this repository's own record and test suite. A fresh
verifier confirmed no other repo-specific reference remained in the shipped skill.
