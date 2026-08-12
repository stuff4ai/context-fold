# Attribute agent contributions as co-authors

## Status

Accepted

## Context

Agents write substantial parts of the changes in this repository.

[Sign-off](0003-sign-off-commits.md) records who takes responsibility for submitting a change,
but says nothing about who wrote it. Without a second signal, history shows only the human,
and the agent's involvement disappears — which is the same failure this project exists to
address, applied to the commit log.

This project studies how agent-assisted development actually works. Its own history is
evidence, and evidence that omits which work was agent-assisted is less useful.

## Decision

When an agent contributes to a commit, the commit carries a `Co-authored-by` trailer naming
that agent and the model it ran as:

```
Signed-off-by: A Human <human@example.com>
Co-authored-by: Claude Opus 5 <noreply@anthropic.com>
```

The address is the one the agent's vendor publishes for this purpose.

Authorship and sign-off remain the human's. Co-authorship is attribution, not responsibility.

Agents add the trailer themselves as part of committing.

## Consequences

History shows which changes were agent-assisted, and forges that understand the trailer
display the agent alongside the human.

The project accumulates a factual record of agent involvement over time, usable as evidence
about its own methodology.

The trailer is self-reported and nothing enforces it. A missing trailer is indistinguishable
from work a human did alone.

Attribution is not verification. This says nothing about whether a commit is cryptographically
signed, which remains undecided — see [0003](0003-sign-off-commits.md).
