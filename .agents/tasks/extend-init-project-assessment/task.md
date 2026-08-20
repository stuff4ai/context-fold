---
status: planned
objective: >-
  Decide whether adoption should assess project-layer capabilities and create separate planned tasks
  for evidence-backed gaps while leaving each project's final structure to its users.
---

# Extend initialization with project assessment

## Why

Context-fold can prescribe the agent layer it installs but cannot assume that project intent,
decisions, documentation, verification or reusable agent procedures are authoritative and
discoverable. Recommendations could help an adopter prepare those sources without silently
migrating the project or prescribing one filesystem layout.

## Scope

- `OPEN-QUESTIONS.md` — the project-readiness assessment question under product boundary,
  behavior at scale and measurement.
- A v0 assessment catalog for intent, decisions, documentation, verification and skills.
- Evidence classification, generated planned tasks, cancellation/folding behavior, context-map
  updates and repeat-adoption behavior.
- `ctxfold-init` procedure, skill, templates and checks only after RFC resolution.

## Out of scope

- Automatically creating PRDs, ADRs, documentation, tests or skills.
- Prescribing one project directory layout or one template as mandatory.
- Assessing operations, security, data, release, integrations, workflows or MCP/tools in v0.

## Blocked by

- `define-agent-sublayer-model` must establish the governed namespace and project/agent boundary.
- `define-context-sublayer` must decide where project-specific summaries and references live.

## Acceptance

1. A resolved RFC decides whether initialization performs project assessment and defines the v0
   capability catalog.
2. Assessment states and evidence requirements distinguish established, partial, absent,
   ambiguous and not-applicable capabilities.
3. Any generated task is self-contained, `planned`, applicable to observed evidence, and leaves
   final project structure to human choice.
4. Completion, cancellation, repeat adoption and context-map updates cannot bury durable outcomes
   or create duplicate recommendation tasks.
5. Any adoption, skill and check changes required by the resolution are complete.

## Approval

Human.
