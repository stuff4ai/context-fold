# Keep the model vendor-neutral

## Status

Accepted

## Context

Every agent product carries its own repository conventions — its own directory, its own
instruction file, its own idea of what an agent should read first. Adopting one of them would
have given this project a working structure immediately. The conventions used by Claude,
Cursor, Codex, GitHub Copilot, and JetBrains tooling were surveyed before anything was
designed.

Two problems made that unattractive. A repository would inherit whichever product's model it
adopted, and that model changes when the product does. And a project using more than one agent
would need the same knowledge expressed several ways, which is the duplication this project
exists to prevent.

Building on an existing spec-driven tool had the same shape. OpenSpec was the specific
candidate and was rejected as a foundation: the goal was a model this project owns and can
change on its own evidence, not a variant of someone else's that inherits their assumptions
along with their structure. Rejecting it as a foundation is not a judgment of the tool, and
does not preclude learning from how it works.

The cost of neutrality is real. A neutral model integrates with nothing out of the box, and
every agent product that could have been supported for free must instead be supported
deliberately or not at all.

## Decision

The canonical model does not depend on any agent product.

The rules an agent follows are written for agents in general. They name no product, assume no
particular tool's directory layout, and require no runtime beyond a filesystem and Git.

Integration with specific products, if it happens, is an adapter over the canonical model. An
adapter may translate the model into what a product expects; it is never the source of truth,
and the model does not change to accommodate one.

This is what the portable rule files in `.agents/` implement. They are identical in every
project using context-fold and carry no project-specific paths, names, or decisions — a
property that only holds because the model underneath them is neutral.

## Consequences

The model survives products. A tool changing its conventions, or being abandoned, costs a
repository nothing.

A project using several agents keeps one copy of its knowledge rather than one per tool.

Nothing works out of the box. There is no integration with any product until someone writes an
adapter, and the neutral model may be more awkward to use with a given tool than that tool's
own convention would be.

The commitment is easy to violate by accident. A rule mentioning any product, or assuming its
layout, breaks it — and the failure is silent, because such a rule still reads correctly to
whoever is using that product.

The products named above are recorded as what was surveyed when this was decided. Their
conventions have almost certainly changed since; what they do now is not this record's claim.
