# Context — add-ctxfold-tasks-skill

## References

- `.agents/tasks/AGENTS.md` — task-package lifecycle, artifact ownership, and archival rules.
- `README.md` — human-facing task model and the boundary between task metadata and project truth.
- `.agents/tasks/AGENTS.md` — task discovery and lifecycle rules after removing the derived index.
- `.agents/tasks/archive/2026-08-20-1505-add-task-rfc/context.md` — earlier note that the proposed
  `ctxfold-tasks` listing skill was separate from task-frontmatter work.
- `.agents/tasks/archive/2026-08-20-2320-replace-task-index/task.md` — migration outcome that
  explicitly deferred agent query tooling and a supported human CLI.

## Discussed direction

- The first supported consumer is an agent invoking an automatically and explicitly invocable
  `ctxfold-tasks` skill; a human-facing CLI remains future work.
- The default view is `unfinished`, containing planned and active tasks. The supported views are
  `unfinished`, `archive`, and `all`.
- Results are machine-readable JSON and retain each observation's source-relative path and useful
  diagnostics rather than flattening the repository into another index.
- Discovery covers the repository and registered Git worktrees, including nested
  `.agents/worktrees/...` checkouts.
- The logical identity is the task slug. For one slug observed in multiple worktrees, select the
  most advanced status using `planned < active < completed/cancelled`; for terminal ties, the later
  archive-directory timestamp wins with a warning.
- Equal-highest-status observations with differing task content are ambiguous and must remain
  visible as a conflict rather than being silently discarded.
- Task lifecycle mutation (start, complete, archive, cancel) is a separate future capability.

## Assumptions

- The first supported consumer is an agent invoking a skill; human ergonomics can be designed later
  without constraining the initial machine-readable contract.
- A logical task is identified by its active slug, with an archived directory's timestamp treated
  as archive metadata rather than part of that identity.
- The task package's own `task.md` remains authoritative for status; filesystem location remains
  authoritative for unfinished versus archived state.

## Open questions

- Which worktree registrations are in scope, and how should missing or inaccessible checkouts be
  reported?
- Should conflicting task bodies at the same highest status be an error, a warning with all sources,
  or both depending on the requested view?
- What exact JSON envelope and exit behavior should the skill expose to agents?
- Which malformed task packages are omitted, surfaced as diagnostics, or fail the query?

## Not relevant

- Designing a human CLI.
- Mutating task lifecycle commands.
- Restoring a hand-maintained task index.
