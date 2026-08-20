# Record a cross-stack handoff in the task package

## Status

Accepted

## Context

More than one agent stack now works this repository. Each runs its own orchestration policy,
dispatches its own named roles, and keeps its own session history that the other cannot read.

The task package already carries the contract, the curated context, the proposal and the plan.
Nothing in it says how one stack asks another for something, or where the answer goes. Without
somewhere to put that exchange it happens in two transcripts: the request, the revision it
referred to, and the verdict all disappear when the sessions end. A repository whose distinctive
claim is that work leaves a record loses the record of precisely the moment two agents disagreed.

Live channels between the stacks exist and work. Both products can run as an MCP server, each
can invoke the other non-interactively, and orchestrators exist that hold several CLIs open at
once. All of them move the exchange out of the repository and into a running process, which is
the property that makes it unreadable afterwards. They also add a channel a dispatched role
could use to delegate onward, which the stacks' own policies forbid it from doing.

`0006` fixes what a package contains, and `0035` created a boundary — the `agent-layer:end`
marker — after which an installation may add its own instructions without forking the portable
rules. That boundary is what makes it possible to try a new package artifact in one repository
before deciding whether every installation should carry it.

## Decision

A task that is worked by more than one agent stack carries `handoff.md` in its package: an
record of requests between stacks and the answers to them. Each exchange is an entry carrying an
id, the addresses it is from and to, its state, the commit under review, and the vocabulary the
answer must use. An entry is not rewritten once dispatched: its request text
is fixed then, and answering it changes only the state and fills the return.

Five rules govern it, stated in full in `.agents/tasks/AGENTS.md`: address by role and never by
model; an entry addressed elsewhere is not yours; answer in the vocabulary the request names;
commit the request before dispatching it; and stop after asking.

The convention is stated as this repository's project suffix, after the `agent-layer:end` marker
in `.agents/tasks/AGENTS.md`. It is not added to the portable managed rule block.

Placing it in the suffix is the substance of this decision, not an implementation detail. `0012`
commits this project to building the methodology before the tooling that would hide its
weaknesses, and to being its own first user. Distributing a rule to every adopter before it has
been followed once here inverts that: the portable rules would describe a practice rather than
record one. The objection is to distributing an unexercised rule, not to ceremony — `handoff.md`
is optional exactly as `rfc.md` and `plan.md` already are, so promoting it would oblige no task
to carry one.

The rules are nonetheless written to be stack-agnostic, naming a stack and a role rather than any
product. Which stacks exist is a fact about an installation; that a handoff addresses a role is
not. This is `0011`'s split — a neutral model, with the product-specific part outside it — applied
inside a suffix, so that promotion later is a move rather than a rewrite.

Promotion is deferred rather than refused, and the observations that would reopen it are named
in the task's RFC and carried into `OPEN-QUESTIONS.md`: repeated use without the format changing,
a second repository asking for the same convention, an exchange that crosses a person rather than
a subprocess, or two stacks holding one package at once.

## Consequences

An exchange between two stacks is now readable in the pull request that contains it, by a
reviewer who was present for neither session. The revision each verdict refers to is recorded, so
a return can be judged against the state it actually described.

The convention needs nothing running. It also does nothing on its own: the repository does not
deliver a request, and a handoff waits until something outside moves the work to the other stack.
That cost is accepted for now — it is the same cost `0012` accepted generally, and automating it
before the format has been used twice would settle the format by accident.

An adopter of the distribution gets none of this. The convention helps this repository only,
until evidence justifies promoting it, and a suffix is not something another project discovers.

`0035`'s suffix is exercised for the first time. If additive project instructions turn out to
strain against the portable rules in practice rather than in principle, this is where that shows.
