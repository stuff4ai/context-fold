# Make the final check verifiable, or stop calling it a check

## Status

completed

## Objective

Decide what the final exact-head check is worth when the agent running it is the agent being
checked, and change the rule to match.

## Why

The check is four gates run at the branch head, and it is the layer's last line before a change
is accepted. On its first foreign use it produced a false pass.

An adoption run archived task zero with Status still `active`. Its gate-3 command was
`rg -n '^## Status$|^completed$|^## Outcome$' …/task.md`, which printed `3:## Status` and
`37:## Outcome` and no `completed` line — the disconfirming evidence, on screen. The `test`
beside it counted files containing a Status heading, `rg -l … | wc -l`, which is `1` whatever the
file says. It then reported `archive and index: CONFIRMED`.

The check was not skipped or misunderstood. It was performed, and it was constructed so that it
could not fail. A self-report is not evidence about the reporter, and the rules ask for exactly
that.

This is not only a foreign-agent problem. This project's own last two tasks were both refuted by
a fresh reviewer after passing a self-run check, on claims the check does not cover.

## Scope

- `templates/agents/tasks/AGENTS.md` — `## Final exact-head check`, and what `## Finishing` says
  about running it.
- A decision record.
- `skills/ctxfold-init/SKILL.md` and `ADOPTING.md` if what they ask an adopting agent to do
  changes.

## Out of scope

- Shipping this repository's `tests/` with the layer. That is a live open question with `0011`
  arguing against imposing a toolchain, and it is a larger decision than this one.
- Requiring any particular reviewer, human or agent. The layer does not get to say who reviews.
- The four gates themselves, which are the right four.

## Acceptance

1. The rule says what the check is evidence of and what it is not, so an agent cannot read a
   self-run pass as acceptance.
2. Each gate is stated so that satisfying it produces something a second reader can confirm, or
   is explicitly marked as unverifiable by the author alone.
3. An agent following the rule in the observed case would not have reported a pass.
4. Nothing is imposed on an adopting project beyond what `0011` permits.

## Outcome

The final exact-head check now produces evidence, not a verdict. Running it does not mean the
change is accepted; it means the change is ready for review, which is where a second reader's
judgment enters — the check was never a substitute for that and now says so.

The four gates split into two kinds. The first two — acceptance criteria, the deletion test — are
judgment about the task's own claims; no script settles either, and a self-run pass on them is
weak evidence, material for a second reader rather than a replacement. The last two — archived
with Status and Outcome, index matching disk — are facts about the repository, checked by reading
the actual content rather than a count or summary. "A check whose verdict cannot disagree with
its own evidence is not a check" names the specific defect: the observed gate-3 assertion counted
files matching a heading, which is `1` whether the file says `active` or `completed`.

Simulated against the original failure rather than only argued: a file with `## Status` /
`active` was checked both ways. The count-based assertion reports pass. Reading the actual value,
as the new instruction requires, does not.

The record cites three independent instances of the same failure shape, not one — the etu-forms
run, and a second and third caught inside this project's own work this session (`git check-ignore
-v`, which exits `0` on any matching pattern including a negation, misread as proof of tracking).
Three instances made the pattern, not the anecdote, the evidence.

Durable artifacts:

- `decisions/0027-produce-evidence-at-the-final-check.md` — the decision.
- `decisions/0007-archive-before-merge.md` — Status: cross-references what "confirm" now means
  for the four gates; the gates and their order are unchanged.
- `skills/ctxfold-init/templates/agents/tasks/AGENTS.md` — `## Final exact-head check` rewritten.
- `OPEN-QUESTIONS.md` — the entry this closes removed.

`SKILL.md` and `ADOPTING.md` needed no change: both point at `.agents/tasks/AGENTS.md` rather
than restating the gates, which is the "reference, do not duplicate" the layer already asks for.

## Problems

### The unquoted-heredoc backtick mistake happened again

Writing the Outcome the first time used `python3 - <<PY` with an unquoted delimiter, and the
shell expanded every backtick-quoted span as a command before Python ever saw the text — file
names and code spans came out blank. This is the exact mistake logged in the previous task's
`## Problems`.
Assumed: having written it down once, I would not do it again.
Actually: a logged mistake changes nothing by itself; nothing re-reads the log before acting. What
changed this time is that I checked the output immediately — a backtick-count sanity check,
`grep -c` first (which counts lines, not occurrences, and nearly gave a false alarm), then a
correct even/odd count in Python — and caught it before it reached the file's final state, rather
than after review. Fixed by using a quoted delimiter, `<<'PYEOF'`, which passes the body through
unchanged.
The general lesson: a habit documented as a finding is not a habit corrected. What worked was
building a check into the next attempt, not remembering the earlier note.

### pymarkdown flags a lone trailing blank line as two

A file ending in `content\n\n` — one blank line before EOF, which several editors leave by
default — was flagged as `MD012: Multiple consecutive blank lines, Expected: 1, Actual: 2`, even
though `wc -l` and a line-by-line scan both showed exactly one blank line, not two.
Assumed: the discrepancy meant something was still corrupted from the heredoc mistake above.
Actually: `pymarkdown` counts the implicit end of file as a boundary that a preceding blank line
doubles up against. Fixed by stripping to a single trailing newline with no blank line before it.
Not a defect in this task's content — a gotcha worth knowing before treating a lint diff like this
as evidence of something else being wrong.

### Running this task's own final check caught a count-based mistake in me

Gate 4 was checked first with `ls .agents/tasks/archive | wc -l`, which returned 22 against 21
rows in the index — a disagreement.
Assumed: a directory listing count is the fact gate 4 asks for.
Actually: `.agents/tasks/archive/` also holds `AGENTS.md`, a file, which `ls | wc -l` counts
alongside the directories. The rule this task just wrote says to read the actual content, not a
count; re-checking with `find -maxdepth 1 -type d` and cross-referencing the test suite gave 21
against 21.
This is the specific failure the record is about, produced by the person who wrote the record,
inside the check meant to catch it — while trying to demonstrate the fix. Left in rather than
quietly recounted, because it is the most direct evidence this task has that the instruction
matters: a count looked wrong even to someone who had just finished arguing counts are the wrong
tool.
