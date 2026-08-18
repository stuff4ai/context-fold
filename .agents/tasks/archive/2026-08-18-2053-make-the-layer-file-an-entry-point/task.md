# Make the layer file a map of what is under `.agents/`

## Status

completed

## Blocked by

- `rules-for-concurrent-tasks` (pull request 21) — **cleared**, merged as `2d5f9cb`. It
  introduced `## Blocked by` itself, the two-line `.gitignore` form this task extends, and
  `0025`, whose position on worktrees this task revises.

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

## Outcome

`.agents/AGENTS.md` ends with a map instead of a pointer. Each thing under `.agents/` gets a
sentence naming its owner: `tasks/` is the layer's, `skills/` answers to whatever installed a
skill and is not a statement about this project, `worktrees/` is parallel checkouts if the
project keeps any. The owner is the useful part, because it decides whether a file is this
project's current state or a copy of it.

They are not called three layers. `0018` separates the layer from the directory it lives in, and
three defects this month came from blurring that.

`templates/worktrees/AGENTS.md` ships, copied once like `templates/task/` rather than replaced
wholesale. Two things forced it: the entry point references the file, and the `.gitignore`
negation names that exact path, so a negation with nothing behind it does nothing.

Durable artifacts:

- `decisions/0026-map-what-is-under-the-agents-directory.md` — the decision.
- `decisions/0025-run-tasks-in-parallel.md` — Status: shipping the convention is not the same as
  the layer adopting it.
- `skills/ctxfold-init/templates/agents/AGENTS.md` — the map.
- `skills/ctxfold-init/templates/worktrees/AGENTS.md` — new, copied once.
- `skills/ctxfold-init/ADOPTING.md` — a copy line, a new ignore step, and re-entry told to leave
  the adopter's copy alone or offer a missing one rather than adding it unasked.
- `skills/ctxfold-init/SKILL.md` — confirm the result by asking the version control system what
  it sees, not by reading the ignore rules.
- `skills/ctxfold-init/templates/agents/tasks/AGENTS.md` — "At the branch head" named a version
  control system in a file that carries none.

Verified by building: two scratch repositories were adopted from the procedure, one with no
`.gitignore` and one with an existing one, then given a real parallel checkout. The file is
tracked in both, the checkout invisible in both, and the existing `.gitignore` kept its contents.

## Problems

### Renumbering the procedure stranded a reference to a step number

Inserting an ignore step between "Install the layer" and "Point at the layer" renumbered the two
sections after it. A sentence in the introduction still said "step 2, where an existing
`AGENTS.md` is added to rather than created", which after the insertion described the ignore
step.
Assumed: renumbering headings is mechanical, so a script that renumbers them finishes the job.
Actually: the numbers are also referred to in prose, where no renumbering script looks. The
reference now names the step rather than its position, which cannot go stale.
Found by grepping for step and section numbers before finishing, rather than by review. That is
the first time this session a twin was caught by sweeping for the specific shape of the change
rather than by a verifier.

### Shipping a shape on one worked example, knowingly, for the second time

`templates/worktrees/AGENTS.md` ships on the evidence of one project using worktrees: this one.
Assumed: nothing — this is the same bet as `templates/task/`, which six adoption runs later has
injected non-content four different ways and is queued for a decision about removing it.
Taken anyway because the failure it prevents was measured rather than imagined, and because the
entry point referencing a file adopters do not have would be worse.
Recorded in `0026`'s Consequences so the next person to weigh it knows the bet was repeated with
open eyes rather than forgotten.
