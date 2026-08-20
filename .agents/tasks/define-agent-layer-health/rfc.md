---
status: draft
---

# RFC — define agent-layer health and recovery

## Problem

The current repeat-adoption procedure can restore managed blocks while preserving suffixes, but a
larger governed namespace introduces more failure states. A required contract may be missing, an
unknown tool may add a directory, a user may intentionally fork rules, or project truth may be
misfiled into agent-only context. Treating all divergence as damage would make adoption destructive.

## Current proposal

Define structural health around contracts context-fold actually owns. Missing or drifted managed
contracts are recoverable after preflight; malformed markers stop repair; independently owned
contents are preserved; unknown extensions are reported with unknown ownership rather than removed.
Intentional forks need an explicit way to leave managed identity.

Keep semantic health separate. Checks may establish paths, markers, references and declared owners,
but whether a summary duplicated project truth or a rule contradicts reality remains a review
judgment unless an authoritative comparison exists.

## Alternatives

- Rely only on repeat adoption and add no broader health model.
- Require every installation to run context-fold checks in CI.
- Claim exclusive ownership of `.agents/` so unexpected content is always invalid.

## Open questions

- Which health evidence belongs in the repository and which can be produced on demand?
- Should repair be automatic after a clean preflight or separately authorized?
- How is an intentional fork represented without introducing mandatory provenance/versioning?
- When should a structural finding create a project task rather than be repaired immediately?
