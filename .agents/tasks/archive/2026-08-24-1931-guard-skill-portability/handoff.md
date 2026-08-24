# Cross-stack handoff

## 001

```yaml
id: 001
from: codex:lead
to: claude:lead
state: requested
rev: c62302558499e96e8fbd690c11795e55bb661ebf
returns: COMPLETED|BLOCKED
```

### Request

**Objective** — Implement the resolved shipped-skill portability contract at `rev`, finish and
archive its task, obtain fresh verification, and open the finished pull request for Human approval.

**Scope** — Dispatch `claude:executor` with exclusive implementation ownership of
`skills/AGENTS.md`, `tests/test_conventions.py`, the provisional
`decisions/0040-guard-shipped-skill-portability.md`, and `decisions/README.md`. Implement every
criterion in `.agents/tasks/guard-skill-portability/task.md` and the selected direction in its
resolved `rfc.md`. The executor reports its result to this Claude lead; it does not answer this
entry, finalize the task, or perform external actions.

**Lead ownership** — The Claude lead alone integrates and commits implementation, records task
Problems, writes the Outcome, archives the package, dispatches the fresh verifier, changes and
commits this entry's return, pushes the branch, and opens the pull request. Work in the existing
`test/guard-skill-portability` branch and task worktree. Codex ownership ended with this request.

**Non-goals** — Do not redesign skill or `.agents/skills/` ownership, define a skills sublayer,
add suppressions or an allowlist, modify either current shipped skill package, merge the pull
request, or make unrelated changes. If the broad detector unexpectedly finds a current violation,
return `BLOCKED` rather than editing the package or widening scope.

**Implementation acceptance** — Add the project-owned author rule and broad UTF-8 lexical check,
the prohibited and allowed regression cases, and the provisional decision exactly as the task
acceptance requires. Prove `skills/ctxfold-init/` and `skills/ctxfold-tasks/` have no diff from
`rev`. Run the full `pytest tests/` suite, recursive `pymarkdown`, `git diff --check`, regression
checks, and readable acceptance/deletion/archive evidence at the stable archived implementation
revision.

**Verification** — Dispatch a fresh verifier against the exact archived implementation revision
and every task acceptance criterion. Only `CONFIRMED` may proceed. After an initial `REFUTED`, use
at most two meaningful in-scope repair, full-check and fresh-verifier cycles; never reverify an
identical fingerprint. A third blocking verdict, unresolved `INCONCLUSIVE`, unavailable verifier,
unexpected skill violation, or unsafe integration returns `BLOCKED`.

**History and integration** — Keep `rev` and the later commit containing this request as ancestors
of every result. Do not rebase, amend, force-push or otherwise rewrite them. If `origin/main`
advances, integrate it only through ancestry-preserving commits. Resolve any provisional
decision-number collision subsequently, then repeat all affected checks and verification.

**Return and delivery** — Every terminal outcome changes only `state:` and `### Return` in a
return-only commit written by the Claude lead. `COMPLETED` records the archived implementation
revision and `CONFIRMED` evidence. `BLOCKED` records the blocker, evidence and exact resume point,
then stops locally without push or pull request. After a `COMPLETED` return commit, rerun full
pytest, recursive Markdown lint, `git diff --check`, and the final exact-head check against that
return commit. Only then push and open a non-draft pull request whose initial head is exactly that
checked commit. Request Human approval and do not merge. Any later change invalidates these gates.

### Return

Pending.
