# Context — let-agents-merge-after-approval

## Base state

`main` is at `4c225d2`. Nineteen decision records, thirteen archived tasks, CI green.

Every task so far ended the same way: the agent archived and pushed, a human approved, and a
human ran the merge.

## References

- `decisions/0001-use-github-flow.md` — "Agents may open and update pull requests; merging is a
  human action." The sentence this narrows.
- `decisions/0007-archive-before-merge.md` — approval authorizes archival, and archival precedes
  merge. Unchanged, and the reason the gap below exists.
- `decisions/0016-check-conventions-in-ci.md` — what CI verifies, which is what covers the
  archival commit once nobody reviews it.

## Assumptions

- Approval is given on a pull request whose work is complete, with only archival outstanding.
  That has been true for every task; nothing enforces it.
- The archival commit is mechanical. Its only written content is the Outcome, which restates work
  the approver already reviewed.

## Context conflicts

`OPEN-QUESTIONS.md` records that approval and merge-readiness are different states with nothing
bridging them, and that a reviewer merging on approval would ship an unarchived task. This makes
the agent responsible for that bridge rather than the reviewer, which resolves the hazard in one
direction and creates a smaller one in the other.

## Open questions

Whether approval should move to after archival, so the approver sees the state that merges. That
would contradict `0007`, which says approval authorizes archival, and is a larger change than
this task.
