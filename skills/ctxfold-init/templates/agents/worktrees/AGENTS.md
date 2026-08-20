# AGENTS.md — worktrees

Parallel checkouts live here, one per task, named for its slug. This project's version control
ignores everything in this directory except this file.

The `AGENTS.md` files are identical in every installation. They carry no project-specific
paths, names, or decisions. Do not edit them to fit this project, and expect them to be
replaced wholesale when the rules are updated.

## These are not context

Each entry beside this file is a separate copy of this repository at a different point in its
history, with its own `.agents/` inside it. Nothing durable belongs here. Delete every one of
them and no project knowledge is lost — only work in progress.

Do not read a worktree as part of this repository. Its decision records, its task packages and
its `INDEX.md` are another copy's, and treating them as this one's produces a second and
contradictory version of everything. Current project truth is what sits at the repository root.

One thing beside this file is worth opening: another task's `task.md`, to see what it claims.
The rules ask you to read the other active tasks before starting, and while those tasks are being
worked their packages exist only in their own checkouts — here. Read them as another copy's
claims about what it holds, which is the opposite of reading them as this one's truth.

The rules that apply inside a worktree are the ones in that checkout, not this file. An agent
working there is at the root of a full repository and should read it as one.

## Lifecycle

With Git, `git worktree add .agents/worktrees/{task-slug}` and `git worktree remove` when the
task has been accepted. Another version control system will have its own spelling; the rule is
one checkout per task, named for the task.

A worktree whose task has landed is finished. Remove it rather than leaving it to drift.

Merging from inside a task's own worktree needs its own order. `main` is checked out at the
repository root the whole time a task worktree exists, so a merge command that tries to also
check out `main` in the worktree it runs from — `gh pr merge --delete-branch`'s local half does
this — fails there, even though the merge itself already went through. Merge first without that
flag, remove the worktree, then delete the branch: `gh pr merge <N> --squash`, `git worktree
remove .agents/worktrees/{task-slug}`, `git branch -D {branch}`, `git push origin --delete
{branch}`.

This is a workflow, not part of the agent layer. The portable rules say how concurrent tasks
share files and declare what blocks them, and name no version control system: see
`.agents/tasks/AGENTS.md`.
