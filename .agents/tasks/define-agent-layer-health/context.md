# Context — define agent-layer health and recovery

## References

- `decisions/0018-ship-a-distribution.md` scopes the installation and leaves unrelated `.agents/`
  contents alone.
- `decisions/0026-map-what-is-under-the-agents-directory.md` records a measured failure caused by
  confusing nested checkouts with current state.
- `decisions/0035-manage-portable-rules-as-replaceable-blocks.md` defines all-target preflight,
  managed-block replacement and suffix preservation.
- `skills/ctxfold-init/ADOPTING.md` defines current repeat-adoption recovery and its stop conditions.
- `OPEN-QUESTIONS.md` asks whether an adopter's installation should be checkable.

## Open questions

- Is health checking part of `ctxfold-init`, a separate skill, repository CI, or more than one?
- What metadata distinguishes an unknown extension from a damaged required sublayer?
- Can a semantic deletion-test violation be diagnosed without presenting an opinion as a check?
- How does an intentional fork leave the managed update path safely?
