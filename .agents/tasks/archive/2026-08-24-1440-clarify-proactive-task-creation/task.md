---
status: completed
objective: >-
  Decide whether the finding-triage rule already authorizes an agent to open a planned task
  proactively, mid-task, without being asked first — and if not, say so explicitly without
  loosening what counts as a triggering finding.
---

# Clarify proactive task creation

## Why

`decisions/0022-route-findings-without-an-owning-task.md` already reads as standing
authorization: "Does the finding call for investigation, a decision, or a change? Then a
`planned` task is opened for that work." Nothing in that sentence, or in its installed copy in
`.agents/tasks/AGENTS.md`, conditions opening the task on being asked first — only the resulting
change's approval and merge require a human, exactly as `## Who approves` already separates
authoring from accepting.

In practice, an agent working the `add-ctxfold-tasks-skill` task surfaced a finding that clearly
met that bar (a shipped skill leaking this repository's own decision numbers and test paths) and
still waited to be told to open `guard-skill-portability`, rather than opening it on the rule's
own authority. Whether that was the rule being unclear or the agent reading a clear rule too
cautiously matters, because only one of those needs a text change.

Separately, the request that prompted this reaches slightly further than `0022`'s trigger: "you
can create tasks when you are working with another task because you can find something like
ideas, problems and other what we should implement or think later." `0022` already tested a
version of "capture everything that might matter later" and rejected it — routing every
observation into a planned task "puts durable project knowledge inside the layer, which the
deletion test forbids," and "makes every observation pretend to be work," producing "a backlog of
tasks nobody intends to start," named there as a real, accepted cost of the alternative it chose
instead. Whether "ideas ... to think about later" is the same shape as "calls for investigation,
a decision, or a change," or a wider category that risks recreating the rejected design, is the
second thing this task needs to settle.

## Scope

- `.agents/tasks/AGENTS.md`'s "When a finding has no owning task" section, and its shipped and
  installed copies, if the resolution adds a clarifying sentence.
- `decisions/0022-route-findings-without-an-owning-task.md` — Status only, if narrowed.
- A new decision record, if the resolution changes or clarifies the portable rule.
- This task's own `rfc.md`, including the still-open question of whether the triggering bar
  itself — not just who may act on it — should extend to ideas that do not yet clearly call for
  investigation, a decision, or a change.

## Out of scope

- Reopening whether a `planned` task may hold durable knowledge on its own. `decisions/0022`
  tested and rejected that, explicitly.
- `context.md`'s task-local "Open questions" section or `OPEN-QUESTIONS.md`'s project-level
  scope; neither is what this task is about.
- `.agents/skills/` sublayer or ownership questions — `define-agent-sublayer-model` and
  `formalize-skills-sublayer` own those.

## Acceptance

1. A resolved RFC states whether the finding-triage rule already authorizes proactive, unasked
   task creation once a finding meets its existing bar, and whether that needs to be said
   explicitly in the portable rule text.
2. The RFC also resolves, or explicitly defers with stated reasoning, whether the triggering bar
   itself should extend to ideas that do not yet clear it — weighed directly against the
   "everything becomes a task" alternative `decisions/0022` already tested and named as a real
   cost.
3. If the portable rule text changes, its shipped and installed copies stay in parity per the
   existing checks, and a decision record captures what changed and why.
4. If the resolution is "the rule already covers this, no text changes needed," the RFC and this
   task's Outcome say so plainly rather than manufacturing a change to justify the task.

## Outcome

`rfc.md` resolves both items. Item 1: `0022`'s triage rule already authorized opening a `planned`
task, or adding to a project artifact, without being asked first — only the resulting change's
review and approval need a human. `.agents/tasks/AGENTS.md` now says this explicitly, next to the
two triage questions. Item 2: the trigger does not widen. "Calls for investigation, a decision, or
a change" already reaches as far as any idea worth keeping should reach; there is no idea worth
keeping that fails to clear it. What was actually missing was a place for the moment before
judgment, not a wider trigger — so `context.md` gains an optional Ideas section, for a finding
noticed in passing but not yet weighed against the triage rule, that expires at archival like any
other unfilled optional heading.

The clarifying sentence and the new Ideas section are in the portable managed block of
`.agents/tasks/AGENTS.md`, and byte-identical in `skills/ctxfold-init/templates/agents/tasks/
AGENTS.md` and its mirrored copy at `.agents/skills/ctxfold-init/templates/agents/tasks/
AGENTS.md`; the active file's project-specific suffix ("Handing work to another agent stack") is
untouched. `tests/test_conventions.py`'s `CONTEXT_OPTIONAL_HEADINGS` includes `Ideas`, so an empty
one at archival is caught the same way an empty `Open questions` already is.
`decisions/0039-confirm-proactive-task-creation-and-hold-unjudged-findings.md` records the
decision and is indexed in `decisions/README.md`.

The full suite (`pytest tests/`, 605 tests) and `pymarkdown --config .pymarkdown.json scan -r
--respect-gitignore .` pass at the finished state.

## Approval

Human.
