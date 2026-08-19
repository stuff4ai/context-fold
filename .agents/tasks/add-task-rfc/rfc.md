# RFC — separate proposal discussion from execution planning

## Status

Draft

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
discussion clear. It is curated working context, not a stored transcript.

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

## Open questions

- What minimum state marker must distinguish a draft, resolved, reopened, or withdrawn RFC
  without turning a free-form discussion into a form?
- Is a written Resolution required before `plan.md` may be created, or is agreement captured in
  `task.md` sufficient?
- Must a task remain `planned` while its RFC has an unresolved direction, even if evidence-gathering
  work is already underway?
- Which structural properties, if any, should convention checks enforce for an optional RFC?

## Review notes

The initial discussion agreed on the separation: RFC for changeable discussion, plan for the
chosen execution approach. It also established that `plan.md` cannot become durable project
authority merely by being called final; accepted decisions still have to pass the deletion test.
