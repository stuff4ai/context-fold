# Park the agent sublayer model

## Status

completed

## Objective

Preserve the discussed agent-sublayer and project-assessment directions as neutral live questions
and separate planned discussion tasks.

## Why

The discussion distinguishes a governed agent namespace from advisory project-layer preparation,
and identifies context, skills, verification, health and initialization concerns worth examining.
Those directions should remain visible without silently replacing the accepted two-layer boundary
or treating proposed directories and workflows as decided.

## Scope

- `OPEN-QUESTIONS.md` — the context-selection, verification, distribution/adoption, product-boundary
  and learning sections only; preserve deferred layer and assessment candidates without assigning
  schedule or priority.
- `.agents/tasks/` — six separate planned discussion packages for the selected questions, this
  task's package, and the corresponding derived index rows.

## Out of scope

- The task-lifecycle section of `OPEN-QUESTIONS.md`, owned by the concurrent
  `replace-task-index` task.
- Accepting or superseding the current ownership model, adding agent sublayer directories, or
  changing portable rules, adoption behavior, skills, checks or project structure.
- Creating execution plans for any parked task.
- Workflows, MCP/tool layers, operations, security, data, release or integration assessment beyond
  preserving them as future questions.

## Acceptance

1. The governed-namespace proposal and its boundary with project-owned truth are represented as
   neutral live questions grounded in accepted repository decisions.
2. The six selected discussions have separate `planned` task packages with self-contained scope,
   evidence references and draft RFCs, and none has an execution plan.
3. Deferred agent-layer and project-assessment candidates remain visible without being promoted to
   tasks, priorities or implementation commitments.
4. The task index agrees with all active task directories, and repository checks pass.

## Outcome

`OPEN-QUESTIONS.md` now preserves the governed-namespace, context, skills, verification, health,
project-assessment and deferred-catalog directions as neutral questions grounded in the current
model. Six separate planned packages carry draft RFCs for the discussions explicitly selected;
none has a resolution or execution plan. The accepted ownership model, portable rules, adoption
behavior and repository structure remain unchanged.

## Problems

### A concurrent task will replace the task index and task metadata format

The `replace-task-index` worktree owns the task-lifecycle open-question section and plans to
migrate every task package after another pull request resolves. This task avoids its authored
open-question scope and records new packages in the format required by the current `main`; the
replacement task will need to include them in its later mechanical migration if it lands second.

### The first Markdown command ignored the repository configuration

Running `pymarkdown scan --recurse .` used the tool's defaults and reported thousands of existing
80-column and skill-frontmatter violations. The repository CI command supplies
`.pymarkdown.json`; rerunning that exact command tests the intended rules instead of the defaults.

### The first final-check loop assumed POSIX scalar splitting

The shell is zsh, so a space-separated scalar of task slugs stayed one word and produced one
combined nonexistent path. Declaring the slugs as a shell array made the loop check each planned
package independently.
