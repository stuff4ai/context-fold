# Categorize open questions and identify task candidates

## Status

completed

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
  items; every complete item block and its top-level evidentiary section remain unchanged.
- Separate planned task packages and `.agents/tasks/INDEX.md` rows only for individual questions
  explicitly selected during a later promotion discussion and recorded in the RFC Review notes;
  each new package declares its own scope.
- `.agents/tasks/categorize-open-questions/` and `.agents/tasks/INDEX.md` — this task's discussion,
  status, and navigation lifecycle.

## Out of scope

- Answering an open question merely by categorizing it.
- Adding priority, schedule, ownership, or roadmap metadata to `OPEN-QUESTIONS.md`.
- Promoting every item in a category automatically; task creation remains an item-by-item judgment.
- Creating `plan.md` or implementing work for any derived task before its own direction is resolved.
- Changing portable task rules, lifecycle automation, or the RFC convention.

## Acceptance

1. A reviewed taxonomy accounts for all 59 live items and 2 explicit non-answers without dropping,
   duplicating, answering, changing, or moving any complete item block out of its top-level
   evidentiary section.
2. `OPEN-QUESTIONS.md` is organized into categories small and coherent enough to discuss, while
   preserving the distinction between live questions, evidence-backed gaps, recurring patterns,
   deferred capability, and questions the project will not answer.
3. The resolved RFC explains how categorization differs from promotion and records which kinds of
   item may become investigation, decision, or change tasks.
4. Before any question is promoted, its exact item or inseparable group is recorded in RFC Review
   notes. Every selected question then has its own separate planned task package with `task.md`,
   `context.md`, and a draft `rfc.md`; no derived task has `plan.md` yet.
5. Questions not selected remain live project questions, with no implied priority or schedule.
6. The task index agrees with task directories, and pytest, recursive Markdown lint, and
   `git diff --check` pass.

## Outcome

`OPEN-QUESTIONS.md` now keeps evidentiary state as its top-level organization and groups 57 live
items under eight topical subsections. The two recurring patterns and two explicit non-answers
remain flat, and every existing item block retains its text and evidentiary parent section.

The resolved RFC separates categorization from promotion and defines when individual or
inseparable questions may share a task. No question was selected for promotion in this task, so no
derived task package, priority, owner, schedule, or roadmap state was created.

## Problems

The initial RFC assumed six subject topics could cleanly partition all 59 live items. Review showed
that the recurring patterns, learning-loop questions, and rule-self-consistency gaps did not fit
without arbitrary placement. The resolved proposal uses topical subsections only where useful,
adds two topics for coherent missing clusters, and leaves the small cross-cutting section flat.

The first plan review found that the proposed mapping incorrectly included the two recurring
patterns among the topically assigned population, and that comparing labels could not detect body
or evidentiary-state changes. It also found that derived-task creation depended on a future user
choice. The plan now pins the complete before-state, compares full item blocks with their parent
sections, and stops the current slice before any derived task or index change.

Running pytest after moving the task but before staging the rename made its Markdown-file inventory
name the four old tracked paths, which no longer existed, so the link test failed with four
`FileNotFoundError`s. Staging the exact archive rename makes the inventory reflect the final
snapshot; verification must run after that point.
