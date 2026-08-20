# Check the conventions in CI

## Status

Accepted. [0035](0035-manage-portable-rules-as-replaceable-blocks.md) narrows portability and
distribution identity checks from whole installed files to their managed rule blocks. Automatic
checking and the boundary between structural and semantic verification stand.

## Context

Nine tasks ended with the same checks run by hand: does the index match the directories, do the
links resolve, is the archive named correctly, did the portable rule files stay free of project
detail. Each was ad-hoc, and they missed things. The index has been wrong once. A leak of
project-specific detail into a portable file reached human review rather than being caught before
it — and that file is copied into every project using context-fold, so the error would have
travelled.

Each of those checks encodes a decision. An unenforced rule drifts, and the drift is quiet: one
task found a rule contradicted by all eight tasks that followed it, with no entry in any problem
log, because nothing forbade the contradiction loudly enough to notice.

[0012](0012-build-the-methodology-before-the-tooling.md) says v0 is plain files and Git, with
"no command, no program, no runtime". Its *argument* is narrower than its wording: it objects to
tooling that makes the methodology cheaper to follow, because a command that produces an artifact
makes producing it effortless, and effortless ceremony is invisible ceremony. Verification tooling
produces nothing and makes violations detectable, which surfaces friction rather than hiding it —
the opposite of what that argument guards against.

The wording still has to give way, because a test suite is a program and requires a runtime. This
record narrows the prohibition rather than claiming an exemption from it.

## Decision

The repository's structural invariants are checked automatically, on every push and pull request.

This narrows `0012`, which said "no command, no program, no runtime". That prohibition now
applies to tooling that produces artifacts — a task package, an index row, an archived directory
— and not to tooling that only reads and reports. The rest of `0012` stands, and its `Status`
records the narrowing.

The checks encode decisions and are derived from them. The record is the specification; the
suite is one expression of it. When a decision changes, the check that encodes it changes with
it.

Only what can be verified mechanically is checked: that the index matches the directories, that
names match their formats, that required sections exist, that records are numbered without gaps
and all listed, that links resolve, and that the portable rule files carry no project-specific
detail. Nothing here reads a statement against what is already decided.

The stack is Python, run identically in CI and locally: `pytest` for the invariants, which are
most of the work and are specific to this repository, and `pymarkdownlnt` for Markdown style.
Dependencies are pinned. There is no repository-level toolchain beyond that.

Style rules are enabled only where the existing content already satisfies them. A rule requiring
changes to existing prose is not adopted — nine tasks of writing are the specification, not the
linter's defaults.

## Consequences

The invariants that encode decisions hold on every change instead of being remembered, and the
portability commitment becomes mechanical after being broken once.

A passing suite proves the structure holds. It says nothing about whether the prose is correct,
consistent with existing decisions, or worth reading. The failure that prompted the strictest
check — a sentence that contradicted an accepted record while reading as a summary of it — would
still pass.

The checks are a second place decisions are expressed, and they can fall out of step with the
records they encode. Nothing detects that; a check enforcing a superseded rule looks identical to
one enforcing a current rule.

Two style rules are disabled and cannot be adopted later. Line length is unsatisfiable because
Markdown table rows cannot be wrapped and this repository's tables reach 250 characters. Fenced
code language is unsatisfiable because an accepted record violates it and accepted records are
immutable apart from `Status` — which means the set of adoptable style rules is bounded by what
history already contains, permanently.

The repository is no longer only Markdown. Adopting context-fold does not require this, but
anyone reading this repository as the reference will see a Python toolchain in it.
