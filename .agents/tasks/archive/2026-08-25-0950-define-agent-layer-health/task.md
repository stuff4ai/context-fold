---
status: completed
objective: >-
  Decide how an installation detects and recovers structural damage to governed agent sublayers
  without overwriting project- or tool-owned contents.
---

# Define agent-layer health and recovery

## Why

Managed blocks can repair portable instructions, but a governed set of sublayers would also need to
distinguish missing contracts, malformed markers, drift, unknown extensions and intentional forks.
The model should promise detectable, recoverable structure rather than pretending repository users
cannot diverge.

## Scope

- `OPEN-QUESTIONS.md` — the adopter-installation-check question under distribution, adoption,
  skills and host integration.
- Health states, diagnostics, repair boundaries, unknown extensions and intentional divergence.
- `ctxfold-init`, a separate procedure, checks or metadata only after RFC resolution.

## Out of scope

- Proving semantic correctness of project documentation or agent instructions.
- Deleting unknown directories or replacing installed skill contents.
- Version discovery and upgrades except where required to distinguish structural drift.

## Acceptance

1. A resolved RFC defines which structural states are healthy, damaged, unknown or intentionally
   forked.
2. Diagnostics identify exact targets and evidence without treating unknown contents as disposable.
3. Recovery preserves project suffixes and all independently owned sublayer contents.
4. The resolution states which semantic boundary violations remain review judgments.
5. Any procedure, metadata and checks required by the resolution are complete.

## Approval

Human.

## Outcome

The RFC resolved by formalizing the classification `0035`
(`decisions/0035-manage-portable-rules-as-replaceable-blocks.md`) and `ADOPTING.md`'s
repeat-adoption preflight already made — absent, legacy, managed, malformed — as the general
structural health model for any recognized-sublayer contract target, rather than building new
diagnostics, checks, or a fork opt-out signal. Evidence against `decisions/0018`, `0026`, `0035`,
and `0041`, plus `skills/ctxfold-init/ADOPTING.md` and `tests/test_conventions.py`, showed the
model this task asked for is already implemented for the portable `AGENTS.md` files; what was
missing was a name generalized past those four files, and an explicit statement of what "damaged"
does and does not cover. Content drift and an adopter-facing portable checker both stay blocked on
the provenance/versioning question `OPEN-QUESTIONS.md` already deferred; an intentional-fork
opt-out signal is named as a hazard with its own reopening bar rather than built without a
recorded case needing it. No change was made to `ctxfold-init`, `ADOPTING.md`, or
`tests/test_conventions.py`, matching the resolution's finding that nothing new was required.

Durable artifacts:

- `decisions/0045-name-agent-layer-structural-health.md`, added to `decisions/README.md`'s index.
- `OPEN-QUESTIONS.md`'s "Should an adopter's installation be checkable?" item, replaced with the
  resolution's named reopening conditions.
- This task's resolved `rfc.md`, archived alongside it.
