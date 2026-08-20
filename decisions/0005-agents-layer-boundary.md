# Separate the agent operating layer from project knowledge

## Status

Accepted. The identification of the layer with the `.agents/` directory is narrowed by
[0018](0018-ship-a-distribution.md). [0035](0035-manage-portable-rules-as-replaceable-blocks.md)
narrows whole-file ownership to the managed rule block; the boundary itself stands.

## Context

Repositories adopting agent tooling accumulate agent-specific directories that gradually fill
with project knowledge — architecture notes, domain vocabulary, requirements. That knowledge
then exists in two places at once, drifts, and nobody can tell which copy is true.

The failure is not the directory. It is the absence of a rule for what may live there.

An agent-oriented layer also needs a stable entry point, and repositories increasingly carry
a root `AGENTS.md` that the project itself owns. Adding a second convention on top of it
risks the same duplication at the entry point.

## Decision

`.agents/` is the agent operating layer, not the project knowledge layer.

Accepted durable project knowledge must never exist only inside `.agents/`. It belongs in the
project's own artifacts — the code, its tests, its documentation, and its decision records.

This layer does not prescribe where those live. Projects differ, and context-fold adapts to
an existing layout rather than imposing one; the rule constrains what may live in `.agents/`,
not how the rest of the repository is arranged.

The boundary is enforced by the deletion test:

> If humans need this information too, it does not belong only in `.agents/`.

The test is applied by removing `.agents/` and reading what remains. It fails when knowledge
is lost — when something a human needs to understand or maintain the project is gone. It does
not fail on references to the layer: removing `.agents/` is an ordinary change, and the files
that pointed at it are updated in the same change.

Scoping the failure condition to knowledge keeps the test mechanical while preventing it from
being read as a prohibition on the project layer ever mentioning the agent layer — a reading
that would forbid the entry point from doing its job.

Inside `.agents/`: agent navigation, task coordination, agent operating rules, task lifecycle
state, temporary working context.

Outside `.agents/`: architecture, domain knowledge, requirements, decisions, API
documentation, product vocabulary.

Ownership of the two entry points differs. Root `AGENTS.md` is owned by the project and holds
global project instructions; context-fold adds only a pointer to `.agents/AGENTS.md` and does
not colonize it. `.agents/AGENTS.md` is owned by this layer, holds stable operating rules,
and never holds project state or current task information.

`.agents/context/` is deliberately not created in v0. Reusable agent-only context should
appear only once it demonstrably exists, so the layer does not become a second documentation
tree by default.

## Consequences

The repository stays usable by humans and by agent tooling that knows nothing about
context-fold.

Removing the layer is safe, which keeps adoption reversible and makes the convention cheap to
try.

Every artifact needs a placement judgment. The deletion test makes that judgment fast, but it
must be applied — including at review time, where duplication is easiest to catch.

Some information genuinely serves both audiences and will be written in the project layer and
referenced from the agent layer, rather than duplicated.
