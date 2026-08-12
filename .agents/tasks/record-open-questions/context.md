# Context — record-open-questions

## Base state

`main` is at `3fe437b`. Ten decision records, three archived tasks, no active work.

## Sources

The questions come from three places:

- The design conversation that produced context-fold, which exists outside this repository and
  is the only record of what was deliberately postponed.
- `context.md` in the three archived task packages, where open questions were written while
  each task ran.
- The problem logs of those tasks, where several gaps in the current rules were found by using
  them.

## References

- `decisions/0005-agents-layer-boundary.md` — why durable knowledge cannot live only in
  `.agents/`.
- `decisions/0006-task-package-model.md` — `context.md` holds task-local facts.
- `.agents/tasks/archive/AGENTS.md` — archived tasks are history, not current truth.

## Assumptions

- A question that outlives its task is project knowledge, and the deletion test applies to it:
  a human deciding what to build next needs it.
- Deferred scope and open questions are the same kind of thing for storage purposes — both are
  "not decided, on purpose" — and separating them into two documents would split one list by a
  distinction nobody needs when reading it.

## Context conflicts

Questions recorded in archived packages are now duplicated by the project-layer list, which
the "reference, do not duplicate" rule would normally forbid. Accepted here because archived
packages are immutable and cannot be trimmed: the archived copy is a historical record of what
was open *at that time*, and the project-layer document is the live list. `0010` states which
one is authoritative.

## Open questions

Recorded in `OPEN-QUESTIONS.md` by this task rather than here — which is the point of it.
