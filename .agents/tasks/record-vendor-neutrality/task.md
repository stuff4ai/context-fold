# Record vendor neutrality

## Status

active

## Objective

Record that the model does not depend on any agent product, and preserve the alternatives that
were considered and rejected before that was chosen.

## Why

Vendor neutrality is the reason the portable rule files exist and must stay free of
project-specific detail. It has shaped several decisions already — `0005` mentions it in
passing, and the layer boundary depends on it — but it has never been decided.

An unstated commitment cannot be violated knowingly. A contributor adding a rule that assumes
one agent product would be following every written rule in the repository.

The alternatives that lost exist nowhere: the survey of conventions from specific agent
products, and the decision not to build on OpenSpec's model. A decision record's Context is
where that belongs.

## Scope

- `decisions/0011-keep-the-model-vendor-neutral.md`.
- `decisions/README.md` index row.
- `OPEN-QUESTIONS.md` — how agent capabilities are distributed across heterogeneous hosts.

## Out of scope

- Methodology before tooling, and the learning loop. Separate tasks.
- Adapters. They stay deferred; this records why they are deferred rather than absent.
- Naming any specific agent product as supported or unsupported.

## Acceptance

1. The record states the commitment, and its Context carries both rejected alternatives — the
   vendor-convention survey and OpenSpec as a foundation.
2. The record explains why the portable rule files follow from it, without restating what
   `0005` already decided.
3. `OPEN-QUESTIONS.md` gains the distribution question, worded as a question rather than a
   plan.
4. No portable rule file changes. If one needs to, the material was misplaced.
5. Nothing added exists in more than one owned location.

## Problems

### The record was first written without naming the alternatives

The Context said "the conventions of several were surveyed" and "building on an existing tool's
model was rejected", naming neither.
Assumed: a Context section explains the forces, and the specific products are incidental.
Actually: the entire reason this task exists is that the rejected alternatives are recorded
nowhere. A Context that describes them abstractly preserves the shape of the reasoning and
loses the content — a reader a year from now learns that something was surveyed, not what.
Rewritten to name Claude, Cursor, Codex, GitHub Copilot, JetBrains tooling, and OpenSpec, with
a consequence stating those are what was surveyed at the time rather than a claim about what
they do now.
The draft would have passed a reading for quality. It failed only against the acceptance
criterion, which demanded both alternatives by name.
