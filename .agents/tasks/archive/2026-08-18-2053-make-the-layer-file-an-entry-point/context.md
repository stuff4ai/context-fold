# Context — make-the-layer-file-an-entry-point

## Base state

`main` is at `ac192b5`. `.agents/` holds `tasks/`, `skills/` and — on pull request 21, not yet on
`main` — `worktrees/`. `.agents/AGENTS.md` has four sections and one line of navigation.

## References

- `.agents/AGENTS.md` — `## Follow scoped instructions` is the line this replaces.
- `decisions/0018-ship-a-distribution.md` — the layer is what was installed and `.agents/` is
  only where it lives. The reason the three are not called layers.
- `decisions/0011-keep-the-model-vendor-neutral.md` — a vendor convention is permitted as an
  adapter, not as part of the model. Bounds what the `skills/` section may say.
- `decisions/0021-separate-what-upgrades-from-what-diverges.md` — why `templates/task/` is copied
  once and `templates/agents/` is replaced wholesale; the new template follows the first.
- `decisions/0025-run-tasks-in-parallel.md` — on pull request 21. Says worktrees are this
  project's workflow, which this task revises.
- `skills/ctxfold-init/ADOPTING.md` — the copy steps and the "if the layer is already there"
  path, both of which gain a file.

## Assumptions

- An adopter who wants parallel checkouts wants them where we put them. Weakly held: it is one
  worked example, and `templates/task/` is a standing reminder that shipping a shape on one
  example produces something half of them ignore.
- `skills/` is the only foreign directory worth naming. It is the one this project has actually
  seen, in an adoption run where an installer had already written there.

## Context conflicts

`0025` calls worktrees "this project's workflow, not part of the layer" and this task ships them.
Both can be true — the distribution already carries `templates/task/` and `INDEX.md`, which are
copied once and then belong to the adopter, so shipping something is not the same as making it
part of the layer. `0025`'s Status has to say so rather than leaving the sentence to be read
literally.

## Open questions

Whether the entry point should describe `.agents/context/` and `.agents/learning/`, which are
named in `OPEN-QUESTIONS.md` as deferred and do not exist. Describing what is absent invites
someone to build it; saying nothing means the map is silent about names a reader may have met.
