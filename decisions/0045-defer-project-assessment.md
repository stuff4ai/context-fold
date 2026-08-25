# Defer project assessment

## Status

Accepted

## Context

[0005](0005-agents-layer-boundary.md) does not prescribe where a project's intent, decisions,
documentation, verification, or reusable procedures live, and does not assume they are
authoritative or discoverable. `extend-init-project-assessment`'s `rfc.md` proposed that
`ctxfold-init` close that gap itself: inspect five project capabilities after installing the
layer, classify each as established, partial, absent, ambiguous, or not applicable, record
established sources, and create a separate `planned` task for each applicable gap with
non-binding recommendations.

[0044](0044-defer-the-context-sublayer.md), resolved immediately before this task, applied
[0005](0005-agents-layer-boundary.md)'s "should appear only once it demonstrably exists" bar to a
related proposal — a project-navigation sublayer — and declined to build it: the only recorded
friction was a citation- and ownership-discipline defect, not a case of an agent failing to
locate an authoritative source.

Project assessment has less evidence behind it than that, not more. `0017` records that
context-fold "has only been applied to the repository that defines it": there has been exactly
one adoption, ever, of this project's own layer onto itself. No adopter, inside this repository or
reported from elsewhere, has failed a task or paid a recorded cost because adoption did not flag
a missing capability. The RFC's own open questions — which evidence makes a capability
"established" rather than merely present, who decides an absence is not applicable, how repeat
adoption avoids reopening a gap a project already declined, how many generated tasks turn
guidance into ceremony — have no answer that is not invented, because nothing has yet shown what
a real gap looks like or what an adopter actually needs recommended.

## Decision

`ctxfold-init` does not gain a project-assessment capability now. No capability catalog, evidence
classification, context-map update, or generated-task mechanism is added. Task zero's existing
base-state discovery in `context.md` — recording, in prose, what conventions a repository
already has and where its durable knowledge lives — remains the only project-readiness step
adoption performs.

This narrows the concern rather than rejecting it: [0005](0005-agents-layer-boundary.md) is right
that context-fold cannot assume a project's intent, decisions, documentation, verification, or
skills are discoverable, and a future assessment step may still be the right answer. It is not
the right answer to build on the evidence available now — building the classification scheme and
task-generation mechanism first, and hoping the open design questions answer themselves once it
exists, is the anticipated-need infrastructure [0005](0005-agents-layer-boundary.md) and
[0044](0044-defer-the-context-sublayer.md) both decline to build.

This decision replaces the open "Should adoption assess project-layer readiness?" item in
`OPEN-QUESTIONS.md` with named reopening conditions, the same treatment `0044` gave the
context-sublayer question, so the question does not stay open indefinitely on the same footing.
Reopen only if one of these appears:

- An adopter, or a task in this repository, demonstrably fails, or pays a recorded cost, for want
  of adoption having flagged a missing or ambiguous project capability.
- Context-fold is adopted onto a second project and evidence from that adoption shows a specific,
  recurring gap that a generic checklist could plausibly have caught.
- A later task finds it cannot proceed by referencing project artifacts directly, the same
  standard [0044](0044-defer-the-context-sublayer.md) applies to project navigation.

## Consequences

`ctxfold-init`, its templates, and its checks are unchanged; no adoption or skill work follows
from this decision.

`extend-init-project-assessment` closes without shipping the capability its RFC proposed. Its
resolution and this record are the durable trace of that judgment, so the concern is not lost —
only the infrastructure is deferred.

The "Should adoption assess project-layer readiness?" question in `OPEN-QUESTIONS.md` is answered
for now with a sharper bar for revisiting it, rather than left open with no criterion for when it
stops being open.
