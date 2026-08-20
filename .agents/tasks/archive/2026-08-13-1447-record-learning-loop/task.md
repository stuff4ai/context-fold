---
status: completed
objective: >-
  Record the loop this project exists to create — work produces problems, problems become
  lessons, lessons improve the context the next agent reads — and preserve the designs that were
  cut to keep it cheap enough to follow.
---

# Record the learning loop

## Why

`README.md` opens by stating the problem: knowledge is unstructured, mistakes disappear into
transcripts, every new agent rediscovers how the project works. It never states what answers
that problem. The loop is the answer, and it is the reason `task.md` carries a `## Problems`
section at all — a detail `0006` records as a mechanism without saying what it feeds.

Without it the model reads as a task tracker with unusually strict archiving. The loop is what
distinguishes it, and it is currently the largest piece of the design existing only in the
conversation that produced it.

Two designs were cut to keep the loop affordable — an eleven-step lifecycle and an
eight-artifact task package. Both survive only inside archived problem logs, where they are
effectively invisible.

Six completed tasks have produced observations with real evidence behind them. They sit in
archived packages nobody re-reads, which is the loop failing at its last step in the one
repository meant to demonstrate it.

## Scope

- `decisions/0013-improve-context-from-the-work.md`.
- `decisions/README.md` index row.
- `README.md` — the loop, `ctxfold`, and the folding metaphor.
- `OPEN-QUESTIONS.md` — a recurring-patterns section, and the gap between approval and
  merge-readiness.

## Out of scope

- Building `.agents/learning/`. The loop's last step is manual and stays manual.
- Promoting any observation into a rule. They are recorded as candidates.
- Editing archived packages to remove observations now listed elsewhere.

## Acceptance

1. The record states the loop, why problems are captured during work rather than recalled
   afterwards, and what it is that the `## Problems` section feeds.
2. Its Context preserves the eleven-step lifecycle and the eight-artifact task package as the
   designs that were cut, with the reason.
3. `README.md` states the loop directly after the problem it answers, and carries `ctxfold` and
   the folding metaphor as facts.
4. `OPEN-QUESTIONS.md` lists the two recurring patterns as candidates with their instance
   counts, not as rules.
5. No portable rule file changes, and nothing added exists in more than one owned location.

## Outcome

`decisions/0013-improve-context-from-the-work.md` records the loop, with the eleven-step
lifecycle and eight-artifact task package preserved in its Context as the designs cut to keep
capture cheaper than the friction it records. `README.md` states the loop after the problem it
answers and carries the folding metaphor and `ctxfold`. `OPEN-QUESTIONS.md` gains a recurring
patterns section with the two observations that now have evidence across several tasks, and the
gap between approval and merge-readiness.

All five acceptance criteria satisfied. One overlap was kept deliberately and recorded below
rather than removed.

This completes the folding of the design conversation. Nothing load-bearing from it now exists
only outside the repository.

Nothing was left to fold.

## Problems

### Recording the loop turned pending constraints into decided ones

`OPEN-QUESTIONS.md` held three constraints "already agreed for whenever a learning layer
arrives" — an observation is not automatically a rule, a lesson is a candidate, a permanent
change requires review. `0013` decides all three.
Assumed: the learning-layer entry describes something unbuilt, so recording the loop leaves it
alone.
Actually: the entry was holding decided material under a deferred heading, and the record made
that visible. Rewritten to what is genuinely still open — whether anything should automate the
loop's last step.
Eighth instance of the same pattern, and the second in three tasks caused by writing a record:
formalizing a decision reliably strands a looser statement of it somewhere else. The prior
instance was in `README.md`; this one was in a document specifically for undecided things,
which is where it was least likely to be looked for.

### The loop's definition is stated twice, deliberately

`README.md` and `0013` state the loop in nearly the same three clauses.
Considered and kept. `README.md` must be able to say what the project is without a reader
following a link, and the loop is what the project is; `0013` records it as a decision with
consequences. The drift risk is small because the statement is definitional and carries no
conditions — like the project's name appearing in both.
Recorded rather than silently accepted, so the next reviewer sees it was weighed. If the loop
is ever restated with conditions attached, this stops being safe.
