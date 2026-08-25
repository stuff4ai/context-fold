---
status: resolved
---

# RFC — define agent-layer health and recovery

## Problem

The current repeat-adoption procedure can restore managed blocks while preserving suffixes, but a
larger governed namespace introduces more failure states. A required contract may be missing, an
unknown tool may add a directory, a user may intentionally fork rules, or project truth may be
misfiled into agent-only context. Treating all divergence as damage would make adoption destructive.

## Current proposal

Define structural health around contracts context-fold actually owns. Missing or drifted managed
contracts are recoverable after preflight; malformed markers stop repair; independently owned
contents are preserved; unknown extensions are reported with unknown ownership rather than removed.
Intentional forks need an explicit way to leave managed identity.

Keep semantic health separate. Checks may establish paths, markers, references and declared owners,
but whether a summary duplicated project truth or a rule contradicts reality remains a review
judgment unless an authoritative comparison exists.

## Alternatives

- Rely only on repeat adoption and add no broader health model.
- Require every installation to run context-fold checks in CI.
- Claim exclusive ownership of `.agents/` so unexpected content is always invalid.

## Open questions

- Which health evidence belongs in the repository and which can be produced on demand?
- Should repair be automatic after a clean preflight or separately authorized?
- How is an intentional fork represented without introducing mandatory provenance/versioning?
- When should a structural finding create a project task rather than be repaired immediately?

## Resolution

Four structural states apply to any target governed by a recognized-sublayer contract
(`decisions/0041-define-governed-agent-sublayers.md`): a missing managed file
is **absent**; a file with no `<!-- agent-layer:` marker line is **legacy**; a file with exactly
one well-formed begin/end marker pair, whatever prose sits inside it, is **managed** — this is the
healthy state; anything else — a displaced, reversed, duplicated, unmatched, or otherwise
malformed marker — is **malformed**, and repair must stop on the whole update rather than guess.
This is not new: `decisions/0035-manage-portable-rules-as-replaceable-blocks.md`
and `skills/ctxfold-init/ADOPTING.md`'s repeat-adoption preflight already classify every portable
target this way, and `tests/test_conventions.py`'s `managed_rule_parts` already implements it and
enforces it in this repository's own CI. The evidence for each state is exactly what that
preflight already produces: the target path and which of the four conditions it matched — nothing
new needs to be built to name a target's evidence.

**Damaged, not stale.** "Damaged" names only the malformed state — a marker shape that repair must
refuse to touch. A managed block that is structurally well-formed but no longer matches the
current upstream template's content is not damaged; it is a separate question — content drift —
that this resolution deliberately does not try to detect. Telling drifted content apart from
merely different content requires knowing the canonical current bytes, which requires the
installation to carry provenance or a version identity. `OPEN-QUESTIONS.md` already defers that
("Versioning, provenance, discovery, and upgrades") for lack of evidence that any installation
needs it yet, and building drift detection here would be exactly the anticipated-need
infrastructure this project defers elsewhere. So: a managed block is healthy regardless of its
content: whether that content is stale or wrong is the semantic judgment named below, not a
structural one.

**Unrecognized content is a separate axis, not a fifth severity.** A direct child of `.agents/`
that is not one of the recognized sublayers, or an extension inside a recognized sublayer that its
own contract does not own (an installed skill package, a project-added worktree file), is
*unrecognized* — never classified as any of the four states above, never repaired, never treated
as disposable. `decisions/0026-map-what-is-under-the-agents-directory.md` and
`decisions/0041-define-governed-agent-sublayers.md` already establish this:
preserve it and defer to its own owner's instructions. This resolution adds nothing to that; it
only names it alongside the four structural states so the two are not confused with each other.

**Intentional fork collapses into legacy.** Nothing today distinguishes "a user deliberately
removed the markers to fork the rules" from "this file was never adopted with markers in the
first place" — both read as legacy, and a future repeat-adoption run replaces legacy wholesale.
`ADOPTING.md` already warns that editing a managed block risks losing the edit; the same is true,
by the same mechanism, of a deliberate fork that stays inside a managed file. Recognizing an
intentional fork would need a new opt-out signal, which is new portable surface with no recorded
case of anyone needing one — no installation has been observed losing a fork this way. Rather than
build that signal speculatively, this resolution names the hazard and sets the bar for building
one: reopen if a real fork is destroyed by a repeat-adoption run, or if an adopter asks for a
supported way to leave managed identity before that happens.

**Semantic correctness stays a review judgment.** Whether prose inside a managed or unrecognized
file is factually stale, contradicts project reality, or duplicates project truth is not decided
by any of the states above and is not automatable without an authoritative source to compare
against — consistent with the RFC's original proposal and with 0035's and 0041's standing
position that semantic ownership mistakes remain review judgments.

**Nothing new is built.** Every state and boundary above is already true of this project's
installation and already implemented by `ADOPTING.md`'s preflight and
`tests/test_conventions.py`. This resolution formalizes the vocabulary and generalizes it from
"the four portable `AGENTS.md` files" to any recognized-sublayer contract target, so the next
sublayer contract (`context/`, `verification/`, or whatever else clears its own evidence bar) has
a named health model to reuse instead of rediscovering one. It does not add a portable checker for
adopters: a generic adopter has no local copy of the current upstream template to preflight
against, only the one they installed, so an adopter-facing check is blocked on the same
provenance/versioning question this resolution declines to build. That remains open in
`OPEN-QUESTIONS.md` with the same evidence bar named above.
