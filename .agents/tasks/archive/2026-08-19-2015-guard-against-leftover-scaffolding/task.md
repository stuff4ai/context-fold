# Guard against leftover scaffolding in a task package

## Status

completed

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

## Problems

- While setting up this task's worktree, read a sibling worktree's (`reconcile-live-questions`)
  `git log` and commit diff, looking for a branch- and commit-naming pattern to copy. Assumed a
  worktree's own history was reusable precedent. `.agents/worktrees/AGENTS.md` only sanctions
  opening another task's `task.md` there ("to see what it claims") — its git history is another
  copy's, and reading it "produces a second and contradictory version of every record and task
  package." Corrected by using `git branch -a` at the repository root instead, which already
  showed the same convention (`docs/reconcile-live-questions` off `main`, worktree dir dropping
  the type prefix).

- Assumed, from `test_task_package_has_required_files` being the only content-adjacent check in
  `tests/test_conventions.py`, that a duplicated heading in a task package was entirely unguarded.
  Wrote and ran a mechanical check for it before checking `.pymarkdown.json`, which already
  enables MD024 (`siblings_only`) — confirmed by reproducing the `etu-forms` duplicated-`##
  Problems` shape in a scratch file and running `pymarkdownlnt` against it directly, which flagged
  it. `tests/test_conventions.py` covers structural invariants specific to this repository; Markdown
  shape rules generic enough for `pymarkdownlnt`'s defaults live in `.pymarkdown.json` instead,
  per `decisions/0016-check-conventions-in-ci.md`. Dropped the redundant pytest check; the empty
  optional-heading check, which no existing tool catches, stayed.

## Outcome

Recorded as `decisions/0031-check-task-packages-for-scaffolding-by-shape.md`: a mechanical check
is added, but only for one of the four `etu-forms` defects. The other three split two ways —
the duplicated-heading defect was already covered by `pymarkdownlnt`'s MD024 (`siblings_only`),
enabled in `.pymarkdown.json` before this task started, so nothing new was needed there; the two
instructional-paragraph defects have no mechanical check that can distinguish copied instruction
from this project's own legitimate quotation of its rule text, and adding one was rejected rather
than deferred.

Durable artifacts:

- `decisions/0031-check-task-packages-for-scaffolding-by-shape.md` — the decision, its reasoning,
  and the stated false-positive/false-negative risk, added to `decisions/README.md`.
- `tests/test_conventions.py::test_archived_task_has_no_empty_optional_heading` — the new check,
  covering the one previously-unguarded defect.
- `.agents/tasks/AGENTS.md` — one sentence: an unfilled optional heading is left out, not kept
  empty against a later archival. Installed identically into `skills/ctxfold-init/templates/agents/tasks/AGENTS.md`
  and `.agents/skills/ctxfold-init/templates/agents/tasks/AGENTS.md`.

`pytest` (292 tests) and `pymarkdownlnt --config .pymarkdown.json scan -r --respect-gitignore .`
both pass at this state, run exactly as `.github/workflows/ci.yml` runs them.
