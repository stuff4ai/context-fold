# Context — define the context sublayer

## References

- `decisions/0005-agents-layer-boundary.md` keeps durable project knowledge outside the layer and
  deliberately omits `.agents/context/` from v0.
- `decisions/0006-task-package-model.md` defines task `context.md` as a curated map by reference.
- `decisions/0010-record-open-questions-in-project-layer.md` keeps durable unknowns visible outside
  archived task packages.
- `OPEN-QUESTIONS.md` records unresolved context discovery, selection, compilation, history,
  provenance and projection questions.

## Assumptions

- The initial proposal contains only navigational summaries and references; it does not store
  reusable domain facts or decisions.

## Open questions

- Does the map need a fixed filename such as `INDEX.md`, or only a contract for whatever the
  project chooses?
- Is the map authored, derived, or a mixture whose ownership must be marked per entry?
- How can a summary be checked for drift without making its source format prescriptive?
