---
status: resolved
---

# RFC — investigate a verification sublayer

## Problem

Current verification is split between project tests, task acceptance and a prose final check. The
open questions propose scenarios, agent-system evals, observable run facts, executable gates and
replay, but those concerns do not automatically share one owner or storage lifecycle.

## Current proposal

Compare three boundaries before selecting structure:

- keep verification in project artifacts and task rules;
- add only an agent-facing summary and reference map of project verification entry points; or
- define a verification sublayer for portable agent-eval contracts and evidence references while
  leaving raw host execution data external or disposable.

A physical sublayer is selected only if investigation identifies information or behavior not
already owned by project tests, task packages or host adapters.

## Alternatives

- Make every task carry an executable verification manifest.
- Treat host telemetry and transcripts as the verification record.
- Put all product and agent checks into one repository-wide gate catalog.

## Open questions

- What is the smallest observable evidence that makes an agent run auditable?
- Which evidence must survive acceptance, and where can it live without becoming project truth?
- How are manual checks, commands and eval thresholds represented across hosts?
- Which semantic diagnostics have an authority strong enough to avoid opinionated warnings?

## Resolution

Three things get called "verification" here and they are not the same thing:

- **Product verification** shows a property of the repository or its output — CI, project tests,
  linters. It already has an owner: the project's own test suite and tooling, outside the agent
  layer entirely.
- **Task acceptance** shows that one task did what it said it would. It already has two owners:
  `task.md`'s Acceptance criteria, and the prose final exact-head check `0027` governs, which
  produces evidence for a reviewer rather than a verdict for itself.
- **Agent-system evaluation** — did the agent select relevant context, respect a decision, use
  permitted tools, avoid unrelated files, recover from failure, stop at the right boundary — is
  a genuinely different concern from the other two. It asks about the agent's conduct during the
  run, not about the state the run produced.

The first two are owned and working; no task has recorded failing, or paying a cost, because
product verification and task acceptance lacked a shared contract. The third has no owner today,
but also has no evidence: no task package in this repository records an agent-system evaluation
that was needed and could not be performed, and no task has built its own ad hoc harness for one
inside the agent layer. `0044` reached the same kind of conclusion for agent-only context by the
same test, and the test applies here without modification — recorded friction, not a plausible
future need, is what clears the bar `0005` and `0041` set for a new sublayer.

**No verification sublayer is built — not the full contract, and not the lighter agent-facing
summary-and-reference map either.** The map option fails for the same reason `0044` rejected the
equivalent context-navigation aid: nothing has failed, or cost anything, for want of a pointer to
where verification already lives. Project tests are found where the project keeps them; task
acceptance and the final check are already written directly into `.agents/tasks/AGENTS.md`.
Adding a reference layer on top of two things that are not hard to find would be anticipated-need
infrastructure, not a response to a demonstrated gap.

This resolution does not select any new persisted evidence. The final check already governs what
evidence a task must produce (`0027`), and that evidence lives in the reviewed diff and the PR it
travels with — not in a new store this sublayer would have had to define authority, retention
and deletion for. `0006` and `0014` already forbid execution history and raw source material
from becoming a second truth inside a task package; nothing here narrows or extends that.

**What reproducibility can mean for a nondeterministic agent:** it cannot mean reproducing the
model's output, because the same request can legitimately produce different tool calls, wording
or paths across runs. What can be reconstructed and checked instead is everything *around* the
model's choice — the request as given, the context selected for it, the tool contract it
operated under, and the sequence of observable actions it took. Replay, if this project ever
builds it, verifies context integrity, authority-boundary enforcement and stopping behavior
against that reconstructed frame; it is not a promise that the same run happens twice. This
investigation states that meaning; it does not build the replay mechanism that would exercise it,
which stays out of scope until a portable need is demonstrated.

The "Does verification need its own agent sublayer?" item in `OPEN-QUESTIONS.md` is answered with
named reopening conditions, on the same model `0044` used for agent-only context, rather than left
open indefinitely on the same footing.
