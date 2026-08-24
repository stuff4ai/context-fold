---
status: completed
objective: >-
  Decide whether `.agents/` should become a governed set of agent sublayers with a goal-oriented
  entry point and a contract for each recognized sublayer.
---

# Define the agent sublayer model

## Why

The current model deliberately treats tasks, skills and worktrees as three things with different
owners rather than three layers. The proposed model would instead let context-fold govern the
namespace and each sublayer boundary without necessarily owning every file inside it. That change
needs an explicit ownership model before any new sublayer is added.

## Scope

- Resolve the RFC and define the recognized-sublayer contract and routing model.
- Update `README.md`, the portable `.agents/AGENTS.md` template, and the installed managed block.
- Add the minimal portable `skills/AGENTS.md` contract and extend adoption/update guidance to five
  managed targets.
- Add the provisional decision record, reconcile affected decision statuses and index entries, and
  update dependent planned-task contracts.
- Extend convention checks to cover the fifth target without classifying nested skill-package files.
- Reinstall the complete `ctxfold-init` skill and verify shipped, installed-skill, template, and
  active managed-block parity.
- Exercise fresh and repeat adoption against the disposable ETU Forms fixture, preserving a custom
  suffix and an unknown extension, then restore its exact clean baseline.

## Out of scope

- Detailed skills authority, provenance, discovery, host projection, package format, or lifecycle.
- Designing or creating the candidate context or verification sublayers.
- Project-layer assessment during adoption.
- Implementing workflows, MCP/tool layers, host adapters or a runtime harness.

## Acceptance

1. The resolved RFC defines a recognized sublayer as a direct functional area with a managed
   `AGENTS.md` contract and specifies purpose/routing, authority boundary, contract owner, content
   owner, lifecycle/deletion, suffix customization, and unknown-extension behavior.
2. The model classifies `tasks/`, `skills/`, and `worktrees/`, leaves `context/` and `verification/`
   as candidates, preserves unknown direct children, and keeps `tasks/archive/` internal.
3. The resolution preserves the project-truth deletion test and identifies every accepted decision
   it keeps, narrows or supersedes.
4. `.agents/AGENTS.md` is a goal-oriented router and the skills contract is minimal and portable.
5. Adoption guidance, the five-target checks, and source/installed/active parity verification are
   complete.
6. Dependent planned tasks are reconciled with the selected model before this task completes.
7. A paired ETU Forms scenario proves fresh adoption, repeat-update suffix preservation, unknown
   extension preservation, and exact restoration of the fixture without creating project documents.

## Outcome

The resolved RFC and proposed decision `decisions/0041-define-governed-agent-sublayers.md` establish
the shared `.agents/` namespace, the recognized `tasks/`, `skills/`, and `worktrees/` contracts,
goal-oriented routing, independently owned contents, and preservation of unknown extensions.
`README.md`, `OPEN-QUESTIONS.md`, affected decision statuses, and the dependent planned tasks now
agree with that model.

The distribution adds the minimal portable `skills/AGENTS.md` contract and installs, preflights,
updates, and checks five managed targets. The complete shipped `ctxfold-init` package matches its
installed copy, and every source, installed-template, and active managed block is identical while
project suffixes remain outside the replaceable block.

At ETU Forms head `d0f902a`, a paired disposable scenario installed the five contracts, task zero,
root pointer, and ignore rules; replaced a valid stale skills block; preserved the project suffix
and unknown-extension hashes; created no PRD or architecture artifact; and restored the checkout to
the same clean head with the original `.gitignore` hash. The final repository state passes all 636
tests, the configured recursive Markdown scan, `git diff --check`, and parity checks.

## Problems

- The Pilotfish skill path in the bootstrap did not match the installed cache layout; the package
  was found under its nested `pilotfish-codex/1.7.1/` directory before implementation continued.
- `rtk` does not accept shell-loop syntax or some `find` flags as a transparent prefix. Inspection
  used simpler prefixed commands and explicit paths instead, preserving the required command
  wrapper without changing repository state.
- A multi-file patch used one main-checkout path by typo and touched `decisions/0026...` outside
  this worktree. Status checks caught the drift before any other worktree action; the exact hunk
  was restored and the main checkout is clean.
- The declared development tools were absent from the base interpreter, so focused and full checks
  were initially inconclusive. A temporary `/tmp` virtual environment installed
  `requirements-dev.txt`; both test and lint commands then completed successfully.
- The existing portable worktrees contract explicitly excluded itself from the agent layer, which
  contradicted the selected recognized-contract model. Its source, installed copy, and active block
  were updated together before final parity verification.
- Re-running the same installed skill would leave every managed block unchanged and would not
  exercise suffix-preserving replacement. The ETU Forms fixture therefore changed one line inside
  an otherwise valid skills block to represent an older installation; repeat adoption restored the
  current block while the suffix and unknown-extension hashes stayed unchanged.
- The first Markdown scan omitted `.pymarkdown.json` and reported the tool's default line-length
  policy across existing documents. Re-running the exact CI command with the repository config and
  `--respect-gitignore` passed.
- Fresh verification found that decision `0017` still described adoption as copying three portable
  rule files. Its Status and the resolved RFC/decision impact lists were updated to include the fifth
  skills contract before the exact-head checks were repeated.
- A second fresh verifier found the same missing reconciliation in decisions `0021` and `0040`:
  their current Status text still described four managed files and denied that the installed skills
  guidance was a sublayer contract. Both statuses and the RFC/decision impact lists were corrected.
- A follow-up search placed Markdown backticks inside a double-quoted shell pattern, so the shell
  attempted to execute the quoted path. It changed nothing; later searches used literal-safe quoting.
- A final decision-corpus sweep found that `0025` never recorded `0032` reversing its old claim that
  `worktrees/AGENTS.md` was unshipped and unchecked. Its Status now records that earlier narrowing;
  `0041`'s separate recognized-sublayer narrowing remains unchanged.

## Approval

Human.
