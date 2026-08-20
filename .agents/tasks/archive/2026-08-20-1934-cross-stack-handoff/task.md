# Record a cross-stack handoff in the task package

## Status

completed

## Objective

Let two agent stacks working the same repository coordinate through a file in the task
package instead of through a live channel, and prove it with a real exchange.

## Why

A repository is increasingly worked by more than one agent stack — here, Claude Code and
Codex CLI, each running its own orchestration policy with its own named roles. The task
package already carries the contract, the context and the plan, but nothing says how one
stack asks another for something and gets an answer back.

Without a place for that exchange, it happens in two transcripts that neither the other
stack nor a reviewer can see. The request, the state it referred to, and the verdict all
vanish. A repository that keeps the record of its work loses precisely the part where two
agents disagreed.

Doing this by artifact rather than by message is the point, not a limitation. The file is
readable in the pull request, it survives both sessions, and it needs nothing running.

## Scope

- `.agents/tasks/cross-stack-handoff/` — this package, including its RFC.
- `decisions/` — one new record, and its row in `decisions/README.md`.
- `.agents/tasks/AGENTS.md` — the project suffix after the `agent-layer:end` marker only.
  The managed block is out of scope; see Out of scope.
- `README.md` — a short pointer, if the RFC resolves that adopters need one.

## Out of scope

- **The portable managed rule block.** Whether `handoff.md` becomes a portable artifact in
  every installation is deliberately deferred until this convention has been used. `0035`
  provides the project suffix for exactly this case. The promotion question is recorded in
  `OPEN-QUESTIONS.md` rather than answered here.
- **Tooling.** No script, no plugin, no daemon. `0012` applies: the methodology is built
  before the tooling that would hide its weaknesses.
- **Changing either stack's own configuration.** Nothing under `~/.claude` or `~/.codex` is
  modified. Both role rosters stay exactly as their installers wrote them.
- **A general multi-agent model.** This records one convention with one worked example, not
  a taxonomy of agent stacks, roles, or capability tiers.

## Acceptance

1. `decisions/` carries a record stating the handoff convention, its rules, and why the
   portable block was not changed; `decisions/README.md` lists it.
2. `.agents/tasks/AGENTS.md` carries the convention as a project suffix. Its managed block
   is byte-identical to `.agents/skills/ctxfold-init/templates/agents/tasks/AGENTS.md` and
   to `skills/ctxfold-init/templates/agents/tasks/AGENTS.md`, verifiable by comparing the
   bytes between the `agent-layer` markers in all three.
3. This package contains a `handoff.md` recording at least one exchange whose revision and
   dispatch lifecycle obeyed *Commit the request, then dispatch it*, each part checkable from
   Git: the entry's `state:` is `returned`; its `rev:` names a commit that already contains
   what the request asked about; the entry itself was committed before dispatch, in a commit
   descended from `rev:`; and that dispatch commit differs from `rev:` in nothing but the
   entry, or the request discloses what else differs.

   This is a claim about one rule, not about the convention. *Stop after asking* and the
   requirement that only a lead answers a handoff leave no trace in Git, and no exchange here
   satisfied either; criterion 7 covers saying so.
4. That exchange was real. The return records which stack and which role produced it, and
   the verdict is one this task did not write for it.
5. The convention's rules are stated somewhere a reader who was not present can apply them
   to a new task without reading this package.
6. `.agents/tasks/AGENTS.md`'s suffix does not contradict its managed block, and states no
   rule that only makes sense for this repository.
7. The record names every rule no exchange exercised, rather than letting evidence for one
   rule read as evidence for the convention. It also distinguishes, in each return, the text
   the answering role produced from the text the asking lead wrote around it.

## Approval

Human. The RFC leaves a direction for the reviewer to choose rather than a claim to check.

## Outcome

Decision `0036` records `handoff.md` as a task-package artifact: a record of what one agent
stack asked another and what came back, governed by five rules — address by role and never by
model, an entry addressed elsewhere is not yours, answer in the vocabulary the request names,
commit the request before dispatching it, and stop after asking. An entry is not rewritten once
dispatched; answering it changes only its state and fills its return.

The convention is stated as this repository's project suffix in `.agents/tasks/AGENTS.md`, the
first use of the boundary `0035` created. The portable managed rule block is untouched, so its
three copies remain byte-identical and no adopter receives the convention. The rules name a
stack and a role rather than any product, so promoting them later is a move rather than a
rewrite.

Promotion is deferred rather than refused. `OPEN-QUESTIONS.md` now carries what would reopen it
— repeated use without the format changing, a second repository asking for it, an exchange that
crosses a person rather than a subprocess, or two stacks holding one package at once — and,
separately, the three details of the entry format this task did not settle.

