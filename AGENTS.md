# AGENTS.md

**context-fold** is a methodology for organizing repository context so humans and agents can
work on the same project coherently over time. See [README.md](README.md).

This project is its own first user: the conventions it defines are applied here before they
are recommended anywhere else.

## Project rules

- Keep changes small and reviewable.
- Prefer plain files and Git-friendly workflows.
- Do not introduce unrelated changes.
- Do not push directly to `main`.
- Do not merge a pull request until a human has approved it. After that, merging is yours to do.
- Update documentation when behavior or conventions change.
- After changing `skills/ctxfold-init/templates/`, reinstall `.agents/` from it before finishing
  — copy the `AGENTS.md` files only, never `INDEX.md`, which is this installation's own.

## Decisions

Durable project decisions are recorded in [`decisions/`](decisions/). Check them before
proposing a change, and add a record when a change introduces or replaces one.

Accepted records are immutable apart from their `Status` field. Supersede them with a new
record; do not rewrite them and do not renumber.

## Agent layer

Agent operating context lives in `.agents/` — how work is organized, tracked, and finished
here.

Read [`.agents/AGENTS.md`](.agents/AGENTS.md) before starting work.

## Change workflow

Use GitHub Flow:

1. Create a short-lived branch from `main`, named `<type>/<kebab-case-topic>` —
   `feat/task-index`, `docs/decision-threshold`, `fix/index-drift`.
2. Make a focused change.
3. Open a pull request. Its description becomes the commit message on `main`, so write it as
   a record of the change — not as a note to the reviewer, and with nothing that stops being
   true once merged.
4. Wait for a human to approve it.
5. Squash merge.

Use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) for commit
messages. A branch's `<type>` comes from the same set of types as its commits.

Sign off every commit with `git commit -s` so it carries a `Signed-off-by` trailer.

When an agent contributes to a commit, it adds a `Co-authored-by` trailer naming itself and
the model it ran as.
