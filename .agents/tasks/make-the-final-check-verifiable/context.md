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

`ctxfold-init` against `etu-forms`, first run, in
`/home/alexengrig/etu/gitlab/it/etu-forms/monorepo/.agents/worktrees/add-context-fold`.

Gate 3 is "The task directory is under `archive/` with final Status and Outcome set." The run
archived the package with Status `active`, ran a command whose output showed no `completed`
line, and reported `archive and index: CONFIRMED`. The accompanying `test` was
`test "$(rg -l '^## Status$' …/task.md | wc -l)" -eq 1`, which asserts that one file contains a
Status heading.

The second run found and repaired it. The consequence for the precedence rule is
[[fix-index-status-precedence]]; this task is about the check that let it through.

Local corroboration: `route-findings-without-an-owning-task` and `approve-after-archival` both
passed a self-run check and were then refuted by a fresh verifier — the first on two stranded
statements, the second on a contradiction the change had introduced into the file it was
correcting. Neither is reachable by the four gates as written.

## Assumptions

- The gates are the right four. Nothing observed suggests a missing gate; what is missing is any
  account of what running them proves.

## Open questions

Whether gate 2, the deletion test, is verifiable by anyone at all without removing the layer and
reading what remains, and whether the rule should say so rather than implying a checklist tick.

Whether "unverifiable by the author alone" is a useful category to write into a portable rule, or
whether it invites skipping the gate rather than escalating it.
