# Adopting context-fold

How a repository takes on the agent layer. Four steps, by hand — there is no installer.

This works the same for an empty repository and one with years of history. What changes is
the pointer step, where an existing `AGENTS.md` is added to rather than created.

## What you are adding

`templates/`, beside this file, is what gets installed. Adoption is installing it. Everything you
need is in this directory — nothing has to be fetched.

```text
templates/agents/   →   .agents/
```

The shape of a task package is not shipped as a skeleton to copy. `.agents/tasks/AGENTS.md`,
installed by the step above, lists the sections a task package needs; task zero below shows it
filled in.

Plus a pointer in the repository's root `AGENTS.md`.

Nothing else in the repository moves. `.agents/` may already hold other tools' files; the layer
sits alongside them and does not claim the directory. Removing the layer later is a normal
change.

Each portable `AGENTS.md` template is one managed block. The block starts at byte zero with
`<!-- agent-layer:begin -->` and ends with a standalone `<!-- agent-layer:end -->` line and its
terminating LF. The template ends there. An installation may append project-specific instructions
after that LF, but they must not contradict the portable rules. Updates replace the managed block
and preserve every byte of that suffix.

## If the layer is already there

`.agents/AGENTS.md` existing means this repository has adopted before. The steps below assume
nothing is installed, and following them as written destroys work: they can overwrite project
suffixes, add the pointer a second time, and open an adoption task for an adoption that already
happened.

Do this instead, in two phases. First preflight all five portable targets before changing any of
them:

1. A missing target is ready to receive its template. Keep the existing offer gate for a missing
   `worktrees/AGENTS.md`: treat it as an install candidate only if the user accepts that file and
   its `.gitignore` lines; otherwise omit that optional target from the update.
2. A target containing no line beginning with `<!-- agent-layer:` is a legacy whole-file
   installation and is ready to be replaced wholesale. The old contract already forbade local
   edits to it; this update does not attempt to recover any.
3. A managed target is valid only when it begins at byte zero with exactly one standalone begin
   marker, contains exactly one later standalone end marker with a terminating LF, and contains no
   other line beginning with `<!-- agent-layer:`. Record every byte after the end-marker LF as its
   project-owned suffix.
4. Anything else — a displaced, reversed, duplicated, unmatched, or malformed marker — is
   ambiguous. Stop the entire update without writing any target and ask the user to repair it.

Only after every target passes preflight, apply all selected candidates: install a missing file,
replace a legacy file wholesale, or replace exactly the managed block and append its recorded
suffix unchanged. Then verify that each installed block is byte-for-byte identical to its template
and every recorded suffix has the same bytes as before. Leave task packages alone.

Leave the root `AGENTS.md` alone if it already points at the layer, and do not open task zero.

If nothing changed, say so. A repository already holding the current rules is the expected
result, not a failure.

## 1. Install the layer

Copy `templates/agents/` from this directory to `.agents/` in your repository, preserving the
structure inside it.

```text
templates/agents/AGENTS.md               →  .agents/AGENTS.md
templates/agents/tasks/AGENTS.md         →  .agents/tasks/AGENTS.md
templates/agents/tasks/archive/AGENTS.md →  .agents/tasks/archive/AGENTS.md
templates/agents/skills/AGENTS.md        →  .agents/skills/AGENTS.md
templates/agents/worktrees/AGENTS.md     →  .agents/worktrees/AGENTS.md
```

Everything in `templates/agents/` — worktree conventions included — is a managed block that stays
byte-identical to its installed counterpart. An installed suffix may differ by design.

The five targets above are the layer contracts. The `skills/AGENTS.md` target is direct: do not
recurse into installed skill packages and classify their nested `AGENTS.md` files as layer
contracts.

**Copy the files. Do not retype them.** On a fresh adoption, use a file copy — `cp`, or whatever
your tools call it — and confirm every installed file is byte-for-byte identical to its template.
On an update, use the all-target preflight above and compare the installed managed blocks instead.
Reproducing contents from what you have read yields invisible differences: a rewrapped line, a
dropped paragraph, or a missing file.

The managed blocks are identical in every installation and carry no project-specific paths, names,
or decisions. Project-specific additions go only after the end marker and must not contradict the
block. That boundary keeps the portable rules replaceable without making the whole file uniform.

If a rule does not fit your project, do not edit or contradict the managed block. Record it as a
problem in task zero so a reviewed portable-rule change can address it.

## 2. Ignore the worktrees directory

`.agents/worktrees/` holds parallel checkouts, which must not be committed — except the file you
just copied there, which explains what they are. Add both lines to `.gitignore`, creating it if
the repository has none:

```text
.agents/worktrees/*
!.agents/worktrees/AGENTS.md
```

Both lines are needed, in that order. A directory excluded outright is never descended into, so
`.agents/worktrees/` alone would ignore the file as well and the exception would never apply.

Append to an existing `.gitignore` rather than rewriting it. If the repository uses something
other than Git, do the equivalent, and say what you did.

If this project will never keep more than one checkout at a time, skip the directory and its
file entirely and say so — nothing else depends on them.

## 3. Point at the layer

The root `AGENTS.md` is your project's file. context-fold adds a pointer to it and nothing else.

If the file already exists, add a section:

```markdown
## Agent layer

Agent operating context lives in `.agents/` — how work is organized, tracked, and finished
here.

Read [`.agents/AGENTS.md`](.agents/AGENTS.md) before starting work.
```

