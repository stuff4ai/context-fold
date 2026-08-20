# Context — categorize open questions

## Base state

`OPEN-QUESTIONS.md` contains 59 live items: 12 under Deferred capability, 35 under Open questions
about the model, 10 under Gaps in the current rules, and 2 under Recurring patterns. Its final
section also records two questions the project explicitly will not answer.

The categorization before-state is commit `793e3072e92c4f82f8c69badd907c3de90322094` and
`OPEN-QUESTIONS.md` blob `3017b1b7472fe7438b0f55d59bfb9a4fc04d1595`: 57 live item blocks will receive a topical
destination, 2 recurring-pattern blocks remain flat, and the 2 non-answer blocks remain flat and
outside the 59-item live count.

No other task package is active. The preceding `add-task-rfc` task was accepted and archived, so
this task can use a draft RFC while discussing taxonomy and create no plan until its direction is
resolved.

## References

- `OPEN-QUESTIONS.md` — the live project-owned source being categorized; it remains authoritative
  throughout this task.
- `decisions/0010-record-open-questions-in-project-layer.md` — keeps live questions in the project
  layer and forbids turning the document into a roadmap.
- `decisions/0013-improve-context-from-the-work.md` — requires evidence and human judgment before a
  recurring problem becomes a rule.
- `decisions/0022-route-findings-without-an-owning-task.md` — defines when a finding calls for a
  planned investigation, decision, or change task.
- `decisions/0033-separate-rfc-discussion-from-execution-planning.md` — gives this task a mutable RFC
  and prevents creating a plan before direction is resolved.
- `.agents/tasks/archive/2026-08-18-2250-park-agent-native-sdlc-questions/task.md` — provenance for
  the large model-question expansion without treating that exploratory proposal as accepted.
- `.agents/tasks/archive/2026-08-19-1928-reconcile-live-questions/task.md` — the most recent
  reconciliation of the live list against accepted decisions and shipped behavior.

## Not relevant

- Archive retrieval or automatic task-index generation are questions in the list, not mechanisms
  this categorization task will build.
- The order in which future tasks should execute is not being decided here.
