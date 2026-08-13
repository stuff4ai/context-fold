# Record that stages are not one-way

## Status

active

## Objective

Record that work returns to earlier stages, and state the rule where agents read it.

## Why

The stage sequence in `.agents/tasks/AGENTS.md` is written as a single arrow from `planned` to
`merge`. Nothing says whether work may go backwards, and every task in this repository has:
`record-index-order` returned to work after its ordering rule failed on first use,
`record-methodology-before-tooling` returned twice after review, and this session's first task
revised its own rules while writing them.

An agent following the written sequence would treat a return as a deviation to explain rather
than the normal shape of the work. The design this came from made the same point in the
opposite direction — that development is several loops rather than one pipeline — and the
lifecycle that encoded those loops as separate stages was collapsed without carrying the
observation forward.

## Scope

- `decisions/0015-stages-are-not-one-way.md`.
- `decisions/README.md` index row.
- `.agents/tasks/AGENTS.md` — the Stages section.

## Out of scope

- Restoring the eleven-step lifecycle, or any stage that was cut.
- Counting or limiting iterations.
- `Status` values, which are unchanged and unaffected.

## Acceptance

1. The record states that stages describe order rather than a path, and that returning changes
   no `Status`.
2. Its Context carries the several-loops observation and why the stages encoding it were
   collapsed anyway.
3. `.agents/tasks/AGENTS.md` states the rule in the Stages section, in a form an agent can apply
   mid-task.
4. That file remains free of project-specific paths, names, and record numbers.
5. Consequences state that nothing distinguishes healthy iteration from a task that is stuck.

## Problems

### The written model had been contradicted by every task that followed it

Eight tasks ran the lifecycle, all of them returning to an earlier stage at least once, and
nothing recorded that as unusual — including the tasks that revised the lifecycle itself.
Assumed: a rule contradicted by practice produces friction that shows up in a problem log.
Actually: the contradiction was silent because the rule was permissive by omission. Nothing
forbade returning, so nobody hit a wall worth logging, and the written sequence quietly drifted
from the practice for eight tasks without a single entry.
The problem log catches friction, not absence of instruction. A rule that is merely incomplete
generates no evidence at all — which is the opposite of how this project assumed defects surface,
and means the audit that found this had no cheaper substitute.

### A sentence added to clarify the order stated it backwards

The new rule ended with "archival follows acceptance". `0007` puts archival *before* acceptance
— approval authorizes archival, and acceptance takes the archived state — and the same file says
so nine lines further down.
Assumed: a short clause restating settled ordering is safe to write from memory.
Actually: "acceptance" and "approval" are adjacent words for adjacent stages, and the sentence
was written to illustrate a different point, so it was never checked against the record that owns
the ordering. It inverted a decision while appearing to summarize it.
Fixed to "archival follows approval and precedes acceptance", with the record cited in `0015`.
Caught by review.

### Nothing in the verification tests consistency with existing decisions

The inverted ordering clause would have shipped. The duplication check looks for the same thing
stated twice; the deletion test looks for knowledge lost; the portability check looks for
project-specific detail; the index and link checks look for structural drift.
Assumed: between them, those cover a change to a rule file.
Actually: none of them reads a new statement against the records that already decided the same
subject. They verify structure and survival, not agreement. A confident sentence contradicting a
merged decision passes every check this project runs, and this one would have entered a portable
file that reaches every installation.
Not proposing a check. One instance is not a pattern, and inventing verification from a single
failure is the speculation `0012` argues against. Recorded so a second instance is recognizable
as a second rather than a first.
