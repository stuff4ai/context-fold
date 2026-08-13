# Add convention checks

## Status

active

## Objective

Enforce the repository invariants that encode decisions, on every change, instead of checking
them by hand.

## Why

Nine tasks have ended with the same manual checks: does `INDEX.md` match the directories, do
links resolve, is the archive named correctly, did the portable files stay free of project
detail. Each was ad-hoc `grep`, and they have already missed things — the index has been wrong
once, and a portability leak reached human review rather than being caught before it.

Every one of these invariants encodes a decision. An unenforced rule drifts, and the drift is
silent: the last task found a rule contradicted by all eight tasks that followed it, with no
entry in any problem log.

There is no CI. Nothing runs on any change.

## Scope

- `tests/test_conventions.py` — the invariant suite.
- `.pymarkdown.json` — style rules.
- `requirements-dev.txt` — pinned `pytest` and `pymarkdownlnt`.
- `.github/workflows/ci.yml`.
- `decisions/0016-check-conventions-in-ci.md` and the index row.
- `OPEN-QUESTIONS.md` — whether the checks should ship with the portable layer.

## Out of scope

- Semantic checks. Nothing here reads a statement against what is already decided.
- External link checking.
- Reformatting existing prose to satisfy a linter.
- Any tooling that creates artifacts rather than checking them.

## Acceptance

1. The suite covers all nine checks in the plan, each naming the decision it encodes.
2. Every check has been made to fail deliberately and then reverted. A check that has never
   failed is unverified.
3. The suite passes on the current tree with no edits to existing content. A check that requires
   editing prose is wrong for this repository.
4. The same command runs locally and in CI with the same result.
5. The record states why verification tooling is consistent with `0012` rather than an exception,
   and that a passing suite proves structure and not correctness.

## Problems

### The linter was scanning a third of the repository

`pymarkdown scan decisions .agents` was reporting four violations and looked close to clean.
`pymarkdown` does not recurse without `-r`, so only the top level of each directory was scanned —
every task package and every archived problem log was skipped.
Assumed: passing a directory to a scanner scans the directory.
Actually: the tool requires `-r`, and the failure mode is a *quieter* report rather than an error.
A config tuned against that report would have been tuned against a third of the content, and the
suite would have passed for the wrong reason. Found only because a 247-character line in
`INDEX.md` should obviously have tripped a line-length rule and did not.
A check that silently examines less than it appears to is worse than one that fails.

### Four of the first five failures were the checks, not the repository

The first run failed on `.adr-template.md`: treated as a decision record with no number, with its
`XXXX-slug.md` placeholder read as a broken link.
Assumed: `Path.glob("*.md")` behaves like the shell and skips dotfiles.
Actually: `pathlib` matches hidden files. The template is correct prose, and the acceptance
criterion said a check requiring edits to existing content is wrong for this repository — so the
checks were fixed rather than the template.
Worth noting the criterion did the work. Without it the tempting fix was renaming the template.

### Two style rules can never be adopted

Line length is unsatisfiable: Markdown table rows cannot be wrapped, and this repository's tables
reach 250 characters. Fenced code language is unsatisfiable for a stranger reason — `0004`
violates it, and accepted records are immutable apart from `Status`.
Assumed: a linter is configured by choosing which rules to enforce.
Actually: for a repository whose accepted records cannot be edited, the adoptable rule set is
bounded by what history already contains, permanently. Every accepted record narrows it. Nothing
about immutability suggested it would constrain tooling chosen years later.

### The suite's first real catch was the record introducing it

`0016` was written without a `## Status` section. Sixteen records had been written by hand and
every one had all four sections; the seventeenth, written while building the thing that checks
for them, did not.
Assumed: the sections are habitual enough not to need checking.
Actually: they were habitual until attention went elsewhere. The omission survived writing the
record, re-reading it, and linking it from the index — three passes by someone thinking about
verification at the time.
The strongest evidence in this task for the checks being worth having, and it arrived before
they were committed.

### The mutation testing found a check that had never been challenged

Nine invariants were broken deliberately to confirm the suite caught them. Nine were caught; the
index check reported a miss.
The mutation was broken, not the check — a `sed` substitution with an empty pattern is a no-op, so
the file was never modified and the check correctly stayed green. Retried properly, it caught it.
Assumed: a mutation that produces no failure means the check is inadequate.
Actually: it can equally mean the mutation did nothing. A negative result from a test of a test
needs its own verification, and the obvious reading — blame the check — would have led to
rewriting a check that was already correct.
