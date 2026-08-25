# Context — extend initialization with project assessment

## References

- `decisions/0005-agents-layer-boundary.md` leaves project knowledge in existing project-owned
  artifacts and does not prescribe their layout.
- `decisions/0017-adoption-procedure.md` makes adoption install the layer without migrating project
  context or conventions.
- `skills/ctxfold-init/ADOPTING.md` records task zero's existing base-state discovery and explicit
  no-migration boundary.
- `OPEN-QUESTIONS.md` asks what product intent a task must reach and whether context-fold organizes
  project knowledge or produces it.
- PR #53 (`docs/extend-init-project-assessment`) carries the first resolution, its review comment
  raising the `etu-forms/monorepo` evidence, and this reopening. `gh pr view 53` and
  `gh pr view 53 --comments` are the record of what was asked and why.
- `decisions/0045-defer-project-assessment.md` (being rewritten by this task) named the reopening
  conditions this evidence is checked against.

## Assumptions

- The v0 assessment catalog contains product intent and requirements, decisions and rationale,
  documentation and project knowledge, tests and verification, and agent skills — unchanged from
  the first pass.
- Operations, security, data, release and integrations remain future assessment candidates, not
  v0 requirements — the `etu-forms/monorepo` evidence available so far does not speak to any of
  them.

## Base state

`etu-forms/monorepo` (external, evidence-only — this task does not touch that repository):
Java/Spring backend, Vite/TypeScript frontend, monorepo, GitLab CI, its own ADR convention split
across `docs/adr` and `backend/docs/adr` — an ADR there (`docs/adr/4-split-adr.md`) does state
the governing precedence (system-wide decisions at the root, part-local decisions beside that
part's code), so this specific capability was not itself a gap — no product-intent or
requirements document anywhere, no root `AGENTS.md` before its own in-progress adoption. Task
zero (bare layer install) is done there; nothing past it has run yet, so this task has no evidence
about how a generated task is actually received or acted on — only that the intent gap above was
concretely found by ordinary base-state discovery, unprompted by any assessment mechanism.

## Open questions

- Which evidence is sufficient to call a capability established rather than merely present?
  Resolved for v0: reuse task zero's own base-state judgment rather than a separate bar — see
  `rfc.md`'s Current proposal.
- Who decides that an absent capability is not applicable? Resolved for v0: the adopting agent,
  from task zero's own discovery, the same judgment call `ADOPTING.md` already delegates to it
  for the pointer and base-state steps.
- How many planned tasks may adoption create before its guidance becomes ceremony? Resolved for
  v0: at most five, one per capability, only for partial/absent/ambiguous classifications, with
  existing task packages (any status) skipped rather than recreated.
- How does repeat adoption avoid reopening a gap a project already declined deliberately?
  Resolved for v0: a task package's existence, regardless of its final status, is itself the
  record of that decision — assessment checks for one before generating another.
- Can the assessment remain vendor-neutral while evaluating agent skills outside languages
  context-fold has been adopted into? Still open — carried into `rfc.md`.
