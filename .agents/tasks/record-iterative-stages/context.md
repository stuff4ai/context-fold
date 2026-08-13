# Context — record-iterative-stages

## Base state

`main` is at `f324180`. Fifteen decision records, eight archived tasks, no active work.

Eight tasks have run the lifecycle. Every one of them returned to an earlier stage at least
once, and none recorded that as an exception, because nothing said it was one.

## References

- `decisions/0006-task-package-model.md` — the four `Status` values, which this does not change.
- `decisions/0013-improve-context-from-the-work.md` — problems are captured during work, which
  presumes work continues after a problem is found rather than ending at it.
- `.agents/tasks/AGENTS.md` — the Stages section, and the existing statement that status is not
  the same as stage. This adds the second half of that distinction.

## Assumptions

- Iteration is free in bookkeeping terms. A task stays `active` through every return, so
  nothing needs updating when work goes backwards — which is why the rule can be permissive
  rather than procedural.
- The eight tasks are evidence about tasks of this kind — small, documentation-shaped, one
  author. Whether longer or multi-author work loops the same way is untested.

## Context conflicts

The source design described several named loops — requirements, design, implementation,
problem-solving, verification, learning — and a lifecycle with a stage for each. That structure
was cut. The observation behind it was correct and the structure expressing it was not, which
is why this records the behaviour without restoring the stages.

## Open questions

Whether a task that keeps returning should eventually be split or cancelled is not decided here.
Nothing counts iterations, and this task does not add anything that would.
