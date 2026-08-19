# Add a Claude Code adapter

## Status

Accepted

## Context

Claude Code auto-loads only `CLAUDE.md` files — a global one and a project-level one, if either
exists — into a session's context at start. It has no built-in awareness of `AGENTS.md`, this
project's own convention for where agent operating rules live.

This surfaced concretely on the pull request that removed `templates/task/`
(`decisions/0029-drop-the-task-template.md`). The agent read `.agents/tasks/AGENTS.md` and
whatever the task itself pointed at, executed the task, and opened a pull request — and read the
root `AGENTS.md` only after being asked directly why it hadn't. By then it had already missed two
rules stated only there: sign every commit, and name branches `<type>/<kebab-case-topic>`. Both
needed fixing after the fact, on a change already pushed. Recorded in that task's own
`## Problems`.

`decisions/0011-keep-the-model-vendor-neutral.md` already anticipated this shape of problem. The
canonical rules "name no product, assume no particular tool's directory layout," and integration
with a specific product, if it happens, is an adapter over the canonical model — never the
source of truth.

## Decision

A root `CLAUDE.md` is added, consisting of a heading and one line:

```markdown
# CLAUDE.md

@AGENTS.md
```

`@AGENTS.md` is Claude Code's own import syntax; it is not Markdown link or reference syntax
that another reader would need to resolve. This makes `CLAUDE.md` a pointer rather than a copy —
nothing in it needs to change when `AGENTS.md` does, and it carries no content of its own to
drift out of sync.

Verified rather than assumed: two fresh, tool-less `claude -p` sessions were started in this
repository, each denied every tool so an answer could only come from what was already in
context at session start, and each asked a question answerable only from `AGENTS.md`. Both
answered correctly and named the source as "the AGENTS.md content shown at session start" — the
first for the branch-naming and commit-sign-off rules together, the second, after `CLAUDE.md`
gained a heading to satisfy the Markdown linter, for branch naming alone. The import works with
or without a heading preceding it.

No portable rule file changed. `.agents/AGENTS.md`, `.agents/tasks/AGENTS.md`, and
`.agents/tasks/archive/AGENTS.md` still name no product and assume no particular tool's layout —
`decisions/0011-keep-the-model-vendor-neutral.md` holds exactly as it did.

## Consequences

A Claude Code session started in this repository has the root `AGENTS.md`'s content — the
project rules, the decision-record pointer, the change workflow — from the first turn, without
being told to read it. The specific failure that prompted this (missed sign-off, wrong branch
name) is closed for that file; `AGENTS.md` in turn points to `.agents/AGENTS.md`, which is not
pulled in by the same import and still depends on an agent following that pointer once it has
`AGENTS.md`'s content.

This is scoped to this repository's own use, not the distribution. `skills/ctxfold-init/` ships
no `CLAUDE.md` and no adapter for any product; an adopter using Claude Code gets nothing from
this decision unless they add the same file themselves. Whether the distribution should offer
this adapter to adopters is a separate, undecided question.

`.claude/RESUME.md` remains untracked, as it was before this decision. Nothing here changes
whether it should be.
