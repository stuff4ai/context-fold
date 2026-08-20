---
status: completed
objective: >-
  Let a task declare that a fresh verifier's `CONFIRMED` verdict is sufficient to merge it, without
  a human. Default to requiring a human when a task says nothing, and give an agent opening a task
  on its own something to judge by when it chooses.
---

# Declare who approves a task

## Why

`0019` hard-codes the only path to merge authorization: "An agent may merge a pull request once a
human has approved it." Every task, regardless of size or risk, waits on the same one person.
That makes a human a bus factor for a project whose own model is meant to let work continue
without depending on any one agent, tool, or — by extension — constant availability.

The proposal is narrower than removing the gate. A task may declare itself verifier-approved, in
which case a fresh verifier's `CONFIRMED` verdict against that task's own acceptance criteria
substitutes for a human's approval before merge. A task that declares nothing still needs a
human, exactly as today — the default does not move, only the option to opt out does.

The trust this extends does not reach as far as skipping verification. What this session
demonstrated, repeatedly, is that the agent who wrote a change cannot be the one who confirms it:
across five pull requests this session, a fresh verifier found something in every one, and none
of it was reachable by the 235 mechanical checks CI already runs. A merge without a human still
needs the one thing that kept working — a reader who did not write the change.

Deciding which mode fits a task is not free, and it should not be a coin flip left to whichever
agent opens the task. `## Blocked by` set a precedent for a declared, judged, optional section;
this needs the same, plus criteria for the judgment itself. An agent opening a task on its own has
to be able to look at what it is about to do and say which one applies, the way it already judges
`## Scope` and `## Out of scope`.

## Scope

- `templates/agents/tasks/AGENTS.md` — an optional `## Approval` section in `task.md`, its two
  values, and criteria for judging which fits a task an agent opens on its own.
- Reinstall `.agents/` from the above.
- Root `AGENTS.md` — this project's default: human approval required unless a task's own
  `## Approval` says otherwise.
- `decisions/0019-agents-may-merge-after-approval.md` — narrow "once a human has approved it" to
  admit a fresh verifier's `CONFIRMED` verdict, when the task and the project's default agree it
  applies.
- `decisions/0023-approve-the-final-state.md` — its Decision needed nothing, but a Consequence
  stated the old norm as universal; narrow that too.
- A new decision record.

## Out of scope

- This task's own merge. It goes through approval as the rule stands today — a human's — because
  the exception it creates does not exist until this lands. No task authorizes its own bypass.
- A mechanical check that an agent-approved merge actually carried a `CONFIRMED` verdict. Worth
  having; a question for whatever `0016` should enforce next, not a requirement of this task.
- Reclassifying any task already planned, active, or archived.
- Categories this project has no evidence for yet — security-sensitive work, destructive
  operations, anything with a blast radius beyond this repository. None of that has occurred in
  this project's own history, and `0012` warns against writing rules for risks that have not been
  observed. If they arise, they are their own task.

## Acceptance

1. `## Approval` is an optional `task.md` section; its absence means the project default from
   root `AGENTS.md` applies.
2. Root `AGENTS.md` states the default explicitly — human required — and a task's own
   `## Approval` overrides it.
3. The rules give an agent something to judge a task's approval mode by, not a bare choice
   between two words.
4. A verifier-approved task cannot merge on a self-run check. The rules state, not imply, that a
   fresh verifier's `CONFIRMED` verdict is what substitutes for a human.
5. `0019`'s Status records the narrowing. Its two other claims — an agent may merge once approved,
   and pushing directly to `main` remains forbidden regardless — stand unchanged.
6. This task's own pull request is approved by a human, matching every task before it.

## Outcome

A task's `## Approval` now declares who satisfies review and approval: `Human`, the project
default when a task says nothing, or `Verifier`, a fresh verifier's `CONFIRMED` verdict against
the task's own acceptance criteria. Declared when the task is written, alongside `## Scope`, not
mid-flight — a task changing its own approval mode partway through is exempting itself from the
thing that would have caught the change.

Two kinds of task keep a human regardless of the project's default: one whose scope is the
approval mechanism itself, which cannot authorize its own bypass, and one whose acceptance
criteria leave a real, undecided choice rather than a checkable claim — a verifier confirms or
refutes a claim and has nothing to return against an open question. Everything else is a
judgment call for whoever writes the task, the same as `## Scope` and `## Blocked by` already
are.

Root `AGENTS.md` states the default explicitly. `0019`'s Status records the narrowing; its two
other claims — an agent may merge once approved, an unapproved agent may not — stand unchanged.

`0023` needed a narrowing I had not scoped in advance. Its Decision already spoke of "review" and
"a reviewer" without naming a human, so nothing there needed touching — but its Consequences
stated "What a human approves is what merges" as a universal, which this task makes one of two.
Found by sweeping for every remaining statement of the old rule rather than trusting the task's
own prepared Scope list, and added once found.

`SKILL.md` and `ADOPTING.md` needed nothing: task zero has no project default to inherit, since
the pointer it establishes doesn't exist until task zero completes, so it is definitionally
human-approved without needing an explicit override.

Durable artifacts:

- `decisions/0028-let-a-task-declare-its-own-approver.md` — the decision.
- `decisions/0019-agents-may-merge-after-approval.md` — Status: who may give approval, narrowed.
- `decisions/0023-approve-the-final-state.md` — Status: the Consequence stating the old universal,
  narrowed alongside it.
- `skills/ctxfold-init/templates/agents/tasks/AGENTS.md` — a new `## Who approves` section, and
  cross-references from `## The files` and `## Finishing`.
- `AGENTS.md` — the project's stated default.

This task's own pull request is approved by a human. It carries no `## Approval` section, which
means it defaults to the rule it is itself writing — the first real instance of the default,
rather than an exception argued for it.

## Problems

### The prepared Scope list didn't anticipate the second record that needed narrowing

Scope named `0019` as the record to narrow. Sweeping for every other statement of "a human has
approved it" after the edit, `0023:60` said "What a human approves is what merges" in its own
Consequences — a universal claim this task makes one of two, in an accepted record whose
Decision needed nothing but whose Consequences did.
Assumed: the task's own prepared Scope, written before the work started, listed every file that
would need touching.
Actually: a Scope list is a plan, and a plan written before reading the affected files can miss
one. The sweep this project keeps requiring after every rule change caught it here before a
verifier had to, this time.

### A code-span convention had to be inferred rather than found stated

The task's own contract, written before this work started, wrote the verifier's verdict as
`` `CONFIRMED` `` — code span, capitals. The first draft of the new rule text and decision
record wrote it as plain lowercase "confirmed", an ordinary adjective rather than the literal
token a verifier actually returns.
Assumed: either casing was a stylistic choice with no consequence.
Actually: this project renders `CONFIRMED`/`REFUTED`/`INCONCLUSIVE` as literal verdict values
everywhere a verifier report appears, and treating one as a code span while introducing the same
concept as prose elsewhere is the twin-stranding pattern in miniature — one true thing, stated
two ways. Standardized on the contract's own convention rather than picking a new one.

### The sweep missed a third statement, in the file it was editing

Root AGENTS.md's own Change workflow said "4. Wait for a human to approve it." — unconditional —
three lines below the bullet this task had just made conditional. The sweep after editing found
0023's Consequences; it did not re-read the rest of the file it had already touched.
Found by a verifier. Fixed: step 4 now states both paths, matching the bullet above it.
