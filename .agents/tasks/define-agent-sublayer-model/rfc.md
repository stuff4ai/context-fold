---
status: draft
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

- What minimum fields or rules make a directory a recognized sublayer?
- Are tasks and worktrees both sublayers even though one stores context and the other stores
  disposable checkouts?
- How does the entry point expose project-specific extensions without making them portable rules?
- What validation proves the router and sublayer contracts agree?
