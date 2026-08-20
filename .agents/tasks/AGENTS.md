<!-- agent-layer:begin -->

<!--
Managed rule block. Updates replace everything between the agent-layer markers.
Do not edit this block. Add only non-conflicting project instructions after the end marker.
-->

# AGENTS.md — tasks

How to run work in this repository.

This managed rule block is the same in every installation of the layer. It carries no
project-specific paths, names, or decisions. An adopting project may append non-conflicting
instructions after the end marker.

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
other tasks* above. `## Approval`, who satisfies review and approval when it is not the
project's default — see *Who approves* below.

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

**`rfc.md`** — proposal discussion. Optional.

Create it when a direction needs discussion before execution: a current proposal, alternatives,
task-local open questions, or review feedback. Curate it; do not store a raw transcript, source
notes, hidden reasoning, or an execution log. Like `context.md`, it is not a durable home: fold any
question or outcome that may outlive the task into the project layer before completion or
cancellation.

Its body is free-form, but it starts with exactly three frontmatter lines: `---`, then
`status: draft` or `status: resolved`, then `---`. A draft has no `## Resolution`; a resolved RFC
has exactly one non-empty Resolution stating the selected direction.

Drafting an initial RFC does not start a `planned` task. Substantive discussion, review, or evidence
gathering does, so change the task to `active` then. Implementation waits until the RFC is resolved
and `task.md` agrees with it.

To reopen a resolved RFC, first fold anything still relevant out of its Resolution and plan. Then
change it to `draft`, remove the Resolution, record why in the RFC, remove `plan.md`, and pause
implementation. A new Resolution is required before returning to `resolved`.

**`plan.md`** — selected execution strategy. Optional.

Create it when the task is multi-step, complex, long-running, or likely to be resumed by
another agent. When an RFC exists, create or keep the plan only while the RFC is resolved, and make
its direction agree with the Resolution and `task.md`. Tactical steps stay mutable. It is not an
execution log or durable project authority.

An optional heading you have nothing to put under yet is left out, not kept empty. An active
task may still fill one in before it is done; one still empty at archival was declared and never
used, and a mechanical check treats it that way.

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
| `planned` | Written down; substantive work not started |
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

An unresolved RFC pauses implementation, not the task lifecycle. A task becomes `active` when its
RFC receives substantive discussion, review, or evidence gathering, and stays active if a resolved
RFC is later reopened.

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

## Who approves

A task's `## Approval` says who satisfies review and approval. Two values:

**Human** — the project's default, and what applies when a task carries no `## Approval` at
all. Whatever this project's own workflow defines as review and approval, a human is the one
who gives it.

**Verifier** — a fresh verifier's `CONFIRMED` verdict against this task's own acceptance criteria
satisfies review and approval instead. Fresh means a different agent from whoever did the
work, with no memory of doing it — the standard a check needs to be evidence rather than a
verdict, applied by someone other than the author. A self-run check, however thorough, is
never this.

Declare it when the task is written, alongside `## Scope` — not partway through the work, and
not by the agent doing the work deciding, once it is underway, that it would rather not wait. A
task that changes its own approval mode mid-flight is exempting itself from the thing that
would have caught the change.

Two kinds of task need a human regardless of a project's stated default. A task whose scope is
the approval mechanism itself — what these values mean, who may set them, what a verifier's
confirmation is worth — cannot authorize its own bypass. And a task whose acceptance criteria
leave a real, undecided choice for whoever reviews it, not a claim to check but a direction to
pick, needs a chooser rather than a checker: a verifier confirms or refutes a claim, and has
nothing to return against an open question.

Everything else is a judgment call for whoever writes the task, the same as `## Scope` and
`## Blocked by` already are.

## Finishing

Before finishing a task with an RFC, fold every question and outcome that may outlive it into the
project layer. A completed task's RFC is resolved. A cancelled task's RFC may remain draft when
abandonment ended discussion without selecting a direction.

1. Set the final Status and add an Outcome to `task.md`: what happened, and which durable
   artifacts it produced.
