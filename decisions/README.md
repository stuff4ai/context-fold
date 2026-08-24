# Decision records

Durable project decisions, recorded as [decision records](https://adr.github.io/).

The scope is any significant decision — workflow, conventions, tooling, structure — not only
architectural ones. Accepted records are immutable apart from their `Status` field: supersede
rather than rewrite, and never renumber.

New records use [`.adr-template.md`](.adr-template.md).

| ID | Title | Status |
| --- | --- | --- |
| 0000 | [Use decision records](0000-use-decision-records.md) | Accepted |
| 0001 | [Use GitHub Flow](0001-use-github-flow.md) | Accepted |
| 0002 | [Use Conventional Commits](0002-use-conventional-commits.md) | Accepted |
| 0003 | [Sign off every commit](0003-sign-off-commits.md) | Accepted |
| 0004 | [Attribute agent contributions as co-authors](0004-co-author-agent-commits.md) | Accepted |
| 0005 | [Separate the agent operating layer from project knowledge](0005-agents-layer-boundary.md) | Accepted |
| 0006 | [Organize work as task packages](0006-task-package-model.md) | Accepted |
| 0007 | [Archive tasks before merge](0007-archive-before-merge.md) | Accepted |
| 0008 | [Squash merge pull requests](0008-squash-merge-pull-requests.md) | Accepted |
| 0009 | [Order the task index newest first](0009-order-task-index-newest-first.md) | Accepted |
| 0010 | [Record open questions in the project layer](0010-record-open-questions-in-project-layer.md) | Accepted |
| 0011 | [Keep the model vendor-neutral](0011-keep-the-model-vendor-neutral.md) | Accepted |
| 0012 | [Build the methodology before the tooling](0012-build-the-methodology-before-the-tooling.md) | Accepted |
| 0013 | [Improve context from the work](0013-improve-context-from-the-work.md) | Accepted |
| 0014 | [Do not store source material](0014-do-not-store-source-material.md) | Accepted |
| 0015 | [Stages are not one-way](0015-stages-are-not-one-way.md) | Accepted |
| 0016 | [Check the conventions in CI](0016-check-conventions-in-ci.md) | Accepted |
| 0017 | [Adoption procedure](0017-adoption-procedure.md) | Accepted |
| 0018 | [Ship a distribution](0018-ship-a-distribution.md) | Accepted |
| 0019 | [Agents may merge after approval](0019-agents-may-merge-after-approval.md) | Accepted |
| 0020 | [Ship an init skill](0020-ship-an-init-skill.md) | Accepted |
| 0021 | [Separate what upgrades from what diverges](0021-separate-what-upgrades-from-what-diverges.md) | Accepted |
| 0022 | [Route findings without an owning task](0022-route-findings-without-an-owning-task.md) | Accepted |
| 0023 | [Approve the final state](0023-approve-the-final-state.md) | Accepted |
| 0024 | [Settle status disagreements by the directory](0024-settle-status-disagreements-by-the-directory.md) | Accepted |
| 0025 | [Run tasks in parallel](0025-run-tasks-in-parallel.md) | Accepted |
| 0026 | [Map what is under the agents directory](0026-map-what-is-under-the-agents-directory.md) | Accepted |
| 0027 | [Produce evidence at the final check](0027-produce-evidence-at-the-final-check.md) | Accepted |
| 0028 | [Let a task declare its own approver](0028-let-a-task-declare-its-own-approver.md) | Accepted |
| 0029 | [Drop the task template](0029-drop-the-task-template.md) | Accepted |
| 0030 | [Add a Claude Code adapter](0030-add-a-claude-code-adapter.md) | Accepted |
| 0031 | [Check task packages for scaffolding by shape](0031-check-task-packages-for-scaffolding-by-shape.md) | Accepted |
| 0032 | [Fold worktrees/AGENTS.md into the byte-identical set](0032-fold-worktrees-agents-md-into-the-byte-identical-set.md) | Accepted |
| 0033 | [Separate RFC discussion from execution planning](0033-separate-rfc-discussion-from-execution-planning.md) | Accepted |
| 0034 | [Extend the Claude Code adapter to skills](0034-extend-the-claude-code-adapter-to-skills.md) | Accepted |
| 0035 | [Manage portable rules as replaceable blocks](0035-manage-portable-rules-as-replaceable-blocks.md) | Accepted |
| 0036 | [Record a cross-stack handoff in the task package](0036-record-cross-stack-handoff.md) | Accepted |
| 0037 | [Replace the task index with frontmatter](0037-replace-task-index-with-frontmatter.md) | Accepted |
| 0038 | [Add a task discovery skill](0038-add-a-task-discovery-skill.md) | Accepted |
| 0039 | [Confirm proactive task creation and hold unjudged findings in context.md](0039-confirm-proactive-task-creation-and-hold-unjudged-findings.md) | Accepted |
| 0040 | [Guard shipped-skill portability](0040-guard-shipped-skill-portability.md) | Accepted |
