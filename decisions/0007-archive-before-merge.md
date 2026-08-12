# Archive tasks before merge

## Status

Accepted. Archive directory naming superseded by
[0009](0009-order-task-index-newest-first.md); the rest stands.

## Context

A task package describes work in progress. Once the work lands, the package is history — but
only if something moves it there.

Archiving after merge means a second commit on `main` that exists purely to file paperwork.
It is easy to skip, and when it is skipped the active task list slowly fills with finished
work until it stops being trustworthy.

There is also a question of when a task is actually done. Finishing the implementation is not
the same as finishing the task: durable outcomes may still be sitting inside the task package
where the deletion test says they must not remain.

This project uses a branch-and-pull-request workflow ([0001](0001-use-github-flow.md)), which
provides a natural approval point before the work becomes part of `main`.

## Decision

A task is archived inside its pull request, before merge, not after.

The order is: implementation, verification, review, approval, fold durable outcomes into the
project layer, archive the task, update `INDEX.md`, final exact-head check, merge.

Approval authorizes archival. Merge accepts the entire final repository state, so the merge
commit contains the project changes, the updated context, and the archived task history
together.

Archived tasks live flat under `.agents/tasks/archive/`. Completed and cancelled tasks are
both historical records and are not separated into different directories; the final state is
recorded in the task's own `task.md` as `completed` or `cancelled`.

Archived directories take a date prefix — `.agents/tasks/archive/{YYYY-MM-DD}-{slug}/` —
while active directories stay slug-only. The date records when the task left active state and
gives the archive chronology; the slug remains the stable identity.

Archived tasks are effectively immutable and are not current project truth.

The final exact-head check is a concrete gate run at the branch head before merge:

1. Each acceptance criterion in `task.md` is satisfied.
2. No durable outcome exists only inside `.agents/` — the deletion test.
3. The task directory is under `archive/` with final Status and Outcome set.
4. `INDEX.md` matches the task directories on disk.

## Consequences

History is self-describing: a merge commit carries the work and the record of the work.

The active task list stays honest, because nothing finished can reach `main` still marked
active.

Review sees the final state, including the Outcome, rather than approving work and trusting
that filing happens later.

The archival move appears in the pull request as a large rename, which adds diff noise to
review.

If review requests changes after archival, the archived package must be amended before merge.
Immutability applies from merge onward, not from the moment of archival.
