# AGENTS.md

Guidance for anyone authoring or editing a skill package under `skills/*/` in this repository.

This file is project-owned, not portable. It is not itself part of any shipped skill package
and is not a contract for `.agents/skills/` ownership — it only tells an author what a shipped
skill's own content may say before a mechanical check (`tests/test_conventions.py`) catches a
mistake instead.

## Every file you ship is read somewhere else

A skill under `skills/*/` is copied whole into a different repository — one that does not carry
this repository's own `decisions/`, `tests/`, or task archive. `skills/ctxfold-init/`'s own
adoption procedure says as much: adoption is a file copy.

That means every file in a skill package — `SKILL.md`, bundled scripts, reference material —
must read correctly with none of this repository's own evidence available. Write down the
reusable contract or procedure you learned while building the skill here, not the decision
record, test file, or task artifact that taught it to you. If a skill needs to explain *why* a
rule exists, explain it in terms an adopting repository can check for itself, not by pointing at
this one's history.

The incident this guards against is concrete: a shipped script once cited this repository's own
decision number and its own test file in a docstring — content that was meaningless, and
misleading, to a repository that only installed the skill. Review caught it after a pull request
was already open; nothing in the test suite would have caught the original mistake.

## What is permitted

- The product name, `context-fold`.
- Generic paths that describe the agent layer any adopting project would have after installing
  it — `.agents/tasks/`, `.agents/worktrees/`, and the like. These name a layer the methodology
  defines, not anything specific to this repository's own installation of it.

## What is prohibited

- A bare numbered decision reference, such as `decision 0037`.
- A decision-record filename or a path into this repository's `decisions/`.
- Any path into this repository's `tests/`, or a `test_*.py` filename.
- A concrete current or archived task slug, or a package identity that exists only because of
  this repository's own implementation.

## The check is lexical, not semantic

`tests/test_conventions.py` scans every UTF-8-decodable regular file under each skill package
for the shapes above. It skips any file that fails to decode as UTF-8 — binary or otherwise
non-UTF-8 content is outside the check's reach, a known false-negative boundary. The same is
true of a paraphrase: rewording a forbidden reference so it no longer matches the check's
patterns still defeats the check, even though it would not defeat a human reviewer.

The matching is deliberately broad, which is also its false-positive risk: a future, legitimate
portable procedure that genuinely needs one of these shapes will be flagged too. The check ships
with no allowlist or suppression mechanism. A real collision is evidence for a later, reviewed
change to the rule or the check — not license to silence it locally. Passing the check is
necessary, not sufficient; a skill that avoids every listed shape can still leak
repository-specific assumptions in ways only a reader would catch.
