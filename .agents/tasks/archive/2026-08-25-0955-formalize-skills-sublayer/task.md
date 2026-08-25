---
status: completed
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

## Outcome

The RFC resolved by refining the `skills/` sublayer contract in place rather than building new
infrastructure. The evidence — two installed packages, the Claude Code host adapter, and the
shipped-skill portability check — already answered three of the four axes empirically:

- **Authority**: a package's own `AGENTS.md`/`SKILL.md` governs its own procedure but never
  raises the layer's permission ceiling, overrides project instructions, or supersedes the
  sublayer contract.
- **Discovery**: no manifest or common format is required; an agent reads a package's own entry
  point.
- **Host projection**: any host-specific path into `skills/` is a non-owning pointer, never
  distributed by context-fold, generalizing `0034`'s Claude Code symlink rather than adding a
  second mechanism.
- **Ownership and coexistence**: unchanged from `0026`/`0041` — preserve, never hide or classify,
  what the contract does not own.

**Provenance** did not clear the evidence bar: no installed package has failed or gone stale for
want of recorded provenance, so the resolution declines to require it and states named reopening
conditions instead, mirroring `0044`'s treatment of the context sublayer.

Durable artifacts produced:

- `decisions/0048-formalize-the-skills-sublayer.md`, recording the resolution.
- `decisions/README.md` — index row for `0045`.
- `decisions/0041-define-governed-agent-sublayers.md` — `Status` narrowed to point at `0045` for
  the detailed skills semantics it routed here.
- The `skills/` sublayer contract, updated in all three copies the distribution keeps in sync:
  `skills/ctxfold-init/templates/agents/skills/AGENTS.md` (source template),
  `.agents/skills/ctxfold-init/templates/agents/skills/AGENTS.md` (this repository's own
  installed copy of the skill that distributes it), and `.agents/skills/AGENTS.md` (this
  repository's active installation of the contract itself).
- `OPEN-QUESTIONS.md` — removed the now-answered "How should the recognized skills sublayer be
  formalized?" item; narrowed the "Further skills and workflows" and "Versioning, provenance,
  discovery, and upgrades" items to note what `0045` settles and the reopening bar it leaves for
  skill provenance specifically.

Existing installed packages (`ctxfold-init`, `ctxfold-tasks`) were not rewritten or relocated;
`tests/` and `pymarkdown` both pass against the finished state.

## Problems

- `pip install -r requirements-dev.txt` was blocked by the sandbox's auto-mode classifier before
  it ran. A prior session had already provisioned `/tmp/ctxfold-venv` with the dev dependencies,
  so `pytest` ran from there instead; a repository with no such venv would need a human to
  install dependencies before the suite can run in this sandbox.
