# Bootstrap the tasks layer

## Status

active

## Objective

Establish context-fold v0: the `.agents/` tasks layer, the project-layer artifacts that must
survive without it, and decision records for what is already settled.

## Why

Every design decision behind context-fold currently lives only in a chat transcript. The
repository holds licensing files and nothing else. That is exactly the failure mode
context-fold exists to fix, so the first task fixes it for context-fold itself.

Doing this by hand — before any tooling exists — is the point. The friction found while
building the layer is the evidence that shapes what comes next.

## Scope

- `.agents/AGENTS.md` — the layer contract.
- `.agents/tasks/` — this task package, `INDEX.md`, `archive/`, and the rules for both.
- `README.md` and root `AGENTS.md` — project-layer entry points.
- `decisions/` — template, index, and records for the settled decisions.

## Out of scope

- CLI, skills, workflows, `.agents/context/`, `.agents/learning/`.
- Adapters for specific agent tools.
- RAG/MCP, index generation, frontmatter schemas, distribution and versioning.
- Installing context-fold into any other repository.

Open questions belong in `context.md`, recorded rather than answered.

## Acceptance

1. **Deletion test.** With `.agents/` removed, `README.md`, root `AGENTS.md`, and `decisions/`
   still explain what the project is, how it works, and why.
2. **Cold-start test.** An agent given only the repository root reaches this task's objective,
   scope, and acceptance via `AGENTS.md → .agents/AGENTS.md → tasks/INDEX.md → task.md`
   without being told the path.
3. **Index consistency.** `INDEX.md` rows match the directories on disk, and every listed
   status matches that task's `task.md`.
4. **Decision completeness.** Every settled decision is recorded in an ADR, and every
   postponed one is listed in `context.md`. Nothing load-bearing remains only in chat.
5. **Friction captured.** `## Problems` below is non-empty. An empty log means the capture
   mechanism failed, not that the work went well.

## Problems

Append during work. Two to four lines each: what happened, what was assumed, what was
actually true.

### `context.md` had to forward-reference artifacts the task creates

Writing the References section meant linking ADRs that did not exist yet, so the section
described the future rather than the present.
Assumed: a task's context references artifacts that already exist.
Actually: a bootstrapping task references artifacts it will create, and a task that
*produces* durable knowledge inverts the normal direction. The file model has no way to mark
a reference as forward-looking.

### The deletion test is ambiguous when the layer is also the subject

`README.md` describes the task package model, which is also what `.agents/` implements here.
Assumed: the project layer and the agent layer describe different things.
Actually: in this repository they overlap, because the methodology is the product. The test
still resolves it — the *description* of the model is project knowledge, the *instance* of
the model is scaffolding — but nothing stated that, and it was not obvious while writing.

### The three entry points duplicated each other

Root `AGENTS.md`, `.agents/AGENTS.md`, and `README.md` each restated the layer boundary and
the deletion test in slightly different words.
Assumed: each file has a distinct audience, so overlap is harmless.
Actually: this is exactly the drift the "reference, do not duplicate" rule forbids, and it
appeared in the files that state the rule. Resolved by keeping the full statement in
`README.md` and `.agents/AGENTS.md`, and reducing root `AGENTS.md` to a pointer — but the
pull toward restating was strong and will recur.

It recurred twice more in the same task, both caught by human review rather than by any rule:
root `AGENTS.md` was left describing what the agent layer *is*, and then still pointed at
`tasks/INDEX.md` directly, restating the navigation rule that `.agents/AGENTS.md` owns. Each
individual restatement looked harmless while writing it. Three occurrences in one task is no
longer a slip — a single pointer is the only stable form, and anything more is drift waiting
to happen.

A fourth and fifth instance then turned up between the layer files themselves:
`.agents/AGENTS.md` and `tasks/AGENTS.md` both explained the index and both defined when a
task is complete, and `task.md is authoritative` appeared three separate times. The cause was
a missing ownership rule between scopes, not carelessness. Resolved by scope: the layer file
holds only what applies everywhere in `.agents/` — the truth boundary, portability,
reference-don't-duplicate, scoped instructions — and everything task-shaped moved down to
`tasks/`. `.agents/AGENTS.md` lost three sections and now points down instead of explaining.

