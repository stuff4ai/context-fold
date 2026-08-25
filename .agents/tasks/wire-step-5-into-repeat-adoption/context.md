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

## Open questions

- Should a catch-up pass run automatically on the next repeat adoption after upgrading
  `ctxfold-init`, or only on explicit request?
- If automatic, what's the gate — zero `assess-project-*` tasks anywhere (any status), a marker
  that step 5 has run at all, something else?
- Does this need new state (e.g., recording in task zero's own package that step 5 ran, and at
  what version) or can it stay evidence-only like step 5 itself?
