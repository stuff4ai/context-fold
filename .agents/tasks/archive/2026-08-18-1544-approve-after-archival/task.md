# Approve after archival, not before

## Status

completed

## Objective

Move the approval gate to after the final exact-head check, so that what a human approves is what
merges.

## Why

`0007` puts approval before folding and archival, and `0019` makes that approval authorize
everything downstream. So the Outcome, the folded durable knowledge, the archival move and the
index update all reach `main` without anyone reading them. CI checks their structure — status
set, index matches disk, links resolve — and structure was never the risk. The Outcome is prose,
and prose is the one thing no check reads.

This is not a trade-off to weigh. `0007` already contradicts itself: two of its five Consequences
describe review happening *after* archival, while its Decision orders approval before. The
Consequences say what was intended, and the ordering sentence is the defect.

> Review sees the final state, including the Outcome, rather than approving work and trusting
> that filing happens later.
>
> If review requests changes after archival, the archived package must be amended before merge.

The portable rules carry the same split. `## Stages` orders `review → approved → fold outcomes
→ archive`, while `## Finishing` lists submission for acceptance as step 5, *after* archival.
One file, two answers.

Sixteen merges have gone through the early gate. The seventeenth was
`route-findings-without-an-owning-task`, where the Outcome and four promotions into
`OPEN-QUESTIONS.md` were written after approval and merged unread.

## Scope

- `decisions/0007-archive-before-merge.md` — Status only, recording what this narrows.
- `decisions/0019-agents-may-merge-after-approval.md` — Status only; approval authorizes the
  merge, not the folding and archival ahead of it.
- A new decision record for the corrected order.
- `templates/agents/tasks/AGENTS.md` — `## Stages`, `## Finishing`, and the sentence in Stages
  that says archival follows approval.
- `skills/ctxfold-init/SKILL.md` and `ADOPTING.md` — both tell an adopting agent to stop before
  archiving and ask for approval, which this inverts.
- `OPEN-QUESTIONS.md` — remove the gap entry this closes.

## Out of scope

- Whether an agent may merge at all. `0019` stands; only what its approval covers changes.
- Squash strategy, branch naming, sign-off, co-authorship.
- Making the Outcome checkable by a program. It is prose by decision, and `0012` defers tooling.
- Reviewing this project's sixteen already-merged Outcomes.

## Acceptance

1. The rules order approval after the final exact-head check, and every statement of the order
   in every artifact agrees.
2. `0007`'s two Consequences that assume post-archival review are true under the new order rather
   than contradicted by it.
3. `0019` records that approval authorizes the merge, not the work that precedes it.
4. The adoption skill and procedure tell an agent to complete archival and then ask, matching the
   rules rather than the old order.
5. A human approving a pull request built under these rules is looking at the Outcome, the
   archived package, and the updated index.
6. The `OPEN-QUESTIONS.md` entry this closes is removed.

## Outcome

Approval is now the last gate before merge. The order is work, verification, fold outcomes,
archive, index, final exact-head check, review, approve, merge. Review and approval collapsed
into one look at the final state rather than two looks at different ones.

The gap turned out not to be the trade-off `OPEN-QUESTIONS.md` recorded. `0007` had been
internally inconsistent since it was accepted: its Decision ordered approval fourth while two of
its Consequences described review happening after archival. Closing the gap satisfies `0007`
instead of contradicting it. The entry had been written from the Decision alone, which is also
how the record was cited five times without anyone noticing.

Durable artifacts:

- `decisions/0023-approve-the-final-state.md` — the decision.
- `decisions/0007-archive-before-merge.md` — Status: stage order and "approval authorizes
  archival" narrowed. Archival before merge, which is what the record is about, stands.
- `decisions/0019-agents-may-merge-after-approval.md` — Status: approval authorizes the merge
  alone.
- `decisions/0020-ship-an-init-skill.md` — Status: the skill stops before merging, not before
  archiving.
- `skills/ctxfold-init/templates/agents/tasks/AGENTS.md` — `## Stages` and `## Finishing`, which
  had disagreed with each other, now agree with each other and with `0007`'s Consequences.
- `skills/ctxfold-init/SKILL.md` and `ADOPTING.md` — an adopting agent now finishes the task and
  stops before merging.
- `README.md` — the front door no longer describes archival as following the accepted state.
- `OPEN-QUESTIONS.md` — the gap entry removed; a new one added for the class of defect that
  produced it, that nothing checks a record against itself.

This task is the first to run under the new order: everything above was written, folded and
archived before approval was requested.

## Problems

### The record contradicted itself and the contradiction was invisible for sixteen tasks

`0007`'s Decision orders approval before folding and archival. Two of its Consequences state that
review sees the final state and that an archived package is amended if review asks. Both
presuppose the opposite order.
Assumed: the gap was a trade-off between reviewing early and reviewing the whole change, which is
how `OPEN-QUESTIONS.md` recorded it — "moving approval to after archival would close this and
would contradict `0007`".
Actually: it would satisfy `0007`. The entry was written from the Decision alone; nobody read the
Consequences alongside it. The record has been internally inconsistent since it was accepted, and
the inconsistency survived being cited in five later records.
Found while scoping this task, by reading the record end to end rather than the sentence being
cited.

### The order was written in five places and two were missed by the obvious edits

Correcting `## Stages`, `## Finishing`, `SKILL.md` and `ADOPTING.md` felt like the whole change.
A sweep found two more: `README.md` told the front door that a task is archived only once the
repository is "in a coherent accepted state", and `0020` instructs the skill to stop before
archiving.
Assumed: the artifacts that state a rule are the ones that teach it.
Actually: the README is the first thing a reader meets and describes the lifecycle in prose that
matches no heading, so no search for the rule's own vocabulary reaches it. `0020` is an accepted
record whose body cannot be edited at all — it needed a Status narrowing instead, which is a
different repair than the one the other four needed.
Found by sweeping rather than by reasoning about where the rule lives, which is the only method
that has ever worked on this in this project.
