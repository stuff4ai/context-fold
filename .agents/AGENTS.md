# AGENTS.md — the agent layer

The agent layer holds how agents work on this repository, not what this repository knows.

These rules are stable. This file must never contain project state or current task
information.

## What the layer is

It is installed rather than authored here, and consists of exactly two things: these
`AGENTS.md` files, and what working here produces — the task index, task packages, and the
archive.

`.agents/` is where it lives, not what it is. Other tools write there too, and their files are
not part of the layer and not its concern. Nothing here claims the directory.

The `AGENTS.md` files are identical in every installation. They carry no project-specific
paths, names, or decisions. Do not edit them to fit this project, and expect them to be
replaced wholesale when the rules are updated.

If a rule here does not fit this project, record it as a problem in the task rather than
editing the rule. An edited rule stops being replaceable and becomes this project's to
maintain.

## Project truth lives outside the layer

Accepted, durable project knowledge belongs in the project's own artifacts — the code, its
tests, its documentation, and its decision records — wherever this project already keeps
them.

The deletion test:

> If humans need this information too, it does not belong only in the layer.

Remove the layer — these `AGENTS.md` files, the index, and the tasks — and read what remains.
The test fails if knowledge was lost, if something a human needs to understand or maintain the
project is now gone. Anything lost that way was in the wrong layer.

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

## Follow scoped instructions

Directories inside the layer carry their own `AGENTS.md` with rules for that scope. The
nearest one applies.

Work is organized under `tasks/`. Start there.
