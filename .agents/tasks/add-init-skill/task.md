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
