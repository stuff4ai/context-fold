# Adopting context-fold

How a repository takes on the agent layer. Five steps, by hand — there is no installer.

This works the same for an empty repository and one with years of history. What changes is
step 4, where an existing `AGENTS.md` is added to rather than created.

## What you are adding

```text
.agents/
├── AGENTS.md              copied
├── SOURCE.md              created — where this came from
└── tasks/
    ├── AGENTS.md          copied
    ├── INDEX.md           created empty
    ├── adopt-context-fold/    task zero
    └── archive/
        └── AGENTS.md      copied
```

Plus a pointer in the repository's root `AGENTS.md`.

Nothing else in the repository moves. The layer is additive, and removing it later is a normal
change.

## 1. Copy the rule files

Take these three from context-fold, preserving their paths:

```text
.agents/AGENTS.md
.agents/tasks/AGENTS.md
.agents/tasks/archive/AGENTS.md
```

Copy them unchanged. They are identical in every project using context-fold and carry no
project-specific paths, names, or decisions — that is what makes them replaceable when
context-fold changes.

If a rule in them does not fit your project, do not edit it. Record it as a problem in task zero.
An edited rule file stops being upgradable and starts being yours.

## 2. Record where they came from

There are no version tags, so the commit is the only provenance an installation has. Without it
there is no way to answer which context-fold you are running, or what changed since.

Get it from your clone of context-fold:

```sh
git -C /path/to/context-fold rev-parse HEAD
```

Or take the commit from the page you copied the files from.

Write `.agents/SOURCE.md`:

```markdown
# Source

The rule files under `.agents/` were copied from context-fold, unchanged.

- Origin: https://github.com/stuff4ai/context-fold
- Commit: 0000000000000000000000000000000000000000
- Copied: YYYY-MM-DD

Update this whenever the rule files are replaced. Nothing verifies it.
```

This is a fact about the installation, not about any task, so it does not live inside a task
package — task zero is archived when it finishes, and archived tasks are history rather than
current state.

context-fold itself has no `SOURCE.md`. It is the origin, not an installation.

## 3. Create the task index

`.agents/tasks/INDEX.md`, empty:

```markdown
# Tasks

Derived navigation view. Each task's `task.md` owns its canonical status — if this table
disagrees with a task file, the task file is right and this table needs repair.

## Active

None.

## Archive

None.
```

## 4. Point at the layer

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

## 5. Open task zero

The adoption is itself a task, and it is the first one. This mirrors how decision records begin —
the first record is the decision to use records.

Create `.agents/tasks/adopt-context-fold/` with `task.md`:

```markdown
# Adopt context-fold

## Status

active

## Objective

Establish the context-fold agent layer in this repository.

## Why

Work in this repository is organized as task packages so that context survives between
sessions and agents, and so that what is learned while working outlasts the working.

## Scope

- `.agents/` — the layer contract, the tasks rules, the index, the archive.
- The root `AGENTS.md` pointer.

## Out of scope

- Changing existing documentation, conventions, or workflow.
- Anything the layer does not require.

## Acceptance

1. The structure exists and the pointer resolves.
2. The layer satisfies the deletion test described in `.agents/AGENTS.md`.
3. The rule files are unmodified from the commit recorded in `.agents/SOURCE.md`.

## Problems
```

And `context.md`:

```markdown
# Context — adopt-context-fold

## Base state

Describe the repository as it is: what it contains, what conventions it already has, and where
its durable knowledge lives.

## Assumptions

## Open questions
```

Then work the task: finish the structure, satisfy the acceptance, log every friction under
`## Problems` while it happens, and archive it before the change is merged. The rules for all of
that are in `.agents/tasks/AGENTS.md`, which you now have.

## What this does not give you

**No customization.** The rules are what they are. If they do not fit, that is worth knowing —
record it as a problem rather than working around it quietly.

**No upgrade path.** Copying is the whole distribution story. `.agents/SOURCE.md` records what
you took, which is enough to work out what has changed since — but nothing tells you when that
happens, and nothing checks that the recorded commit is the one you actually copied.

**Nothing runs.** There is no command, no check, and no automation. The layer is Markdown and a
directory structure, maintained by hand.
