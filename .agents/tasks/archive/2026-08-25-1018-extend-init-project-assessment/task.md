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
  left resolving that to this task's RFC work). The first resolution here built no assessment
  mechanism at all, so the question was moot. Reopened below, v0 answers it the same way the
  Problems entry anticipated: established sources are recorded in ordinary task `context.md`
  prose, not a new context-map mechanism — `decisions/0044-defer-the-context-sublayer.md` still
  applies.
- The task was completed, archived in PR #53, and its RFC resolved against building anything —
  then reopened on PR review feedback citing a second real adoption
  (`etu-forms/monorepo`) that met reopening condition #2 in the decision record this task
  produced (then named `0045-defer-project-assessment.md`, since rewritten in place — see
  Outcome). Assumed: the prior Resolution's "no track record"
  reasoning would hold until this project itself hit a failure. Actual: a different, concrete
  reopening path applied first — a second adopter surfacing the same checklist-shaped gap
  (missing product-intent document) this project also has no dedicated document for, distinct
  from its `README.md`. `.agents/tasks/AGENTS.md`'s reopening procedure (fold, then re-draft,
  then record why) applied cleanly to a task already merged into PR review, not just to one still
  under first-pass discussion.

## Outcome

The RFC reopened on new evidence and resolved to build v0. `etu-forms/monorepo` — a second real,
external, non-trivial adoption — met reopening condition #2 in the decision record this task
maintains: its task-zero base-state discovery found a checklist-shaped gap (no product-intent
document anywhere in the repository, the same gap shape context-fold's own adoption also has)
before any assessment mechanism existed to prompt looking for it, and its adopter explicitly
asked for the capability this RFC proposes.

`ctxfold-init` gains a v0 project-assessment step, added to `skills/ctxfold-init/ADOPTING.md` as
step 5 (run at the end of task zero, before it is finished) and to `SKILL.md` (the judgment calls
it asks of the adopting agent). It classifies the five listed capabilities — intent and
requirements, decisions and rationale, documentation and knowledge, tests and verification, and
agent skills — using only what task zero's own base-state discovery already found, as established,
partial, absent, ambiguous, or not applicable. For each partial, absent, or ambiguous capability
it opens one `planned` `assess-project-{capability}` task carrying that evidence and a
non-binding recommendation, skipping any capability a task package of that slug already covers
anywhere in the repository (any status, including archived) so repeat adoption cannot reopen a
gap already decided. No new context-map mechanism was added: established sources are recorded in
task zero's own `context.md` prose, the same boundary
`decisions/0044-defer-the-context-sublayer.md` set.

`decisions/0045-defer-project-assessment.md` is rewritten in place as
`decisions/0046-adopt-project-assessment.md` (this branch was unmerged, so the record was still a
proposal, not history) recording the reversal and its evidence, re-indexed in
`decisions/README.md`. `OPEN-QUESTIONS.md`'s project-assessment item is narrowed to what v0 leaves
open: vendor-neutral skills assessment outside languages context-fold has been adopted into, and
what future evidence would justify further capabilities.

Acceptance:

1. Satisfied — the RFC is resolved and states the v0 catalog: intent, decisions, documentation,
   verification, skills.
2. Satisfied — `rfc.md`'s Current proposal and `ADOPTING.md`'s step 5 both state the five
   classification states and the evidence each one requires (task zero's own base-state
   discovery, not a new investigation).
3. Satisfied — `ADOPTING.md` has the adopting agent create each generated task `planned`,
   scoped to one capability, carrying repository evidence and a non-binding recommendation that
   offers rather than chooses.
4. Satisfied — the existing-package check before creating `assess-project-{capability}` prevents
   duplicate tasks across repeat adoption; cancellation and completion of a generated task follow
   `.agents/tasks/AGENTS.md`'s ordinary fold-then-archive rules, unchanged by this task.
5. Satisfied — `skills/ctxfold-init/ADOPTING.md` and `SKILL.md` carry the resolution; the
   installed copy under `.agents/skills/ctxfold-init/` is byte-identical to the shipped one.
   `templates/` needed no changes: generated tasks are ordinary task packages, not a new
   templated artifact.

Durable artifacts produced: `decisions/0046-adopt-project-assessment.md` (indexed in
`decisions/README.md`), the narrowed item in `OPEN-QUESTIONS.md`, and the assessment step in
`skills/ctxfold-init/ADOPTING.md` and `SKILL.md` (installed and verified byte-identical under
`.agents/skills/ctxfold-init/`).

## Approval

Human.
