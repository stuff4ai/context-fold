---
status: resolved
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

## Resolution

Do not create `.agents/context/`. `decisions/0044-defer-the-context-sublayer.md` keeps this the
first alternative: root `AGENTS.md` stays the only project-owned entry point, and task
`context.md` files stay the only agent-layer context selection. Neither changes.

The evidence available now does not clear decision 0005's bar — "should appear only once it
demonstrably exists." The recorded friction (`OPEN-QUESTIONS.md`'s "rules get stated where they
are relevant rather than where they are owned" pattern) is a citation- and ownership-discipline
defect: rules were placed near where they seemed relevant instead of where they were owned. A
navigational index would not have prevented that — the rules were already visible in the
project layer; nothing failed to find them. No task has yet failed, or paid a recorded cost, for
lack of a place that only points at authoritative sources.

Building the sublayer now, absent that evidence, would repeat the exact failure mode 0005 warned
against: a second documentation tree grown from anticipated need rather than demonstrated use.

This resolves `extend-init-project-assessment`'s blocker without building anything for it:
assessment references established project artifacts directly, the same way any task's
`context.md` already does. It does not need a dedicated sublayer to record where those sources
are.

The task-local open questions above (fixed filename, authored vs. derived, drift-checking,
initialization ownership) are about the shape of a sublayer this resolution does not build, so
none of them outlive this task. `decisions/0044-defer-the-context-sublayer.md` records sharper
reopening conditions in place of the open item this RFC answers.
