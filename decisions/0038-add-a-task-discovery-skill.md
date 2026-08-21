# Add a task discovery skill

## Status

Accepted

## Context

`0037` made each task package's own frontmatter authoritative and removed the shared task index,
but deliberately left agent discovery unsupported: nothing read task packages across the
repository and its Git worktrees, or grouped the same logical task when it appeared in more than
one checkout. Absent a defined contract, discovery would happen ad hoc and inconsistently across
agents, or reintroduce a hand-maintained index by another name.

`.agents/worktrees/AGENTS.md` is this project's only registry of nested checkouts: one Git
worktree per task slug under `.agents/worktrees/`. A task in progress there is invisible to an
agent working at the repository root unless something looks.

## Decision

An agent-only skill, `ctxfold-tasks`, ships at `skills/ctxfold-tasks/` and is installed at
`.agents/skills/ctxfold-tasks/` for this repository's own use, matching `0034`'s Claude Code
adapter that already exposes everything under `.agents/skills/`. It bundles one stdlib-only
Python script, `query_tasks.py`, that:

- Enumerates direct children of `.agents/tasks/` other than `archive/` as unfinished packages,
  and `.agents/tasks/archive/*` as archived ones, decoding `status`/`objective` with the exact
  frontmatter contract `0037` defines. A package that fails to decode is excluded from the result
  and reported as a `malformed_task` diagnostic naming its path and the problem, rather than
  failing the whole query.
- Also scans every `.agents/worktrees/*` directory as a registered nested checkout, repeating
  discovery against that checkout's own `.agents/tasks/`. A worktree directory with no
  `.agents/tasks` becomes a `missing_worktree` diagnostic, not a fatal error.
- Groups observations by task slug — the directory name, or an archive directory's slug suffix —
  as the logical task identity. One status is selected per slug by precedence
  `planned < active < completed/cancelled`. Differing content among the observations at that
  selected status is never dropped: the entry is flagged `conflict` and carries every
  disagreeing observation. A tie between multiple terminal-status (`completed`/`cancelled`)
  observations is broken by the later archive-directory timestamp, flagged `tie_broken`, and
  recorded as a `terminal_tie` diagnostic.
- Supports three views — `unfinished` (default), `archive`, `all` — and prints one JSON object,
  `{"tasks": [...], "diagnostics": [...]}`, to stdout. The exit code is `0` whenever the query
  ran, even with diagnostics present; a non-zero exit means the query itself could not run at
  all, for example because the working directory is not inside a context-fold repository.

Mutating task-lifecycle operations (start, complete, archive, cancel) and any human-facing CLI
are explicitly out of scope. The skill is a query, not a cache: it re-reads task packages on
every invocation and asserts no authority over their content.

## Consequences

An agent can find unfinished or archived work across the repository and its registered
worktrees without hand-rolling frontmatter parsing or silently missing work in progress
elsewhere. Ambiguity — a malformed package, a missing worktree, conflicting content, a resolved
tie — stays visible in `diagnostics` instead of being resolved silently or failing the query for
every other, unrelated task.

`tests/test_ctxfold_tasks.py` behaviorally tests grouping, precedence, conflict, tie-breaking,
diagnostics, and the CLI's JSON and exit-code contract against synthetic fixtures, independent of
the general skill and portable-rule conventions `tests/test_conventions.py` already checks. A
dedicated case keeps `query_tasks.py`'s frontmatter decoding in lockstep with `tests/test_conventions.py`'s
own `task_metadata`, so the skill and the convention suite cannot silently disagree about what
counts as a valid task package.

`OPEN-QUESTIONS.md`'s task-lifecycle entry asking how agents find blocked work at scale is
narrowed: general cross-worktree task discovery now exists, though this skill does not parse
`## Blocked by` itself, so exposing blockers specifically remains open. No human-facing CLI is
created by this decision; that interface, along with mutating lifecycle operations, remains
separate future work, the same boundary `0037` already drew.
