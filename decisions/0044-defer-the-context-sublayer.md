# Defer the context sublayer

## Status

Accepted

## Context

[0005](0005-agents-layer-boundary.md) deliberately left `.agents/context/` out of v0: reusable
agent-only context "should appear only once it demonstrably exists, so the layer does not become
a second documentation tree by default."
[0041](0041-define-governed-agent-sublayers.md) revisited the recognized-sublayer model and again
left `context/` a candidate only, requiring evidence before it earns a physical contract, and
routed that question to the `define-context-sublayer` task.

That task's `rfc.md` drafted a minimal proposal — a portable contract plus one disposable,
project-specific navigation artifact holding only summaries and references, never domain
knowledge — and asked whether the evidence bar is now cleared.

`extend-init-project-assessment` is blocked on this task deciding "where project-specific
summaries and references live," giving the question a concrete downstream consumer for the first
time.

`OPEN-QUESTIONS.md`'s "Recurring patterns" section records roughly eighteen instances across five
tasks of rules being stated where they seemed relevant rather than where they were owned. That is
the only concrete, repeated friction on record that touches project navigation.

## Decision

Do not create `.agents/context/`. Root `AGENTS.md` remains the only project-owned entry point,
and task `context.md` files remain the only agent-layer context selection; this decision changes
neither.

The recorded friction does not clear 0005's bar. The eighteen instances are about rules placed
near where they seemed relevant instead of where they were owned — a citation- and
ownership-discipline defect. The rules in question already lived in the project layer and were
visible there; nothing failed to find them for want of an index. No task has recorded failing, or
paying a cost, because it could not locate authoritative intent, decisions, documentation, or
verification sources. Building a navigation sublayer on that evidence would be exactly the
anticipated-need infrastructure 0005 warned against.

`extend-init-project-assessment`'s blocker is resolved without building anything: project
assessment references established project artifacts directly, the same way any task's
`context.md` already does. It does not require a dedicated sublayer to record where those sources
are, so its `## Blocked by` is removed rather than satisfied by new structure.

This decision replaces the open "Agent-only context" item in `OPEN-QUESTIONS.md` with named
reopening conditions, so the question does not stay open indefinitely on the same footing. Reopen
only if one of these appears:

- An agent demonstrably fails, or pays a recorded cost, on a task specifically for want of a
  navigation pointer this sublayer would have supplied.
- Two or more tasks independently build their own ad hoc project-navigation aid inside the agent
  layer, showing convergent need rather than a hypothetical one.
- A later task — assessment or otherwise — finds it cannot proceed without one, rather than being
  able to reference project artifacts directly as this decision assumes.

## Consequences

`.agents/context/` stays absent; nothing new ships, and no adoption, template, or check changes.

`extend-init-project-assessment` proceeds without a sublayer dependency; its assessment
recommendations reference project artifacts directly.

The "Agent-only context" question in `OPEN-QUESTIONS.md` is answered for now with a sharper bar
for revisiting it, rather than left as an open item with no criterion for when it stops being
open.
