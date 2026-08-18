# Settle status disagreements by the directory

## Status

Accepted

## Context

[0006](0006-task-package-model.md) made `INDEX.md` a derived view and `task.md` the owner of
canonical status: "When the two disagree, `task.md` wins and the index is repaired." The portable
rules said the same.

That rule assumes one failure mode — the derived view drifting away from a correct source. The
failure that actually occurs is the other one.

Finishing a task edits the Status in `task.md`, moves the directory under `archive/`, and updates
the index. Three operations, and nothing is atomic across them. An agent that stops part-way
leaves the two files disagreeing, and which one is stale depends on where it stopped.

Adopting `etu-forms` produced exactly this. The run wrote the Outcome, archived the package,
updated `INDEX.md` to `completed`, and never set the Status, which stayed `active`. A second
agent found the disagreement and corrected `task.md`. Following the rule as written, it would
have reverted a finished task to `active` and brought the index into agreement with a lie.

The rule was unreachable from this repository. No task here has been left half-archived, because
the same agent has always finished the sequence in one pass.

## Decision

When `task.md` and `INDEX.md` disagree about a status, the task's own directory settles it.

A package under `archive/` is finished, whatever `task.md` still says. A package that is not
under `archive/` is unfinished, whatever the index says. Repair whichever file the directory
contradicts.

The directory is the right arbiter because it is the one fact neither file asserts. Both files
are statements about the task; the location is the task. It is also the operation in the middle
of the sequence, so it partitions the failure: if the move happened, the edits before it happened
too and the ones after may not.

A disagreement means an archival stopped part-way, so repairing the stale status is not the whole
repair. Whatever else that sequence leaves undone — an unwritten Outcome, an index row never
added — is undone too.

Where the directory cannot settle it, `task.md` is still right. An archived task called
`completed` by one file and `cancelled` by the other is a disagreement about something the
location does not record.

This narrows `0006`. That the index is derived, and that it is rebuilt from the task directories
rather than resolved by hand, is unchanged.

## Consequences

The rule now describes the failure that happens rather than the one that was imagined. An agent
following it in the observed case reaches the right answer, which the previous rule prevented.

Regenerating the index from task directories copies each `task.md`'s status, so a stale task file
produces a consistent and wrong index. The rules say to settle disagreements before rebuilding;
nothing enforces the order.

"Canonical" is gone from the description of `task.md`. It was the word doing the damage — it
implied that a disagreement is always the other file's fault, which is what the second agent had
to override to be right.

The arbiter is only available for status. Nothing else in a task package has a fact outside the
files to appeal to, so any other disagreement is still settled by whoever notices it.

The rule is stated in `INDEX.md`'s header as well as in the rules, and `INDEX.md` is copied once
and then diverges ([0021](0021-separate-what-upgrades-from-what-diverges.md)). So the corrected
wording reaches new adopters and no existing one, and nothing detects the difference: the
identity check covers `templates/agents/`, which is what `0021` separated `INDEX.md` from. The
two headers agree here because someone remembered.

Three narrowings now sit in `0006`'s Status, which is more than a reader will hold at once. The
record is becoming a list of things that turned out to be wrong, and at some point it should be
superseded whole rather than narrowed again.
