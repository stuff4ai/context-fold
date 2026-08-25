# Wire step 5 into repeat adoption

## Status

Accepted

## Context

[0046](0046-adopt-project-assessment.md) gave `ctxfold-init` a v0 project-assessment step, run
once as the last part of task zero. Its Consequences claimed a repository that already holds an
`assess-project-{capability}` task "keeps it rather than getting a duplicate on every
re-adoption" — implying step 5 runs again on repeat adoption. `ADOPTING.md`'s "If the layer is
already there" section never called step 5 at all: it only preflighted and updated the five
managed `AGENTS.md` targets, said to leave task packages alone, and said not to reopen task zero.
Step 5 was wired only into task zero's own flow, which by definition runs once per repository. A
repository that adopted before step 5 existed — or one that legitimately wants its assessment
redone — had no documented way to get it short of deleting `.agents/` and the root pointer and
redoing task zero from scratch, unsafe once real work sits on top of the layer.

This was found and reported on `0046`'s own pull request, before merge, while testing adoption
against a real external fixture; recorded afterward as `wire-step-5-into-repeat-adoption` once
that PR had merged and its task package was no longer writable.

## Decision

Repeat adoption performs a one-time catch-up assessment. After the existing five-target
preflight, check three signals anywhere under `.agents/tasks/` (including `archive/`): an
`assess-project-{capability}` task package, a `project-capability-catchup` package, or task
zero's own package carrying a "Project-capability assessment" section in its `context.md`. Any
one of them means step 5 has already run once; skip. If none exist, classify the five
capabilities against the repository's current state — not by reopening task zero — and open the
same `planned` tasks step 5 would have opened at adoption time, then record the pass itself as
its own completed task package, `project-capability-catchup`, so a repository that finds zero
gaps has a durable "this was checked" record exactly as a repository that finds several does.

No new persistent flag or version marker was added. The gate reuses evidence the layer already
produces — existing `assess-project-*` packages, task zero's own content, or the catch-up
package itself — the same "appear only once it demonstrably exists" bar
[0005](0005-agents-layer-boundary.md) and [0044](0044-defer-the-context-sublayer.md) apply
elsewhere.

## Consequences

`skills/ctxfold-init/ADOPTING.md`'s repeat-run section and `SKILL.md`'s judgment-call guidance
now describe the catch-up pass and its three-signal gate; both stay byte-identical between
`skills/ctxfold-init/` and the installed `.agents/skills/ctxfold-init/` copy, as verified.

A repository whose task zero predates step 5 gets the assessment on its next repeat adoption
rather than never. A repository that already ran step 5 — with or without finding gaps — does
not get a duplicate or spurious pass, because at least one of the three signals is already
present.

[0046](0046-adopt-project-assessment.md)'s Consequences claim now matches what `ADOPTING.md`
actually implements.
