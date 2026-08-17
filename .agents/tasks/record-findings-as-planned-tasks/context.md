# Context — record-findings-as-planned-tasks

## Base state

`main` is at `bc4b9b0`. Twenty-two decision records, fifteen archived tasks, all `completed`.
No task has ever carried the `planned` status.

## References

- `.agents/tasks/AGENTS.md` — the rules this changes: capture, and where outliving questions go.
- `decisions/0013-improve-context-from-the-work.md` — the loop whose capture step is task-scoped.
- `decisions/0007-archive-before-merge.md` — why archival precedes merge, which is what puts
  findings outside a task in the first place.
- `decisions/0010-record-open-questions-in-project-layer.md` — this repository's own destination
  for open questions, which an adopter does not have.
- `OPEN-QUESTIONS.md` — the entry this closes.

## Assumptions

- Post-archival findings stay rare. Three in fifteen tasks, so a task package is not too much
  ceremony for one — `0013` warns that capture must cost less than the irritation it records.
- A planned task is a legitimate index entry. The checks already permit `planned` for a task that
  is not archived; nothing needs relaxing.

## Context conflicts

`0010` puts this repository's open questions in `OPEN-QUESTIONS.md`, and the portable rule cannot
name that file. The rule therefore treats a planned task as the fallback when a project has no
place of its own, which leaves `0010` intact here and gives adopters a route.

## Open questions

Whether the index's Active section should be renamed now that it can list planned work. Left
alone: it is a naming quibble, the status column disambiguates, and renaming is churn until it
demonstrably grates.
