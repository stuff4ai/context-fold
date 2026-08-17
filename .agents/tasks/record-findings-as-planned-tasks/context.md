# Context — record-findings-as-planned-tasks

## Base state

`main` is at `bc4b9b0`. Twenty-two decision records, fifteen archived tasks, all `completed`.
No task has ever carried the `planned` status.

## References

- `.agents/tasks/AGENTS.md` — the rules this changes: capture, and where outliving questions go.
- `decisions/0007-archive-before-merge.md` — its Consequences put immutability at merge, not at
  archival, which is the boundary the first three versions of this task got wrong.
- `decisions/0018-ship-a-distribution.md` — the layer is removable; `.agents/` is where it lives,
  not what it is.
- `decisions/0013-improve-context-from-the-work.md` — the loop whose capture step is task-scoped.
- `decisions/0010-record-open-questions-in-project-layer.md` — this repository's own destination
  for open questions, which an adopter does not have.
- `OPEN-QUESTIONS.md` — the entry this closes.

## Assumptions

- Findings with no owning task stay rare. Three in fifteen tasks, and fewer now that findings
  from merging are recognised as belonging to the task being merged — so a task package is not
  too much ceremony for one. `0013` warns that capture must cost less than the irritation it
  records.
- A planned task is a legitimate index entry. The checks already permit `planned` for a task that
  is not archived; nothing needs relaxing.

## Context conflicts

`0010` puts this repository's open questions in `OPEN-QUESTIONS.md`, and the portable rule cannot
name that file. The rule therefore asks only whether removing the layer would lose durable
project knowledge, and leaves each installation to answer with whatever it has —
`OPEN-QUESTIONS.md` here. Where a project has nothing, the gap is named and a planned task holds
the finding until a destination exists. `0010` stays intact, and an adopter gets a question
instead of a destination that would lose the answer.

## Open questions

Whether the index's Active section should be renamed now that it can list planned work. Left
alone: it is a naming quibble, the status column disambiguates, and renaming is churn until it
demonstrably grates.
