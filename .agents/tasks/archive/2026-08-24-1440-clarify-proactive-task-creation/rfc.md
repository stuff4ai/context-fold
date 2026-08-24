---
status: resolved
---

# RFC — clarify proactive task creation

## Problem

`decisions/0022-route-findings-without-an-owning-task.md` already says: "Does the finding call
for investigation, a decision, or a change? Then a `planned` task is opened for that work."
Nothing in that sentence, or in its installed copy in `.agents/tasks/AGENTS.md`, conditions
opening the task on being asked first — only the eventual change's approval and merge require a
human. In practice, though, an agent working another task waited to be told to open one rather
than acting on its own trigger. Whether that hesitation was the rule being unclear, or the agent
misreading a clear rule, is itself worth settling — an ambiguous rule and an overcautious reading
of a clear one look the same from outside, and only one of them needs a text change.

Separately, the request that prompted this — "you can create tasks when you are working with
another task because you can find something like ideas, problems and other what we should
implement or think later" — reaches slightly further than `0022`'s trigger. `0022` already
tested a version of "capture everything that might matter later" and rejected it: routing every
observation into a planned task "puts durable project knowledge inside the layer, which the
deletion test forbids," and "makes every observation pretend to be work," producing "a backlog
of tasks nobody intends to start" — named in that record as a real, accepted cost of the
narrower rule it chose instead, not a hypothetical one. Whether "ideas ... to think about later"
is the same shape as "calls for investigation, a decision, or a change," or a wider category that
risks recreating the rejected design, is the second thing this RFC needs to settle.

## Current proposal

Two separable changes; only the first currently has a clear direction.

1. **Proactive creation under the existing bar.** State explicitly, in
   `.agents/tasks/AGENTS.md`'s "When a finding has no owning task" section, that opening a
   planned task under either triage question needs no prior permission — only the resulting
   change's approval and merge do, exactly as `## Who approves` already separates authoring from
   accepting. This is a clarification, not a new authorization: the rule already reads this way;
   saying so out loud stops the next agent from hesitating the way this one did.

2. **Whether the trigger itself should widen.** Not yet resolved. The request that prompted this
   task reaches for "ideas ... to think about later," which is broader than "calls for
   investigation, a decision, or a change." Widening the bar without also reopening `0022`'s
   explicitly-tested-and-rejected "everything becomes a task" design needs either: a narrower new
   category that is demonstrably not that, defined precisely enough to tell them apart, or a
   decision that the existing bar already covers everything worth keeping — an idea worth keeping
   is, definitionally, one that calls for at least investigation.

## Alternatives

- **Do nothing; treat the rule as already sufficient.** The text already permits proactive
  creation under the existing bar; the gap was one agent's caution, not the rule. Closes item 1
  by declaring the clarification unnecessary. Leaves item 2 unaddressed.
- **Widen the trigger to include any idea worth recording**, whether or not it yet calls for
  investigation, a decision, or a change. Closest to the original request's wording. Directly
  risks recreating the design `0022` tested and rejected — needs to answer, specifically, why
  this is different from "routing everything into a planned task," not just assert that it is.
- **Add a lighter-weight place for a not-yet-actionable idea** — for example, a running list
  inside the *current* task's `context.md`, distinct from a new task package and with no
  lifecycle of its own — so an idea has somewhere to land without becoming operational state that
  must eventually be started or cancelled. Untested against `0022`'s objections; worth weighing
  against them explicitly before adopting.

## Open questions

- Is "an idea worth thinking about later" ever something that does *not* call for at least
  investigation? If not, item 2 may already be closed by `0022` as written, and the original
  request is fully satisfied by item 1 alone.
- If the trigger does widen, what stops the resulting backlog from being the exact cost
  `decisions/0022`'s Consequences already named and accepted as a risk of the narrower rule — at
  a larger scale?
- Does "proactive" mean an agent should open such a task without narrating the decision to the
  user first, or only that it needs no advance permission? `0022`'s own text already separates
  authoring from approval; this task's Scope keeps that separation rather than reopening it.

## Resolution

Item 1 is confirmed as written: `0022`'s triage rule already authorizes opening a `planned` task,
or adding to a project artifact, the moment a finding meets one of its two questions — no advance
permission needed, only the resulting change's own review and approval. `.agents/tasks/AGENTS.md`
now says this explicitly, next to the two questions, so the next agent does not hesitate the way
this one did.

Item 2 does not widen the trigger. The first open question above answers itself: an idea not yet
worth investigating is not yet worth anything operational, and one that is worth investigating
already clears `0022`'s bar as written. There is no idea worth keeping that the existing trigger
fails to reach.

What the trigger did lack was a place for the moment *before* judgment — a raw idea noticed in
passing, not yet weighed against the triage rule. The third alternative above answers that:
`context.md` gains an optional Ideas section, holding a finding until it is judged rather than
forcing that judgment on the spot. It expires at archival like any other optional heading — acted
on under the triage rule, or dropped — so it never becomes a second durable-knowledge channel
alongside the one `0022` already closed off.

Recorded as `decisions/0039-confirm-proactive-task-creation-and-hold-unjudged-findings.md`.
