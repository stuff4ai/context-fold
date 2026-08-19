# Context — add-task-rfc

## Base state

The task model defines `task.md` and `context.md` as required and `plan.md` as an optional,
mutable execution strategy. Across the accepted history, only the bootstrap task contains a
`plan.md`; it labels itself mutable and uses the file for ordering and execution steps. No task
contains `rfc.md`.

## References

- `decisions/0006-task-package-model.md` — the accepted task-package contents and current mutable
  meaning of `plan.md`.
- `decisions/0014-do-not-store-source-material.md` — the boundary against preserving raw source
  conversations instead of curated outcomes.
- `.agents/tasks/AGENTS.md` — the portable lifecycle and artifact responsibilities an agent
  follows.
- `README.md` — the human-facing summary of task artifacts.
- `.agents/tasks/archive/2026-08-13-0023-bootstrap-tasks-layer/plan.md` — the only accepted use of
  `plan.md` and evidence for its current execution-strategy role.
- `OPEN-QUESTIONS.md` — the live home for unresolved project-level questions that must not be
  buried in a task RFC.

## Not relevant

- The proposed `ctxfold-tasks` listing skill and task frontmatter are separate possible changes.
- The planned reorganization of `OPEN-QUESTIONS.md` is a later task after this artifact boundary
  is settled.
