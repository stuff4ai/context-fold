---
status: completed
objective: >-
  Prevent proposed or inconsistently indexed decision records from reaching a merge-ready state.
---

# Guard decision merge readiness

## Why

Decision 0041 merged as `Proposed` even though its task was complete, reviewed, and approved. The
record and index agreed with each other, so an index-parity check alone would not have caught it.
The correction needed a second pull request after acceptance.

## Scope

- Record the merge-ready status rule in a new decision and the root project instructions.
- Extend `tests/test_conventions.py` to reject `Proposed` records and validate recognized decision
  statuses plus semantic agreement with the decision index.
- Correct the existing decision 0009 index-status mismatch exposed by that check.
- Update the decision template only as needed to make drafting versus merge readiness unambiguous.

## Out of scope

- Portable agent-layer rules or `ctxfold-init` templates.
- GitHub-specific approval, merge-queue, or branch-protection automation.
- Changing accepted decision content outside mutable Status fields and the derived decision index.
- Generalizing task approval or exact-head verification beyond decision-record readiness.

## Acceptance

1. Durable project guidance distinguishes a branch proposal from a record's post-merge Status and
   requires decision-bearing changes to be merge-ready before review.
2. Convention tests reject `Proposed` decision records, malformed status shapes, and record/index
   status disagreement, including a mismatched supersession target.
3. Accepted status prose may retain narrowing notes, and superseded records retain their target.
4. Decision 0009 and its index row agree without changing the accepted record outside Status.
5. Full tests, Markdown lint, and `git diff --check` pass.

## Outcome

Decision 0042 and the root project instructions now distinguish Git proposal state from the
post-merge state written in a decision record. The drafting template starts at `Proposed`, while
the convention suite rejects that state from actual merge-ready records and accepts explanatory
notes on `Accepted` statuses.

Decision status parsing also validates supersession link shapes and targets. The derived decision
index is compared semantically with every record, and its existing 0009 row now names the same
0037 supersession target as the record. Full tests, Markdown lint, and `git diff --check` pass.

## Problems

- The proposed index-parity guard immediately exposed older drift: decision 0009 says
  `Superseded by 0037`, while its index row still says `Accepted`. The task therefore includes
  reconciling that derived row and testing supersession targets, not only state names.

## Approval

Human.
