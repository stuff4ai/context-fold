# Stages are not one-way

## Status

Accepted

## Context

The stages a task passes through are written as a single sequence from `planned` to `merge`.
Read literally, that describes work reaching verification, then review, then acceptance, with
each stage entered once.

No task has worked that way. Review sends work back. Verification finds something that changes
the design. A rule fails on its first application and the task returns to writing it. In eight
completed tasks, every one returned to an earlier stage at least once, and several did so
repeatedly.

The design this model came from made the observation directly: development is several loops —
clarifying, designing, implementing, solving problems, verifying — rather than one pipeline. It
expressed that as a lifecycle with a stage for each loop, eleven in total, which was cut for
being more ceremony than anyone would perform. The structure was wrong; the observation was not,
and it was lost with the structure.

What remains is a written sequence that quietly disagrees with every task that has followed it.
An agent applying it would treat returning to an earlier stage as a deviation worth explaining,
or worse, avoid returning at all — accepting work that should have gone back, because the
written model offers no way to go back.

## Decision

Stages describe the order work passes through, not a path it travels once.

Work returns to an earlier stage whenever review, verification, or a finding requires it. This
is the normal shape of the work, not an exception, and it needs no justification or record.

Returning changes no `Status`. A task is `active` from the moment work starts until it is
archived, regardless of how many times it moves between stages, so iteration costs nothing in
bookkeeping. This is the second half of the existing distinction between status and stage: status
is what a task *is*, stages are what it is *doing*, and only the former is written down.

The stage sequence is still meaningful — it says what must have happened before what. Archival
follows acceptance; verification precedes review. Order is constrained; repetition is not.

## Consequences

The written model matches what tasks actually do, and an agent mid-task has a rule permitting
what it was going to do anyway.

Work that should go back does. A model with no way to return creates pressure to accept
something rather than admit the stage was left too early.

Nothing distinguishes healthy iteration from a task that is stuck. A task on its second return
and one on its twelfth look identical from outside, and no signal exists to notice the
difference — the same permissiveness that makes returning free makes circling invisible.

The observation that produced this is preserved without the structure that expressed it. Anyone
proposing per-loop stages again should know it was tried and cut, and why.

Whether long-running or multi-author tasks loop the same way is unknown. The evidence is eight
small, single-author, documentation-shaped tasks.
