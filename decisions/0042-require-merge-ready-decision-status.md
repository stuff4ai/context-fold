# Require merge-ready decision status

## Status

Accepted

## Context

[0000](0000-use-decision-records.md) says a record on a branch is a proposal and becomes project
truth when it merges. It did not distinguish that Git state from the record's own Status field.
Decision 0041 therefore reached review, approval, and merge while both its record and index still
said `Proposed`; correcting the accepted state required a second pull request.

The index can drift independently too. Decision 0009 says it is superseded by 0037, while its
index row continued to say `Accepted`. Existing checks require every record to be listed but do
not compare their statuses.

## Decision

A branch makes an unmerged decision record a proposal. The record's `## Status` instead describes
the state that would become project truth if the branch merged. A new record begins as `Proposed`
while it is being drafted and changes to `Accepted` during outcome folding, before its task is
archived and the final state is submitted for review. Approval covers that merge-ready status;
nothing changes it between approval and merge.

An actual decision record has one of these semantic states:

- `Proposed`, exactly, as a temporary drafting state;
- `Accepted`, optionally followed by prose recording later narrowings;
- `Superseded by [NNNN](NNNN-slug.md)`, with matching target number and filename.

The decision index mirrors each record's semantic state. An accepted record's explanatory
narrowing prose stays in the record while its index cell says `Accepted`. A superseded index cell
names the same target as the record. `Proposed` is never merge-ready in either place.

Convention checks parse those shapes, reject every actual `Proposed` record, and compare every
record with its index row, including a supersession target. The hidden decision template keeps
`Proposed` as its drafting default, so the check intentionally remains red until a copied record
is ready for archival and review.

This clarifies [0000](0000-use-decision-records.md), extends the structural checks in
[0016](0016-check-conventions-in-ci.md), and applies [0023](0023-approve-the-final-state.md)'s
final-state approval rule to decision statuses.

## Consequences

A stale proposed status or a divergent index blocks the same pull request that introduced it,
instead of requiring a corrective pull request after merge. Drafting a new decision temporarily
makes the full convention suite fail; changing it to `Accepted` is an explicit readiness step,
not a claim that the unmerged branch is already project truth.

The check verifies status structure and agreement, not whether the decision should be accepted.
Human or verifier review still supplies the approval required by the task and project workflow.
