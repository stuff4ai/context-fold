# Agents may merge after approval

## Status

Accepted. What approval authorizes is narrowed by
[0023](0023-approve-the-final-state.md) to the merge alone, since folding, archival and
the final check now precede it. That an agent may merge stands.

## Context

[0001](0001-use-github-flow.md) reserves merging for a person: agents open and update pull
requests, a human merges. The reason was that merging is where work becomes `main`, and a human
should decide that.

Approval already is that decision. What the rule adds is a second action after it, and in
thirteen tasks that action has never changed an outcome — every merge followed an approval
already given, separated only by the archival the agent performs in between.

The cost is not the keystroke. It is that the end of every task takes three exchanges instead of
one, and the middle one exists because the agent must stop, hand back, and wait to be told to
finish something already authorized.

There is a real objection. [0007](0007-archive-before-merge.md) puts approval before archival:
review, approve, fold, archive, merge. So the commit that merges is not the commit that was
approved — archival happens after. Today the human's merge is an implicit second look at that
commit. Removing it means the archival commit reaches `main` without anyone having seen it.

## Decision

An agent may merge a pull request once a human has approved it.

Approval authorizes everything downstream: folding outcomes, archiving the task, the final
exact-head check, and the merge itself. An agent that has not been approved does not merge, and
pushing to `main` directly remains forbidden regardless.

Nothing else about the workflow changes. `0007` still requires archival before merge, and
[0008](0008-squash-merge-pull-requests.md) still governs how.

This narrows `0001`, whose other provisions stand.

## Consequences

A task ends when it is finished rather than when someone is available to type a command.

The archival commit merges unreviewed. CI covers its mechanical content — that the index matches
the directories, that the task carries a final `Status` and an `Outcome`, that the installed rule
files still match the distribution, that links resolve. That is most of what archival is.

It does not cover the Outcome prose, which is the one thing in that commit a person writes. An
Outcome that is wrong, overstated, or omits what was not done will merge, and the only reader
who would have caught it is the approver who no longer looks.

The approver's window narrows correspondingly. Approval now covers work they have seen plus a
step they have not, and the distinction is easy to lose sight of precisely because the step is
routine.

Reverting is cheap — the rule is one sentence — but a merge is not, and the asymmetry is the
point of the objection above.