2. Move the directory to `.agents/tasks/archive/{YYYY-MM-DD-HHMM}-{slug}/`, timed to the
   minute it left active state.
3. Update `INDEX.md`.
4. Run the final exact-head check.
5. Submit the change for review, and stop until it is given — see *Who approves* for what
   gives it. What a reviewer sees is now the whole change: the work, the record of the work,
   and the repository in the state that merging would accept.
6. Merge once approved.

## Final exact-head check

At the finished state of the change, produce the evidence for all four — not a verdict, the
evidence itself, in a form someone other than you could read and judge:

1. Each acceptance criterion in `task.md` is satisfied.
2. No durable outcome exists only inside the layer — remove it mentally and see what is lost.
3. The task directory is under `archive/` with final Status and Outcome set.
4. `INDEX.md` matches the directories on disk.

Running this check does not mean the change is accepted. It means the change is ready to be
looked at by someone who did not write it — review, next in the sequence, is where that happens.
A pass here is necessary and never sufficient, whoever runs it: the person closest to a claim is
the worst-placed to test it, which is true of this check for exactly the reason it is true of the
work itself.

The first two are judgment about what this task itself claims. No script settles whether an
acceptance criterion is met or whether something durable was left only in the layer — reading the
diff against the claim is the check, and doing that once, as the person who already believes the
claim, is weak evidence. It is what a second reader needs, not a substitute for one.

The last two are facts about the repository as it stands, and facts can be checked plainly: a
path either is or is not under `archive/`; a table either does or does not match a directory
listing. Read the actual content — the file, the table — not a count or a summary that reports
success regardless of what the content says. A check whose verdict cannot disagree with its own
evidence is not a check: if nothing you could observe would make it report failure, it is not
testing the thing it claims to.

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
<!-- agent-layer:end -->

## Handing work to another agent stack

*This section is this project's own, not part of the portable layer. See
[`decisions/0036-record-cross-stack-handoff.md`](../../decisions/0036-record-cross-stack-handoff.md).*

More than one agent stack may work this repository — different products, each with its own
roles and its own lead session. They coordinate through the package rather than through a live
channel between them, so that what one asked and what another answered stays readable in the
change afterwards.

A task that needs this carries `handoff.md`. An entry opens with a fenced `yaml` block carrying
`id`, `from`, `to`, `state`, `rev` and `returns`, then a `### Request` section and a `### Return`
section. The header is fenced rather than document frontmatter because the file holds many
entries.

An entry is not rewritten once it is dispatched. Its request text is fixed at that moment, and
answering it changes only `state:` and fills `### Return`. A new exchange is a new entry; nothing
edits an earlier one. Correcting the record is the one exception: a fact that turns out to be
wrong is corrected by adding to the entry, marked as added afterwards, never by replacing what it
corrects.

- **Address by role, never by model.** `to:` names a stack and one of the roles that stack
  already has. The role's own definition decides what it runs as, so an address naming a model
  would assert something it does not own.
- **An entry addressed elsewhere is not yours.** `state: requested` plus your stack in `to:` is
  the whole inbox rule. Do not answer, amend, or act on any other entry.
- **Answer in the vocabulary the request names.** `returns:` says what shape the reply takes. A
  request for a review is answered and returned, not continued into the work it reviewed — the
  asking stack decides what to do with a verdict.
- **Commit the request, then dispatch it.** `rev:` names the commit under review — what the
  verdict will be about. A request read from an uncommitted working tree cannot be shown
  afterwards to be what was actually asked, so the entry is committed too, necessarily in a
  later commit than `rev:`: an entry cannot name the commit that contains it, because writing
  the hash in would change it. Both guarantees hold anyway, since the entry's own commit is in
  the history. Where the tree at dispatch differs from `rev:` in anything but the entry, the
  request says what and why.
- **Stop after asking.** Writing a request ends your turn. Nothing in the repository delivers
  it; something outside does.

Only a lead session writes or answers a handoff. A role dispatched by a lead does that work and
reports back to that lead — asking another stack is not among the things it was given to do.

Whether this belongs in the portable layer is
[an open question](../../OPEN-QUESTIONS.md), deferred until the convention has been used.
