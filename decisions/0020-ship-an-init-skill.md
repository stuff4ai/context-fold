# Ship an init skill

## Status

Accepted. The instruction that the skill stop before archiving is narrowed by
[0023](0023-approve-the-final-state.md): it now stops before merging, with the task
finished. The rest stands.

## Context

Adoption was a document. Following it required having this repository beside the one being
adopted, which is exactly the situation a repository adopting context-fold is not in.

Skill installers solve the delivery problem: they copy a skill directory whole, subdirectories
included.

Seven installed third-party skills were examined in another repository. Every one carries a
`README.md` beside its `SKILL.md`. One also ships a `SECURITY.md` and a `scripts/` directory of
seven Python files, and its `SKILL.md` points at them as "adjacent to this SKILL.md". So
`SKILL.md` is what a runtime loads, and the rest of the directory is material its instructions
refer to — bundling what adoption needs is how skills already work, not a stretch of the format.

That decides the shape rather than merely permitting it. If the skill directory is what travels,
everything adoption needs must be inside it — including the procedure. A skill whose
instructions point at a document left behind in another repository is a skill that works only
where it was written.

[0011](0011-keep-the-model-vendor-neutral.md) allows an agent product's convention only as an
adapter over the canonical model, never as the model itself. A `SKILL.md` that contained the
procedure would make one vendor's format the definition of adoption.

## Decision

`skills/ctxfold-init/` is the unit of distribution. It contains `SKILL.md`, the procedure
`ADOPTING.md`, and `templates/`. The latter two moved there from the repository root; they are
not duplicated.

`ADOPTING.md` sits at the package root rather than under a `references/` subdirectory. That
matches what the examined skills do — their `README.md` and `SECURITY.md` are at the root, and
only executable code was nested. It also keeps the procedure at the same level as the file that
points at it, which is what a reader arriving at the directory needs.

`ADOPTING.md` remains what adoption is, and is readable by anyone. `SKILL.md` covers only what
the procedure leaves to the agent following it:

- Find the project's workflow in its root `AGENTS.md` and follow it. When the file says nothing
  about branching, commits, or review, make the changes and commit nothing, saying so — rather
  than inventing a process for a project that has not chosen one.
- Supply the judgment the procedure asks for: a pointer that does not rewrite a file the project
  owns, and a task zero base state describing the repository as it actually is.
- Stop before archiving and ask for approval. [0007](0007-archive-before-merge.md) makes
  approval authorize archival, so an agent that archives unasked has skipped the gate.

Checks enforce that the package survives being copied: `SKILL.md` declares a name matching its
directory, and every path referenced anywhere in the package resolves inside it.

## Consequences

A repository can adopt the layer without first obtaining this one, and adoption is still defined
by a document that owes nothing to any agent product.

Nothing binds `SKILL.md` to `ADOPTING.md`. The templates cannot drift from their installation
because a check compares them; the skill's instructions can contradict the procedure they wrap
and only a reader would notice.

The canonical procedure and distribution now sit inside an adapter's directory, which this
project's own neutrality argument would prefer they did not. The alternatives were duplicating
them or shipping a skill that cannot install itself.

A project not using skills gains nothing here. It still reads `ADOPTING.md`, now at a longer
path.

The format was taken from seven installed skills rather than from a specification, and all seven
came through one installer. What is conventional there may not be conventional elsewhere, and
the package would be wrong in a way nothing here detects.
