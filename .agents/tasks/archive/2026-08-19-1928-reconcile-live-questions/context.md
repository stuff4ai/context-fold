# Context — reconcile-live-questions

## Base state

PR #27 is merged on `origin/main`. Its final head contains correction `27c5479`, its merge commit
is an ancestor of the task base, and every path it touched matches the merge result. The
repository has twenty-five archived tasks: twenty-three put `## Outcome` before `## Problems`
and two put it after.

## References

- `README.md` — the project front door and one source of stale layer/status language.
- `OPEN-QUESTIONS.md` — the live project-layer destination for unresolved questions.
- `decisions/0012-build-the-methodology-before-the-tooling.md` — artifact-producing lifecycle
  tooling remains deferred while convention checks exist.
- `decisions/0013-improve-context-from-the-work.md` — promotion of repeated problems remains a
  manual judgment.
- `decisions/0018-ship-a-distribution.md` — separates the layer from the directory and scopes
  the deletion test to layer-owned files.
- `decisions/0020-ship-an-init-skill.md` — establishes `ctxfold-init` as an adapter over the
  canonical adoption procedure.
- `decisions/0021-separate-what-upgrades-from-what-diverges.md` — separates replaceable rule
  files from installation-owned state.
- `decisions/0026-map-what-is-under-the-agents-directory.md` — records the heterogeneous owners
  under `.agents/`.
- `decisions/0029-drop-the-task-template.md` — removes the task skeleton without changing the
  manually maintained task lifecycle.
- `decisions/0030-add-a-claude-code-adapter.md` — adds one repository-local host adapter while
  leaving distribution to heterogeneous hosts unresolved.
- `skills/ctxfold-init/ADOPTING.md` and `skills/ctxfold-init/SKILL.md` — current adoption
  behavior and its explicit limits.

## Not relevant

- Portable rule templates and convention checks are evidence only; this task does not change
  them.
