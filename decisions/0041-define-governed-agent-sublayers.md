# Define governed agent sublayers

## Status

Accepted

## Context

The shared `.agents/` namespace contains task state, reusable procedures, and disposable
checkouts, but the previous map described them only as unrelated areas with different owners.
That made routing by goal ambiguous and left no reusable contract for deciding whether a future
agent-operating area was recognized or merely an extension. At the same time, claiming the whole
directory would overwrite project- or tool-owned contents and would fail the project-truth
deletion test.

## Decision

Governance attaches to explicit contracts, not to the `.agents/` directory as a whole. A direct
`.agents/<name>/` functional area becomes a recognized sublayer only through a reviewed decision
that classifies it and a portable, context-fold-managed `AGENTS.md` contract shipped by the
distribution. Mere presence under `.agents/` does not make an area recognized or layer-owned.

Every recognized contract covers the same fields: purpose and routing; authority and
source-of-truth boundary; contract ownership; content ownership; lifecycle and deletion behavior;
customization-suffix boundary; and treatment of unknown extensions. Those fields separate the
portable contract from the contents it governs, so context-fold can own a contract without
claiming the packages, checkouts, or project additions beside it.

The initial registry is:

| Sublayer | Role | Contract owner | Content owner and lifecycle |
| --- | --- | --- | --- |
| `tasks/` | Core lifecycle | context-fold | context-fold owns task packages; `tasks/archive/` is internal structure |
| `skills/` | Interoperability | context-fold | each author, installer, or project owns its packages |
| `worktrees/` | Disposable operation | context-fold | the adopting project owns disposable checkouts and workflow |

`context/` and `verification/` remain candidates and are not created by this decision. Any other
direct child is an unrecognized extension: preserve it, do not classify or overwrite it, and
follow its own instructions when they address the goal. Managed contracts may carry a
project-owned suffix, which updates preserve byte-for-byte.

`.agents/AGENTS.md` is the goal-oriented router. It names recognized sublayers, points to their
nearest contracts, states their ownership boundaries, and routes unknown extensions to their own
owners. Durable human-needed knowledge remains in project-owned artifacts. Removing the
layer-owned managed contracts and task packages must not remove that knowledge; independently
owned packages, suffixes, unknown extensions, and disposable checkouts remain governed by their
owners and deletion behavior.

This record narrows the classification and distribution language in
[0005](0005-agents-layer-boundary.md), [0017](0017-adoption-procedure.md),
[0018](0018-ship-a-distribution.md),
[0021](0021-separate-what-upgrades-from-what-diverges.md),
[0025](0025-run-tasks-in-parallel.md), [0026](0026-map-what-is-under-the-agents-directory.md),
[0032](0032-fold-worktrees-agents-md-into-the-byte-identical-set.md),
[0034](0034-extend-the-claude-code-adapter-to-skills.md),
[0035](0035-manage-portable-rules-as-replaceable-blocks.md), and
[0040](0040-guard-shipped-skill-portability.md). Their project-truth boundary,
ownership of package contents, deletion conclusions, vendor neutrality, distribution identity,
and suffix-preserving update rules remain in force.

## Consequences

Agents have one entry point for routing by goal and a stable contract shape for recognized areas.
Context-fold can update contracts without replacing independently owned skill packages or
worktree contents, and unknown tools can coexist under `.agents/` without being silently adopted.

The recognized set is intentionally small. Context and verification still need evidence before a
physical directory and contract are added, and the skills task must define authority, provenance,
host projections, format, and lifecycle semantics. Semantic ownership mistakes remain review
judgments rather than automatic deletion or migration.
