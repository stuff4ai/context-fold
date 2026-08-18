# Say what the rules mean when tasks run in parallel

## Status

completed

## Objective

Make the portable rules answer the questions two simultaneous tasks raise, and settle where this
repository's parallel checkouts live.

## Why

Every rule in the layer was written and exercised with one task running. The index already
anticipates concurrency — "one file that every concurrent task touches, so conflicts are
normal" — and nothing else does.

Five things break, or are simply unstated, the moment a second task starts.

**Two branches claim the same decision number.** Each passes the numbering check alone; only the
second merge fails. `0000` already says a record on a branch is a proposal and becomes truth at
merge, so renumbering before merge is permitted and nobody has said it is the answer. Decision
records are this project's convention rather than the layer's, so that belongs in the project
layer.

**Contention is only described for one file.** `INDEX.md` has a rule. `decisions/README.md` is
the same shape — a derived index every task edits — and has none. `OPEN-QUESTIONS.md` is
different in kind, authored rather than derived, and the difference is what decides how a
conflict in it is resolved.

**Nothing compares scope across active tasks, and the file is the wrong unit anyway.** Four of
this project's last five tasks edited `tasks/AGENTS.md`, almost always in different sections. A
rule that forbids sharing a file would serialise work that can safely run in parallel; the unit
that matters is the section.

**Nothing lets one task say it is waiting for another.** Work will be planned ahead of being
done, and some of it cannot start until something else lands. The four statuses describe what a
task *is*, not what it is waiting for, and there is nowhere to say "not yet, because".

**A finding may belong to a task you are not in.** `0022` routes a finding to its owning task.
With one task running the owner is obvious. With three it is a judgement, and the rule does not
say to make it.

Separately, this repository needs somewhere to put parallel checkouts, and that is a workflow
choice rather than a rule for adopters.

## Scope

- `templates/agents/tasks/AGENTS.md` — working alongside other tasks: declaring scope by section
  when a file is shared, declaring what a task is blocked by, whose task a finding belongs to,
  and conflicts in derived versus authored files.
- A decision record for the above, and for this project's own answers below.
- `AGENTS.md` — where this repository's worktrees live, and that a decision number is provisional
  until merge.
- `.gitignore` — so worktrees are not committed.
- `tests/test_conventions.py` — discovery must respect `.gitignore` rather than a hardcoded
  directory list, or the suite reads every parallel checkout as part of the repository.
- `OPEN-QUESTIONS.md` — correct the archive-collision entry, which describes a collision that
  cannot happen; record what this change deliberately leaves undecided.

## Out of scope

- Making the layer name git, worktrees, or any other version control mechanism. Review and merge
  already mean whatever a project defines, and this does not change that.
- Putting decision-record numbering in the portable rules. Records are this project's convention;
  `0005` says the layer does not prescribe another project's layout.
- Detecting scope overlap or unmet dependencies mechanically. The rules can say to declare and to
  look; parsing prose scope statements is a different and larger thing.
- A fifth status. Blocked is not what a task *is*, and `0006`'s four values stand.
- Showing dependencies in `INDEX.md`. Start with the declaration; add the derived view only if
  scanning task files turns out to be the thing that fails.
- Locking, claiming, or any protocol that requires agents to communicate.

## Acceptance

1. The rules say to read the other active tasks before starting, and that two tasks may hold the
   same file when they hold different sections of it.
2. A task can declare what it is waiting for, and the rules say not to start it until that is
   met. No new status value is introduced.
3. The rules distinguish a derived file, which is rebuilt after a conflict, from an authored one,
   which is merged — and `INDEX.md`'s existing rule is the general case rather than a special one.
4. The rules say a finding belongs to the task whose work produced it even when that is not the
   task you are in.
5. Nothing added to the portable rules names git, or decision records, or any artifact a project
   might not have.
6. This repository states where its worktrees live and that a decision number is provisional
   until merge.
7. A worktree under `.agents/worktrees/` is invisible to both the linter and the test suite —
   verified by creating one and running both, not by reading the code.
8. The `OPEN-QUESTIONS.md` archive-collision entry says what can actually go wrong.

## Outcome

The layer now says what it means when two tasks run at once, without naming git or anything else
a project might not have.

