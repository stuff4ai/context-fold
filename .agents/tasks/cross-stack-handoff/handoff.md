# Handoff — cross-stack handoff

Exchanges between agent stacks working this task. Append-only: a new exchange is a new
section, and a return is written into its own entry rather than replacing the request.

---

## 001

```yaml
id: 001
from: claude:lead
to: codex:plan-verifier
state: returned
rev: 9a668f0
returns: READY|REVISE
```

### Request

**Objective** — Decide whether `.agents/tasks/cross-stack-handoff/rfc.md` is ready to be
resolved in favour of Alternative B, stating the handoff convention as this repository's
project suffix rather than adding it to the portable managed rule block.

**Scope** — `.agents/tasks/cross-stack-handoff/rfc.md`, `.agents/tasks/cross-stack-handoff/task.md`,
`.agents/tasks/cross-stack-handoff/context.md`. The decisions they rest on:
`decisions/0006-task-package-model.md`, `decisions/0011-keep-the-model-vendor-neutral.md`,
`decisions/0012-build-the-methodology-before-the-tooling.md`,
`decisions/0035-manage-portable-rules-as-replaceable-blocks.md`.

**Non-goals** — Do not judge the note format's field list; that is settled enough to try.
Do not propose tooling. Do not edit any file.

**Acceptance** — A reader who was not present can tell, from the RFC alone, why the
convention was placed where it was and what evidence would move it. The argument against
Alternative A must be one this project's own decisions actually support, not a preference.

**Read first** — `.agents/tasks/cross-stack-handoff/rfc.md`, then the four decision records
named above, then `.agents/tasks/AGENTS.md` for what a package may contain today.

### Return

Answered by `codex:plan-verifier` (pilotfish-codex v1.7.1, `gpt-5.6-sol`, reasoning effort
high, read-only sandbox), against `9a668f0`.

Verdict: `REVISE`, with two blockers, quoted in full:

> Blocker: The argument against Alternative A overstates what decision 0006 supports.
>
> Evidence: The RFC makes `handoff.md` optional but equates documenting it portably with
> creating a fifth artifact in every task. Decision 0006 does not support that inference;
> decision 0012 supplies the relevant exercise-before-portability rationale.
>
> Minimum revision: Ground the deferral in decision 0012 and distinguish distributing an
> optional rule from creating an artifact in every package.
>
> Acceptance check: The argument against Alternative A follows directly from an accepted
> decision without claiming every task would contain `handoff.md`.
>
> Blocker: The RFC does not state what evidence would justify reconsidering promotion.
>
> Evidence: It promises future evidence but identifies no observation or threshold that
> would move the convention from the project suffix to the portable block.
>
> Minimum revision: State the concrete evidence that would trigger reconsideration without
> deciding promotion now.
>
> Acceptance check: From the RFC alone, a reader can identify both the evidence currently
> missing and the observable evidence that would reopen Alternative A.

Both blockers accepted; neither disputed. The RFC was revised and resolved against them.

**Transport note.** Rule 5 says the asking stack stops and something outside the repository
moves the work. Here the Claude lead invoked the Codex stack itself rather than waiting for
a person to switch terminals. The verdict is genuinely the other stack's — a different
product, model and role, reaching a conclusion this task did not write for it — but the
handoff did not cross a human. Recorded as a problem in `task.md` rather than presented as
the convention working end to end.
