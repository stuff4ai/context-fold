# Context — guard-against-leftover-scaffolding

## Base state

`tests/test_conventions.py::test_task_package_has_required_files` checks that a task package
has `task.md` and `context.md`. Nothing checks what is inside a section beyond that a decision
record has the four required headings (`test_record_has_required_sections`) — no equivalent
exists for task packages, and neither check reads section bodies for leftover scaffolding.

## References

- `decisions/0029-drop-the-task-template.md` — removed `templates/task/`, the mechanism that
  produced the defects this task is about; explains why removal alone does not close every path
  to the same failure.
- `.agents/tasks/archive/2026-08-19-1250-decide-whether-the-task-template-earns-its-place/context.md`
  — the four `etu-forms` defects, the concrete cases a check would need to catch: an
  instructional paragraph kept under `## References`, one kept under `## Open questions`, an
  `## Assumptions` heading left empty, and a duplicated `## Problems` heading.
- `tests/test_conventions.py` — `test_task_package_has_required_files`, the check this task
  would extend or sit beside.
- `.agents/tasks/AGENTS.md` — lists the sections a task package requires; the current source of
  truth for what belongs in each.

## Open questions

Whether a check like this can be precise enough to be worth having. `## Assumptions` shipping
empty was correct by the old template's own design — nothing marks an unfilled optional section
as wrong on its own, only as wrong when nothing was ever going to fill it. A check would need to
tell "declared and left for later" apart from "copied and never noticed," which the four
`etu-forms` defects do not obviously give a general rule for.
