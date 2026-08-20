---
status: completed
objective: >-
  Make the portable rules answer the questions two simultaneous tasks raise, and settle where this
  repository's parallel checkouts live.
---

# Say what the rules mean when tasks run in parallel

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
- `.gitignore` — so worktrees are not committed, and so the one file below is.
- `.agents/worktrees/AGENTS.md` — a project-owned marker saying the checkouts beside it are not
  this repository's context.
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
- `.gitignore` — two lines, because a directory excluded outright is never descended into.
- `.agents/worktrees/AGENTS.md` — the one tracked file there, saying the checkouts beside it
  belong to other branches.
- `tests/test_conventions.py` — discovery asks Git what the repository contains.
- `OPEN-QUESTIONS.md` — the archive-collision entry corrected to the problem that exists;
  two entries added for what this deliberately left undecided.

Verified by building it rather than reading it: a probe worktree was created under
`.agents/worktrees/`, both tools run, and removed. Git ignored it, the suite counted the same
number with and without it, and the linter stayed clean. Under the old discovery the same probe
would have added 91 phantom files to a repository of 92.

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

### Rewrote a correct entry into a wrong one, arguing against my own change

`OPEN-QUESTIONS.md` said archive names "can still collide", which faithfully paraphrased `0009`.
I replaced it with an entry declaring collision impossible and accusing `0009` of treating the
timestamp as settling order.
Assumed: the entry was inherited and unchecked, and the directory shape `{timestamp}-{slug}`
proved collision impossible because two active tasks cannot share a slug.
Actually: `0009`'s Consequences say both things verbatim — "two tasks archived in the same minute
unordered relative to each other", and "concurrent branches also cannot collide on a directory
name unless they archive within the same minute, which a day-only prefix made likely and this
makes remote". The original entry was right; the correction was wrong; and the accusation was of
an oversight the record does not have.
The reasoning failed in the direction of the change being made. "Two active tasks cannot share a
slug" holds inside one working tree. This task introduces separate checkouts per task, where two
agents pick slugs without seeing each other's and nothing on `main` registers one in flight — so
collision became *more* reachable in the same commit that declared it impossible.
Third instance this session of asserting something about the project without reading the record
that owns it: the re-entry gap `ADOPTING.md` had covered, the renumbering rule `0000` had already
scoped, and now this. The first was caught by a verifier, the second by checking because of the
first, and this one by a verifier again — checking is not yet a habit, it is a reaction.

### Answered "should the layer have a worktrees AGENTS.md" without considering the third option

The proposal was `.agents/worktrees/AGENTS.md`. I argued against it because a rule file inside
the layer ships to every installation, which would make git worktrees part of the model.
Assumed: a file at that path is necessarily a layer file, so the objection settles the question.
Actually: `0018` says the layer is what was installed and `.agents/` is only where it lives, and
the checks already follow that — `installed_layer_files()` reads `.agents/AGENTS.md` and
`.agents/tasks/` and claims nothing else, `PORTABLE` is an explicit list of three. A
project-owned file at that path was available all along and fails nothing.
It also has a purpose the portable rules cannot serve. The directory is reachable from the main
checkout, and an agent that wanders in finds a full second copy of every record, task package and
index with nothing saying they belong to another branch. That warning has to live where the
mistake happens.
The objection was sound about the shipped version and I let it answer a question it did not
cover. Raised again by the person who proposed it, after the change had shipped without it.

### `git check-ignore` exit status does not mean what it looks like

Verifying that the new file escapes `.gitignore`, `git check-ignore -v` exited 0 and the check
printed "STILL IGNORED".
Assumed: exit 0 from `check-ignore` means the path is ignored.
Actually: it means a pattern *matched*, and a negation is a pattern. The `-v` output said
`.gitignore:7:!.agents/worktrees/AGENTS.md` — the `!` being the whole answer. The file was
tracked and the test reported the opposite.
Caught because `git status --porcelain -uall` disagreed with it in the same output. Re-verified
against `git status` with a real worktree present, which is the oracle: `AGENTS.md` listed,
the checkout absent.

### Repaired the false claim in one file and left it in the file that called it a checked fact

The collision claim was corrected in `OPEN-QUESTIONS.md` after a verifier refuted it. The same
reasoning, in the same words, stayed in this package's `context.md` under the heading "Base facts
checked rather than assumed".
Assumed: the refuted statement lived where the verifier pointed, so repairing that closed it.
Actually: I had written it twice in the same change — once as a project open question and once as
the task's own base state — and repaired only the copy that was cited. The surviving copy was
introduced by this branch, contradicted `0009` and contradicted the repair, and sat under a
heading asserting it had been checked.
Found by the next verifier, in the round whose whole purpose was confirming the repair.
This is the twin-stranding pattern applied to a correction rather than to a rule, which is worse:
a stale rule is out of date, a stale correction re-asserts something already known to be false.
The section now keeps the claim as a disproved assumption rather than deleting it, because what
it got wrong is the useful part.
