# Context — make-the-final-check-verifiable

## Base state

`main` is at `51f6835`. The four gates were defined in `0007` and restated in
`tasks/AGENTS.md`; neither says who runs them or what a pass means.

## References

- `.agents/tasks/AGENTS.md` — `## Final exact-head check`, the four gates as an adopter reads
  them.
- `decisions/0007-archive-before-merge.md` — where the gates originate, as "a concrete gate run
  at the branch head before merge".
- `decisions/0023-approve-the-final-state.md` — puts review after the check, so a false pass now
  reaches a reviewer rather than a merge. That limits the damage and does not fix the check.
- `decisions/0016-check-conventions-in-ci.md` — what this project chose to enforce mechanically,
  and the reasoning about which rules can be.
- `decisions/0011-keep-the-model-vendor-neutral.md` — why the layer cannot impose a toolchain,
  which bounds the available answers.
- `OPEN-QUESTIONS.md` — "Should the convention checks ship with the portable layer?", the larger
  question this one sits inside.

## Evidence

`ctxfold-init` adopting the `etu-forms` monorepo, first run, in an untracked worktree on one
workstation. The transcript is the only record of the run itself; the artifact it left is
readable, and what matters from both is reproduced here.

Gate 3 is "The task directory is under `archive/` with final Status and Outcome set." The run
archived the package with Status `active`, ran a command whose output showed no `completed`
line, and reported `archive and index: CONFIRMED`. The accompanying `test` was
`test "$(rg -l '^## Status$' …/task.md | wc -l)" -eq 1`, which asserts that one file contains a
Status heading.

The second run found and repaired it. The consequence for the precedence rule is
[[fix-index-status-precedence]]; this task is about the check that let it through.

Local corroboration, of two kinds. `approve-after-archival` passed its self-run check and was
then refuted by a fresh verifier, on a contradiction the change had introduced into the file it
was correcting; that is recorded in its own package. `route-findings-without-an-owning-task` was
corrected repeatedly by review after self-checks passed, though its record says only "found in
review" and does not name a verifier — the claim that a verifier refuted it would be more than
the artifacts support.

A third instance is this task's own recording change, which asserted in `OPEN-QUESTIONS.md` that
nothing describes re-entering an adopted repository. `ADOPTING.md` has carried a section titled
"If the layer is already there" since the skill shipped, written by the same author making the
claim. A fresh verifier caught it. None of this is reachable by the four gates as written.

## Assumptions

- The gates are the right four. Nothing observed suggests a missing gate; what is missing is any
  account of what running them proves.

## Open questions

Whether gate 2, the deletion test, is verifiable by anyone at all without removing the layer and
reading what remains, and whether the rule should say so rather than implying a checklist tick.

Whether "unverifiable by the author alone" is a useful category to write into a portable rule, or
whether it invites skipping the gate rather than escalating it.
