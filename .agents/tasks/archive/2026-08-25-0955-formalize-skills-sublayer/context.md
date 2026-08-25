# Context — formalize the skills sublayer

## References

- `decisions/0011-keep-the-model-vendor-neutral.md` permits product integration only as an adapter.
- `decisions/0020-ship-an-init-skill.md` packages adoption as a skill without making the skill the
  canonical procedure.
- `decisions/0026-map-what-is-under-the-agents-directory.md` classifies `.agents/skills/` as owned
  by whatever installed its contents.
- `decisions/0034-extend-the-claude-code-adapter-to-skills.md` exposes the installed skills through
  a host-native projection without changing their authority.
- `OPEN-QUESTIONS.md` leaves further skills, workflows, naming, procedure parity and heterogeneous
  host delivery unresolved.

## Assumptions

- Skills are the only capability family selected for v0 discussion; workflows and MCP/tools remain
  future questions.

## Open questions

- Can one contract cover project-authored, third-party and context-fold-installed skills?
- Does a skill remain an adapter when its format is shared across several agent hosts?
- Which installation metadata can be required without adopting one installer as canonical?
