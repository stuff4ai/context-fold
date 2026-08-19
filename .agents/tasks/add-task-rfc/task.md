# Add an RFC artifact to task packages

## Status

planned

## Objective

Add an optional `rfc.md` for mutable proposal discussion, and distinguish it from an agreed
`plan.md` that guides execution after the direction is settled.

## Why

The current task model gives `plan.md` two jobs. It is the place where an execution strategy is
written, and it is explicitly mutable while work proceeds. There is no task artifact for an
earlier conversation whose proposal, alternatives, review feedback, and open questions are still
changing.

Putting that discussion into `plan.md` makes it unclear whether a direction has been selected.
Treating the plan as an immutable decision would create a different problem: durable decisions
belong in project artifacts, while implementation details still need to adapt to what execution
reveals. A separate RFC can hold the unsettled proposal without becoming a raw transcript or a
second source of project truth.

## Scope

- The task-package model and a decision record defining optional `rfc.md` and the revised role of
  `plan.md`.
- `README.md` — the task-artifact summary.
- The portable task rules, their shipped template, and this repository's installed copies.
- Convention checks only where a decided structural invariant can be checked mechanically.
- `OPEN-QUESTIONS.md` — only questions directly resolved or narrowed by this decision.
- `.agents/tasks/INDEX.md` — this task's derived row and eventual archival update.

## Out of scope

- Reorganizing all entries in `OPEN-QUESTIONS.md` by topic.
- Storing raw chat transcripts, hidden reasoning, or uncurated source material.
- Making an RFC mandatory for every task.
- Moving durable project decisions out of `decisions/` or other project-owned documentation.
- Changing task creation, archival, index maintenance, or other lifecycle automation.

## Acceptance

1. A decision record defines the responsibilities and lifecycle of `task.md`, `context.md`,
   optional `rfc.md`, optional `plan.md`, and durable project decisions without assigning the
   same authority to two artifacts.
2. `rfc.md` is the mutable place for a curated proposal, alternatives, open questions, and review
   feedback while direction is unsettled; it is explicitly not a raw transcript or durable
   project authority.
3. `plan.md` represents the selected execution strategy. Its direction is settled before work
   starts, while tactical details may still change without altering the task contract.
4. The portable rules say when either optional artifact earns its place, how an RFC is resolved
   or reopened, and where its durable outcome must be folded before acceptance.
5. This task uses `rfc.md` while planned and does not create `plan.md` until its RFC is resolved.
6. Shipped and installed portable rules remain byte-identical, relevant documentation and live
   questions agree with the decision, and pytest, recursive Markdown lint, and
   `git diff --check` pass.
