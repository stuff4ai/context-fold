# Drop the task template

## Status

Accepted. Narrows [0018](0018-ship-a-distribution.md),
[0021](0021-separate-what-upgrades-from-what-diverges.md), and
[0026](0026-map-what-is-under-the-agents-directory.md), which describe `templates/task/` as part
of what ships.

## Context

`templates/task/` shipped a `task.md`/`context.md` skeleton to copy when starting a task package.
It was added when the distribution was separated from the installation
([0018](0018-ship-a-distribution.md)), on the assumption that a skeleton is how the shape of a
task package is transmitted to an adopter.

That assumption had a competitor from the start: `.agents/tasks/AGENTS.md` lists the required
sections, and `ADOPTING.md` describes task zero's content in prose. Both ship with every
installation and are read before or during the first task, whether or not the template is
opened.

Seven foreign adoption runs measured the two against each other. Five wrote task packages —
three from scratch, two by copying the template — and all five carried every required section:
the rules and the procedure were sufficient on their own. The template's one distinctive effect
was a defect: two runs kept an example line, written in the voice of a real entry, that named a
file that happened to exist in their repository. A single braced placeholder fixed the specific
line; the fix went untested, because the next run wrote its package from scratch.

Two further runs, both adopting `etu-forms`, tested it directly. The first used the template as
intended and finished a task package carrying four things that were never meant to be content:
the instructional paragraph under `## References`, the one under `## Open questions`, an
`## Assumptions` heading left in place with nothing under it, and a duplicated `## Problems`
heading holding the placeholder beside the real entry. The second, adopting the same repository,
found and repaired the fourth of these without prompting; the first three were still there when
it archived.

Across every measured use, the template produced a defect — an instruction or a placeholder
surviving into content that was supposed to describe real work — and never once supplied a
section the rules and the procedure would otherwise have missed. It is not a case of a rough
tool that helps more often than it hurts; nothing in seven runs shows it helping at all.

## Decision

`templates/task/` is removed from the distribution — not fixed, not made an example instead of a
skeleton. The shape of a task package continues to travel exactly as it did whenever the template
went unused: through `.agents/tasks/AGENTS.md`'s list of required sections and `ADOPTING.md`'s
description of task zero.

`ADOPTING.md` no longer tells an adopter to copy the template for task zero. It tells them to
create `task.md` and `context.md` directly, using the sections `.agents/tasks/AGENTS.md`
requires, and gives task zero's content the same way it already did.

A fixed template — placeholders instead of instructional prose, no empty optional headings — was
considered and rejected. One fix of exactly that shape, a braced placeholder replacing a
realistic-looking example line, was already applied before this decision and went unexercised
until `etu-forms` — where none of the four defects found was that line reappearing. What
`etu-forms` found instead was a category the earlier fix never touched: instructional prose left
in place, and headings left empty or duplicated. A skeleton's failure mode is that whatever sits
in a section survives if the author does not notice it is not theirs; fixing one instance of that
says nothing about the categories it has not yet been tried against, and two rounds of evidence
are not enough to show a fixed template would stop producing new ones.

## Consequences

Adopting the layer no longer offers a file to copy for a new task package, in exchange for
removing the only mechanism in the distribution that has been measured to leave placeholder text
in a finished package. An adopter writes `task.md` and `context.md` from the description in
`ADOPTING.md` and the section list in `.agents/tasks/AGENTS.md`, the same as every task package
after task zero already does.

The identity check between `skills/ctxfold-init/templates/` and its installed copy loses two
files on each side; nothing else about it changes; `templates/task/` was never part of the
byte-identical set `templates/agents/` requires.

[0018](0018-ship-a-distribution.md), [0021](0021-separate-what-upgrades-from-what-diverges.md),
and [0026](0026-map-what-is-under-the-agents-directory.md) each describe `templates/task/` as
part of what the distribution ships. That description is now false; the decisions that made it —
separating the distribution from the installation, and separating what upgrades from what
diverges — stand unchanged.
