# Plan — add-ctxfold-tasks-skill

Executes the resolved direction in `rfc.md`. Tactical steps below may still change; the
direction (output shape, view-only filtering, Python helper) does not.

## Steps

1. Branch `feat/add-ctxfold-tasks-skill` from `main`.
2. Write `skills/ctxfold-tasks/SKILL.md`: agent-only frontmatter (name, description with an
   explicit trigger, no human-facing invocation wording), modeled on
   `skills/ctxfold-init/SKILL.md`'s structure but scoped to this skill's own contract.
3. Write the bundled private helper (Python, stdlib-only) under `skills/ctxfold-tasks/`:
   - Locate the repository root and `.agents/tasks/`.
   - Enumerate direct children of `.agents/tasks/` other than `archive/` as unfinished packages;
     enumerate `.agents/tasks/archive/*` as archived packages.
   - Enumerate `.agents/worktrees/*` as registered checkouts; for each, repeat discovery against
     that checkout's own `.agents/tasks/`. A missing, non-Git, or unreadable worktree directory
     becomes a diagnostic entry, not a fatal error.
   - Decode `status`/`objective` frontmatter using the same contract
     `tests/test_conventions.py::task_metadata` already enforces (strict two-key LF frontmatter,
     folded objective). A package that fails to decode becomes a diagnostic entry naming its path
     and the problem, and is excluded from `tasks`.
   - Group decoded observations by slug. Select one status per slug by precedence
     `planned < active < completed/cancelled`; break a terminal-status tie by the later
     archive-directory timestamp and record the tie in a diagnostic. Differing task content at
     the same highest-status observation is kept as a conflict: all sources appear in the entry,
     flagged, rather than one being dropped.
   - Filter by the requested view (`unfinished` default, `archive`, `all`) and emit
     `{"tasks": [...], "diagnostics": [...]}`. Exit `0` whenever the query ran, even with
     diagnostics; non-zero only when the query could not run at all (not inside a context-fold
     repository).
4. Install the skill into `.agents/skills/ctxfold-tasks/`, matching the copy-then-verify
   discipline `skills/ctxfold-init/SKILL.md` documents for its own installation, so
   `test_installed_skill_matches_the_shipped_one` passes.
5. Add tests exercising: unfinished/archive/all views; worktree registration including a missing
   worktree; a malformed package surfaced as a diagnostic and excluded from `tasks`; a same-status
   slug conflict surfaced rather than dropped; a terminal-status tie broken by archive timestamp.
   Extend `tests/test_conventions.py` or add a sibling test module, whichever keeps the existing
   file's scope coherent.
6. Add a decision record (next number after `0037`) stating the skill's discovery scope, slug
   identity and status-precedence rule, conflict/diagnostic handling, and JSON contract — mirroring
   `decisions/0037-replace-task-index-with-frontmatter.md`'s level of specificity — and add its row
   to `decisions/README.md`.
7. Update `.agents/tasks/AGENTS.md` (portable rules and installed copy) only if discovery guidance
   there needs to name the new skill; otherwise leave it alone per this task's Out of scope.
8. Run the full convention suite (`pytest tests/`), fix findings, then write this task's Outcome,
   fold any durable decision reference into the project layer, and archive per
   `.agents/tasks/AGENTS.md`'s finishing rules.

## Out of scope (restated from task.md)

No human-facing CLI, no mutating lifecycle operations, no `INDEX.md` revival, no copying task
contents into a second store.
