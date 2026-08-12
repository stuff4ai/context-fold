# Open questions

What this project has deliberately not decided, and what using it has shown to be unresolved.

Nothing here is a plan or a schedule. Items are removed when they become decisions in
[`decisions/`](decisions/), or when they turn out not to matter.

Archived task packages contain questions that were open while those tasks ran. Those are
historical records. This document is the live list.

## Deferred capability

Chosen not to build yet, so that the methodology can be judged on its own before tooling
hides its weaknesses.

- **A CLI.** Everything is plain files and Git. Whether a tool is needed, and for what, should
  come from friction rather than from the assumption that a product needs a binary.
- **Skills and workflows.** `.agents/skills/` and `.agents/workflows/` are unbuilt. Reusable
  procedures should appear only when a pattern has actually repeated.
- **A learning layer.** `.agents/learning/` is unbuilt. Problem logs accumulate the evidence
  it would need. Three constraints are already agreed for whenever it arrives: an observation
  is not automatically a rule, a lesson is a candidate rather than a decision, and a permanent
  behavior change requires a reviewed change to the rules. It must not become a second source
  of truth.
- **Agent-only context.** `.agents/context/` is unbuilt, so the layer cannot quietly become a
  second documentation tree.
- **Adapters for specific agent tools.** The canonical model is vendor-neutral. Integrations
  for particular products come later, if at all.
- **Retrieval.** Whether archived context should be reachable through search or a protocol
  rather than by reading files.
- **Automatic context selection.** Whether the layer should decide which context a task needs
  rather than a person curating it in `context.md`.
- **Context compilation.** Whether the durable artifacts a task references should be assembled
  into something derived, rather than read where they live.
- **Behavior at scale.** Every rule here was written against a repository with a handful of
  tasks. What breaks at hundreds of archived tasks is unknown.
- **Index generation.** `INDEX.md` is maintained by hand and repaired by regeneration rules
  that no program implements.
- **External tracker synchronization.** Whether tasks should correspond to issues elsewhere.
- **Distribution and versioning.** How the portable rule files reach another repository, and
  how an installation is upgraded.
- **Metadata schemas.** No frontmatter, no structured fields. Everything is prose under known
  headings.

## Open questions about the model

- **How broad should a decision record be?** Recording every small choice creates noise;
  recording too few loses the reasoning. Three sentences of workflow rules once produced three
  records, which felt wrong in ratio but right in substance. Size is a poor test — a one-line
  change to a portable rule file affects every installation, and a large change to one
  repository's own documents affects nobody else.
- **When is a task package warranted?** The rules describe how to start a task but never say
  what is too small to need one.
- **How does a task split when it grows mid-flight?** The slug is fixed identity once work
  starts, so a task that turns out to be two has no defined way to become two.
- **Should the portable rule files be able to cite their own rationale?** They cannot today:
  the reasoning lives in context-fold, and decision numbering is local to whoever installed
  the layer. "Reference, do not duplicate" has no answer for a cross-repository reference.
- **How much does index-based navigation earn?** A cold agent found its task by searching the
  tree, reading the index last, where it changed nothing. Well-named, self-sufficient files
  did the work. Whether the index is worth maintaining by hand is genuinely unclear.
- **Should other derived views follow the index's rules?** Only one derived view exists. If
  more appear, whether ordering and regeneration are general properties or decided per view is
  undecided.
- **Should the workflow be enforced rather than written down?** Branch protection could require
  what `0001` and `0008` describe, instead of relying on repository settings any administrator
  can change. Enforcement makes rules real but moves them out of the repository.

## Gaps in the current rules

Found by using them. Each is a defect with evidence, not a hypothetical.

- **`0003` says every commit carries a sign-off, but `0008` discards branch commits.** Only
  the squashed commit can carry the assertion. Whether "every commit" means every commit or
  every commit that reaches `main` needs a record superseding `0003`.
- **Supersession is described as whole-record, but is usually partial.** `0009` superseded only
  the archive naming in `0007`, whose other decision stands. The wording for that was invented
  rather than derived from `0000`.
- **Findings that arrive after archival have nowhere to go.** Merging is the last stage, so
  anything learned from a merge arrives after its task is closed and immutable. It has twice
  reached the next task only because a person carried it there.
- **Archive directory names can still collide.** Minute granularity makes it remote rather
  than impossible for two concurrent branches to archive under the same name.
- **Commit signing is undecided.** `0003` records sign-off as an assertion of responsibility
  and explicitly leaves cryptographic verification open. `0004` attributes agent contributions
  but cannot prove them.

## Questions this project will not answer

Recorded so they are not mistaken for oversights.

- How other repositories should organize their own documentation. context-fold constrains what
  may live in `.agents/`, not how the rest of a repository is arranged.
- Which agent products or models a project should use.
