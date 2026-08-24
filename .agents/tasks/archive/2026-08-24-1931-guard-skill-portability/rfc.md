---
status: resolved
---

# RFC — guard shipped-skill portability

## Problem

A shipped skill is copied into a repository that does not carry this source repository's decision
records, tests or task archive. `ctxfold-tasks` nevertheless once shipped docstrings referring to
`decision 0037` and `tests/test_conventions.py`. Review removed them, but the existing portability
check covers managed rule blocks rather than every file in a skill package and would not have
caught those exact strings.

The repository needs both a boundary an author can read before writing and a mechanical backstop.
The check must be broad enough to catch nearby forms of the observed mistake without banning the
methodology's own name or generic paths that describe an adopter's installed layer.

## Selected boundary

Every UTF-8-decodable regular file inside each directory under `skills/*/` is portable
distribution content, including Markdown, scripts and references. It may name `context-fold` and
generic adopter contracts such as `.agents/tasks/` and `.agents/worktrees/`. It must not name the
source repository's evidence:

- a bare numbered decision reference, a decision-record filename or a `decisions/` path;
- any `tests/` path or `test_*.py` filename;
- a concrete current or archived task slug or package identity.

The check is lexical. Non-UTF-8 or binary files are skipped, so they are a known false-negative
boundary; paraphrased repository detail can also evade matching. Broad strings can false-positive
when a future portable procedure legitimately needs one. The first version has no allowlist or
inline suppression: a real collision is evidence for a later reviewed change to the rule or check,
not authority to silence it locally.

## Author guidance

Add project-owned `skills/AGENTS.md` so an author sees the boundary before CI. It tells authors to
carry the reusable contract or procedure learned here, not the decision, test or task artifact that
produced it. The file governs authoring in this repository; it is not itself part of any shipped
skill package or a contract for `.agents/skills/` ownership.

## Mechanical check

Extend `tests/test_conventions.py` beside the existing skill checks. Regression cases demonstrate
every rejected category and the explicitly permitted product and generic-path cases. The original
escaped strings are fixtures, not only prose explaining the test. Both current shipped skills must
pass without content changes, compared exactly with the contract revision named by the handoff.

## Alternatives

- Mirror only the existing managed-rule denylist. Rejected because it would miss both observed
  strings: `decision 0037` is not a filename, and `tests/test_conventions.py` is not a
  `decisions/` path.
- Detect only the exact observed strings. Rejected because trivial variants would repeat the same
  portability failure.
- Add guidance without a check, or a check without guidance. Rejected because one leaves recurrence
  silent and the other teaches the boundary only after an author crosses it.
- Ship a suppression or allowlist immediately. Deferred until a legitimate collision shows what
  exception semantics are actually needed.

## Resolution

Add both `skills/AGENTS.md` author guidance and a broad lexical convention check over every
UTF-8-decodable file in shipped skill packages. Reject source-repository decision, test and task
references; permit the product name and generic adopter layer paths. Add no exception mechanism in
the first version, preserve both current skill packages unchanged, record the choice provisionally
as `decisions/0040-guard-shipped-skill-portability.md`, and retain semantic review for leaks a
lexical check cannot prove absent.
