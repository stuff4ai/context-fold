<!-- agent-layer:begin -->

<!--
Managed rule block. Updates replace everything between the agent-layer markers.
Do not edit this block. Add only non-conflicting project instructions after the end marker.
-->

# AGENTS.md — archive

Completed and cancelled tasks, flat, one directory each:
`{YYYY-MM-DD-HHMM}-{slug}/`, timed to the minute the task left active state.

Both outcomes live here together. The final state is recorded in each task's own `task.md` as
`completed` or `cancelled` — the directory does not encode it.

## These are historical records

Archived tasks describe how something came to be, not how things are now. They are not
current project truth, and they are not a place to look up how the project works — that
belongs in the project's own documentation and decision records.

Archived packages are immutable once the change is accepted. Do not edit them to reflect later
changes. If
something in an archived task is wrong or has been superseded, the correction belongs in the
project layer or in a new task.

During v0, a repository-wide task-schema migration is the one exception. It must be an explicit
task whose declared scope names the accepted archive, preserves the meaning of migrated metadata
and every unrelated byte, and verifies the complete corpus before review. Never rewrite an
accepted package opportunistically while doing other work.

## Reading them

Useful for: why a decision was made the way it was, what was tried and rejected, what went
wrong and how it was handled.

The `## Problems` sections are the reason the archive is worth keeping. A problem that recurs
across several archived tasks is a signal that something in the project layer or in these
operating rules needs to change.
<!-- agent-layer:end -->
