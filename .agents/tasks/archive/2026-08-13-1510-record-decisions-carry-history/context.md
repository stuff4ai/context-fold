# Context — record-decisions-carry-history

## Base state

`main` is at `6f4069f`. Fourteen decision records, seven archived tasks, no active work.

The `history/` directory was built on a branch, committed, and reset before being pushed. It is
in no commit that reached `main`, so nothing in the repository refers to it and nothing needs
removing.

## References

- `decisions/0000-use-decision-records.md` — Context, Decision, Consequences, and `Status` as
  the one mutable field. The mechanism this decision relies on.
- `decisions/0013-improve-context-from-the-work.md` — the loop whose promotion step this task
  locates.
- `.agents/tasks/archive/AGENTS.md` — immutable material that is explicitly not current truth,
  which is the precedent that made storing sources look safe.

## Assumptions

- The eight instances of duplication recorded across seven task problem logs are enough to
  treat "a second unstructured copy drifts" as established rather than predicted.
- The recurring-patterns section performs the promotion whether or not anything says so. This
  task documents it; it does not create it.

## Context conflicts

The rejected approach had a real argument behind it, and an earlier decision record was written
arguing for it before being reverted. Recording the decision the other way risks presenting the
alternative as obviously wrong. It was not — the Context is written to make the case for it.

## Open questions

None raised by this task.
