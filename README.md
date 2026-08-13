# context-fold

> 🗂️ Fold your repo context for humans and agents.

A repository should contain more than code and documentation. It should carry an explicit
operating context that says how to understand the project, how work moves through it, and
where durable knowledge belongs — so that humans and agents can work on the same project
coherently over time.

The name is the metaphor: repository context is too large to hold at once, so it is folded into
structures that can be opened where needed and left closed everywhere else. Short form
`ctxfold`.

## The problem

Agents rarely fail because a repository contains too little information. They fail because
project knowledge is unstructured, work history is disconnected from durable knowledge,
mistakes disappear into transcripts instead of becoming lessons, and every new agent
rediscovers how the project works from scratch.

## The loop

Work produces problems. Problems become lessons. Lessons change the context the next agent
reads.

Friction is written down while it happens — what was assumed, what was actually true — because
recalling it afterwards produces a tidy account of a process that felt smooth in retrospect. A
single instance is bad luck; the same problem across several tasks is evidence, and evidence is
what justifies changing a rule.

Nothing promotes itself. A pattern becomes a rule only through a reviewed change, and a person
decides which patterns matter. This is the part that makes a repository get better at being
worked on rather than merely bigger.

## The principle

Two layers, with a hard boundary between them.

**The project layer** holds what the project knows: the code, its tests, its documentation,
and its decision records. This is durable, human-owned truth.

**The agent layer** (`.agents/`) holds how agents operate: navigation, task coordination,
lifecycle state, working context. It is scaffolding, not knowledge.

The boundary is enforced by a test anyone can apply:

> If humans need this information too, it does not belong only in `.agents/`.

Remove `.agents/` and read what remains. The test fails if knowledge was lost, not if a
pointer to the layer dangles — removing the layer is an ordinary change, and what pointed at
it is updated alongside. A layer that fails has quietly become a second, drifting source of
truth.

## Tasks

Work is organized into task packages under `.agents/tasks/{slug}/`:

| File | Purpose |
| --- | --- |
| `task.md` | The contract — objective, scope, acceptance, and the problems hit along the way |
| `context.md` | A curated map of what matters for this task, by reference |
| `plan.md` | Execution strategy, when the task is large enough to need one |

Tasks are named by descriptive slug rather than ticket number, so paths stay meaningful and
no separate numbering system is required.

A task is not complete when the coding is done. It is complete when acceptance is satisfied,
durable outcomes have been folded into the project layer, review has happened, and the
repository is in a coherent accepted state. Only then is it archived — inside the pull
request, so the merge commit carries both the work and the record of the work.

## Decisions

Durable project decisions are recorded as decision records. They cover any significant
decision, not only architectural ones: workflow, conventions, tooling, and structure.
Accepted records are immutable apart from their `Status` field — a decision is replaced by a
new record that supersedes it, never by rewriting the old one.

This repository keeps them in [`decisions/`](decisions/). That location is a choice, not a
requirement.

## Adopting it

Everything a repository needs is in
[`skills/ctxfold-init/`](skills/ctxfold-init/): the procedure in
[`ADOPTING.md`](skills/ctxfold-init/ADOPTING.md), the files it installs, and a skill that carries
out the adoption for an agent that supports one.

## Status

v0. Methodology and repository conventions, applied to this repository first.

Nothing produces anything. Task packages, the index, and the archive are maintained by hand, by
decision rather than by omission — see
[0012](decisions/0012-build-the-methodology-before-the-tooling.md). Checks that verify those
conventions run in CI ([0016](decisions/0016-check-conventions-in-ci.md)).

What is deliberately unbuilt, and what using it has shown to be unresolved, is in
[OPEN-QUESTIONS.md](OPEN-QUESTIONS.md).

## License

Apache-2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
