# Record a cross-stack handoff in the task package

## Status

completed

## Objective

Establish the record two agent stacks use to ask each other for work through a file in the
task package rather than a live channel, and exercise it far enough to learn what that record
has to say.

One exchange did coordinate that way. Entry 004 was committed, the asking lead's turn ended,
a person carried the work to the other stack, and the Codex lead found the entry, dispatched
its own `plan-verifier`, and wrote the return. Entries 001–003 did not: the asking lead invoked
the answering role as a subprocess, so no turn ended and no answering lead took part. Which
rules that leaves evidenced and which it does not is accounted for in the Outcome, rule by rule,
and is not summarised here.

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

   This is a claim about one rule, not about the convention. Entry 004 satisfied *stop after
   asking* and the requirement that only a lead answers a handoff, but neither leaves a trace
   in Git and both rest on the record of how that exchange was carried out. *Commit the
   return* no exchange has satisfied at all. Criterion 7 covers saying so.
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
stack asked another and what came back. The rules governing it live in `.agents/tasks/AGENTS.md`
and are not restated here. An entry is not rewritten once dispatched; answering it changes only
its state and fills its return.

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

Entry 004 is the exchange that tested the rest. It was committed, the asking lead stopped, a
person carried it across, and the Codex lead found it, dispatched its own `plan-verifier`,
waited, and wrote the return itself — quoting the role's verdict verbatim and marking which
words were whose. It returned `REVISE`, and the blocker was this Outcome's own rule accounting.

Rule by rule, as the record stands:

| Rule | Obeyed by | Broken by |
| --- | --- | --- |
| Address by role, never by model | 001–004 | — |
| Check for entries addressed to you before starting | 004, after a second prompt | 004 on first attempt |
| An entry addressed elsewhere is not yours | 004 | 001–003 |
| Answer in the vocabulary the request names | 001–004 | — |
| Commit the return | — | 004, which is why the rule exists |
| Commit the request, then dispatch it | 003, 004 | 001, 002 |
| Stop after asking | 004 | 001–003 |
| Only a lead answers a handoff | 004 | 001–003 |

Entries 001–003 broke the third rule as well as the last two, which this Outcome previously
counted as merely unexercised: each was addressed to the Codex stack and answered by the Claude
lead that sent it. That is the failure the rule exists to prevent, committed three times by the
author of the rule, and found by the exchange that finally obeyed it.

One rule has no exchange that obeyed it. *Commit the return* was written because entry 004
exposed the gap — the Codex lead wrote its answer and left it in the working tree, where the
asking stack could not have told it from an answer never written — and nothing has run since to
exercise it. Every rule that exactly one exchange obeyed was obeyed by entry 004.

No count of the rules appears in this package or in `0036`. Three separate statements of how
many there were went stale as the set grew, which is the same failure as restating the rules
themselves: `.agents/tasks/AGENTS.md` owns them, and the table above is an account of exchanges
rather than a second copy of the list.

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
rules", when they establish only the revision and dispatch lifecycle. Two of the rules as they
then stood leave no trace in Git at all — stopping after dispatch, and the requirement that only a lead
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

The Objective outlived what the task could show. It promised to let two stacks "coordinate
through a file in the task package instead of through a live channel, and prove it with a real
exchange", and every exchange run against it used a live channel: the asking lead invoked the
answering stack as a subprocess, so no turn ended and no answering lead took part. The Outcome
was corrected to admit this while the Objective above it still made the original promise, which
left the package asserting two incompatible things about the same work. Narrowing the acceptance
criteria made them truthful and left the Objective they were meant to serve untouched — a
criterion can be honest about what it checks and still not answer the question that was asked.
The Objective now claims the record format and says plainly that file-mediated coordination is
deferred.

That is four sections of this one file — Outcome, acceptance criterion 3, criterion 7 and now
Objective — each corrected in a separate round, each stale for the same reason: written early,
overtaken by what the work found, and not re-read when it was. Nothing in the lifecycle prompts
re-reading a task's own contract against its findings before archival, and the final check does
not compare the Objective with the Outcome.

A Codex lead followed the layer's own navigation and did not find the handoff. Given only "you
are the Codex lead in this repository, follow AGENTS.md", it read the root file, the layer file,
the tasks rules and `INDEX.md`, then reported that there were no active tasks. It was right:
the index says `Active: None.`, and the entry addressed to it sat in an archived package. Two
causes, both in the convention. The inbox rule said what an entry addressed to you *is* and
never said to go looking, so it described recognising mail without describing checking the
letterbox. And a request outlives archival by design — `0007` archives before review, so any
handoff sent during review lands in an archived package, invisible to a navigation path built
around the active list. Found only because the exchange crossed a person; three subprocess
dispatches had been handed the file path directly and could not have surfaced it. The rule is
now active and names the archive.

The asking lead answered its own requests, three times. Entries 001–003 were addressed to
`codex:plan-verifier`, and the Claude lead that sent them wrote every return — quoting a role's
verdict, but composing the attribution, the commentary and the acceptance of blockers. That is
precisely what *an entry addressed elsewhere is not yours* forbids, and this Outcome had counted
the rule among those merely visible in the entries rather than among those broken. The
dispatched verifier caught the miscount; the underlying violation had been sitting in the file
since the first exchange. Writing the return for a handoff you sent feels like bookkeeping and
is the thing the rule exists to stop.

The answering lead did not commit its return. The convention said who writes a return and never
said who commits it, so the answer sat in the working tree where the asking stack could not
distinguish it from an answer never written. Added to the rule.

An exchange was credited with obeying a rule written after it ran. The Outcome table said entry
004 obeyed *answer in the vocabulary the request names*, and that rule had just been amended to
require the answering lead to commit the return — which entry 004 did not do, as the problem log
directly above said. Amending a rule silently re-scored every exchange already recorded against
it. The delivery requirement is now its own rule so that its accounting cannot hide inside
another's, and no exchange has obeyed it.

Counting the rules went stale three times. `0036` said five while the suffix had six bullets and
a lead-only clause and the Outcome table listed eight rows. Each count was written when it was
true and none was revisited when the set grew, which is the restatement problem in its smallest
form: a number is a copy of a list. No count appears anywhere now — `.agents/tasks/AGENTS.md`
owns the rules, `0036` points at it without enumerating, and the Outcome table is an account of
exchanges rather than a second copy of the set.

Five sections of this file have now been corrected in five successive rounds, every one for the
same reason: written when true, overtaken by the work, not re-read. The pattern outlasted being
named in the problem log twice, which suggests noticing it is not the same as having a place in
the lifecycle where re-reading happens.

The Objective went stale a second time, from the round that fixed the Outcome it summarised. It
had been corrected once already, and the correction introduced its own summary — that every rule
had an obeying exchange and three were obeyed only once. Splitting the delivery requirement into
its own rule falsified both halves in the same commit that wrote the accurate account four
paragraphs below. Correcting a section does not inoculate it: the new text is a summary too, and
a summary goes stale whenever the thing it summarises moves. The sentence is gone rather than
rewritten, and the Objective now points at the Outcome instead of restating it, which is the same
remedy the rules themselves needed.

That makes six sections corrected in six rounds, and the sixth was a re-correction. Each fix was
right about the fact it corrected and wrong to state the fact in a second place. The remedy that
finally holds is not a more careful summary but no summary: one owner per claim, pointers
everywhere else. Nothing in the lifecycle would have caught any of them — the final exact-head
check reads the repository's structure and never compares two sections of a task against each
other.
