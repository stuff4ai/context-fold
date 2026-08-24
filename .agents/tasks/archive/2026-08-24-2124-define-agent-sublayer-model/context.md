# Context — define the agent sublayer model

## References

- `README.md` states the current two ownership layers and deletion test.
- `decisions/0005-agents-layer-boundary.md` separates project truth from agent operating state.
- `decisions/0018-ship-a-distribution.md` distinguishes the layer from the shared `.agents/`
  directory.
- `decisions/0026-map-what-is-under-the-agents-directory.md` rejects calling tasks, skills and
  worktrees three layers and records their different owners.
- `decisions/0035-manage-portable-rules-as-replaceable-blocks.md` defines managed contracts and
  project-owned suffixes.
- `OPEN-QUESTIONS.md` asks whether the two ownership layers need a more detailed responsibility
  map.

## External evidence

- `/home/alexengrig/etu/gitlab/it/etu-forms/monorepo/.agents/worktrees/add-context-fold` is a
  disposable adopter fixture. At the start of this task it was clean at `d0f902a`, with no root
  `AGENTS.md` or `.agents/`. Its project truth is distributed across root, backend and frontend
  READMEs, system ADRs under `docs/adr/`, a backend ADR, code and tests; it has no dedicated PRD or
  system-architecture document.
- The fixture is evidence for installation and update behavior, not a durable dependency. No
  experimental fixture change is committed, and the paired scenario must restore its exact clean
  baseline after the repeat run.

## Open questions

- Can context-fold govern a sublayer contract without claiming the tool- or project-owned contents?
- Is a governed namespace compatible with leaving unknown `.agents/` extensions untouched?
- Which concerns are physical sublayers, and which remain cross-cutting processes or projections?
