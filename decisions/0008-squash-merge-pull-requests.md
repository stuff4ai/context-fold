# Squash merge pull requests

## Status

Accepted

## Context

A pull request in this repository is one task ([0007](0007-archive-before-merge.md)), and
carries both the work and the archived record of the work. How it lands on `main` decides what
the project's history looks like.

Preserving every branch commit puts working steps — corrections, review responses, renames —
onto `main`, which obscures the task-level view that the task model exists to provide.
Replaying commits without a merge point loses the grouping entirely and rewrites their
identity, which would invalidate signatures if commits are ever signed.

Squashing produces one commit per task, but discards the branch commits, so whatever the
squashed message contains is the only surviving description of the change.

## Decision

Pull requests are squash merged. Merge commits and rebase merging are disabled, so there is
one way for a change to reach `main`.

The squashed commit message is the pull request title and description. The title supplies the
subject and follows [Conventional Commits](0002-use-conventional-commits.md); the description
supplies the body.

Because the description becomes the permanent commit message, it is written as a record of the
change, not as a note to the reviewer. It describes what the change does and why in terms that
stay true after merge. It does not contain sections about what will happen on approval, what
remains to be done before merging, or anything else that is only true while the pull request
is open. Discussion aimed at reviewers belongs in comments, which are not merged.

Branch commits are working state. They still follow the commit conventions, but they are
discarded on merge and are not the historical record.

## Consequences

`main` reads as a list of completed tasks, one commit each, with the reasoning in the body and
the archived task package in the same commit.

Work in progress can be committed freely without polluting the history.

The pull request description carries more weight than usual and must be revised before merge
if the change evolved during review — a description written early and left alone will land
stale.

Rich formatting degrades. Tables and long lines wrap poorly as a commit body, so descriptions
should stay close to plain prose and short lists.

Branch commits are lost, including their individual `Signed-off-by` and `Co-authored-by`
trailers. Those trailers must be present on the squashed commit; whether the forge carries
them across automatically is a property of the forge and should be checked rather than
assumed.

The strategy depends on repository settings that any administrator can change, and nothing in
the repository enforces it.
