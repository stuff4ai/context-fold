# Declare who approves a task

## Status

planned

## Objective

Let a task declare that a fresh verifier's `CONFIRMED` verdict is sufficient to merge it, without
a human. Default to requiring a human when a task says nothing, and give an agent opening a task
on its own something to judge by when it chooses.

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
  applies. Confirm during the work whether `0023` needs anything; its language already speaks of
  "review" and "a reviewer" without naming a human, so it may need nothing.
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
