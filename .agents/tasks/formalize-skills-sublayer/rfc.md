---
status: draft
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
