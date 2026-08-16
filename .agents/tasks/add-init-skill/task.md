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
6. The skill runs against this repository — already adopted — and changes nothing: the index and
   task packages survive, the pointer is not duplicated, and no adoption task is opened.

## Problems

### The procedure assumed nothing was installed, and never said so

Running the skill against this repository — the first real user, and already adopted — broke
every step. Step 1 copies `templates/agents/` wholesale, taking `INDEX.md` with it: fourteen rows
became zero while thirteen task packages sat on disk. Step 2 appended a second `## Agent layer`
section. Step 3 would have opened an adoption task beside a live one.
Assumed: adoption happens once, so the procedure only needs the unadopted case.
Actually: every run after the first is the adopted case, on any repository — including a run
started by accident. It is the main path, not an edge, and the procedure had no branch for it.
All three failures are silent. `cp` reports nothing, the resulting index is valid Markdown that
simply lies, and a duplicated section reads fine. Our own suite catches the index damage; an
adopter has no suite, which is what makes silence the problem rather than untidiness.
Added an already-there path ahead of the steps: replace only the `AGENTS.md` files, leave the
index and tasks, leave an existing pointer, open no task zero, and say when nothing changed.

### The skill contradicted the procedure it ships

`ADOPTING.md` step 3 ended "archive it before the change is merged". `SKILL.md` says "Do not
archive the task, and do not merge anything."
Assumed: `SKILL.md` covers what the procedure leaves out, as it claims.
Actually: it overrode the procedure rather than supplementing it, and an agent reading both in
the order the skill directs would be told to archive and then told not to.
`ADOPTING.md` now stops at asking for approval, which is what `0007` actually requires — approval
authorizes archival. The procedure had compressed a three-stage sequence into one clause.
Fourth contradiction found in this repository that nothing checks for, and the first between two
files that ship together as one unit.

### The task template is optional in practice

Five runs produced five structurally correct task packages. Three wrote them from scratch; two
copied `templates/task/` and edited it. Every one had all seven required sections.
Assumed: shipping a skeleton is how the shape gets transmitted.
Actually: the shape is transmitted by `tasks/AGENTS.md`, which lists the sections, and by
`ADOPTING.md`, which describes task zero's content. The template restates it in a third place,
and agents reach for it about half the time.
Its only distinctive effect so far has been the placeholder leak, which is a failure mode the
template introduces rather than one it prevents.
Recorded, not acted on. Two of five used it and it worked, and the fix for the leak has not been
tested — the run after it was written bypassed the template entirely, so the absence of residue
proves nothing.

### Template examples written in the voice of real content survived as content

Two more foreign runs, in two unrelated repositories, both left
`` `.agents/tasks/AGENTS.md` — why it matters here. `` in the finished package. The other example
line was replaced in both, because it named a file that did not exist there.
Assumed: an example in a template reads as a shape to copy.
Actually: only if it is marked as one. The two example lines were written in the same voice and
format as real entries, so the one naming a real file read as a valid entry with a lazy
description — and a lazy description is not obviously wrong, so it stayed.
Both examples were added when the relative-links defect was fixed. Fixing one problem introduced
this one, and it took two runs in two repositories to see it because a single run looks like an
agent being careless.
Replaced with one line using a braced placeholder, matching how the index shape is already
written. Two examples also invited keeping one; one cannot be kept.

### A hazard left as documented bit a second time, in the opposite direction

`templates/agents/` held three files that must never change and one that must change
immediately. When reinstalling destroyed a populated index earlier in this task, that was
recorded and the layout left alone: "one instance of the hazard is not enough to choose."
A third foreign run then compared every installed file against its template — including the
index it had just correctly filled in — and got a failure describing nothing wrong. It
recognised its own mistake and fixed the check.
Assumed: documenting a trap is enough when it has been seen once.
Actually: the same ambiguity produced data loss in one direction and a false alarm in the other,
from two different agents. What made both reasonable is that the directory looks uniform and
is not.
`INDEX.md` moved out of `templates/agents/`, so the rule now follows from the layout: everything
in that directory is safe to copy over an installation, always. The identity check lost its
exclusion, and the shipped rule files lost their relative link to `INDEX.md` for the same reason
task packages lost theirs — written in one directory, read from another.

### Two runs of the same instructions diverged on the index

A second foreign run, same repository, fresh session, left `INDEX.md` saying `None.` under
Active while the task directory it had just created sat beside it. Its own acceptance pass
reported success. The first run had added the row.
Assumed: one of the runs was wrong.
Actually: both followed what is written. `ADOPTING.md` never says to add the task to the index,
and the tasks rules mention updating `INDEX.md` only under Finishing, at archival. Starting a
task says to write `task.md` and `context.md` and stops there.
This repository always adds the row because a check fails otherwise — the convention is enforced
here and stated nowhere, so it never shipped. Same shape as the relative-links finding, found
the same way: two agents doing different reasonable things with the same instructions.
Now stated where a task starts, with the reason: the index is derived from disk, so a missing
task makes it wrong from the moment the task begins.

### The agent retyped the rule files instead of copying them

