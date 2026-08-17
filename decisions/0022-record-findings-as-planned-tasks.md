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

Meanwhile `planned` — "written down, not started" — was defined in the first task and never used
once across fifteen.

Two repairs were tried and rejected before this one.

Naming a project-layer file would prescribe another project's layout, which
[0011](0011-keep-the-model-vendor-neutral.md) declines to do.

Routing *everything* into a planned task looked simpler and fails twice over. It puts durable
project knowledge inside `.agents/`, which the deletion test forbids — a question humans need
would vanish with the layer, and a task later archived or cancelled buries it just as thoroughly
as the package it was rescued from. And it makes every observation pretend to be work, which
[0013](0013-improve-context-from-the-work.md) explicitly declines: a problem is an observation
until a person judges it into a change. A backlog of tasks nobody intends to start is a different
failure from losing findings, not an absence of one.

## Decision

Where a finding goes when no task is open depends on what it is, and deciding that is the work.

Something to do — an investigation, a decision, a change — becomes a `planned` task. The
observation goes in its `## Problems` as a self-contained account: what happened, what was
assumed, what was actually true, and where the evidence is. Not a quotation of wherever it was
first written, which may depend on context the new task does not carry. The Objective is what the
task would achieve.

Something the project needs to know — an open question, a constraint, a fact about how the
project works — goes to the project's own artifacts. If the project has nowhere for it, that is
said and asked about rather than resolved by leaving it in the layer.

Findings during a task are unchanged: they go in that task's `## Problems`.

Cancelling a task no longer skips folding. Work abandoned halfway may still have learned
something durable, and archiving it unfolded loses that exactly as completing it would.

## Consequences

A finding that names work becomes visible in the index rather than held in someone's memory,
which is what decided whether the last three survived.

The task shape forces the question of what should be done. A finding with no answer to that is
not filed as work; it is either project knowledge or it was not worth keeping.

Triage happens at capture, by whoever found the thing, and they may get it wrong. An observation
misjudged as project knowledge goes somewhere no one revisits; one misjudged as work becomes a
task nobody starts.

Planned tasks still accumulate, and nothing prompts anyone to start or cancel one. Narrowing what
becomes a task slows that; it does not stop it.

The index lists planned tasks under Active, which is now slightly wrong: a planned task is
neither being worked nor archived. The status column disambiguates and the heading is unchanged,
because renaming it is churn until it demonstrably confuses someone.

A project with no home for its own open questions still has no home for them. This says to raise
that rather than paper over it, which is honest and unsatisfying — and better than a fallback
that hides the gap by putting the answer somewhere it will be deleted.
