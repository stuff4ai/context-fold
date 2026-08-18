# Fix which file wins when the index and a task disagree

## Status

planned

## Objective

Correct the precedence rule so it repairs the file that is actually stale, rather than always
assuming the index is.

## Why

`tasks/AGENTS.md` says the index is a derived view and that `task.md` owns canonical status: "if
this table disagrees with a task file, the task file is right and this table needs repair."

A foreign adoption run produced the opposite case. Archiving updates two things — the task's
Status and the index row — and the agent finished one. `INDEX.md` said `completed`; the archived
`task.md` still said `active`. A second agent found the disagreement and corrected `task.md`,
against the letter of the rule, and was right to.

The rule assumes disagreement means the derived view drifted. The observed failure mode is the
canonical file lagging, because it is updated first and the archival move happens between the two
edits. Following the rule literally would have reverted a finished task to `active` and put the
index back in step with a lie.

This is a defect in a portable rule, so every installation currently has it. It was unreachable
from this repository: no task here has ever been left half-archived.

## Scope

- `templates/agents/tasks/AGENTS.md` — the precedence sentence under `## Finding work`, and
  anything in `## Index conflicts` that inherits from it.
- A decision record, and whatever `0006` or `0009` need in their Status.

## Out of scope

- Making the index generated rather than hand-maintained. That is deferred capability, and this
  rule has to be right either way.
- The ordering rules for the index, which are `0009`'s and are not implicated.

## Acceptance

1. The rule says how to tell which file is stale rather than assuming, and an agent reading it
   would have corrected `task.md` in the observed case.
2. The reasoning names the failure mode: archival updates two files and can stop between them.
3. Every statement of precedence across the rules agrees.
