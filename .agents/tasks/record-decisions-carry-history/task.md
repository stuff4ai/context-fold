# Record that decisions carry history

## Status

active

## Objective

Record that source material is not stored raw, and locate the step in the loop where a
task-local problem becomes project-scoped.

## Why

The material this project was designed from was stored verbatim under `history/` and then
reverted. The reasoning that killed it — that a decision record's Context already carries the
alternative that lost, and `Status` supersession already records when an opinion changed — is
nowhere in the repository. It is a decision in substance and the kind of proposal that returns.

Separately, `0013` describes a chain from problem to candidate lesson without saying where the
promotion happens. It happens in the recurring-patterns section of `OPEN-QUESTIONS.md`, which
was created in the same change and never connected to the record describing it.

## Scope

- `decisions/0014-do-not-store-source-material.md`.
- `decisions/README.md` index row.
- `OPEN-QUESTIONS.md` — the recurring-patterns preamble.

## Out of scope

- Iterative stages. Separate task.
- Any change to `0013`, which is merged and immutable. This locates its chain rather than
  restating it.
- Building `.agents/learning/`, or promoting either recurring pattern into a rule.

## Acceptance

1. The record states the decision, and its Context carries the case *for* storing source
   material as well as against — the rejected approach was reasonable.
2. Consequences state the cost without softening: folding is lossy and irreversible, and no
   original remains to check a bad fold against.
3. `OPEN-QUESTIONS.md` says where a task-local problem becomes project-scoped, describing what
   the section already does rather than deciding something new.
4. No portable rule file changes.
5. Nothing added exists in more than one owned location.

## Problems

### A record was written arguing against its own decision

The reverted `history/` change included a record whose Consequences said an unstructured
document beside structured ones becomes a second source of truth and that this project had hit
that failure repeatedly — while deciding to create one.
Assumed: stating the objection inside the record is rigour, and shows the decision was made
with eyes open.
Actually: a record that argues convincingly against itself is not balanced, it is rationalizing.
The Consequences section is for costs accepted, not for the case that the decision is wrong. If
the objection is strong enough to write at that length, it has not been answered.
Usable as a check on any future record: if its Consequences read as an argument for the
alternative, the decision is not ready.

### The duplication check found nothing, for the first time in four tasks

Every previous task that added a decision record stranded a looser statement of it somewhere
else. This one did not.
Not a problem, recorded because the absence is the interesting part: the difference is that
`0014` decides something the repository had never stated loosely anywhere, having no prose about
source material to begin with. That is consistent with the pattern rather than a break from it —
formalizing strands a looser statement only when a looser statement exists.
