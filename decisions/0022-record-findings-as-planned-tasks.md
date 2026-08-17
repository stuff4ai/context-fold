# Record findings as planned tasks

## Status

Accepted

## Context

[0013](0013-improve-context-from-the-work.md) captures friction in the task's `## Problems`
section, and that is the only destination the rules name. So learning that happens with no task
open has nowhere legal to go.

That is not an edge case. [0007](0007-archive-before-merge.md) archives a task before the change
is accepted, so everything discovered while merging — the last stage of every task — arrives
after the package is immutable. Three findings reached a home only because a person carried them
to the next task, or because the fix happened to need a task of its own.

The obvious repair fails. "Put it in the project layer" is the sentence the rules already use for
questions that outlive a task, and a foreign adoption run showed what it is worth: told an
outliving question belonged there, the agent found no such place in that repository and filed it
into the package that gets archived. Naming a file instead would prescribe another project's
layout, which [0011](0011-keep-the-model-vendor-neutral.md) declines to do.

Meanwhile `planned` — "written down, not started" — was defined in the first task and never used
once across fifteen.

## Decision

A finding that arrives when no task is open becomes a `planned` task.

The finding goes verbatim in that task's `## Problems`. Its Objective is the question to resolve:
what should be done about this. It stays in the index until someone starts it or cancels it.

The same route handles a question that outlives its task in a project with no place for one.

Findings during a task are unchanged: they go in that task's `## Problems`, which works.

This needs nothing a project does not already have. A planned task lives in `tasks/`, which every
installation has by definition, so no project-layer artifact is created and no layout is imposed.

## Consequences

A finding is visible in the index rather than held in someone's memory, which is what decided
whether the last three survived.

The task shape asks what should be done, which an observation filed as prose does not. A finding
with no answer to that question may not have been worth keeping.

Not every finding is work. Some are evidence — a pattern with three instances and no obvious
remedy — and forcing those into a task makes a package nobody intends to start. The Objective
becomes "decide whether this matters", which is honest but thinner than a real task.

Planned tasks accumulate. Nothing prompts anyone to start or cancel one, and an index filling
with parked findings is a different failure from losing them, not an absence of failure.

The index lists them under Active, which is now slightly wrong: a planned task is neither being
worked nor archived. The status column disambiguates and the heading is unchanged, because
renaming it is churn until it demonstrably confuses someone.
