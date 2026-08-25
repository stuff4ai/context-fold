---
status: completed
objective: >-
  Determine whether agent verification and evidence need a distinct sublayer or remain responsibilities
  of project tests and task lifecycle rules.
---

# Investigate a verification sublayer

## Why

Project checks establish product properties, while agent-system evaluations could examine context
selection, authority boundaries, tool use, recovery and stopping behavior. Observable run facts,
executable gates and replay might need shared contracts, but no current artifact proves that a
separate directory earns its maintenance cost.

## Scope

- `OPEN-QUESTIONS.md` — the verification-sublayer question under verification, evidence and
  observable execution.
- The boundary among project tests, task acceptance, final checks, agent evaluations, run evidence
  and host-specific execution data.
- A sublayer contract or an explicit no-sublayer conclusion after RFC resolution.

## Out of scope

- Storing raw transcripts, hidden reasoning or host telemetry by default.
- Choosing one test framework, eval runtime or command schema for adopters.
- Implementing replay, telemetry or a runtime harness before the RFC establishes a portable need.

## Acceptance

1. Investigation distinguishes product verification, task acceptance and agent-system evaluation.
2. A resolved RFC decides whether a physical verification sublayer earns its place.
3. Any selected persisted evidence has a defined authority, retention rule and deletion behavior
   without duplicating project tests or raw execution history.
4. The resolution states what reproducibility can mean for nondeterministic execution.
5. Any portable artifacts and checks required by the resolution are complete.

## Approval

Human.

## Outcome

The investigation distinguished product verification (project tests and CI, owning a property of
the repository or its output), task acceptance (`task.md`'s Acceptance criteria plus the prose
final check `0027` governs), and agent-system evaluation (whether the agent's own conduct —
context selection, authority-boundary respect, tool use, recovery, stopping — was sound). The
first two are owned and working; the third has no recorded instance in this repository of failing,
or costing anything, for want of an owner.

The resolved `rfc.md` decided against building `.agents/verification/`, in either the full
agent-eval-contract form or the lighter agent-facing summary-and-reference map, on the same
recorded-friction test `decisions/0044-defer-the-context-sublayer.md` applied to the sibling
`context/` question. It also stated what reproducibility can mean for a nondeterministic agent:
not reproducing the model's output, but reconstructing and checking the request, selected
context, tool contract, and observable actions taken under it.

Durable outcomes folded into the project layer:

- `decisions/0045-defer-the-verification-sublayer.md` — new decision record, added to
  `decisions/README.md`'s index as Accepted.
- `OPEN-QUESTIONS.md` — the "Does verification need its own agent sublayer?" item under
  "Open questions about the model" was replaced with a resolved-with-reopening-conditions entry
  under "Deferred capability" › "Verification, evidence, and observable execution", naming the
  three conditions that would reopen it.

No persisted evidence store was selected, so no new authority, retention, or deletion rule was
needed; `0006` and `0014`'s existing boundary against execution history and raw source material is
unchanged. No portable artifact or check was required beyond the `OPEN-QUESTIONS.md` edit, since
the resolution builds no new structure.
