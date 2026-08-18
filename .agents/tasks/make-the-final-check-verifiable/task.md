# Make the final check verifiable, or stop calling it a check

## Status

planned

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
