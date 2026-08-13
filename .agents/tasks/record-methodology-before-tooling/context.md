# Context — record-methodology-before-tooling

## Base state

`main` is at `ec82d91`. Eleven decision records, five archived tasks, no active work.

Five tasks have now been completed using the methodology, which is the entire evidence base
for it.

## References

- `decisions/0011-keep-the-model-vendor-neutral.md` — neutrality is why tooling would have to
  be written rather than adopted, which raises its cost and supports deferring it.
- `OPEN-QUESTIONS.md` — currently lists a CLI under deferred capability, wording that does not
  distinguish "not yet built" from "deliberately not built".
- `README.md` — the Status section already states there is no CLI and that the goal is to find
  out which parts earn their keep. That is the consequence; this task records the decision.

## Assumptions

- Skills as the eventual vehicle is intent rather than decision. It was reached before any of
  the current structure existed and has not been tested, so it belongs in open questions
  rather than in the record.
- The self-adoption constraint is genuinely load-bearing: it produced the bootstrap ordering
  of the first task, and every problem found there came from following it.

## Context conflicts

The source describes v1 as "context-fold methodology plus Agent Skills plus repository
conventions", implying skills would exist by now. They do not, and the numbering it uses does
not match this repository's. The record states the ordering that survived rather than the plan
as originally phrased.

## Open questions

Whether the eventual tooling should be skills, a CLI, or neither is not settled here. This
task records that tooling comes second, not what it will be.
