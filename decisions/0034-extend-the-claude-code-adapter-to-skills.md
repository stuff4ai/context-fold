# Extend the Claude Code adapter to skills

## Status

Accepted

## Context

Claude Code discovers skills only under `.claude/skills/` — its own convention for where a
project makes reusable procedures available to it. It has no awareness of `.agents/skills/`,
this project's own convention (`decisions/0026-map-what-is-under-the-agents-directory.md`) for
where an installed tool's skills live.

This repository already carries `.agents/skills/ctxfold-init/` — `SKILL.md`, `ADOPTING.md`,
`templates/`, all tracked in Git — the installed copy of this project's own init skill, landed
there the same way `0026` describes any tool's skill landing: "not the layer's ... answers to
whatever put it there." A Claude Code session in this repository could not use it. There was no
`.claude/skills/` directory, so the skill never appeared in an available-skills listing and could
not be invoked by name.

`decisions/0030-add-a-claude-code-adapter.md` already solved the same shape of problem for
`AGENTS.md`: a root `CLAUDE.md` containing `@AGENTS.md`, Claude Code's own import syntax, so a
session has the project's rules from the first turn without being told to read them. That
record established the pattern this one follows — an adapter that is a pointer, not a copy, so
nothing needs to change when the thing it points at does, and scoped to this repository's own
use rather than the distribution.

`decisions/0011-keep-the-model-vendor-neutral.md` permits integration with a specific product
only as an adapter over the neutral canonical model, never as the model's source of truth. A
directory-level symlink is that shape applied to a directory instead of a file:
`.agents/skills/` stays the one real location, and `.claude/skills` becomes a second,
non-authoritative path to it.

`OPEN-QUESTIONS.md` already names the broader shape of this gap as unresolved: "How do agent
capabilities and context reach heterogeneous hosts?" — whether context-fold should implement
client adapters at all, or leave delivery outside the project entirely, is undecided. This
record does not answer that question; it is one concrete, local instance of it, for one tool, in
this repository only, the same way `0030` was.

## Decision

A directory-level symlink is added at `.claude/skills`, pointing at `../.agents/skills`, tracked
in Git so it reproduces in every clone and worktree:

```bash
ln -s ../.agents/skills .claude/skills
git add .claude/skills
```

The target is relative, not absolute, so the link resolves correctly wherever the repository is
cloned or a worktree is checked out.

Verified as a real symlink rather than assumed: `git ls-files -s .claude/skills` reports Git's
symlink mode `120000` with a single entry, and the tracked blob's content is exactly
`../.agents/skills` — confirming Git stored a pointer, not a copy of the skill's files.

Verified empirically, the same way `0030` was, with two fresh `claude -p` sessions, each with
no prior conversation state:

1. Asked to list its available skills without using any tool, a session named `ctxfold-init`
   first among them, with a description matching `.agents/skills/ctxfold-init/SKILL.md`'s own
   frontmatter — confirming the symlink makes the skill discoverable at session start.
2. Asked to invoke `ctxfold-init` and report the exact filesystem paths it read, a session ran
   the skill's own adoption-check procedure end to end (re-copied the four template
   `AGENTS.md` files, confirmed each byte-identical to the installed copies, confirmed
   `.gitignore`'s two required lines, left `.agents/tasks/` and task zero untouched per the
   skill's own instructions) and listed every path it read as
   `.../.claude/skills/ctxfold-init/...` — `SKILL.md`, `ADOPTING.md`, and each file under
   `templates/` — confirming content, not just the skill's name, resolves through the symlink.
   The session's tool calls left the working tree unchanged (`git status` after it exited showed
   only this task's own edits), consistent with its own claim that nothing needed to change.

No content under `.agents/skills/` moves or is duplicated. `.claude/RESUME.md` and
`.claude/scheduled_tasks.lock`, already untracked runtime state noted in `0030`, are unaffected —
this adds exactly one new tracked path.

## Consequences

A Claude Code session in this repository can now use `ctxfold-init` as a skill, the same way it
already gets `AGENTS.md`'s content through `CLAUDE.md` (`0030`) — without an adopter, tool, or
human copying anything into `.claude/` by hand.

Scoped the same way `0030` was: this is this repository's own adapter, not something
`skills/ctxfold-init/templates/` ships or the distribution offers an adopter. An adopter using
Claude Code gets nothing from this decision unless they add the same symlink themselves; whether
the distribution should do that is left open, same as `0030` left the `CLAUDE.md` question open.

`.agents/skills/` remains the one real location. Nothing about `0026`'s classification of
`skills/` as "not the layer's" changes — Claude Code becomes a second reader of that directory,
not a second owner of it. No portable rule file changed: `.agents/AGENTS.md`, `tasks/AGENTS.md`,
`archive/AGENTS.md`, and `worktrees/AGENTS.md` still name no product, so `0011` holds exactly as
it did.

`OPEN-QUESTIONS.md`'s line naming "how agent capabilities and context reach heterogeneous hosts"
stays open. This closes the gap for one tool, in this one repository, the same way `0030` closed
only the `AGENTS.md`-import gap for Claude Code and left the wider distribution question alone.

A known limitation, not solved here: a tracked symlink depends on the checkout environment
supporting symlinks — Git's `core.symlinks` and the underlying filesystem. Where Git instead
checks out a symlink as a plain text file containing the target path (for example, Windows
without symlink support enabled), `.claude/skills` would appear as a file, not a directory, and
Claude Code would not see the skill there. This repository's CI runs on `ubuntu-latest`, where
this does not occur; it is recorded as a portability caveat rather than solved.

If `.agents/skills/` ever holds more than `ctxfold-init`, or a skill placed there by another
tool is not addressed to Claude Code, the whole directory becomes visible to Claude Code,
including anything not meant for it. This is accepted: symlinking one skill at a time instead
was rejected as adding a second thing to keep in sync with whatever `.agents/skills/` contains.
