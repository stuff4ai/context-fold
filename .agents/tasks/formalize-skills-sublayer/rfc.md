---
status: draft
---

# RFC — formalize the skills sublayer

## Problem

`.agents/skills/` is useful to agents but currently answers only to whatever put each skill there.
An entry-point router cannot describe skills as a sublayer unless it can say which rules are
portable, which contents are independently owned, and what reading or invoking a skill means.

## Current proposal

Give the directory a managed `AGENTS.md` contract while preserving every installed skill package.
The contract describes skills as reusable procedures rather than project truth, requires agents to
respect the current task and user authority, and states that a skill's own instructions apply when
the skill is selected. Context-fold owns the layer contract; installers or projects own packages.

Keep workflows and MCP/tools outside the v0 contract. They remain future candidates until their
different semantics are demonstrated in use.

## Alternatives

- Keep `.agents/skills/` outside the governed model and let each host or installer define it.
- Let context-fold own and distribute every skill under the directory.
- Treat skills, workflows and tools as one capability sublayer immediately.

## Open questions

- Does a layer-level contract conflict with an installed skill's own `AGENTS.md` or `SKILL.md`?
- What prevents a skill from being mistaken for project authority or implementation permission?
- Should the contract require names, provenance, locks or checks, and who supplies them?
- How are unknown or host-incompatible skill packages represented without hiding them?
