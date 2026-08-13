# Use GitHub Flow

## Status

Accepted. Merging as a human-only action is narrowed by
[0019](0019-agents-may-merge-after-approval.md); the rest stands.

## Context

The project needs a branching model that humans and agents can both follow without
coordination overhead.

Long-lived branches accumulate conflicts and delay review. Committing directly to `main`
removes the approval point that other decisions in this project depend on — archiving a task
before merge assumes there is a merge, and a review that authorizes it.

Agents also need an unambiguous rule about what they may do unattended. "Open a pull request
and stop" is checkable; "use good judgment about merging" is not.

## Decision

We will use GitHub Flow: short-lived branches cut from `main`, one focused change each,
merged through a pull request after human review.

Branches are named `<type>/<kebab-case-topic>`, where `<type>` is drawn from the same set of
types used in commit messages — `feat/task-index`, `docs/decision-threshold`, `fix/index-drift`.

`main` is always releasable and is never pushed to directly. Agents may open and update pull
requests; merging is a human action.

## Consequences

Every change has a review point, which the task lifecycle relies on for approval before
archival.

Branch names describe their contents, and sorting them groups related work by type.

The model assumes a hosted pull request workflow. A project using a different forge or a
patch-based workflow would need a different record.

Small changes carry the cost of a branch and a pull request. That cost is accepted in exchange
for a uniform rule that does not require judging which changes are small enough to skip it.
