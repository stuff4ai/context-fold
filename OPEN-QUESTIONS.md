# Open questions

What this project has deliberately not decided, and what using it has shown to be unresolved.

Nothing here is a plan or a schedule. Items are removed when they become decisions in
[`decisions/`](decisions/), or when they turn out not to matter.

Archived task packages contain questions that were open while those tasks ran. Those are
historical records. This document is the live list.

## Deferred capability

Chosen not to build yet, so that the methodology can be judged on its own before tooling
hides its weaknesses.

### Task lifecycle and coordination

- **Ongoing task-lifecycle automation.** `ctxfold-init` performs adoption, but creating an
  ordinary task package and moving it to the archive are still done by hand, by decision rather
  than omission. What, if anything, should automate that ongoing lifecycle — a command, further
  agent skills, workflows, or something else — is undecided.
- **Should a cross-stack handoff be portable?** `0036` records `handoff.md` — how one agent
  stack asks another for something and where the answer goes — as this project's suffix rather
  than a portable rule, because the rule had not been followed once when it was written. One of
  the four conditions named for reopening it has since been met: an exchange crossed a person
  rather than a subprocess, and immediately found two defects three subprocess exchanges could
  not. The other three stand — repeated use without the format changing, a second repository
  asking for the same convention, and two stacks holding one package at once. Against them, the
  format changed in response to every one of the four exchanges so far, which is the opposite of
  the stability promotion would need. If instead the file ends up mostly empty or mostly one
  stack talking to itself, it did not earn the suffix either.
- **Three details of the handoff entry are undecided.** Whether `returns:` should be a closed
  vocabulary — checkable, but bound to the verdicts two particular stacks happen to use now;
  whether a request nobody answers needs an expiry, or whether a stale entry is visible enough
  to correct itself; and whether `from:` earns its place, given that the return says who
  answered and the branch usually says who asked. `0036` settles where the convention lives,
  not these.

### Context selection and knowledge boundaries

- **Agent-only context.** [`0044`](decisions/0044-defer-the-context-sublayer.md) kept
  `.agents/context/` unbuilt: the recorded friction was a citation- and ownership-discipline
  defect, not evidence that an agent failed to locate authoritative sources. Reopen only if an
  agent demonstrably fails, or pays a recorded cost, for want of a navigation pointer; two or more
  tasks independently build their own ad hoc project-navigation aid; or a later task finds it
  cannot proceed by referencing project artifacts directly.
- **Retrieval.** Whether archived context should be reachable through search or a protocol
  rather than by reading files.
- **Automatic context selection.** Whether the layer should decide which context a task needs
  rather than a person curating it in `context.md`; and, if it should, whether an explicit policy
  distinguishes context that is always loaded from context triggered by paths, concepts or task
  properties. It is also unknown whether selection needs a portable classification of why an item
  is included, distinct from when it is loaded, and which purposes could be shared across hosts.
- **Context compilation.** Whether the durable artifacts a task references should be assembled
  into something derived, rather than read where they live; whether that bundle carries the
  source and reason for every item; and what would demonstrate that it was both sufficient and
  no larger than necessary.

### Verification, evidence, and observable execution

- **Does verification need its own agent sublayer?**
  [`0045`](decisions/0045-defer-the-verification-sublayer.md) kept `.agents/verification/`
  unbuilt, in either the full-contract or lighter reference-map form: no task package records an
  agent-system evaluation that was needed and could not be performed, and none has built its own
  ad hoc evaluation harness inside the agent layer. Product verification and task acceptance
  already have working owners. Reopen only if an agent-system property — context selection,
  authority-boundary respect, permitted tool use, recovery, or stopping behavior — demonstrably
  fails, or is shown to have failed undetected, for want of an evaluation this sublayer would have
  supplied; two or more tasks independently build their own ad hoc agent-evaluation harness; or a
  portable, host-independent way to state an agent-eval contract is demonstrated without fixing a
  runtime, model, or tool schema.

