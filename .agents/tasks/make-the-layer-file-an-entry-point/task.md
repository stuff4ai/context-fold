# Make the layer file a map of what is under `.agents/`

## Status

planned

## Blocked by

- `rules-for-concurrent-tasks` (pull request 21) — it introduces `## Blocked by` itself, adds the
  two-line `.gitignore` form this task extends, and creates `0025`, whose position on worktrees
  this task revises. Starting before it merges would edit `.gitignore` and `0025` from two
  branches at once.

## Objective

Turn `.agents/AGENTS.md` into an entry point that says what an agent will find under `.agents/`
and who owns each part, and ship the worktrees convention so an adopter can have one too.

## Why

`.agents/AGENTS.md` explains what the layer is and how to think about it, then ends with one line
of navigation: "Work is organized under `tasks/`. Start there." That was true when `tasks/` was
the only thing there.

Three things are under `.agents/` now, with three different owners. `tasks/` is the layer's and
its rules ship with it. `skills/` belongs to whatever installed a skill — this project's own
`ctxfold-init` lands there — and nothing about it is the layer's business. `worktrees/` is
parallel checkouts, which `0025` makes this project's workflow.

An agent arriving at `.agents/` gets no account of that. It finds three directories, one line
pointing at one of them, and no statement of which are safe to read as this repository's context.
That is the failure measured while adding worktrees: a checkout under `.agents/` reads as a
second copy of every record and task package unless something says otherwise.

The entry point should name each, describe it in a sentence, say who owns it, and point at the
detailed rules where they exist.

Two consequences follow, and both are the point rather than side effects.

`worktrees/AGENTS.md` has to ship. Once the entry point references it, an adopter needs one; and
the `.gitignore` negation the skill will write names that exact file, so a negation with nothing
behind it is pointless. It ships as a copied-once template beside `templates/task/`, not as part
of what upgrades — the mechanics are the adopter's to change.

`0025` says worktrees are "this project's workflow, not part of the layer". That stops being
accurate the moment the distribution carries them, so `0025` needs its Status narrowed by
whatever record this task produces.

## Scope

- `templates/agents/AGENTS.md` — replace `## Follow scoped instructions` with a map of what is
  under `.agents/`: `tasks/`, `skills/`, `worktrees/`, each with an owner and a pointer.
- `templates/worktrees/AGENTS.md` — new, copied once, carrying the detail.
- `templates/agents/tasks/AGENTS.md` — `## Final exact-head check` only: "At the branch head"
  names a version control system in a file that carries none.
- `skills/ctxfold-init/SKILL.md` and `ADOPTING.md` — create or update `.gitignore` with the
  two-line form, and copy the worktrees template.
- `tests/test_conventions.py` — whatever the new template requires of the distribution checks.
- A decision record, and `0025`'s Status.

## Out of scope

- Calling `tasks/`, `skills/` and `worktrees/` three layers. `0018` separates the layer from the
  directory it lives in, and three defects this month came from blurring that. They are three
  things under one directory with three owners.
- Adopting the `skills/` convention, or saying anything about what belongs in it beyond that it
  is not ours. `0011` permits a vendor convention only as an adapter over the canonical model.
- Requiring an adopter to use parallel checkouts. The section describes where they go if the
  project has them.
- `.agents/context/` and `.agents/learning/`, which remain unbuilt and deferred.

## Acceptance

1. `.agents/AGENTS.md` names each thing under `.agents/`, says who owns it in a sentence, and
   points at detailed rules where they exist.
2. The `skills/` section tells an agent it is not the layer's and not to touch it, without
   adopting the convention or describing what belongs in it.
3. The worktrees section is true for a project that has no worktrees.
4. `templates/worktrees/AGENTS.md` ships, is copied once rather than upgraded, and the checks
   treat it as they treat `templates/task/`.
5. Following the skill on a repository with no `.gitignore` produces one with the two-line form;
   following it on a repository that has one leaves the existing content alone.
6. The `.gitignore` negation names a file the skill actually creates.
7. `0025`'s Status records that worktrees are no longer only this project's.
8. No portable rule file names a version control system, including `## Final exact-head check`.