Scope is declared by section rather than only by file, so two tasks sharing `tasks/AGENTS.md` is
ordinary rather than a conflict — which is what four of the last five tasks actually did. A task
that cannot start yet carries `## Blocked by` and stays `planned`; blocked is what a task waits
for, not what it is, so `0006`'s four values are untouched. `## Index conflicts` became
`## Conflicts`, with `INDEX.md` as the example of a derived file rather than the only file
anyone thought about, and a test for telling derived from authored: ask what deleting it would
cost. And a finding belongs to the task whose work produced it, which is now stated because with
three tasks open it stops being obvious.

This repository's own half: worktrees under `.agents/worktrees/{task-slug}`, ignored by Git, and
decision numbers provisional until merge — the second branch to reach a number renumbers, which
`0000` already permitted by calling a branch record a proposal.

Durable artifacts:

- `decisions/0025-run-tasks-in-parallel.md` — the decision, both halves.
- `skills/ctxfold-init/templates/agents/tasks/AGENTS.md` — a new `## Working alongside other
  tasks`, `## Conflicts` replacing `## Index conflicts`, and `## Blocked by` in the file list.
- `AGENTS.md` — the worktree convention and provisional numbering.
- `.gitignore` — one line.
- `tests/test_conventions.py` — discovery asks Git what the repository contains.
- `OPEN-QUESTIONS.md` — the archive-collision entry corrected to the problem that exists;
  two entries added for what this deliberately left undecided.

Verified by building it rather than reading it: a probe worktree was created under
`.agents/worktrees/`, both tools run, and removed. Git ignored it, the suite counted 224 both
times, the linter stayed clean. Under the old discovery the same probe would have added 91
phantom files to a repository of 92.

## Problems

### Nearly asserted a second gap that a shipped record already closes

The plan was to narrow `0000`'s "records are never renumbered" so that a branch could renumber.
Assumed: an absolute-sounding rule in an accepted record needs narrowing before it can be worked
around.
Actually: `0000` already says "A decision record becomes project truth when it is merged into
`main`. A record proposed on a branch is a proposal", two paragraphs above the sentence in
question. Renumbering a proposal was never forbidden. The narrowing would have been ceremony
attached to a rule that already worked.
This is the same mistake as claiming nothing describes re-entering an adopted repository, which
`ADOPTING.md` had covered since it shipped. Both were caught by reading the whole file before
writing about it — the first by a verifier, this one by checking because of the first.

### The suite and the linter disagreed about what the repository is

`markdown_files()` walked the tree against a hardcoded `{".git", ".venv", ".idea", ".vscode"}`;
`pymarkdown` ran with `--respect-gitignore`.
Assumed: both tools see the repository, so a `.gitignore` entry is enough to hide a worktree.
Actually: only one of them reads `.gitignore`. With a single probe worktree present, the old
discovery found 183 Markdown files where 92 exist — a second copy of every record and every
archived task, checked as though it belonged here. The linter saw none of them.
Measured rather than reasoned about: the probe was created, both tools run, then removed.
Fixed by asking Git what the repository contains instead of keeping a list that has to be
remembered. The list had four entries and would have needed a fifth today.

### Editing prose by slicing on a heading cut through a code span

Rewriting `## Scope` by slicing the file between headings cut at the first occurrence of the
string, which was inside `` `## Scope` `` in a sentence of the Why section. The result spliced
an orphaned fragment of the old text into the middle of the file.
Assumed: a heading is a safe anchor in a document about headings.
Actually: this project writes about its own section names constantly, so heading strings appear
in prose more often than as headings. Caught immediately because the section list came out wrong,
but nothing would have caught a subtler cut.

### git mv cannot archive a task package that was never committed

Finishing ran `git mv` on the task directory and it failed with "source directory is empty" —
the package was untracked, so Git had nothing to move.
Assumed: archival is a `git mv`, because that is what every previous task used and it always
worked.
Actually: every previous task committed its package early, so by archival time Git knew about it.
This one was written and finished without an intermediate commit. `git mv` refuses untracked
files, a plain `mv` does not, and `## Finishing` says "move the directory" without saying how.
Worse than the failure: the index update ran anyway and inserted a row naming the wrong
directory, because it read the archive as it was after the failed move. Two mistakes, one
visible, one not — the checks caught the second.
Repaired by rebuilding the archive rows from disk, which is what `## Conflicts` now says to do
with a derived file. The rule written this task fixed the mistake made finishing it.
