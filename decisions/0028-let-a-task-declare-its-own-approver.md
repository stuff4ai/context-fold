# Let a task declare its own approver

## Status

Accepted

## Context

`0019` hard-coded the only path to merge authorization: "An agent may merge a pull request once
a human has approved it." Every task, regardless of size or risk, waited on the same one person.
That makes the human a bus factor for a project whose own model is meant to let work continue
without depending on any one thing.

`0027`, produced immediately before this one, established what a fresh reader is worth that the
author of a change is not: across a run of pull requests, a fresh verifier found something real
in every one that reached it, none of it reachable by the mechanical checks already in place. The
verifier role exists exactly to be someone other than the author, returning a `CONFIRMED`,
`REFUTED`, or `INCONCLUSIVE` verdict against an exact claim. The trust this project has already
extended to that role — as evidence for a human, not as a replacement for one — is the direct
precedent for extending it further.

## Decision

A task's `## Approval` declares who satisfies review and approval: `Human`, the default when a
task says nothing, or `Verifier`, a fresh verifier's `CONFIRMED` verdict against the task's own
acceptance criteria. Declared when the task is written, alongside `## Scope`, never mid-flight —
the full rule, including the two cases that default to human regardless of a project's setting,
is in `templates/agents/tasks/AGENTS.md` under *Who approves*.

Root `AGENTS.md` states the project's default explicitly: a pull request is not merged until it
is approved — a human's, by default, or a fresh verifier's `CONFIRMED` verdict when the task's own
`## Approval` says so.

`0023`'s Decision needed no change — it already speaks of "review" and "a reviewer" without
naming a human, leaving who fills that role open on purpose. Its Consequences did: "What a human
approves is what merges" stated the norm as universal, and this decision makes it one of two.
Status narrowed rather than the sentence rewritten, since the record is accepted.

No mechanical check binds a task's `## Approval` value, or confirms that a verifier-approved
merge actually carried a `CONFIRMED` verdict. `## Blocked by` shipped the same way — declared,
unenforced — and this follows the precedent rather than inventing a new one for this case alone.

This task's own merge is approved by a human. The mechanism it creates does not authorize its
own bypass; nothing before this decision could have.

## Consequences

Most work can proceed without waiting on the one person who has approved every task so far. What
it waits on instead is a fresh reader who did not write it — the same standard `0027` already
asked of a self-run check, now extended to who may close it out.

The two cases that keep a human — a task about the approval mechanism itself, a task whose
acceptance criteria leave a real choice rather than a checkable claim — are judgment for whoever
writes the task, not a rule a program enforces. A task could misclassify itself, and nothing
catches that except a reader noticing, which is weaker than a check and stronger than nothing.

A verifier confirming a verifier-approved task is asked to confirm the task's acceptance
criteria, not to re-judge whether the task should have been verifier-approved at all. That
question is left to the same weak enforcement as the classification itself. Recorded here as a
real gap rather than closed by expanding what a verifier is asked to do beyond `0027`'s own
scope.

Nothing traces, from the merged pull request alone, that a `CONFIRMED` verdict actually preceded
it. The Outcome recording it, which every task in this project has done by habit, is what stands
in for that trace; nothing requires the habit to continue.
