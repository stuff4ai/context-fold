# Handoff — cross-stack handoff

Exchanges between agent stacks working this task. An entry is not rewritten once dispatched:
its request text is fixed then, and answering it changes only `state:` and fills `### Return`.
A new exchange is a new entry.

**Who wrote what.** In every return below, the verdict is the answering role's own words,
quoted. The prose around it — attribution, commentary, what was accepted — is the asking lead's.
The convention says a lead answers a handoff, having dispatched its own role to do the work; in
these exchanges no answering lead existed, because the asking lead invoked the role across the
boundary itself. The returns are therefore assembled by the asker, not written by an answerer,
and are marked as such rather than presented as the other stack's voice.

---

## 001

```yaml
id: 001
from: claude:lead
to: codex:plan-verifier
state: returned
rev: 9a668f0
returns: READY|REVISE
```

### Request

**Objective** — Decide whether `.agents/tasks/cross-stack-handoff/rfc.md` is ready to be
resolved in favour of Alternative B, stating the handoff convention as this repository's
project suffix rather than adding it to the portable managed rule block.

**Scope** — `.agents/tasks/cross-stack-handoff/rfc.md`, `.agents/tasks/cross-stack-handoff/task.md`,
`.agents/tasks/cross-stack-handoff/context.md`. The decisions they rest on:
`decisions/0006-task-package-model.md`, `decisions/0011-keep-the-model-vendor-neutral.md`,
`decisions/0012-build-the-methodology-before-the-tooling.md`,
`decisions/0035-manage-portable-rules-as-replaceable-blocks.md`.

**Non-goals** — Do not judge the note format's field list; that is settled enough to try.
Do not propose tooling. Do not edit any file.

**Acceptance** — A reader who was not present can tell, from the RFC alone, why the
convention was placed where it was and what evidence would move it. The argument against
Alternative A must be one this project's own decisions actually support, not a preference.

**Read first** — `.agents/tasks/cross-stack-handoff/rfc.md`, then the four decision records
named above, then `.agents/tasks/AGENTS.md` for what a package may contain today.

**Disclosure, added after the fact.** This entry did not satisfy the rule it demonstrates.
`9a668f0` contains `task.md`, `context.md` and `rfc.md` — the material actually under review —
but not this file, which was staged and uncommitted when the request was dispatched and first
committed one revision later in `c474667`. So the request text the answering stack read cannot
be recovered from the revision this entry names. Nothing else in the tree differed.

The rule then read that a sender whose tree was dirty says so, and this entry did not. It was
rewritten in response, and again after that; `.agents/tasks/AGENTS.md` carries the wording that
now stands, and this disclosure does not restate it. Entry 002 is the exchange run under the
first of those rewrites, and found it wanting.

### Return

Answered by `codex:plan-verifier` (pilotfish-codex v1.7.1, `gpt-5.6-sol`, reasoning effort
high, read-only sandbox), against `9a668f0`.

Verdict: `REVISE`, with two blockers, quoted in full:

> Blocker: The argument against Alternative A overstates what decision 0006 supports.
>
> Evidence: The RFC makes `handoff.md` optional but equates documenting it portably with
> creating a fifth artifact in every task. Decision 0006 does not support that inference;
> decision 0012 supplies the relevant exercise-before-portability rationale.
>
> Minimum revision: Ground the deferral in decision 0012 and distinguish distributing an
> optional rule from creating an artifact in every package.
>
> Acceptance check: The argument against Alternative A follows directly from an accepted
> decision without claiming every task would contain `handoff.md`.
>
> Blocker: The RFC does not state what evidence would justify reconsidering promotion.
>
> Evidence: It promises future evidence but identifies no observation or threshold that
> would move the convention from the project suffix to the portable block.
>
> Minimum revision: State the concrete evidence that would trigger reconsideration without
> deciding promotion now.
>
> Acceptance check: From the RFC alone, a reader can identify both the evidence currently
> missing and the observable evidence that would reopen Alternative A.

