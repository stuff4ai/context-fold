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

Chronology does not depend on the index. Archived directories carry a date prefix
([0007](0007-archive-before-merge.md)), and the commit history is a better record of order
than a table. The index is therefore free to be ordered for reading rather than for
record-keeping.

The index must also stay regenerable: conflicts in it are repaired by rebuilding from the task
directories rather than by hand, which requires an order that can be derived rather than
remembered.

## Decision

The task index lists tasks newest first, in both its active and archive sections.

Regeneration sorts archived tasks by directory name descending, which orders them by date
prefix without consulting the task files.

The index states no rule about its own ordering. The rule lives in
`.agents/tasks/AGENTS.md`, alongside the other instructions for working with tasks.

## Consequences

The most recently completed work is at the top, where it is read.

The order remains derivable, so the conflict-repair rule holds unchanged.

Reading the archive as a narrative of how the project developed now runs bottom to top, which
is the less natural direction for that purpose. Commit history serves that reading better
anyway.

Date prefixes have day granularity, so tasks completed on the same day are not ordered by the
prefix alone. Their relative order within a day is whatever regeneration produces and is not
meaningful.

This changes a portable instruction file, so it applies to every project using context-fold,
not only this one.
