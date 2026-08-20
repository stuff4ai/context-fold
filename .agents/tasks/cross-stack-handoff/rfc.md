---
status: draft
---

# RFC — where a cross-stack handoff lives, and what it looks like

## The proposal

A task package may carry `handoff.md`: an append-only record of requests between agent
stacks working the same repository, and the answers to them.

Each entry is one exchange. Frontmatter carries the address and state; the body carries the
request and, later, the return.

```markdown
---
id: 001
from: claude:lead
to: codex:plan-verifier
state: requested          # requested | returned
rev: d7e4bd4              # the revision the request refers to
returns: READY|REVISE     # the vocabulary expected back
---

## Request

**Objective** — one sentence: the outcome being judged.
**Scope** — what is in play.
**Non-goals** — what is deliberately excluded.
**Acceptance** — the check that would prove the outcome.
**Read first** — where to look, as paths from the repository root.

## Return
```

Four rules:

1. **Address.** `to:` names a stack and a role within it. Roles are the ones that stack
   already has; a handoff never invents one and never names a model, because the role
   definition already pins it.
2. **Inbox.** An entry with `state: requested` addressed to your stack is yours. Nothing
   else is.
3. **Return.** The receiving lead answers in the vocabulary `returns:` names, appends it
   under `## Return`, and sets `state: returned`. A review request is answered, not
   continued into implementation.
4. **Stop.** After writing a request, stop. Something outside the repository moves the work
   to the other stack; the file does not deliver itself.

`rev:` is what makes a return meaningful: a verdict is about a state, and without one
recorded the reader cannot tell what was judged. A sender whose tree is dirty says so in
the request rather than pretending a rev describes it.

## The question this RFC exists to settle

Where does the convention live: the portable managed rule block, or this project's suffix?

### Alternative A — portable block

Add `handoff.md` to the package contents in `templates/agents/tasks/AGENTS.md`, alongside
`task.md`, `context.md`, `rfc.md` and `plan.md`. Every installation receives it.

For: multi-stack work is a general problem, not one peculiar to this repository, and the
portable rules are where the package model is defined. `0011` permits it — the format names
no product, only opaque addresses and a vocabulary name.

Against: no evidence. `0006` opens by warning that task systems "tend toward ceremony: a
full set of artifacts per task, most of them empty, most of them abandoned within weeks."
A fifth artifact pushed into every installation on the day it was invented is that warning
being ignored. Updating the portable rules also means the three-way block parity procedure
and a change to every adopter, to ship a format nobody has used twice.

### Alternative B — project suffix

State the convention after the `agent-layer:end` marker in this repository's
`.agents/tasks/AGENTS.md`. `0035` created that boundary for additions exactly like this
one, and this project is its own first user.

For: small, reversible, and honest about the evidence. It exercises `0035`'s suffix for the
first time, which is itself worth learning from. Promotion stays available and becomes a
question with evidence behind it rather than a guess.

Against: an adopter gets nothing. The convention helps only this repository until it is
promoted, and a suffix is not something another project can discover.

### Alternative C — a decision record only

Record the convention in `decisions/` and change no rule file. Nothing instructs an agent
to look for a handoff.

Against: a decision nobody reads at the moment of the work is not a convention. The task
rules are where an agent finds out what a package may contain.

## Open questions

- Whether `returns:` should be closed. Closed is mechanically checkable, but binds the
  format to the verdicts two particular stacks happen to use now.
- Whether a request nobody answers needs an expiry, or whether a stale entry is visible
  enough to correct itself.
- Whether `from:` earns its place. The return says who answered; the request's author is
  usually evident from the branch. It is kept for now because an unanswered request with no
  author is hard to chase.
