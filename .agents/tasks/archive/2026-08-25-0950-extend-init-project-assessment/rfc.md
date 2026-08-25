---
status: resolved
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

## Resolution

Do not build project assessment now. `ctxfold-init` gains no capability catalog, evidence
classification, or generated-task mechanism. Task zero's existing base-state discovery —
recording what conventions a repository already has and where its durable knowledge lives, in
`context.md` prose — remains the only project-readiness step adoption performs.

`decisions/0044-defer-the-context-sublayer.md`, resolved immediately before this task, already
supplies the applicable bar: `.agents/context/` "should appear only once it demonstrably exists,
so the layer does not become a second documentation tree by default"
(`decisions/0005-agents-layer-boundary.md`), and recorded friction that is a
discipline defect rather than a demonstrated failure to find authoritative sources does not clear
it. The evidence available for this task is thinner still: context-fold has been adopted exactly
once, on itself, so there is no track record — inside this repository or reported from
elsewhere — of an adopter missing an authoritative source for intent, decisions, documentation,
verification, or skills because adoption did not flag its absence.

The current proposal's own open questions above are the shape that evidence gap takes in design
terms. "Which evidence is sufficient to call a capability established" and "who decides an absent
capability is not applicable" (`context.md`) have no answer that isn't invented, because nothing
has yet told this project what a real gap looks like or what an adopter actually needs
recommended.
Building the classification scheme, the non-duplication rule across repeat adoptions, and the
task-generation mechanism first and hoping the design questions answer themselves in use is the
anticipated-need infrastructure `decisions/0005-agents-layer-boundary.md` and
`decisions/0044-defer-the-context-sublayer.md` both decline to build. It also risks
exactly the ceremony this task's own `context.md` flags — "how many planned tasks may adoption
create before its guidance becomes ceremony" — before a single real adopter has shown the
ceremony is worth paying for.

This is a narrower outcome than the current proposal, not a rejection of the underlying concern:
`decisions/0005-agents-layer-boundary.md` is right that context-fold cannot assume
project intent, decisions, documentation, verification, or skills are discoverable, and a future
assessment step may still be the right answer. It is not the right answer to build yet, on the
evidence this repository currently has.

`OPEN-QUESTIONS.md`'s "Should adoption assess project-layer readiness?" item is replaced with
named reopening conditions, the same treatment `0044` gave the context-sublayer question, so the
question does not stay open indefinitely on the same footing.

Of the alternatives considered, this comes closest to "install only the agent layer and leave all
project preparation outside context-fold," but stops short of closing the door: the reopening
conditions below keep the concern recorded rather than discarded.
