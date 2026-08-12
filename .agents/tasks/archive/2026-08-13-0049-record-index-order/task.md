# Record the task index order

## Status

completed

## Objective

Record that the task index is ordered newest first, and state the rule in the portable tasks
instructions.

## Why

The index was reordered newest first in PR #2 without the convention being written down, so
the ordering currently holds by example rather than by rule. The next task appending a row has
nothing to follow.

The rule belongs in `.agents/tasks/AGENTS.md`, which is portable and identical in every
project using context-fold. Changing it changes every installation, and the portable file
cannot carry its own rationale — hence a decision record here.

## Scope

- `decisions/0009-order-task-index-newest-first.md`.
- `decisions/README.md` index row.
- `.agents/tasks/AGENTS.md` — the ordering rule and its effect on regeneration.

## Out of scope

- The `0003` sign-off ambiguity, still open from the previous task.
- Automated index generation.
- Any change to the task package model or the archive.

## Acceptance

1. The ordering and its rationale are recorded in one decision record.
2. `.agents/tasks/AGENTS.md` states the order and the regeneration sort, and carries no
   project-specific detail.
3. The index row is added and the record is linked.
4. `INDEX.md` already satisfies the rule; no reordering is needed.

## Outcome

The ordering is recorded in `decisions/0009-order-task-index-newest-first.md`, and the rule
plus its regeneration sort are stated in `.agents/tasks/AGENTS.md`. `decisions/README.md`
carries the index row.

All four acceptance criteria satisfied. The fourth needed a correction first: with three
same-day tasks the day-only prefix placed the newest second, so `0009` was amended before merge
to use a `{YYYY-MM-DD-HHMM}` prefix. That supersedes the archive naming in `0007`, whose
`Status` now points at `0009`; the rest of `0007` stands. Existing archive directories were
renamed from the timestamps of their archival commits.

This task changed a portable rule file, so it applies to every project using context-fold.

Nothing was left to fold.

## Problems

### The regeneration rule appears to work but is untested

Sorting the two archived directories by name descending reproduces the index exactly, which
looks like confirmation that the rule is correct.
Assumed: matching output means the sort orders tasks by recency.
Actually: both tasks share the date `2026-08-13`, so the prefix contributes nothing and the
order came from comparing `record-merge-strategy` against `bootstrap-tasks-layer`
alphabetically. It matched completion order by accident. The rule has not actually been
exercised on tasks from different days, and a same-day pair whose slugs sort the other way
would produce a wrong-looking index that is still "correct" by the rule.
The check that passed here proves the sort is deterministic, not that it is meaningful.

### The limitation materialized on the rule's first application

Archiving this task gave three same-day directories. Sorting by name descending yields
`record-merge-strategy`, `record-index-order`, `bootstrap-tasks-layer` — placing the newest
task second, below one completed before it.
Assumed: the day-granularity limit was a theoretical edge case worth noting in consequences.
Actually: it appeared on the very next task, because a project working in a single session
completes several tasks a day. The index now shows an order that is correct by the rule and
wrong by the rule's stated purpose of putting the most recent work at the top.
Followed the rule as recorded rather than deviating from it silently — `0009` explicitly said
within-day order is not meaningful, so this was the documented behavior, not a violation. But
the purpose and the mechanism disagreed after one use, which was reason enough to fix the rule
rather than wait for more evidence.

Resolved before merge by moving the prefix to `{YYYY-MM-DD-HHMM}`, which orders by recency and
makes a same-name collision between concurrent branches remote rather than likely. Existing
directories were renamed using the timestamps of their own archival commits.

### Superseding a record turned out to be partial, and the model has no word for it

The archive path format was set by `0007`, which is merged and accepted. Changing it meant
superseding a record that also carries the archive-before-merge decision, which is untouched.
Assumed: supersession replaces a whole record, as `0000` describes.
Actually: records bundle several decisions, and a later one usually contradicts only part of
an earlier one. Replacing `0007` wholesale would have meant restating a decision nobody
disputes, purely to satisfy the form. Handled by pointing `0007`'s `Status` at `0009` and
saying what was superseded — `Status` is the one field an accepted record may change, so this
stays inside the rules — but `0000` describes no such thing, and the wording had to be
invented here.
