# Decide whether the task template earns its place

## Status

planned

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
