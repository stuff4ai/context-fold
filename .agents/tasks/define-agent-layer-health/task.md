---
status: planned
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