The convention was exercised on itself, and that is where nearly everything it now says came
from. `handoff.md` entry 001 asked the Codex stack's `plan-verifier` whether the RFC was ready
to resolve, and entry 002 asked whether the corrections made after the first round of
pull-request review held. Both returned `REVISE`; every blocker was accepted.

Neither of those two exchanges obeyed the convention. Entry 001's request was uncommitted when
it was dispatched, so the text the answering stack read is not recoverable from the revision the
entry names. Entry 002 named a revision that did not yet contain the fix it asked about, and its
dispatch commit changed three files the entry never disclosed. Each failure produced the rule
that now forbids it, which is the substance of what this task learned: the rules were not
designed and then demonstrated, they were extracted from the demonstration going wrong.

Entry 003 obeyed the revision and dispatch rule, and is the only evidence that that rule can be
obeyed. It named a revision already containing what it asked about, was committed before
dispatch in that revision's immediate child, changed nothing but the entry, and returned
`READY`. Every part of that is checkable from Git, and the request asked for it to be checked
rather than asserted. The verdict is a separate matter: a returning `REVISE` would have
demonstrated the rule just as well.

Two rules were exercised by no exchange at all, and Git cannot show otherwise either way.
*Stop after asking* was broken every time: the asking lead dispatched and then continued in the
same turn, because it invoked the answering stack itself instead of stopping for something
outside to carry the work. And no answering *lead* was ever involved — the asking lead invoked
`codex:plan-verifier` directly, so the convention's requirement that only a lead answers a
handoff, which is what keeps a dispatched role from being addressed across stacks, has never
been tested. In each entry the verdict is the role's, quoted; the prose around it is the asking
lead's.

So the convention is evidenced in part. One rule is demonstrated, three are visible in the
entries as written, and two remain claims. A handoff that crosses a person is already recorded
as a condition that would reopen promotion; it is also what would exercise the two.

## Problems

Argued against portability from the wrong decision record. The RFC's case for the project
suffix leaned on `0006`'s warning that task systems tend toward ceremony — "a full set of
artifacts per task, most of them empty" — as though promoting `handoff.md` would put a
fifth file in every package. It would not: the file is optional, exactly as `rfc.md` and
`plan.md` already are, both of which are portable. The applicable record was `0012`, about
exercising the methodology before distributing it. Caught by `codex:plan-verifier`, not by
the author, and it had already been copied into the draft decision record before it was
found. Quoting the sentence that supports the conclusion is how a wrong citation survives —
the same pattern `OPEN-QUESTIONS.md` already records under *Rules get stated where they are
relevant rather than where they are owned*.

Deferred promotion without saying what would end the deferral. The RFC promised evidence
and named none, which makes the deferral unfalsifiable — nothing could ever arrive that
would settle it. Also caught by the reviewer. Writing the four reopening conditions was
harder than writing the deferral, which is probably why it had been skipped.

The RFC described a format the task was not using. Its example showed each entry opening
with `---` frontmatter, copied from how `rfc.md` opens, while the real `handoff.md` used a
fenced `yaml` block because a Markdown document has only one frontmatter block and this
file holds many entries. The rule count disagreed too: four in the RFC, five everywhere
else. Both went unnoticed until the files were read side by side after the review, so the
reviewer did not catch them either — it was only asked about the placement argument.

The first exchange did not cross a person, which is the rule most likely to be wrong.
Rule 5 says the asking stack stops and something outside the repository moves the work.
Here the Claude lead invoked Codex as a subprocess instead. The verdict is genuinely the
other stack's, so the format and the vocabulary were exercised, but the one part of the
convention that assumes a human in the loop was not. Recorded in `handoff.md` entry 001 and
named as a reopening condition rather than left to look like a completed round trip.

The worked example broke the rule it was demonstrating. Entry 001 named `9a668f0` as the
revision its request referred to, but `9a668f0` does not contain `handoff.md` — the file was
staged and uncommitted at dispatch and first landed in `c474667`. The request the answering
stack actually read is therefore not recoverable from the revision the entry names, which is
the one thing `rev:` exists to make possible. The rule as written only required a dirty tree
to be disclosed, and even that was not done. Caught in review of the pull request, not by the
author and not by the reviewing stack — which had the evidence, having run `git status` and
seen the file staged, and did not treat it as a defect because it was asked about the
placement argument instead. A review answers the question it was given.

The rule was rewritten in response, and rewritten again when that version turned out to be
unsatisfiable — see the next two entries. `.agents/tasks/AGENTS.md` owns the wording that
stands; restating it here is what made three copies go stale at once.

