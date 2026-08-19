# Decide whether the task template earns its place

## Status

completed

## Objective

Decide whether `templates/task/` should be kept, changed, or dropped.

## Why

Five foreign adoption runs produced five structurally correct task packages. Three wrote the
package from scratch and two copied the template, and all five carried every required section.

The assumption behind shipping a skeleton was that this is how the shape is transmitted. The
evidence says otherwise: `tasks/AGENTS.md` lists the required sections and `ADOPTING.md`
describes task zero's content, so the shape arrives whether or not the template is opened. The
template restates it in a third place, reached for about half the time.

Its one distinctive effect so far has been a defect it introduced. Two example lines were added
to `templates/task/context.md` while fixing an unrelated problem, both written in the voice of
real entries; two runs kept the one that named a file that existed. The fix — a single braced
placeholder — is untested, because the run after it wrote the package from scratch and never
touched the template. The absence of residue there proves nothing.

A sixth run settles the direction. Adopting `etu-forms` produced a finished, archived package
carrying three separate pieces of the template that were never meant to be content: the
instructional paragraph under `## References`, the one under `## Open questions`, and an
`## Assumptions` heading with nothing beneath it. A second agent inspecting the same repository
found a fourth independently — a duplicated `## Problems` heading, the placeholder left in place
beside the real entry.

So the template's distinctive effect is now measured rather than suspected: four defects, none of
which the rules alone could have caused, in the one run that used it most faithfully. The
question is no longer whether it earns its place but whether anything survives — headings without
prose, or nothing.

## Scope

- `skills/ctxfold-init/templates/task/`.
- Whatever the decision requires: a record, or a change to the rules if the template goes.

## Out of scope

- `templates/agents/`, which is a different question with a different answer.

## Acceptance

1. A decision, recorded, with the evidence behind it.
2. If the template stays, something is different about it — otherwise the evidence said nothing.

## Problems

`decisions/0026-map-what-is-under-the-agents-directory.md`, written before this task opened,
already named `templates/task/` as "under review for removal" while making an unrelated point
about `templates/worktrees/AGENTS.md`. It was not treated as pre-deciding this task — the record
states an intent to review, not a verdict — but it corroborates the direction the evidence in
`## Why` already pointed, from a decision made without reference to this one.

Decision records are immutable apart from `Status` (`decisions/README.md`). Three existing
records — 0018, 0021, 0026 — describe `templates/task/` as part of what ships, and removing it
made those descriptions false. Narrowing each record's `Status` line, rather than editing its
`Context`/`Decision`/`Consequences`, is what 0018 itself already did to narrow 0021's target when
0021 was written; this task follows the same pattern rather than inventing one.

`.agents/skills/ctxfold-init/` is a byte-identical installed copy of `skills/ctxfold-init/`,
enforced by `tests/test_conventions.py::test_installed_skill_matches_the_shipped_one`. Removing
`templates/task/` and editing `ADOPTING.md` had to happen in both trees or the suite would fail;
not obvious from the task's own `## Scope`, which names only the distribution copy.

## Outcome

Decided: drop. `skills/ctxfold-init/templates/task/` is removed from both the distribution
(`skills/ctxfold-init/`) and this repository's own installed copy (`.agents/skills/ctxfold-init/`).
`ADOPTING.md` (both copies) no longer tells an adopter to copy the template for task zero; it
tells them to write `task.md` and `context.md` directly, using the required sections
`.agents/tasks/AGENTS.md` lists.

The decision and its evidence are recorded durably in
`decisions/0029-drop-the-task-template.md`, indexed in `decisions/README.md`. It narrows
`decisions/0018-ship-a-distribution.md`, `decisions/0021-separate-what-upgrades-from-what-diverges.md`,
and `decisions/0026-map-what-is-under-the-agents-directory.md`, each of which described
`templates/task/` as shipped; their `Status` lines now say so, their bodies are otherwise
unchanged.

Acceptance:

1. Satisfied — `decisions/0029-drop-the-task-template.md` records the decision and the six-run
   evidence behind it.
2. Satisfied on the "dropped" branch: the template does not survive, so there is nothing left to
   be different. `templates/task/` no longer exists in either the distribution or the installed
   copy.
