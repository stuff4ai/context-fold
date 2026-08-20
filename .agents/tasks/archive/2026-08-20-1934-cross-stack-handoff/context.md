# Context — cross-stack handoff

## Project artifacts that matter

- `decisions/0006-task-package-model.md` — fixes what a package contains. A handoff record
  is an addition to that set, so this task either extends it or stays outside it.
- `decisions/0011-keep-the-model-vendor-neutral.md` — the canonical model names no product;
  product integration is an adapter over it and never the source of truth. This is the
  constraint that decides where the convention may name Claude Code and Codex.
- `decisions/0035-manage-portable-rules-as-replaceable-blocks.md` — an installation may
  append project instructions after the `agent-layer:end` marker. This is what makes a
  project-suffix-first approach available rather than a fork.
- `decisions/0012-build-the-methodology-before-the-tooling.md` — why no script ships with
  this.
- `decisions/0005-agents-layer-boundary.md` — the deletion test the handoff file must pass:
  it is coordination, not knowledge.
- `decisions/0025-run-tasks-in-parallel.md` and `.agents/tasks/AGENTS.md`'s *Working
  alongside other tasks* — scope is declared by section. A second stack holding the same
  package is the same problem one directory down.
- `decisions/0030-add-a-claude-code-adapter.md` — establishes that a root `CLAUDE.md`
  containing `@AGENTS.md` gives a Claude Code session this repository's `AGENTS.md`. This is
  why no change under `~/.claude` is needed for a Claude session to find a handoff.
- `OPEN-QUESTIONS.md` — where the deferred promotion question is recorded.

## Task-local facts

The two stacks this was designed against, as installed on the author's machine at the time
of writing. Neither is part of this repository, and nothing here depends on their contents
beyond the shape described below.

- Claude Code runs pilotfish v1.3.10; its roles are files in `~/.claude/agents/`:
  `scout`, `Explore`, `plan-verifier`, `security-reviewer`, `mech-executor`, `executor`,
  `verifier`, `security-executor`.
- Codex CLI runs pilotfish-codex v1.7.1; its roles are files in `~/.codex/agents/`:
  the same set without `Explore`.
- Both pin a model per role in the role definition, so a handoff addressing a role never
  names a model.
- Both emit the same verdict vocabularies: `READY`/`REVISE` before approval, and
  `CONFIRMED`/`REFUTED`/`INCONCLUSIVE` after implementation.
- Both forbid a named role from delegating onward; only the session's own lead dispatches.

The last two are what the convention rests on. The verdict vocabularies mean a handoff can
name what it expects back without inventing a schema, and the delegation rule means a
handoff needs no access control: only a lead reads or writes one, because only a lead is
permitted to ask for work in the first place.

Codex reads a repository's `AGENTS.md` natively; Claude Code reaches the same file through
the adapter in `0030`. Both stacks therefore find the convention without either being
configured for it.

## Assumptions

- That the two stacks work the same checkout, one at a time. Concurrent stacks in separate
  worktrees are the same problem `.agents/tasks/AGENTS.md` already handles for concurrent
  tasks, and are not tested here.
- That a git rev is enough to identify what a request referred to. A dirty working tree at
  request time would break that, which is why the convention requires the sender to say so.

## Open questions

- Whether `returns:` should be a closed vocabulary or free text. Closed is checkable but
  binds the convention to the verdicts two particular stacks happen to use today.
- Whether a handoff addressed to a stack that never answers needs an expiry, or whether a
  stale request is simply visible and therefore self-correcting.

## Not relevant

- `~/GitHub/alexengrig/personal-agent-os` — solves the general cross-provider problem with
  provider-neutral role contracts and generated orchestrator profiles. Deliberately not
  used: this task starts from the two stacks as installed rather than from a role taxonomy.
- CLI orchestrators evaluated and set aside: AWS Labs CAO, herdr, `pal-mcp-server`'s clink,
  and the built-in MCP server modes of both CLIs. All provide a live channel, which is the
  thing this task is choosing not to build on.
