---
name: ctxfold-init
description: >
  Install the context-fold agent layer into a repository: a task package structure under
  .agents/, a pointer in the root AGENTS.md, and a first task recording the adoption.
  Works on an empty repository, one with years of history, or one that has already adopted
  it; repeat runs update managed rule blocks while leaving project additions and anything
  else already under .agents/ untouched.
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

## Install or update, then verify

The install step is a file copy, not a transcription. Agents that edit by patch tend to
reproduce file contents from what they have read, which yields files that differ from the
originals in ways nobody notices — a rewrapped line, a paragraph dropped, a file forgotten
entirely.

On a fresh adoption, copy the files, then compare each installed file byte-for-byte against its
template before going further. If they differ, the copy failed; do it again rather than editing
the installation until it matches.

On a repeat run, do not copy whole files over an installation that has managed blocks. Follow
`ADOPTING.md`'s two-phase update literally: classify all portable targets before writing any,
abort all of them if one marker structure is ambiguous, then replace only valid managed blocks
and restore every recorded suffix byte. An unmarked target still belongs to the legacy whole-file
contract and is replaced wholesale.

After updating, compare each installed managed block byte-for-byte against its template and
compare every preserved suffix against the bytes recorded during preflight. A correct block with
a project suffix is intentionally not byte-identical to the whole template file.

## Ignore what must not be committed

Adoption adds a directory whose contents are checkouts, not context, and one file inside it that
explains that. Both `.gitignore` lines the procedure gives are needed and their order matters —
a directory excluded outright is never descended into, so the exception would never apply.

Create `.gitignore` if the repository has none. Append to it if it has one; do not rewrite it.
Then confirm the file is tracked and the directory is not, by asking the version control system
what it sees rather than by reading the ignore rules — a negation pattern is easy to write and
easy to get backwards.

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

## Stop before merging

Complete the work, satisfy the acceptance criteria, then finish the task: write the Outcome, fold
anything durable out into the project's own artifacts, archive the package, and run the final
exact-head check. `.agents/tasks/AGENTS.md` describes all of it.

Then stop. Do not merge anything. Approval authorizes the merge and has not been given — and a
reviewer asked before the Outcome exists is being asked to approve a promise.

Report what you did, what you could not do, what the problem log says, and ask for approval.
