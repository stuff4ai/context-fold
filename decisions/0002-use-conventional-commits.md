# Use Conventional Commits

## Status

Accepted

## Context

Commit history is the one record of a project that is never rewritten and always present. It
is also the record most likely to be written carelessly, because the cost of a vague message
falls on whoever reads it months later.

Agents write commits, and they write whatever the surrounding history suggests. An
inconsistent history produces more inconsistency; a mechanical convention produces conformity
without needing judgment.

A structured format also makes history machine-readable, which keeps later automation —
changelog generation, release tooling — available without a migration.

## Decision

We will use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) for commit
messages: `<type>(<optional scope>): <description>`.

The same set of types names branches, so a branch and the commits on it agree.

## Consequences

History can be scanned by type, and the nature of a change is visible without opening it.

Changelog and release tooling remain possible later without rewriting history.

The convention constrains phrasing, and some changes do not map cleanly onto a single type.
Choosing the closest type is better than inventing new ones.

The format is not enforced by tooling. It holds by convention, which means it will drift
unless review notices.
