# Context — rules-for-concurrent-tasks

## Base state

`main` is at `ac192b5`. Twenty-five decision records, nineteen archived tasks, two `planned`
tasks queued. Every task so far has run alone, which is why none of this has been hit.

## References

- `.agents/tasks/AGENTS.md` — `## Index conflicts` is the only concurrency rule that exists, and
  is the model for the general one.
- `decisions/0000-use-decision-records.md` — a record on a branch is a proposal and becomes truth
  at merge, which is why renumbering before merge needs no new permission.
- `decisions/0009-order-task-index-newest-first.md` — the index is rebuilt from the task
  directories rather than merged by hand.
- `decisions/0024-settle-status-disagreements-by-the-directory.md` — the most recent case of two
  files describing one task and disagreeing; concurrency makes that ordinary rather than rare.
- `decisions/0022-route-findings-without-an-owning-task.md` — routes a finding with no owning
  task; silent on a finding with the wrong one.
- `decisions/0011-keep-the-model-vendor-neutral.md` — why the portable rules will not name git.
- `tests/test_conventions.py` — `IGNORED_DIRS` at line 54 and `markdown_files()` at 57.

## Base facts checked rather than assumed

`markdown_files()` walks `ROOT.rglob("*.md")` filtered by a hardcoded
`{".git", ".venv", ".idea", ".vscode"}`. It does not read `.gitignore`. `pymarkdown` is invoked
with `--respect-gitignore` and does. So a checkout under `.agents/worktrees/` would be invisible
to the linter and fully visible to the suite, which would then read a second copy of every
record, every archived task and every `AGENTS.md` as though it belonged to this repository.

An archive directory is `{YYYY-MM-DD-HHMM}-{slug}`, so two branches collide only by archiving in
the same minute under the same slug. `0009` records that as remote rather than impossible.

This section first claimed the collision was impossible, reasoning that two active tasks cannot
share a slug because the slug is the directory name. That holds inside one working tree and this
task introduces several, where each branch has a private `.agents/tasks/` and nothing on `main`
registers a slug in flight. The claim is left here as what it was — an assumption written under a
heading promising checked facts, and disproved by the change it was written for.

## Assumptions

- Parallel tasks will be few and short-lived — two or three branches, not twenty. Rules that
  depend on reading every other active task are affordable at that size and would not be at a
  larger one.
- Conflicts are resolved by a person or agent who can see both sides. Nothing here tries to
  prevent a conflict, only to say what resolving it means.

## Context conflicts

`0000` forbids renumbering accepted records, and this change relies on renumbering unaccepted
ones. That is not a conflict once the whole record is read — it draws the boundary at merge two
paragraphs earlier — but the two sentences are far enough apart that the first draft of this task
misread them.

## Open questions

Whether the layer should state, once and generally, that identity fixes at acceptance. It is now
established three times separately: `0000` for record numbers, `0022` for task slugs, and the
rename of `0022`'s own filename before it merged. The portable rules say it only about slugs, so
each new case has been rediscovered rather than derived.
