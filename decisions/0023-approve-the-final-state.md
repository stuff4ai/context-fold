# Approve the final state

## Status

Accepted

## Context

[0007](0007-archive-before-merge.md) ordered the stages as implementation, verification, review,
approval, fold outcomes, archive, index, final check, merge. Approval came fourth, and
[0019](0019-agents-may-merge-after-approval.md) made it authorize everything after it: the
folding, the archival, the final check and the merge.

So the last four steps of every task reached `main` without anyone reading them. CI checked their
structure — status set, index matching disk, links resolving — and structure was never the risk.
The Outcome is prose. What was folded out of the package and into the project's artifacts is
prose. Those are the loop's product under [0013](0013-improve-context-from-the-work.md), and they
are the only part of the change no check can read.

`0007` already said this should not happen. Two of its Consequences describe the opposite order
from its own Decision:

> Review sees the final state, including the Outcome, rather than approving work and trusting
> that filing happens later.
>
> If review requests changes after archival, the archived package must be amended before merge.

Both presuppose review after archival. The record has been internally inconsistent since it was
accepted, and was cited in five later records without anyone reading it end to end. The gap was
recorded in the project's open questions as a trade-off — closing it "would contradict `0007`" —
which is the reading that comes from the Decision alone.

The portable rules carried the same split. `## Stages` ordered approval before folding while
`## Finishing` listed submission for acceptance after archival: one file, two answers, and an
agent could satisfy either.

## Decision

Approval is the last gate before merge. The order is: work, verification, fold durable outcomes
into the project layer, archive the task, update the index, run the final exact-head check,
review, approve, merge.

Everything a reviewer must judge exists before they are asked. Approval authorizes the merge and
nothing else, because nothing else remains.

Review and approval are one gate at the final state rather than two looks at different states.
Feedback during the work is ordinary and needs no stage of its own —
[0015](0015-stages-are-not-one-way.md) already makes going back the normal shape of the work,
including going back after archival, which `0007` sanctions.

This narrows `0007`'s ordering and its sentence that approval authorizes archival. Archival
before merge, which is what `0007` is about, is unchanged. It narrows `0019` to what its title
says: an agent may merge after approval, and approval no longer reaches back over work the
reviewer has not seen.

An agent working alone therefore finishes the task completely and then stops. It does not merge.

## Consequences

What a human approves is what merges. That was the intent recorded in `0007` and it is now the
order as well.

The Outcome gets read. It is the one artifact in a task package written for someone other than
the person who wrote it, and until now nothing guaranteed a reader.

Work rejected outright after archival wastes the folding and the archival. Both are cheap — a
`git mv`, an index row, and a few paragraphs — and `0015` already treats going back as normal
rather than as a failure.

A reviewer now always sees the archival rename in the diff. `0007` recorded that noise as the
cost of archiving before merge; this makes it unavoidable rather than merely usual.

Nothing prevents someone asking for feedback earlier, and nothing records it when they do. The
rule fixes when approval happens, not when conversation happens.

Sixteen merged tasks were approved under the old order, and their Outcomes were never reviewed.
They are history and are not revisited.
