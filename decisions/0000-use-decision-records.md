# Use decision records

## Status

Accepted

## Context

The project needs a simple way to record important choices so humans and AI agents can
understand why the project works the way it does.

Without such a record, decisions live in conversations and pull request threads. Agents
rediscover settled questions, and reopen them differently each time.

This project's own design decisions were made in conversation and existed nowhere in the
repository. Recording that this repository uses decision records is the first of them.

## Decision

We will record important project decisions as [decision records](https://adr.github.io/),
stored as Markdown files in `decisions/` and numbered with a four-digit prefix.

We use the Nygard template: Status, Context, Decision, Consequences. The template lives in
`decisions/.adr-template.md` and the index in `decisions/README.md`.

The scope is any durable project decision — workflow, conventions, tooling, structure — not
only architectural ones.

A decision record becomes project truth when it is merged into `main`. A record proposed on a
branch is a proposal.

Accepted records are immutable history, with one exception: `Status`. It is the record's
current standing rather than part of what was decided, and it is the only field that may
change after acceptance.

To replace a record, add a new one that supersedes it and set the old record's `Status` to
point at the replacement. Context, Decision, and Consequences are never rewritten, and records
are never renumbered.

## Consequences

Important decisions become easy to find, review, and change through Git.

Agents have a durable source of project context before proposing changes.

Writing records adds a small amount of process, so records stay brief and focused. Decisions
that are not durable do not need one.
