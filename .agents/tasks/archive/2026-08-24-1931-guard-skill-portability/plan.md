# Plan — guard shipped-skill portability

1. The Codex lead commits this resolved RFC, active task contract, curated context and plan. A
   separate committed handoff addresses `claude:lead` and names that contract revision.
2. The Claude lead dispatches `claude:executor` with exclusive ownership of `skills/AGENTS.md`,
   `tests/test_conventions.py`, the provisional decision record and decision index. The executor
   reports to its lead and does not answer the handoff or perform external actions.
3. Implement the author guidance and broad UTF-8 lexical detector exactly as `rfc.md` and
   `task.md` specify. Add forbidden and permitted regression cases. Do not change either existing
   shipped skill package; an unexpected existing violation returns `BLOCKED` rather than widening
   scope.
4. Record the durable decision and run the full acceptance suite. The Claude lead integrates the
   work, records Problems as they occur, writes the Outcome, archives the task and commits that
   stable implementation state.
5. At the archived implementation revision, run `pytest tests/`, recursive `pymarkdown`,
   `git diff --check`, regression checks, exact skill-package comparisons against the handoff
   revision, and the task acceptance/deletion/archive checks. Then obtain a fresh verifier verdict
   against that exact claim and revision.
6. Only `CONFIRMED` proceeds. After an initial `REFUTED`, allow at most two meaningful in-scope
   repair, full-check and fresh-verifier cycles; do not reverify an identical fingerprint. A third
   blocking verdict, unresolved `INCONCLUSIVE`, unavailable verification or unsafe integration
   returns `BLOCKED`.
7. The Claude lead answers every terminal path in a commit changing only the handoff entry.
   `COMPLETED` records the implementation revision and `CONFIRMED` evidence; `BLOCKED` records the
   evidence and resume point and performs no push or pull-request action.
8. After a `COMPLETED` return commit, rerun the full checks and produce final exact-head evidence
   against that return commit. Only then push the branch and open a non-draft pull request at that
   exact head for Human approval. Do not merge.

Dispatched contract and request commits remain ancestors of the final head. Do not rebase, amend,
force-push or otherwise rewrite them. If `origin/main` advances, integrate it only through
ancestry-preserving commits; resolve a provisional decision-number collision subsequently and
repeat every affected check and fresh verification gate.
