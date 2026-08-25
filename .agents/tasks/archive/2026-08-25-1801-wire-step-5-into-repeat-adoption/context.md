# Context — wire step 5 into repeat adoption

## References

- `skills/ctxfold-init/ADOPTING.md` — "If the layer is already there" (repeat-run section) and
  "## 5. Assess project-layer capabilities" (task-zero-only section).
- `decisions/0046-adopt-project-assessment.md` — Consequences claims re-adoption does not
  duplicate an existing `assess-project-{capability}` task; the mechanism that claim assumes
  isn't wired into the repeat-run path.
- PR #53 (`https://github.com/stuff4ai/context-fold/pull/53`) — comment thread where this was
  found and reported, on the `etu-forms/monorepo` fixture, before that PR merged.

## Base state

`ADOPTING.md`'s repeat-run section preflights and updates only the five managed `AGENTS.md`
targets; it explicitly says to leave task packages alone and not reopen task zero. Step 5's own
text places it inside task zero's sequence ("Before finishing it, do step 5 below"), with no
other entry point. A fresh adoption today gets step 5 exactly once, at task zero; every
subsequent repeat run gets none, regardless of whether step 5 existed at the time of the
original task zero.

## Resolved

Automatic, gated on three signals rather than one: an `assess-project-*` package, a
`project-capability-catchup` package, or task zero's own "Project-capability assessment" section
— any one existing means step 5 has already run. No new persistent state: the gate reuses
evidence the layer already produces. See `decisions/0049-wire-step-5-into-repeat-adoption.md` and
this task's Outcome.
