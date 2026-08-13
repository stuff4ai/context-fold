# Adoption procedure

## Status

Accepted

## Context

context-fold has only been applied to the repository that defines it. The next evidence worth
having comes from elsewhere, and nothing described how it gets there.

Copying three files and improvising the rest would have worked, and would have measured the
improvisation. A written procedure makes installation repeatable and, more usefully, makes its
gaps visible: a step that is vague, wrong, or silent is a finding rather than something the
installer quietly compensates for.

Where the procedure lives matters. [0011](0011-keep-the-model-vendor-neutral.md) permits
integrations with particular agent products only as adapters over the canonical model. Adoption
instructions that existed only inside one product's skill format would leave every other project
with nothing, so the procedure has to stand alone and any tooling has to follow it rather than
replace it.

How adoption starts was open. One proposal was that initialization opens a task whose work is
discovering the project's context. That assumed `.agents/context/`, which v0 deliberately omits —
discovered knowledge would have nowhere to go inside the layer, and the deletion test would push
it into the project layer the adopting repository already has.

## Decision

Adoption is four steps, described in `ADOPTING.md` in the project layer: copy the three portable
rule files unchanged, create an empty task index, add a pointer to the repository's root
`AGENTS.md`, and open task zero.

Provenance is not tracked. An installation records nothing about which context-fold it took. That
question only has a consumer once there is a way to upgrade, and upgrading is deferred — so
answering it now would mean maintaining a hand-written fact that nothing reads and nothing
verifies.

The root `AGENTS.md` is added to when it exists and created when it does not. Either way
context-fold contributes only the pointer, per [0005](0005-agents-layer-boundary.md).

Task zero is the adoption itself — `adopt-context-fold`, whose subject is the layer that
contains it. This is the shape [0000](0000-use-decision-records.md) uses: the first record is the
decision to keep records. Discovery-as-task-zero is rejected for the reason above.

The procedure is canonical. Tooling that automates it is an adapter and follows it.

## Consequences

A repository can adopt context-fold without anyone reconstructing how, and following the written
steps is a test of them.

There is no upgrade path. Copying is the entire distribution mechanism: an installation cannot
learn that its rule files are stale, nothing announces when they change, and a project that
adopted early has no way to discover it is behind. Provenance and upgrading are one question, and
v0 answers neither rather than half-answering both.

There is no customization. An adopter who wants different rules is told to record that as a
problem rather than edit, which keeps the layer replaceable at the cost of asking people to live
with rules that may not fit.

An installation cannot say which context-fold it is running. Git can answer it — the commit that
last touched the rule files, if its message says where they came from — but that is a convention
nothing states and nothing enforces.

The procedure describes copying files that this project cannot guarantee are correct elsewhere.
The first dry run found two defects in them — a claim to own a shared directory, and a deletion
test that destroys other tools' data — neither of which was visible from inside the repository
that wrote them.
