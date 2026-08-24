# Guard shipped-skill portability

## Status

Accepted

## Context

`skills/*/` packages are portable the same way the managed `AGENTS.md` blocks are:
[0011](0011-keep-the-model-vendor-neutral.md) requires the neutral model to name no product and
assume no particular repository, and [0005](0005-agents-layer-boundary.md) draws the boundary
between the agent operating layer and project knowledge that only makes sense inside this
repository. `skills/ctxfold-init/`'s own adoption procedure says installing a skill is a file
copy into a different repository — one that carries none of this repository's own `decisions/`,
`tests/`, or task archive.

`tests/test_conventions.py::test_portable_rules_carry_no_project_detail` already enforces a
version of this for the managed `AGENTS.md` blocks, but it scans only those four files, not
every file a shipped skill package distributes.

The gap was not theoretical. The shipped `skills/ctxfold-tasks/scripts/query_tasks.py` once
named this repository's own decision number and its own `tests/test_conventions.py` in a
docstring — content that would be meaningless, and misleading, in a repository that only
installed the skill. Review caught it after the pull request was already open; a fresh verifier
confirmed the fix, but nothing in the test suite would have caught the original mistake, or
would catch a repeat of it in either shipped package or a future one.

## Decision

Every UTF-8-decodable regular file inside each directory under `skills/*/` is portable
distribution content — `SKILL.md`, bundled scripts, and reference material alike. It may name
`context-fold` and generic paths that describe an adopter's installed agent layer, such as
`.agents/tasks/` and `.agents/worktrees/`. It must not name this source repository's own
evidence:

- a bare numbered decision reference (`decision 0037` and shapes like it);
- a decision-record filename or a path into this repository's `decisions/`;
- any path into this repository's `tests/`, or a `test_*.py` filename;
- a concrete current or archived task slug, or a package identity that exists only because of
  this repository's own implementation.

`tests/test_conventions.py` enforces this mechanically, beside the existing skill checks. It
walks every regular file under each skill package, decodes it as UTF-8, and skips any file that
fails to decode — binary or otherwise non-UTF-8 content is out of scope for a lexical check, a
known false-negative boundary the check states rather than hides. The check is lexical, not
semantic: it matches substrings and regular expressions, not meaning, so a paraphrase of a
forbidden reference can still slip through, and a legitimate future use of one of the matched
shapes can be flagged as a false positive. Regression cases exercise every prohibited category
directly, including the original `decision 0037` and `tests/test_conventions.py` strings as
literal fixtures, and confirm the permitted product name and generic paths produce no offenders.

The first version adds no allowlist, suppression, or inline exception mechanism. A legitimate
collision is evidence for a later, reviewed change to the rule or the check, not authority to
silence it locally.

Project-owned `skills/AGENTS.md` states the same boundary for a human or agent authoring a skill
to read before the check catches a mistake instead. It is not itself part of any shipped skill
package, and it is not a contract for `.agents/skills/` ownership or the broader agent-sublayer
questions that remain separate work.

Both `skills/ctxfold-init/` and `skills/ctxfold-tasks/` already pass the new check without
content changes.

This extends [0011](0011-keep-the-model-vendor-neutral.md)'s vendor-neutral, project-detail-free
model and [0005](0005-agents-layer-boundary.md)'s agent-layer/project-knowledge boundary from the
managed `AGENTS.md` blocks to every file a shipped skill distributes. Neither record's underlying
boundary changes; this closes a gap in what already enforces it.

## Consequences

A shipped skill that names this repository's own decision numbers, `decisions/` or `tests/`
paths, or task slugs now fails `pytest` instead of shipping until a human reviewer happens to
notice. The specific incident this guards against cannot recur silently.

The check is mechanical and lexical. It cannot prove the absence of a paraphrased leak, and
semantic review of skill content for portability remains necessary; passing the check is
evidence, not proof, that a skill is portable. A future legitimate portable procedure that
genuinely needs one of the matched shapes will be flagged too, with no built-in way to silence
it — only a reviewed change to the rule or the check itself, deferred until a real collision
shows what exception semantics are actually needed.
