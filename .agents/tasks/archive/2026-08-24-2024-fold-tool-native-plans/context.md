# Context

## Base state

- `.agents/tasks/AGENTS.md` — installed managed block; source is
  `skills/ctxfold-init/templates/agents/tasks/AGENTS.md`. Fully defines `rfc.md` and `plan.md`
  (lines ~121–150 before this task's edit) but says nothing about tool-native planning output.
- `decisions/0011-keep-the-model-vendor-neutral.md` — the portable layer names no product and
  assumes no tool's layout; an adapter, if one exists, sits over the model and is never its
  source of truth.
- `decisions/0030-add-a-claude-code-adapter.md` and
  `decisions/0034-extend-the-claude-code-adapter-to-skills.md` — the adapter pattern this task
  deliberately does *not* need: both exist because Claude Code doesn't read something without
  help. This task's rule names no product, so nothing analogous is required for it.
- `decisions/0033-separate-rfc-discussion-from-execution-planning.md` — shapes this task's
  decision record; the closest precedent for a change to `rfc.md`/`plan.md`'s own lifecycle
  rules rather than a new file or an adapter.
- `decisions/0035-manage-portable-rules-as-replaceable-blocks.md` — the managed-block mechanics
  this task's reinstall step follows.
- `decisions/0042-require-merge-ready-decision-status.md` — landed on `main` while this task's
  plan was being written (see `task.md`'s Problems). Requires this task's own decision record to
  read `## Status` `Accepted`, matching its index row, before archival — not `Proposed`.
- Root `AGENTS.md`'s own project rule (non-portable, appended after the managed block): "After
  changing `skills/ctxfold-init/templates/`, reinstall the complete skill into
  `.agents/skills/ctxfold-init/`, invoke that installed skill to update the managed rule blocks,
  and verify block parity before finishing." This task follows that rule exactly.
- `tests/test_conventions.py` — `RFC_FRONTMATTER`, `DECISION_INDEX_ROW`, and the
  `decision_status`/`merge_ready_decision_status` helpers encode the frontmatter and status
  formats this task's new decision record and unchanged `rfc.md` frontmatter must satisfy.

## Not relevant

- `README.md`'s task-file summary table (`## Tasks`) — checked; it's a one-line-per-file summary
  and doesn't need this rule spelled out at that level of detail.
