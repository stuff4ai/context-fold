# Context — fold-worktrees-into-agents-template

## Base state

`skills/ctxfold-init/templates/agents/` holds three files that must stay byte-identical to their
installation forever: `AGENTS.md`, `tasks/AGENTS.md`, `tasks/archive/AGENTS.md`. Enforced by
`tests/test_conventions.py::test_installation_matches_the_distribution` (byte-compares everything
under `AGENT_TEMPLATES`), `test_distribution_is_complete` (set-equality between shipped and
installed `AGENTS.md` files, computed by `installed_layer_files()`), and
`test_portable_rules_carry_no_project_detail` (over the `PORTABLE` list).

`skills/ctxfold-init/templates/worktrees/AGENTS.md` sits outside that tree. It installs once to
`.agents/worktrees/AGENTS.md` and is never re-synced — no mechanical check covers its content at
all today. Its own text says so directly.

## References

- `decisions/0021-separate-what-upgrades-from-what-diverges.md` — established the byte-identical
  vs. diverges split.
- `decisions/0026-map-what-is-under-the-agents-directory.md` — classified `worktrees/AGENTS.md`
  into the diverges category specifically, and gave the reasoning this task's decision record
  narrows.
- `decisions/0029-drop-the-task-template.md` — the precedent for narrowing an accepted record
  (Status line only, body untouched) rather than rewriting it.
- `skills/ctxfold-init/ADOPTING.md` — the install-mapping table and the "If the layer is already
  there" re-adoption section, both describing the current three-way split.
- `.agents/AGENTS.md` — "What you will find under `.agents/`", where `tasks/` and `skills/` get
  explicit is/isn't-the-layer labels and `worktrees/` currently does not.
- `tests/test_conventions.py` — `installed_layer_files()` (`~line 238`), `PORTABLE` (`~line 35`),
  `installed_rule_files()` (`~line 207`, needs no change — picks up the moved file automatically
  via `AGENT_TEMPLATES.rglob("*")`).
- `.agents/worktrees/AGENTS.md` — carries the `gh pr merge` conflict-avoidance paragraph added
  earlier this session (task `2026-08-19-2059-avoid-worktree-merge-branch-conflict`); that content
  moves with the file, untouched, only the opening ownership sentence changes.

## Assumptions

- The re-adoption behavior change (existing `.agents/worktrees/AGENTS.md` customizations are now
  overwritten on reinstall, not preserved) has zero practical blast radius, since context-fold is
  its own only known adopter today. Recorded as a stated consequence regardless, not silently
  assumed away.

## Not relevant

The parallel `add-task-rfc` task (running in another worktree on this machine) touches
`.agents/tasks/AGENTS.md`, `plan.md`/`rfc.md`, and `README.md` — a different file set and a
different concern (task-package artifact shape, not the template/install split). Only shared
surface: `.agents/tasks/INDEX.md` (derived, rebuilt on conflict, not merged by hand) and decision
record numbering (provisional until merge, per `.agents/AGENTS.md`'s own rule).
