# Plan — bootstrap-tasks-layer

Execution strategy. Mutable. Not a log — friction goes in `task.md` under `## Problems`.

## Ordering constraint

A valid task package needs `tasks/AGENTS.md` to define what a task package is, but writing
that file is part of this task. The same shape as recording the decision to use decision
records.

Resolution: build the package by hand from what is already settled, use it while building
everything else, and write `tasks/AGENTS.md` last as a codification of what actually
happened. Where the codified rule differs from what felt natural, that difference is a
finding.

## Steps

1. **Task package** — `task.md`, `context.md`, `plan.md`. Done first, by hand.
2. **`.agents/AGENTS.md`** — the layer contract. Stable rules only; no project state, no
   current task information.
3. **Project layer** — `README.md` and root `AGENTS.md`. Written before the ADRs so the
   deletion test has something to pass against.
4. **`decisions/`** — `.adr-template.md`, index `README.md`, and records `0000`–`0007`.
5. **`tasks/AGENTS.md`, `archive/AGENTS.md`, `INDEX.md`** — codified last.
6. **Verify** — run all five acceptance criteria.
7. **Close** — final `Status` and `Outcome`, archive to
   `.agents/tasks/archive/{YYYY-MM-DD}-bootstrap-tasks-layer/`, update `INDEX.md`, run the
   final exact-head check, open the pull request.

## Guard

The failure mode is writing elegantly about context-fold instead of building it. If a section
wants a third round of wordsmithing, ship it and record the dissatisfaction as a problem.
