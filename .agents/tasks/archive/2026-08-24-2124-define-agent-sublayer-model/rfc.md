---
status: resolved
---

# RFC — define the agent sublayer model

## Problem

`.agents/AGENTS.md` maps tasks, skills and worktrees by owner, but the directory does not provide a
general model for adding more agent-operating concerns or routing an agent to detailed rules by
goal. Treating every directory as part of one layer would conflict with the accepted ownership
boundary and could make context-fold overwrite content installed by other tools.

## Current proposal

Treat `.agents/` as a governed namespace whose entry point routes agents to recognized sublayers.
Each sublayer has a managed `AGENTS.md` contract and may have installation-owned, project-owned,
tool-owned or disposable contents defined by that contract. Context-fold owns the portable
contract and navigation, not necessarily every byte below the directory.

Keep two source-of-truth ownership layers: project truth and agent operating state. Sublayers are
functional divisions inside agent operation, not new authorities. Cross-cutting concerns such as
identity, distribution, health and learning need not become directories.

## Alternatives

- Keep the current map of unrelated owners and add no general sublayer concept.
- Let context-fold own all of `.agents/`, requiring other tools to use another namespace.
- Define only a logical responsibility map without introducing physical sublayer contracts.

## Open questions

The detailed semantics of the skills contract, and whether the candidate context and verification
areas earn physical directories, remain owned by their downstream tasks.

## Resolution

Adopt governed agent sublayers inside the shared `.agents/` namespace without claiming ownership
of the namespace or of every file below it. A recognized sublayer is a direct `.agents/<name>/`
functional area with one context-fold-managed `AGENTS.md` contract. The contract must state its
required fields: purpose and routing; authority and source-of-truth boundary; contract ownership;
content ownership; lifecycle and deletion behavior; customization-suffix boundary; and treatment
of unknown extensions.
The managed block is portable; an adopting project may append a non-conflicting suffix, and the
update procedure preserves it byte-for-byte.

The initial classifications are:

- `tasks/` is the recognized core lifecycle sublayer. Context-fold owns its contract and task
  package lifecycle; `tasks/archive/` is internal archive structure, not another sublayer.
- `skills/` is the recognized interoperability sublayer. Context-fold owns only its managed
  contract; each installed skill package remains owned by its author, installer, or project.
- `worktrees/` is the recognized disposable-operation sublayer. Its contract is portable, while
  the adopting project's workflow owns the disposable checkouts; deleting them loses no project
  knowledge.
- `context/` and `verification/` remain candidates only. This task creates neither directory.
- Any other direct child is an unrecognized extension. It is preserved and is not classified or
  overwritten by context-fold; its own instructions apply when addressed by that extension.

`.agents/AGENTS.md` is a goal-oriented router: it identifies recognized sublayers, names their
ownership boundaries, points to their nearest contracts, and tells an agent to preserve unknown
extensions. It does not become a catalog of project truth or a claim over the whole directory.
The project/agent deletion test remains unchanged in substance: durable human-needed knowledge
stays in project-owned artifacts; removing layer-owned contracts and task state must not remove
that knowledge, and independently owned packages, suffixes, unknown extensions, and disposable
checkouts are treated according to their owners.

This resolution narrows the classification and distribution language in decisions 0005, 0017,
0018, 0021, 0025, 0026, 0032, 0034, 0035, and 0040 while preserving their project-truth,
ownership, deletion, vendor-neutrality, distribution, portability, and suffix-preservation
conclusions. Decision 0041 records the durable model.
