# Improve context from the work

## Status

Accepted

## Context

A repository accumulates knowledge about what it is and almost none about what it is like to
work on. The wrong assumption an agent made on Tuesday, the command that behaved unexpectedly,
the document that pointed somewhere stale — all of it stays in a transcript nobody reads again,
and the next agent makes the same mistake at the same cost.

Specification tools and task trackers do not address this. They record what should be built and
whether it was, which is a different question from whether the repository was any good to build
it in.

Two things make the friction recoverable. It has to be written down while it happens, because
recalling it afterwards produces a sanitized account of a process that felt smooth in
retrospect. And it has to accumulate somewhere durable, because a single instance is
indistinguishable from bad luck — the same problem appearing across several tasks is what
turns an anecdote into evidence.

The obvious design was an apparatus for this: a lifecycle with a stage for problem-solving, one
for retrospective, one for context improvement, and a task package with artifacts for
requirements, design, iterations, problems, verification, and publishing. Eleven steps and
eight files. It was cut to a four-value status with stages, and three files of which one is
optional.

The reason for the cut is the loop itself. Ceremony nobody performs produces no evidence, and a
problem log that costs a form to fill in stays empty. The capture has to be cheaper than the
irritation of the problem, or it does not happen at the moment it has to happen.

## Decision

Work produces problems; problems become lessons; lessons change the context the next agent
reads.

Friction is recorded in the task's `## Problems` section during the work, in a few lines: what
happened, what was assumed, what was actually true. This is what makes the mechanism in
[0006](0006-task-package-model.md) worth its cost — the section exists to feed this loop, not
to document a task.

Problems are observations, not conclusions. A pattern appearing across several tasks is a
candidate lesson, and a candidate becomes a rule only through a reviewed change to the
documents that carry rules — a decision record, or the instructions an agent follows. Nothing
promotes itself.

The last step is deliberately manual. A person reads the accumulated problems, judges what
recurs, and decides what to change. No automation performs that step, and none is required for
the loop to run.

A completed task is expected to leave the repository slightly better to work in than it found
it. Where it does not, the problem log says why.

## Consequences

The repository accumulates evidence about itself that no other artifact captures, and later
decisions can cite instances rather than impressions.

The loop's weakest step is the one that closes it. Nothing forces anyone to read accumulated
problems, and a project that stops doing so keeps paying the capture cost while receiving
nothing — the failure is silent, because the logs still look healthy.

Capture depends on judgment about what counts as friction, and that judgment degrades as work
feels routine. An empty problem log is more likely to mean the habit lapsed than that nothing
went wrong.

Problems accumulate in archived packages, which are immutable and rarely re-read. Evidence
gathered this way is only as findable as whatever points at it.

Keeping capture cheap means the model records less than it could. The stages and artifacts that
were cut would each have produced something, and the loop is a bet that unfilled structure is
worth less than a habit that survives.
