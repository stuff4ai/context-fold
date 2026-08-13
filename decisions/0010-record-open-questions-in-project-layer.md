# Record open questions in the project layer

## Status

Accepted

## Context

A task's `context.md` holds an Open questions section
([0006](0006-task-package-model.md)), which is the right place for a question that belongs to
that task — something unresolved while the work runs and settled or irrelevant once it ends.

Most questions are not like that. What a project has deliberately postponed, and what using it
has shown to be unresolved, outlives the task that noticed it. Written into a task package,
such a question is archived along with the task, and archived packages are historical records
rather than current truth. The project's live unknowns then sit where the rules say not to
look for current state.

Deferred scope has the same problem. A decision not to build something is durable project
knowledge — it tells a reader what is missing on purpose — and the deletion test says durable
knowledge cannot live only inside `.agents/`.

## Decision

Open questions and deferred scope live in `OPEN-QUESTIONS.md`, in the project layer.

A task's `context.md` holds only questions local to that task: things that must be resolved,
assumed, or worked around to finish it. A question that will outlive the task belongs in
`OPEN-QUESTIONS.md` instead, and may be added there by the task that raised it.

An item leaves `OPEN-QUESTIONS.md` when it becomes a decision record, or when it turns out not
to matter. The document records no plan, schedule, or priority — those would make it a roadmap,
and this project has no basis for one.

Where an archived package and `OPEN-QUESTIONS.md` disagree, the project-layer document is
current and the archived copy is history.

## Consequences

The questions a project has not answered are visible in the project layer, next to the answers
it has.

A reader deciding what to build next has one list to read rather than an archive to excavate.

Questions already written into archived packages are now duplicated by the live list. The
archived copies cannot be trimmed, so the duplication is permanent, and the rule above is what
keeps it from becoming ambiguity.

The distinction between a task-local question and a project question is a judgment, and
judgments decay. A question misfiled into a task package will be archived with it and lost
from view.

Nothing enforces that an item is removed when it is answered, so the document will drift toward
listing questions that are already decided.