The install produced rule files that differed from their templates on three of four
comparisons — pure line-rewrapping, semantically identical, byte-different — and omitted
`tasks/archive/AGENTS.md` entirely on the first pass. The agent had reproduced the contents from
what it had read rather than copying files.
Assumed: "copy them unchanged" describes a copy.
Actually: for an agent that edits by patch, writing a file is the default way to create one, and
"copy" reads as a description of intent rather than of mechanism. A copy cannot drop a file or
rewrap a line; a transcription does both silently.
It ended correct only because it byte-compared unprompted and iterated until `cmp` passed —
behaviour the procedure never asked for. `ADOPTING.md` and `SKILL.md` now say to copy rather than
retype, and to verify byte-identity before continuing.

### A foreign agent installed it, and the parts that held were the ones never tested here

A second agent, on a different model and a different installer, ran the skill against an
unrelated production monorepo. Its installer had copied the whole package — templates included —
to a global skills directory, which validates the bundling decision independently of the one
installer examined when it was made.

The run read the procedure first, checked base state before writing, left the existing
`.agents/` artifacts alone, verified the rule files byte-for-byte against the templates unasked,
ran the project's own format check, logged two real problems, and stopped before archiving to
ask for approval.

Recorded because every one of those was a behaviour this repository could not test. Self-
application cannot show whether an instruction survives an agent that has never read the
reasoning behind it.

### Relative links in a task package break when the package is archived

The foreign run's `context.md` pointed at `../../docs/prd.md`. The file exists; the link
resolves to `.agents/docs/prd.md` and misses by one directory. Four of its seven references were
dead that way, and two more resolved to the wrong file while looking correct —
`../../AGENTS.md` labelled as the repository's conventions is the layer contract, not the root.
Assumed: getting the depth right is the fix.
Actually: depth is not stable. A package sits at `.agents/tasks/{slug}/` and archives to
`.agents/tasks/archive/{ts}-{slug}/`, one level deeper, so a link that is correct today breaks on
archival — or keeps resolving and silently points somewhere else, which is worse.
This repository never hit it because its packages reference project artifacts as root-relative
paths in code spans. Thirteen archived packages, zero relative links, entirely by instinct: the
convention was being followed and had never been written down, so it shipped to nobody.
Now in the template with an example, and in the rules with the reason.

### Adoption met a repository that already had a task system

The target's `.agents/` held roughly twenty-three archived task directories from an earlier
workflow, plus an active package in `.agents/tasks/`. The layer installed a second task system
beside the first: `.agents/tasks/archive/` next to `.agents/archive/`, and an index listing one
task while another sat undeclared in the same directory.
Assumed: "other tools write there too" covers coexistence. It covers `skills/`.
Actually: it does not cover another tool doing the same job. The index ships as a derived view of
task directories and was false in its first real installation.
The foreign agent invented the right answer without being told — record the existing system as
base state, leave it untouched, note it under `## Problems`. That is now in the procedure as an
explicit limit: this installs a layer, it does not convert one. Migration stays out of scope, and
saying so is what stops the next agent re-deriving it.

A cold run by a second agent — Codex, no knowledge of this project — ended without installing
anything: its sandbox permitted reading `.agents/` and not writing it. It probed with a `touch`,
reported the constraint precisely, reverted the one partial edit it had made, and left the tree
clean.
Not a defect in the skill, and worth recording anyway: adoption writes to a hidden directory,
and an agent under a default sandbox may be able to read the whole repository while being unable
to create the one thing it was asked to create. Nothing in the procedure anticipates being
unable to write, and the failure surfaced only because that agent checked rather than assuming.
The behaviour under the constraint was better than the procedure asks for — it left nothing
half-installed, which no instruction told it to do.

### A check still treated the whole of `.agents/` as the layer

Installing the skill to `.agents/skills/ctxfold-init/` broke
`test_distribution_is_complete` immediately. It globbed every `AGENTS.md` under `.agents/` and
swept up the skill's own bundled templates, which are not part of any installation.
Assumed: `0018` fixed the layer-is-not-the-directory confusion.
Actually: it fixed the prose. The check was written before that record and kept the old
assumption, and nothing connected the two — a record narrows what a document claims, not what
code does. The check had been correct only because nothing else had ever been under `.agents/`
in this repository, which is the same reason the original defect was invisible.
Narrowed to the layer's own subtrees, and verified it still catches both directions.
Found by changing where the skill installs. The first thing that ever shared `.agents/` here
exposed it in seconds.

### The installed skill was stale, and the run used the old copy

Invoking the skill loaded `.claude/skills/ctxfold-init/`, a copy made before the fixes above.
The run followed the pre-fix procedure.
Assumed: editing `skills/ctxfold-init/` changes the skill.
Actually: installing copies it. The installed skill is an installation of the distribution, with
exactly the drift problem `0018` solved for `.agents/` — and nothing detects this one. `.agents/`
has an identity check because it is tracked; `.claude/` is untracked and vendor-specific, so the
same check would require deciding whether an adapter directory belongs in the repository at all.
Noticed only because a section I had just written was missing from the loaded instructions.

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
