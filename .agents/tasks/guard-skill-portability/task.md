---
status: planned
objective: >-
  Decide whether to add a mechanical check that catches a shipped skill referencing this
  repository's own project-specific artifacts — and implement it if the decision is yes.
---

# Guard skill portability

## Why

`decisions/0011-keep-the-model-vendor-neutral.md` and
`decisions/0005-agents-layer-boundary.md` already establish that portable content must not
assume the reader has this specific repository, and
`tests/test_conventions.py::test_portable_rules_carry_no_project_detail` enforces that
mechanically for the managed `AGENTS.md` blocks — checking for decision-record filenames, paths
into `decisions/`, the project's own name, and task slugs.

Skills under `skills/*/` are portable the same way: `skills/ctxfold-init/`'s own instructions say
adoption is a file copy into a different repository. Nothing mechanically enforces the same
no-project-detail rule there. During
`.agents/tasks/archive/2026-08-21-1816-add-ctxfold-tasks-skill/`, the shipped
`skills/ctxfold-tasks/scripts/query_tasks.py` named this repository's own decision number and
`tests/test_conventions.py` in its docstrings — content that would be meaningless, and
misleading, in a different project that only installed the skill. Review caught it after the
pull request was already open; a fresh verifier confirmed the fix, but nothing in the test suite
would have caught the original mistake or would catch a repeat of it.

## Scope

- `tests/test_conventions.py` — whether and how to extend it to scan `skills/*/` content
  (`SKILL.md`, any bundled scripts or reference files) for this-repository-specific references,
  mirroring `test_portable_rules_carry_no_project_detail`'s approach.
- A precise, checkable definition of what counts as acceptable general content (the methodology's
  own name, generic layer paths any adopting project would have, such as `.agents/tasks/` or
  `.agents/worktrees/`) versus a leak (this repository's own decision numbers or `decisions/`
  paths, `tests/`, task slugs, or other artifacts that exist only because of this repository's own
  implementation).
- Whether the rule belongs only in the check, or also as a stated authoring rule somewhere a
  human or agent writing a new skill would read it before the check catches a mistake.

## Out of scope

- Auditing or rewriting already-shipped skill content beyond what the new check requires; both
  `skills/ctxfold-init/` and `skills/ctxfold-tasks/` should already pass without further changes.
- `.agents/skills/` ownership, contract, or sublayer questions generally — that is
  `define-agent-sublayer-model` and `formalize-skills-sublayer`'s territory. This task is only
  about what a shipped skill's own content may say, not where installed skills live or who owns
  that directory.

## Acceptance

1. A decision, recorded: whether a mechanical check is added, and if not, why not.
2. If added: the check runs in the existing `pytest` suite and CI, states its false-positive and
   false-negative risk, and both currently shipped skills pass it without content changes beyond
   what already landed fixing the incident this task cites.

## Approval

Human.
