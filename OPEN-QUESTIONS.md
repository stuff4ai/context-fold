# Open questions

What this project has deliberately not decided, and what using it has shown to be unresolved.

Nothing here is a plan or a schedule. Items are removed when they become decisions in
[`decisions/`](decisions/), or when they turn out not to matter.

Archived task packages contain questions that were open while those tasks ran. Those are
historical records. This document is the live list.

## Deferred capability

Chosen not to build yet, so that the methodology can be judged on its own before tooling
hides its weaknesses.

- **Tooling that produces artifacts.** Creating a task package, moving it to the archive, and
  maintaining the index are done by hand, by decision rather than omission. What the eventual
  tooling should be — a command, agent skills, or neither — is undecided. Skills were the
  original intent, reached before any of the current structure existed and never tested
  against it.
- **Skills and workflows.** `.agents/skills/` and `.agents/workflows/` are unbuilt. Reusable
  procedures should appear only when a pattern has actually repeated.
- **Automating the loop.** `0013` runs its last step by hand: a person reads accumulated
  problems and decides what recurs. `.agents/learning/` is unbuilt, and whether anything should
  perform that step is undecided — it would have to hold candidate lessons without becoming a
  second place where rules live.
- **Agent-only context.** `.agents/context/` is unbuilt, so the layer cannot quietly become a
  second documentation tree.
- **Adapters for specific agent tools.** Integrations for particular products come later, if
  at all — the model is neutral by decision, so nothing works out of the box until someone
  writes one.
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
  how an installation is upgraded. The direction favoured so far is a single repository plus
  Git tags, installed by whatever ecosystem tooling already exists, rather than a registry of
  this project's own — but nothing has been built or tried.
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
- **What does adopting this into an existing repository look like?** Establishing the structure
  in an empty repository is solved — this one did it. An existing repository already has
  documentation, conventions, and history, and nothing describes how the layer arrives without
  either ignoring them or rewriting them. Whoever adopts it also needs somewhere to disagree
  with the defaults, and no customization mechanism exists.
- **Should an adopter's installation be checkable?** This repository verifies that its installed
  rule files match the distribution, so editing them fails CI. An adopter gets no such check —
  the instruction not to edit is a request, and a copy that drifts is indistinguishable from one
  that did not.
- **What distinguishes a workflow from a skill?** Both are deferred, and the difference matters
  before either is built: roughly, how work moves through stages versus a reusable capability
  applied within a stage. Whether that distinction survives contact with real use is untested.
- **What convention governs skill names?** `ctxfold-init` follows the pattern observed in
  installed skills — a lowercase hyphenated name matching its directory — and a check enforces
  the match. Whether the `ctxfold-` prefix is right, and what a second skill would be called,
  is answered for one case and not settled.
- **Should the skill be checked against the procedure it wraps?** A check binds the templates to
  their installation, so they cannot drift. Nothing binds `SKILL.md` to `ADOPTING.md`; the skill
  can contradict the procedure it exists to follow and only a reader would notice.
- **Should the convention checks ship with the portable layer?** They encode portable rules, so
  every installation would want them, and a rule enforced in one repository and unenforced in the
  next is only half a convention. But shipping executable content is a larger question than
  shipping Markdown — it imposes a toolchain, and `0011` argues against imposing anything.
- **How do agent capabilities reach heterogeneous hosts?** A neutral model puts the burden of
  configuration on whoever installs it, and agent hosts each configure capabilities their own
  way, with no common installer. Whether context-fold should address that at all, or leave it
  entirely to adapters, is undecided.

## Gaps in the current rules

Found by using them. Each is a defect with evidence, not a hypothetical.

- **`0003` says every commit carries a sign-off, but `0008` discards branch commits.** Only
  the squashed commit can carry the assertion. Whether "every commit" means every commit or
  every commit that reaches `main` needs a record superseding `0003`.
- **Supersession is described as whole-record, but is usually partial.** `0009` superseded only
  the archive naming in `0007`, whose other decision stands. The wording for that was invented
  rather than derived from `0000`.
- **The archival commit merges without review.** `0007` puts approval before archival and `0019`
  lets the agent merge after it, so the commit that reaches `main` is not the one that was
  approved. CI covers the mechanical part; the Outcome is the one written thing in that commit
  and nothing verifies it. Moving approval to after archival would close this and would
  contradict `0007`.
- **Findings that arrive after archival have nowhere to go.** Merging is the last stage, so
  anything learned from a merge arrives after its task is closed and immutable. It has twice
  reached the next task only because a person carried it there.
- **Archive directory names can still collide.** Minute granularity makes it remote rather
  than impossible for two concurrent branches to archive under the same name.
- **Commit signing is undecided.** `0003` records sign-off as an assertion of responsibility
  and explicitly leaves cryptographic verification open. `0004` attributes agent contributions
  but cannot prove them.

## Recurring patterns

Observations with evidence across several tasks, not yet acted on. Candidates, not rules — a
pattern becomes a rule only through a reviewed change. Counts are given so the evidence can be
judged rather than the framing.

This is where a problem stops being task-local. A single entry in one task's problem log is an
incident; the same thing recurring is a property of the project, and moving it here is the
promotion `0013` describes between a problem and a candidate lesson.

- **Symmetry is spent as though it were a reason.** Three instances: a rule stated for "both
  sections" of the task index whose justification covered only one; a section of `AGENTS.md`
  built on a borrowed frame imported along with its sentence shape; a rule extended past the
  argument that produced it. Each time the pull was toward matching shapes. Consistency is
  worth something, but it is not a reason on its own.
- **Rules get stated where they are relevant rather than where they are owned.** Seven
  instances across four tasks, one of which hid a contradiction: the immutability rule was
  paraphrased in four places, and one paraphrase silently made `Status` an exception nobody had
  decided on. Every file finds every rule relevant, so "reference, do not duplicate" does not
  prevent this on its own — it forbids copying without saying who owns the original. Recording
  a decision is the most common trigger, because a record formalizes something already stated
  loosely somewhere else.

## Questions this project will not answer

Recorded so they are not mistaken for oversights.

- How other repositories should organize their own documentation. context-fold constrains what
  may live in `.agents/`, not how the rest of a repository is arranged.
- Which agent products or models a project should use.
