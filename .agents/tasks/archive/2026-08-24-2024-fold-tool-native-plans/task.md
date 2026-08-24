---
status: active
objective: >-
  Ensure a coding agent's own tool-native planning output — a plan-mode
  scratch file, an ephemeral step tracker, or similar — is folded into the
  task package's rfc.md or plan.md before implementation begins, instead of
  staying only in a tool-local place a later session or a different tool
  cannot read.
---

# Fold tool-native plans into the task package

## Why

A user asked why Claude Code's Plan Mode writes its scratch plan to `~/.claude/plans/` — a path
the harness controls, global and per-user, outside any repository — and how to get plans an
agent's own tool produces stored in this repository instead, using the existing
`.agents/tasks/{slug}/rfc.md`/`plan.md` convention.

`.agents/tasks/AGENTS.md` already fully describes `rfc.md` (direction discussion) and `plan.md`
(execution strategy) — see `decisions/0033`. It says nothing about output a tool produced on its
own, so a plan approved in a tool-native planning phase can vanish: never folded into either
file, lost to a later session or a different tool.

Since the tool-side write path can't be changed, the fix is a portable rule: fold whatever is
worth keeping into `rfc.md`/`plan.md` before implementation begins. It names no product, so it
needs no repository-scoped adapter (unlike `decisions/0030`/`0034`) — every tool that already
reads `AGENTS.md`, including Claude Code (through `decisions/0030`'s import) and Codex (which
reads `AGENTS.md` natively), gets it automatically.

## Scope

- `skills/ctxfold-init/templates/agents/tasks/AGENTS.md` — one new paragraph after the `rfc.md`
  and `plan.md` descriptions.
- Reinstalling `.agents/skills/ctxfold-init/` from that template and regenerating
  `.agents/tasks/AGENTS.md`'s managed block, preserving its project-owned suffix.
- A new decision record for this convention.

## Out of scope

- A product-specific adapter for Claude Code, Codex, or any other tool — the rule is vendor-
  neutral by design, per `decisions/0011`, and needs none.
- Changing `rfc.md`/`plan.md`'s frontmatter, structure, or lifecycle — `decisions/0033`'s rules
  stand; this only adds one more source for what ends up in those files.

## Acceptance

1. `skills/ctxfold-init/templates/agents/tasks/AGENTS.md` states that a tool-native planning
   phase's output is a draft, to be folded into `rfc.md` or `plan.md` before implementation
   begins — naming no product, directory, or tool convention.
2. `.agents/skills/ctxfold-init/` is a byte-for-byte reinstall of `skills/ctxfold-init/`.
3. Every one of the five portable managed blocks under `.agents/` matches its template
   byte-for-byte, verified by diff rather than assumed, with every project-owned suffix
   preserved unchanged.
4. `decisions/0043-fold-tool-native-planning-into-the-task-package.md` exists with `## Status`
   `Accepted`, and `decisions/README.md`'s index row for it shows the same status.
5. `tests/test_conventions.py` passes.

## Problems

- Drafted the decision record as `0043` after confirming `0042` had already landed on `main`
  from a concurrent branch (`feat: guard decision merge readiness`, #49) while this task's plan
  was being written — exactly the provisional-numbering case `AGENTS.md`'s Decisions section
  describes. No rework needed beyond picking the next free number.
- On the first attempt, `decisions/0043-*.md` was written to the main checkout
  (`/home/alexengrig/GitHub/stuff4ai/context-fold/decisions/`) instead of this task's worktree,
  because the file-write tool takes an absolute path independent of the shell's current
  directory. Caught immediately via `git status` in both trees and moved into the worktree
  before anything else touched it; no commit was made from the main checkout. Worth remembering
  when working from a worktree: an absolute path handed to a non-shell tool does not follow the
  shell's `cd`.
