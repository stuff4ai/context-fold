---
status: resolved
---

# RFC — formalize the skills sublayer

## Problem

`.agents/skills/` is useful to agents and is now a recognized interoperability sublayer. Its
minimal portable contract routes agents to independently owned packages but deliberately does not
settle authority, provenance, projection, format, or lifecycle semantics.

## Current proposal

Refine the recognized directory contract while preserving every installed skill package. Define
how reusable procedures relate to project truth, current task and user authority, installation
provenance, and host projections, without moving the package ownership boundary.

Keep workflows and MCP/tools outside the v0 contract. They remain future candidates until their
different semantics are demonstrated in use.

## Alternatives

- Leave the minimal contract without authority or provenance semantics.
- Let the contract claim ownership of every skill package.
- Expand the recognized skills sublayer to workflows and tools without evidence.

## Open questions

- Does a layer-level contract conflict with an installed skill's own `AGENTS.md` or `SKILL.md`?
- What prevents a skill from being mistaken for project authority or implementation permission?
- Should the contract require names, provenance, locks or checks, and who supplies them?
- How are unknown or host-incompatible skill packages represented without hiding them?

## Resolution

Refine the recognized contract in place; do not build new infrastructure. The evidence available
today is two installed packages (`ctxfold-init`, `ctxfold-tasks`), the Claude Code adapter
(`0034`), the shipped-skill portability check (`0040`), and the sublayer registry (`0041`). Read
together, they already answer most of the Current proposal's questions empirically; this
resolution states those answers in the contract instead of leaving them implicit, and is honest
about the one axis — provenance — where nothing in that evidence shows a need to build anything.

**Authority.** A package is a reusable procedure, never project truth and never a grant of
permission. Following one does not authorize work beyond the current user request, project
instructions, and task scope — the existing contract already said this. What it left unsaid is
the case that actually creates the conflict named in the RFC's first open question: a package
carries its own `AGENTS.md` or `SKILL.md` (`ctxfold-init` does, with its own "stop before
archiving" instruction). That file governs how to carry out its own package's procedure; it never
raises the layer's authority ceiling, overrides project instructions, or supersedes this contract.
There is no conflict once the two documents are read as answering different questions —
capability instructions versus a permission ceiling — and the contract now says so instead of
leaving a reader to work it out.

**Discovery.** No manifest, lock file, or required index. An agent finds packages by reading the
direct children of the directory and each package's own entry point. This project's own two
packages both expose a `SKILL.md` with `name` and `description` because that is what their host
loads; nothing here requires every future package to use that shape, because the sublayer
contract routes to hosts generically and a format requirement beyond what a package already needs
for its own host would be exactly the anticipated-need standardization this task is scoped to
avoid.

**Provenance.** Not required. Neither installed package records its source or an installed
version, and neither has failed, drifted unnoticed, or blocked a task for lack of one —
`ctxfold-init` is re-installed by re-copying its own distribution, which is how staleness is
already caught. This mirrors `0044`'s reasoning for the context sublayer: building a requirement
ahead of a demonstrated failure is the anticipated-need infrastructure this project defers.
Reopen if a package installed here is later found stale, mismatched, or ambiguous in origin with
no way to tell, or if a second, independently maintained package needs to declare compatibility
with a specific host or contract version.

**Host projection.** `0034`'s Claude Code symlink is the one example, and it already carries the
right shape: a non-owning pointer added at the adopting project's own discretion, never
distributed by context-fold, never a second authoritative copy. This resolution generalizes that
shape into the contract itself rather than leaving it a fact about one adapter decision: any host
projection over this directory follows it. It does not add a second, portable adapter mechanism —
`OPEN-QUESTIONS.md`'s broader question of how capabilities reach heterogeneous hosts stays open,
because one adapter is not evidence for a general mechanism.

**Package ownership and coexistence.** Unchanged from `0026`/`0041`: each package is owned by
whatever installed it, the contract preserves unknown or host-incompatible packages exactly as it
preserves known ones, and nothing here classifies or overwrites content it does not own. Stating
"preserve, do not hide" already answers the RFC's fourth open question; an unrecognized package
is not made to look native, and it is not concealed either.

Workflows and MCP/tools stay out of the v0 contract, as the Current proposal already said —
nothing in this evidence touches either.
