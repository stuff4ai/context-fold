# Context — link-claude-skills

## References

- `decisions/0011-keep-the-model-vendor-neutral.md` — integration with a specific product is
  permitted only as an adapter over the neutral canonical model, never its source of truth. The
  symlink is that shape applied to a directory: `.agents/skills/` stays the one real location.
- `decisions/0026-map-what-is-under-the-agents-directory.md` — establishes `.agents/skills/` as
  "not the layer's ... answers to whatever put it there." This task doesn't change that
  ownership; Claude Code becomes a second reader of the directory, not a second owner.
- `decisions/0030-add-a-claude-code-adapter.md` — the precedent this task follows: a pointer
  rather than a copy, scoped to this repository's own use rather than the distribution, verified
  empirically with fresh `claude -p` sessions rather than asserted to work.
- `OPEN-QUESTIONS.md`, line ~226 — "How do agent capabilities and context reach heterogeneous
  hosts?" names the broader, still-unresolved question this task is one local instance of.

## Base state

`main` is at `6e63bc7` (`feat: add RFC lifecycle to task packages (#35)`) as of this task's
start. The next unused decision number is `0034` — `0033` was taken by
`decisions/0033-separate-rfc-discussion-from-execution-planning.md`, merged just before this
task began.
