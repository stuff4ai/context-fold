# Run tasks in parallel

## Status

Accepted. That worktrees are "this project's workflow, not part of the layer" is narrowed
by [0026](0026-map-what-is-under-the-agents-directory.md): the convention now ships as a
copied-once template, which is not the same as joining the layer. The rest stands.
[0032](0032-fold-worktrees-agents-md-into-the-byte-identical-set.md) makes
`worktrees/AGENTS.md` a shipped, checked managed contract rather than the unbound project file
described below.
[0037](0037-replace-task-index-with-frontmatter.md) removes the index conflict example and its
blocker-visibility claim; [0041](0041-define-governed-agent-sublayers.md) recognizes the
worktrees contract as a disposable-operation sublayer while leaving the checkouts project-owned;
section ownership and concurrent-task rules stand.

## Context

Every rule in the layer was written and exercised with one task running. Only `INDEX.md` was ever
described as contended — "one file that every concurrent task touches, so conflicts are normal" —
and nothing else acknowledged that a second task could exist.

That is about to stop being true here: work will be planned in one checkout while it is done in
another, by different agents at the same time.

Five things are unstated the moment a second task starts.

Nothing compares scope across active tasks, and the file is the wrong unit to compare anyway.
Four of the last five tasks edited `tasks/AGENTS.md`, almost always in different sections. A rule
forbidding two tasks from sharing a file would serialise work that can safely run at once.

Nothing lets a task say it is waiting for another. The four statuses in
[0006](0006-task-package-model.md) describe what a task *is*; none of them says "not yet,
because".

Contention is described for one file and not for the class. `decisions/README.md` has the same
shape as `INDEX.md` and no rule; `OPEN-QUESTIONS.md` is a different shape entirely, and the
difference is what decides how a conflict in it is resolved.

[0022](0022-route-findings-without-an-owning-task.md) routes a finding to the task whose work
produced it. With one task running that is a tautology. With three it is a judgement nobody is
asked to make.

And two branches can claim the same decision number, each passing the numbering check alone.

## Decision

Scope is declared by section, not only by file. Two tasks may hold the same file when they hold
different parts of it. Where they need the same section, one owns it and the other records that
in `## Out of scope`.

A task that cannot start yet carries `## Blocked by`, naming what it waits for and what it needs
from each. Its status stays `planned`. Blocked is not what a task is, it is what the task is
waiting for, and `0006`'s four values describe the first — so no fifth value is added.

Conflicts are resolved according to what kind of file conflicted. A *derived* file restates what
is true elsewhere and is rebuilt from its sources rather than merged; `INDEX.md` becomes the
example rather than the special case. An *authored* file says something no other file says and is
merged as prose. The test between them is what deleting the file would cost: a derived file can
be built again, an authored one is gone.

A finding belongs to the task whose work produced it, which is not always the task you are in.

None of that names a version control system, a decision record, or any artifact a project might
not have.

Two things are this project's own rather than the layer's. Parallel checkouts live in Git
worktrees under `.agents/worktrees/{task-slug}`, ignored by Git: they are checkouts, not context,
and deleting them all loses nothing. `.agents/worktrees/AGENTS.md` is the exception to that
ignore and says so in place, because the directory is reachable from the main checkout and an
agent that wanders into it would otherwise find a second copy of every record and task package
with nothing marking them as another branch's. And a decision number is provisional until
merge — `0000` already says a record on a branch is a proposal, so whichever branch merges first
keeps the number and the other renumbers. That is ordinary rather than a breach of "never
renumber", which governs records that have landed.

## Consequences

Two agents can work at once without a protocol between them. Nothing here requires them to
communicate; it requires each to read what the others have written down, which is what the task
package is for.

Section-level scope is only as good as the sections. It works on a file with stable headings and
fails on one without them, which makes the granularity of a document part of whether it can be
worked on in parallel.

`## Blocked by` is declared and not enforced. Nothing detects an unmet blocker, a stale one, or a
cycle. A dependency that is wrong is worse than none, because it stops work for a reason that no
longer holds.

Blockers are visible only inside task files. `INDEX.md` shows status and objective, so finding
what is blocked means opening each active task. That is affordable at three and not at thirty,
and adding a column is deferred until scanning is what actually fails.

The suite now asks Git what belongs to the repository rather than walking the tree against a
hardcoded list of directories to skip. Measured once with a probe worktree in place, the old
discovery found 183 Markdown files against the 92 that existed at that moment — a second copy of
every record and every archived task, read as though it were this one. The suite and the linter
now agree about what the repository contains, which they did not before.

That couples the checks to Git. They already ran only in a Git repository, and `0016` chose to
enforce conventions in CI, so the coupling is real but not new.

A tracked file inside a Git-ignored directory needs the two-line form — `.agents/worktrees/*`
and then `!.agents/worktrees/AGENTS.md`. A directory excluded outright is never descended into,
so a negation for a file inside it does not apply. That is easy to get wrong and silent when
wrong.

`.agents/worktrees/AGENTS.md` is a rule file inside `.agents/` that the distribution does not
ship and no check binds. `0018` already permits that — the layer is what was installed, and
`.agents/` is only where it lives — and the checks follow it: `installed_layer_files()` reads
`.agents/AGENTS.md` and `.agents/tasks/` and claims nothing else, and `PORTABLE` is an explicit
list of three. So the file is free to carry project detail, which is the point, and free to
drift, which nothing will catch.
