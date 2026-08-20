---
status: draft
---

# RFC — categorize live open questions and promote selected items

## Problem

The current top-level sections mix two useful dimensions:

- what kind of uncertainty an item represents — deferred capability, model question, observed gap,
  recurring pattern, or explicit non-goal;
- what subject the item concerns — task lifecycle, context, decisions, verification, distribution,
  integrations, or the product boundary.

The first dimension explains evidentiary state but leaves 35 model questions in one long section.
The second would make discussion manageable but could hide whether an item is hypothetical,
evidence-backed, deliberately deferred, or outside the project's scope.

Categorization also must not become task authorization. A category can contain questions at
different levels of readiness, and `OPEN-QUESTIONS.md` is explicitly not a roadmap.

## Current proposal

Keep the existing evidentiary distinctions, but split large sections into topical subsections.
Start with these candidate topics and revise them as items are reviewed:

- task lifecycle and coordination;
- context selection and knowledge boundaries;
- decisions, identity, and traceability;
- verification, evidence, and observable execution;
- distribution, adoption, skills, and host integration;
- product boundary, behavior at scale, and measurement.

Promotion remains item-by-item:

- an evidence-backed gap is the strongest candidate for a task, but still needs an RFC when its
  direction is unsettled;
- a deferred capability becomes a task only when discussion establishes why now;
- a model question usually needs investigation or an RFC before an implementation plan;
- a recurring pattern becomes a task only when its evidence supports a concrete rule or context
  change;
- a question the project will not answer never becomes a context-fold task.

Opening a task does not remove its question from `OPEN-QUESTIONS.md`. The item remains live until a
decision resolves it or it turns out not to matter, as the existing project-layer rule requires.

## Open questions

- Should the document keep evidentiary state as the top-level organization with topical
  subsections, or use topics first and preserve state in prose?
- Are the six proposed topics coherent, or should any be split, combined, or renamed?
- Should we discuss and promote candidates one topical group at a time, starting with the ten
  evidence-backed rule gaps?
- Does promotion require selecting individual questions only, or is there any case where a whole
  tightly-coupled group should share one task?

## Review notes

The initiating discussion established that the RFC-artifact work was a prerequisite, not the
categorization itself. This task exists to finish that original objective without conflating an
organized question list with an execution plan.
