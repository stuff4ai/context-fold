# Sign off every commit

## Status

Accepted

## Context

This project is Apache-2.0 licensed and accepts contributions. Contribution provenance —
who asserts the right to submit a change — is worth recording in the commit itself rather
than in a separate agreement.

The [Developer Certificate of Origin](https://developercertificate.org/) is the established,
lightweight form of that assertion: a `Signed-off-by` trailer stating that the contributor has
the right to submit the work under the project's license.

This matters more, not less, as agents write commits. Work produced by an agent is submitted
by a person, and the trailer records who that person is.

## Decision

Every commit carries a `Signed-off-by` trailer, added with `git commit -s`.

The trailer records the human accountable for submitting the change, whoever or whatever
produced its content.

## Consequences

Provenance is recorded in history, not in a side channel, and travels with the commit.

Contributors must configure `user.name` and `user.email`, and remember `-s`. Forgetting it
requires amending the commit before merge.

Sign-off is an assertion, not an identity proof. It says who claims responsibility; it does
not cryptographically verify who authored the commit. Commit signing is a separate question
and is not decided here.
