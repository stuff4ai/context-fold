# Avoid the worktree/merge branch-conflict on delete-branch merges

## Status

completed

## Objective

Document, in `.agents/worktrees/AGENTS.md`, a merge sequence that does not conflict with a task
worktree still holding the branch being merged.

## Why

Merging `feat/guard-against-leftover-scaffolding` via `gh pr merge --delete-branch`, run from
inside that PR's own task worktree, failed: `gh`'s local cleanup step tries to check out `main` in
the worktree it ran from, but `main` was already checked out in the repository's root worktree, so
Git refused ("'main' is already used by worktree at ..."). The PR still merged on GitHub — `gh pr
merge`'s API call happens before its local cleanup — but the local and remote branch deletion had
to be redone by hand: `git push origin --delete`, `git worktree remove`, `git branch -D`.

`main` is always checked out at the repository root under this project's worktree convention, so
any future merge run with `--delete-branch` from inside a task worktree hits the same conflict.

## Scope

- `.agents/worktrees/AGENTS.md` — add the merge sequence next to the existing `git worktree
  remove` note in `## Lifecycle`.

## Out of scope

- Automating or scripting the sequence. This is a documentation fix, not tooling.
- Changing `gh`'s behavior or filing anything against it.

## Acceptance

1. `.agents/worktrees/AGENTS.md` says not to rely on `gh pr merge --delete-branch`'s local cleanup
   from inside a task worktree, and states the sequence that avoids the conflict: merge without
   `--delete-branch`, then `git worktree remove` the task worktree, then delete the local and
   remote branch.

## Problems

## Outcome

Added a paragraph to `.agents/worktrees/AGENTS.md`'s `## Lifecycle` section stating the merge
sequence that avoids the conflict: `gh pr merge <N> --squash` (no `--delete-branch`), then `git
worktree remove`, then `git branch -D` and `git push origin --delete` for the branch. The shipped
template at `skills/ctxfold-init/templates/worktrees/AGENTS.md` was left unchanged — it is a
one-time seed for adopters, not required to stay in sync with this repository's own copy (unlike
`templates/agents/`, nothing checks the two match).

`pytest` (304 passed) and `pymarkdownlnt --config .pymarkdown.json scan -r --respect-gitignore .`
both pass at this state, run exactly as `.github/workflows/ci.yml` runs them.