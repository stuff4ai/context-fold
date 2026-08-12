# Record the merge strategy

## Status

completed

## Objective

Record how pull requests are merged, and the convention that follows from it for writing pull
request descriptions.

## Why

The repository is configured for squash merging with the pull request description as the
commit body, but nothing records that choice or why. The first merge already showed the
convention it implies is not obvious: PR #1 landed on `main` with a "Before merge" section
stating the task was still active, which was true for reviewers and false the moment it
merged.

## Scope

- `decisions/0008-squash-merge-pull-requests.md`.
- `decisions/README.md` index row.
- Root `AGENTS.md` change workflow.

## Out of scope

- Commit signing, still undecided under `0003`.
- Branch protection and required checks.
- Any change to the archive or task model.

## Acceptance

1. The merge strategy, the squash message source, and the pull request description convention
   are recorded in one decision record.
2. Root `AGENTS.md` states the convention operationally, without restating the reasoning.
3. The index row is added and the record is linked.
4. Nothing in the record contradicts `0001`, `0002`, `0003`, `0004`, or `0007`.

## Outcome

The merge strategy is recorded in `decisions/0008-squash-merge-pull-requests.md`: squash
merging, the pull request description as commit body, and the convention that descriptions are
written as the permanent record rather than as notes to the reviewer. Root `AGENTS.md` states
the convention operationally; `decisions/README.md` carries the index row.

All four acceptance criteria satisfied.

The `0003` ambiguity that squashing exposes — whether "every commit" means every commit or
every commit that lands on `main` — is left open in `context.md`. Resolving it requires a
record superseding `0003`, which is out of this task's scope.

Nothing was left to fold.

## Problems

### A finding arrived after its task was archived

The pull request description defect was discovered by inspecting `main` after PR #1 merged,
by which point `2026-08-13-bootstrap-tasks-layer` was archived and immutable.
Assumed: findings arrive while the task that produces them is open.
Actually: merging is the last stage, so anything learned from it necessarily arrives after
archival. `archive/AGENTS.md` says recurring problems across archived tasks are the signal to
change something, but nothing says where a post-merge finding is recorded when its own task is
closed. It landed here only because a person remembered it across the gap.
