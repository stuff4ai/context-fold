# AGENTS.md — the `.agents/` layer

`.agents/` is the agent operating layer. It holds how agents work on this repository, not
what this repository knows.

These rules are stable. This file must never contain project state or current task
information.

## What here is portable

The `AGENTS.md` files in this layer are identical in every project using context-fold. They
carry no project-specific paths, names, or decisions. Treat them as installed rather than
authored: do not edit them to fit this project, and expect them to be replaced when
context-fold is updated.

Everything else under `.agents/` is this project's own, produced by working here — the task
index, task packages, and the archive.

If a rule here does not fit this project, that is a context-fold problem, not a local one.
Record it as a problem in the task rather than editing the rule, or the layer stops being
upgradable.

## Project truth lives outside `.agents/`

Accepted, durable project knowledge belongs in the project's own artifacts — the code, its
tests, its documentation, and its decision records — wherever this project already keeps
them.

The deletion test:

> If humans need this information too, it does not belong only in `.agents/`.

Remove `.agents/` and read what remains. The test fails if knowledge was lost — if something a
human needs to understand or maintain the project is now gone. Anything lost that way was in
the wrong layer.

It does not fail on references to the layer. Removing `.agents/` is an ordinary change, and
whatever pointed at it is updated in the same change.

Belongs outside `.agents/`: architecture, domain knowledge, requirements, decisions, API
documentation, product vocabulary.

Belongs inside `.agents/`: agent navigation, task coordination, agent operating rules,
task lifecycle state, temporary working context.

Knowledge left sitting only inside this layer is lost when the work that produced it is
archived.

## Reference, do not duplicate

Point at canonical project artifacts instead of copying them. A copy drifts, and once it
drifts nobody knows which version is true.

When a task needs project knowledge, link to where that knowledge lives. When a task
produces project knowledge, write it to where it belongs and link back.

## Follow scoped instructions

Directories inside `.agents/` carry their own `AGENTS.md` with rules for that scope. The
nearest one applies.

Work is organized under `tasks/`. Start there.