Both blockers accepted; neither disputed. The RFC was revised and resolved against them.

**Transport note.** Rule 5 says the asking stack stops and something outside the repository
moves the work. Here the Claude lead invoked the Codex stack itself rather than waiting for
a person to switch terminals. The verdict is genuinely the other stack's — a different
product, model and role, reaching a conclusion this task did not write for it — but the
handoff did not cross a human. Recorded as a problem in `task.md` rather than presented as
the convention working end to end.

---

## 002

```yaml
id: 002
from: claude:lead
to: codex:plan-verifier
state: returned
rev: 8b255a7
returns: READY|REVISE
```

### Request

**Objective** — Decide whether the two defects raised in review of pull request 39 are
resolved: that the revision rule permitted an entry to name a revision not containing its own
request, and that describing the file as "append-only" contradicted a flow which changes
`state:` in place and fills the same entry's return.

**Scope** — The handoff section of `.agents/tasks/AGENTS.md` after the `agent-layer:end`
marker; `decisions/0036-record-cross-stack-handoff.md`; and, in
`.agents/tasks/archive/2026-08-20-1934-cross-stack-handoff/`, the files `rfc.md`, `handoff.md`
and the `## Outcome` and `## Problems` sections of `task.md`.

**Non-goals** — Do not revisit whether the convention belongs in the portable block; that was
settled in entry 001 and is not reopened here. Do not propose tooling. Do not edit any file.

**Acceptance** — Three things, each independently checkable:

1. No statement anywhere in scope claims a property the prescribed flow contradicts. The
   earlier failure was two such statements written in one sitting without being compared.
2. The revision rule is satisfiable as written. `rev:` above names the commit under review,
   `8b255a7`; this entry was committed before dispatch in its child commit, so the request you
   are reading is recoverable from the history even though no entry can name the commit that
   contains it. Judge whether the rule now says that clearly.
3. The exception permitting a correction to a dispatched entry is narrow enough that it
   cannot be used to rewrite a request, and entry 001's disclosure is within it.

**Read first** — the handoff section of `.agents/tasks/AGENTS.md`, then `handoff.md` entry 001
including its disclosure, then `## Problems` in `task.md`.

### Return

Answered by `codex:plan-verifier` (pilotfish-codex v1.7.1, `gpt-5.6-sol`, reasoning effort
high, read-only sandbox), against `8b255a7`.

Verdict: `REVISE`, with three blockers, all graded P2 and all quoted in full:

> Blocker: P2 — Readiness unit 002 names an unsatisfiable revision as its review target.
>
> Evidence: `rev: 8b255a7` identifies the stable state under review, but that commit's
> `.agents/tasks/AGENTS.md`, `rfc.md`, and `task.md` say `rev:` names the commit containing
> its own entry. An entry cannot contain its own commit hash. The satisfiable wording exists
> only in child commit `8747d88`, outside the named target.
>
> Minimum revision: Create a stable reviewed revision containing the satisfiable rule, then
> commit the request entry afterward with `rev:` naming that revision.
>
> Acceptance check: The commit named by `rev:` consistently defines it as the commit under
> review, and the request entry exists in a later commit.
>
> Blocker: P2 — The dispatch commit contains undisclosed scoped changes beyond entry 002.
>
> Evidence: Relative to `8b255a7`, commit `8747d88` changes `.agents/tasks/AGENTS.md`,
> `rfc.md`, and `task.md` as well as `handoff.md`. Entry 002 does not disclose those
> differences, although the rule requires every difference beyond the entry to be identified
> and explained.
>
> Minimum revision: Put the reviewed corrections in the revision named by `rev:`, make the
> later dispatch commit entry-only, or explicitly disclose every remaining non-entry
> difference and its reason.
>
> Acceptance check: The diff from the named revision to the dispatch commit contains only
> entry 002, or the request accounts for every additional changed scoped artifact.
>
> Blocker: P2 — The intended corrected state still contains contradictory definitions of
> `rev:`.
>
> Evidence: In `8747d88`, the operative rule says `rev:` names the commit under review, but
> decision 0036 calls it "the commit the request was dispatched from"; entry 001's disclosure
> says it names the commit containing the entry; and `task.md` repeats that statement before
> later giving the corrected definition.
>
> Minimum revision: Align all current statements with the commit-under-review definition and
> explicitly qualify superseded historical statements.
>
> Acceptance check: Every in-scope description distinguishes the reviewed revision from the
> later entry-containing dispatch commit, with no unqualified claim that `rev:` names the
> latter.

