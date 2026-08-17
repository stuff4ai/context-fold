# Decide whether the task template earns its place

## Status

planned

## Objective

Decide whether `templates/task/` should be kept, changed, or dropped.

## Why

Five foreign runs produced five structurally correct task packages. Two copied the template and
edited it; three wrote the package from scratch and were no worse for it. The shape is already
carried by the rules, which list the required sections, and by the procedure, which describes
task zero's content — so the template restates it in a third place.

Its one distinctive effect so far has been a defect it introduced: example lines written in the
voice of real content, which two runs left in the finished package.

Nothing is broken today, so this is not urgent. It is recorded because the evidence exists now
and will be harder to reconstruct later.

## Scope

- `skills/ctxfold-init/templates/task/`.
- Whatever the decision requires: a record, or a change to the rules if the template goes.

## Out of scope

- `templates/agents/`, which is a different question with a different answer.

## Acceptance

1. A decision, recorded, with the evidence behind it.
2. If the template stays, something is different about it — otherwise the evidence said nothing.

## Problems

### The template is used about half the time and the rules carry the load

Five runs: three wrote the package from scratch, two copied the template. All five produced every
required section, because `tasks/AGENTS.md` lists them and `ADOPTING.md` describes task zero.
Assumed: shipping a skeleton is how the shape is transmitted.
Actually: the rules transmit it. The template is a third statement of the same thing, reached for
about half the time.

### Its only distinctive effect was to introduce a defect

Two example lines were added to `templates/task/context.md` while fixing an unrelated problem.
Both were written like real entries, and two runs kept the one naming a file that existed.
The fix — a single braced placeholder — is untested: the run after it wrote the package from
scratch and never touched the template, so the absence of residue proves nothing.
