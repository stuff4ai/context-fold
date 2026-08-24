# Context — guard decision merge readiness

## References

- `decisions/0000-use-decision-records.md` — a record becomes project truth on merge; a branch is
  what makes an unmerged record a proposal.
- `decisions/0016-check-conventions-in-ci.md` — structural invariants are checked on pushes and
  pull requests.
- `decisions/0023-approve-the-final-state.md` — approval applies to the finished state rather than
  a promised post-review edit.
- `decisions/.adr-template.md` — currently lists `Proposed`, `Accepted`, and supersession as status
  choices without stating when drafting must end.
- `decisions/README.md` — derived decision index; its 0009 row currently disagrees with the record.
- `tests/test_conventions.py` — checks decision sections, numbering, and index membership, but not
  status grammar, merge readiness, or index-status agreement.
- `.agents/tasks/archive/2026-08-24-2124-define-agent-sublayer-model/task.md` — the task whose
  decision merged with stale proposed status.
- `.agents/tasks/archive/2026-08-24-2239-accept-sublayer-decision/task.md` — the status-only
  correction required after pull request 47 merged.

## Base state

The task starts from `main` at `596872b95f751305f55f9e3a6be57ee9c0807cf3`, after pull request
48 recorded decision 0041 as accepted. All actual decision records are now non-proposed, but the
suite would allow another `Proposed` record and does not compare index status with record status.
