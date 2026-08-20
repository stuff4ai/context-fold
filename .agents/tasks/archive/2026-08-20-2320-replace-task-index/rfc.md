---
status: resolved
---

# Replace the task index with canonical frontmatter

## Proposal

Make `task.md` self-describing through strict frontmatter and remove `INDEX.md`. Agents discover
work by enumerating task directories and reading their metadata. Rewrite the existing archive in
one repository migration and support only the new format.

The task-query skill is separate work. It may later bundle a private helper for agents; this task
does not expose a human command or establish that skill's output contract.

## Resolution

Use exactly two ordered frontmatter keys, `status` and a folded `objective`; reject legacy heading
metadata. Migrate all task packages atomically, remove the repository and template indexes, and
permit accepted archives to change during v0 only through an explicit verified schema-migration
task. Start concurrently from current `main`, defer PR #39's shared sections, and integrate its
final state before review.
