# Confirm proactive task creation and hold unjudged findings in context.md

## Status

Accepted

## Context

[0022](0022-route-findings-without-an-owning-task.md) already reads as standing authorization:
"Does the finding call for investigation, a decision, or a change? Then a `planned` task is
opened for that work." Nothing in that sentence, or in its installed copy in
`.agents/tasks/AGENTS.md`, conditions opening the task on being asked first — only the resulting
change's own review and approval require a human, exactly as *Who approves* already separates
authoring from acceptance.

In practice an agent working another task surfaced a finding that clearly met that bar — a
shipped skill leaking this repository's own decision numbers and test paths — and waited to be
told to open the task the finding called for, rather than acting on the rule's own authority. The
rule was already sufficient; nothing in its text said so plainly enough to stop the hesitation.

Separately, a request to extend that authority — to open a task for "ideas, problems and other
what we should implement or think later," encountered while working something else — reached
slightly further than `0022`'s trigger. `0022` already tested and rejected a version of "capture
everything that might matter later": routing every observation into a planned task "puts durable
project knowledge inside the layer, which the deletion test forbids," and "makes every
observation pretend to be work," producing "a backlog of tasks nobody intends to start" — a
named, accepted cost of the narrower rule it chose instead.

Widening the trigger to admit "an idea worth thinking about later" turns out not to add anything:
an idea not yet worth investigating is not yet worth anything operational, and one that is worth
investigating already clears `0022`'s bar as written. The real gap sits earlier than the trigger,
not at its edge — a raw idea noticed in passing needs somewhere to sit until someone judges it,
without being forced through triage on the spot (which produces the wrong answer as often as the
right one under whatever pressure produced the finding) and without being dropped for lack of
anywhere to write it down.

## Decision

Both questions in `0022`'s triage rule authorize action on their own, the moment a finding meets
one: opening a `planned` task, or adding to a project artifact. Neither needs to be asked for
first. `.agents/tasks/AGENTS.md` now says this explicitly, beside the two questions.

The trigger itself does not widen. "Calls for investigation, a decision, or a change" already
reaches as far as any idea worth keeping should reach.

`context.md` gains an optional Ideas section: a finding noticed while doing a task's own work but
not yet judged against the triage rule. It holds the finding until it is judged, not instead of
judging it — before the task is archived, each one is either acted on under the triage rule or
dropped. One still there at archival is treated the same as any other unfilled optional heading:
declared and never used.

## Consequences

An agent that meets the existing trigger no longer needs to be told to act on it. A raw,
not-yet-judged idea has somewhere to go that is neither a task's own operational state nor a
silent drop — but it still expires at archival rather than becoming a second durable-knowledge
channel the deletion test would need to cover.
