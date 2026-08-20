---
status: planned
objective: >-
  Provide agents with a supported way to discover unfinished and archived context-fold tasks
  across the repository and its registered Git worktrees.
---

# Add the ctxfold-tasks query skill

## Why

The task-index migration deliberately removed the private listing helper and did not provide a
human CLI. The follow-up now needs a durable task contract before implementation starts, while
keeping the agent query interface separate from future human tooling.

## Scope

- An agent-only `ctxfold-tasks` skill with a documented invocation and output contract.
- A private helper bundled with the skill, if the selected design still needs one.
- Discovery of task packages in the repository and registered nested worktrees, including
  unfinished and archived packages.
- Deterministic grouping of the same logical task across worktrees, status precedence, timestamp
  tie handling, and ambiguity diagnostics.
- Skill installation, documentation, and convention checks required by the selected design.
- This task's RFC or plan, if design questions need to be settled before implementation.

## Out of scope

- A supported human-facing CLI; that is a later interface.
- Mutating task lifecycle operations such as starting, completing, archiving, or cancelling tasks.
- Reintroducing a repository-wide `INDEX.md` as the query source of truth.
- Copying task contents into a second index or durable project knowledge store.

## Acceptance

1. A resolved design defines the skill's invocation, default view, output schema, source paths, and
   behavior for malformed, duplicated, or ambiguous task packages.
2. The skill discovers tasks from the repository and registered worktrees without treating the
   derived index as authoritative.
3. Cross-worktree grouping and status selection are deterministic and preserve source paths and
   diagnostics when content conflicts.
4. The implementation, installation path, documentation, and checks required by the resolved
   design are complete, while human CLI and mutating lifecycle operations remain separate.
5. The final task outcome records any durable design decision in the project layer before archival.

## Approval

Human.
