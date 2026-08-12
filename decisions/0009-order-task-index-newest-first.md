# Order the task index newest first

## Status

Accepted

## Context

The task index is a derived view for finding work ([0006](0006-task-package-model.md)). Its
archive section only grows: tasks are added on completion and never removed.

Appending each completed task to the end pushes the most recent work to the bottom of an
ever-longer file. That is the worst position for it, because recent tasks are the ones most
likely to carry relevant context, and the bottom of a long file is what gets skimmed past or
truncated when the file is read into a limited context.

Chronology does not depend on the index. Archived directories carry a timestamp prefix
([0007](0007-archive-before-merge.md)), and the commit history is a better record of order
than a table. The index is therefore free to be ordered for reading rather than for
record-keeping.

The index must also stay regenerable: conflicts in it are repaired by rebuilding from the task
directories rather than by hand, which requires an order that can be derived rather than
remembered.

## Decision

The archive section of the task index lists tasks newest first.

The active section is sorted by directory name ascending. That order carries no meaning — it
exists so the index can be rebuilt whole. Newest-first is not applied there: the reasoning
above depends on a list that grows without bound, and active tasks leave the list when they
are archived.

Archived task directories are named `{YYYY-MM-DD-HHMM}-{slug}`, timed to the minute the task
left active state. This supersedes the day-only prefix in
[0007](0007-archive-before-merge.md); nothing else in that record changes.

Regeneration sorts archived tasks by directory name descending, which orders them by recency,
and active tasks by directory name ascending. Neither consults the task files.

The index states no rule about its own ordering. The rule lives in
`.agents/tasks/AGENTS.md`, alongside the other instructions for working with tasks.

## Consequences

The most recently completed work is at the top, where it is read.

Both sections remain derivable, so the conflict-repair rule holds unchanged.

The two sections are ordered differently, which is a small inconsistency. Active tasks carry
no timestamp — slugs are deliberately free of ordering metadata ([0006](0006-task-package-model.md))
— so ordering them by recency would mean adding a creation prefix that exists only to satisfy
symmetry.

Reading the archive as a narrative of how the project developed now runs bottom to top, which
is the less natural direction for that purpose. Commit history serves that reading better
anyway.

Directory names are longer and carry a time that is rarely interesting on its own. That cost
buys an order that is correct rather than incidental: a day-only prefix was tried first and
placed the newest of three same-day tasks second, because the sort fell through to comparing
slugs alphabetically.

Minute granularity leaves two tasks archived in the same minute unordered relative to each
other. Concurrent branches also cannot collide on a directory name unless they archive within
the same minute, which a day-only prefix made likely and this makes remote.

This changes a portable instruction file, so it applies to every project using context-fold,
not only this one.
