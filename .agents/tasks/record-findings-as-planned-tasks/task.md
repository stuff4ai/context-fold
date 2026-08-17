# Record findings as planned tasks

## Status

active

## Objective

Give a finding somewhere to go when no task is open, using the `planned` status that already
exists and has never been used.

## Why

The loop captures friction in the task's `## Problems` section. That is the only destination the
rules name, so learning that happens with no task open has none — and merging, the last stage,
produces exactly that. Three findings have arrived after archival and reached a home only because
a person carried them or a fix happened to need a task.

The obvious repair — "put it in the project layer" — is the sentence that already failed. A
foreign run was told an outliving question belongs there, found no such place in its repository,
and filed it into a package that gets archived.

A planned task needs no project layer. It lives in `tasks/`, which every installation has, and
appears in the index, so the finding is visible rather than buried.

`planned` means "written down, not started". It was defined in the first task and has not been
used since, across fifteen tasks. This is what it was for.

## Scope

- `templates/agents/tasks/AGENTS.md` — where a finding goes when no task is open, and what a
  planned task looks like when it holds one.
- `decisions/0022-record-findings-as-planned-tasks.md` and the index row.
- `OPEN-QUESTIONS.md` — remove the two entries this closes.
- One real finding, parked as a planned task, to demonstrate it.

## Out of scope

- Findings during a task. Those go in that task's `## Problems`, which works.
- Renaming the index's Active section, which would now list planned tasks too.
- Any change to `0007`, `0010`, or `0013`.

## Acceptance

1. The rules say where a finding goes when no task is open, and where an outliving question goes
   when the project has no place for one.
2. A planned task holding a finding is described: the finding in `## Problems`, the Objective
   being the question to resolve.
3. A real finding from this session is parked as a planned task, and the checks accept it —
   `planned` status, no Outcome, listed in the index.
4. The `OPEN-QUESTIONS.md` entry this closes is removed.

## Problems

### The second finding this task fixes had never been recorded

Acceptance said two `OPEN-QUESTIONS.md` entries would be removed: the post-archival gap, and the
one about the rules pointing outliving questions at a project layer an adopter has not got.
Only the first existed.
Assumed: a finding discussed at length across two adoption runs, and named repeatedly as an open
item, was written down somewhere.
Actually: it was named in conversation and never recorded. It survived only in the transcript,
and was noticed here solely because a criterion assumed otherwise.
This is the failure this task exists to fix, in its plainest form — a finding that arrived with
no task open, and went nowhere. That it happened while writing the fix, to the person writing it,
says the mechanism was needed rather than that someone was careless.
The criterion was corrected to describe one entry. A scope correction, not a criterion bent to
match a result: the second entry was never in scope because it was never there.
