---
status: completed
objective: >-
  Preserve proposed agent-native SDLC and harness directions as live, neutral questions without
  treating the proposal as an accepted architecture or implementation plan.
---

# Park agent-native SDLC questions

## Why

The proposal connects product intent, decisions, context selection, traceability, verification,
runtime provenance, replay and telemetry. Some of its description assumes artifacts that this
repository does not currently have, and its suggested structures may conflict with the layer's
ownership and vendor-neutrality boundaries. The durable part is therefore the set of questions
the proposal raises, after checking them against current project truth.

## Scope

- `OPEN-QUESTIONS.md` — `## Deferred capability` and `## Open questions about the model` only.
- Reconcile each added question with current documentation and accepted decisions.

## Out of scope

- Accepting the proposed layer model or directory structure.
- Adding product documents, decision records, manifests, trace graphs, scenarios, evals, runtime
  contracts, episodes, checks or telemetry.
- Resolving any parked question.
- Existing entries outside the two named sections.

## Acceptance

1. Each durable direction in the supplied proposal is either represented by a neutral live
   question or omitted because an existing entry already covers it.
2. Added context describes this repository as it exists rather than repeating mistaken
   assumptions from the proposal.
3. No wording presents a proposed artifact, layer boundary or implementation order as decided.
4. The task stays active while further material is expected, then is completed and archived
   before review.

## Outcome

`OPEN-QUESTIONS.md` now preserves the supplied agent-native SDLC, integration-layer and product-
positioning directions as neutral questions grounded in the current model. Existing questions
were extended where they already owned context selection, compilation, schemas and heterogeneous
hosts; distinct questions were added for intent, local decisions, traceability, scenarios, evals,
runtime provenance, replay, executable gates, telemetry, manifests, projections, snapshots,
lessons, fold proposals, system models, active history and the product's knowledge-ownership
boundary. No proposed artifact, command, layer model or implementation order was adopted.

## Problems

- The first worktree command tried to start its shell inside the checkout before Git had created
  it. Running `git worktree add` from the repository root created the checkout normally; no
  repository state changed during the failed attempt.
- An initial documentation search named `ADOPTING.md` at the repository root, following an older
  layout assumption. The current canonical file is `skills/ctxfold-init/ADOPTING.md`; the failed
  lookup reinforced that source claims had to be checked before folding them.
- The repository's configured `pytest` and `pymarkdown` commands were initially not installed in
  this environment. A temporary environment installed `requirements-dev.txt`; all 230 tests and
  the recursive Markdown scan then passed.
- Independent Plan review found that static/dynamic loading had been preserved but portable
  semantic context classification had not. The existing context-selection question now asks
  about purpose separately from loading policy without adopting the proposed taxonomy; re-review
  returned `READY`.
- Review of the second batch found that the fold-proposal wording assigned folding to a person
  even though the rules do not, and that a new adapter-ownership question duplicated the existing
  heterogeneous-host question. The fold step is now stated impersonally, and adapter ownership
  and external integration are consolidated into the existing question; re-review returned
  `READY`.
- Review of the product-positioning batch found that generated system maps had been treated as
  authored project knowledge solely because they were generated. The question now leaves them as
  disposable projections unless authority, persistence and independent maintenance make them
  project knowledge; re-review returned `READY`.
- The first custom final-check assertion searched for the literal text `^## Outcome` instead of
  anchoring a regular expression, so it failed despite the heading being present. Correcting the
  assertion made the check test the intended condition.
- Fresh verification was initially inconclusive because its isolated context did not contain the
  source conversations needed to test semantic coverage. Given a binding checklist of the source
  directions, the same verifier confirmed coverage, lifecycle state and checks with no P0-P2
  findings.
