---
status: draft
---

# RFC — define the context sublayer

## Problem

Agents need a compact way to discover which project artifacts carry intent, decisions,
documentation and verification. Root `AGENTS.md` should remain a small project-owned entry point,
and task `context.md` files should remain task-specific. Repeating project facts in a global agent
directory would create another source of truth.

## Current proposal

If the parent model admits sublayers, add a context contract plus one project-specific navigation
artifact. The contract permits only short navigational summaries and references to authoritative
project-layer sources. The map is disposable: deleting it loses convenience rather than project
knowledge. Task packages continue to select the subset needed for one task.

A possible physical shape is `.agents/context/AGENTS.md` for portable rules and
`.agents/context/INDEX.md` for installation-specific navigation. The names and update lifecycle
remain proposals, not settled structure.

## Alternatives

- Keep project navigation in root `AGENTS.md` and add no context sublayer.
- Keep all selection in task `context.md` files and rely on repository search for discovery.
- Allow curated reusable agent-only knowledge in the context sublayer.

## Open questions

- What distinguishes a navigational summary from a duplicated project fact?
- Must every summary carry a source reference, provenance and update trigger?
- Does initialization write the first map, or do separate project-preparation tasks build it?
- What evidence would justify later retrieval, compilation or generated projections?
