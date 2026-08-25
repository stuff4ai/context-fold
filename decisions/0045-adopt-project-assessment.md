# Adopt project assessment

## Status

Accepted

## Context

[0005](0005-agents-layer-boundary.md) does not prescribe where a project's intent, decisions,
documentation, verification, or reusable procedures live, and does not assume they are
authoritative or discoverable. `extend-init-project-assessment`'s `rfc.md` proposed that
`ctxfold-init` close that gap itself: inspect five project capabilities as the last part of task
zero, classify each as established, partial, absent, ambiguous, or not applicable, record
established sources, and create a separate `planned` task for each applicable gap with
non-binding recommendations.

This record first resolved against building that capability: `0017` recorded that context-fold
"has only been applied to the repository that defines it," so there was exactly one adoption ever,
and no adopter, inside this repository or reported from elsewhere, had failed a task or paid a
recorded cost because adoption did not flag a missing capability. The RFC's own open questions —
which evidence makes a capability "established" rather than merely present, who decides an
absence is not applicable, how repeat adoption avoids reopening a gap a project already declined,
how many generated tasks turn guidance into ceremony — had no answer that was not invented,
because nothing had yet shown what a real gap looks like or what an adopter actually needs
recommended. That resolution named three conditions under which it would be reopened.

The second of those conditions has now been met. `etu-forms/monorepo` — an external, non-trivial
repository (Java/Spring backend, Vite/TypeScript frontend, monorepo, its own ADR convention split
across two directories, GitLab CI, no prior agent layer) — is adopting context-fold. Its task
zero's base-state discovery, done before any assessment mechanism existed to prompt it, already
found two checklist-shaped gaps: no product-intent or requirements document anywhere in the
repository, and decisions recorded as ADRs split across `docs/adr` and `backend/docs/adr` with no
stated precedence between them. The adopter explicitly asked that adoption produce planned tasks
for gaps like these, rather than the capability being proposed on their behalf. Context-fold's own
adoption shares the first shape of that gap — no document distinct from `README.md` states intent
as a requirements document would — which is what makes the finding a recurring pattern across the
two known adoptions rather than a single hypothetical case.

## Decision

`ctxfold-init` gains a v0 project-assessment step, run as the last part of task zero. It inspects
five capabilities — intent and requirements, decisions and rationale, documentation and knowledge,
tests and verification, and agent skills — classifying each from what task zero's own base-state
discovery already found, using the same five states the RFC proposed: established, partial,
absent, ambiguous, not applicable. Established and not-applicable capabilities need nothing
further. For each partial, absent, or ambiguous capability, adoption opens one `planned`
`assess-project-{capability}` task carrying the repository evidence and a non-binding
recommendation, unless a task package of that slug already exists anywhere in the repository —
`planned`, `active`, or archived under any terminal status — in which case none is created, and
the existing package is noted instead.

This adds no new discovery mechanism and no context map: `decisions/0044-defer-the-context-sublayer.md`'s
bar — a capability should appear only once it demonstrably exists — is satisfied by reusing task
zero's existing base-state judgment rather than building a separate one. `skills/ctxfold-init/ADOPTING.md`
and `skills/ctxfold-init/SKILL.md` carry the procedure and the judgment calls it asks of the
adopting agent.

Scope stays v0-sized: no auto-created PRDs, ADRs, documentation, tests, or skills; no prescribed
project layout; only the five listed capabilities, not operations, security, data, release,
integrations, workflows, or MCP/tools. Whether the skills capability can be assessed in a
vendor-neutral way outside languages context-fold has been adopted into remains an open question,
recorded in `OPEN-QUESTIONS.md`.

## Consequences

`skills/ctxfold-init/ADOPTING.md` and `SKILL.md` gain the assessment step and the judgment it
asks of an adopting agent; the portable `.agents/` templates are unchanged, since assessment
produces ordinary task packages rather than a new installed artifact.

A future adoption may generate up to five `assess-project-{capability}` tasks; a repository that
already holds one keeps it rather than getting a duplicate on every re-adoption. Each generated
task still requires a human to choose the project's structure, improve an existing convention, or
decide the capability is not warranted — assessment recommends, it does not build.

The "Should adoption assess project-layer readiness?" question in `OPEN-QUESTIONS.md` is answered:
adoption now performs a bounded v0 version of it, with the vendor-neutral-skills question and any
future expansion (operations, security, data, release, integrations) recorded as what remains
open rather than settled by this decision.
