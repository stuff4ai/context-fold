# Context — delete-branches-on-merge

## Base state

`main` is at `cf806ab`, with `feat/add-init-skill` left on the remote after the first pull
request an agent merged. Every earlier branch is gone, deleted by the human who merged it.

## References

- `decisions/0001-use-github-flow.md` — chooses short-lived branches, and says nothing about
  when one ends.
- `decisions/0019-agents-may-merge-after-approval.md` — moved merging to agents, which is when
  the branches started surviving.
- `decisions/0008-squash-merge-pull-requests.md` — how merging happens; deletion is the step
  after it.
- `AGENTS.md` — the change workflow this task edits.

## Assumptions

- Deleting the branch loses nothing. The work is on `main` as a squashed commit, and the
  pull request keeps its own record.

## Open questions

None.
