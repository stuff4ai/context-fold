# Context — bootstrap-tasks-layer

## Base state

The repository contained only `LICENSE`, `NOTICE`, and `HEADER` when this task started. There
is no prior structure to migrate and no existing convention to preserve.

`HEADER` carries the SPDX source-file header. It applies to source files; Markdown artifacts
in this task do not carry it.

## References

- `decisions/0005-agents-layer-boundary.md` — why `.agents/` is an operating layer and what
  the deletion test is.
- `decisions/0006-task-package-model.md` — what a task package contains and who owns status.
- `decisions/0007-archive-before-merge.md` — why archival happens inside the pull request.

These records are created *by* this task. Until they exist, the decisions they carry live in
this file and in `task.md`.

## Assumptions

- One task package is enough to exercise the layer. The rules are codified from what this
  task actually does, not designed ahead of it.
- Markdown and Git are sufficient. No tooling is needed to make v0 useful.
- The layer is agent-tool agnostic. Nothing here depends on a specific agent product.

## Context conflicts

Four refinements were adopted that diverge from the original design discussion:

- The design left no place to record friction during work, which starves the future learning
  layer of its only input. A `## Problems` section was added to `task.md`.
- A flat slug-only archive has no chronology and collides on repeated slugs, so archived
  directories take a date prefix while active ones stay slug-only.
- `INDEX.md` is a single file every concurrent task edits, so conflicts are expected;
  regeneration replaces manual resolution.
- The "final exact-head check" was an undefined step, so it was given concrete criteria.

Each is recorded in the relevant ADR rather than only here.

## Open questions

Recorded, not answered. Postponing these is deliberate — resolving them before the layer has
been used once would replace evidence with speculation.

- Automatic context selection.
- Context compilation.
- RAG/MCP integration.
- CLI implementation.
- Task index generation.
- External issue tracker synchronization.
- Skill distribution.
- Workflow engine.
- Learning automation. Three constraints were agreed and should survive into whatever this
  becomes: an observation is not automatically a rule; a lesson is a candidate, not a
  decision; and a permanent behavior change requires a reviewed change to `AGENTS.md`, a
  skill, a workflow, or a template. The learning layer must not become a second source of
  truth. Not recorded as a decision record because the layer does not exist yet.
- Metadata schemas and frontmatter.
- Large-scale context optimization.

Two more surfaced while scoping this task:

- How does a task split when it grows too large mid-flight, given that the slug is fixed
  identity once work starts?
- What is the threshold for a decision to deserve an ADR, now that decision records are not
  limited to architecture?

## Not relevant

- Other repositories and their conventions. v0 targets this repository only.
- The eventual product surface. v0 is methodology and repository conventions.
