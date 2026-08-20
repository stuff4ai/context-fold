---
status: draft
---

# RFC — extend initialization with project assessment

## Problem

Installing agent operating rules does not make project knowledge discoverable or complete. A new
agent may still lack an authoritative path to intent, decisions, documentation, tests or reusable
procedures. Automatically creating those artifacts would exceed adoption's authority and impose a
project layout without evidence.

## Current proposal

After installing the agent layer, inspect five project capabilities: intent and requirements,
decisions and rationale, documentation and knowledge, tests and verification, and agent skills.
Classify each as established, partial, absent, ambiguous or not applicable. Record established
sources in the proposed context map. Create a separate planned task for each applicable partial,
absent or ambiguous capability, carrying repository evidence and non-binding recommendations.

The user resolves each task by choosing the project's structure, improving an existing convention,
or deciding that the capability is not warranted. Cancellation still folds durable findings out;
postponement leaves the task planned. Recommendations may offer paths and templates as examples but
do not choose them.

## Alternatives

- Install only the agent layer and leave all project preparation outside context-fold.
- Produce a report but create no task packages.
- Create a standard project structure automatically during adoption.
- Ask about every capability before creating any task.

## Open questions

- Does project assessment belong in task zero or after task zero establishes the layer?
- How does repeat adoption avoid reopening a gap a project already declined deliberately?
- Can the assessment remain vendor-neutral while evaluating agent skills?
- Which future evidence would justify adding operations, security, data, release or integrations?
