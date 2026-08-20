# Context — manage-agent-rule-blocks

## Base state

Four files under `skills/ctxfold-init/templates/agents/` are copied into `.agents/` and must remain
byte-identical for their lifetime. Re-running `ctxfold-init` replaces those files wholesale. The
source skill and `.agents/skills/ctxfold-init/` are also kept byte-identical as a separate
dogfooding invariant.

## References

- `decisions/0005-agents-layer-boundary.md` and `decisions/0011-keep-the-model-vendor-neutral.md` —
  the layer ownership and portability boundaries that the managed block must preserve.
- `decisions/0017-adoption-procedure.md`, `decisions/0018-ship-a-distribution.md`, and
  `decisions/0021-separate-what-upgrades-from-what-diverges.md` — the current copy, distribution,
  and whole-file replacement model.
- `decisions/0032-fold-worktrees-agents-md-into-the-byte-identical-set.md` — the fourth portable
  file and the most recent whole-file identity decision.
- `skills/ctxfold-init/ADOPTING.md` and `skills/ctxfold-init/SKILL.md` — canonical adoption and the
  agent adapter that must preflight before replacing blocks.
- `tests/test_conventions.py` — whole-skill identity, installed-rule identity, distribution
  completeness, and portable-content checks.
- `OPEN-QUESTIONS.md` — the live customization and update questions narrowed by this change.

## Not relevant

- Root `AGENTS.md` remains wholly project-owned; only its reinstall instruction changes.
- The Claude Code adapter exposes the repository-installed skill but does not define adoption or
  managed-block behavior.