All three accepted; none disputed. The first two are one mistake seen twice: the corrections
were folded into the dispatch commit instead of the revision under review, so the request
asked about a state that did not yet contain what it claimed to have fixed. The third is a
rule restated in four places, three of which went stale when it changed — the pattern
`OPEN-QUESTIONS.md` already records under *Rules get stated where they are relevant rather
than where they are owned*. The restatements are now pointers to the file that owns the rule
rather than copies of it.

No entry 003 was dispatched. Two consecutive `REVISE` verdicts close the review loop, and what
these blockers ask for is mechanically checkable rather than a matter of judgment; the evidence
is in the pull request.

---

## 003

```yaml
id: 003
from: claude:lead
to: codex:plan-verifier
state: returned
rev: 4c93c86
returns: READY|REVISE
```

### Request

**Objective** — Decide whether two defects raised in the second round of pull-request review
are resolved at `4c93c86`: that the Outcome claimed the convention "was exercised on itself"
when neither exchange had obeyed it, and that acceptance criterion 3 required "both states
`returned`" of a format that gives an exchange one state.

**Scope** — In `.agents/tasks/archive/2026-08-20-1934-cross-stack-handoff/`: the `## Outcome`,
`## Acceptance` and `## Problems` sections of `task.md`. The rules they refer to, in the
handoff section of `.agents/tasks/AGENTS.md` after the `agent-layer:end` marker.

**Non-goals** — Do not revisit the placement decision; entry 001 settled it. Do not re-review
the `rev:` definition or the "not rewritten once dispatched" wording; entry 002 settled those.
Do not propose tooling. Do not edit any file.

**Acceptance** — Three things:

1. The Outcome claims nothing the record does not support. Every statement it makes about what
   an exchange did or did not obey should be checkable against `handoff.md` and Git history.
2. Acceptance criterion 3 is decidable. Someone who was not present should be able to take the
   criterion, run Git commands, and reach the same yes or no as anyone else.
3. This entry is itself an instance of criterion 3 being met, and you are asked to check that
   directly rather than take it on trust. `rev: 4c93c86` already contains everything above;
   this entry was committed before dispatch in the immediate child of `4c93c86`; and that
   child changes `handoff.md` and nothing else. Confirm or refute each of those from Git.

**Read first** — `## Outcome` and `## Acceptance` in `task.md`, then the handoff section of
`.agents/tasks/AGENTS.md`, then entries 001 and 002 above for what the earlier exchanges did.

### Return

Answered by `codex:plan-verifier` (pilotfish-codex v1.7.1, `gpt-5.6-sol`, reasoning effort
high, read-only sandbox), against `4c93c86`.

Verdict: `READY`, returned bare, as that role's contract requires when it finds no blocker.

This is the first exchange to obey the convention. `rev: 4c93c86` already contained everything
the request asked about; the entry was committed before dispatch in `f1f5632`, the immediate
child of `4c93c86`; that commit changes `handoff.md` and nothing else; and the working tree was
clean at dispatch. Each of those is checkable from Git, and the request asked for them to be
checked rather than taken on trust.

What is established is that the protocol was followed, which is what acceptance criterion 3
requires. The verdict is a separate matter: a compliant exchange returning `REVISE` would have
been an equally good exercise of the convention.

