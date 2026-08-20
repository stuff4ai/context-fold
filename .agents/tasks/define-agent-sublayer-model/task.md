# Define the agent sublayer model

## Status

planned

## Objective

Decide whether `.agents/` should become a governed set of agent sublayers with a goal-oriented
entry point and a contract for each recognized sublayer.

## Why

The current model deliberately treats tasks, skills and worktrees as three things with different
owners rather than three layers. The proposed model would instead let context-fold govern the
namespace and each sublayer boundary without necessarily owning every file inside it. That change
needs an explicit ownership model before any new sublayer is added.

## Scope

- `OPEN-QUESTIONS.md` — the detailed-responsibility-map item under context selection and knowledge
  boundaries.
- `README.md`, `.agents/AGENTS.md` and accepted decisions that define the layer, distribution and
  `.agents/` ownership, if the RFC selects a change.
- The definition, ownership and routing contract shared by downstream sublayer tasks.

## Out of scope

- Designing the contents of context, skills or verification sublayers.
- Project-layer assessment during adoption.
- Implementing workflows, MCP/tool layers, host adapters or a runtime harness.

## Acceptance

1. A resolved RFC defines whether sublayers exist, what makes one a sublayer, what context-fold
   owns, and how extensions coexist.
2. The resolution preserves the project-truth deletion test and identifies every accepted decision
   it keeps, narrows or supersedes.
3. `.agents/AGENTS.md` has one unambiguous routing role if the governed-sublayer model is selected.
4. Dependent planned tasks are reconciled with the selected model before this task completes.

## Approval

Human.
