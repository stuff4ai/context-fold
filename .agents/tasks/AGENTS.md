# AGENTS.md — tasks

How to run work in this repository.

These rules are the same in every installation of the layer. They carry no project-specific
paths, names, or decisions.

## Finding work

Start at [`INDEX.md`](INDEX.md). It is a derived view — each task's `task.md` owns its
canonical status. If they disagree, `task.md` is right and the index needs repair.

The archive is listed newest first: it only grows, so the most recent work belongs at the top
where it is read. Active tasks are listed by slug, in no meaningful order.

Each section is a table of task, status, and a one-line objective. A section with nothing in it
says `None.` instead:

```markdown
## Active

| Task | Status | Objective |
| --- | --- | --- |
| [{slug}]({slug}/task.md) | active | What the task is for |

## Archive

| Task | Status | Objective |
| --- | --- | --- |
| [{YYYY-MM-DD-HHMM}-{slug}](archive/{YYYY-MM-DD-HHMM}-{slug}/task.md) | completed | ... |
```

## Starting a task

Create `.agents/tasks/{slug}/` with a descriptive slug: `add-retry-to-uploads`, not
`TASK-042`. Once work starts, the slug is fixed identity. Do not rename it because the wording
improved — the title inside `task.md` can change instead.

Write `task.md` and `context.md` before starting the work, not after.

## The files

**`task.md`** — the contract.

Sections while active: Status, Objective, Why, Scope, Out of scope, Acceptance, Problems.

Keep it short. No context dumps, no execution history. Acceptance criteria must be checkable
by someone who was not present for the work.

**`context.md`** — the curated context map.

References to the project artifacts that matter and why, plus task-local facts. Prefer a
reference over a copy; a copy drifts. Optional sections: Assumptions, Open questions, Context
conflicts, Base state, Not relevant.

Write references as paths from the repository root, in code spans, not as relative links. The
package moves when it is archived — one directory deeper — so a relative link either breaks or,
worse, keeps resolving and points at a different file.

Open questions are recorded, not resolved. A question that must be answered to proceed is
work, not context.

Only task-local questions belong here — things unresolved while this task runs, and settled or
irrelevant once it ends. A question that will outlive the task belongs in the project layer,
where it stays visible after this package is archived.

**`plan.md`** — execution strategy. Optional.

Create it when the task is multi-step, complex, long-running, or likely to be resumed by
another agent. Keep it mutable and short. It is not an execution log.

## Recording problems

Append to `## Problems` in `task.md` **while working**, not at the end. A few lines per entry:
what happened, what was assumed, what was actually true.

Worth recording: an incorrect assumption, missing or misleading context, an ambiguous
requirement, a command or tool that behaved unexpectedly, a workaround, a mistake made twice.

Not worth recording: routine steps that went as expected.

An empty problem log at the end of a real task means the capture failed, not that the work
went well.

## Status

`task.md` carries one of four values:

| Status | Meaning |
| --- | --- |
| `planned` | Written down, not started |
| `active` | Being worked on |
| `completed` | Finished and archived |
| `cancelled` | Abandoned and archived |

Status is not the same as stage. The stages below describe how work moves; only the four
values above appear in a file.

## Stages

```
planned → active → work → verification → review → approved
        → fold outcomes → archive → final check → merge
```

Cancelled work skips to archive.

The sequence is the order stages come in, not a path travelled once. Go back whenever review,
verification, or something you find requires it — that is the normal shape of the work, not a
deviation, and it needs no explanation. Returning changes no `Status`: the task stays `active`
until it is archived, however many times it moves.

What the order does constrain is what must happen before what. Verification precedes review;
archival follows approval and precedes acceptance.

*Review*, *approved*, and *merge* mean whatever this project's own workflow defines them to
mean. The rule is only that a change is archived before it is accepted, not that acceptance
happens through any particular mechanism.

A task is not complete when the coding is done. It is complete when acceptance is satisfied,
durable outcomes have been folded into the project layer, review has happened, and the
repository is in a coherent accepted state.

**Fold outcomes** is the stage most easily skipped and the most costly to skip. Anything a
human would need that currently exists only inside the task package must be moved into the
project's own artifacts — documentation, a decision record, the code — before archival.
Whatever is left behind is lost.

## Finishing

1. Set the final Status and add an Outcome to `task.md`: what happened, and which durable
   artifacts it produced.
2. Move the directory to `.agents/tasks/archive/{YYYY-MM-DD-HHMM}-{slug}/`, timed to the
   minute it left active state.
3. Update `INDEX.md`.
4. Run the final exact-head check.
5. Submit the change for acceptance. Archival happens *before* the change is accepted, so
   that what is accepted contains both the work and the record of the work.

## Final exact-head check

At the branch head, confirm all four:

1. Each acceptance criterion in `task.md` is satisfied.
2. No durable outcome exists only inside the layer — remove it mentally and see what is lost.
3. The task directory is under `archive/` with final Status and Outcome set.
4. `INDEX.md` matches the directories on disk.

## Index conflicts

`INDEX.md` is one file that every concurrent task touches, so conflicts are normal. Do not
resolve them by hand — rebuild the affected rows from the task directories, sorting archived
tasks by directory name descending and active tasks ascending.
