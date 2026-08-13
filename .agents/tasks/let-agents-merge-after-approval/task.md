# Let agents merge after approval

## Status

active

## Objective

Allow an agent to merge a pull request once a human has approved it, and record what that
changes about the gate.

## Why

`0001` makes merging a human action: agents open and update pull requests, a person merges. In
practice that produces three exchanges at the end of every task — approve, wait for archival,
merge — where the middle step is mechanical and the last is a single command.

Thirteen tasks have run that way. The waiting has never caught anything; every merge followed an
approval that was already given.

## Scope

- `decisions/0019-agents-may-merge-after-approval.md` and the index row.
- `0001`'s `Status`, recording the narrowing.
- Root `AGENTS.md` — the project rule that currently forbids it.

## Out of scope

- Who approves, or what approval means. Unchanged.
- Pushing to `main` directly, which stays forbidden.
- Any change to `0007`: approval still authorizes archival, and archival still precedes merge.

## Acceptance

1. The record states the narrowing and what it costs — the archival commit merges without a
   human having seen it, since approval precedes archival.
2. It states what covers that gap and what does not: CI verifies the archival invariants; the
   Outcome prose is unverified by anything.
3. Root `AGENTS.md` permits merging after approval and still forbids pushing to `main`.
4. `0001` is unedited apart from its `Status`.

## Problems

### The conflict was written down and then not acted on

`OPEN-QUESTIONS.md` recorded that approval and merge-readiness are different states with nothing
bridging them. `0019` makes the agent that bridge, so the entry became false the moment the
record was written. It was left in place.
Assumed: nothing — this one was seen. The task's own `context.md` names the conflict under
Context conflicts, in the sentence "this makes the agent responsible for that bridge rather than
the reviewer".
Actually: noticing a conflict and recording it in a task-local file is not resolving it. The
observation went where it would be archived, and the live document it described stayed wrong.
Thirteenth instance of a decision stranding an older statement, and the first where the
staleness was identified in writing before it shipped. That is a worse failure than the previous
twelve, not a better one: the others were blind spots, this was a note to nobody.
Replaced with what is now true — the archival commit merges unreviewed — which is the cost
`0019` accepts, and belongs in the live list rather than only in the record's consequences.

### The instructions had told agents both to merge and not to merge

Project rule: "Do not merge pull requests." Change workflow, step 5: "Squash merge." Both in
`AGENTS.md`, both addressed to agents, since the whole file is.
Assumed: the rule and the workflow described the same process from different angles.
Actually: they contradicted each other outright, and had since `0008` added the squash step. No
agent hit it because the human always merged first, so the ambiguity never had to resolve —
which is why it survived thirteen tasks and two reviews of that file.
Resolved incidentally by this change: rule 15 now permits merging after approval, and step 5 is
the same instruction.
Third contradiction found in this repository that nothing checks for, and the second where the
two halves sat in one file. Structural checks do not read for agreement.
