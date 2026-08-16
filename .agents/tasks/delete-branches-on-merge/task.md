# Delete branches on merge

## Status

active

## Objective

State that merging deletes the branch, so "short-lived" holds now that agents merge.

## Why

`0001` chose short-lived branches. Nothing said when one stops existing, and it did not matter
while a human merged through the forge, where deleting is offered by default.

`0019` moved merging to agents, and the first agent-merged pull request left its branch behind.
The rule change removed the habit that had been quietly enforcing the decision.

## Scope

- Root `AGENTS.md` — the change workflow step.
- The stale `feat/add-init-skill` branch on the remote.

## Out of scope

- A decision record. `0001` already decides short-lived branches; this states how that is
  carried out, as `AGENTS.md` states `git commit -s` for the sign-off `0003` decides.
- Branch protection or any forge setting that would enforce it.

## Acceptance

1. The workflow step says the branch is deleted when the pull request is merged.
2. No stale branch remains on the remote.

## Problems

### A rule was being upheld by a habit nobody had written down

`0001` says branches are short-lived. Nothing said they are deleted when merged, and for
thirteen pull requests it did not need to: a human merged each one through a forge that offers
deletion as a default, so the decision held without being stated.
Assumed: a decision that has never been violated is being followed.
Actually: it was being followed by a mechanism outside the repository. `0019` moved merging to
an agent running a command with no such default, and the branch survived its first merge.
The class is broader than branches — a rule can be upheld by tooling, habit, or a person's
routine, and none of that is visible in the repository. Changing who does the work removes the
support without touching the rule, and nothing registers that the rule is now unsupported.

### The finding arrived after its task was archived, for the third time

This was found while reviewing the merge of `add-init-skill`, which was already archived and
merged. `OPEN-QUESTIONS.md` records that findings arriving after archival have nowhere to go,
noting it had twice reached the next task only because a person carried it there.
This is the third, and it landed here only because the fix itself needed a task. Had the
instruction been correct and the observation merely interesting, it would have had nowhere to
sit.