### Decisions, identity, and traceability

- **Metadata schemas beyond tasks and RFC state.** `0033` and `0037` define separate exact
  frontmatter schemas for RFC lifecycle and task status/objective rather than a general YAML
  schema. Traceability, executable checks and event records would each need stable identity and
  relationships, but it is still unknown whether those consumers justify broader structured
  metadata.

### Distribution, adoption, skills, and host integration

- **Further skills and workflows.** `ctxfold-init` packages one repeated procedure: adoption.
  Which other repeated procedures merit a skill, whether workflows earn a separate form, and
  where either should be distributed remain open. MCP/tool capabilities may have different
  authority, discovery and runtime semantics again; whether they ever belong beside skills or
  workflows is deferred until use provides evidence. The recognized `skills/` contract does not
  settle those detailed semantics.
- **External tracker synchronization.** Whether tasks should correspond to issues elsewhere.
- **Versioning, provenance, discovery, and upgrades.** `ctxfold-init` distributes the portable
  files, performs adoption, and can explicitly replace their managed blocks while preserving an
  installation's additive suffix. An installation still records neither its source nor a version
  and cannot discover that upstream rules changed. What identity it needs and how it discovers
  changes remain undecided.

### Product boundary, behavior at scale, and measurement

- **Behavior at scale.** Every rule here was written against a repository with a handful of
  tasks. What breaks at hundreds of archived tasks is unknown.

### Learning and the improvement loop

- **Automating the loop.** `0013` runs its last step by hand: a person reads accumulated
  problems and decides what recurs. `.agents/learning/` is unbuilt, and whether anything should
  perform that step is undecided — it would have to hold candidate lessons without becoming a
  second place where rules live. A disposable summary-and-reference view could avoid owning
  candidate state, but it has not shown value beyond the task archive and this live list.

## Open questions about the model

### Task lifecycle and coordination

- **Should folding outcomes produce an explicit proposal?** Finishing already requires durable
  outcomes to be moved into documentation, decisions, code or tests before archival, while
  temporary material is left behind. A tool could propose those destinations and deletions for
  review without promoting anything automatically. It is unknown whether a separate fold
  proposal would make that judgment inspectable or merely restate the task's Outcome and final
  diff.
- **How should agents find which blocked task is waiting on what, at scale?** `0025` puts
  `## Blocked by` in the task file. `0038`'s `ctxfold-tasks` skill now gives agents cross-worktree
  task discovery, but it decodes only `status`/`objective`, not `## Blocked by` itself — finding
  what a task is waiting on still means opening it. Whether that belongs in the same skill's
  contract or a separate one is undecided.
- **When is a task package warranted?** The rules describe how to start a task but never say
  what is too small to need one.
- **How does a task split when it grows mid-flight?** The slug is fixed identity once work
  starts, so a task that turns out to be two has no defined way to become two.
- **Should derived views share lifecycle rules?** The task index was removed rather than made a
  precedent. If other derived views appear, whether ordering and regeneration are general
  properties or decided per view is still undecided.

### Context selection and knowledge boundaries

- **Should context discovery have a canonical manifest?** Task `context.md` files curate what one
  task needs, and the project layer keeps durable knowledge wherever the project already owns it.
  A manifest could identify authoritative locations, ignored areas, priorities and derived
  outputs without copying their contents. It is unknown who would consume it, whether it belongs
  in the project or agent layer, and how it avoids becoming a parallel model of the repository.
- **Are generated agent-facing views disposable projections?** One possible invariant is that
  project knowledge remains authoritative while client instructions and compiled context can be
  rebuilt and discarded. That requires an unambiguous canonical source, generation provenance
  and a rule for files such as root `AGENTS.md` that are project-owned rather than generated.
  Without those boundaries, a projection becomes another authored copy that can drift.
