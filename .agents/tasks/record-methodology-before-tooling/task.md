# Record methodology before tooling

## Status

active

## Objective

Record that v0 is conventions in plain files rather than software, and preserve the reasoning
and the rejected alternative that produced it.

## Why

`OPEN-QUESTIONS.md` lists a CLI as deferred capability, which reads as something not yet
reached. It was a choice: the project deliberately moved away from building a product, on the
grounds that tooling over an unproven methodology hides the methodology's weaknesses.

Two commitments follow from it and are also unrecorded. The project dogfoods itself before
being offered to anyone — every rule here was produced by using it. And it must be able to
adopt itself, which is why the first task built the layer while using the layer rather than
building it and testing afterwards.

Skills were the intended vehicle for tooling when tooling arrives. That intent is written down
nowhere, so a future contributor deciding how to distribute this would be starting from
nothing.

## Scope

- `decisions/0012-build-the-methodology-before-the-tooling.md`.
- `decisions/README.md` index row.
- `OPEN-QUESTIONS.md` — skill naming, distribution direction, `init` behavior, and the
  workflow-versus-skill distinction.

## Out of scope

- The learning loop. Separate task.
- Deciding when tooling should be built, or what it should do. The record states the ordering,
  not a trigger.
- Naming any repository other than this one as a validation target.

## Acceptance

1. The record states the ordering as a choice, with the CLI product path preserved as the
   alternative that lost.
2. Dogfooding and self-adoption are recorded as constraints, with the evidence that they have
   been followed.
3. The record says plainly that all evidence so far comes from this repository alone.
4. `OPEN-QUESTIONS.md` gains four items, each worded as a question rather than a plan, and the
   existing CLI entry no longer implies the absence is merely unreached.
5. No portable rule file changes.

## Problems

### Recording a decision made its rationale duplicate an existing summary

`README.md` said there is no CLI *and* that the goal is to find out by using the conventions
which parts earn their keep. The second half is the reasoning, which `0012` now owns.
Assumed: writing a new record is additive and leaves existing documents alone.
Actually: a record almost always formalizes something already stated loosely somewhere, so
writing one creates duplication unless the looser statement is trimmed in the same change.
Trimmed to the fact plus a pointer.
Seventh instance of this pattern, and the first found by a check rather than by review. The
duplication check in the plan was written for exactly this and would have been easy to treat
as ceremony.
