# Route findings without an owning task

## Status

completed

## Objective

Give a finding somewhere to go when it has no owning task, using the `planned` status that
already exists and has never been used.

## Why

The loop captures friction in the task's `## Problems` section, and that is the only destination
the rules name. Learning that arrives with no task to hold it has none.

Part of that gap was self-inflicted. The rules read as though archival sealed the package, so
anything found while merging looked orphaned — but `0007` says the opposite: an archived package
is amended when review requires it, and immutability starts at merge. Those findings had an
owning task the whole time.

The rest is real. Once a change is accepted, editing its task rewrites merged history. Three
findings arrived there and reached a home only because a person carried them or a fix happened to
need a task.

`planned` means "written down, not started". It was defined in the first task and has not been
used since, across fifteen. A finding that names work fits it exactly: the task lives in `tasks/`,
which every installation has, and appears in the index, so the work is visible rather than held
in someone's memory.

What a planned task cannot be is a home for knowledge. The layer is removable by design, and the
task is archived or cancelled eventually, so anything that must outlive it has to reach the
project's own artifacts. Where a project has no artifact for it, a planned task can hold the
finding while one is established — with folding out as the condition for closing the task, not an
intention. The two questions stay independent: a finding can be both, and "should the project
support X?" is.

## Scope

- `templates/agents/tasks/AGENTS.md` — which findings still have an owning task, how the rest are
  triaged, what a planned task looks like when it holds one, and when a slug fixes.
- `decisions/0022-route-findings-without-an-owning-task.md` and the index row.
- `decisions/0006-task-package-model.md` — Status only, to record what `0022` narrows.
- `OPEN-QUESTIONS.md` — remove the entry this closes, and correct the supersession entry's
  evidence, which this change adds a sixth instance to.
- One real finding, parked as a planned task, to demonstrate it.

## Out of scope

- Findings during a task. Those go in that task's `## Problems`, which works.
- Renaming the index's Active section, which would now list planned tasks too.
- Any change to `0007`, `0010`, or `0013`.

## Acceptance

1. The rules say a finding belongs to its task until the change is accepted, matching `0007` on
   when a package stops being writable, so archival alone does not orphan it.
2. The rules triage a finding with no *writable* owning task by two independent questions —
   whether removing the layer would lose durable project knowledge, and whether there is work to
   do — and both answers may be yes.
3. Durable knowledge with no project artifact to hold it gets the gap named and a planned task to
   establish one, which cannot be completed or cancelled until the knowledge is folded out.
4. A real finding that names work is parked as a planned task, and the checks accept it —
   `planned` status, no Outcome, listed in the index. Its self-contained account is in `Why` and
   its provenance in `context.md`, with no `## Problems` until the work starts.
5. `0006` records both narrowings in its Status and nowhere else: `## Problems` is required only
   of tasks that have started, and slug identity fixes at acceptance rather than at the start of
   work.
6. This task's slug, its decision record's filename, and its branch all name the design that
   shipped rather than the one review rejected.
7. Cancelling a task no longer skips folding durable outcomes out of it.
8. The `OPEN-QUESTIONS.md` entry this closes is removed.

## Outcome

A finding now belongs to the task whose work produced it for as long as that task is writable,
which is until the change is accepted rather than until the package moves under `archive/`. Most
of the gap this task set out to close did not exist: `0007` had always allowed an archived
package to be amended before merge, and three versions of the fix were built on the opposite
premise before a reviewer checked it.

What remained is triage. A finding with no writable owning task is routed by two independent
questions — whether removing the layer would lose durable project knowledge, and whether there
is investigation, a decision or a change to make. Both may be yes. Knowledge goes to the
project's own artifacts; where a project has none, the gap is named and a `planned` task
coordinates moving it there, and that task cannot be completed or cancelled until it has.

Durable artifacts:

- `decisions/0022-route-findings-without-an-owning-task.md` — the decision.
- `decisions/0006-task-package-model.md` — Status narrowed twice: `## Problems` is required only
  of tasks that have started, and slug identity fixes at acceptance rather than at the start of
  work.
- `skills/ctxfold-init/templates/agents/tasks/AGENTS.md` — the portable rule, plus two fixes
  older than this task: cancelled work no longer skips **fold outcomes**, and the slug rule.
- `OPEN-QUESTIONS.md` — the post-archival entry removed; three structural gaps added (the
  unenforced wrap width, unchecked citations, the pull request description no check can see);
  the supersession entry corrected from one instance to six; the twin-stranding pattern
  recounted from seven to around eighteen.
- `.agents/tasks/decide-whether-the-task-template-earns-its-place/` — the first `planned` task
  in this project, demonstrating the shape: account in `Why`, provenance in `context.md`, no
  `## Problems` until the work starts.

