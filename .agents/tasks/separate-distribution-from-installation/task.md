# Separate distribution from installation

## Status

active

## Objective

Ship a distribution, install this repository from it, and make the fact that they match a check
rather than a claim.

## Why

`ADOPTING.md` tells an adopter to copy three files out of this repository's `.agents/`. That
directory is this project's own installation, not its distribution — copying it into another
project exports every local fact about this one.

The previous task's dry run found the consequence: two statements in a distributed file that are
false where another tool also writes to `.agents/`. Both are symptoms. Nothing separated the
artifact we ship from the copy we use, so the copy was the artifact.

Separating them makes ownership structural. The templates define what an installation contains,
so nothing needs asserting about whatever else shares the directory. And it makes dogfooding
verifiable: "we use what we ship" becomes a test instead of a sentence.

## Scope

- `templates/agents/` and `templates/task/` — what context-fold ships.
- `.agents/` — reinstalled from the templates, keeping this installation's own data.
- `tests/test_conventions.py` — the check that installed rule files match the templates.
- `ADOPTING.md`, `decisions/0018-ship-a-distribution.md`, `0005`'s `Status`, `OPEN-QUESTIONS.md`.

## Out of scope

- The `/ctxfold-init` skill. It adapts `ADOPTING.md` and follows this.
- Versioning, upgrade paths, or any way for an adopter's copy to learn it is stale.
- Moving out of `.agents/` to a directory nothing else shares.

## Acceptance

1. `templates/agents/` holds the rule files and an empty index; `templates/task/` holds a task
   package skeleton. The rule files were moved, not copied.
2. The two defects the dry run found are fixed in the templates: no claim over the whole
   directory, and a deletion test scoped to what context-fold installed.
3. `.agents/` is byte-identical to the templates for every rule file, and a check enforces it.
   That check has been made to fail and then reverted.
4. Reinstalling the rule files changes nothing, and `ADOPTING.md` says which files a reinstall
   may copy. Copying the whole distribution twice is destructive and is documented as such.
5. The adoption dry run against a scratch copy of a real repository succeeds using the rewritten
   `ADOPTING.md`, and both fixed statements are true there.

## Problems

### Reinstalling destroyed this installation's data

Verifying that reinstalling is a no-op — `cp -r templates/agents/. .agents/` — replaced
`.agents/tasks/INDEX.md` with the empty template, discarding eleven archived rows.
Assumed: install and reinstall are the same operation, since the distribution is the same.
Actually: the distribution contains one file that is a starting point rather than a fixed
artifact. Copying it is correct exactly once. Every subsequent copy is destructive, and
destructive in a way that looks like success — the command reports nothing and the index is
valid, just empty.
Caught by the verification step written for it. It would not have been caught by the identity
check, which excludes `INDEX.md` by design, nor by review, since the diff would read as a
deliberate reset.
`ADOPTING.md` now says to copy `INDEX.md` once and to copy only the `AGENTS.md` files when
replacing rules later. The deeper issue — that upgrading has no defined procedure — is
unresolved and deferred.

### The shipped rules named the project that ships them

Five places in the distribution said "context-fold" — installed by it, replaced when it updates,
a problem with it, what it installed, projects using it.
Assumed: naming the installer is useful, because it tells the reader what put the file there.
Actually: the rules describe the layer, and the layer is the thing being installed. Naming its
vendor is wrong for anyone who forks and maintains the rules themselves, and it is the same
assumption as naming an agent product — which `0011` already rejects. Provenance is metadata,
which is deferred, and the earlier attempt to record it as a file was removed for the same
reason.
Removed all five and added the project name to the portability check, so the exclusion is
enforced rather than remembered. I had defended keeping four of the five one message earlier.

### A shipped rule pointed somewhere the reader may not have

`tasks/AGENTS.md` opened with "the reasoning behind them lives in context-fold, not here." In an
adopter's repository that is a pointer to somewhere they may not have; in context-fold's own
installation it is false, since the reasoning lives exactly here.
Assumed: a shipped file can refer to the project that ships it.
Actually: it can name it — "installed by context-fold", "replaced when context-fold is updated"
— because those are true everywhere and tell the reader what put the file there. Directing them
to reasoning they cannot reach is different, and the sentence was self-contradictory in the one
installation that could reach it. Removed; the clause told nobody anything actionable.
The mirror of what the dry run found. Those defects were visible only from outside this
repository; this one was visible only from inside it, and neither review pass saw the other's.

### Acceptance claimed reinstalling was a no-op after that was known false

Criterion 4 said copying the templates over `.agents/` twice leaves the tree clean. The problem
log two entries above records that doing so destroys `INDEX.md`. `ADOPTING.md` was corrected;
the criterion measuring it was not.
Assumed: recording a finding and fixing the affected document closes it.
Actually: the acceptance criteria are a third place the same claim lived, and they were the one
place still asserting the disproved version — in the same task that disproved it.
Twelfth instance of a change stranding an older statement, and the second consecutive task where
the stranded statement was in the acceptance criteria specifically. That is no longer a
coincidence: criteria are written early, consulted at the end, and never reread in between,
which is exactly the profile of prose that goes stale.

### The distribution mixes two kinds of file under one instruction

`templates/agents/` holds four files: three that must never change in an installation, and one
that must change immediately. "Copy this directory" is right for one and wrong for the other, and
nothing in the layout distinguishes them.
Assumed: shipping a directory and installing a directory are symmetric.
Actually: the shipped set is not homogeneous. The identity check already encodes the distinction
— it covers the `AGENTS.md` files and excludes `INDEX.md` — so the knowledge exists in the tests
and not in the structure it describes.
Left as is. Splitting the directory would make the instruction safer and the layout stranger, and
one instance of the hazard is not enough to choose.
