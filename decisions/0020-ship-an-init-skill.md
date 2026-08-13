# Ship an init skill

## Status

Accepted

## Context

Adoption was a document. Following it required having this repository beside the one being
adopted, which is exactly the situation a repository adopting context-fold is not in.

Skill installers solve the delivery problem: they copy a skill directory whole, subdirectories
included. An installed third-party skill was found carrying seven scripts in a subdirectory, so
a skill that bundles what adoption needs is installable by tooling that already exists.

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

The frontmatter convention was taken from installed skills rather than a specification, and one
installer was examined. If either differs elsewhere, the package is wrong in a way nothing here
detects.
