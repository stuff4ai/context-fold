---
status: completed
objective: >-
  Record decision 0041 as accepted after its approved pull request merged with a proposed status.
---

# Accept the governed agent-sublayers decision

## Why

Pull request 47 was approved and merged, but decision 0041 and its decision-index row still say
`Proposed`. Accepted decisions in this repository land as `Accepted`; leaving the merged record
proposed makes the durable decision state disagree with its acceptance.

## Scope

- The `## Status` value in `decisions/0041-define-governed-agent-sublayers.md`.
- The 0041 status cell in `decisions/README.md`.
- This correction task and its archival.

## Out of scope

- Changing decision 0041's accepted content.
- Reopening or rewriting the accepted `define-agent-sublayer-model` task.
- Any other decision, agent-layer contract, or implementation behavior.

## Acceptance

1. Decision 0041 and its index row both say `Accepted`.
2. No content of decision 0041 changes outside its mutable Status field.
3. Convention tests, Markdown lint, and `git diff --check` pass.

## Problems

- The approval-to-merge sequence omitted the normal `Proposed` to `Accepted` status transition.
  The omission was found only after pull request 47 had merged and its worktree and branches were
  removed, so the correction requires a new GitHub Flow change rather than editing accepted task
  history or pushing directly to `main`.

## Outcome

Decision 0041's mutable Status field and its decision-index row now both say `Accepted`, matching
the approved and merged state of pull request 47. No accepted decision content changed. The final
state passes all 648 convention tests, the configured recursive Markdown scan, and
`git diff --check`.

## Approval

Human.
