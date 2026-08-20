# Manage portable agent rules by block

## Status

active

## Objective

Let an adopted repository append project-specific agent instructions without losing them when
`ctxfold-init` updates the portable rules.

## Why

The four portable `AGENTS.md` files are currently owned and compared as whole files. That makes
updates simple, but any project-specific addition turns the file into an unsupported fork that a
later update overwrites. One managed block per file can keep the portable rules replaceable while
leaving an additive suffix under the adopting project's ownership.

## Scope

- The ownership and update contract for the four portable rule files, including a new decision
  record and Status-only narrowing of the accepted whole-file decisions it replaces.
- `skills/ctxfold-init/` and `.agents/skills/ctxfold-init/` — the canonical procedure, skill,
  templates, and this repository's whole-package installation.
- Root `AGENTS.md`, the four installed `.agents/**/AGENTS.md` files, README, and convention checks.
- `OPEN-QUESTIONS.md` — only the wording of **Versioning, provenance, discovery, and upgrades**,
  **How should an adopter customize or replace the portable rules?**, and **Should an adopter's
  installation be checkable?** The concurrent `categorize-open-questions` task retains heading
  structure, introductions, and item placement.
- `.agents/tasks/INDEX.md` — this task's derived row and eventual archival update; rebuild it from
  task directories after integrating concurrent work.

## Out of scope

- Conflicting local overrides, more than one managed block per file, or finer-grained blocks.
- Versions, digests, source provenance, update discovery, changelogs, or automatic migrations.
- Recovering edits made to legacy whole-file-owned installations despite their existing warning.
- A runtime updater or changing the project-owned root `AGENTS.md` pointer.
- Changing the concurrent question-categorization task or its worktree.

## Acceptance

1. Each portable template is one vendor-neutral `agent-layer` managed block at byte zero, with a
   source-visible HTML comment warning that updates replace the block and project additions belong
   only after it; rendered Markdown shows only the operating rules.
2. Fresh installation writes the templates; repeat adoption preflights all four targets, replaces
   unmarked legacy files wholesale, replaces a single valid managed block while preserving every
   suffix byte, and makes no writes when any marker structure is malformed.
3. The shipped and installed skill packages remain byte-identical, while the three corresponding
   managed blocks in the shipped template, installed-skill template, and active installation are
   byte-identical and installed suffixes may differ.
4. A decision record narrows the accepted whole-file ownership, portability, adoption,
   distribution, and checking claims without weakening vendor neutrality.
5. README, the two owned open-question items, root project workflow, and portable rules agree with
   the new contract; conflicting overrides, granularity, identity, discovery, and migration remain
   deferred.
6. Disposable fixtures demonstrate suffix preservation and all-target no-write behavior, and
   pytest, recursive Markdown lint, skill parity, and `git diff --check` pass.

## Problems

### The planned prerequisite remained active when implementation was authorized

Assumed: this task would begin only after `categorize-open-questions` landed or was cancelled.

Actually: the user explicitly authorized starting while that task is active. The tasks can share
`OPEN-QUESTIONS.md` by section: this task owns only three item bodies, while categorization owns
their placement and surrounding structure. The derived index will be rebuilt after integration.

### Block-scoped checks change a third live question

Assumed: only the upgrade and customization items needed wording changes.

Actually: the adjacent installation-check item said any installed-file edit fails this
repository's CI. Additive suffixes are now valid and excluded from portability checks, so leaving
that item unchanged would make the live question assert superseded behavior. Its wording joined
this task's section-level scope; categorization still owns its placement.

### A shell preflight probe masked an invalid earlier target

Assumed: `set -e` inside a shell loop used as an `if` condition would stop when one target failed
marker validation.

Actually: the conditional context suppressed that behavior, and a later valid target made the
whole loop succeed. No repository file was written. The corrected disposable probe accumulates an
explicit invalid flag across every target before deciding whether any update may run, matching the
procedure's all-target preflight rule.
