---
status: completed
objective: >-
  Add a Claude Code adapter so a session started in this repository has `AGENTS.md`'s content
  without being told to read it.
---

# Support Claude Code reading AGENTS.md

## Why

Claude Code auto-loads only `CLAUDE.md` files — a global one and a project-level one, if either
exists — into a session's context at start. It has no built-in awareness of `AGENTS.md`, which is
this project's own convention, not something Claude Code's tooling treats specially.

This surfaced concretely while working the task that removed `templates/task/`
(`decisions/0029-drop-the-task-template.md`, once merged). The agent read `.agents/tasks/AGENTS.md`
and whatever the task itself pointed at, executed the task, and opened a pull request — and read
the root `AGENTS.md` only after being asked directly why it hadn't. By then it had already missed
two rules stated only there: sign every commit, and name branches `<type>/<kebab-case-topic>`.
Both needed fixing after the fact, on a change already pushed.

`decisions/0011-keep-the-model-vendor-neutral.md` already anticipates this. The canonical rules
"name no product, assume no particular tool's directory layout," and integration with a specific
product, if it happens, is an adapter over the canonical model — never the source of truth. A
`CLAUDE.md` that references `AGENTS.md`, rather than restating it, is that adapter.

## Scope

- A root `CLAUDE.md` that loads `AGENTS.md`'s content into a Claude Code session automatically.
- Confirming the actual mechanism Claude Code uses for this (an `@path` import, as suggested when
  this task was opened, or whatever loading a fresh session shows actually happens) before
  relying on it.

## Out of scope

- Adapters for other products — Cursor, Copilot, JetBrains tooling, etc. A separate task if
  wanted.
- Shipping this adapter as part of the context-fold distribution (`skills/ctxfold-init/`) for
  other adopters. This task is scoped to this repository's own use; whether the distribution
  should offer the same adapter to adopters using Claude Code is a separate, open question.
- Changing `AGENTS.md`, `.agents/AGENTS.md`, or any portable rule file to accommodate this.

## Acceptance

1. `CLAUDE.md` exists at the repository root and its content is a reference to `AGENTS.md`, not a
   copy of it — nothing in it needs updating when `AGENTS.md` changes.
2. A fresh Claude Code session started in this repository has `AGENTS.md`'s content in context at
   the start of the session, without being told to read it — verified by starting one, not
   assumed from how the mechanism is documented.
3. No portable rule file (`.agents/AGENTS.md`, `.agents/tasks/AGENTS.md`,
   `.agents/tasks/archive/AGENTS.md`) names Claude Code or assumes its layout —
   `decisions/0011-keep-the-model-vendor-neutral.md` still holds.

## Problems

The Markdown linter (`pymarkdown`, `MD041`) rejected `CLAUDE.md` with only `@AGENTS.md` on its
first line — every tracked document needs a top-level heading. Added `# CLAUDE.md` above the
import and re-ran the verification session to confirm the import still resolves with a heading
preceding it, rather than assuming a one-line change to a file the linter had just flagged was
safe.

## Outcome

`CLAUDE.md` added at the repository root: a heading plus `@AGENTS.md`, Claude Code's own import
syntax. Verified with two fresh, tool-less `claude -p` sessions in this repository — each denied
every tool so an answer could only come from context already loaded at session start — that
correctly answered questions about branch naming and commit sign-off from `AGENTS.md` and named
the source as "the AGENTS.md content shown at session start." Recorded in
`decisions/0030-add-a-claude-code-adapter.md`.

No portable rule file changed; `decisions/0011-keep-the-model-vendor-neutral.md` holds.

Acceptance:

1. Satisfied — `CLAUDE.md` is a one-line pointer, not a copy.
2. Satisfied — verified empirically, twice, not assumed.
3. Satisfied — `.agents/AGENTS.md`, `.agents/tasks/AGENTS.md`, and
   `.agents/tasks/archive/AGENTS.md` are unchanged.
