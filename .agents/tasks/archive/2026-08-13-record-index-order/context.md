# Context — record-index-order

## Base state

`main` is at `332c006`. `INDEX.md` already lists the archive newest first, applied in PR #2
without a rule behind it. Two tasks are archived, both dated 2026-08-13.

## References

- `decisions/0006-task-package-model.md` — the index is a derived view; `task.md` owns status.
- `decisions/0007-archive-before-merge.md` — dated archive directories.
- `decisions/0005-agents-layer-boundary.md` — the portable/instance split within `.agents/`.

## Assumptions

- The archive grows without bound and is never pruned.
- Dated directory prefixes remain the source of chronology, so the index is free to order for
  reading.

## Context conflicts

The change was made before the rule was recorded, which inverts the normal order. It was
agreed deliberately — the reordering was mechanical and reversible, and separating it kept the
previous pull request focused. This task closes the gap.

## Open questions

- Two archived tasks share a date, so the prefix alone does not order them. Sorting is stable
  only to the day. Whether that matters depends on how many tasks a day a project completes;
  not resolved, because one day of evidence cannot answer it.
- Whether other derived views, if any appear, should follow the same rule or decide
  separately.

## Not relevant

- Sorting of `decisions/`, which is numbered and read in dependency order.