Standing pattern across all five: a rule stated where it is *relevant* rather than where it is
*owned*. Relevance is not ownership, and every file finds every rule relevant.

### Restating a rule three times let a contradiction hide inside it

The immutability rule appeared in three files. Two said accepted records must not be edited;
the third said to update the superseded record's Status. Both readings are reasonable and they
cannot both be followed.
Assumed: repeating a short rule verbatim is safe even when duplication of longer text is not.
Actually: the restatements were paraphrases, and a paraphrase silently decides what the rule
covers. Nobody chose to make Status an exception — the wording did it, in one file, and the
other two contradicted it. Fixed by naming Status as the sole permitted mutation and saying so
identically in all three.
This is the same relevance-versus-ownership pattern above, but with a sharper consequence:
duplication does not only risk drift, it can encode a decision that was never made.

### The deletion test left a mandatory instruction pointing at a deleted file

Root `AGENTS.md` said "Read `.agents/AGENTS.md`" unconditionally, which becomes a broken
instruction the moment the layer is removed.
Assumed: the deletion test is about whether knowledge survives.
Actually: it is also about whether the surviving files still make sense. A repository that
orders its reader to open a nonexistent file is not "understandable and maintainable", so the
test was passing on a technicality. Both this and the earlier portability defect were found by
review, not by the acceptance criteria — the criteria check for presence of knowledge and never
for coherence of what remains.

The first fix — a conditional "if it is present" — was then reverted. Hedging an instruction
against a hypothetical deletion weakened it for the case that actually holds, and root
`AGENTS.md` is project-owned, so whoever removes the layer updates this file in the same
change. The finding was real; the remedy was wrong, and it took a second review to see that.

A third review then raised the identical finding again, because the unconditional pointer had
returned. Three passes, two opposite remedies, every reviewer reasonable — at which point the
defect is clearly in the rule and not in the file being corrected. The test said "delete
`.agents/` and the repository must remain understandable and maintainable", which reads as a
literal operation permitting no edits, while it was only ever meant to prevent knowledge from
being trapped in the layer. Under the literal reading the conditional pointer fixes nothing
anyway: `README.md` would still describe a layer that no longer exists.

Resolved by scoping the failure condition rather than patching the pointer. The procedure stays
mechanical — remove the layer, read what remains — but it fails only on lost knowledge, never
on a dangling reference.

The general lesson is about how ambiguity presents: not as disagreement over an answer, but as
a fix that will not stay fixed. Two reverts of the same line were the signal, and both times
the reflex was to edit the line again.

### The same contradiction was still hiding in a fourth file

Moving `docs/adr/` to `decisions/` surfaced a fourth statement of the immutability rule, in
`README.md`, still saying a record is replaced "never by editing the old one".
Assumed: fixing the three known copies fixed the contradiction.
Actually: nobody had counted the copies. Three were found by review and a fourth by an
unrelated refactor, which means the count was never known and could still be wrong. A rule
restated an unknown number of times cannot be corrected reliably — the fix is not better
proofreading but reducing the number of statements to one owned location.

### Relocating the decision directory touched no portable file

`docs/adr/` became `decisions/` with edits to `README.md`, root `AGENTS.md`, the records
themselves, and this task package — and not one line of `.agents/AGENTS.md`,
`tasks/AGENTS.md`, or `archive/AGENTS.md`.
Assumed: nothing; this was a check, not a surprise.
Worth recording anyway as the first positive evidence that the portable/instance split holds.
Before the earlier de-pathing, this rename would have required editing the layer contract
itself — which is precisely what would have made the layer non-upgradable.

### The designed lifecycle conflated status with stage

The lifecycle was specified as one chain: `planned → ready → active → work → verification →
review → approved → fold → finalize → archive → final check → merge`.
Assumed: those are the values a task's Status can hold.
Actually: only four are ever written to a file — `planned`, `active`, `completed`,
`cancelled`. The rest are stages the work passes through, several of which happen while
Status stays `active`. Writing `ready` or `approved` into `task.md` would make status
unmaintainable, since nothing observes the transitions. Codified as two separate concepts.

### Splitting rationale from procedure across ADR and AGENTS.md needed a rule

