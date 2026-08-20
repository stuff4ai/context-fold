# Categorize open questions and identify task candidates

## Status

active

## Objective

Organize the live open questions into useful categories, discuss how each category should be
handled, and identify individual questions that should become separate planned tasks.

## Why

`OPEN-QUESTIONS.md` currently holds 59 live items. Its broad sections distinguish deferred
capability, model uncertainty, evidence-backed rule gaps, and recurring patterns, but the
35-question model section is too large to discuss coherently as one group. The list is navigable as
a record of uncertainty, not yet as a set of manageable conversations.

The original discussion intended to split these questions into categories and decide which could
move into task planning. That work was explicitly left out of the RFC-artifact task. Now that
`rfc.md` has a defined role, this task can hold the mutable taxonomy and promotion discussion
without turning `OPEN-QUESTIONS.md` into a roadmap or creating execution plans prematurely.

## Scope

- `OPEN-QUESTIONS.md` — heading hierarchy, category introductions, and placement of existing live
  items; wording changes only when needed to keep meaning and transitions accurate after grouping.
- Separate planned task packages and `.agents/tasks/INDEX.md` rows only for individual questions
  explicitly selected during RFC resolution; each new package declares its own scope.
- `.agents/tasks/categorize-open-questions/` and `.agents/tasks/INDEX.md` — this task's discussion,
  status, and navigation lifecycle.

## Out of scope

- Answering an open question merely by categorizing it.
- Adding priority, schedule, ownership, or roadmap metadata to `OPEN-QUESTIONS.md`.
- Promoting every item in a category automatically; task creation remains an item-by-item judgment.
- Creating `plan.md` or implementing work for any derived task before its own direction is resolved.
- Changing portable task rules, lifecycle automation, or the RFC convention.

## Acceptance

1. A reviewed taxonomy accounts for every currently live item without silently dropping,
   duplicating, answering, or changing its meaning.
2. `OPEN-QUESTIONS.md` is organized into categories small and coherent enough to discuss, while
   preserving the distinction between live questions, evidence-backed gaps, recurring patterns,
   deferred capability, and questions the project will not answer.
3. The resolved RFC explains how categorization differs from promotion and records which kinds of
   item may become investigation, decision, or change tasks.
4. Every question explicitly selected for promotion has its own separate planned task package with
   `task.md`, `context.md`, and a draft `rfc.md`; no derived task has `plan.md` yet.
5. Questions not selected remain live project questions, with no implied priority or schedule.
6. The task index agrees with task directories, and pytest, recursive Markdown lint, and
   `git diff --check` pass.
