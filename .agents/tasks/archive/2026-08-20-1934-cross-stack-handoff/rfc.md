---
status: resolved
---

# RFC — where a cross-stack handoff lives, and what it looks like

## The proposal

A task package may carry `handoff.md`: a record of requests between agent stacks working the
same repository, and the answers to them. An entry is not rewritten once dispatched — its
request text is fixed then, and answering it changes only `state:` and fills `### Return`. A
fact that turns out to be wrong is corrected by adding to the entry, marked as added
afterwards.

Each entry is one exchange, opening with a fenced `yaml` block and then two sections. The
header is fenced rather than document frontmatter because the file holds many entries and a
Markdown document has only one frontmatter block.

````markdown
## 001

```yaml
id: 001
from: claude:lead
to: codex:plan-verifier
state: requested          # requested | returned
rev: d7e4bd4              # the revision the request refers to
returns: READY|REVISE     # the vocabulary expected back
```

### Request

**Objective** — one sentence: the outcome being judged.
**Scope** — what is in play.
**Non-goals** — what is deliberately excluded.
**Acceptance** — the check that would prove the outcome.
**Read first** — where to look, as paths from the repository root.

### Return
````

Five rules:

1. **Address.** `to:` names a stack and a role within it. Roles are the ones that stack
   already has; a handoff never invents one and never names a model, because the role
   definition already pins it.
2. **Inbox.** An entry with `state: requested` addressed to your stack is yours. Nothing
   else is.
3. **Return.** The receiving lead answers in the vocabulary `returns:` names, appends it
   under `### Return`, and sets `state: returned`. A review request is answered, not
   continued into implementation.
4. **Commit the request, then dispatch it.** `rev:` names the commit under review. The
   entry is committed too, necessarily in a later commit, since an entry cannot name the
   commit containing it. Where the tree at dispatch differs from `rev:` in anything but the
   entry, the request says what and why.
5. **Stop.** After writing a request, stop. Something outside the repository moves the work
   to the other stack; the file does not deliver itself.

## The question this RFC exists to settle

Where does the convention live: the portable managed rule block, or this project's suffix?

### Alternative A — portable block

Add `handoff.md` to the package contents in `templates/agents/tasks/AGENTS.md`, alongside
`task.md`, `context.md`, `rfc.md` and `plan.md`. Every installation receives it.

For: multi-stack work is a general problem, not one peculiar to this repository, and the
portable rules are where the package model is defined. `0011` permits it — the format names
no product, only opaque addresses and a vocabulary name.

Against: `0012` commits this project to building the methodology before the tooling that
would hide its weaknesses, and to being its own first user. A rule distributed to every
adopter before it has been followed once here is that commitment inverted — the portable
rules would be describing a practice rather than recording one.

The objection is about distributing an unexercised rule, not about ceremony. `handoff.md`
is optional, exactly as `rfc.md` and `plan.md` already are, so promoting it would not put a
fifth file in every package or oblige any task to carry one. `0006`'s warning about a full
set of artifacts per task is not the argument here and does not support one.

The practical cost is smaller than the principle: promotion means the three-way block parity
procedure and a change reaching every adopter, to ship a format nobody has yet used twice.

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

## What would reopen Alternative A

The evidence missing today is use: one exchange, run by this task against itself, with the
Claude lead invoking the Codex stack directly rather than a person carrying the work across.
That is enough to show the format parses and a verdict comes back. It is not enough to show
the convention survives the situations a portable rule would have to cover.

Any one of these is a reason to reconsider:

- **Three tasks carry a handoff without the format changing.** Repeated use with a stable
  shape is the difference between a convention and a draft.
- **A second repository wants it.** A project that has adopted the layer and asks for the
  same convention shows the need is not local, which is the one thing a suffix cannot
  demonstrate.
- **An exchange crosses a person rather than a subprocess.** Rule 5 assumes the asking stack
  stops and something outside moves the work. Until that has actually happened, the rule most
  likely to be wrong is the one least tested.
- **Two stacks hold the same package concurrently.** The portable rules already say how
  concurrent tasks share files by section. If handoffs need the same treatment one directory
  down, that belongs in the portable rules rather than beside them.

Any one of these is also a reason the format might need to change first. Reconsidering means
reopening this RFC, not promoting the current text.

Against promotion, and unchanged by any of the above: if after several tasks the file is
mostly empty or mostly one stack talking to itself, the convention did not earn a suffix
either, let alone a portable rule.

## Open questions

Three details of the entry format are undecided — whether `returns:` should be a closed
vocabulary, whether an unanswered request needs an expiry, and whether `from:` earns its
place. They outlive this task, so they are recorded in `OPEN-QUESTIONS.md` rather than here.

## Resolution

**Alternative B.** The convention is stated as this repository's project suffix, after the
`agent-layer:end` marker in `.agents/tasks/AGENTS.md`. The portable managed rule block is
unchanged, so all three copies of it stay byte-identical.

The rules are written to name a stack and a role rather than any product, so that which
stacks exist stays a fact about an installation while the shape of an address does not.
That is `0011`'s split applied inside a suffix, and it is what makes promotion later a move
rather than a rewrite.

Promotion is deferred, not refused, on the grounds in *What would reopen Alternative A*
above. The question is recorded in `OPEN-QUESTIONS.md` so it stays visible after this
package is archived.

This resolution was reviewed before adoption by `codex:plan-verifier`, which returned
`REVISE` against the two arguments this section now rests on; see `handoff.md` entry 001.
The reasoning above is what replaced them.
