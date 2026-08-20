---
status: active
objective: >-
  Make each task package directly discoverable and machine-readable without a duplicated index by
  putting canonical status and objective metadata in strict frontmatter.
---

# Replace the task index with canonical frontmatter

## Why

`INDEX.md` repeats data already owned by each task and becomes a shared write hotspot. Agents need
structured task metadata now; a supported human CLI can be designed later. One canonical task
format is simpler than a transition parser because context-fold has no external installations to
preserve.

## Scope

- The managed task rules and their `ctxfold-init` template: task discovery, metadata, lifecycle,
  finishing, final checks, and conflict guidance.
- Every existing `.agents/tasks/**/task.md`: mechanical metadata migration only for accepted
  archives; this task's package may change normally while it is active.
- `skills/ctxfold-init/` and its installed copy: adoption instructions, task-zero creation,
  templates, and validation-facing behavior.
- Root project rules, methodology documentation, convention tests, and a new decision record.
- After PR #39 resolves: `.agents/tasks/INDEX.md`, the decision table in `decisions/README.md`,
  and `OPEN-QUESTIONS.md` section `### Task lifecycle and coordination`.

## Out of scope

- The project suffix after `agent-layer:end` in `.agents/tasks/AGENTS.md`; PR #39 owns it and this
  task preserves it during managed-block replacement.
- Before PR #39 resolves: `.agents/tasks/INDEX.md`, the decision table, and the named
  `OPEN-QUESTIONS.md` section. PR #39 owns those shared sections until integration.
- The body and supporting files of PR #39's handoff task, apart from the eventual mechanical
  frontmatter migration of its `task.md`.
- An agent task-query skill, `list_tasks.py`, or any supported human CLI.
- Compatibility behavior for installations outside this repository.

## Acceptance

1. Every task uses the exact new frontmatter schema; no task uses `## Status` or `## Objective`,
   and convention checks reject legacy or malformed metadata.
2. Migration evidence proves that each pre-migration task kept its status, normalized objective,
   title, and remaining body, and that every other file in accepted archives is byte-identical.
3. Task discovery and lifecycle rules read task packages directly; no task index or index template
   remains after integration.
4. Fresh adoption creates task zero in the new format and no index; repeat adoption preserves
   project suffixes, task state, and unrelated `.agents/` content.
5. The complete source skill is reinstalled, the installed skill updates the managed blocks, and
   every managed block and installed skill file has the required parity.
6. A decision records the replacement and the v0 archive-migration exception; affected accepted
   decisions are narrowed only through their Status fields.
7. PR #39's additions survive the final rebase unchanged except for its task's mechanical metadata
   migration, and all checks pass on the integrated head.

## Approval

Human.

## Problems

### The implementation base does not yet contain the concurrent handoff task

The task starts from `main` at `d7e4bd4` while PR #39 is still moving. Work that does not overlap
can proceed, but final corpus migration, index deletion, decision-table editing, and the adjacent
open-question edit wait for the PR to merge or close. The integration base will be recorded in
`context.md` after that disposition.

### Metadata sections are not always adjacent

The first migration pass assumed every task began with Status immediately followed by Objective.
`2026-08-18-2053-make-the-layer-file-an-entry-point` has `## Blocked by` between them, so the pass
stopped after rewriting the earlier files. Git still held every accepted original and no other
archive file changed. The migration now locates the two metadata sections independently and treats
everything else, including section order, as retained authored content.

### Markdown discovery treated deleted files as visible

Deleting the two index templates left their paths in `git ls-files --cached` until staging. The
Markdown helper returned those paths as repository documents and the link test crashed while
opening files that no longer existed. Discovery now keeps Git's tracked-and-untracked boundary but
filters it to files present in the working tree, so deletion changes are testable before staging.
