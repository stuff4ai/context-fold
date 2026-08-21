---
name: ctxfold-tasks
description: >
  Discover context-fold task packages across a repository and its registered Git worktrees —
  unfinished (planned/active) and archived (completed/cancelled) — without treating the result
  as a durable index. Returns machine-readable JSON with grouping and diagnostics for the same
  logical task observed in more than one checkout.
  Trigger: an agent needs to find unfinished or archived context-fold tasks, including work
  in progress in another worktree, before starting or coordinating work.
---

# Query context-fold tasks

Agent-only. This skill has no supported human-facing interface; a human reads task packages
directly, the way `.agents/tasks/AGENTS.md` describes.

## What to run

`query_tasks.py`, beside this file, is the whole implementation — stdlib-only, nothing to
install. Run it from anywhere inside the repository you want to query:

```
python3 <path-to-this-skill>/query_tasks.py [unfinished|archive|all]
```

`unfinished` is the default and matches `planned` + `active` tasks. `archive` matches
`completed` + `cancelled`. `all` returns every status.

The script finds its own repository root (the nearest ancestor with a `.agents/tasks`
directory) from the current working directory, so it does not need to be invoked from the
repository root itself.

## Reading the result

One JSON object on stdout: `{"tasks": [...], "diagnostics": [...]}`.

Each task entry has `slug`, `status`, `objective`, `title`, and `sources` (every
source-relative path this task was observed at, across the repository and its worktrees).
`conflict` is `true` when sources at the task's selected status disagree on content; when it
is, the entry also carries `observations`, one per disagreeing source, so nothing is silently
dropped in favor of the others. `tie_broken` is `true` when two archived observations of the
same task were resolved by the later archive-directory timestamp.

`diagnostics` covers everything that could not become a clean task entry: a malformed task
package, a registered worktree with no `.agents/tasks`, a conflict, or a timestamp tie-break.
Treat it as required reading, not an error log to ignore — a query that found tasks can still
have something worth surfacing to whoever asked.

The exit code is `0` whenever the query ran, even with diagnostics present. A non-zero exit
means the query itself could not run — for example, the working directory is not inside a
context-fold repository, or an unsupported view was requested — and stdout still carries a
JSON object with an `error` key describing why.

## What this does not do

No mutation: starting, completing, archiving, or cancelling a task is untouched, and nothing
this skill does changes a task package. Treat the result as a query, not a cache — run it again
rather than remembering a prior answer, since task packages change as work proceeds.
