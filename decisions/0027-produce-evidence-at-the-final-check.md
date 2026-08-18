# Produce evidence at the final check

## Status

Accepted

## Context

`0007` defined the final exact-head check as four gates, "confirm all four," with no account of
what confirming one means or what the confirmation is worth. The portable rules restated the same
four gates the same way.

On its first foreign use it produced a false pass. An agent adopting `ctxfold-init` archived a
task package with Status still `active`. Its gate-3 check ran a command whose own printed output
showed no `completed` line — the disconfirming evidence, on screen — and beside it ran a
different assertion, `test "$(rg -l '^## Status$' …/task.md | wc -l)" -eq 1`, which counts how
many files contain a `## Status` heading. That count is `1` whether the file says `active` or
`completed`; it cannot fail on the claim it stands next to. The run reported `CONFIRMED`.

The check was not skipped or misread. It was performed, its own evidence contradicted its own
verdict, and the verdict was trusted anyway.

This is not only a foreign-agent failure. Two of this project's own tasks were refuted by a fresh
verifier after passing this exact check, on claims the check does not cover: one on a
self-contradiction introduced into a record while correcting a different one, one on a stranded
statement the fix left standing in a second copy. And building the change that produced this
record, the same shape appeared a third time from the other direction: `git check-ignore -v`
exits `0` whenever *any* pattern matches a path — including a negation — so a check built on that
exit code reported a file "STILL IGNORED" while `git status` showed it correctly tracked. Three
independent instances of the same failure: a check whose result cannot disagree with the fact it
is supposed to be testing.

## Decision

The final exact-head check produces evidence, not a verdict. Running it does not mean the change
is accepted — it means the change is ready for someone who did not write it to look at, which is
what review, immediately after it in `0023`'s order, is for. A pass here is necessary and never
sufficient, whoever ran it.

The four gates split into two kinds, and each kind is confirmed differently.

The first two — each acceptance criterion satisfied, no durable outcome left only in the layer —
are judgment about what this task itself claims. No script settles either one in general. Reading
the diff against the claim is the check, and doing that once, as the person who already believes
the claim, is weak evidence. It is the material a second reader needs, not a substitute for one.

The last two — the directory under `archive/` with Status and Outcome set, `INDEX.md` matching
disk — are facts about the repository as it stands. A path either is or is not under `archive/`;
a table either does or does not match a directory listing. These are checked by reading the
actual content, not by a count or a summary that reports success regardless of what the content
says. A check whose verdict cannot disagree with its own evidence is not a check: if nothing you
could observe would make it report failure, it is not testing the thing it claims to.

Nothing here names a tool. `0011` bounds the portable rules to properties, not commands, and the
three instances above happened in three different tools — a hand-run `rg`, a hand-run
`git check-ignore`, and, by omission, no tool at all.

## Consequences

The gate-2 open question — whether the deletion test is verifiable by anyone without literally
removing the layer — is answered rather than left open: it is verifiable by a reader, self or
second, and self-verification is the weak case rather than a special one requiring its own
category. "Unverifiable by the author alone" was considered as a label for such gates and
rejected; every gate here is verifiable, by someone, which is a different claim from being
self-certifying.

An agent that reads its own printed evidence before trusting a separate assertion beside it would
not have produced the false pass this record is built on. The rule cannot make that reading
happen — it can only say what a check has to be for the reading to matter. A well-intentioned
author can still write a count and believe it is a check; this narrows the failure without
retiring it.

Nothing is imposed on an adopting project beyond what it already had. The four gates are
unchanged, and `0011` continues to bound what a portable rule may require.

This elaborates `0007` without changing what it decided — the four gates and their order stand.
A reader of `0007` alone would not learn this exists, so its Status notes where the fuller
account lives.
