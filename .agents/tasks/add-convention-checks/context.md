# Context — add-convention-checks

## Base state

`main` is at `0a828d9`. Sixteen decision records, nine archived tasks, no CI, no tests, no
language toolchain in the repository.

The repository is entirely Markdown. This task adds the first non-prose files.

## References

- `decisions/0012-build-the-methodology-before-the-tooling.md` — the record this must be
  reconciled with. Its argument is against tooling that makes the methodology cheaper to follow;
  verification tooling produces nothing and only makes violations visible.
- `decisions/0005-agents-layer-boundary.md` and `0011-keep-the-model-vendor-neutral.md` — the
  portability commitment the most valuable check enforces.
- `decisions/0009-order-task-index-newest-first.md` — the index ordering and regeneration sort,
  which the index check verifies.
- `.agents/tasks/AGENTS.md` — the final exact-head check, which is the manual version of most of
  this.

## Assumptions

- Every invariant worth checking already exists as a decision. The suite encodes decisions; it
  does not introduce rules.
- The current tree satisfies all of them. If a check fails on unmodified content, the check is
  wrong rather than the content — nine tasks of prose are the specification here.

## Context conflicts

`0012` says v0 is plain files and Git with no tooling, and `README.md` repeats it. Adding a test
suite and CI makes that literally false as stated. The distinction between tooling that produces
and tooling that verifies has to be recorded, or `0016` reads as an exception to `0012` rather
than something outside its scope.

## Open questions

Whether the checks should eventually ship with the portable layer is raised in
`OPEN-QUESTIONS.md` by this task. They encode portable rules, so every installation would want
them, but distribution is deferred and shipping executable content is a larger question than
shipping Markdown.
