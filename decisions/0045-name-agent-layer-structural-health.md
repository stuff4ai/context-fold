# Name agent-layer structural health

## Status

Accepted

## Context

[0041](0041-define-governed-agent-sublayers.md) established recognized sublayer contracts but
left health, diagnosis, and recovery for each one to the `define-agent-layer-health` task. That
task's `rfc.md` drafted a proposal: define structural health around the contracts context-fold
actually owns, keep semantic health a separate review judgment, and find an explicit way for an
intentional fork to leave managed identity.

`OPEN-QUESTIONS.md` already recorded the concrete ask this task was scoped to answer: "Should an
adopter's installation be checkable?" — noting that this repository verifies its own installed
managed blocks against its distribution while an adopter's installation gets no such check, and
naming health states, diagnosis without overwriting owned content, and intentional-fork exit as
undecided.

Evidence gathered against that question shows most of it already answered elsewhere.
[0035](0035-manage-portable-rules-as-replaceable-blocks.md) defines exactly four ways a managed
target can be found — missing, legacy (no marker), well-formed single block, or ambiguously
marked — and requires the last to stop repair before writing anything. `ADOPTING.md`'s
repeat-adoption preflight already implements this for every portable target, and
`tests/test_conventions.py`'s `managed_rule_parts` implements and enforces the same classification
for this project's own installation.
[0026](0026-map-what-is-under-the-agents-directory.md) and 0041 already say what happens to
content none of that owns: preserve it, do not classify it, defer to its own owner.

What evidence does not show is a case for building anything past that. No installation has been
recorded losing a deliberate fork to a repeat-adoption run. No adopter has asked for a checker.
Distinguishing a managed block whose content has drifted from the current upstream template from
one that was always different requires knowing the canonical current bytes — which needs
provenance or a version identity, a question `OPEN-QUESTIONS.md` already defers for the same
reason: no installation has shown it needs one yet.

## Decision

Adopt four names for the structural states a recognized-sublayer contract target can be in —
**absent**, **legacy**, **managed**, and **malformed** — matching exactly what 0035 already
decided and `ADOPTING.md`'s preflight and `tests/test_conventions.py` already implement for the
portable `AGENTS.md` files. This generalizes the vocabulary from those four files to any target a
recognized sublayer contract governs, so a future contract (`context/`, `verification/`, or
whatever else clears its own evidence bar) can reuse a named health model instead of inventing
one. It does not change what the preflight does.

"Malformed" is the only state repair refuses: an ambiguous marker shape, where guessing risks
silent data loss. "Managed" is healthy regardless of what its content says — a well-formed block
whose prose is stale is not damaged, because telling stale content apart from merely different
content needs the canonical current bytes, which needs provenance this project has not built and
has no evidence it needs yet. Content staleness is a semantic question and stays a review
judgment, unchanged from 0035 and 0041's standing position.

Content the four states do not govern — an unrecognized direct child of `.agents/`, or an
extension inside a recognized sublayer that its own contract does not own — is a separate axis,
not a fifth severity: never classified, never repaired, never treated as disposable, per 0026 and
0041.

An intentional fork is not a distinguishable fifth state. Removing the markers to fork the rules
produces the same shape as a file that was never adopted with markers at all — both read as
legacy, and a future repeat-adoption run replaces legacy wholesale. No opt-out signal is added on
this record: no installation has been observed losing a fork this way, and inventing one now
would be exactly the anticipated-need infrastructure this project defers elsewhere. The hazard is
named instead, with its own reopening bar: build an opt-out signal if a real fork is destroyed by
a repeat-adoption run, or if an adopter asks for a supported way to leave managed identity before
that happens.

No portable checker is added for adopters generally. A generic adopter holds only the copy of the
templates they installed, not the current upstream ones, so a drift check for them is blocked on
the same provenance question named above — not on anything this record could build instead. This
project's own CI check remains what 0018 already described: a dogfooding-specific comparison
against the distribution this repository also ships, not a portable mechanism.

`OPEN-QUESTIONS.md`'s "Should an adopter's installation be checkable?" item is replaced with named
reopening conditions, matching the pattern
[0044](0044-defer-the-context-sublayer.md) used for the context sublayer question.

## Consequences

The next recognized sublayer contract can name its targets' health in four words instead of
rederiving the classification 0035 already made. Nothing about `ADOPTING.md`, the repeat-adoption
procedure, or `tests/test_conventions.py` changes: they already implement this.

An adopter's installation remains unchecked. The instruction not to edit a managed block, and the
risk that a deliberate fork is silently overwritten by a later repeat-adoption run, both remain
requests rather than enforced guarantees, unchanged from before this record, until a recorded
loss or request meets the named bar.

Content drift — a well-formed managed block whose prose no longer matches the current upstream
template — stays undetectable without provenance or a version identity, which remains an open
question in `OPEN-QUESTIONS.md`. Whether prose anywhere in `.agents/` is factually stale or
contradicts project reality remains a review judgment this record does not attempt to automate.
