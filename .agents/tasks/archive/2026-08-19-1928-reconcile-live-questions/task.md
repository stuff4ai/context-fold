# Reconcile live project questions

## Status

completed

## Objective

Correct the README and live open-question list where accepted decisions and shipped work have
made their descriptions stale.

## Why

The project now ships `ctxfold-init`, distinguishes the layer from the shared `.agents/`
directory, and has exercised adoption in existing repositories. The front door and live question
list still describe parts of that accepted state as absent or undecided, which makes current
documentation contradict the records it points to.

## Scope

- `README.md` — the layer boundary, deletion test, adoption, and current status.
- `OPEN-QUESTIONS.md` — settled portions of deferred capabilities, model questions, and gaps.
- `.agents/tasks/INDEX.md` — the derived row for this task.

## Approval

Verifier

## Out of scope

- Making a new methodology decision or resolving a question that accepted work has not settled.
- Portable rules, decision records, tests, tooling, or the `ctxfold-init` implementation.
- Rewording unrelated live questions.

## Acceptance

1. `README.md` distinguishes the agent layer from the shared `.agents/` directory, scopes the
   deletion test to layer-owned files, and says that `ctxfold-init` automates adoption while
   ordinary task lifecycle and learning remain manual.
2. `OPEN-QUESTIONS.md` removes or narrows statements settled by accepted decisions while keeping
   the genuinely unresolved lifecycle, customization, provenance, discovery, upgrade, and
   heterogeneous-host questions visible.
3. Both documents agree with the accepted decisions they summarize and introduce no new
   methodology decision.
4. The existing `pytest` suite and recursive Markdown scan pass, targeted stale-claim searches
   find no obsolete statement, and `git diff --check` passes.

## Outcome

`README.md` now distinguishes the layer from its shared directory, scopes the deletion test to
layer-owned files, and separates automated adoption from the manual task and learning lifecycle.
`OPEN-QUESTIONS.md` now removes settled absence claims and states the remaining lifecycle,
customization, versioning, provenance, discovery, upgrade, heterogeneous-host, and Outcome-order
questions against the accepted project state. No decision, portable rule, test, or tool changed.

## Problems

- Fetching `main` and the deleted PR source branch in one command failed after PR #27 merged.
  The assumption was that the remote branch would remain; GitHub had already deleted it. Fetched
  `main` and the retained pull-request head ref separately.
- A zsh loop used `path` as its item variable, which is tied to `PATH` in zsh and made `git`
  unavailable inside the loop. Its path-mismatch output was invalid; rerunning with `filepath`
  verified all PR-touched paths with no mismatches.
- The first package patch assumed a shortened objective for the concurrent task's index row and
  did not apply. Reading the worktree's actual derived index supplied the exact insertion point;
  no partial files had been created.
- The branch push succeeded, but GitHub's API timed out during PR creation and during both
  GraphQL and REST existence checks. No blind creation retry was made while a duplicate could
  not be ruled out; a later REST check confirmed none existed and allowed one safe retry.
- The first verifier found that the `## Outcome` count was taken before this task joined the
  archive: the live question said twenty-three of twenty-five instead of twenty-four of
  twenty-six. Updated the current evidence and invalidated the old head's CI and verifier gates.
