# Replace the task index with frontmatter

## Status

Proposed

## Context

Each task already owns its status and objective, but `INDEX.md` repeats both for navigation. Every
task start and finish therefore edits a shared file, and an interrupted sequence can leave the
copy disagreeing with the package. Concurrency turns that duplicated view into a predictable
conflict surface.

Agents need structured task discovery. Humans do not yet need a supported command, and exposing a
script now would make its interface a product decision before the methodology has been exercised.
A future agent skill and a future human CLI can read the same canonical files without defining
either interface here.

This repository is the methodology's only current installation. Carrying both the heading format
and a new format would add a transition protocol without preserving a real adopter.

## Decision

`task.md` starts at byte zero with LF-only frontmatter containing exactly two keys in this order:

```yaml
---
status: active
objective: >-
  A non-empty objective, folded across lines when useful.
---

# Task title
```

`status` is `planned`, `active`, `completed`, or `cancelled`. `objective` has one or more non-empty
lines, each indented by exactly two spaces with no trailing whitespace; joining the lines with one
space yields the objective. No other or duplicate key is accepted. `## Status` and
`## Objective` headings are not part of the format. There is no legacy parser.

Agents discover unfinished work by enumerating direct child directories of `.agents/tasks/`
other than `archive/` and reading each package's frontmatter. They read `archive/` only when
history matters. A direct child has an unfinished status; an archived package has a terminal
status. Location and frontmatter together expose an interrupted finish without a second view.

`INDEX.md` and its distribution template are removed. Fresh adoption creates task zero directly
in the new format and creates no index. Repeat adoption updates managed blocks and leaves task
packages alone; it does not add compatibility behavior for an index from another installation.

Accepted task archives are normally immutable. During v0, an explicit repository-wide
task-schema migration may rewrite them when its declared scope names the archive, it preserves
the meaning of migrated metadata and every unrelated byte, and it verifies the complete corpus
before review. An ordinary task may never rewrite accepted history opportunistically.

This supersedes [0009](0009-order-task-index-newest-first.md) and narrows the index or heading
parts of [0006](0006-task-package-model.md), [0007](0007-archive-before-merge.md),
[0016](0016-check-conventions-in-ci.md), [0017](0017-adoption-procedure.md),
[0018](0018-ship-a-distribution.md),
[0021](0021-separate-what-upgrades-from-what-diverges.md),
[0022](0022-route-findings-without-an-owning-task.md),
[0024](0024-settle-status-disagreements-by-the-directory.md),
[0025](0025-run-tasks-in-parallel.md), [0026](0026-map-what-is-under-the-agents-directory.md),
[0027](0027-produce-evidence-at-the-final-check.md),
[0032](0032-fold-worktrees-agents-md-into-the-byte-identical-set.md), and
[0033](0033-separate-rfc-discussion-from-execution-planning.md). Their remaining decisions stand.

## Consequences

A task has one machine-readable source for its lifecycle metadata. Starting, finishing, and
working concurrently no longer require editing a shared navigation file. Plain directory listing
and file reading remain sufficient when no query skill is installed.

The format is intentionally strict. Adding metadata later is a schema change, not an unreviewed
extension, and old task files fail checks rather than being interpreted heuristically.

The archive migration changes accepted `task.md` files, so its evidence must distinguish the
mechanical metadata move from authored history. This is an explicit v0 cost, not a general license
to edit archives.

No agent query skill, helper script, or human CLI is created by this decision. Those interfaces
can be designed separately after the canonical files exist.
