<!-- agent-layer:begin -->

# AGENTS.md — the agent layer

> **Managed rule block.** Updates replace everything between the `agent-layer` markers.
> Do not edit this block. Add only non-conflicting project instructions after the end marker.

The agent layer holds how agents work on this repository, not what this repository knows.

These rules are stable. This file must never contain project state or current task
information.

## What the layer is

It is installed rather than authored here, and consists of exactly two things: the managed
blocks in these `AGENTS.md` files, and what working here produces — the task index, task
packages, and the archive.

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

Remove the layer — the managed rule blocks, the index, and the tasks — and read what remains.
The test fails if knowledge was lost, if something a human needs to understand or maintain the
project is now gone. Project-owned suffixes remain. Anything lost that way was in the wrong layer.

It does not fail on references to the layer. Removing it is an ordinary change, and whatever
pointed at it is updated in the same change.

Anything else under `.agents/` belongs to whatever put it there. Leave it alone; it is not part
of this test.

Belongs outside the layer: architecture, domain knowledge, requirements, decisions, API
documentation, product vocabulary.

Belongs inside it: agent navigation, task coordination, agent operating rules, task lifecycle
state, temporary working context.

Knowledge left sitting only inside this layer is lost when the work that produced it is
archived.

## Reference, do not duplicate

Point at canonical project artifacts instead of copying them. A copy drifts, and once it
drifts nobody knows which version is true.

When a task needs project knowledge, link to where that knowledge lives. When a task
produces project knowledge, write it to where it belongs and link back.

## What you will find under `.agents/`

More than the layer. Each thing here has an owner, and knowing which is which is the difference
between reading this project's current state and reading a copy of it.

**`tasks/`** — the layer's. How work is organized, tracked and finished, and the task packages
and index that working here produces. Its rules are in `tasks/AGENTS.md`. Start there.

**`skills/`** — not the layer's. Agent tooling installs reusable procedures here, by a convention
this layer neither defines nor relies on. What is there answers to whatever put it there: read it
if it is addressed to you, and do not treat it as a statement about this project.

**`worktrees/`** — parallel checkouts, if this project keeps any, and not the layer's: the
workflow is this project's own, described in `worktrees/AGENTS.md`. That file's managed block
ships byte-identical, the same as this one; everything beside it is checkouts, not context — each a
separate copy of this repository at a different point in its history, so reading one as part of
this copy produces a second and contradictory version of every record and task package.

Directories inside the layer carry their own `AGENTS.md` with rules for that scope, and the
nearest one applies. Anything else you find here answers to whatever created it.
<!-- agent-layer:end -->
