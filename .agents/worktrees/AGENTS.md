# AGENTS.md — worktrees

Parallel checkouts live here, one per task, named for its slug. Git ignores everything in this
directory except this file.

## These are not context

Each entry beside this file is an ordinary checkout of this repository on another branch, with
its own `.agents/` inside it. Nothing durable belongs here. Delete every one of them and no
project knowledge is lost — only work in progress.

Do not read a worktree as part of this repository. Its `decisions/`, its task packages and its
`INDEX.md` belong to another branch, and treating them as this branch's produces a second,
contradictory copy of everything. Current project truth is `decisions/` and `.agents/tasks/` at
the repository root.

The rules that apply inside a worktree are the ones in that checkout, not this file. An agent
working there is at the root of a full repository and should read it as one.

## Lifecycle

Created and removed with `git worktree add` and `git worktree remove`. A worktree whose task has
merged is finished — remove it rather than leaving it to drift against `main`.

This is this project's workflow, not part of the agent layer. The portable rules say how
concurrent tasks share files and declare what blocks them, and name no version control system:
see `.agents/tasks/AGENTS.md`.
