---
status: resolved
---

# RFC — separate proposal discussion from execution planning

## Problem

A chat plan can contain a direction, alternatives, unanswered questions, and review feedback that
change during discussion. The current task package has nowhere to curate that material except
`plan.md`, but the same file is also the execution strategy used after a direction has been
chosen.

Those are different states. Mixing them makes it hard for a resumed agent to tell whether it may
execute the document or should continue discussing it.

## Current proposal

Add optional `rfc.md` as the task-local, mutable proposal artifact. It may contain the problem,
current proposal, alternatives, open questions, and review notes in whatever structure makes the
discussion clear. It is curated working context, not a stored transcript. Its open questions are
task-local; any unresolved question that may outlive the task is folded into the project layer
before the task is accepted, including when the task is cancelled.

Once the direction is resolved:

1. Fold durable decisions into project-owned documentation or a decision record.
2. Make `task.md`'s objective, scope, and acceptance agree with the selected direction.
3. Write `plan.md` when the execution is complex enough to need one.
4. Keep the RFC as historical task context rather than treating it as current project authority.

`plan.md` is final in the sense that the direction has been selected, not immutable. Tactical
steps may change as execution reveals new facts. A change to the chosen direction reopens the RFC
and requires the task contract and plan to be reconciled again before execution continues.

## Artifact responsibilities

| Artifact | Responsibility |
| --- | --- |
| `task.md` | Authoritative task contract: objective, scope, exclusions, and acceptance |
| `context.md` | Curated references and task-local facts |
| `rfc.md` | Mutable discussion while the direction is unsettled |
| `plan.md` | Selected execution strategy after the direction is settled |
| Project documentation or decision record | Durable authority that survives removal of the agent layer |

## Resolution

### RFC state

Require a deliberately minimal YAML frontmatter block at the start of the file: delimiter lines
containing `---` and exactly one field, `status: draft` or `status: resolved`. No YAML dependency is
needed to recognize that grammar. Task cancellation already represents abandonment, so the RFC
does not need a separate `withdrawn` state. This keeps machine-readable lifecycle state separate
from the free-form discussion body without introducing a general metadata schema.

### Resolution and plan

When an RFC exists, require a written `## Resolution` before creating `plan.md`. The resolution
states the selected direction and may point to the reconciled task contract or a project decision;
it does not duplicate durable reasoning. A task without an RFC may still create `plan.md` directly
once its direction is settled.

If a direction changes after resolution, first fold still-relevant facts, rationale, and durable
outcomes out of the Resolution and existing plan. Then change the RFC back to `draft`, remove its
now-obsolete `## Resolution`, summarize why it was reopened in Review notes, remove the invalid
`plan.md`, and pause execution. A new current Resolution is required before the RFC returns to
`resolved`; the task contract and replacement plan must agree with it before execution continues.
Removal is intentional disposal after folding, not an assumption that Git history preserved an
uncommitted artifact.

### Task status while discussing

An RFC may be drafted while its task is `planned`, before substantive work starts. Change the task
to `active` when RFC discussion, review, or evidence gathering begins. A task may therefore be
active with a draft RFC, but implementation does not begin until the RFC is resolved and the task
contract is reconciled. If an active task reopens its RFC, it stays active under the existing rule
that returning to an earlier stage does not change task status, while execution pauses.

### Open questions and finished tasks

RFC questions are task-local working context. Before either completion or cancellation, fold any
question that remains relevant beyond the task into the project layer. A completed task with an RFC
must archive it as `resolved`; a cancelled task may archive either a draft or resolved RFC because
cancellation may end discussion without selecting a direction.

The supported combinations are:

| Task status | RFC status | Resolution | `plan.md` |
| --- | --- | --- | --- |
| `planned` | absent | n/a | governed by the existing plan rule |
| `planned` | `draft` | absent | absent |
| `active` | absent | n/a | governed by the existing plan rule |
| `active` | `draft` | absent | absent |
| `active` | `resolved` | present | optional |
| `completed` | absent | n/a | governed by the existing plan rule |
| `completed` | `resolved` | present | optional |
| `cancelled` | absent | n/a | governed by the existing plan rule |
| `cancelled` | `draft` | absent | absent |
| `cancelled` | `resolved` | present | optional |

A `planned` task cannot have a resolved RFC because resolving it requires substantive review and
therefore activates the task. When no RFC exists, this decision does not narrow the existing rules
for `plan.md`.

### Mechanical checks

Check only structure that represents an explicit lifecycle invariant:

- an existing `rfc.md` has the exact minimal frontmatter shape and a recognized status;
- a resolved RFC has one non-empty `## Resolution`, while a draft RFC has none;
- when both `rfc.md` and `plan.md` exist, the RFC is resolved;
- a completed task with an RFC archives it as resolved, while a cancelled task may archive either
  state.

Exercise every row in the state matrix with isolated positive cases rather than relying on the
repository's one final task state, including planned draft and completed resolved packages. Add
isolated negative cases for malformed frontmatter, unknown status, planned resolved, draft with a
Resolution or plan, resolved without exactly one non-empty Resolution, and completed with a draft
RFC.

Do not require particular discussion sections, alternatives, question counts, or review-note
formats. Their usefulness is semantic and cannot be established mechanically.

## Review notes

The initial discussion agreed on the separation: RFC for changeable discussion, plan for the
chosen execution approach. It also established that `plan.md` cannot become durable project
authority merely by being called final; accepted decisions still have to pass the deletion test.

The first repository-grounded review proposed three stable RFC states, an explicit Resolution
gate for a plan, `planned` as the pre-execution state, and checks limited to lifecycle structure.

Review replaced the Status heading with YAML frontmatter so lifecycle metadata is structured while
the RFC body stays free-form.

A fresh plan-verifier found that the proposal left stale Resolutions reusable after reopening,
contradicted the accepted meaning of `planned`, left `withdrawn` undefined, did not route durable
open questions, and assumed removed plans were committed. Resolution incorporated all five
findings: draft RFC work activates a task; withdrawal uses task cancellation; reopening removes the
old Resolution and plan only after folding; and structural checks cover the resulting state
combinations.
