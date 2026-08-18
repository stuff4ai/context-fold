# Adopting context-fold

How a repository takes on the agent layer. Three steps, by hand — there is no installer.

This works the same for an empty repository and one with years of history. What changes is
the pointer step, where an existing `AGENTS.md` is added to rather than created.

## What you are adding

`templates/`, beside this file, is what gets installed. Adoption is installing it. Everything you
need is in this directory — nothing has to be fetched.

```text
templates/agents/   →   .agents/
templates/task/     →   the shape of a task package
```

Plus a pointer in the repository's root `AGENTS.md`.

Nothing else in the repository moves. `.agents/` may already hold other tools' files; the layer
sits alongside them and does not claim the directory. Removing the layer later is a normal
change.

## If the layer is already there

`.agents/AGENTS.md` existing means this repository has adopted before. The steps below assume
nothing is installed, and following them as written destroys work: they overwrite the index,
add the pointer a second time, and open an adoption task for an adoption that already happened.

Do this instead:

- Copy only the `AGENTS.md` files from `templates/agents/`. Leave `INDEX.md` and everything under
  `tasks/` alone — those are this repository's, not the distribution's.
- Leave `.agents/worktrees/AGENTS.md` alone if it is there. It is the repository's copy and may
  have been edited on purpose. If it is missing, the repository adopted before this file existed:
  offer it and the `.gitignore` lines rather than adding them unasked.
- Leave the root `AGENTS.md` alone if it already points at the layer.
- Do not open task zero.

If nothing changed, say so. A repository already holding the current rules is the expected
result, not a failure.

## 1. Install the layer

Copy `templates/agents/` from this directory to `.agents/` in your repository, preserving the
structure inside it.

```text
templates/agents/AGENTS.md               →  .agents/AGENTS.md
templates/agents/tasks/AGENTS.md         →  .agents/tasks/AGENTS.md
templates/agents/tasks/archive/AGENTS.md →  .agents/tasks/archive/AGENTS.md
templates/INDEX.md                       →  .agents/tasks/INDEX.md
templates/worktrees/AGENTS.md            →  .agents/worktrees/AGENTS.md
```

`templates/agents/` is separate from the other two on purpose. Everything in `templates/agents/`
must stay byte-identical to its template for as long as it is installed. `INDEX.md` stops
matching the moment you record your first task, and `worktrees/AGENTS.md` describes a workflow
this project may not share — both are yours once copied.

## 2. Ignore the worktrees directory

`.agents/worktrees/` holds parallel checkouts, which must not be committed — except the file you
just copied there, which explains what they are. Add both lines to `.gitignore`, creating it if
the repository has none:

```text
.agents/worktrees/*
!.agents/worktrees/AGENTS.md
```

Both lines are needed, in that order. A directory excluded outright is never descended into, so
`.agents/worktrees/` alone would ignore the file as well and the exception would never apply.

Append to an existing `.gitignore` rather than rewriting it. If the repository uses something
other than Git, do the equivalent, and say what you did.

If this project will never keep more than one checkout at a time, skip the directory and its
file entirely and say so — nothing else depends on them.

**Copy the files. Do not retype them.** Use a file copy — `cp`, or whatever your tools call it —
and then confirm every installed file is byte-for-byte identical to its template. Reproducing
the contents from what you have read produces files that look right and differ: a rewrapped
line, a dropped paragraph, a missing file. Those differences are invisible on reading and break
every future comparison against the distribution.

The `AGENTS.md` files are identical in every installation and carry no project-specific paths,
names, or decisions — that is what makes them replaceable when the rules change, and that
property survives only if the copy is exact.

`INDEX.md` ships empty and becomes yours as you work. Copy it once, on adoption, and never
again — replacing the rule files later means copying `templates/agents/` over `.agents/`, which
leaves your index alone.

If a rule does not fit your project, do not edit it. Record it as a problem in task zero. An
edited rule file stops being upgradable and starts being yours.

## 3. Point at the layer

The root `AGENTS.md` is your project's file. context-fold adds a pointer to it and nothing else.

If the file already exists, add a section:

```markdown
## Agent layer

Agent operating context lives in `.agents/` — how work is organized, tracked, and finished
here.

Read [`.agents/AGENTS.md`](.agents/AGENTS.md) before starting work.
```

If the repository has no `AGENTS.md`, create one. It belongs to the project, so it should say
what the project is and how to work on it; the section above is the only part context-fold
contributes.

## 4. Open task zero

The adoption is itself a task, and it is the first one. This mirrors how decision records begin —
the first record is the decision to use records.

Copy `templates/task/` to `.agents/tasks/adopt-context-fold/` and fill it in. The skeleton is
generic; for task zero the content is:

**`task.md`** — Objective: establish the context-fold agent layer in this repository. Why: work
here is organized as task packages so context survives between sessions and agents, and so what
is learned while working outlasts the working. Scope: the layer and the root `AGENTS.md` pointer.
Out of scope: changing existing documentation, conventions, or workflow.

Acceptance:

1. The layer is installed and the pointer resolves.
2. It satisfies the deletion test described in `.agents/AGENTS.md`.
3. The rule files are unmodified — nothing in them was adjusted to fit this project.

**`context.md`** — Base state: the repository as it is. What it contains, what conventions it
already has, where its durable knowledge lives, and what else already writes to `.agents/`.

Then work the task: finish the structure, satisfy the acceptance, and log every friction under
`## Problems` while it happens. Then finish it — Outcome, fold, archive, index, final check —
and stop there to ask for approval. Approval authorizes the merge, and what it is given for is
the finished state rather than a promise to file the paperwork later. The rules for all of that
are in `.agents/tasks/AGENTS.md`, which you now have.

## What this does not give you

**No customization.** The rules are what they are. If they do not fit, that is worth knowing —
record it as a problem rather than working around it quietly.

**No migration.** This installs a layer; it does not convert one. If `.agents/` already holds a
task system of its own — packages, an archive, another index — leave it exactly where it is.
Describe it in task zero's base state, note it under `## Problems`, and let the two coexist.
Deciding what to do about it is a later decision for that project, and not something adoption
should make on its behalf.

**No provenance, and no upgrade path.** Copying is the whole distribution story. Nothing records
which version you took, nothing tells you when the rule files change upstream, and there is no
procedure for replacing them. Note the source commit in your adoption commit message if you
want it later.

**Nothing runs.** There is no command, no check, and no automation. The layer is Markdown and a
directory structure, maintained by hand.
