# Record open questions in the project layer

## Status

completed

## Objective

Give the project's unresolved questions and deferred scope a home in the project layer, and
record that they belong there rather than in task packages.

## Why

Open questions have been written into each task's `context.md`. All three tasks so far are
archived, and archived packages are history rather than current truth — so every unresolved
question this project has is buried where the rules say not to look for current state.

The questions themselves also exist mostly outside the repository, in the conversation that
produced the design. They survive only as long as that conversation does.

## Scope

- `OPEN-QUESTIONS.md` — deferred scope, open questions about the model, and known gaps in the
  current rules.
- `decisions/0010-record-open-questions-in-project-layer.md`.
- `decisions/README.md` index row.
- `.agents/tasks/AGENTS.md` — where a task-local question ends and a project question begins.

## Out of scope

- Answering any of the questions.
- Founding decisions not yet recorded — agnosticism, no CLI, problems as first-class
  artifacts. Those follow in their own task.
- Editing archived task packages. Their questions stay as written; the project-layer document
  supersedes them as the live list.

## Acceptance

1. `OPEN-QUESTIONS.md` holds the deferred scope, the unresolved questions about the model, and
   the gaps surfaced by the three completed tasks.
2. Every open question currently living in an archived `context.md` is either present in
   `OPEN-QUESTIONS.md` or deliberately dropped as answered.
3. A decision record states that live open questions belong in the project layer, and that
   task `context.md` holds only questions local to that task.
4. `.agents/tasks/AGENTS.md` reflects the distinction and stays free of project-specific
   detail.
5. Nothing in `OPEN-QUESTIONS.md` restates an answer already recorded in `decisions/`.

## Outcome

`OPEN-QUESTIONS.md` holds the deferred capability, the open questions about the model, and the
five rule gaps found by the three completed tasks. `decisions/0010-record-open-questions-in-project-layer.md`
records that live questions belong in the project layer and that a task's `context.md` keeps
only task-local ones. `.agents/tasks/AGENTS.md` carries the distinction; `README.md` points at
the document rather than listing deferred items itself.

All five acceptance criteria satisfied. The second required comparing the new document against
every archived `context.md`, which found five questions with no counterpart.

Much of what this document holds existed only in the conversation that produced the design.
It is now in the repository.

Nothing was left to fold.

## Problems

### The deferred list was duplicated into README on sight

`README.md` already carried a Status section listing what was deferred — skills, workflows,
learning, adapters, retrieval, distribution — which `OPEN-QUESTIONS.md` then restated.
Assumed: a short summary in the entry point and a full list elsewhere are different things.
Actually: it is the same list twice, and the short one drifts first because nobody updates a
summary when adding an item. Replaced with a pointer.
Sixth instance of this pattern in the project, and the first where the duplication was created
and caught inside the same task.

### Five archived questions were nearly lost in the transfer

Cross-checking the three archived `context.md` files against the new document found five
questions with no counterpart: automatic context selection, context compilation, behavior at
scale, branch protection as enforcement, and whether other derived views follow the index's
rules.
Assumed: writing the list from the source conversation would cover what the tasks had recorded.
Actually: the tasks had accumulated questions the conversation never raised, and the
conversation's list had drifted from theirs. Neither source was complete alone.
Only found because the acceptance criterion demanded the comparison. A criterion asking for
the document to "hold the open questions" would have passed on the first draft.
