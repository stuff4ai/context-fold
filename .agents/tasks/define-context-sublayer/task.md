---
status: planned
objective: >-
  Decide whether agent-facing project navigation should have a context sublayer containing only
  summaries and references to authoritative project artifacts.
---

# Define the context sublayer

## Why

Task `context.md` files select context for one task, while durable project knowledge stays in the
project layer. A reusable project map could help agents discover intent, decisions, documentation
and verification without copying that knowledge, but it could also become the second documentation
tree the current model deliberately avoids.

## Scope

- `OPEN-QUESTIONS.md` — the agent-only-context and canonical-context-manifest questions.
- The proposed context contract, project-specific navigation artifact, deletion test, provenance
  and relationship to task `context.md` files.
- Portable rules, templates, adoption guidance and checks only after the RFC resolves.

## Out of scope

- Choosing where adopters store project documentation, requirements, decisions or tests.
- Automatic retrieval, context compilation, snapshots or host-specific loading policy unless the
  RFC establishes them as necessary for the minimal boundary.
- Authoring project knowledge inside `.agents/context/`.

## Acceptance

1. A resolved RFC decides whether the context sublayer exists and distinguishes it from project
   knowledge and per-task context selection.
2. If selected, every persisted summary identifies authoritative sources and deletion loses no
   durable project knowledge.
3. The resolution defines the owner and update lifecycle of the project-specific context map.
4. Any portable files, adoption changes and checks required by the resolution are complete.

## Approval

Human.
