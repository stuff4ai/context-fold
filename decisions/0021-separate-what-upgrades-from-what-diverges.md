# Separate what upgrades from what diverges

## Status

Accepted. `templates/task/` is removed by [0029](0029-drop-the-task-template.md); the split
between what upgrades and what diverges stands for what remains.

## Context

`templates/agents/` held four files with two incompatible lifetimes. Three are rule files that
must stay byte-identical to their template for as long as they are installed. The fourth,
`INDEX.md`, ships empty and stops matching the moment a task is recorded.

Nothing in the layout said so. The identity check knew — it excluded `INDEX.md` by name — and
`ADOPTING.md` warned about it in prose. Both are instructions rather than structure, and both
were followed by whoever wrote them and nobody else.

It cost twice. Verifying that reinstalling was a no-op replaced a populated index with the empty
template, discarding eleven rows; the command reported nothing and the result was a valid, empty
index. Later, an agent adopting the layer in another repository compared every installed file
against its template, including the index it had just correctly filled in, and got a failure that
described nothing wrong.

Two failures in opposite directions — one destroying data, one inventing a defect — from the same
cause: a directory whose contents look uniform and are not.

## Decision

`templates/agents/` contains only what must never change: the three `AGENTS.md` files. Everything
copied once and then owned by the installation lives outside it — `templates/INDEX.md` and
`templates/task/`.

The rule follows from the layout rather than being stated alongside it. Copying
`templates/agents/` over `.agents/` is always safe, at adoption and at every upgrade, because
there is nothing in it that an installation is meant to have changed.

The identity check loses its exclusion: everything under `templates/agents/` is compared, with no
file needing special treatment.

Shipped rule files also stop using relative links. A rule file is written in one directory and
read from another, so `[INDEX.md](INDEX.md)` resolved in an installation and dangled in the
distribution. Named in a code span, it is correct in both — the same reason task packages
reference project artifacts by path rather than by link.

## Consequences

The hazard is removed rather than documented. Reinstalling cannot clobber an index, and verifying
an installation cannot produce a false failure, because neither operation encounters a file whose
divergence is intended.

`templates/` is less tidy to look at: two entries beside a directory rather than one directory
holding everything. That is the point — the shape now carries information the uniform version hid.

Anything added to the distribution has to be placed deliberately, and putting a divergent file
under `templates/agents/` would reintroduce exactly this. Nothing prevents it.

An installation made before this change has `INDEX.md` in the same place — the target path did not
move, only its source did — so nothing needs migrating.