- **What system model must be available to a task, if any?** Service ownership, dependency and
  domain boundaries, invariants and impact relationships can answer where a change belongs and
  what it must not break. They may already be expressed in code, tests or project documentation,
  and `0005` leaves that layout to the project. Requiring maps for them could improve context
  selection while creating another model whose freshness and authority must be established.
- **Should a task identify the context snapshot under which it ran?** Git already versions the
  repository, and the accepted change archives its task beside the project state it produced.
  An explicit snapshot earns its place only if selected context, generated projections, external
  inputs or runtime rules cannot be reconstructed from that commit. What identity and retention
  would make such a reference useful rather than a second version number is unknown.
- **Which history should remain active context?** Migrations, deprecated approaches, incidents,
  postmortems and the conditions for revisiting an old choice can explain why current code looks
  wrong but is deliberate. Keeping all history available defeats context selection, while keeping
  it only in an archive makes a relevant failed approach easy to repeat. The criterion that turns
  historical evidence into current guidance is not defined.
- **How should the recognized sublayer contracts evolve?** [0041](decisions/0041-define-governed-agent-sublayers.md)
  establishes goal-oriented routing, contract ownership, package ownership,
  suffix preservation, and unknown-extension coexistence for `tasks/`, `skills/`, and
  `worktrees/`. The detailed skills semantics remain open, and `context/` and `verification/`
  still need evidence before they earn physical contracts.

### Decisions, identity, and traceability

- **Should intent, decisions, behavior and evidence form an explicit trace?** Today acceptance,
  context, project decisions, tests and outcomes can reference one another, but no rule makes
  them a traversable chain in either direction. Stable relationships could answer why a check or
  change exists, expose requirements with no evidence, and guide later context selection.
  Identifiers and a machine-readable graph would also duplicate relationships already expressed
  in prose unless one representation clearly owns them. Calling the graph context does not make
  it current: it would need either authoritative edges or a way to derive them from authoritative
  artifacts.
- **Should the layer say once that identity fixes at acceptance?** It has been established
  three times separately: `0000` for record numbers, `0022` for task slugs, and the rename of
  `0022`'s own filename before it merged. The portable rules state it only about slugs, so each
  new case is rediscovered rather than derived. Stating it generally would touch `0000`, `0022`
  and the rules at once, and generalising from three cases is how this project has produced
  rules it later had to narrow.
- **How broad should a decision record be?** Recording every small choice creates noise;
  recording too few loses the reasoning. Three sentences of workflow rules once produced three
  records, which felt wrong in ratio but right in substance. Size is a poor test — a one-line
  change to a portable rule file affects every installation, and a large change to one
  repository's own documents affects nobody else.
- **Should the portable rule files be able to cite their own rationale?** They cannot today:
  the reasoning lives in context-fold, and decision numbering is local to whoever installed
  the layer. "Reference, do not duplicate" has no answer for a cross-repository reference.

### Verification, evidence, and observable execution

- **When does acceptance need behavior scenarios rather than criteria alone?** `task.md` states
  checkable acceptance criteria without prescribing Given/When/Then examples or a mapping to
  project tests. Scenarios could connect user-visible journeys to deterministic checks and expose
  ambiguous requirements before implementation. Making them a standard task artifact would
  impose a specification style and recurring ceremony even on work with no behavioral surface.
- **Does verification need to distinguish product checks from agent-system evals?** Tests and
  acceptance show properties of the repository or its product; a different kind of evaluation
  could ask whether an agent selected relevant context, respected a decision, used permitted
  tools, avoided unrelated files, recovered from failure and stopped at the right boundary.
  Context-fold has evidence for structural checks, but none yet that these agent behaviors can be
  evaluated portably without depending on a particular runtime.
- **Which observable execution facts should survive a run?** `0006` keeps execution history out
  of task packages, and `0014` rejects raw transcripts as a second source of truth. Recording
  context inputs, tool schemas, tool calls and results, compaction, verification events and the
  outcome could make a run auditable without storing hidden model reasoning. Whether hashes or
  durable evidence references belong in the task, ignored local state or an external store is
  undecided.
