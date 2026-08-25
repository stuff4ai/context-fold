---
status: completed
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

## Problems

- Scope named "context-map updates" among the mechanisms to build, wording left ambiguous by
  `define-context-sublayer`'s own Problems log (it noted the phrase presumed either the
  context sublayer that task might have built, or ordinary task `context.md` maintenance, and
  left resolving that to this task's RFC work). The resolution here builds no assessment
  mechanism at all, so the question is moot: there is no context map, of either kind, for
  adoption to update.

## Outcome

The RFC resolved against building project assessment. `ctxfold-init` gains no capability
catalog, evidence classification, or generated-task mechanism: context-fold has been adopted
exactly once, on itself, and no adopter has failed a task or paid a recorded cost for want of
adoption flagging a missing project capability. Building the classification scheme and
task-generation mechanism now, before evidence exists to answer the RFC's own open design
questions, would be the anticipated-need infrastructure `decisions/0005-agents-layer-boundary.md`
and `decisions/0044-defer-the-context-sublayer.md` both decline to build.

`decisions/0045-defer-project-assessment.md` records the decision and names three concrete
reopening conditions, replacing the open "Should adoption assess project-layer readiness?" item
in `OPEN-QUESTIONS.md` with those conditions.

Acceptance item 1 is satisfied: the RFC is resolved and states the v0 catalog is not built.
Items 2–4 are satisfied vacuously, the same way `define-context-sublayer` recorded it: nothing
was selected to classify, generate, or update, so there is no duplicate-task or buried-outcome
risk to guard against. Item 5 is satisfied: the resolution requires no `ctxfold-init` procedure,
skill, template, or check change.

Durable artifacts produced: `decisions/0045-defer-project-assessment.md` (indexed in
`decisions/README.md`), and the replacement item in `OPEN-QUESTIONS.md`'s "Deferred capability"
section under "Product boundary, behavior at scale, and measurement."

## Approval

Human.
