# Check task packages for scaffolding by shape

## Status

Accepted

## Context

[0029](0029-drop-the-task-template.md) removed `templates/task/` because, across seven measured
adoption runs, copying it was the only mechanism shown to leave placeholder or instructional text
in a finished task package. Two runs adopting `etu-forms`, evidence recorded in
`.agents/tasks/archive/2026-08-19-1250-decide-whether-the-task-template-earns-its-place/context.md`,
found four defects in one finished package: an instructional paragraph kept under
`## References`, one kept under `## Open questions`, an `## Assumptions` heading left in place
with nothing under it, and a duplicated `## Problems` heading holding the placeholder beside the
real entry. Removing the template closes the one mechanism measured to produce these; it does not
stop a `task.md` modeled on an old archived package, or `ADOPTING.md`'s task-zero prose copied
without trimming, from producing the same four shapes by a different path.

`tests/test_conventions.py::test_task_package_has_required_files` checks that a package has
`task.md` and `context.md`. Nothing checked what sits inside a section beyond that.

The four defects split into two kinds. The duplicated heading and the empty `## Assumptions` are
facts about document *shape* — checkable by reading heading structure, with no judgment about
what the prose says. The two instructional paragraphs are facts about document *content* — telling
them apart from real content means recognizing that a sentence restates this project's own rule
text rather than describing this task's own work.

Of the two shape defects, only one is actually unchecked. `.pymarkdown.json` already enables
MD024 with `siblings_only`, and [0016](0016-check-conventions-in-ci.md) already runs
`pymarkdownlnt` over every Markdown file in CI — confirmed directly, against a file reproducing
the duplicated-`## Problems` shape, which MD024 flags. A duplicate heading in a task package was
never actually unguarded; it only looked that way because `test_conventions.py` alone does not
check content, and the lint step that does was not the one this task started from. Only the empty
`## Assumptions` heading has no existing check.

The two instructional-paragraph defects have no precise implementation available. The candidate
rule text lives in `.agents/tasks/AGENTS.md` and `skills/ctxfold-init/ADOPTING.md`, and this
project's own decision records and task packages routinely quote that same text on purpose —
[0029](0029-drop-the-task-template.md) itself quotes the two instructional paragraphs verbatim, in
its own `## Context`, to describe the defects. A check precise enough to flag a copied instruction
without flagging a deliberate quotation would need to read intent, not shape. Matching literal
phrases from the current rule text catches only today's wording — the exact narrowness
[0029](0029-drop-the-task-template.md) rejected in a fixed template, whose one applied fix ("a
braced placeholder replacing a realistic-looking example line") went unexercised until
`etu-forms` found a category it never touched. Matching by similarity threshold trades that
narrowness for an opaque one: a threshold tuned on two known runs offers no way to state, in
advance, what it will and will not catch in the next one.

## Decision

`tests/test_conventions.py` gains one check: `test_archived_task_has_no_empty_optional_heading`.
Once a task is archived, none of its optional headings (`## Blocked by`, `## Approval` in
`task.md`; `## Assumptions`, `## Open questions`, `## Context conflicts`, `## Base state`,
`## Not relevant` in `context.md`) may have an empty body. Archival is what turns "declared and
left for later" into "declared and never used": `.agents/tasks/AGENTS.md` already lets an active
task carry an optional heading it means to fill before it is done, so only archived packages are
checked.

No check is added for duplicated headings. MD024 (`siblings_only`) already catches a heading
repeated among its siblings in one file, in the lint step [0016](0016-check-conventions-in-ci.md)
already runs — adding a second, pytest-side check for the same shape would be two expressions of
one rule with no decision behind the duplication.

No check is added for the two instructional-paragraph defects. Recognizing copied instruction
against deliberate quotation of the same source text is not a shape a mechanical check can read
reliably in this project, for the reason in `## Context`. This is a decision not to add the check,
not a deferral pending a better idea — the two mechanisms considered are named above, and both
were rejected on their own terms.

`.agents/tasks/AGENTS.md` gains one sentence, next to where optional headings are introduced for
`task.md` and `context.md`: an optional heading not yet filled in is left out, not kept empty
against a later archival — matching the new check.

## Consequences

Three of the four `etu-forms` defects are covered mechanically, in CI, between two independent
mechanisms: the duplicated-heading shape by the existing `pymarkdownlnt` step, unchanged by this
record, and the empty-`## Assumptions` shape by the one check this record adds to `pytest`.
Tested against the reported evidence directly: a file reproducing the duplicated `## Problems`
heading fails the existing lint step, and one reproducing the empty `## Assumptions` heading fails
the new `pytest` check. The full suite passes unchanged against every task package currently on
disk.

False-positive risk for the new check: near zero. An optional heading empty at archival is, by the
argument above, always something that was declared and never used — there is no legitimate reason
to ship one that way.

False-negative risk: by design, total, for the two instructional-paragraph defects — nothing added
here reads section content for copied prose. A future run can still reproduce those two
`etu-forms` defects undetected. Catching them stays a human review concern, the same as it was
before this record, and a project that wants that coverage back needs a different mechanism than
the one considered and rejected here, not a tuning of this one.

The new check reads only task packages, matching this task's own scope; it says nothing about
empty optional headings in decision records or elsewhere in the repository.
