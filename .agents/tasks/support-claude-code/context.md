# Context — support-claude-code

## Base state

No `CLAUDE.md` exists at the repository root today. `.claude/` exists and holds
`.claude/RESUME.md`, a session checkpoint file — currently untracked by Git (`git ls-files
.claude/` returns nothing), so nothing under it is part of the repository as checked out fresh.

## References

- `AGENTS.md` — the file this task is about surfacing automatically; also states the project's
  git workflow (branch naming, commit sign-off) that was missed as a direct result of it not
  being read.
- `decisions/0011-keep-the-model-vendor-neutral.md` — the constraint this adapter must satisfy:
  the canonical rules name no product, and integration with one is an adapter over the model,
  never the source of truth.
- `decisions/0026-map-what-is-under-the-agents-directory.md` — prior art on treating a
  vendor-specific presence as "not ours, and not a statement about this project"; written about
  `skills/` and `.agents/`, not about a repository-root file, so it may not transfer directly.
- `.agents/tasks/archive/2026-08-17-0116-add-init-skill/task.md` — records `.claude/` as
  "untracked and vendor-specific," the prior discussion of where Claude-specific files sit in
  this repository.
- `.agents/tasks/archive/2026-08-19-1250-decide-whether-the-task-template-earns-its-place/task.md`
  — `## Problems` records the incident that prompted this task.

## Open questions

Whether Claude Code's `@path` import syntax actually loads the referenced file's content into a
session automatically at start, or only makes it available on request — needs verifying by
starting a session and checking, not assumed from how the mechanism is described.

Whether `.claude/RESUME.md` being untracked is intentional — a session-local file that should
stay out of version control — or an oversight. Relevant only if it turns out to block adding
`CLAUDE.md` cleanly; otherwise a separate matter from this task.
