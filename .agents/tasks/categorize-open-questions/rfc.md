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

A review pass placed all 59 live items under the six candidate topics. Every Deferred-capability
and Gaps-in-the-current-rules item found an unambiguous home. Three clusters did not:

- The two Recurring-patterns entries — symmetry treated as a reason on its own, and rules
  stated where they are relevant rather than where they are owned — describe a property of how
  rules get written across the project, not a subject any one topic owns. Assigning either to a
  topic would give it a home by force, not by fit.
- "Should lessons become a first-class project artifact?" and "Automating the loop" form a
  small learning cluster. Task lifecycle and coordination is the closest of the six, but only
  because the fold step happens during finishing, not because the question is about lifecycle or
  coordination.
- A rule-self-consistency cluster in Gaps — the undetected `0007` contradiction, the uncaught
  wrong citation, the pull request description outside every check, the unenforced 98-column
  wrap, and the unbound `INDEX.md` header — splits close to evenly between "decisions, identity,
  and traceability" and "verification, evidence, and observable execution." Each entry could sit
  in either without a clear tiebreaker.

This means the six topics are subject-coherent for most of the list but not a clean partition of
all of it. Before subsections are cut into `OPEN-QUESTIONS.md`, it is worth deciding explicitly
whether every item must land under exactly one topic, or whether a small number of genuinely
cross-cutting items get an explicit allowance rather than a forced placement.

On the RFC's first open question: keeping evidentiary state as the top-level organization, with
topics as subsections, avoids re-deriving each item's evidentiary status in prose alongside its
topic — the topical split only has to do one job, not two. That favors the proposal's current
direction over flipping the two axes.

On the third open question: the ten evidence-backed gaps do not cluster under one or two
topics — they already spread across at least four of the six (decisions and traceability, task
lifecycle, verification, distribution). Starting the promotion discussion there surfaces the
cross-cutting problem immediately rather than easing into it with a more topically coherent
group first. That is a reason to choose the starting group deliberately, not a reason to avoid
the gaps.
