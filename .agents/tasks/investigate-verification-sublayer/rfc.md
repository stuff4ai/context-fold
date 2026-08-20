---
status: draft
---

# RFC — investigate a verification sublayer

## Problem

Current verification is split between project tests, task acceptance and a prose final check. The
open questions propose scenarios, agent-system evals, observable run facts, executable gates and
replay, but those concerns do not automatically share one owner or storage lifecycle.

## Current proposal

Compare three boundaries before selecting structure:

- keep verification in project artifacts and task rules;
- add only an agent-facing summary and reference map of project verification entry points; or
- define a verification sublayer for portable agent-eval contracts and evidence references while
  leaving raw host execution data external or disposable.

A physical sublayer is selected only if investigation identifies information or behavior not
already owned by project tests, task packages or host adapters.

## Alternatives

- Make every task carry an executable verification manifest.
- Treat host telemetry and transcripts as the verification record.
- Put all product and agent checks into one repository-wide gate catalog.

## Open questions

- What is the smallest observable evidence that makes an agent run auditable?
- Which evidence must survive acceptance, and where can it live without becoming project truth?
- How are manual checks, commands and eval thresholds represented across hosts?
- Which semantic diagnostics have an authority strong enough to avoid opinionated warnings?
