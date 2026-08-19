# Context — decide-whether-the-task-template-earns-its-place

## Base state

`skills/ctxfold-init/templates/task/` holds `task.md` and `context.md`, copied into a new task
package and filled in. It was added when the distribution was separated from the installation.

The first five adoption runs are recorded in
`.agents/tasks/archive/2026-08-17-0116-add-init-skill/task.md`, under the entries about the
template being optional and about its example lines surviving as content. Two more are recorded
below.

## References

- `.agents/tasks/archive/2026-08-17-0116-add-init-skill/task.md` — the five runs and both
  findings.
- `skills/ctxfold-init/ADOPTING.md` — describes task zero's content, which is one of the two
  places already carrying the shape.
- `.agents/tasks/AGENTS.md` — lists the required sections, which is the other.
- `decisions/0018-ship-a-distribution.md` — what is shipped and why.

## Evidence from adoption of etu-forms

Two runs adopting the `etu-forms` monorepo. The artifact is its archived task zero, in an
untracked worktree on one workstation — so it is evidence that cannot be cited durably, and what
matters is reproduced here. Template text found in the finished package:

- `## References` — "Paths from the repository root, in code spans — not links. This package
  moves when it is archived…", instruction to the author, kept as content.
- `## Open questions` — "Questions local to this task. Anything that will outlive it belongs in
  the project layer…", the same.
- `## Assumptions` — heading retained with an empty body, because the template ships it empty and
  nothing says to delete an unused optional section.
- `## Problems` — duplicated, the placeholder surviving beside the real entry. Found and
  repaired by the second run without prompting, so unlike the three above it is no longer in the
  artifact; the repair is what records it.

This is a different failure from the one already recorded. The earlier runs kept example *lines*
written in the voice of content; these kept the *instructions*.

## Assumptions

- The runs are representative of how agents approach a task package. Two models through two
  installers now, which is better than the original five allowed, but still narrow.

## Open questions

Whether "used half the time" argues for removing the template or for making it easier to reach.
Both readings fit the evidence.
