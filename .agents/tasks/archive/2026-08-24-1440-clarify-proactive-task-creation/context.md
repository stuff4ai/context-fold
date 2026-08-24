# Context — clarify-proactive-task-creation

## References

- `decisions/0022-route-findings-without-an-owning-task.md` — the rule this task revisits. Its
  Decision text is what a resolution must either restate explicitly or deliberately narrow; its
  Consequences ("Planned tasks still accumulate, and nothing prompts anyone to start or cancel
  one. Narrowing what becomes a task slows that; it does not stop it.") already accept the cost a
  wider trigger would make larger.
- `.agents/tasks/AGENTS.md`'s "When a finding has no owning task" section — the portable rule as
  currently installed, and the exact text any clarification edits.
- `.agents/tasks/archive/2026-08-18-1518-route-findings-without-an-owning-task/task.md` — the
  task that produced `0022`. Its `## Problems` log records a rejected earlier design in detail
  ("The fix routed project knowledge into the layer the deletion test forbids") that any
  bar-widening proposal here must not recreate without saying why it's different.
- `.agents/tasks/archive/2026-08-21-1816-add-ctxfold-tasks-skill/` and
  `.agents/tasks/guard-skill-portability/` — the concrete incident: a finding surfaced while
  working `add-ctxfold-tasks-skill`, and the agent opened `guard-skill-portability` only after
  being explicitly asked, despite `0022`'s rule reading as standing authorization already.

## Discussed direction

- The user proposed a broader rule permitting an agent to open a task for "ideas, problems, and
  other things to implement or think about later" while working another task.
- Discussion separated two distinct questions bundled in that proposal: (a) may an agent act on
  `0022`'s existing trigger without being asked first, and (b) should the trigger itself widen to
  catch ideas that do not yet clearly meet it.
- The user resolved (a): an agent can be proactive. (b) is still open going into the RFC.

## Not relevant

- Whether a planned task can store durable knowledge on its own — `0022` already settled that: no.