Writing `tasks/AGENTS.md` after the ADRs meant deciding, line by line, what to restate.
Assumed: the ADR records the decision and the operating file just points at it.
Actually: a pointer alone is unusable mid-task — an agent needs the procedure inline. The
working rule became: the ADR carries *why and what was decided*, `AGENTS.md` carries *how to
do it now*, and only the rule itself is repeated, never the reasoning. This rule was invented
during the task and is not written down anywhere in the project layer.

### The cold-start agent ignored the navigation chain and globbed instead

A fresh agent given only the repository root was asked what work is in progress. It found the
task, but by searching the directory tree directly — reaching root `AGENTS.md` only as its
fourth file, after it already had the answer.
Assumed: agents enter at the root entry point and follow links down to the index.
Actually: agents search first and read entry points afterwards, if at all. `INDEX.md` was read
last and changed nothing. The chain `AGENTS.md → .agents/AGENTS.md → INDEX.md → task.md` is
how a human would navigate, not how an agent does. Acceptance criterion 2, which asserts that
chain, does not hold as written.
The layer still worked — everything was reachable and the agent reported the objective, scope,
and acceptance correctly — but it worked because the *files were well named and self-contained*,
not because the navigation chain guided it. That is a different property than the one designed
for, and it suggests index-based navigation is worth less than assumed while naming and
per-file self-sufficiency are worth more.

Secondary observation: the agent's own report claimed "no guessing occurred" while also
describing step 1 as directory-structure discovery. A subagent's self-assessment of whether it
followed a protocol is not reliable evidence that it did.

### The tool-agnostic rule was written with this repository's paths baked in

The layer boundary was stated four times as "belongs in `README.md`, `docs/`, `docs/adr/`" —
turning a general principle into a prescription of one layout.
Assumed: naming concrete paths makes the rule easier to apply.
Actually: it makes the rule wrong for any project that keeps documentation elsewhere, and
tool-agnosticism is a core commitment. Restated by kind of artifact — code, tests,
documentation, decision records — with placement left to the project. This repository's actual
paths still appear where a file refers to *this* repository, which is correct.

Caught by human review, not by any of the five acceptance criteria. The deletion test only
checks that knowledge survives, never that a rule is portable. Nothing in the current
acceptance model would have found this.

Note on process: `0005-agents-layer-boundary.md` was edited rather than superseded, which is
legitimate — it is still on a branch, and a record becomes immutable when merged, not when
written. Worth remembering that the immutability rule has this window in it.

### One request for three lines of workflow rules produced three decision records

Adding branch naming, commit format, and sign-off to `AGENTS.md` meant three new records —
nearly doubling the repository's decision history for three sentences of instruction.
Assumed: durable decisions map roughly one-to-one onto the effort of making them.
Actually: cheap-to-state decisions can be expensive to record properly, because each has a
distinct rationale and bundling them produces an incoherent Context section. Splitting them
was right; the ratio still feels wrong.

This is the open question about how broad decision records should be, arriving concretely
rather than in the abstract. No threshold rule is proposed yet — one data point is not a
pattern, and the next few tasks should say whether this repeats.

### The layer's own rule files were not portable

`tasks/AGENTS.md` opened by linking two of this repository's decision records by number, used
this repository's task slug as its example, and instructed agents to "open a pull request".
Assumed: `.agents/` is one uniform thing.
Actually: it holds two kinds of file with opposite properties. The `AGENTS.md` rule files must
be identical in every project — installed, never edited, replaceable on upgrade. The index,
task packages, and archive are the opposite: entirely this project's, never touched by an
upgrade. Nothing stated the split, so project detail leaked into the portable half within one
task of writing it.

Fixed by removing the decision-record back-links, neutralizing the example, and decoupling the
stage names from any particular acceptance mechanism. The split is now stated in
`.agents/AGENTS.md`, along with the rule that a misfitting rule is recorded as a problem rather
than edited locally — otherwise the layer stops being upgradable.

Consequence worth noting: the rule files can no longer cite their own rationale, because the
rationale lives in context-fold and the numbering is local to whichever project is reading. The
"reference, do not duplicate" rule has no answer for a cross-repository reference.
