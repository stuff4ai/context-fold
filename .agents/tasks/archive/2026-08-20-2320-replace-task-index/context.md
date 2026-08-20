# Context

## Base state

- Initial base: `d7e4bd442317d15009a1f24b372e3b846465e87d` (`main`).
- PR #39, `feat/cross-stack-handoff`, was concurrent and owned the shared sections named in
  `task.md`. It merged as `14cfe724c52c75fc86c8e7d8c01fd8eb42b36bd7`.
- Final integration base: `b49f6f0fdced571909f0aead2da767b52e6f9a0c` (`origin/main` after
  PRs #39 and #40).

## References

- `.agents/tasks/AGENTS.md` — canonical task lifecycle and metadata rules.
- `.agents/worktrees/AGENTS.md` — this repository's concurrent-checkout workflow.
- `skills/ctxfold-init/` — distributable adoption skill and managed-rule templates.
- `tests/test_conventions.py` — executable repository and distribution invariants.
- `decisions/0006-task-package-model.md` — original task-package and index model.
- `decisions/0009-order-task-index-newest-first.md` — index-specific decision to supersede.
- `decisions/0012-build-the-methodology-before-the-tooling.md` — reason to defer query tooling.
- `decisions/0035-manage-portable-rules-as-replaceable-blocks.md` — managed-block ownership.

## Assumptions

- Context-fold currently has no external installation whose old task format must remain readable.
- PR #39 keeps provisional decision number `0036`; this task uses `0037` unless integration shows
  that `0036` became available again.
