# Defer the verification sublayer

## Status

Accepted

## Context

[0041](0041-define-governed-agent-sublayers.md) left `verification/` a candidate only, alongside
`context/`, requiring evidence before either earns a physical contract. `OPEN-QUESTIONS.md`'s
"Verification, evidence, and observable execution" section asked whether verification needs its
own agent sublayer to describe portable agent evals, executable gates or evidence references,
while raw host execution stays external or disposable.

The `investigate-verification-sublayer` task's `rfc.md` compared three boundaries: keep
verification in project artifacts and task rules; add only an agent-facing summary and reference
map of project verification entry points; or define a full sublayer for portable agent-eval
contracts and evidence references.

Doing so required separating three things that "verification" loosely covers: product
verification (CI, tests — a property of the repository or its output), task acceptance
(`task.md`'s Acceptance criteria and the prose final check `0027` governs), and agent-system
evaluation (whether the agent itself selected relevant context, respected a decision, used
permitted tools, avoided unrelated files, recovered from failure, and stopped at the right
boundary — a property of the run's conduct, not its output).

[0044](0044-defer-the-context-sublayer.md) recently answered the sibling `context/` question by
the same method: recorded friction, not a plausible future need, is what clears the bar `0005` and
`0041` set for a new sublayer. No task package in this repository records an agent-system
evaluation that was needed and could not be performed, and no task has built its own ad hoc
evaluation harness inside the agent layer. Product verification and task acceptance are owned and
working; no task has recorded failing, or paying a cost, because they lacked a shared contract
with each other or with a hypothetical third owner.

## Decision

Do not create `.agents/verification/`, in either form the RFC compared — not the full contract
for portable agent-eval contracts and evidence references, and not the lighter agent-facing
summary-and-reference map either. Product verification stays where the project already keeps its
tests. Task acceptance stays owned by `task.md` and the final check `0027` governs. Agent-system
evaluation — the one concern with no existing owner — has no recorded instance of failing or
costing anything for want of one, so nothing is built for it now.

The map option fails the same test the full contract does: nothing has failed, or cost anything,
for want of a pointer to where verification already lives, and `.agents/tasks/AGENTS.md` already
states directly where task acceptance and the final check live. Adding a reference layer on top
of artifacts that are not hard to find would be anticipated-need infrastructure, the same
objection `0044` raised against the equivalent context-navigation aid.

This decision also states, independent of the structural question, what reproducibility can mean
for a nondeterministic agent: not reproducing the model's output, which can legitimately differ
across runs on the same request, but reconstructing and checking the request, the selected
context, the tool contract, and the sequence of observable actions taken under it. A future replay
mechanism would verify context integrity, authority-boundary enforcement, and stopping behavior
against that reconstructed frame — it is not a promise that the same run happens twice. This
record states that meaning; it does not build replay, telemetry, or a runtime harness, which stay
out of scope until a portable need is demonstrated.

This decision replaces the "Does verification need its own agent sublayer?" item in
`OPEN-QUESTIONS.md` with named reopening conditions, on the same model `0044` used for agent-only
context, so the question does not stay open indefinitely on the same footing. Reopen only if one
of these appears:

- An agent-system property — context selection, authority-boundary respect, permitted tool use,
  recovery, or stopping behavior — demonstrably fails, or is shown to have failed undetected, on
  a task specifically for want of an evaluation this sublayer would have supplied.
- Two or more tasks independently build their own ad hoc agent-evaluation harness inside the
  agent layer, showing convergent need rather than a hypothetical one.
- A portable, host-independent way to state an agent-eval contract or executable gate is
  demonstrated to exist without fixing a runtime, model, or tool schema — removing the reason
  this record gives for not building one yet.

## Consequences

`.agents/verification/` stays absent; nothing new ships, and no adoption, template, or check
changes.

Product verification, task acceptance, and the final check continue exactly as `0006`, `0014`,
and `0027` already define them. No new persisted evidence store is created, so this record needs
no authority, retention, or deletion rule of its own — the existing boundary against raw
execution history and source material (`0006`, `0014`) is unchanged.

The reproducibility statement is available the next time replay, an executable gate
representation, or an agent-eval contract is proposed, without having settled how any of those
would be built.

The "Does verification need its own agent sublayer?" question in `OPEN-QUESTIONS.md` is answered
for now with a sharper bar for revisiting it, rather than left open with no criterion for when it
stops being open.