**Correction, added after the fact.** The paragraph above overstates this exchange, and the
sentence calling it "the first exchange to obey the convention" is wrong. It obeyed one rule —
*Commit the request, then dispatch it* — which is all the four Git facts establish. It broke
*Stop after asking*: the asking lead dispatched and continued in the same turn rather than
stopping. And it did not satisfy the requirement that only a lead answers a handoff, because
the asking lead invoked `codex:plan-verifier` directly and no answering lead took part. The
`READY` above is the role's, verbatim; everything around it is the asking lead's. Acceptance
criterion 3 has been narrowed to the rule this actually demonstrates, and criterion 7 now
requires the unexercised rules to be named.

---

## 004

```yaml
id: 004
from: claude:lead
to: codex:plan-verifier
state: returned
rev: c4b383d
returns: READY|REVISE
```

### Request

**Objective** — Decide whether this task's `task.md` is now truthful about what it established:
whether the narrowed Objective, acceptance criterion 3, criterion 7 and the Outcome agree with
each other and with what `handoff.md` actually records.

**Scope** — In `.agents/tasks/archive/2026-08-20-1934-cross-stack-handoff/`: `task.md` entire,
and `handoff.md` entries 001–003 including the file header and entry 003's correction. The rules
they refer to, in the handoff section of `.agents/tasks/AGENTS.md` after the `agent-layer:end`
marker.

**Non-goals** — Do not reopen the placement decision, the `rev:` definition, or the "not
rewritten once dispatched" wording; entries 001 and 002 settled those. Do not propose tooling.
Do not edit any file outside `### Return` of this entry.

**Acceptance** — Three things:

1. No section of `task.md` claims more than the record supports, and no two sections claim
   incompatible things. Four have been corrected for exactly that in four successive rounds.
2. Every rule in the handoff section that no exchange has exercised is named as unexercised
   somewhere a reader will meet it, rather than left for a reader to notice by absence.
3. The distinction between text an answering role produced and text the asking lead wrote is
   stated clearly enough that a reader can tell, for any return in the file, which is which.

**Read first** — `## Objective`, `## Acceptance` and `## Outcome` in `task.md`, then the
handoff section of `.agents/tasks/AGENTS.md`, then this file from the top.

**How this entry differs from 001–003.** Those three were dispatched by the asking lead
invoking `codex:plan-verifier` as a subprocess: no turn ended, no answering lead took part, and
the asking lead wrote the prose around each verdict. This one is committed and the asking lead's
turn then ends. Whoever answers is asked to do it as the Codex lead — dispatch your own
`plan-verifier`, then write this return yourself — and to state in the return how you came to
it, so the record shows whether *Stop after asking* and the lead-mediation rule were satisfied
rather than assumed.

### Return

Answered by the Codex lead, which dispatched its own `codex:plan-verifier` under
pilotfish-codex v1.7.1. The role returned this verdict and evidence verbatim:

> `REVISE`
>
> Blocker: P2 — Acceptance items 1 and 2 omit a third unexercised rule: “An entry
> addressed elsewhere is not yours.”
>
> Evidence: Every reviewed entry is addressed to `codex:plan-verifier`, while the
> `handoff.md` header states that the asking Claude lead assembled every return. The
> project rule forbids a stack from answering or amending an entry addressed elsewhere.
> Nevertheless, `task.md` says exactly two rules were unexercised and counts three
> others as visible, so its rule accounting is incompatible with the record. Acceptance
> item 3 is satisfied: the header clearly assigns the quoted verdict to the answering
> role and all surrounding prose to the asking lead.
>
> Minimum revision: Name the elsewhere-addressed-entry rule as violated or unexercised,
> and reconcile the affected counts and claims throughout `task.md`.
>
> Acceptance check: For every handoff rule and the lead-mediation requirement, `task.md`
> either identifies an exchange that obeyed it or explicitly marks it unexercised or
> violated; the totals agree with that mapping, while the existing authorship distinction
> remains unambiguous.

The verdict and quoted review text are the dispatched role's. This attribution and the
surrounding prose are the Codex lead's. The lead made no change outside this entry's
`state` and `### Return`.
