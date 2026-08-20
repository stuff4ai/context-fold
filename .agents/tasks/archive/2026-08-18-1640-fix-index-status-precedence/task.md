---
status: completed
objective: >-
  Correct the precedence rule so it repairs the file that is actually stale, rather than always
  assuming the index is.
---

# Fix which file wins when the index and a task disagree

## Why

`tasks/AGENTS.md` says the index is a derived view and that `task.md` owns canonical status: "if
this table disagrees with a task file, the task file is right and this table needs repair."

A foreign adoption run produced the opposite case. Archiving updates two things — the task's
Status and the index row — and the agent finished one. `INDEX.md` said `completed`; the archived
`task.md` still said `active`. A second agent found the disagreement and corrected `task.md`,
against the letter of the rule, and was right to.

The rule assumes disagreement means the derived view drifted. The observed failure mode is the
canonical file lagging, because it is updated first and the archival move happens between the two
edits. Following the rule literally would have reverted a finished task to `active` and put the
index back in step with a lie.

This is a defect in a portable rule, so every installation currently has it. It was unreachable
from this repository: no task here has ever been left half-archived.

## Scope

- `templates/agents/tasks/AGENTS.md` — the precedence sentence under `## Finding work`, and
  anything in `## Index conflicts` that inherits from it.
- A decision record, and whatever `0006` or `0009` need in their Status.

## Out of scope

- Making the index generated rather than hand-maintained. That is deferred capability, and this
  rule has to be right either way.
- The ordering rules for the index, which are `0009`'s and are not implicated.

## Acceptance

1. The rule says how to tell which file is stale rather than assuming, and an agent reading it
   would have corrected `task.md` in the observed case.
2. The reasoning names the failure mode: archival updates two files and can stop between them.
3. Every statement of precedence across the rules agrees.

## Outcome

The task's directory now settles a status disagreement. A package under `archive/` is finished
whatever `task.md` says; one that is not is unfinished whatever the index says. `task.md` still
wins where the location cannot tell them apart, such as `completed` against `cancelled`.

The arbiter works because it is the one fact neither file asserts, and because `0007` fixes what
the location means. It deliberately does not reason from the order of the steps: the observed run
did the second and third and skipped the first, so reaching a later step implies nothing about an
earlier one. A disagreement therefore means finishing did not happen cleanly, and the rule says to
check the whole sequence rather than only the field that disagreed.

"Canonical" is gone. It was the word doing the damage — it made every disagreement the index's
fault, which is what the foreign run's successor had to override to be right.

Durable artifacts:

- `decisions/0024-settle-status-disagreements-by-the-directory.md` — the decision.
- `decisions/0006-task-package-model.md` — Status: a third narrowing.
- `skills/ctxfold-init/templates/agents/tasks/AGENTS.md` — `## Finding work`, and a note in
  `## Index conflicts` that rebuilding copies a task's status, so a disagreement must be settled
  before regenerating or the index becomes consistent and wrong.
- `skills/ctxfold-init/templates/INDEX.md` and `.agents/tasks/INDEX.md` — the header, which
  states the rule and had to be edited in both places by hand.
- `OPEN-QUESTIONS.md` — the gap entry removed; a new one added for `INDEX.md`'s header, which
  carries rules but has neither an upgrade path nor a check.

## Problems

### The rule lived in a file the reinstall loop does not touch

Changing the rule meant editing `templates/agents/tasks/AGENTS.md` and reinstalling, which is the
routine. It also lives in `INDEX.md`'s header.
Assumed: reinstalling `templates/agents/` propagates a rule change to this repository's
installation, because that is what it has always done.
Actually: `0021` deliberately moved `INDEX.md` out of `templates/agents/`, so the reinstall loop
skips it and the identity check does not cover it. The shipped header and the installed one had
to be edited separately, and they agree now because a sweep found the second copy rather than
because anything binds them.
Worse for an adopter: `INDEX.md` is copied once and never replaced, so an installation made
before today keeps the old rule permanently and nothing anywhere will say so.
Found by sweeping for statements of the rule, not by the checks.

### A record's Status is accumulating narrowings faster than it is being read

`0006` now carries three, from `0022` twice and `0024` once, in a paragraph a reader meets before
the Context.
Assumed: a Status narrowing is a cheap, local repair, so more of them cost nothing.
Actually: each is cheap and the pile is not. The Status has become a list of things the record
got wrong, which is the point at which superseding it whole is more honest than narrowing it
again. Recorded in `0024`'s Consequences rather than acted on, because replacing `0006` is a
larger change than this task.

### The record's rationale was refuted by the record's own Context

`0024` argued that the directory move "partitions the failure: if the move happened, the edits
before it happened too". Four paragraphs above, its own evidence says the run archived the
package, updated the index, and never set the Status — which `## Finishing` orders first.
Assumed: an agent that reaches step two has done step one, so the sequence fails by truncation.
Actually: it failed by skipping. A step can be omitted as easily as a run can stop, and nothing
makes the steps atomic with each other. The argument asserted the impossibility of the failure
the record exists to fix.
The rule survived because it rested on a second, independent ground — the directory is the one
fact neither file asserts — so only the reasoning was wrong. But the reasoning is the part that
would have taught the next reader, and a record is immutable once merged.
Found by a fresh verifier, which also noticed the claim had been copied into the Outcome and the
assumption behind it into `context.md`. This is the second time in three tasks that a record
contradicted itself; `0023` exists because `0007` did.
The skipped-step model is the stronger argument and now carries the record: precisely because
reaching a later step implies nothing about an earlier one, an inference about which file ran is
worthless and a fact outside both is required.
