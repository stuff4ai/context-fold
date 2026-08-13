# Write the adoption procedure

## Status

active

## Objective

Describe how another repository adopts context-fold, well enough that following the description
is the test rather than the improvisation around it.

## Why

Ten tasks have run here and nowhere else. Every rule was written by the same process that tested
it, against documentation-shaped work, by one author, never concurrently. The next evidence worth
having comes from a repository with code, tests, CI, and conventions of its own.

Nothing describes how it gets there. Copying three files and improvising the rest would measure
the improvisation. A written procedure turns installation into an experiment: every point where
it is vague, wrong, or silent is evidence.

## Scope

- `ADOPTING.md` — the canonical procedure, with the snippets an adopter needs inline.
- `decisions/0017-adoption-procedure.md` and the index row.
- `OPEN-QUESTIONS.md` — resolve initialization; keep customization and upgrades open.

## Out of scope

- The `/ctxfold-init` skill. Separate task, and an adapter over this.
- Version tags, upgrade paths, or any way for an installation to learn it is stale.
- Customization.
- Adopting into a live repository. This makes it possible and tests it in a scratch copy.

## Acceptance

1. `ADOPTING.md` is followable by a human or an agent with no access to this conversation, and
   names the commit as provenance.
2. It handles both a repository with an existing root `AGENTS.md` and one without.
3. Task zero is the adoption itself, and the record says why discovery-as-task-zero is rejected.
4. A dry run against a scratch copy of a real repository — one with code, CI, an existing root
   `AGENTS.md`, and an existing `.agents/skills/` — completes using only the procedure and the
   copied rule files, with no reference back to this repository.
5. That dry run produces at least one problem entry. A run with no findings means the procedure
   was tested against the assumptions that wrote it.

## Problems

### The layer claims a directory it does not own

`.agents/AGENTS.md` says "Everything else under `.agents/` is this project's own, produced by
working here — the task index, task packages, and the archive." In the repository used for the
dry run, `.agents/skills/` holds third-party skills installed by a tool and tracked in a lock
file at the repository root. They were not produced by working there and are not that project's
own.
Assumed: context-fold owns `.agents/`, having created it.
Actually: it shares it. `.agents/` is a convention several tools write into, and this repository
only looked like the owner because it was the only occupant. The claim is false in any repository
using a skill installer, which is common, and it is stated in a portable file — so it is false
everywhere that happens, not just once.

### The deletion test tells an adopter to delete other tools' data

The same file states the test as "Remove `.agents/` and read what remains." Doing that in the dry
run repository also removed every vendored skill and left its lock file describing nothing.
Assumed: the layer and the directory are the same thing, so removing one removes the other.
Actually: the test should be scoped to what context-fold put there — the three rule files and
`tasks/` — not to the directory. As written it is destructive in exactly the repositories most
likely to adopt this, and it is the first instruction task zero gives an adopter.
Not fixed here. Both defects are in a portable rule file, which reaches every installation, so
they need their own task and record rather than riding along in this one. `ADOPTING.md` was
changed to reference the test rather than restate it, so this document does not contradict the
file it tells people to copy.

### An incomplete instruction was completed instead of questioned

The procedure said to record the commit the rule files came from, without saying where to write
it or how to obtain it. Review found the gap, and the first response was to fill it: a
`.agents/SOURCE.md` holding origin, commit, and date.
Assumed: an instruction with a gap needs the gap filled.
Actually: it needed asking what the instruction was for. Provenance answers "which version am I
running", which only has a consumer once upgrading exists — and upgrading is deferred. The fix
added a hand-maintained file that nothing reads and nothing verifies, to serve a capability that
does not exist. The file said "nothing verifies it" in its own body, which should have been the
tell.
Removed. Git already answers the question when it needs answering, and v0 declines both
provenance and upgrading rather than half-answering both.
This project has nine logged instances of hand-maintained restatements drifting from their
source. The tenth was designed in deliberately, in the same session that recorded the pattern.

### The dry run performed a step the procedure had not written down

Step two was missing from the document but not from the run: the commit went into a shell
variable, so the procedure looked followable while being incomplete.
Assumed: following your own procedure tests it.
Actually: the author supplies gaps without noticing, because the knowledge that fills them is not
in the document. A dry run by whoever wrote the procedure is much weaker evidence than it feels
like — the real test is someone following it cold.

### The lint step enumerated the repository by hand and immediately went stale

`ADOPTING.md` was added and CI did not lint it, because the workflow listed paths explicitly.
Assumed: naming the paths is precise and therefore safe.
Actually: it is a second enumeration of the repository's contents, kept in step by memory. A new
root document is silently unlinted, and silence is the failure mode again — the step passes,
reporting on less than it appears to.
Replaced with a recursive scan honouring `.gitignore`, which derives the file list instead of
repeating it. Third instance in two tasks of a tool quietly examining less than expected; the
first was the linter not recursing, the second was checks vanishing on an empty parameter set.

### The linter's exit code had never been checked

The CI step ran the linter and assumed a violation would fail the build. Nothing had confirmed
it: every run so far was clean, so the step had only ever returned zero.
Verified directly — clean exits 0, a trailing-whitespace violation exits 1.
Assumed: a linter in CI fails CI.
Actually: that is a property of the tool, and an unverified one is a decorative step. The same
mistake as trusting a check that has never failed, one level up: the suite's checks were all
mutation-tested, and the linter wrapping them was not.

### The dry run's value was in what it contradicted, not what it produced

The procedure itself worked: four steps, no ambiguity found, layer coexisting with an existing
`.agents/skills/` and an existing root `AGENTS.md` without conflict.
Assumed: a dry run tests the procedure.
Actually: the procedure was the least interesting thing it tested. Both findings are in files the
procedure only copies, and neither would have surfaced from reading them here — they required a
repository whose `.agents/` already had an occupant. Self-application cannot produce that, no
matter how carefully it is done.
