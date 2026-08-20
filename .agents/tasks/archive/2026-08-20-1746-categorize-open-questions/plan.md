# Plan — categorize open questions and identify task candidates

## Strategy

Preserve evidentiary state as the authoritative top-level organization and add topical subsections
only where they make a large or mixed section easier to discuss. Move complete item blocks without
rewriting them, then compare their full text and parent evidentiary sections against the pinned
before-state.

Task promotion is a separate pass after categorization. Start with the
rule-consistency-and-enforceability gap cluster and create no derived task until the user selects an
individual question or an inseparable group under the RFC's shared-task rule.

## Pinned before-state

- Commit: `793e3072e92c4f82f8c69badd907c3de90322094`.
- `OPEN-QUESTIONS.md` blob: `3017b1b7472fe7438b0f55d59bfb9a4fc04d1595`.
- Population: 57 live item blocks receive one topical destination; 2 Recurring-patterns blocks
  remain flat; 2 explicit non-answer blocks remain flat and are outside the 59-live-item count.

## Current slice

The current slice may change `OPEN-QUESTIONS.md` and this task's own RFC, plan, and problem log. It
may add the eight resolved topic names as level-three headings and short category introductions,
and may move exactly 57 complete live-item blocks. It changes no item prose, creates no task
directory, and does not edit `INDEX.md`.

1. Build an explicit mapping for the 57 topically assigned live item blocks. Leave the 2 recurring
   patterns in their existing top-level section without a topic, and leave both non-answer blocks
   unchanged in their final section.
2. Add topical subsection headings and short introductions to `OPEN-QUESTIONS.md`, moving each of
   the 57 mapped blocks exactly once. Preserve every block byte-for-byte and keep its level-two
   evidentiary section unchanged.
3. Parse before and after into records keyed by the exact bold item label, with the complete bullet
   block and parent level-two heading as values while ignoring level-three topic headings. Require
   59 unique, one-to-one live records with identical blocks and parents. Separately require the 2
   non-answer blocks and their final parent heading to be identical. The prose-difference allowlist
   is empty.
4. Review the rendered hierarchy and present the rule-consistency-and-enforceability gap cluster as
   the first promotion group. Stop with zero derived task packages and no index change.
5. Run pytest, recursive Markdown lint, and `git diff --check`, and report the block-conservation
   comparison with the first promotion group.

## Later promotion slice

This slice is unrunnable until the user names exact item labels and grouping, and that selection is
recorded in RFC Review notes. Before creating anything, update this plan with the selected task
slugs, owned files, and exact number of task packages and index rows. Each task receives
`task.md`, `context.md`, and a draft `rfc.md`, with no plan.

## Rollback

Before the current slice is committed, the pinned commit's `OPEN-QUESTIONS.md` is the byte-exact
restore source. Remove only the slice's task-local progress note and restore that file from
`793e3072e92c4f82f8c69badd907c3de90322094`; no derived directory or index row exists to unwind.

## Stop conditions

- Reopen the RFC if categorization requires changing evidentiary state, duplicating items, or
  adding roadmap metadata.
- Stop before creating any derived task or editing the index in the current slice.
- Stop the later slice when its exact item selection, grouping, or file budget is absent.
