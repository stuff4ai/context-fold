# Guard against leftover scaffolding in a task package

## Status

planned

## Objective

Decide whether to add a mechanical check that catches leftover instructional prose, empty
optional headings, or duplicated headings surviving into a task package's real content — and
implement it if the decision is yes.

## Why

`decisions/0029-drop-the-task-template.md` removed `templates/task/` because, across seven
measured adoption runs, copying it was the only mechanism shown to leave placeholder or
instructional text in a finished task package. Removing the template closes that one vector.

Nothing stops the same failure through a different path: modeling a new `task.md` on an old
archived package and keeping a line that was never meant as content, or copying `ADOPTING.md`'s
task-zero prose without trimming it once it no longer applies. `tests/test_conventions.py`
checks that a task package has the required files and sections; it does not read whether what
sits in a section is real content or leftover scaffolding.

Raised as a review finding on the pull request that removed the template
(`decisions/0029-drop-the-task-template.md`) and deferred as out of scope there, because that
task's acceptance was a decision about the template, not a guard against every path to the same
failure.

## Scope

- `tests/test_conventions.py` — whether and how to extend it.
- `.agents/tasks/AGENTS.md`, if a new authoring rule follows from the decision.

## Out of scope

- Re-opening whether `templates/task/` should exist. `decisions/0029-drop-the-task-template.md`
  settled that.
- General content-quality review of task packages. Only leftover scaffolding — unfilled
  placeholders, instructional prose copied from `ADOPTING.md` or another package, empty optional
  headings, duplicated headings — is in scope; judging whether an entry is well-written is not.

## Acceptance

1. A decision, recorded: whether a mechanical check is added, and if not, why not.
2. If added: the check runs in the existing `pytest` suite and CI, and its false-positive and
   false-negative risk is stated. A check that flags real content as scaffolding, or misses real
   scaffolding, is worse than no check — the four `etu-forms` defects it would need to catch are
   the concrete cases to test it against.
