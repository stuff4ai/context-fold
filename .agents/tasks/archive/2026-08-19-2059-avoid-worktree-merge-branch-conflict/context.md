# Context — avoid-worktree-merge-branch-conflict

## Base state

`.agents/worktrees/AGENTS.md` describes the worktree lifecycle: `git worktree add
.agents/worktrees/{task-slug}` to start, `git worktree remove` "when the task has been accepted."
It says nothing about how to merge a pull request whose branch is checked out in that worktree,
or about the conflict that causes.

## References

- `.agents/worktrees/AGENTS.md` — the file this task extends.
- `gh pr merge --help` — `--delete-branch` "Delete the local and remote branch after merge";
  its local half checks out the base branch and deletes the head branch in the current checkout.

## Not relevant

The GitHub-side merge itself (squash, PR description as commit message, CI-before-merge) is
unaffected and already documented in the root `AGENTS.md`'s `## Change workflow`. This task only
covers the worktree-specific ordering problem.
