---
name: ctxfold-init
description: >
  Install the context-fold agent layer into a repository: a task package structure under
  .agents/, a pointer in the root AGENTS.md, and a first task recording the adoption.
  Works on an empty repository, one with years of history, or one that has already adopted
  it, and leaves anything else already under .agents/ untouched.
  Trigger: /ctxfold-init, "adopt context-fold", "set up the agent layer".
---

# Initialize context-fold

## What to follow

The procedure is [`ADOPTING.md`](ADOPTING.md), beside this file. Read it and follow it. Its
steps are not repeated here.

`templates/` is beside this file too. Everything the procedure tells you to copy is there;
nothing needs fetching.

This file covers only what the procedure leaves to you.

## Find the workflow before changing anything

How a change gets made, reviewed, and accepted is the project's business, not the layer's. The
layer's rules say review and merge mean whatever the project defines them to mean.

Read the repository's root `AGENTS.md` first, and follow whatever it says about branching,
commits, and review.

If it says nothing — or does not exist — make the changes in the working tree, commit nothing,
and say so when you report. Do not invent a branch name, a commit convention, or a review
process for a project that has not chosen one.

## Copy, then verify

The install step is a file copy, not a transcription. Agents that edit by patch tend to
reproduce file contents from what they have read, which yields files that differ from the
originals in ways nobody notices — a rewrapped line, a paragraph dropped, a file forgotten
entirely.

Copy the files, then compare each installed file byte-for-byte against its template before
going further. If they differ, the copy failed; do it again rather than editing the
installation until it matches.

## Supply the judgment the procedure asks for

Two steps need something only a reader of this repository can provide.

**The pointer.** When a root `AGENTS.md` already exists, add the section without rewriting what
is there — it belongs to the project. When there is none, the file you create should say what
the project is and how to work on it, not only that a layer exists.

**Task zero's base state.** Describe this repository as it actually is: what it contains, what
conventions it already follows, where its durable knowledge lives, and what else already writes
to `.agents/`. This is the one part of the adoption that cannot be copied, and a generic answer
here makes the task package worthless to whoever reads it next.

## Log friction while it happens

Anything that made the adoption awkward goes under `## Problems` in task zero as you hit it: a
step that did not fit, a rule that contradicts something the project already does, an
instruction that assumed a repository unlike this one.

Write it when it happens. Recalling it afterwards produces a tidy account of a process that felt
smooth in retrospect.

## Stop before archiving

Complete the work and satisfy the acceptance criteria. Then stop.

Do not archive the task, and do not merge anything. Approval authorizes archival, and it has not
been given — an agent that archives unasked has skipped the gate the layer exists to keep.

Report what you did, what you could not do, what the problem log says, and ask for approval.
