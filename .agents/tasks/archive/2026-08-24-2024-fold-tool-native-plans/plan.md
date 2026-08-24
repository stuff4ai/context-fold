# Plan

## Strategy

Add one vendor-neutral paragraph to the portable `rfc.md`/`plan.md` description, propagate it
through the skill-reinstall mechanics this repository already has, and record the convention as
a decision. No adapter, no new file, no frontmatter change.

## Steps

1. Edit `skills/ctxfold-init/templates/agents/tasks/AGENTS.md`: add the new paragraph after the
   `plan.md` description, before `## Recording problems`.
2. Reinstall the complete skill into `.agents/skills/ctxfold-init/` by file copy (not
   transcription); verify byte-for-byte identical to the source.
3. Regenerate `.agents/tasks/AGENTS.md`'s managed block from the updated template, preserving its
   existing project-owned suffix (the "Handing work to another agent stack" section) exactly.
   Verify all five portable managed blocks under `.agents/` still match their templates.
4. Add `decisions/0043-fold-tool-native-planning-into-the-task-package.md` and its
   `decisions/README.md` index row, both `Accepted` — this task's own record must already be
   merge-ready per `decisions/0042` before archival.
5. Check `README.md`'s task-file summary for whether it needs a matching update — no change
   needed (see `context.md`).
6. Verify: diff-based parity check across all five managed blocks; grep the new paragraph for
   product names; run `tests/test_conventions.py`.

## Stop conditions

Stop and reconsider only if a portable managed block's project-owned suffix can't be recovered
byte-for-byte, or if `tests/test_conventions.py` fails for a reason this task didn't anticipate.
Neither occurred.
