<!-- agent-layer:begin -->

<!--
Managed rule block. Updates replace everything between the agent-layer markers.
Do not edit this block. Add only non-conflicting project instructions after the end marker.
-->

# AGENTS.md — the agent layer

The agent layer holds how agents work on this repository, not what this repository knows.

These rules are stable. This file must never contain project state or current task
information.

## What the layer is

It is installed rather than authored here, and consists of the managed blocks in these
`AGENTS.md` files and what working here produces — task packages and their archive. A managed
block may describe a recognized sublayer whose contents have another owner; the contract is part
of the layer, not every file below it.

`.agents/` is where it lives, not what it is. Other tools write there too, and their files are
not part of the layer and not its concern. Nothing here claims the directory.

The managed rule blocks are identical in every installation. They carry no project-specific
paths, names, or decisions. An adopting project may append instructions after the end marker,
but those additions do not become portable rules and must not contradict this block.

If a rule here does not fit this project, record it as a problem in the task rather than
overriding it locally. The portable rule can then change through the distribution's reviewed
workflow instead of becoming a different rule in each installation.

## Project truth lives outside the layer

Accepted, durable project knowledge belongs in the project's own artifacts — the code, its
tests, its documentation, and its decision records — wherever this project already keeps
them.

The deletion test:

> If humans need this information too, it does not belong only in the layer.

Remove the layer — its managed rule blocks and its tasks — and read what remains.
The test fails if knowledge was lost, if something a human needs to understand or maintain the
project is now gone. Project-owned suffixes remain. Anything lost that way was in the wrong layer.

It does not fail on references to the layer. Removing it is an ordinary change, and whatever
pointed at it is updated in the same change.

Recognized sublayer contracts belong to the layer; their packages, checkouts, and other contents
belong to the owner named by that contract. Unknown direct children under `.agents/` belong to
whatever put them there. Preserve all of them; none is part of the deletion test unless its own
owner says otherwise.

Belongs outside the layer: architecture, domain knowledge, requirements, decisions, API
documentation, product vocabulary.

Belongs inside it: agent navigation, recognized-sublayer contracts, task coordination, agent
operating rules, task lifecycle state, temporary working context.

Knowledge left sitting only inside this layer is lost when the work that produced it is
archived.

## Reference, do not duplicate

Point at canonical project artifacts instead of copying them. A copy drifts, and once it
drifts nobody knows which version is true.

When a task needs project knowledge, link to where that knowledge lives. When a task
produces project knowledge, write it to where it belongs and link back.

## Route by goal

`.agents/` is a shared namespace, not a claim over every direct child. A recognized sublayer is a
direct functional area with its own managed `AGENTS.md` contract. Read the contract nearest to the
goal before reading its contents; it names the purpose, routing, authority boundary, contract and
content owners, lifecycle, suffix boundary, and treatment of unknown extensions.

**`tasks/`** is the recognized core lifecycle sublayer. Read `tasks/AGENTS.md` first for task
packages, coordination, and archive rules. `tasks/archive/` is internal archive structure, not a
separate sublayer.

**`skills/`** is the recognized interoperability sublayer. Read `skills/AGENTS.md` before using a
reusable procedure. Its packages remain owned by the authors, installers, or projects that put
them there.

**`worktrees/`** is the recognized disposable-operation sublayer. Read `worktrees/AGENTS.md` for
the checkout workflow. The checkouts are disposable project workflow state, not project context.

`context/` and `verification/` are candidates only; no contract or directory is implied here.
Any other direct child is an unrecognized extension. Preserve it and follow its own instructions
when it addresses your goal; do not classify or overwrite it as part of this layer.

The nearest applicable `AGENTS.md` governs a scope. A package or checkout may contain further
instructions owned by its author or project; those do not change the recognized sublayer contract.
<!-- agent-layer:end -->
