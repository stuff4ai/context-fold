---
status: planned
objective: >-
  Decide whether `.agents/skills/` should have a portable sublayer contract while preserving the
  ownership and contents of skills installed by projects and tools.
---

# Formalize the skills sublayer

## Why

This repository already installs `ctxfold-init` under `.agents/skills/`, and host adapters can
expose that directory. The current agent-layer map deliberately says skills are not the layer's.
A sublayer contract could explain discovery, authority and coexistence without making
context-fold the owner of every installed procedure.

## Scope

- `OPEN-QUESTIONS.md` — the skills-sublayer question under distribution, adoption, skills and host
  integration.
- The boundary between portable skills-layer instructions and independently owned skill packages.
- Portable files, templates, adoption guidance, adapters and checks only after RFC resolution.

## Out of scope

- Defining workflow, MCP or general tool sublayers in v0.
- Standardizing a skill format beyond what the selected contract demonstrably requires.
- Rewriting or relocating installed skill packages.

## Blocked by

- `define-agent-sublayer-model` must define whether context-fold can govern a contract without
  owning a sublayer's contents.

## Acceptance

1. A resolved RFC decides whether skills are a recognized sublayer and defines ownership of its
   contract and contents.
2. Existing project and tool-installed skills remain intact and usable through supported host
   projections.
3. The resolution states what authority a skill has, how it relates to task scope, and whether
   installation provenance is required.
4. Any portable files, adoption changes and checks required by the resolution are complete.

## Approval

Human.
