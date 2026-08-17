# Route findings without an owning task

## Status

Accepted

## Context

[0013](0013-improve-context-from-the-work.md) captures friction in the task's `## Problems`
section, and that is the only destination the rules name. So learning that happens with no task
to hold it has nowhere legal to go.

Part of that gap was imaginary. [0007](0007-archive-before-merge.md) archives a task before the
change is accepted, and the rules read as though archival sealed the package — but `0007` says
the opposite: an archived package is amended if review requires it, and immutability applies from
merge onward. A finding produced while merging still has an owning task, and belongs in it.

What remains is real. Once a change is accepted, its task is history; editing it would rewrite
the record of something already merged. Findings arriving after that, or belonging to no task at
all, have no home. Three reached one only because a person carried them to the next task, or
because the fix happened to need a task of its own.

Meanwhile `planned` — "written down, not started" — was defined in the first task and never used
once across fifteen.

Two repairs were tried and rejected before this one.

Naming a project-layer file would prescribe another project's layout, which
[0005](0005-agents-layer-boundary.md) declines to do: the layer constrains what may live in
`.agents/`, not how the rest of a repository is arranged.

Routing *everything* into a planned task looked simpler and fails twice over. It puts durable
project knowledge inside the layer, which the deletion test forbids — a fact the project needs
would vanish with the layer, and a task later archived or cancelled buries it just as thoroughly
as the package it was rescued from. And it makes every observation pretend to be work, which
[0013](0013-improve-context-from-the-work.md) explicitly declines: a problem is an observation
until a person judges it into a change. A backlog of tasks nobody intends to start is a different
failure from losing findings, not an absence of one.

## Decision

A finding belongs to the task whose work produced it, for as long as that task is writable —
which is until the change is accepted, not until the package moves under `archive/`.

A finding with no such task is routed by two questions, asked independently. Both can be yes.

Would removing the layer lose durable project knowledge — something that must stay true or
visible even if no follow-up work is ever done? Then it goes in the project's own artifacts. The
layer is removable by design, and a task later archived or cancelled buries its contents as
thoroughly as the package the finding was rescued from.

Where a project has no artifact for it, the missing destination is named rather than worked
around. A `planned` task is opened to establish one and record the knowledge there. That task is
temporary operational state, not the home: it cannot be completed or cancelled until the
knowledge has been folded into the project layer.

Does the finding call for investigation, a decision, or a change? Then a `planned` task is opened
for that work. `Why` carries the self-contained account — what happened, what was assumed, what
was actually true — rather than a quotation of wherever it was first written, which may depend on
context the new task does not carry. `context.md` carries the provenance. `## Problems` opens
when the work does, because it records friction met while working, not the reason the work
exists.

The tests are not exclusive because the cases are not. "Should the project support X?" is
knowledge a reader needs and a decision someone must make.

Cancelling a task no longer skips folding. Work abandoned halfway may still have learned
something durable, and archiving it unfolded loses that exactly as completing it would. A task
opened to house knowledge until it has a destination depends on this: cancelling it must not be a
way to drop what it holds.

## Consequences

The archival gap turns out to be narrower than it looked. Most post-archival findings still have
an owning task, and the rules now say so instead of sending them somewhere new.

A finding that names work becomes visible in the index rather than held in someone's memory,
which is what decided whether the last three survived.

Triage happens at capture, by whoever found the thing, and they may get it wrong. Answering the
first question wrongly is the costly direction: knowledge a reader needed, filed only as work, is
deleted with the layer. Answering the second wrongly produces a task nobody starts, which is
visible and cheap to cancel.

Planned tasks still accumulate, and nothing prompts anyone to start or cancel one. Narrowing what
becomes a task slows that; it does not stop it.

The index lists planned tasks under Active, which is now slightly wrong: a planned task is
neither being worked nor archived. The status column disambiguates and the heading is unchanged,
because renaming it is churn until it demonstrably confuses someone.

A project with no home for its own durable knowledge still has to build one, and this says to
raise that rather than paper over it. The planned task carrying the finding meanwhile is a
holding position with an explicit exit condition, which is honest — and better than a fallback
that hides the gap by putting the answer somewhere it will be deleted.
