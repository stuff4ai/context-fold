---
status: active
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

- `tests/test_conventions.py` — extend it to scan shipped `skills/*/` content (`SKILL.md`,
  bundled scripts and reference files) for this-repository-specific references.
- A precise, checkable definition of what counts as acceptable general content (the methodology's
  own name, generic layer paths any adopting project would have, such as `.agents/tasks/` or
  `.agents/worktrees/`) versus a leak (this repository's own decision numbers or `decisions/`
  paths, `tests/`, task slugs, or other artifacts that exist only because of this repository's own
  implementation).
- `skills/AGENTS.md` — state the same boundary where a human or agent writing a skill reads it
  before the check catches a mistake.
- A decision record for the selected portability boundary, enforcement and known limits.

## Out of scope

- Auditing or rewriting already-shipped skill content beyond what the new check requires; both
  `skills/ctxfold-init/` and `skills/ctxfold-tasks/` should already pass without further changes.
- `.agents/skills/` ownership, contract, or sublayer questions generally — that is
  `define-agent-sublayer-model` and `formalize-skills-sublayer`'s territory. This task is only
  about what a shipped skill's own content may say, not where installed skills live or who owns
  that directory.

## Acceptance

1. A resolved RFC and decision record require both author guidance and a mechanical check for
   repository-specific references in shipped skills.
2. `skills/AGENTS.md` tells skill authors to carry the reusable contract or procedure rather than
   this repository's evidence, and distinguishes permitted product/generic adopter paths from
   prohibited source-repository references.
3. The existing `pytest` suite scans every UTF-8-decodable regular file inside each shipped skill
   package. It reports that non-UTF-8 or binary content is outside the lexical check and states the
   resulting false-negative boundary and the check's false-positive risk.
4. The check rejects bare numbered decision references, decision-record filenames and
   `decisions/` paths, any `tests/` or `test_*.py` reference, and concrete current or archived task
   slugs or package identities. It permits the `context-fold` name and generic adopter paths such
   as `.agents/tasks/` and `.agents/worktrees/`.
5. Regression cases cover every prohibited category, including the escaped `decision 0037` and
   `tests/test_conventions.py` strings, plus the permitted categories. No allowlist or suppression
   mechanism is added; a legitimate collision requires a later reviewed rule or check change.
6. Both current shipped packages pass unchanged from the handoff's contract revision, proven by
   an exact Git comparison of `skills/ctxfold-init/` and `skills/ctxfold-tasks/`.
7. The full `pytest tests/` suite, recursive `pymarkdown` scan and `git diff --check` pass at the
   finished revision.

## Problems

### Cross-stack ownership and final-head ordering were initially underspecified

The first handoff plan addressed Claude's executor directly and placed its return after the final
check. The project rule says only a lead session writes or answers a handoff, and a return commit
changes the head being checked. The contract now addresses `claude:lead`, makes its executor
report-only, and requires the return-only commit before the final exact-head check and PR.

## Approval

Human.
