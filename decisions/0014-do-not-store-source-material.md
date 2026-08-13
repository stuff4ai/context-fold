# Do not store source material

## Status

Accepted

## Context

This project was designed in a conversation held elsewhere. What it settled became decision
records; what it postponed became `OPEN-QUESTIONS.md`. Both are summaries, and summarizing
discards things.

The case for keeping the source verbatim is real and was acted on: the material was written
into the repository before being reverted. A record states what was decided and why, but rarely
preserves what the alternative looked like before it lost, and when a decision is revisited that
is usually the question. Source material is also perishable in a way a file is not — a
conversation ends. And the repository already holds immutable historical material in archived
task packages, which are read to understand how something came to be, so the pattern was
available.

What defeats it is what the same material would then be. An unstructured document sitting beside
structured ones is a second place an answer can be found, and the two diverge from the moment
the first decision changes. This project has produced that failure eight times across seven
tasks, in far smaller duplications than a full transcript — including once where a rule
paraphrased in four places silently acquired an exception nobody had decided on.

The mechanism for history already exists and is not the archive. A record's Context states what
was considered and rejected. `Status` supersession states when an opinion changed and what
replaced it. The chain of records is the history: not a narrative of it, but the decisions
themselves in the order they were taken.

## Decision

Source material is not stored raw.

What matters from a source is folded. Alternatives that were considered and lost go into the
Context of the record that decided against them — that is what Context is for. What remains
undecided goes into `OPEN-QUESTIONS.md`. What is a fact about the project goes where facts live.
What is left over is dropped.

This applies to design conversations, transcripts, and notes written elsewhere. It does not
apply to task packages, whose problem logs are produced by the work itself and archived with it.

## Consequences

There is one place to look for any given answer, and no second copy to drift from it.

Folding is lossy and the loss is irreversible. Verbatim phrasing is gone, and so is anything
judged unimportant at the time of folding by someone who could be wrong about that.

There is no original to check a fold against. A misremembered rejection, or an alternative
recorded inaccurately, is undetectable from inside the repository.

Folding must happen while the source still exists. A conversation that ends before it is folded
takes everything unfolded with it, and nothing in the repository will show that anything is
missing.

Judging what to fold is a judgment, made once, under time pressure, by whoever happens to be
holding the source.
