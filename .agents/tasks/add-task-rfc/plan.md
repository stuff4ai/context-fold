# Plan — add an RFC artifact to task packages

## Strategy

Extend the accepted task-package model with an optional, state-bearing RFC while preserving one
authority for each kind of information: `task.md` remains the contract, `rfc.md` holds unsettled
task-local discussion, `plan.md` holds the selected execution strategy, and project artifacts hold
durable truth.

## Steps

1. Integrate `origin/main` at or beyond `0a4d777`, which contains the accepted former concurrent
   task and decision `0032`. Confirm that no new active task claims the exact sections in this
   task's Scope before editing shared files.
2. Add provisional decision `0033`, defining the RFC lifecycle, artifact boundaries, state matrix,
   reopening behavior, and folding obligations. Add it to the table in `decisions/README.md` and
   narrow `decisions/0006-task-package-model.md` through its Status. If another record lands first,
   renumber the filename, index row, `0006` Status link, test rationale, and every other reference
   atomically before verification.
3. Update `README.md`'s `## Tasks` artifact summary. Resolve the task-local-choice entry in
   `OPEN-QUESTIONS.md` and narrow its metadata-schema entry to preserve the broader question beyond
   this deliberately minimal RFC field.
4. Update `## The files`, `## Status`, `## Stages`, and `## Finishing` in the shipped portable task
   rules, then reinstall that changed `AGENTS.md` into the installed skill and this repository so
   all three copies are byte-identical. Do not copy `INDEX.md`.
5. Implement a dependency-free recognizer for the exact three-line frontmatter block selected by
   the RFC. Add isolated positive cases for every matrix row: planned, active, completed, and
   cancelled packages without an RFC; planned/active/cancelled draft RFCs; and
   active/completed/cancelled resolved RFCs, including both allowed plan-presence variants where an
   RFC is resolved. Add negative cases for malformed frontmatter, unknown status, planned resolved,
   draft with Resolution, draft with a plan, resolved without a non-empty Resolution, and completed
   with a draft RFC. Do not add a YAML dependency.
6. Run focused state-matrix and decision integration tests while iterating, then the full pytest
   suite, recursive Markdown lint, explicit portable-file byte comparisons, and `git diff --check`.
7. Fold the outcome into project artifacts, write the task Outcome, archive the package, update the
   index, and produce criterion-by-criterion exact-head evidence before review.

## Stop conditions

- Stop and reopen the RFC if implementation requires a different artifact authority or lifecycle
  state than the Resolution defines.
- Stop for coordination if a new active task claims one of this task's named sections after the
  base check, or if the provisional decision number changes without every reference changing in
  the same diff.
