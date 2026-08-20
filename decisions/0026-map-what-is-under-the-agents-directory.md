# Map what is under the agents directory

## Status

Accepted. `templates/task/` is removed by [0029](0029-drop-the-task-template.md); the map and the
ownership rules stand for what remains.
[0032](0032-fold-worktrees-agents-md-into-the-byte-identical-set.md) narrows this record's
classification of `templates/worktrees/AGENTS.md` as copied-once-and-diverges — it now ships
byte-identical instead, while remaining, as this record already established, not part of the
layer merely by being shipped.
[0035](0035-manage-portable-rules-as-replaceable-blocks.md) narrows that whole-file identity to
the managed rule block; the map and ownership distinctions stand.
[0037](0037-replace-task-index-with-frontmatter.md) removes the task index from the installation
and distribution map.

## Context

`.agents/AGENTS.md` explains what the layer is, what belongs outside it, and not to duplicate
what already exists. Then it ends with one line of navigation: "Work is organized under `tasks/`.
Start there."

That was complete when `tasks/` was the only thing there. Three things are now, with three
owners. `tasks/` is the layer's and its rules ship with it. `skills/` belongs to whatever
installed a skill — this project's own `ctxfold-init` lands there, and an adoption run found an
installer had already written to it in a repository being adopted. `worktrees/` is parallel
checkouts, which [0025](0025-run-tasks-in-parallel.md) established.

An agent arriving at `.agents/` finds three directories, one pointer, and no statement of which
are safe to read as this project's current state. That is not hypothetical: adding worktrees
produced a measured failure where a checkout under `.agents/` read as a second copy of every
record and task package.

## Decision

`.agents/AGENTS.md` names each thing under `.agents/`, says who owns it in a sentence, and points
at the detailed rules where they exist. It is a map, not a table of contents: the useful part is
the owner, because that is what decides whether a file is this project's current state or a copy
of it.

They are not called three layers. [0018](0018-ship-a-distribution.md) separates the layer — what
was installed — from `.agents/`, which is only where it lives. Three defects this month came from
blurring that, including a rule that said `.agents/` is removable when the layer is. Three things
under one directory with three owners is what they are.

The `skills/` entry says the directory is not the layer's and answers to whatever put it there.
It does not describe what belongs in it or adopt the convention;
[0011](0011-keep-the-model-vendor-neutral.md) permits a vendor convention only as an adapter, and
this is not even that. Saying "not ours, and not a statement about this project" is the whole
content, and it is worth saying because the alternative is an agent reading someone else's
tooling as project truth.

The `worktrees/` entry is conditional — "if this project keeps any" — so it is true for a project
that keeps none.

`templates/worktrees/AGENTS.md` ships, copied once like `templates/task/` and `templates/INDEX.md`
rather than replaced wholesale like `templates/agents/`
([0021](0021-separate-what-upgrades-from-what-diverges.md)). Two things force this. The entry
point references the file, so an adopter needs one; and the `.gitignore` negation the procedure
writes names that exact path, so a negation with nothing behind it does nothing.

The procedure gains a step: ignore `.agents/worktrees/` and except that one file, creating
`.gitignore` if the repository has none and appending if it has one. That makes
[0017](0017-adoption-procedure.md)'s enumeration of what adoption copies and does incomplete, so
its Status is narrowed too.

This narrows `0025`, which called worktrees "this project's workflow, not part of the layer".
Shipping something is not the same as making it part of the layer — the distribution already
carries `INDEX.md` and `templates/task/`, which belong to the adopter the moment they land.

## Consequences

An agent can tell, from the first file it reads, which parts of `.agents/` are this project and
which are copies or other tools' business. That is the failure worktrees produced, closed at the
entry point rather than only at the door it came through.

The distribution now names Git, in three places and none of them upgradable.
`templates/worktrees/AGENTS.md` is copied once and belongs to the adopter, and gives the rule in
a form another system can follow — one checkout per task, named for the task. The procedure and
the skill both name `.gitignore`, and the procedure says what to do if the project uses
something else; neither named Git at all before this. The portable rules still name nothing. The
line this holds is that what upgrades must stay neutral, not that everything shipped must.

`## Final exact-head check` said "At the branch head", which named a version control system in a
file that carries none. Corrected. The section's own name keeps "head", because renaming it
ripples through three other records for a word that is not specific to any system.

An adopter who never runs two tasks at once now installs a directory and a file for a workflow
they do not use. The procedure says to skip both and say so, which trades a decision for the
adopter against a hazard for the ones who do.

Shipping a shape on one worked example is what produced `templates/task/`, which six adoption
runs later has injected non-content four different ways and is under review for removal. This is
the same bet with the same evidence base. It is taken because the failure it prevents was
measured rather than imagined, and recorded here so that the next person to weigh it knows the
bet was knowingly repeated.
