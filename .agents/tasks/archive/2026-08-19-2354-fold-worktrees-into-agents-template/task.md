---
status: completed
objective: >-
  Move `templates/worktrees/AGENTS.md` into `templates/agents/worktrees/AGENTS.md`, so it joins the
  byte-identical/portable set the rest of `templates/agents/` already belongs to, instead of being a
  one-time seed that is copied once and never re-synced.
---

# Fold worktrees/AGENTS.md into the byte-identical template set

## Why

`skills/ctxfold-init/templates/` currently ships three things with different lifetimes:
`templates/agents/**` (byte-identical forever, mechanically enforced), `templates/worktrees/AGENTS.md`
(copied once at adoption, then explicitly never re-synced — its own text says so), and
`templates/INDEX.md` (copied once, then diverges immediately by construction, since it's a live
index of real tasks).

This session hit real confusion from that split twice while working in a worktree: whether
`templates/worktrees/AGENTS.md` needed to track `.agents/worktrees/AGENTS.md` after a workflow
fix was added to the installed copy. `decisions/0021` and `decisions/0026` justified keeping
`worktrees/AGENTS.md` outside the byte-identical set on the assumption its content would need
per-project editing (different VCS, different worktree conventions). In this project's actual
history that assumption hasn't held: the content has stayed fully generic, already handles
"another version control system will have its own spelling," and carries no context-fold-specific
detail.

Decided: fold it into the single `templates/agents/` structure now — one install mechanism,
byte-identical like the rest — and only reintroduce a special case later if a concrete need for
divergence actually appears. `templates/INDEX.md` stays separate; it is not in the same position,
since its divergence isn't a risk to guard against, it's the file's entire purpose.

## Scope

- `skills/ctxfold-init/templates/worktrees/AGENTS.md` → moved to
  `skills/ctxfold-init/templates/agents/worktrees/AGENTS.md`, with its self-referential opening
  paragraph rewritten to match the other three portable files.
- `.agents/skills/ctxfold-init/templates/worktrees/AGENTS.md` → moved identically, to keep the
  installed skill copy matching what ships.
- `.agents/worktrees/AGENTS.md` → updated in place to match.
- `tests/test_conventions.py` — `installed_layer_files()` (a safe, direct existence check for
  `worktrees/AGENTS.md`, not a reuse of the `tasks/`-style recursive glob) and `PORTABLE`.
- `skills/ctxfold-init/ADOPTING.md` — the install-mapping table, the paragraph explaining the
  split, and the re-adoption section's per-file instructions.
- `.agents/AGENTS.md` and its template source `skills/ctxfold-init/templates/agents/AGENTS.md`
  (and the installed skill mirror) — the "What you will find under `.agents/`" `worktrees/`
  bullet, giving it an explicit is/isn't-the-layer label like `tasks/` and `skills/` already have.
- A new decision record narrowing `decisions/0021`, `decisions/0026`, and `decisions/0017` (their
  `Status` lines only; body text is immutable).
- `.agents/tasks/INDEX.md` — this task's row and eventual archival update.

## Out of scope

- Moving `templates/INDEX.md`. It cannot join the byte-identical set even in principle — it is a
  live index, not a rule file.
- Anything under `.agents/tasks/AGENTS.md`, `plan.md`/`rfc.md`, or task-package structure — that
  is the parallel `add-task-rfc` task's scope, not this one's.
- Auditing other adopting repositories for the re-adoption behavior change noted below. There are
  none known; context-fold is its own first user.

## Acceptance

1. All three copies of the worktrees `AGENTS.md` (shipped template, installed skill mirror, this
   project's installed copy) are byte-identical.
2. `pytest` passes, including `test_installation_matches_the_distribution`,
   `test_distribution_is_complete`, `test_portable_rules_carry_no_project_detail`, and
   `test_installed_skill_matches_the_shipped_one` — with a task worktree checked out at the same
   time, confirming `installed_layer_files()`'s fix does not recurse into live worktree checkouts.
3. `pymarkdownlnt --config .pymarkdown.json scan -r --respect-gitignore .` passes.
4. `ADOPTING.md` and `.agents/AGENTS.md` read consistently with the new structure — no leftover
   sentence claiming `worktrees/AGENTS.md` diverges or is left alone on re-adoption.
5. A decision record exists, narrowing `0021` and `0026`, stating the re-adoption behavior change
   (existing customizations to `.agents/worktrees/AGENTS.md` are now overwritten on reinstall,
   where before they were preserved) as a consequence.

## Problems

- The plan only named `decisions/0021` and `decisions/0026` for narrowing. Grepping for leftover
  `templates/worktrees` references after the main edit found `decisions/0017-adoption-procedure.md`
  also carried a stale narrowing note (from `0026`) describing `templates/worktrees/AGENTS.md` as
  a separate "also copies" step distinct from the portable rule files — which stops being accurate
  once it's one of them. Added a third `Status` narrowing note there, same pattern.

## Outcome

`templates/worktrees/AGENTS.md` moved to `templates/agents/worktrees/AGENTS.md` and now ships
byte-identical, joining `PORTABLE` and the mechanical checks the other three portable files
already had. All three copies (shipped template, installed skill mirror, this project's own
`.agents/worktrees/AGENTS.md`) verified byte-identical. `installed_layer_files()` gained a direct
existence check for `worktrees/AGENTS.md` rather than reusing the `tasks/`-style recursive glob,
which would have wrongly recursed into live worktree checkouts — verified by running the full
suite with two worktrees checked out at once. `ADOPTING.md` and `.agents/AGENTS.md` updated to
match the new structure, including the re-adoption behavior change stated inline. Decision record
`decisions/0032-fold-worktrees-agents-md-into-the-byte-identical-set.md` added, narrowing
`0021`, `0026`, and `0017`'s `Status` lines (bodies untouched).

`templates/INDEX.md` was not moved — out of scope, structurally incompatible with byte-identity.

Durable artifacts: `decisions/0032-...md`; the moved/updated `AGENTS.md` in all three locations;
`tests/test_conventions.py`'s `PORTABLE` and `installed_layer_files()`; `ADOPTING.md`'s
install-mapping table, split-explanation paragraph, and re-adoption section; `.agents/AGENTS.md`'s
`worktrees/` bullet.

`pytest` (315 passed) and `pymarkdownlnt --config .pymarkdown.json scan -r --respect-gitignore .`
both pass at this state, run exactly as `.github/workflows/ci.yml` runs them.
