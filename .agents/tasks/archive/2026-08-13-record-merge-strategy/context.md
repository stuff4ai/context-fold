# Context — record-merge-strategy

## Base state

`main` is at `cd18080`, the squashed merge of PR #1. It is the only merge this repository has
performed, and the only evidence available about how the strategy behaves.

Observed on that commit:

- The squashed message is the pull request title and description.
- `Signed-off-by` and `Co-authored-by` both survived, appended after a separator. Whether the
  forge collected them from the branch commits or they were added at merge time is not known
  from the result alone.
- Markdown tables in the description wrapped badly as a commit body.
- The description's "Before merge" section became a permanent statement that the task was
  still active.

## References

- `decisions/0001-use-github-flow.md` — branches, pull requests, review before merge.
- `decisions/0002-use-conventional-commits.md` — why the pull request title must be
  conventional if it becomes the commit subject.
- `decisions/0003-sign-off-commits.md` — sign-off, and commit signing left undecided.
- `decisions/0007-archive-before-merge.md` — the merge commit carries the work and its record.

## Assumptions

- One task maps to one pull request maps to one commit on `main`. This holds for the only
  merge so far.
- Trailer survival is a property of the forge, not of this project, and may change.

## Open questions

- Does `0003` mean every commit, or every commit that lands on `main`? Squashing makes the
  distinction real: branch commits are discarded, so only the squashed one can carry the
  assertion. Not resolved here; the record states what happens without reinterpreting `0003`.
- Should branch protection enforce the strategy rather than relying on repository settings
  that any admin can change?
