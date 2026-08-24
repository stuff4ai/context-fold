---
status: planned
objective: >-
  Define authority, provenance, discovery and host projection for the recognized skills sublayer
  while preserving independently owned packages.
---

# Formalize the skills sublayer

## Why

This repository already installs `ctxfold-init` under `.agents/skills/`, and host adapters can
expose that directory. The parent agent-sublayer model now recognizes `skills/` as an
interoperability sublayer while keeping each installed procedure independently owned. This task
defines the detailed semantics that the minimal portable contract intentionally leaves open.

## Scope

- `OPEN-QUESTIONS.md` — the skills-sublayer question under distribution, adoption, skills and host
  integration.
- Skill authority, provenance, discovery, host projection, and coexistence within the recognized
  skills sublayer.
- Portable files, templates, adoption guidance, adapters and checks only after RFC resolution.

## Out of scope

- Defining workflow, MCP or general tool sublayers in v0.
- Standardizing a skill format beyond what the selected contract demonstrably requires.
- Rewriting or relocating installed skill packages.

## Acceptance

1. A resolved RFC refines the recognized skills sublayer's authority, provenance, discovery,
   projection, and package-ownership semantics without re-deciding whether it is recognized.
2. Existing project and tool-installed skills remain intact and usable through supported host
   projections.
3. The resolution states what authority a skill has, how it relates to task scope, and whether
   installation provenance is required.
4. Any portable files, adoption changes and checks required by the resolution are complete.

## Approval

Human.
