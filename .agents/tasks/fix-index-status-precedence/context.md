# Context — fix-index-status-precedence

## Base state

`main` is at `51f6835`. The precedence sentence has been in `tasks/AGENTS.md` since the layer was
bootstrapped and has never been exercised in this repository, because no task here has been left
part-way through archival.

## References

- `.agents/tasks/AGENTS.md` — `## Finding work` states the precedence; `## Index conflicts`
  describes rebuilding rows from the task directories, which assumes the same thing.
- `decisions/0006-task-package-model.md` — where the index is defined as a derived view and
  `task.md` as the owner of canonical status.
- `decisions/0009-order-task-index-newest-first.md` — the index's ordering and regeneration
  rules, which are adjacent but not implicated.
- `decisions/0007-archive-before-merge.md` — archival is the operation that touches both files,
  which is why the window exists.

## Evidence

Two `ctxfold-init` runs adopting the `etu-forms` monorepo, in an untracked worktree on one
workstation. That is evidence no other reader can follow, so what matters is reproduced here.

The first run wrote the Outcome, moved the package to
`.agents/tasks/archive/2026-08-18-1605-adopt-context-fold/`, and updated `INDEX.md` to
`completed` — without setting Status in `task.md`, which stayed `active`. Its own final check
printed the disconfirming evidence and reported success anyway; that failure is
[[make-the-final-check-verifiable]], not this task.

The second run found `INDEX.md` saying `completed` and `task.md` saying `active`, and corrected
`task.md`. Its problem log records it: "The archived task initially retained `active` while
`INDEX.md` recorded `completed`; the canonical task status was corrected to keep the final
exact-head check consistent."

## Assumptions

- The lagging-canonical-file case is the common one, because `## Finishing` orders the Status
  edit first and the index update third, with the directory move between them. An interruption
  anywhere in that window leaves the index ahead. The reverse — an index edited without the task
  — requires someone editing the derived view directly, which the rules already discourage.

## Open questions

Whether the repair rule can be stated without reference to archival, so that it holds for
disagreements that arise some other way. Naming the mechanism makes it checkable; naming only the
symptom makes it general.
