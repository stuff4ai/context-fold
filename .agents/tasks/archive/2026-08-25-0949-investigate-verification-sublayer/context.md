# Context — investigate a verification sublayer

## References

- `decisions/0006-task-package-model.md` keeps execution history out of task packages.
- `decisions/0014-do-not-store-source-material.md` rejects raw source material as a second truth.
- `decisions/0027-produce-evidence-at-the-final-check.md` defines evidence required before review.
- `OPEN-QUESTIONS.md` asks about behavior scenarios, agent-system evals, observable run facts,
  reproducibility, executable gates and semantic diagnostics.

## Assumptions

- The investigation does not presume that `.agents/verification/` should exist.

## Open questions

- Which consumers need persisted agent-run evidence rather than a task's final-check report?
- Can agent evaluations be portable without fixing a runtime, model or tool schema?
- Is a verification index merely another context map, or does it own executable gate state?
- What can replay verify without promising deterministic model output?
