# Context — separate-distribution-from-installation

## Base state

`main` is at `971bb59`. Seventeen decision records, eleven archived tasks, a check suite and CI.

The three rule files live only in `.agents/`, which is simultaneously this repository's
installation and the thing `ADOPTING.md` points adopters at. There is no distribution.

A scratch copy of a real repository from the previous task's dry run still exists, with the
unfixed rule files installed into it.

## References

- `decisions/0005-agents-layer-boundary.md` — states that everything under `.agents/` other than
  the rule files is the project's own. That reading is what this narrows.
- `decisions/0017-adoption-procedure.md` — the procedure whose first step this changes.
- `.agents/tasks/archive/2026-08-13-1838-write-the-adoption-procedure/task.md` — the dry run that
  found both defects, and why neither was reachable from inside this repository.

## Assumptions

- Byte-identity is the right check. Anything looser permits the installation to drift in ways that
  read as intentional.
- `INDEX.md` is instance data. Its divergence from the empty template is the whole point of it,
  so it is excluded from the identity check rather than special-cased inside it.

## Context conflicts

`0005` says the rule files are "identical in every project using context-fold" and treats
`.agents/` as the layer. After this, the identical thing is the template and `.agents/` is one
installation of it. The wording survives with a different referent, which is exactly the kind of
drift that hides — hence a record rather than an edit.

## Open questions

Whether `templates/` is the right name for what is shipped. It describes the files accurately
today, but a template implies filling in, and three of these five are copied unchanged.
