---
status: completed
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

## Problems

- Decision 0042 (merged concurrently, unrelated to this task) requires a new decision record to
  begin `Proposed` and move to `Accepted` only while folding outcomes, immediately before
  archival. This task folds its outcome in the same pass that drafts the record, so
  `0044-defer-the-context-sublayer.md` was written directly as `Accepted` rather than through a
  visible `Proposed` intermediate state.
- PR #50 merged to `main` first and had already claimed decision number `0043` for an unrelated
  record. Rebasing found the collision; this task's record was renumbered to `0044` before
  merge, per the ordinary renumbering rule for records still on a branch.
- `extend-init-project-assessment`'s Scope names "context-map updates" without saying whether
  that presumed the (now not built) sublayer or ordinary task `context.md` maintenance. Resolving
  that ambiguity is that task's own RFC work, not this one's, so the wording was left unedited
  once its `## Blocked by` was removed.

## Outcome

The RFC resolved against building the sublayer. The recorded friction (`OPEN-QUESTIONS.md`'s
"rules stated where relevant rather than owned" pattern) is a citation- and ownership-discipline
defect, not evidence that an agent has failed to locate authoritative sources, so it does not
clear decision 0005's "should appear only once it demonstrably exists" bar.
`decisions/0044-defer-the-context-sublayer.md` records the decision and names three concrete
reopening conditions, replacing the open-ended "Agent-only context" item in `OPEN-QUESTIONS.md`.

`extend-init-project-assessment`'s `## Blocked by` is removed: assessment references established
project artifacts directly, without needing a dedicated sublayer to record where they are.

No portable files, templates, adoption guidance or checks were added, matching the resolution.
Acceptance items 2–4 are satisfied vacuously: nothing was selected to persist, own, or check.

## Approval

Human.
