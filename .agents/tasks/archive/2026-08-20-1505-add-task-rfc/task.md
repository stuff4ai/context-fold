---
status: completed
objective: >-
  Add an optional `rfc.md` for mutable proposal discussion, and distinguish it from an agreed
  `plan.md` that guides execution after the direction is settled.
---

# Add an RFC artifact to task packages

## Why

The current task model gives `plan.md` two jobs. It is the place where an execution strategy is
written, and it is explicitly mutable while work proceeds. There is no task artifact for an
earlier conversation whose proposal, alternatives, review feedback, and open questions are still
changing.

Putting that discussion into `plan.md` makes it unclear whether a direction has been selected.
Treating the plan as an immutable decision would create a different problem: durable decisions
belong in project artifacts, while implementation details still need to adapt to what execution
reveals. A separate RFC can hold the unsettled proposal without becoming a raw transcript or a
second source of project truth.

## Scope

- `decisions/0033-*.md` — a provisional decision defining optional `rfc.md` and the revised role of
  `plan.md`; its number and every reference to it move together if the number collides before
  merge.
- `decisions/0006-task-package-model.md` — Status only, naming the new narrowing.
- `decisions/README.md` — decision-index table only, adding the new record under its final number.
- `README.md` — `## Tasks` only, updating the task-artifact summary.
- The `## The files`, `## Status`, `## Stages`, and `## Finishing` sections of the portable task
  rules in `.agents/tasks/AGENTS.md`, their shipped template, and the installed skill copy.
- `tests/test_conventions.py` — task-package helpers and tests only, encoding the decided RFC state
  matrix with direct positive and negative cases.
- `OPEN-QUESTIONS.md` — only the **Metadata schemas** and **Which task-local choices are worth
  preserving as decisions?** entries directly narrowed or resolved by this decision.
- `.agents/tasks/INDEX.md` — this task's derived row and eventual archival update.

## Out of scope

- Reorganizing all entries in `OPEN-QUESTIONS.md` by topic.
- Storing raw chat transcripts, hidden reasoning, or uncurated source material.
- Making an RFC mandatory for every task.
- Moving durable project decisions out of `decisions/` or other project-owned documentation.
- Changing task creation, archival, index maintenance, or other lifecycle automation.

## Acceptance

1. A decision record defines the responsibilities and lifecycle of `task.md`, `context.md`,
   optional `rfc.md`, optional `plan.md`, and durable project decisions without assigning the
   same authority to two artifacts.
2. `rfc.md` is the mutable place for a curated proposal, alternatives, open questions, and review
   feedback while direction is unsettled; it is explicitly not a raw transcript or durable
   project authority.
3. `plan.md` represents the selected execution strategy. Its direction is settled before
   implementation starts, while tactical details may still change without altering the task
   contract.
4. The portable rules say when either optional artifact earns its place, how an RFC is resolved
   or reopened, and where its durable outcome must be folded before acceptance.
5. The final task package has a resolved RFC with one non-empty Resolution and a plan consistent
   with that Resolution.
6. Convention tests use a dependency-free recognizer for the exact three-line RFC frontmatter and
   directly exercise every supported row in the decided task/RFC/plan matrix plus each named
   malformed or forbidden case; no YAML dependency is added.
7. Shipped and installed portable rules remain byte-identical, relevant documentation and live
   questions agree with the decision, and pytest, recursive Markdown lint, and
   `git diff --check` pass.

## Problems

The initial acceptance criterion said the task would discuss its RFC while remaining `planned`.
Fresh review showed that this contradicted the accepted status model: substantive discussion,
review, and evidence gathering are work, even when implementation is still gated. The task became
`active`, and the RFC now separates task status from permission to implement.

The first plan-readiness review found four omissions: decision-index and supersession integration,
a precise dependency-free frontmatter grammar with isolated state-matrix tests, actionable shared
section ownership, and acceptance phrased as final-state evidence. The task contract and plan were
narrowed accordingly. The only concurrent task then merged as `0032`, leaving no live shared owner;
this branch uses provisional decision number `0033` after integrating that accepted base.

The final plan-readiness pass found that `planned` RFC combinations and the completed-resolved
positive case were not explicitly covered, while acceptance could still pass on the old suite.
The RFC now contains the complete supported matrix, and acceptance requires its isolated positive
and negative cases plus the exact dependency-free recognizer.

The first full check after archival failed four link-test cases because Markdown discovery reads
Git's cached file list: before the move was staged, it returned the old active-task paths that no
longer existed on disk. Staging the archival rename made the index and filesystem describe the same
candidate change; the unchanged checks were then rerun.

## Outcome

Added optional `rfc.md` as the mutable, curated proposal artifact and narrowed `plan.md` to the
selected execution strategy. Decision `0033` owns the durable lifecycle and authority boundaries;
the README, portable task rules, and live questions now agree with it. A dependency-free convention
check enforces the exact RFC frontmatter and supported task/RFC/plan matrix with isolated positive
and negative cases. The shipped template, installed skill, and this repository's installed task
rules remain byte-identical.