If the repository has no `AGENTS.md`, create one. It belongs to the project, so it should say
what the project is and how to work on it; the section above is the only part context-fold
contributes.

## 4. Open task zero

The adoption is itself a task, and it is the first one. This mirrors how decision records begin —
the first record is the decision to use records.

Create `.agents/tasks/adopt-context-fold/task.md` and `context.md` directly, with the frontmatter
and sections `.agents/tasks/AGENTS.md` requires. Start `task.md` exactly like this:

```yaml
---
status: active
objective: >-
  Establish the context-fold agent layer in this repository.
---

# Adopt context-fold
```

Then add the required sections. For task zero their content is:

**`task.md`** — Why: work here is organized as task packages so context survives between sessions
and agents, and so what is learned while working outlasts the working. Scope: the layer and the
root `AGENTS.md` pointer. Out of scope: changing existing documentation, conventions, or workflow.

Acceptance:

1. The layer is installed and the pointer resolves.
2. It satisfies the deletion test described in `.agents/AGENTS.md`.
3. The managed rule blocks are unmodified — nothing in them was adjusted to fit this project.

**`context.md`** — Base state: the repository as it is. What it contains, what conventions it
already has, where its durable knowledge lives, and what else already writes to `.agents/`.

Then work the task: finish the structure, satisfy the acceptance, and log every friction under
`## Problems` while it happens.

Before finishing it, do step 5 below — its findings belong in this same task's base state, not a
task opened afterward. Then finish task zero — Outcome, fold, archive, final check — and stop
there to ask for approval. Approval authorizes the merge, and what it is given for is the
finished state rather than a promise to file the paperwork later. The rules for all of that are
in `.agents/tasks/AGENTS.md`, which you now have.

## 5. Assess project-layer capabilities

Task zero's base-state discovery already looked at the repository once. This step asks it a
second, narrower question: for each of five capabilities, does the repository have an
authoritative, discoverable source, or not? Installing agent operating rules does not by itself
make a project's intent, decisions, documentation, verification, or reusable procedures
discoverable — this step checks whether they already are, without assuming an adopting
repository has any of them in place.

The five capabilities, and the question each one asks:

1. **Intent and requirements** — is there a document, anywhere, that states what the project is
   for and what it needs to do? A README's project description can satisfy this if it actually
   states intent; a README that only explains installation or usage does not.
2. **Decisions and rationale** — is there a place decisions and their reasoning are recorded, and
   is it singular or does it say which source governs when more than one exists?
3. **Documentation and knowledge** — is there a discoverable home for durable project knowledge
   beyond decisions — how things work, what a newcomer needs?
4. **Tests and verification** — is there a way to check the project behaves as intended, if the
   project has executable behavior to check at all?
5. **Agent skills** — is there any documented, reusable procedure an agent could follow for
   recurring work, in whatever format or location the project already uses, if any?

Classify each capability using only what task zero's base-state discovery already found — do not
open a new investigation:

- **Established** — an authoritative source exists and task zero's `context.md` already names it.
- **Partial** — something exists but is incomplete, split across locations with no stated
  precedence, or not clearly authoritative.
- **Absent** — nothing plays this role in the repository at all.
- **Ambiguous** — the evidence conflicts, or task zero's discovery could not tell which of the
  above applies.
- **Not applicable** — the project has no use for the capability (for example, no test suite
  because the repository holds no executable code).

Established and not-applicable capabilities need nothing further; task zero's base state already
names or accounts for them.

For each capability classified partial, absent, or ambiguous, first check whether a task package
named `assess-project-{capability}` already exists anywhere — `planned`, `active`, or under
`archive/` regardless of terminal status. If one does, do not create another: a human already
made or deferred that decision for this repository, and rediscovering it on every adoption run
turns guidance into ceremony. Note its path in task zero's base state instead.

Otherwise, create `.agents/tasks/assess-project-{capability}/task.md` and `context.md`, `planned`,
following the same shape task zero itself uses: `task.md`'s Why states the capability and cites
this step; Scope names the one capability being assessed; Out of scope repeats the boundary
below; Acceptance asks the human to choose the project's structure, improve what exists, or
decide the capability is not warranted, and to fold that decision into the project's own
artifacts before the task is archived. `context.md`'s Base state carries the specific evidence
task zero found — what exists, what is missing, where it conflicts — and may offer non-binding
recommendations naming paths or conventions as examples. The recommendation offers; it does not
choose. Do not create the document yourself.

This step assesses only the five capabilities above. Operations, security, data, release,
integrations, workflows, and MCP or tool configuration are out of scope for it — the same
boundary `task.md`'s Out of scope names for this task's own work, applied to what adoption does
in every repository.

## What this does not give you

**No overrides.** A repository may append non-conflicting instructions after a managed block. If a
portable rule does not fit, record it as a problem rather than overriding it locally. Multiple
blocks and finer-grained customization are not defined.

**No migration.** This installs a layer; it does not convert one. If `.agents/` already holds a
task system of its own — packages, an archive, another index — leave it exactly where it is.
Describe it in task zero's base state, note it under `## Problems`, and let the two coexist.
Deciding what to do about it is a later decision for that project, and not something adoption
should make on its behalf.

**No provenance or update discovery.** Re-running this procedure safely replaces managed blocks,
but nothing records which version you took or tells you when upstream rules changed. Note the
source commit in your adoption commit message if you want it later.

**Nothing runs.** There is no command, no check, and no automation. The layer is Markdown and a
directory structure, maintained by hand.