- **What would reproducible execution mean for a nondeterministic agent?** Reconstructing the
  request, selected context, tool contract and observable actions is a different promise from
  reproducing the model's output. Replay could test context integrity, policy enforcement and
  verification independently of the original agent, but the invariant worth promising has not
  been stated.
- **Should verification gates have an executable representation?** Acceptance criteria and the
  final check are prose, while repository CI checks only selected structural decisions. Declared
  commands, eval thresholds, manual checks and the requirements they verify could make the repair
  loop executable and its evidence comparable. They would also add a task artifact, a schema and
  host-dependent command semantics before repeated use has shown that each earns its cost.
- **What should validation diagnose beyond structural invariants?** Current checks can find
  broken links, malformed task packages and divergence between shipped and installed rules; they
  deliberately cannot tell whether prose contradicts repository reality. A future diagnostic
  could look for stale context, duplicated knowledge, abandoned task state or unsupported
  decisions, but each semantic warning needs evidence and an authority to compare against or it
  becomes an opinion presented as a check.

### Distribution, adoption, skills, and host integration

- **Where is the boundary between the neutral model and an agent harness?** `0011` requires no
  runtime beyond a filesystem and Git and puts product integrations in adapters. Tool semantics,
  permissions, context assembly, hooks, model routing and quality gates nevertheless affect how
  the written method is executed. It is unknown which of those, if any, need canonical contracts
  for runs to be comparable, and which must remain properties of a host or adapter.
- **How should an adopter override or replace the portable rules?** An adopter may append
  non-conflicting project instructions after a managed rule block, and `ctxfold-init` preserves
  them during an explicit update. Conflicting overrides, finer-grained customizable blocks, and
  maintained forks remain undefined.
- **Should an adopter's installation be checkable?** This repository verifies that its installed
  managed blocks match the distribution while permitting additive suffixes. An adopter gets no
  such check — the instruction not to edit a block is a request, and a block that drifts is
  indistinguishable from one that did not. The recognized contracts identify managed targets,
  unknown extensions, independently owned contents and intentional forks. What can be diagnosed
  or repaired without overwriting user or tool state, and which semantic boundary violations
  remain review judgments, are undecided.
- **How should the recognized skills sublayer be formalized?** `.agents/skills/` has a portable
  routing and ownership contract while `0034`'s host projection remains an adapter. Authority,
  provenance, format, lifecycle, and package discovery semantics are left to the skills task.
- **What distinguishes a workflow from a skill?** `ctxfold-init` demonstrates a reusable
  capability applied to adoption; no workflow has been built. Whether a workflow should instead
  describe how work moves through stages, and whether that distinction survives real use, is
  untested.
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
- **How do agent capabilities and context reach heterogeneous hosts?** A neutral model puts the
  burden of configuration on whoever installs it, and agent hosts each configure capabilities
  their own way, with no common installer. Whether context-fold should implement client adapters,
  expose canonical inputs to a separate integration layer that produces host-specific views, or
  leave delivery entirely outside the project is undecided. Any integration would still have to
  remain a projection rather than the source of truth.

### Product boundary, behavior at scale, and measurement

- **What product intent must a task be able to reach?** A task's `context.md` can point to any
  project artifact, while `0005` deliberately does not prescribe where requirements, product
  vocabulary or other durable knowledge live. Requiring a path from a task back to problems,
  actors, journeys, goals, non-goals, success criteria and constraints that must remain true could
  prevent locally correct work that misses its purpose. Requiring a PRD or policy shape would
  instead make context-fold prescribe a project's documentation layout for the first time.
