# Fold tool-native planning into the task package

## Status

Accepted

## Context

Many agent products carry their own planning mechanism, separate from anything this project
defines: a scratch file shown for approval before implementation, an ephemeral step tracker kept
only for the running session, or something else again. None of it lives in the repository. Once
the tool moves on to implementation, whatever it decided during that phase either survives only
in a tool-local place a later session or a different tool cannot read, or is lost outright.

`0006` already gives this project's own answer to "where does a plan live": `plan.md`, optional
execution strategy, mutable while work proceeds. `0033` adds `rfc.md` for the case where a
direction still needs discussion before execution. Between them, `.agents/tasks/AGENTS.md`
(`skills/ctxfold-init/templates/agents/tasks/AGENTS.md:121–150`) fully describes what a durable
plan looks like and when each file applies. It says nothing about a plan that started somewhere
else — a tool's own planning phase can run to completion, get approved, and never touch either
file.

`0011` requires the portable layer to name no product and assume no particular tool's layout.
That looked at first like a reason to leave this unaddressed at the portable layer and solve it
per product, the way `0030` and `0034` add a repository-scoped adapter for gaps Claude Code
specifically has (no awareness of `AGENTS.md`, no awareness of `.agents/skills/`). This gap is
different: it is not that some product fails to read a portable rule it would otherwise follow,
it is that no portable rule yet says what to do with output a tool produced on its own. A rule
addressing that says nothing about which tool, so it needs no adapter — it belongs in the
portable layer alongside the rest of `rfc.md` and `plan.md`'s own lifecycle rules, and a tool
picks it up the same way it already picks up everything else there: by reading `AGENTS.md`
(directly, or through a product-specific import such as `0030`'s `CLAUDE.md`).

## Decision

`.agents/tasks/AGENTS.md`'s description of `rfc.md` and `plan.md` gains one more rule, placed
after both: a planning phase a tool runs on its own — a scratch file, an ephemeral step tracker,
anything living outside the task package — produces a draft, not a durable record. Before
implementation begins, whatever is worth keeping is folded into `rfc.md`, when the tool-native
phase settled a direction among alternatives, or `plan.md`, when it settled execution steps.
Nothing durable stays only in a place a later session, or a different tool, can't read.

The rule names no product, no file path outside this repository, and no tool-specific mechanism.
It extends `rfc.md`/`plan.md`'s existing lifecycle rather than adding a third file or a new
frontmatter field: the same draft-vs-resolved and mutable-execution-strategy distinctions `0033`
already established apply regardless of where the first draft came from.

## Consequences

A plan an agent's own tool produced no longer has to be re-derived or lost when the task package
is what a later session, or a different tool, actually reads. This covers every tool that already
reads `AGENTS.md` — including Claude Code (through `0030`'s import) and Codex (which reads
`AGENTS.md` as its own native convention) — without a repository-scoped adapter for either, and a
future tool gets the same behavior automatically as long as it reads `AGENTS.md`.

The rule adds no mechanical check: whether a given piece of tool-native output was "worth
keeping" is the same judgment call `rfc.md`'s curation rule and `plan.md`'s optionality already
require, not a new one. Nothing distinguishes, at the file level, a `plan.md` folded from a
tool's own planning phase from one written directly — which is intentional: the task package
gains one more source for these files, not a second kind of them.
