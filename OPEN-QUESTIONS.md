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

- **Should the layer say once that identity fixes at acceptance?** It has been established
  three times separately: `0000` for record numbers, `0022` for task slugs, and the rename of
  `0022`'s own filename before it merged. The portable rules state it only about slugs, so each
  new case is rediscovered rather than derived. Stating it generally would touch `0000`, `0022`
  and the rules at once, and generalising from three cases is how this project has produced
  rules it later had to narrow.
- **Should `INDEX.md` show what a task is blocked by?** `0025` puts `## Blocked by` in the task
  file and nowhere else, so finding what is blocked means opening every active task. That is
  affordable at three concurrent tasks and not at thirty. Adding a column changes the shipped
  index format for every installation, including the ones that never run two tasks at once.
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
- **Supersession is described as whole-record, but is usually partial.** Six records now carry a
  Status that narrows one part and leaves the rest standing — `0001`, `0005`, `0006`, `0007`,
  `0012`, `0018`. `0000` permits the Status edit and describes only whole-record replacement, so
  the wording every one of them uses was invented rather than derived. It is consistent by
  imitation, which is not the same as decided.
- **Archive directory names can still collide, and parallel work makes it likelier.** `0009`
  records the risk as remote rather than impossible: two branches collide only if they archive
  within the same minute under the same slug. It is less remote now. `0025` gives each task its
  own checkout, so two agents choose slugs without seeing each other's, and nothing on `main`
  registers a slug that is in flight. The checks test a slug's shape and never its uniqueness
  across branches.
- **The 98-column wrap is a convention no check enforces.** Every hand-written line honours it
  and `pymarkdown`'s line-length rule is off, so three lines of 141, 105 and 109 characters
  passed four green runs. Turning the rule on fails on archived task packages, which are history
  and should not be rewritten to satisfy a rule added afterwards, so the decision is whether the
  check exempts `archive/` — not whether to flip a flag.
- **`INDEX.md`'s header states rules but cannot be upgraded or checked.** `0021` moved
  `INDEX.md` out of `templates/agents/` because its rows are the installation's own, and the
  identity check follows that boundary. Its header is not the installation's own — it restates
  the precedence rule — so a correction to that rule reaches new adopters and no existing one,
  and nothing detects when a shipped header and an installed one diverge. Either the header
  carries no rules, or something has to bind it.
- **A self-run gate is not evidence about the agent that ran it.** An adoption run archived a
  task with Status `active`, ran a gate-3 command that printed no `completed` line, and reported
  the gate confirmed; the accompanying assertion counted files containing a heading and could not
  fail. Both of this project's last two tasks also passed a self-run check and were then refuted
  by a fresh reviewer. What a check proves when author and checker are the same is undecided, and
  the rules currently imply it proves acceptance.
- **Where does `## Outcome` go?** Every archived task here puts it before `## Problems`; a
  foreign run put it after. `## Finishing` says to add an Outcome and does not say where. A
  convention nobody wrote down is a convention adopters get wrong.
- **Nothing checks a record against itself.** `0007`'s Decision ordered approval before
  archival while two of its Consequences described review after it. The contradiction survived
  acceptance, five citations by later records, and every check, because checks read structure and
  links rather than claims. It was found by reading the record end to end, which nothing prompts
  anyone to do — the citing habit is to quote the sentence you need.
- **Nothing checks that a citation supports what it is cited for.** `0022` attributed a claim
  about project layout to `0011`, which is about vendor neutrality; `0005` is the actual
  authority. The link resolved, so every check passed. A wrong citation is worse than none: it
  sends a reader to a record that will not confirm the claim and looks supported to anyone who
  does not follow it.
- **The pull request description is outside every check.** It is the surface reviewers read
  first, and the only one CI cannot see. A sentence corrected in the rules and in a decision
  record was left standing there for a round, and nothing but a reader could have caught it.
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
- **Rules get stated where they are relevant rather than where they are owned.** Around eighteen
  instances across five tasks, one of which hid a contradiction: the immutability rule was
  paraphrased in four places, and one paraphrase silently made `Status` an exception nobody had
  decided on. Every file finds every rule relevant, so "reference, do not duplicate" does not
  prevent this on its own — it forbids copying without saying who owns the original. Recording
  a decision is the most common trigger, because a record formalizes something already stated
  loosely somewhere else.

  The count more than doubled in one task, which says the earlier figure was undercounted rather
  than that the rate changed. Two variants showed up there that the entry did not anticipate: a
  statement stranded in an artifact outside the repository, where no check can reach it, and
  three *names* — a decision filename, a branch, a task slug — left describing a design their
  own body had rejected. Every instance was caught by a reviewer. Nothing else has ever caught
  one, which is the argument for making it mechanical rather than for trying harder.

## Questions this project will not answer

Recorded so they are not mistaken for oversights.

- How other repositories should organize their own documentation. context-fold constrains what
  may live in `.agents/`, not how the rest of a repository is arranged.
- Which agent products or models a project should use.