`planned` was defined in the first task and unused across fifteen. It now has a defined purpose
and one instance.

Six review rounds. The design was settled after three; the rest was names and stranded
statements, which is where this project's defects live.

## Problems

### The fix routed project knowledge into the layer the deletion test forbids

The first version sent any outliving question to a `planned` task when the project had no place
for one.
Assumed: a planned task is a safe destination because every installation has `tasks/`.
Actually: it is inside `.agents/`, which is removable by design, so a question humans need would
go with it. And a planned task is archived or cancelled eventually, which buries it exactly as
the package it was rescued from would have. The repair recreated the failure it was fixing, one
level up, and broke the layer's own central rule doing it.
Found in review. Nothing in the checks reads a new rule against the deletion test.

### A record argued against its own decision, again

`0022` listed among its consequences that the rule "will produce tasks nobody intends to start",
and shipped anyway.
Assumed: naming a cost is how a record stays honest.
Actually: a cost that defeats the purpose is not a cost, it is a refutation. This exact tell was
identified earlier in this project and written down as a reusable check — a record whose
Consequences argue for the alternative is rationalizing rather than deciding. I wrote that check
and then failed it.
Second instance, and it says something about checks that live only in prose: nothing makes them
fire. The first time it was caught by a reviewer, and so was this.

### One statement changed, its twins left behind

The rule gained a fallback in `tasks/AGENTS.md`; the shipped task template kept the old sentence,
so an adopter would get opposite instructions depending on which file it read. Scope and context
still said two `OPEN-QUESTIONS.md` entries would be removed after the criterion was corrected to
one.
Both found in review. Roughly the fifteenth instance in this project, and the second within a
single task — the criterion was fixed and the scope describing it was not.

Then a third, in the next round: the rule and `0022` were rewritten around triage, and this
task's own Why and `context.md` were left arguing the rejected design — that the project-layer
route had failed and a planned task was the fallback. The contract contradicted the thing it had
produced. A reviewer found it; nothing else would have. Narrowing the rule again in the same
round stranded an acceptance criterion, which still described the two routes as a distinction to
draw rather than two questions to ask.

### Cancelling a task skips folding, and always has

Reviewing this change surfaced a defect older than it: `tasks/AGENTS.md` says cancelled work
skips to archive, and the stage it skips past includes **fold outcomes**. A task abandoned
halfway loses whatever durable thing it learned, by rule.
Assumed: cancellation means the work did not produce anything worth keeping.
Actually: it means the work was not finished. Those are different, and the second one still
learns things.
Fixed here because it is the same failure this task addresses — durable content with nowhere to
go — arriving from the other end of the lifecycle.

### The two routes were written as a choice, and the real cases are both

The triage rule said where a finding goes "depends on what it is", then described work and
knowledge as if picking one.
Assumed: a finding is either something to do or something to know.
Actually: the common case is both. "Should the project support X?" is a question a reader needs
and a decision someone must make, and an exclusive rule forces half of it to be dropped —
silently, and with no way to tell which half. Rewritten as two independent tests, either or both
of which can be yes.
Found in review. The exclusive framing came from the previous round's fix, which was itself a
narrowing of an over-broad rule: correcting too far in one direction produced the opposite defect
rather than the middle.

### The record cited a decision that does not say what it was cited for

`0022` attributed "does not prescribe another project's layout" to `0011`, which is about vendor
neutrality. `0005` is where the layer's boundary actually says it.
Assumed: a plausible-sounding citation to a record I had read is a checked one.
Actually: it was chosen from memory of what the records are broadly about. A wrong citation is
worse than none — it sends a reader to a record that will not confirm the claim, and it makes the
claim look supported to anyone who does not follow it.
Found in review. No check reads citations for relevance; only the link target's existence is
verified, and that passed.

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

### The rule invented an immutability the records deny

Every version of this fix so far opened with the same premise: a finding produced while merging
arrives after archival, and archived packages cannot be edited.
Assumed: archival seals a package. It is the last stage before merge, the directory moves, and
the rules call archived tasks history.
Actually: `0007` says an archived package is amended if review requires it, and that immutability
applies from merge onward. It says so in its own Consequences. The premise was contradicted by
the record the task cites as its motivation, and I read that record while writing the task.
So most of the gap did not exist: a finding from merging has an owning task and belongs in it.
What survives is the case after acceptance. The mechanism is still needed, for less.
Found in review, three rounds in. Two reviewers and I all reasoned from the wrong boundary.

### The finding was filed under Problems, which means something else

The rule put the observation that caused a planned task into that task's `## Problems`.
Assumed: `## Problems` is where findings go, so a finding that becomes a task goes in the new
task's.
Actually: `0013` defines it as friction met *while working on that task*. A planned task has not
started, so its problem log describing work that has not happened redefines the section — and
duplicates `Why` and `context.md`, which already carry the reason and the provenance.
The demonstration task had the same shape and has been rewritten.

