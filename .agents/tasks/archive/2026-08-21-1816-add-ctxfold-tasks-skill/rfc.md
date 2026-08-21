---
status: resolved
---

# RFC — add the ctxfold-tasks query skill

## Problem

The task-index migration (decision `0037`) removed the shared `INDEX.md` and made each task
package's own frontmatter authoritative, but left agent discovery unsupported: nothing yet reads
task packages across the repository and its Git worktrees and groups the same logical task when
it appears in more than one checkout. Without a defined contract, discovery happens ad hoc and
inconsistently across agents, or reintroduces a hand-maintained index.

## Current proposal

An agent-only skill, `ctxfold-tasks`, self-contained per the existing skill conventions
(`tests/test_conventions.py::test_skill_is_self_contained`), bundling a private helper that:

- Scans `.agents/tasks/*` at the repository root, excluding `archive/`, for unfinished
  (`planned`/`active`) task packages, and `.agents/tasks/archive/*` for archived
  (`completed`/`cancelled`) ones, decoding `status` and `objective` with the same frontmatter
  contract `tests/test_conventions.py` already enforces, so the skill and the tests read metadata
  identically.
- Also scans every `.agents/worktrees/*` directory at the repository root as a registered nested
  checkout — each one a full repository with its own `.agents/tasks/` — the only worktree
  registry this project defines (`.agents/worktrees/AGENTS.md`). A worktree directory that is
  missing, not a Git checkout, or unreadable is reported as a diagnostic entry, not a fatal error.
- Groups observations by task slug (the directory name, or the archive directory's slug suffix)
  as the logical task identity, and picks one status per slug using the already-agreed precedence
  `planned < active < completed/cancelled`; a terminal-status tie is broken by the later
  archive-directory timestamp, with a diagnostic recording that choice.
- Treats differing task content at the same highest-status observation as an unresolved conflict:
  the query never silently drops one side. All conflicting sources are returned together, tagged
  as a conflict, instead of the skill picking a winner.
- Skips a malformed task package (missing or unparseable frontmatter, wrong directory shape)
  rather than failing the whole query, and reports it as a diagnostic entry naming its path and
  the problem.
- Supports three views: `unfinished` (default; `planned` + `active`), `archive`, `all`.
- Returns machine-readable JSON: a list of task entries (slug, status, objective, title,
  source-relative path(s), conflict/tie flags) plus a separate diagnostics list (missing
  worktrees, malformed packages, ambiguity notes). Exit code stays `0` whenever the query itself
  ran, even with diagnostics present; a non-zero exit is reserved for a query that could not run
  at all (for example, not inside a context-fold repository).

Mutating operations (start, complete, archive, cancel) and any human-facing CLI stay out of
scope, matching the boundary already recorded in the archived task-index migration
(`.agents/tasks/archive/2026-08-20-2320-replace-task-index/task.md`) and this task's own scope.

## Alternatives

- A thin skill with no bundled helper, relying on the invoking agent to grep or parse frontmatter
  itself. Rejected as a starting proposal: it reintroduces per-agent parsing drift, which
  canonical frontmatter (decision `0037`) was meant to end.
- Treating worktree discovery as out of scope for v0, covering only the repository root. Simpler,
  but defeats the stated objective ("across ... registered Git worktrees") and would need a
  second migration once cross-worktree discovery is added.
- Erroring with a non-zero exit on any conflict or malformed package instead of returning
  diagnostics. Rejected: one bad or ambiguous task package would make the whole query unusable
  for every other, unrelated task.

## Resolution

- **Output shape.** Flat: `{"tasks": [...], "diagnostics": [...]}`. Each task entry carries its
  own source path(s) and conflict/tie flags; diagnostics is a separate, ungrouped list.
- **Filtering.** v0 exposes only the three views (`unfinished`/`archive`/`all`). No slug filter;
  an agent that wants one task filters the returned JSON itself. A filter can be added later
  without breaking this contract.
- **Helper language.** Python, stdlib-only so it satisfies
  `tests/test_conventions.py::test_skill_is_self_contained`, decoding frontmatter the same way
  `tests/test_conventions.py` already does so the skill and the test suite can never disagree on
  what counts as valid task metadata.
