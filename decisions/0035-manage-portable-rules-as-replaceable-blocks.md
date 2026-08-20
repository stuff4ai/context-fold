# Manage portable rules as replaceable blocks

## Status

Accepted

## Context

The distribution owns four portable `AGENTS.md` files as whole files. That makes copying and
checking them exact, but it also makes any project-specific addition an unsupported fork. A repeat
adoption overwrites the whole file, so an adopter must choose between local guidance and receiving
later portable-rule changes safely.

The index already demonstrates that distribution-owned and installation-owned content need
different lifetimes. It is kept outside `templates/agents/` because replacing it would destroy
state. Moving each rule file to the copied-once side would preserve local edits but give up the
portable rules' update path entirely.

A file can instead carry both lifetimes when their boundary is explicit.
[Pilotfish](https://github.com/Nanako0129/pilotfish) provided an example of replacing one marked
Markdown block while preserving surrounding content, but its vendor-named markers would violate
this project's neutral portable model. The boundary here must describe the agent layer rather
than who distributed it.

## Decision

Each file under `templates/agents/` consists of exactly one managed rule block. It begins at byte
zero with a standalone `<!-- agent-layer:begin -->` line and ends with a standalone
`<!-- agent-layer:end -->` line and its terminating LF. The template ends there. The markers are
generic because the portable model names no vendor and a fork may maintain the same rules.

The whole portable document, including its title and a source-visible ownership warning in an
HTML comment, lives inside the block. Rendered Markdown shows only the operating rules, while
humans and agents editing the source can still see the update boundary. An installation may
append project-specific instructions after the end-marker LF.
Those instructions belong to the adopting project, must not contradict the portable rules, and
are not part of the layer's distribution. Conflicting overrides and finer-grained blocks are not
defined.

Fresh adoption still copies each template whole. A repeat run preflights every portable target
before changing any of them:

- a missing target can receive its template;
- a target with no line beginning with `<!-- agent-layer:` is a legacy whole-file installation
  and is replaced whole;
- a target with exactly one well-formed block at byte zero has only that block replaced, with
  every byte after its end-marker LF preserved; and
- any displaced, reversed, duplicated, unmatched, or malformed marker stops the entire update
  before any target is written.

After writing, the installed managed blocks must equal their templates byte for byte and every
recorded suffix must equal its preflight bytes. An explicit re-run is the update procedure.
Versioning, source provenance, discovery of upstream changes, changelogs, and recovery of edits to
legacy whole-owned files remain unbuilt.

This repository keeps two different dogfooding identities. `skills/ctxfold-init/` and
`.agents/skills/ctxfold-init/` remain whole-directory identical: one is the shipped skill and one
is its installation. The source template, installed-skill template, and active `.agents/` rule
file must instead expose the same managed block; the active file may have a project suffix.

This narrows [0005](0005-agents-layer-boundary.md)'s whole-file ownership,
[0011](0011-keep-the-model-vendor-neutral.md)'s whole-file identity,
[0016](0016-check-conventions-in-ci.md)'s whole-file portability check,
[0017](0017-adoption-procedure.md)'s unchanged-copy and no-update consequences,
[0018](0018-ship-a-distribution.md)'s byte-identical installation,
[0021](0021-separate-what-upgrades-from-what-diverges.md)'s claim that wholesale replacement is
always safe, [0026](0026-map-what-is-under-the-agents-directory.md)'s whole-file classification,
and [0032](0032-fold-worktrees-agents-md-into-the-byte-identical-set.md)'s whole-file identity and
overwrite behavior. Their underlying boundaries, neutrality, distribution, and file set stand.

## Consequences

An adopter can add local operating guidance and still update the portable rules without a manual
merge. The markers and ownership comment make the boundary visible in source to humans, agents,
and mechanical checks without adding update metadata to rendered instructions.

Updating is no longer a directory copy. The procedure must classify every target before writing,
preserve suffix bytes, and stop as one operation when any marker is ambiguous. It remains a
written agent procedure rather than a runtime updater, so checks can enforce the resulting shape
but cannot prove that every agent will follow the order.

The first marked release replaces an unmarked installation whole. That is the behavior the old
files already announced. A user who edited one despite the warning may lose those edits, and this
change deliberately does not build historical-template recognition to recover them.

Additive instructions can still create tension without literally contradicting a sentence. The
portable warning states the boundary, but semantic compatibility remains a review judgment.
