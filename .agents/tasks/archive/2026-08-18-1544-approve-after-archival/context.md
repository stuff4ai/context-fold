# Context — approve-after-archival

## Base state

`main` is at `eb36902`. Twenty-three decision records, seventeen archived tasks, one `planned`
task carried over. Every merge so far has approved the work before the Outcome existed.

## References

- `decisions/0007-archive-before-merge.md` — the record this corrects. Its Decision orders
  approval fourth; its Consequences twice assume review comes after archival.
- `decisions/0019-agents-may-merge-after-approval.md` — "Approval authorizes everything
  downstream: folding outcomes, archiving the task, the final exact-head check, and the merge
  itself." That sentence is what makes the gap reachable by an agent working alone.
- `decisions/0015-stages-are-not-one-way.md` — going back is normal, so review finding something
  after archival needs no new machinery.
- `decisions/0013-improve-context-from-the-work.md` — the Outcome and the promotion of problems
  are the loop's product, and the part nothing verifies.
- `.agents/tasks/AGENTS.md` — `## Stages` and `## Finishing` disagree with each other about when
  acceptance happens.
- `skills/ctxfold-init/SKILL.md` — tells an adopting agent to stop before archiving.
- `skills/ctxfold-init/ADOPTING.md` — same instruction, in the canonical procedure.
- `.agents/tasks/archive/2026-08-18-1518-route-findings-without-an-owning-task/task.md` — the
  most recent instance: Outcome and four `OPEN-QUESTIONS.md` promotions merged unread.

## Assumptions

- A reviewer looking at a pull request that already contains the archival rename can still read
  it. `0007` records the diff noise as a known cost of archiving before merge, and that cost is
  unchanged by moving the gate — the rename is in the diff either way.
- Iterative review during the work continues to happen and is not a stage that needs defining.
  `0015` already covers going back.

## Context conflicts

`0019` says approval authorizes folding, archival, the final check and the merge. Under the
corrected order it authorizes only the merge, because everything else has already happened. This
narrows `0019` without touching its decision that an agent may merge at all.

`OPEN-QUESTIONS.md` states that moving approval after archival "would contradict `0007`". That is
the assessment this task refutes, and the entry is removed rather than corrected, because the
question it asks is answered.

## Open questions

Whether `review` should remain a separate stage before `fold outcomes` once `approved` moves to
the end, or whether the two collapse into one gate at the final state. Leaving `review` in place
preserves early feedback; collapsing them is simpler and matches what `0007`'s Consequences
describe. This is the one design choice in the task and it is not yet made.
