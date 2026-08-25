---
status: resolved
---

# RFC — extend initialization with project assessment

## Reopened

This RFC was resolved against building project assessment (its Resolution reasoned from
`decisions/0005-agents-layer-boundary.md` and `decisions/0044-defer-the-context-sublayer.md`
that context-fold had been adopted exactly once, on itself, and no adopter had failed a task or
paid a recorded cost for want of adoption flagging a missing capability) and archived as
`extend-init-project-assessment` in PR #53. It is reopened per `.agents/tasks/AGENTS.md`'s
reopening procedure — folding the still-relevant parts of that reasoning into the re-evaluation
below rather than repeating it unexamined — on new evidence raised as review feedback on that
still-open PR.

A concurrent, real adoption is underway at `etu-forms/monorepo` — an external, non-trivial
repository (Java/Spring backend, Vite/TypeScript frontend, monorepo, its own ADR convention split
across `docs/adr` and `backend/docs/adr`, GitLab CI, no prior agent layer). Task zero (bare layer
install) is already done there. Its base-state discovery found: decisions exist as ADRs, but no
product-intent or requirements document exists anywhere in the repository, and there was no root
`AGENTS.md` before adoption. The adopter explicitly asked that `ctxfold-init` produce planned
tasks assessing project-layer gaps as part of adoption.

This is `decisions/0045-defer-project-assessment.md`'s own reopening condition #2: "a second real
adoption surfaces a specific, recurring gap a generic checklist could plausibly have caught."
Context-fold's own adoption (the only one this RFC previously had evidence from) also has no
formal product-intent or requirements document distinct from `README.md` — the same shape of gap,
now observed at both known adoptions rather than asserted as a hypothetical. That reading of
"recurring" is the specific thing that changed: one occurrence was exactly the "no track record"
this RFC's prior Resolution described; two independent adoptions surfacing the same
checklist-shaped absence is what the reopening condition was written to require before treating
the gap as more than speculation.

The prior Resolution's own open design questions — what evidence makes a capability
"established," how repeat adoption avoids reopening a gap a project already declined, how many
generated tasks become ceremony — did not have a real adopter to design against then. They do
now, and are re-answered below rather than left to answer themselves once a mechanism exists,
which was the specific failure mode the prior Resolution declined to risk.

## Problem

Installing agent operating rules does not make project knowledge discoverable or complete. A new
agent may still lack an authoritative path to intent, decisions, documentation, tests or reusable
procedures. Automatically creating those artifacts would exceed adoption's authority and impose a
project layout without evidence.

## Current proposal

As the last part of task zero, after the layer is installed and its base state is recorded,
inspect five project capabilities: intent and requirements, decisions and rationale,
documentation and knowledge, tests and verification, and agent skills. For each, classify what
task zero's own base-state discovery already found:

- **Established** — an authoritative source exists and task zero's `context.md` already names
  it. No task.
- **Partial** — something exists but is incomplete, split across locations without a stated
  reason, or not clearly authoritative (for example, decisions recorded in more than one place
  with no note of which one governs, or which one prevails on conflict).
- **Absent** — nothing in the repository plays this role at all.
- **Ambiguous** — evidence conflicts or task zero's discovery could not tell which of the above
  applies.
- **Not applicable** — the project has no use for the capability (for example, no test suite
  because the repository holds no executable code).

Record established sources in `context.md`'s existing Base state prose — no new context-map
mechanism, per `decisions/0044-defer-the-context-sublayer.md`. For each applicable partial,
absent, or ambiguous capability, create one separate `planned` task package, slugged
`assess-project-{capability}` (e.g. `assess-project-intent`), carrying the repository evidence
task zero already gathered and non-binding recommendations. The user resolves each task by
choosing the project's structure, improving an existing convention, or deciding the capability is
not warranted; cancellation still folds durable findings out, postponement leaves the task
planned. Recommendations may offer paths and templates as examples but do not choose them.

This answers the prior open questions with the etu-forms/monorepo evidence in hand rather than
inventing an answer ahead of any adopter:

- **Evidence threshold ("established" vs. merely present).** Task zero's discovery already
  distinguishes these in prose for its own base-state purpose (it names authoritative sources, not
  just what exists); assessment reuses that same judgment rather than a separate evidentiary bar.
  Nothing in the etu-forms adoption asked for a stricter standard than that.