### "The layer is removable" became ".agents/ is removable"

Two paragraphs written this round said `.agents/` is removable by design.
Assumed: they are the same thing, since that is where the layer lives.
Actually: `0018` says `.agents/` is where the layer lives, not what it is — other tools write
there and their files are not ours to remove. The deletion test is about the layer. Saying the
directory is removable authorises deleting someone else's data, which is the exact failure an
adoption run hit in a real repository.
Found in review. A distinction the project made deliberately, lost by paraphrase in new prose.

### The record was named after the design that was rejected

`0022` was still titled "Record findings as planned tasks" after review narrowed it to triage,
where only actionable findings become tasks.
Assumed: the title is a label, and the body carries the decision.
Actually: the title is what the index shows and what anyone scanning the records reads. It
advertised the version that had been argued out of the record two rounds earlier.
Renamed to describe the rule. Renaming a record is normally forbidden; this one has not merged,
and `0007` puts immutability at merge, which is the same boundary this task just got wrong.

### Narrowing a rule left the record that states it untouched

Dropping `## Problems` from a planned task contradicted `0006`, which requires the section of
every `task.md`.
Assumed: changing the portable rules and writing a new record covers the change.
Actually: the old record still said the old thing, and nothing reconciled them. A reader
following `0006` would have restored the section the new rule removes.
Found in review. This is the same failure as the immutability premise from the round before —
a new rule written without checking the record it overrides — and the second time in this task
that the fix contradicted an existing decision. Both were caught by a reviewer; the checks read
structure and links, not claims.
Recorded in `0006`'s Status as a partial supersession, which is the pattern four other records
already use and which `OPEN-QUESTIONS.md` still lists as invented rather than derived from
`0000`.

### Three names outlived the design that produced them

The rule was narrowed to triage in one round and rewritten around owning tasks in the next, and
after both the decision record was still called `0022-record-findings-as-planned-tasks`, the
branch `feat/record-findings-as-planned-tasks`, and the task directory the same.
Assumed: names are labels, and correcting the body is correcting the artifact.
Actually: the record filename is what the decisions index shows, the branch is what the pull
request advertises, and the slug is what the archive will carry forever. All three named the
design the work had rejected. Each was found by a reviewer, one round apart, because fixing one
did not prompt anyone to look at the others.
Renaming the record was easy: it had not merged. Renaming the branch closed the pull request —
GitHub retargets open pull requests on a branch rename, but the API rename dropped this one, so
the work continues under a new number with the commits intact. Renaming the slug required
narrowing `0006`, which fixed identity at the start of work.
The rule now fixes all three at acceptance, which is where `0007` already put immutability. One
rule was stricter than the others and nothing had said why.

### An open question cited one instance of a pattern that had six

`OPEN-QUESTIONS.md` said partial supersession was invented for `0009` superseding part of
`0007`. Verifying that `0006`'s Status edit was legitimate turned up `0001`, `0005`, `0007`,
`0012` and `0018` all doing the same thing, with `0006` making six.
Assumed: an entry written when a pattern was first seen stays accurate as the pattern recurs.
Actually: nothing revisits it. The entry read as a one-off curiosity when it is the normal way
records are amended here — consistent by imitation, which is not the same as decided. The
difference matters for whether the gap is worth closing.
Found while checking a reviewer's question about whether the record format permits this at all.
It does: `0000` names `Status` as the one exception to immutability. The mechanism was never in
doubt; the wording around it is what nothing defines.

### The pull request description is a twin, and nothing checks it

The absolute claim about cancellation burying knowledge was softened in the rules and in `0022`
and left standing in the pull request description.
Assumed: fixing the repository fixes the change.
Actually: the description is what reviewers read first, and it is the one surface no check
covers. `test_relative_links_resolve` and the identity checks stop at tracked files; the body of
the pull request is outside the repository and outside CI.
Found in review, one round after the same sentence was fixed everywhere a check could see it.
Roughly the eighteenth instance of one statement changing while its twins did not, and the first
where the stranded twin was outside the repository.

### Rewriting prose by string substitution left lines twice the wrap width

Three replacements this task joined sentences without rewrapping, leaving lines of 141, 105 and
109 characters where the files wrap near 98.
Assumed: the linter enforces what the files visibly do.
Actually: `pymarkdown`'s line-length rule is off, so nothing failed. The convention is real —
every hand-written line honours it — and entirely unenforced, which is why three violations
shipped through four green runs.
Found in review. `templates/agents/AGENTS.md:35` has been 165 characters since before this task
and no check or reviewer has ever caught it, which is the same gap seen from the other side.
