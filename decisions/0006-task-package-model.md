# Organize work as task packages

## Status

Accepted. Two parts are narrowed by
[0022](0022-route-findings-without-an-owning-task.md): the requirement that `task.md` carry
`## Problems`, to tasks that have started, and slug identity, which fixes at acceptance rather
than at the start of work. The rest stands.

## Context

Agent work needs a unit that survives between sessions. Without one, each session
reconstructs the objective, the scope, and the reasoning from a transcript that the next
agent cannot see.

Ticket identifiers such as `TASK-042` solve identity but introduce a numbering mechanism the
repository must maintain, and produce paths that say nothing about their contents.

Task systems tend toward ceremony: a full set of artifacts per task, most of them empty, most
of them abandoned within weeks.

Recording friction is the distinctive claim of this project — repeated problems should become
lessons, and lessons should improve the context the next agent reads. That requires the
friction to be captured while it happens. Retrospective recall does not work; the wrong
assumption made on Tuesday is not remembered on Friday.

## Decision

Work is organized as task packages under `.agents/tasks/{slug}/`.

Tasks are identified by descriptive slug — `bootstrap-tasks-layer`, not `TASK-042`. The slug
becomes stable identity once work starts and is not renamed when wording changes. The title
inside `task.md` may evolve independently.

A package contains:

- `task.md` — the contract. Status, Objective, Why, Scope, Out of scope, Acceptance. Before
  archival, the final Status and an Outcome describing what happened and which durable
  artifacts it produced. It carries no context dumps and no execution history.
- `context.md` — a curated context map for this task: references to relevant project
  artifacts, why they matter, and task-local facts. It prefers references over copies.
  Assumptions, open questions, context conflicts, base state, and explicit non-relevance are
  optional sections.
- `plan.md` — mutable execution strategy. Optional; created when a task is multi-step,
  complex, long-running, or likely to be resumed by another agent. It is not an execution
  log.

`task.md` additionally carries a `## Problems` section, appended to during work: a few lines
per entry recording what happened, what was assumed, and what was actually true. It is the
only place execution friction is recorded, and it is the input to any future learning layer.

`.agents/tasks/INDEX.md` is a derived navigation view for discovery. Each task's `task.md`
owns its canonical status. When the two disagree, `task.md` wins and the index is repaired.
Because every concurrent task edits the index, merge conflicts in it are expected and are
resolved by regenerating from the task directories rather than by hand.

Workflows and skills are not part of this model. The lifecycle lives in
`.agents/tasks/AGENTS.md`, and reusable procedures should appear only when repeated patterns
justify them.

## Consequences

Paths are meaningful, and no numbering mechanism is needed.

A task is resumable by an agent with no memory of how it started.

Friction has a home from the first task, so the evidence for later improvements accumulates
from the beginning instead of being reconstructed.

Slugs must be chosen before the shape of the work is fully known, and a task that changes
character mid-flight keeps a name that no longer fits. Renaming is worse than the mismatch.

Two of three files are mandatory even for small tasks. If that proves too heavy in practice,
the evidence will be in the problem logs.
