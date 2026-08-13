# Context — record-vendor-neutrality

## Base state

`main` is at `d12e838`. Ten decision records, four archived tasks, no active work.

## References

- `decisions/0005-agents-layer-boundary.md` — mentions that the layer does not prescribe where
  project artifacts live, and that context-fold adapts to an existing layout. That is the
  boundary's consequence of neutrality, not the commitment itself.
- `OPEN-QUESTIONS.md` — lists adapters as deferred and describes the canonical model as
  vendor-neutral in passing, which is currently the only written trace of the commitment.
- `.agents/tasks/AGENTS.md` — the portable rule file whose existence this decision explains.

## Assumptions

- The commitment is genuinely settled rather than a preference. It has already constrained
  four tasks' worth of work, and reversing it would invalidate the portable/instance split.
- Naming products in the record is safe as history — what was surveyed — but not as policy.

## Context conflicts

The source describes the vendor survey as covering Claude, Cursor, Codex, GitHub Copilot, and
JetBrains tooling. Those conventions have almost certainly changed since. The record states
what was surveyed and when, not what those tools do now, so it does not decay into a wrong
claim about anyone's product.

## Open questions

Whether adapters will ever be built is not decided here and stays in `OPEN-QUESTIONS.md`.
This task records why they are deferred rather than simply absent.
