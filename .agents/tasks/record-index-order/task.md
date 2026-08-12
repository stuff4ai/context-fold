# Record the task index order

## Status

active

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
