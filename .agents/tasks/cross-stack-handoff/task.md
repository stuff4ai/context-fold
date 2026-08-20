# Record a cross-stack handoff in the task package

## Status

active

## Objective

Let two agent stacks working the same repository coordinate through a file in the task
package instead of through a live channel, and prove it with a real exchange.

## Why

A repository is increasingly worked by more than one agent stack — here, Claude Code and
Codex CLI, each running its own orchestration policy with its own named roles. The task
package already carries the contract, the context and the plan, but nothing says how one
stack asks another for something and gets an answer back.

Without a place for that exchange, it happens in two transcripts that neither the other
stack nor a reviewer can see. The request, the state it referred to, and the verdict all
vanish. A repository that keeps the record of its work loses precisely the part where two
agents disagreed.

Doing this by artifact rather than by message is the point, not a limitation. The file is
readable in the pull request, it survives both sessions, and it needs nothing running.

## Scope

- `.agents/tasks/cross-stack-handoff/` — this package, including its RFC.
- `decisions/` — one new record, and its row in `decisions/README.md`.
- `.agents/tasks/AGENTS.md` — the project suffix after the `agent-layer:end` marker only.
  The managed block is out of scope; see Out of scope.
- `README.md` — a short pointer, if the RFC resolves that adopters need one.

## Out of scope

- **The portable managed rule block.** Whether `handoff.md` becomes a portable artifact in
  every installation is deliberately deferred until this convention has been used. `0035`
  provides the project suffix for exactly this case. The promotion question is recorded in
  `OPEN-QUESTIONS.md` rather than answered here.
- **Tooling.** No script, no plugin, no daemon. `0012` applies: the methodology is built
  before the tooling that would hide its weaknesses.
- **Changing either stack's own configuration.** Nothing under `~/.claude` or `~/.codex` is
  modified. Both role rosters stay exactly as their installers wrote them.
- **A general multi-agent model.** This records one convention with one worked example, not
  a taxonomy of agent stacks, roles, or capability tiers.

## Acceptance

1. `decisions/` carries a record stating the handoff convention, its rules, and why the
   portable block was not changed; `decisions/README.md` lists it.
2. `.agents/tasks/AGENTS.md` carries the convention as a project suffix. Its managed block
   is byte-identical to `.agents/skills/ctxfold-init/templates/agents/tasks/AGENTS.md` and
   to `skills/ctxfold-init/templates/agents/tasks/AGENTS.md`, verifiable by comparing the
   bytes between the `agent-layer` markers in all three.
3. This package contains a `handoff.md` recording at least one completed exchange with a
   second agent stack: a request in one stack's hand, a return in the other's, both states
   `returned`, naming the git rev the request referred to.
4. That exchange was real. The return records which stack and which role produced it, and
   the verdict is one this task did not write for it.
5. The convention's rules are stated somewhere a reader who was not present can apply them
   to a new task without reading this package.
6. `.agents/tasks/AGENTS.md`'s suffix does not contradict its managed block, and states no
   rule that only makes sense for this repository.

## Approval

Human. The RFC leaves a direction for the reviewer to choose rather than a claim to check.

## Problems
