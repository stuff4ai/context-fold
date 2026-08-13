# Build the methodology before the tooling

## Status

Accepted

## Context

The natural shape for this project was software: a command that initializes the structure,
creates tasks, maintains the index, and archives work. That path was started and abandoned.

Tooling makes a methodology cheaper to follow, which is the problem. A command that creates a
task package makes creating one effortless, and effortless ceremony is invisible ceremony —
nobody notices that an artifact is never read when producing it costs a keystroke. The
friction is the signal. Automating it away before knowing which parts earn their keep would
preserve the weak parts along with the strong ones, and make both expensive to change once a
tool depends on them.

Building tooling first also front-loads the decisions that matter least. A command's flags,
output format, and configuration are real work, and none of it tells you whether the model
underneath is right.

There was a second reason specific to this project. If the methodology cannot be followed by
hand with plain files, it is too complicated to be worth automating — and the only way to find
that out is to follow it by hand.

## Decision

v0 is repository conventions in plain files and Git. No command, no program, no runtime.

The methodology is applied to this repository before it is offered to any other. Every rule
here is produced by using it, and a rule that has not been exercised is not recorded as though
it had been.

The project must be able to adopt itself. The structure is established by a task that uses the
structure while creating it, rather than by building it first and testing afterwards. A
methodology that cannot bootstrap into a repository using its own process would not survive
contact with an existing one.

Tooling comes after the conventions have been used enough to show which of them matter. What
that tooling should be is not decided here.

## Consequences

Weak parts of the model surface as friction rather than being hidden by automation. Five tasks
produced a problem log of defects found this way, several of which changed the rules.

Following the methodology is more laborious than it needs to be, permanently until tooling
exists. Index rows are maintained by hand, archival is a manual move, and the regeneration
rules that repair a conflicted index are written for a program that does not exist.

Manual application is error-prone in exactly the places a tool would be reliable. The index has
already been wrong, and nothing but review catches it.

All evidence for this methodology comes from one repository — this one — applying it to
itself. Self-application is the weakest possible validation: the rules were written by the same
process that tested them, and nothing here has met an existing codebase, a second contributor,
or concurrent tasks.

Deferring tooling defers distribution. There is no way for another project to install these
conventions except by copying files.
