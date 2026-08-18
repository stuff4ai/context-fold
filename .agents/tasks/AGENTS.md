# AGENTS.md — tasks

How to run work in this repository.

These rules are the same in every installation of the layer. They carry no project-specific
paths, names, or decisions.

## Finding work

Start at `INDEX.md`, beside this file. It is a derived view: each task's `task.md` owns its
status and the index restates it for navigation.

When they disagree, one of them is stale, and the task's own directory says which. A package
under `archive/` is finished whatever `task.md` still says; a package that is not under
`archive/` is unfinished whatever the index says. Repair the file the directory contradicts.

Then check the rest of finishing. It writes an Outcome, sets the Status, moves the package and
updates the index, and a disagreement means that did not happen cleanly — a step can be skipped
as easily as a sequence can be cut short, so do not assume the steps either side of the one that
failed are sound. If the work is genuinely done and the package was never moved, complete the
archival; the statuses follow from it.

Where the directory cannot settle it — an archived task the two call `completed` and `cancelled`
— `task.md` is right and the index needs repair.

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
`TASK-042`. The slug becomes fixed identity when the change is accepted — the same point at
which the package stops being writable — and after that it does not change, because other things
reference it. Before then, rename it only if the work turned out to be something else. Improved
wording is not a reason; the title inside `task.md` absorbs that.

Write `task.md` and `context.md` before starting the work, not after.

Add the task to `INDEX.md` under Active as soon as the directory exists. The index is a derived
view of what is on disk, so a task missing from it makes the index wrong from the moment the
task begins — not at the end, when it is updated again on archival.

## Working alongside other tasks

More than one task can be open at once. Before starting, read the other active ones: their
`task.md` says what they are touching, and yours has to fit around it.

**Scope is declared by section, not only by file.** Two tasks may hold the same file when they
hold different parts of it, and that is the ordinary case rather than an exception. Name the
sections in `## Scope` when a file is shared, so the boundary is written down instead of assumed.
Where two tasks genuinely need the same section, one of them owns it and the other says so in
`## Out of scope`.

**A task that cannot start yet says why.** Add `## Blocked by` to `task.md`, listing what it is
waiting for and what it needs from each. Its status stays `planned`: blocked is not what a task
*is*, it is what the task is waiting for, and the four values describe the first. Do not start a
task whose blockers are unmet — clear them, or change the task until it no longer needs them.

**A finding still belongs to the task whose work produced it**, as it always did. With one task
open that was a tautology; with several it is a judgement. Recording an observation where you
happen to be is how it ends up archived under work it has nothing to do with.

## The files

**`task.md`** — the contract.

Sections while active: Status, Objective, Why, Scope, Out of scope, Acceptance, Problems.

A `planned` task carries the same sections without Problems. That section records friction met
while doing the work, so it opens when the work does.

Optional: `## Blocked by`, when the task is waiting on other work — see *Working alongside
other tasks* above.

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

If the project has no place for such questions, say so and ask for one. Leaving it here buries
it: this package is archived when the task ends, and once the change is accepted it is history
rather than current state. A `planned` task can hold the question while a destination is
established, but it is not the destination — see the triage rule below.

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

## When a finding has no owning task

A finding belongs to the task whose work produced it, and that task stays writable until the
change is accepted. Archiving moves the package; it does not seal it. So something learned while
merging goes in `## Problems` of the task being merged, even though its directory is already
under `archive/`.

Past acceptance the task is history, and editing it would rewrite the record of an accepted
change. Do not carry the finding to whatever comes next in your head either.

A finding with no writable owning task — because its task was accepted, or because no task owns
it — is triaged by two questions. They are independent, and both can be yes.

**Would removing the layer lose durable project knowledge — something that must stay true or
visible even if no follow-up work is ever done?** Then it belongs in the project's own artifacts:
a documented uncertainty, a constraint, a fact about how the project works. The layer is removable
by design, so nothing kept only inside it survives, and a task later archived or cancelled is not
a reliable place to preserve durable knowledge.

If the project has no artifact for it, say so rather than settling for somewhere convenient. Open
a `planned` task to establish a destination and coordinate moving the knowledge there. The task
is operational state, not its home: it cannot be completed or cancelled until the knowledge has
been folded out into the project layer.

**Does the finding call for investigation, a decision, or a change?** Then open a `planned` task
for that work. `Why` carries the self-contained account — what happened, what was assumed, what
was actually true — rather than a quotation of wherever you first wrote it, which may depend on
context this task does not carry. `context.md` carries the provenance: where the evidence is and
what it references.

"Should the project support X?" is both — knowledge a reader needs and a decision someone must
make. Record it, then plan it. If neither answer is yes, the finding had no reader and no
consequence, and did not need keeping.

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
planned → active → work → verification → fold outcomes
        → archive → final check → review → approved → merge
```

Cancelled work skips to archive — but not past **fold outcomes**. A task abandoned halfway may
still have learned something the project needs, and archiving it without folding that out loses
it exactly as completion would.

The sequence is the order stages come in, not a path travelled once. Go back whenever review,
verification, or something you find requires it — that is the normal shape of the work, not a
deviation, and it needs no explanation. Returning changes no `Status`: the task stays `active`
until it is archived, however many times it moves.

What the order does constrain is what must happen before what. Verification precedes review,
and archival precedes both. Everything a reviewer must judge — the work, the Outcome, what was
folded out, the archived package, the index — exists before anyone is asked to approve it.
Approval authorizes the merge and nothing else, because nothing else is left.

Do not ask for approval earlier. Work approved before the Outcome is written is work approved on
a promise, and the Outcome is the one thing in the change that no check can read.

*Review*, *approved*, and *merge* mean whatever this project's own workflow defines them to
mean. The rule is only that a change is archived before it is reviewed, and reviewed before it
is accepted, not that acceptance happens through any particular mechanism.

A task is not complete when the coding is done. It is complete when acceptance is satisfied,
durable outcomes have been folded into the project layer, and the package is archived. All of
that happens before review, so what is approved is the finished state rather than a promise of
one.

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
5. Submit the change for review, and stop. What a reviewer sees is now the whole change: the
   work, the record of the work, and the repository in the state that merging would accept.
6. Merge once approved.

## Final exact-head check

At the finished state of the change, confirm all four:

1. Each acceptance criterion in `task.md` is satisfied.
2. No durable outcome exists only inside the layer — remove it mentally and see what is lost.
3. The task directory is under `archive/` with final Status and Outcome set.
4. `INDEX.md` matches the directories on disk.

## Conflicts

Files that every task touches will conflict, and how to resolve one depends on what kind of file
it is.

A **derived** file restates what is already true somewhere else. Do not merge it by hand: rebuild
it from its sources and the conflict is gone. `INDEX.md` is one — rebuild the affected rows from
the task directories, sorting archived tasks by directory name descending and active tasks
ascending. Rebuilding copies each `task.md`'s status, so settle any disagreement first;
regenerating from a stale task file produces an index that agrees with it and is wrong twice.

An **authored** file says something no other file says. Merge it like any other prose — read both
sides and write what is true of both. Nothing can regenerate it, so a conflict resolved carelessly
loses content and nothing will say so.

If you cannot tell which a file is, ask what deleting it would cost. A derived file can be built
again from what remains; an authored one is gone.