- **Non-duplication across repeat adoption.** Before creating `assess-project-{capability}`,
  check whether a task package of that slug already exists anywhere `ctxfold-tasks` discovery
  covers — `planned`, `active`, or archived, at any status including `cancelled`. If one exists,
  do not recreate it: a human already made or deferred that decision, and rediscovering the same
  gap on every adoption run is exactly the ceremony the prior Resolution warned about. Note the
  existing package's path in the current run's task zero instead.
- **Ceremony ceiling.** At most five tasks can ever be generated by one adoption run — one per
  capability — and only for capabilities classified partial, absent, or ambiguous. Established and
  not-applicable capabilities produce no task at all. The etu-forms discovery found two candidate
  gaps (intent, and ambiguous decision-location), not five, which is the expected shape: most
  repositories will not warrant a task for every capability.
- **Vendor neutrality for skills.** The skills capability asks only whether the repository has any
  documented, reusable agent procedure at all (a skill, a runbook, a checklist another agent could
  follow) — not whether it uses this project's own `skills/` convention or any particular tool's
  format.

## Alternatives

- Install only the agent layer and leave all project preparation outside context-fold.
- Produce a report but create no task packages.
- Create a standard project structure automatically during adoption.
- Ask about every capability before creating any task.
- Defer further and wait for a completed adoption (past task zero) to show whether the generated
  tasks are acted on, rather than building against a task-zero-only data point. Rejected: the
  mechanism only needs to run at task zero to be useful (it is a discovery step, not a step that
  depends on later adoption progress), and the two capability gaps found so far are already
  concrete and checklist-shaped rather than speculative.

## Open questions

- Can the assessment remain vendor-neutral while evaluating agent skills in languages or
  ecosystems context-fold has not yet been adopted into?
- Which future evidence would justify adding operations, security, data, release or integrations?

## Resolution

Build v0 of the current proposal: after task zero's base-state discovery, classify the five
listed capabilities against what that discovery already found, and open one `planned`
`assess-project-{capability}` task per applicable partial, absent, or ambiguous capability,
skipping any capability a task package anywhere already covers.

This reverses the prior Resolution on the strength of evidence that Resolution explicitly named
as the thing that would change its mind. It held that "context-fold has been adopted exactly
once, on itself, so there is no track record ... of an adopter missing an authoritative source ...
because adoption did not flag its absence," and it named reopening condition #2 in
`decisions/0045-defer-project-assessment.md` for exactly this case: "a second real adoption
surfaces a specific, recurring gap a generic checklist could plausibly have caught." That
condition is now met: `etu-forms/monorepo` is a second real, external, non-trivial adoption, its
task-zero discovery already surfaced two checklist-shaped gaps (no product-intent document
anywhere, and decisions split across two ADR directories with no stated precedence), and its
adopter explicitly asked for the capability this RFC proposes rather than the request being
invented on this project's behalf.

The prior Resolution is still right about what it declined to do: invent answers to the open
design questions before any adopter existed to check them against. What is different now is that
answers exist to check — the Current proposal's evidence-threshold, non-duplication, and ceremony
answers above are each drawn directly from what task zero's own discovery already produces or
from the two gaps this specific adoption surfaced, not from further speculation about a
hypothetical adopter. `decisions/0005-agents-layer-boundary.md` and
`decisions/0044-defer-the-context-sublayer.md`'s shared bar — a capability should appear once it
demonstrably exists — is satisfied by classification and task generation reusing task zero's
existing discovery rather than adding a new discovery mechanism (no context map, no new
evidence-gathering step): the only new thing this RFC adds is deciding, from evidence task zero
already collects, whether to open a task about it.

Scope stays v0-sized on purpose, matching `task.md`'s Out of scope: no auto-created PRDs, ADRs,
documentation, tests, or skills; no prescribed project layout; only the five listed capabilities,
not operations, security, data, release, integrations, workflows, or MCP/tools. The remaining
open question — vendor-neutral skills evaluation outside languages context-fold has been adopted
into — is recorded above rather than answered, because no adoption yet has tested it.

`OPEN-QUESTIONS.md`'s reopening-conditions item is replaced with a record of this decision.
`decisions/0045-defer-project-assessment.md` is rewritten in place (this branch is unmerged, so it
is still a proposal, not history) to record adopting the capability instead of deferring it.
