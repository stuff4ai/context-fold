# Context — write-the-adoption-procedure

## Base state

`main` is at `a082fe7`. Seventeen decision records, ten archived tasks, a check suite and CI.

The portable layer is three rule files totalling 222 lines. `.agents/tasks/INDEX.md` is instance
data — it holds this repository's ten rows — so an adopter needs an empty one, which does not
exist anywhere.

## References

- `decisions/0005-agents-layer-boundary.md` — the root `AGENTS.md` is project-owned and
  context-fold adds only a pointer. This governs step three.
- `decisions/0011-keep-the-model-vendor-neutral.md` — why the procedure must stand alone rather
  than living inside a skill.
- `decisions/0012-build-the-methodology-before-the-tooling.md` — deferred tooling until the
  conventions had been used enough to show which matter, which is the precondition this meets.
- `decisions/0000-use-decision-records.md` — the bootstrap shape task zero copies: the first
  record is the decision to use records.

## Assumptions

- The three rule files are genuinely portable. The check suite enforces it, but only against this
  repository's vocabulary — a phrase that is project-specific in some other repository would pass.
- Copying is an adequate distribution mechanism for one experiment. It is not one for adoption in
  general, and the record says so.

## Context conflicts

`0012` says v0 has no tooling that produces artifacts, and `OPEN-QUESTIONS.md` lists it as
deferred. A written procedure produces nothing, so it is outside that — but the skill built on it
next is not, and that record will have to narrow `0012` the way `0016` did rather than claim an
exemption.

## Open questions

The dry run uses a scratch copy of an existing repository. Which repository is a choice about
evidence, not about the procedure: one with code, CI, an existing root `AGENTS.md`, and an
existing `.agents/skills/` tests the most assumptions at once.
