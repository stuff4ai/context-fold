# Fold worktrees/AGENTS.md into the byte-identical set

## Status

Accepted. Narrows [0021](0021-separate-what-upgrades-from-what-diverges.md),
[0026](0026-map-what-is-under-the-agents-directory.md), and
[0017](0017-adoption-procedure.md)'s narrowing of `0026`.

## Context

[0021](0021-separate-what-upgrades-from-what-diverges.md) put exactly three files under
`templates/agents/` — the ones that "must never change" — because a fourth file that diverges by
design, mixed into the same directory, had already produced two measured failures: reinstalling
silently discarded a populated `INDEX.md`, and comparing an installation against its template
reported a correctly-filled index as broken. Its Consequences section named the risk directly:
"putting a divergent file under `templates/agents/` would reintroduce exactly this. Nothing
prevents it."

[0026](0026-map-what-is-under-the-agents-directory.md) later shipped `templates/worktrees/AGENTS.md`
and classified it into the diverges group by the same reasoning, "copied once like
`templates/task/` and `templates/INDEX.md` rather than replaced wholesale like
`templates/agents/`." The stated justification was that the file describes a workflow — worktree
and VCS conventions — a project might need to edit to fit itself.

That justification hasn't held up against this project's own history. `worktrees/AGENTS.md`'s
content has never diverged: it already generalizes past Git ("Another version control system will
have its own spelling") and carries no context-fold-specific detail. The one edit it has received
in this project — a paragraph documenting how to merge a pull request from inside a task worktree
without conflicting with `main` at the repository root, added this session — is exactly the kind
of generic operational advice the byte-identical files already carry, not a project-specific
customization. Working across two tasks this same session produced real, repeated confusion over
whether the shipped template needed to track that edit, because the split gives no mechanical
signal either way.

This is the same shape as [0029](0029-drop-the-task-template.md): a file shipped on the
expectation of future divergence that, once measured against actual use, never diverged. `0029`
removed `templates/task/` outright because it actively produced defects; this file has produced
none, so the fix here is to fold it into the safe path rather than remove it.

## Decision

`templates/agents/` gains a fourth byte-identical file: `templates/agents/worktrees/AGENTS.md`,
installing to `.agents/worktrees/AGENTS.md`. It joins `PORTABLE` and the mechanical checks the
other three already have — `test_installation_matches_the_distribution`,
`test_distribution_is_complete`, `test_portable_rules_carry_no_project_detail`.

`templates/INDEX.md` does not move. It is not in the same position: its divergence isn't a
possibility to weigh, it's the file's entire purpose, true on day one and every day after. Nothing
in this record's reasoning — "this file's content has stayed generic in practice" — applies to a
live index of a project's actual tasks.

[0021](0021-separate-what-upgrades-from-what-diverges.md)'s caution stands and is knowingly
overridden for this one file, not argued away: adding a file to `templates/agents/` that later
turns out to need per-project divergence would reintroduce the exact hazard `0021` fixed, and
nothing about this change makes that structurally impossible again. The claim here is narrower —
that `worktrees/AGENTS.md` is not that file, based on the evidence above — not that the underlying
risk stopped applying. If a real adopter needs to edit it, the fix is to move it back out to a
one-time seed, the shape `0026` originally chose, not to weaken the byte-identical check for
everyone to accommodate one case.

`.agents/AGENTS.md`'s "What you will find under `.agents/`" section is updated to say so: the
`worktrees/` entry's `AGENTS.md` ships byte-identical now, while the directory and workflow it
describes remain, as before, not part of the layer — shipping something byte-identical is not the
same as making it part of the layer, the same distinction `0026` already drew for `INDEX.md` and
`templates/task/`.

## Consequences

Two of the confusions this session hit — whether the shipped template needed the `gh pr merge`
paragraph added to `.agents/worktrees/AGENTS.md`, asked twice — cannot recur: the mechanical check
now says so, the same way it already does for the other three files.

`installed_layer_files()` (`tests/test_conventions.py`) cannot reuse the `tasks/`-style recursive
`AGENTS.md` glob for `worktrees/`: that directory also holds live git worktree checkouts, each a
full nested copy of this repository with its own nested `AGENTS.md` files, which a recursive glob
would wrongly sweep in whenever a task worktree happens to be checked out — routinely, in this
project's own normal workflow. It checks for the single file directly instead.

Re-adoption behavior changes: `ADOPTING.md`'s "If the layer is already there" section previously
said to leave `.agents/worktrees/AGENTS.md` alone, since it might carry a deliberate edit. It now
says to overwrite it like the other three files. Any adopter that customized this file under the
old rule would lose that customization on its next reinstall. Context-fold is its own only known
adopter today, so the practical blast radius is believed to be zero, but the rule itself changed
and this is stated rather than left implicit.
