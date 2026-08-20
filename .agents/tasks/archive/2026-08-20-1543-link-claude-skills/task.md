---
status: completed
objective: >-
  Let a Claude Code session in this repository discover and invoke the already-installed
  `ctxfold-init` skill.
---

# Link Claude Code to the installed skills

## Why

Claude Code only discovers skills under `.claude/skills/`. This repository already carries
`.agents/skills/ctxfold-init/` — `SKILL.md`, `ADOPTING.md`, `templates/`, all tracked in Git —
per `decisions/0026-map-what-is-under-the-agents-directory.md` ("not the layer's ... answers to
whatever put it there"). There is no `.claude/skills/`, so the skill is present but invisible to
Claude Code.

`decisions/0030-add-a-claude-code-adapter.md` already solved the same shape of problem for
`AGENTS.md`: a pointer (`CLAUDE.md` containing `@AGENTS.md`), scoped to this repository's own
use, verified empirically rather than asserted. This task extends the same adapter pattern to
skills.

## Scope

- A tracked directory symlink `.claude/skills` → `../.agents/skills`.
- `decisions/0034-extend-the-claude-code-adapter-to-skills.md` (new decision record).
- `decisions/README.md` (new index row).

## Out of scope

- `skills/ctxfold-init/templates/` — no change; this is a local adapter, not a portable-rule
  change.
- `OPEN-QUESTIONS.md` — the "heterogeneous hosts" question stays open; this narrows it by one
  instance, the same way `0030` did, and does not warrant an edit there (confirmed against
  `0030`'s own commit, which didn't touch it for a materially identical case).
- `AGENTS.md`, `.agents/AGENTS.md`, `README.md` — none currently describe `.claude/`, so none go
  stale.

## Acceptance

- `.claude/skills` exists, is tracked by Git as a symlink (mode `120000`), and its stored content
  is exactly `../.agents/skills`.
- A fresh `claude -p` session started in this worktree lists `ctxfold-init` among its available
  skills, with a description matching `.agents/skills/ctxfold-init/SKILL.md`'s actual
  frontmatter, and can answer a question whose answer only appears in that skill's own content —
  confirming the skill's body, not just its name, is reachable through the symlink.
- `pytest` and `pymarkdown --config .pymarkdown.json scan -r --respect-gitignore .` both pass
  from the repository root.
- `decisions/0034-extend-the-claude-code-adapter-to-skills.md` exists, Accepted, and states what
  was actually observed in the verification above (not asserted).
- `decisions/README.md` lists `0034`.

## Problems

None — the work matched the plan going in. One naming detail: `0033` was expected to be free
but had just been taken by `0033-separate-rfc-discussion-from-execution-planning.md` (merged to
`main` immediately before this task started); the new record used `0034` instead, per the
project's own renumbering rule for provisional numbers.

## Outcome

`.claude/skills` is a tracked symlink to `../.agents/skills` (verified: `git ls-files -s` mode
`120000`, blob content exactly `../.agents/skills`). `decisions/0034-extend-the-claude-code-adapter-to-skills.md`
records the decision, Accepted, with the actual observed output of two fresh `claude -p`
verification sessions — one listing `ctxfold-init` among available skills, one invoking it and
reporting every path read as `.claude/skills/ctxfold-init/...`. `decisions/README.md` lists
`0034`. `pytest` (389 passed, 2 skipped, run against the final archived state) and
`pymarkdown --config .pymarkdown.json scan -r --respect-gitignore .` (no findings) both pass from
the repository root.

Durable artifacts: `.claude/skills` (the symlink itself), `decisions/0034-extend-the-claude-code-adapter-to-skills.md`,
the `decisions/README.md` index row. Nothing else needed changing —
`skills/ctxfold-init/templates/`, `OPEN-QUESTIONS.md`, `AGENTS.md`, `.agents/AGENTS.md`, and
`README.md` were checked directly and none mention `.claude/` in a way this makes stale.
