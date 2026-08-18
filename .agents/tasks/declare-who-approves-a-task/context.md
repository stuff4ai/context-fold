# Context — declare-who-approves-a-task

## Base state

`main` is at `23e49e6`. Two other `planned` tasks are queued:
`decide-whether-the-task-template-earns-its-place` and `make-the-final-check-verifiable`. Neither
blocks this one and neither is blocked by it.

## References

- `decisions/0019-agents-may-merge-after-approval.md:30` — the sentence this narrows: "An agent
  may merge a pull request once a human has approved it."
- `decisions/0023-approve-the-final-state.md` — speaks of "review" and "a reviewer" without naming
  a human anywhere; may need no change at all. Confirm rather than assume.
- `decisions/0006-task-package-model.md` — `task.md`'s defined sections and the precedent for
  narrowing a record's Status rather than rewriting its body.
- `decisions/0025-run-tasks-in-parallel.md` — `## Blocked by` is the precedent for a declared,
  optional, judged `task.md` section. This follows the same shape.
- `decisions/0016-check-conventions-in-ci.md` — what this project already chooses to enforce
  mechanically. Bounds what this task should promise to check versus merely state.
- `decisions/0012-build-the-methodology-before-the-tooling.md` — do not write rules for risks that
  have not been observed in this project's own history.
- This session's own record, informally: roughly a dozen verifier passes across pull requests
  17–22, at least one real finding in every pull request that reached a verifier, none of it
  reachable by the 235 checks CI already runs. The direct evidence behind trusting a fresh
  verifier's `CONFIRMED` as a substitute for a human's eyes, rather than for the agent's own.

## Assumptions

- One human reviewer, for the foreseeable future. Nothing here assumes or creates multiple
  approvers.
- "Trust" is procedural, not self-assessed. `0019` already says "an agent that has not been
  approved does not merge" — this task narrows what counts as approval; it does not let an agent
  approve itself. A verifier is fresh-context by definition, never the task's own author.

## Open questions

Whether a check should confirm that an agent-approved merge actually carried a `CONFIRMED`
verdict, traceable from the pull request or the Outcome. Deferred — out of scope here, and it may
turn out that the Outcome recording it, as this session's tasks already do by habit, is enough
without a check forcing it.

Whether `0023` needs a cross-reference to this at all, given its language already covers a
non-human reviewer without saying so explicitly. A judgment call for whoever starts this task,
not settled here.
