# Context — guard-skill-portability

## References

- `decisions/0011-keep-the-model-vendor-neutral.md` — the existing vendor-neutrality decision
  this task would extend from the managed `AGENTS.md` blocks to shipped skills.
- `decisions/0005-agents-layer-boundary.md` — the project-layer/agent-layer boundary that a
  shipped skill leaking this repository's own artifacts violates.
- `tests/test_conventions.py::test_portable_rules_carry_no_project_detail` — the existing check
  to model a `skills/*/` version on: what it flags (decision-record filenames, `decisions/`
  paths, the project's own name, task slugs) and how it reads the managed block before scanning.
- `tests/test_conventions.py::test_skill_is_self_contained`,
  `test_skill_has_usable_frontmatter` — the existing skill-specific checks this would sit beside.
- `.agents/tasks/archive/2026-08-21-1816-add-ctxfold-tasks-skill/task.md` — the concrete
  incident this task exists to prevent a repeat of: its `## Problems` section records a shipped
  docstring naming this repository's own decision number and test file, found by review after
  the pull request opened, fixed, and confirmed by a fresh verifier — with no automated check
  that would have caught the original mistake.
- `skills/ctxfold-tasks/scripts/query_tasks.py` — the current, already-fixed file; a new check
  should pass against it as-is.
- `decisions/0034-extend-the-claude-code-adapter-to-skills.md` — records that `.agents/skills/`
  is a second reader of shipped skill content, not a second owner; relevant context for scoping
  this task to `skills/*/` rather than also `.agents/skills/*/` (which is meant to mirror
  `skills/*/` byte-for-byte, so a check against the shipped copy already covers it).
- `rfc.md` — resolves the portability boundary, broad lexical enforcement and author guidance.
- `plan.md` — defines the cross-stack implementation, verification and delivery sequence.
- `decisions/0040-guard-shipped-skill-portability.md` — the provisional durable record the
  implementation will add.
- `skills/AGENTS.md` — the project-owned author guidance the implementation will add.

## Not relevant

- `.agents/skills/` ownership, contract, or sublayer questions — `define-agent-sublayer-model`
  and `formalize-skills-sublayer` own that.
- Content-quality review of skills beyond the specific portability question — whether a skill is
  well-written is not this task's concern.

## Base state

- The task worktree starts from fetched `origin/main` at `1d3be58c1cc3bb22c4622cd1def3baf43a0dba49`.
- A read-only scan found neither broad forbidden references nor current task-slug overlaps in
  `skills/ctxfold-init/` or `skills/ctxfold-tasks/`; their contents should remain unchanged.
