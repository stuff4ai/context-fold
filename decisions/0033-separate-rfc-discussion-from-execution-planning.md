# Separate RFC discussion from execution planning

## Status

Accepted. Narrows [0006](0006-task-package-model.md)'s task-package model and applies
[0010](0010-record-open-questions-in-project-layer.md),
[0014](0014-do-not-store-source-material.md), and
[0015](0015-stages-are-not-one-way.md) to proposal discussion.

## Context

`0006` gives an optional `plan.md` two properties: it is an execution strategy, and it stays
mutable while work proceeds. A conversation before execution has a different shape. Its current
proposal, alternatives, questions, and review feedback are deliberately unsettled. Putting that
material in `plan.md` leaves a resumed agent unable to tell whether the document is executable or
still asks for a direction to be chosen.

Making `plan.md` immutable would resolve that ambiguity by creating another one. Durable decisions
belong in project-owned artifacts, not in the removable agent layer, while tactical execution
details still have to adapt to facts found during work. "Final" can mean that a direction has been
selected without meaning that every step is frozen.

Keeping the source conversation is also not the answer. `0014` rejects raw transcripts and notes
because they become a second, drifting source. The task needs curated working context, not stored
source material or hidden reasoning.

## Decision

A task package may contain `rfc.md`, an optional mutable artifact for a curated proposal while its
direction is unsettled. It may carry the problem, current proposal, alternatives, task-local open
questions, and review notes in whatever body structure makes the discussion clear. It is not a raw
transcript, an execution log, or durable project authority.

An RFC starts with exactly this three-line frontmatter block:

```yaml
---
status: draft
---
```

The value changes to `resolved` when the direction is selected. The deliberately minimal grammar
has delimiter lines containing `---` and exactly one field. It does not introduce a general
metadata schema or require a YAML parser.

A draft RFC has no `## Resolution`. A resolved RFC has exactly one non-empty `## Resolution` that
states the selected direction. The Resolution may point to the reconciled task contract or a
project decision, but does not duplicate durable reasoning.

Substantive RFC discussion, review, or evidence gathering is work and makes a task `active` under
the existing status model. A `planned` task may have no RFC or an initial draft, but not a resolved
RFC. Implementation is a separate gate: when an RFC exists, implementation does not begin until
the RFC is resolved and `task.md` agrees with it.

`plan.md` remains optional execution strategy. When an RFC exists, a plan may exist only while the
RFC is resolved. Its chosen direction agrees with the Resolution and task contract, while tactical
details remain mutable as execution reveals facts. A task without an RFC follows the existing plan
rule unchanged.

Reopening is a transition, not a third RFC status. Before reopening, fold any still-relevant facts,
rationale, questions, and durable outcomes out of the current Resolution and plan. Then change the
RFC to `draft`, remove `## Resolution`, record why in its review notes, remove the invalid plan, and
pause implementation. Removal is intentional disposal after folding, not reliance on Git having
preserved an uncommitted file. A new Resolution is required before returning to `resolved`.

The supported combinations are:

| Task status | RFC status | Resolution | `plan.md` |
| --- | --- | --- | --- |
| `planned` | absent | n/a | Existing rule |
| `planned` | `draft` | absent | Absent |
| `active` | absent | n/a | Existing rule |
| `active` | `draft` | absent | Absent |
| `active` | `resolved` | present | Optional |
| `completed` | absent | n/a | Existing rule |
| `completed` | `resolved` | present | Optional |
| `cancelled` | absent | n/a | Existing rule |
| `cancelled` | `draft` | absent | Absent |
| `cancelled` | `resolved` | present | Optional |

An RFC's open questions are task-local. Before completion or cancellation, anything that may
outlive the task is folded into the project layer under `0010`. A completed task cannot archive a
draft RFC; a cancelled task may, because abandonment can end discussion without selecting a
direction.

## Consequences

A resumed agent can tell from the task package whether to continue discussing a direction or
execute the selected strategy. `task.md`, `rfc.md`, `plan.md`, and project artifacts each retain one
responsibility instead of competing for authority.

Small tasks pay nothing: both RFC and plan remain optional. A task that needs proposal discussion
pays for a frontmatter field, a Resolution transition, and reconciliation before implementation.

Reopening is deliberately lossy after folding. The live package exposes no stale Resolution or
executable-looking plan, but discarded tactical detail is not preserved merely for history.

Mechanical checks can establish the frontmatter grammar and lifecycle matrix. They cannot decide
whether an RFC is well argued, its Resolution is correct, or a question should outlive the task;
those remain review judgments.