- **Should adoption assess project-layer readiness?** Context-fold can prescribe the agent
  structure it installs but cannot assume that project intent, decisions, documentation,
  verification or reusable agent procedures are authoritative and discoverable. One proposal is
  to classify those five capabilities as established, partial, absent, ambiguous or not
  applicable, reference established sources from agent context, and create separate planned tasks
  for applicable gaps with recommendations rather than mandatory paths. Whether assessment belongs
  in adoption, how repeat runs avoid duplicate or unwanted tasks, and what evidence justifies each
  classification are unresolved. Operations, security, data, release and integrations are possible
  future assessment categories, not part of the initial proposal.
- **How should outcome and context economy be measured?** Success, human intervention, retries,
  tool calls, elapsed time, cost and context volume are observable in some hosts. Proposed notions
  such as context precision and context sufficiency are closer to the project's purpose, but both
  require a defensible account of which context was relevant and which missing item caused a
  failure. A metric without that ground truth may reward smaller bundles rather than better work.
- **Does context-fold organize project knowledge or produce it?** The current product is a
  methodology in plain files: it routes durable knowledge to project-owned artifacts and keeps
  the agent layer replaceable. Extracted architecture, domain or dependency maps could remain
  disposable projections, or become authored project knowledge when their outputs are
  authoritative, persisted and maintained independently. A provenance-aware bundle that only
  explains what was selected could be a derived implementation of the existing metaphor;
  maintaining rationale or becoming a context-intelligence or agent-operating system would raise
  a broader product boundary whose ownership and evidence have not been established.

### Learning and the improvement loop

- **Should lessons become a first-class project artifact?** `0013` currently treats a repeated
  problem as a candidate lesson and a reviewed change to a rule as the lesson's only durable
  promotion; recurring candidates remain in this document. A separate lifecycle could preserve
  evidence, rejected interpretations and integration status. It could also create a registry
  that duplicates the rule or decision where an accepted lesson must ultimately live.

### Rule consistency and enforceability

- **Should the workflow be enforced rather than written down?** Branch protection could require
  what `0001` and `0008` describe, instead of relying on repository settings any administrator
  can change. Enforcement makes rules real but moves them out of the repository.

## Gaps in the current rules

Found by using them. Each is a defect with evidence, not a hypothetical.

### Task lifecycle and coordination

- **Archive directory names can still collide, and parallel work makes it likelier.** `0009`
  records the risk as remote rather than impossible: two branches collide only if they archive
  within the same minute under the same slug. It is less remote now. `0025` gives each task its
  own checkout, so two agents choose slugs without seeing each other's, and nothing on `main`
  registers a slug that is in flight. The checks test a slug's shape and never its uniqueness
  across branches.
- **Where does `## Outcome` go?** Twenty-four of the twenty-six archived tasks here put it
  before `## Problems`; two put it after. `## Finishing` says to add an Outcome and does not say
  where. The dominant order is therefore a convention by imitation, not a written rule.

### Decisions, identity, and traceability

- **`0003` says every commit carries a sign-off, but `0008` discards branch commits.** Only
  the squashed commit can carry the assertion. Whether "every commit" means every commit or
  every commit that reaches `main` needs a record superseding `0003`.
- **Supersession is described as whole-record, but is usually partial.** Six records now carry a
  Status that narrows one part and leaves the rest standing — `0001`, `0005`, `0006`, `0007`,
  `0012`, `0018`. `0000` permits the Status edit and describes only whole-record replacement, so
  the wording every one of them uses was invented rather than derived. It is consistent by
  imitation, which is not the same as decided.
- **Commit signing is undecided.** `0003` records sign-off as an assertion of responsibility
  and explicitly leaves cryptographic verification open. `0004` attributes agent contributions
  but cannot prove them.

### Rule consistency and enforceability

- **The 98-column wrap is a convention no check enforces.** Every hand-written line honours it
  and `pymarkdown`'s line-length rule is off, so three lines of 141, 105 and 109 characters
  passed four green runs. Turning the rule on fails on archived task packages, which are history
  and should not be rewritten to satisfy a rule added afterwards, so the decision is whether the
  check exempts `archive/` — not whether to flip a flag.
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
