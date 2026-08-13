# Add an init skill

## Status

active

## Objective

Ship adoption as a skill an agent can invoke, without the skill becoming the definition of what
adoption is.

## Why

`ADOPTING.md` works — the previous task followed it by hand against a real repository. It cannot
reach a repository that does not already have this one beside it.

Skill installers copy a whole skill directory, subdirectories included, so a skill that bundles
the distribution is installable by tooling that already exists. That makes the skill directory
the unit of distribution: everything adoption needs has to live inside it, including the
procedure itself.

`0011` permits an agent product's convention only as an adapter. The procedure travels with the
skill and stays authoritative; the skill covers what the procedure does not — how an agent should
conduct itself while following it.

## Scope

- `skills/ctxfold-init/` — `SKILL.md`, plus `ADOPTING.md` and `templates/` moved from the root.
- `tests/test_conventions.py` — the relocated templates path, and checks for the skill package.
- `decisions/0020-ship-an-init-skill.md` and the index row.
- `README.md`, root `AGENTS.md`, `OPEN-QUESTIONS.md`.

## Out of scope

- Versioning, pinning, and upgrade paths.
- A check binding the skill's instructions to the procedure's steps.
- Adopting into a live repository.
- Skills beyond `init`.

## Acceptance

1. `skills/ctxfold-init/` contains everything adoption needs, and nothing it references falls
   outside the directory.
2. `SKILL.md` does not restate the procedure. It covers finding the project's workflow, supplying
   judgment, and stopping before archival.
3. The skill package's checks — frontmatter, name matching the directory, self-containment — each
   made to fail and reverted.
4. A dry run driven by `SKILL.md`, against a scratch copy of a real repository, installs the layer
   beside an existing `.agents/skills/`, writes the pointer into an existing `AGENTS.md`, fills in
   task zero, and stops before archival.
5. What the skill produced matches what `ADOPTING.md` specifies, or a divergence is recorded as a
   defect in one of them.

## Problems

### The package layout was justified from principle when evidence existed

`0020` argued for bundling `ADOPTING.md` and `templates/` beside `SKILL.md` from first
principles — the directory is what travels, so everything must be inside it. Correct, and
unnecessary: seven installed skills were sitting in another repository, every one carrying a
`README.md` at its root, one shipping `SECURITY.md` and a `scripts/` directory its `SKILL.md`
refers to as adjacent.
Assumed: the reasoning was the justification, so the observation was background.
Actually: the observation is the stronger argument and the one a reader can check. Reasoning
about what a format probably allows is guesswork next to seven examples of it being done.
Prompted by being asked whether a skill may contain anything but `SKILL.md` — a question the
evidence answered immediately and the record had not.
Also settled the layout: `ADOPTING.md` at the package root rather than under `references/`,
because that is where the examined skills put their prose and only code was nested.

### The guard written for silent skips did not cover the finder added after it

`skills()` returns an empty list when `skills/` is missing, so both skill checks would skip and
CI would pass with the whole package deleted.
Assumed: this class was handled — `test_discovery_finds_content` exists precisely because a
finder returning nothing removes its checks without failing anything.
Actually: the guard names the finders that existed when it was written. Adding `skills()` and
`installed_rule_files()` created two more silent-skip holes, and nothing connected the new
finders to the check protecting against exactly that.
Found in review. A fix for a class of bug does not cover later instances of the class, and
nothing reminds you — the guard cannot know what it does not enumerate.

### A stray file sat in the distribution and every check passed

Testing the guard above, a botched shell mutation left `tmpl.bak` inside
`templates/`. The full suite ran green with it there.
Assumed: the checks cover the distribution, since several of them read it.
Actually: they read the files they expect — `AGENTS.md` by name, Markdown by extension. Nothing
looked at what else was present. Everything in a skill directory ships, so that file would have
reached every installation, and the only reason it did not is that it was untracked.
Added a check for backup and editor artifacts. It is narrow on purpose: skills may legitimately
ship scripts and other non-Markdown, so the rule targets things that are obviously nobody's
deliverable rather than constraining what a package may contain.
Found by an accident during verification, which is the second time this task that the mistake
was more informative than the test.

### The plan had the skill following a file it would not ship with

The first plan said the skill "follows `ADOPTING.md` rather than restating it", with `ADOPTING.md`
staying at the repository root.
Assumed: the skill can reference the procedure, since they live in the same repository.
Actually: the skill directory is what an installer copies, so once installed the procedure would
not be there. The skill would have had to restate it — the duplication the sentence claimed to
avoid, arrived at by the plan that claimed to avoid it.
Caught in review before anything was built. Resolved by moving `ADOPTING.md` into the package, so
the reference resolves wherever the skill goes.
The self-containment check now encodes this: it is the same mistake, mechanized.

### Moving the procedure made its own instructions imprecise

`ADOPTING.md` said "copy `templates/agents/` from context-fold" and "context-fold ships
`templates/`". Both were written when it sat at the root and templates were a sibling directory
in the same repository. After the move, `templates/` is beside it in the package, and "from
context-fold" sends a reader looking for a checkout they do not need.
Assumed: moving a document does not change what it says.
Actually: it changes what its relative references mean. The paths still resolved — the check
passes — because they were relative and the relationship happened to be preserved. The prose was
what broke, and prose is what nothing checks.
Found by following the procedure rather than reading it.

### The linter misparsed the first file with frontmatter

`SKILL.md` produced six style violations: no top-level heading, headings not surrounded by blank
lines, inconsistent heading style. The file has none of those problems. The linter read the
opening `---` as a setext heading underline and reported the consequences.
Assumed: a clean lint run means the files are well-formed.
Actually: it means the linter parsed them the way it expects. A new file format produces
violations that describe the misparse rather than announcing it, and every one of the six looked
like an ordinary style complaint worth fixing by editing the file.
Fixed by enabling the front-matter extension. Editing `SKILL.md` to satisfy the misparse would
have broken the skill, and nothing would have said so.
