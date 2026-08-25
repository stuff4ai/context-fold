# Formalize the skills sublayer

## Status

Accepted

## Context

[0041](0041-define-governed-agent-sublayers.md) recognized `skills/` as an interoperability
sublayer with a portable contract, but left authority, provenance, discovery, host-projection,
and package-ownership semantics as a candidate for a later, dedicated decision — routed to the
`formalize-skills-sublayer` task.

That task's `rfc.md` drafted a proposal to refine the contract along those axes without moving
the package-ownership boundary, and asked four concrete questions: whether a layer-level contract
conflicts with an installed package's own `AGENTS.md` or `SKILL.md`; what prevents a package from
being mistaken for project authority or implementation permission; whether the contract should
require names, provenance, locks, or checks; and how unknown or host-incompatible packages are
represented without hiding them.

The evidence available to answer those questions already exists. Two packages are installed under
`.agents/skills/`: `ctxfold-init`, which carries its own `AGENTS.md`-equivalent instructions
(`SKILL.md`) including a "stop before archiving" step, and `ctxfold-tasks`, an agent-only script
with no human-facing interface. [0034](0034-extend-the-claude-code-adapter-to-skills.md) records
one host projection — a Claude Code symlink — as a non-owning, per-repository pointer, never
distributed by context-fold.
[0040](0040-guard-shipped-skill-portability.md) enforces that every shipped package stays free of
this repository's own project detail, and its companion `skills/AGENTS.md` documents that
boundary for an author. Neither installed package records where it came from or which version is
installed, and neither has failed, drifted unnoticed, or blocked a task for lack of it.

Nothing in that evidence shows an agent has been unable to tell a package's instructions from
project authority, has needed a manifest or naming scheme beyond what a package's own host
already requires, or has needed to know a package's provenance to use it correctly.

## Decision

Refine the existing `.agents/skills/AGENTS.md` contract in place. No new directory, manifest,
lock file, or distributed adapter mechanism is created.

**Authority.** A package is a reusable procedure, never project truth and never a grant of
permission. Finding one does not authorize work beyond the current user request, project
instructions, and task scope — restated from the existing contract. Added: a package's own
`AGENTS.md` or `SKILL.md` governs how to carry out that package's procedure; it never raises this
ceiling, overrides project instructions, or supersedes the sublayer contract. The two answer
different questions — capability instructions versus a permission ceiling — so a package carrying
its own instructions is not a conflict once the contract says which one binds.

**Discovery.** No manifest, lock file, or common entry-point format is required. An agent finds
packages by reading the direct children of the directory and each package's own entry point.
Both installed packages expose a `SKILL.md` because that is what their host loads; the contract
does not extend that shape to every future package, because a package answers to whatever host
loads it and a shape requirement beyond that would standardize a format the evidence has not
demonstrated a need for — exactly what the sublayer's own registry entry warned against.

**Provenance.** Not required. Neither installed package records its source or version, and
neither has failed or gone stale unnoticed for lack of it; `ctxfold-init` is refreshed by
re-copying its own distribution, which already catches drift. Building a requirement ahead of a
demonstrated failure is the anticipated-need infrastructure this project defers, the same
reasoning [0044](0044-defer-the-context-sublayer.md) applied to the context sublayer. Reopen if a
package installed here is later found stale, mismatched, or of ambiguous origin with no way to
tell, or if a second, independently maintained package needs to declare compatibility with a
specific host or contract version.

**Host projection.** Generalizes `0034`'s shape into the contract: any host-specific path or
format for reaching a package that already lives here is a non-owning pointer, added at the
adopting project's own discretion, never distributed by context-fold, and never a second
authoritative location. This does not add a second, portable adapter mechanism; one worked example
is not evidence for a general one, and `OPEN-QUESTIONS.md`'s broader question of how capabilities
reach heterogeneous hosts stays open.

**Ownership and coexistence.** Unchanged from `0026` and `0041`: each package is owned by
whatever installed it. Added explicitly: preserve every package, project suffix, and unknown or
host-incompatible direct child alongside the contract — do not classify, hide, or overwrite what
the contract does not own.

Workflows and MCP/tool sublayers remain out of scope, as `0041` already stated; nothing here
extends to them.

`OPEN-QUESTIONS.md`'s "How should the recognized skills sublayer be formalized?" item is removed
as answered. Its "Further skills and workflows" and "Versioning, provenance, discovery, and
upgrades" items are narrowed to note what this decision does and does not settle, including named
conditions for reopening skill provenance specifically.

## Consequences

`.agents/skills/AGENTS.md` states an authority ceiling that already held in practice, closing the
gap the RFC's first open question named: a package with its own instructions no longer reads as
an ambiguous second authority.

No package format, manifest, provenance field, or distributed host adapter is added. An installed
package that wants to record its own provenance may still do so; nothing here requires or forbids
it.

The recognized `skills/` sublayer's detailed semantics are now settled for authority, discovery,
host projection, and ownership. Provenance is deliberately left unbuilt, with a sharper bar for
revisiting it than "left to the skills task" gave before this record.

Workflows, MCP/tools, and the broader heterogeneous-host delivery question remain open, exactly as
they were.
