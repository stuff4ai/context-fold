# Investigate a verification sublayer

## Status

planned

## Objective

Determine whether agent verification and evidence need a distinct sublayer or remain responsibilities
of project tests and task lifecycle rules.

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

## Blocked by

- `define-agent-sublayer-model` must define what a functional sublayer owns and when one is warranted.

## Acceptance

1. Investigation distinguishes product verification, task acceptance and agent-system evaluation.
2. A resolved RFC decides whether a physical verification sublayer earns its place.
3. Any selected persisted evidence has a defined authority, retention rule and deletion behavior
   without duplicating project tests or raw execution history.
4. The resolution states what reproducibility can mean for nondeterministic execution.
5. Any portable artifacts and checks required by the resolution are complete.

## Approval

Human.
