---
status: completed
objective: >-
  Decide how a repository that adopted context-fold before step 5 existed — or that wants its
  project-capability assessment redone — can get it without a full reset.
---

# Wire step 5 into repeat adoption

## Why

`decisions/0046-adopt-project-assessment.md`'s Consequences claims a repository that already
holds an `assess-project-{capability}` task "keeps it rather than getting a duplicate on every
re-adoption" — implying step 5 runs again on repeat adoption. `skills/ctxfold-init/ADOPTING.md`
does not implement that: its "If the layer is already there" section only preflights and updates
the five managed `AGENTS.md` targets, says "Leave task packages alone," and says "do not open
task zero." Step 5 is wired only into task zero's own flow, which by definition runs once. There
is currently no documented path for a repository that adopted before step 5 existed — or that
wants its assessment redone after a capability changed — to get it without deleting `.agents/`
and the root pointer and redoing task zero from scratch, which isn't safe once real work is built
on top of the layer.

This was found by testing adoption against a real external fixture
(`etu-forms/monorepo`) while `extend-init-project-assessment` (now merged as PR #53,
`decisions/0046-adopt-project-assessment.md`) was still open, and reported on that PR before
merge. Recorded here per `.agents/tasks/AGENTS.md`'s finding-triage rule, since that task is now
merged and no longer writable.

## Scope

- `skills/ctxfold-init/ADOPTING.md`'s "If the layer is already there" section.
- Whether repeat adoption should attempt a one-time catch-up assessment pass, and what gates it
  so it does not refire on a project that legitimately has zero gaps or already declined them.
- `decisions/0046-adopt-project-assessment.md`'s Consequences claim, corrected to match whatever
  this task resolves.

## Out of scope

- Reopening whether step 5 / project assessment should exist at all — `0046` already decided that.
- Any capability beyond the five `0046` already scoped.

## Acceptance

1. A resolved decision states whether repeat adoption performs a catch-up assessment pass, and if
   so, what gates it (for example: only when zero `assess-project-*` tasks exist anywhere in the
   repository, planned/active/archived).
2. `ADOPTING.md`'s repeat-run section and `decisions/0046-adopt-project-assessment.md`'s
   Consequences agree with each other and with the implemented behavior.
3. A repository that already ran step 5 and legitimately has no gaps does not get a spurious
   assessment pass on every subsequent repeat adoption.

## Problems

- Considered recording the catch-up pass by appending to task zero's own archived `task.md` or
  `context.md`, since that's where step 5's evidence already lives when it runs on schedule.
  `.agents/tasks/AGENTS.md` forbids editing an archived-and-accepted task's content as rewriting
  history. Resolved by giving the catch-up pass its own task package,
  `project-capability-catchup`, instead of touching task zero's — which also gives the
  three-signal detection gate a name to check for that doesn't depend on task zero's age or
  content.

## Outcome

Resolved: repeat adoption performs a one-time catch-up assessment, gated on three signals
(`assess-project-*` packages, a `project-capability-catchup` package, or task zero's own
"Project-capability assessment" section) so it never runs more than once per repository and never
duplicates a check that already happened, with or without gaps found.

`skills/ctxfold-init/ADOPTING.md`'s "If the layer is already there" section and `SKILL.md`'s
judgment-call guidance now describe the catch-up pass and its gate; both stay byte-identical
between `skills/ctxfold-init/` and the installed `.agents/skills/ctxfold-init/` copy.

`decisions/0049-wire-step-5-into-repeat-adoption.md` records the decision; `0046`'s Status now
points to it rather than the Consequences claim being left silently wrong.

Acceptance:

1. Satisfied — `0049` states the catch-up pass runs and names its three-signal gate.
2. Satisfied — `ADOPTING.md` and `0046`'s Status agree; `0046`'s own Context/Decision/Consequences
   prose is left untouched, per the immutability rule for accepted records.
3. Satisfied — any one of the three signals existing is sufficient to skip, so a repository that
   already checked and found nothing does not get rechecked.

Durable artifacts produced: `decisions/0049-wire-step-5-into-repeat-adoption.md` (indexed in
`decisions/README.md`), `0046`'s Status update, and the `ADOPTING.md`/`SKILL.md` changes
(installed and verified byte-identical under `.agents/skills/ctxfold-init/`).

## Approval

Human.
