# Context — add-init-skill

## Base state

`main` is at `4dfe982`. Twenty decision records, thirteen archived tasks, CI green. `templates/`
and `ADOPTING.md` sit at the repository root; nothing named `skills/` exists.

## References

- `decisions/0011-keep-the-model-vendor-neutral.md` — adapters may translate the model into what
  a product expects and are never the source of truth. The constraint that shapes the split
  between `SKILL.md` and `ADOPTING.md`.
- `decisions/0018-ship-a-distribution.md` — what is shipped versus what is installed, and the
  identity check that binds them. Its `TEMPLATES` path moves.
- `decisions/0007-archive-before-merge.md` — approval authorizes archival, which is why the skill
  stops where it does.
- `.agents/tasks/archive/2026-08-13-1838-write-the-adoption-procedure/task.md` — the dry run whose
  findings shaped the procedure the skill now carries.

## Assumptions

- Skill installers copy whole directories. Verified against an installed skill carrying seven
  scripts in a subdirectory, but only one installer was examined.
- The frontmatter convention is `name` plus `description`, with invocation cues in the
  description. Taken from installed skills rather than from a specification.

## Context conflicts

The canonical procedure and distribution end up inside an adapter's directory, which `0011`
argues against. Accepted because the alternatives are duplication or a skill that cannot install
itself, and recorded in `0020` rather than left implicit.

## Open questions

Whether `ctxfold-init` settles the skill-naming question or only answers it for one skill. The
convention was never established; this picks one and does not prove it is the right one.