"Append-only" described the file as something it was not. The rules said each exchange was a
new entry and a return went into its own entry, while the prescribed flow changed `state:
requested` to `state: returned` in place and filled that same entry's `### Return`. Both
statements were written in the same sitting and neither was checked against the other, because
the wrong word was reached for first and then justified. It now says what is actually
guaranteed: an entry is not rewritten once dispatched, its request text is fixed then, and
answering changes only the state and the return.

Correcting entry 001 then violated the rule that had just replaced it. Adding the disclosure
meant editing a dispatched entry, which "not rewritten once dispatched" forbids outright —
leaving no way to fix a factual error in a record whose value is being accurate. The rule now
carries one narrow exception: a correction is added to the entry and marked as added
afterwards, never substituted for what it corrects. Found by applying the new rule to the act
of writing it, which is the cheapest review available and was not done for the first version.

The rule written to fix the revision defect was unsatisfiable. It said `rev:` names the commit
containing the entry, which no entry can do: writing the hash in changes the content and so
changes the hash. Discovered by trying to follow it — the entry was committed with a
placeholder, the real hash substituted, and the tree then no longer matched the commit just
made. `rev:` now names the commit under review, and the entry is committed before dispatch in a
later commit; both guarantees hold, and the impossibility is stated in the rule so the next
reader does not rediscover it. Two rules in a row were written confidently and were wrong, and
neither survived its first application. Writing a rule and following it are separate acts, and
only the second is a check.

Entry 002 asked about a fix that was not in the revision it named. `rev: 8b255a7` was the
commit before the correction; the corrected rule reached the repository only in `8747d88`, the
commit carrying the entry itself. So the request asked the answering stack to judge a state
that still contained the defect it claimed to have fixed, and the same commit also changed
three files the entry never mentioned, which the disclosure rule required. One mistake with two
faces: corrections belong in the revision under review, and the dispatch commit should add the
entry and nothing else. The rule now says a named revision must already contain whatever the
request asks about.

The rule about `rev:` was restated in four places and three went stale the moment it changed.
`0036`, entry 001's disclosure and this log each carried their own copy; when the wording was
corrected, the copies contradicted the original and each other. This is the pattern
`OPEN-QUESTIONS.md` already records — rules stated where they are relevant rather than where
they are owned — and it was reproduced here within an hour of citing it. The copies are now
pointers to `.agents/tasks/AGENTS.md`, which owns the rule.

Three rounds of review, each finding real defects, none of them in the placement decision the
task was actually about. Every finding was in the worked example or in the rules governing it —
the parts written quickly because they seemed like description rather than design. The review
loop was closed after the second `REVISE` rather than running a third exchange: the remaining
blockers ask for things a grep and a diff settle, and a fourth opinion on them would be
ceremony.

The Outcome claimed a successful exercise the record did not support. It said the convention
"was exercised on itself" while both exchanges had broken it — one dispatched uncommitted, the
other naming a revision without the fix it asked about — and it described only entry 001, having
been written before entry 002 existed and never revisited. A summary written once and left alone
while the thing it summarizes changes underneath is how an accurate record becomes a false one.

Acceptance criterion 3 was written against a design that had already been abandoned. It required
"both states `returned`", which made sense when a request and its return were separate entries;
once an exchange became one entry with one state, the criterion had no meaning and could not be
checked either way. It was drafted at the start and not re-read when the format changed. Criteria
are as capable of going stale as rules, and nothing prompts a re-read of them at the point the
design moves.

Evidence for one rule was presented as evidence for the convention. Acceptance criterion 3
listed four facts recoverable from Git and called satisfying them "followed the convention's own
rules", when they establish only the revision and dispatch lifecycle. Two of the five rules
leave no trace in Git at all — stopping after dispatch, and the requirement that only a lead
answers a handoff — and both were broken in every exchange, including the one held up as
compliant. The asking lead invoked the answering role directly and continued in the same turn,
so no answering lead ever existed and no turn ever ended. Checkability is not coverage: the
rules that can be verified mechanically are not the rules most likely to be broken, and
collecting the easy evidence made the record look complete. The criterion now claims one rule,
a new criterion requires the unexercised ones to be named, and entry 003 carries a correction
saying what it did and did not demonstrate.

Returns were written to read as the other stack's voice. Each begins "Answered by
`codex:plan-verifier`", but only the verdict is that role's; the attribution, the commentary and
the acceptance of blockers were all written by the asking lead, which under the convention is
the one participant that should not be composing the answer. The file now states that boundary
once at the top rather than leaving each return to imply otherwise.
