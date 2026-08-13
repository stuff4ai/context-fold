# Ship a distribution

## Status

Accepted

## Context

Adoption meant copying files out of this repository's `.agents/`. That directory is this
project's installation of context-fold, not context-fold itself, and nothing separated the two.
Copying one project's installation into another is not shipping — it is borrowing, and it makes
every local fact about this repository a potential export.

The cost showed up as two statements in a distributed file that were false in the first
repository they were tried against: a claim that everything under `.agents/` is the project's own
work, and a deletion test instructing the reader to remove the directory. In that repository
`.agents/skills/` held third-party skills installed by a tool and tracked in a lock file. The
claim was untrue and the test destructive.

Both were symptoms of the same thing. Without a distribution, the installation was the artifact,
and the artifact described itself as though it were alone in the directory — which it was, here,
and only here.

Dogfooding had the same weakness. "We use what we ship" was true only because there was one copy
serving as both, so nothing could detect it becoming false.

## Decision

context-fold ships `templates/`. `templates/agents/` installs to `.agents/`; `templates/task/` is
the shape of a task package.

This repository installs itself from those templates. `.agents/` here is one installation, no
different in kind from any other, and its rule files are byte-identical to the shipped ones.

A check enforces that identity. Editing an installed rule file fails it, and so does changing the
distribution without reinstalling. `INDEX.md` is excluded: it ships empty and becomes instance
data immediately.

Ownership follows from this rather than being asserted. The templates define exactly what an
installation contains, so the layer is what was installed plus what working there produced.
`.agents/` is where it lives, not what it is; other tools write there, their files are not part
of the layer, and the deletion test is scoped to the layer.

The shipped files name nothing that ships them. They describe the layer, and a set of rules that
names its vendor is wrong for anyone who forks and maintains them — and was already false in one
place here, where a rule said its reasoning lived elsewhere while sitting in the repository that
holds it. Where an installation came from, and which version it is, is metadata; that is not
built yet and does not belong in the rules. The portability check enforces the exclusion.

This narrows [0005](0005-agents-layer-boundary.md), which treats the directory and the layer as
the same thing and claims everything under it. The boundary that record draws is unchanged — only
what falls inside it.

## Consequences

Dogfooding is verifiable. The claim that this project uses what it distributes now fails CI when
it stops being true, rather than being a sentence nobody can check.

The distributed rules describe an installation rather than this repository, so a statement that
is only true here cannot silently ship.

Adopters still drift freely. The check binds this repository alone; a copy elsewhere can be
edited, and nothing detects it. The instruction not to edit is a request.

Two copies of the rule files exist here, and someone editing both in the same change defeats the
check. It catches carelessness, not intent.

`.agents/` remains shared with whatever else writes there, and there is no mechanism to
coordinate. The layer stays out of the way by describing only itself, which is a convention, not
an enforcement.
