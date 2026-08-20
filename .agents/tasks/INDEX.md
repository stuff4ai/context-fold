# Tasks

Derived navigation view. Each task's `task.md` owns its status and this table restates it. When
they disagree, the task's directory says which is stale: a package under `archive/` is finished
whatever `task.md` says, and one that is not is unfinished whatever this table says.

## Active

None.

## Archive

| Task | Status | Objective |
| --- | --- | --- |
| [2026-08-20-1934-cross-stack-handoff](archive/2026-08-20-1934-cross-stack-handoff/task.md) | completed | Let two agent stacks coordinate through a file in the task package instead of a live channel |
| [2026-08-20-1804-manage-agent-rule-blocks](archive/2026-08-20-1804-manage-agent-rule-blocks/task.md) | completed | Let adopted repositories preserve additive project instructions while portable rules update by managed block |
| [2026-08-20-1746-categorize-open-questions](archive/2026-08-20-1746-categorize-open-questions/task.md) | completed | Organize live questions into discussion categories and identify individual task candidates |
| [2026-08-20-1543-link-claude-skills](archive/2026-08-20-1543-link-claude-skills/task.md) | completed | Let a Claude Code session in this repository discover and invoke the already-installed `ctxfold-init` skill |
| [2026-08-20-1505-add-task-rfc](archive/2026-08-20-1505-add-task-rfc/task.md) | completed | Add an optional RFC artifact for mutable proposal discussion before an execution plan is settled |
| [2026-08-19-2354-fold-worktrees-into-agents-template](archive/2026-08-19-2354-fold-worktrees-into-agents-template/task.md) | completed | Move `templates/worktrees/AGENTS.md` into `templates/agents/worktrees/AGENTS.md`, joining the byte-identical/portable set |
| [2026-08-19-2059-avoid-worktree-merge-branch-conflict](archive/2026-08-19-2059-avoid-worktree-merge-branch-conflict/task.md) | completed | Document a merge sequence for task worktrees that avoids `gh pr merge --delete-branch`'s local checkout conflict with `main` |
| [2026-08-19-2015-guard-against-leftover-scaffolding](archive/2026-08-19-2015-guard-against-leftover-scaffolding/task.md) | completed | Decide whether to add a mechanical check that catches leftover instructional prose, empty headings, or duplicated headings in a task package |
| [2026-08-19-1928-reconcile-live-questions](archive/2026-08-19-1928-reconcile-live-questions/task.md) | completed | Correct the README and live open-question list where accepted decisions and shipped work have made their descriptions stale |
| [2026-08-19-1619-support-claude-code](archive/2026-08-19-1619-support-claude-code/task.md) | completed | Add a Claude Code adapter so a session in this repository has `AGENTS.md`'s content without being told to read it |
| [2026-08-19-1250-decide-whether-the-task-template-earns-its-place](archive/2026-08-19-1250-decide-whether-the-task-template-earns-its-place/task.md) | completed | Decide whether `templates/task/` should be kept, changed, or dropped |
| [2026-08-18-2312-declare-who-approves-a-task](archive/2026-08-18-2312-declare-who-approves-a-task/task.md) | completed | Let a task declare that a fresh verifier's CONFIRMED verdict is sufficient to merge it |
| [2026-08-18-2250-park-agent-native-sdlc-questions](archive/2026-08-18-2250-park-agent-native-sdlc-questions/task.md) | completed | Preserve proposed agent-native SDLC and harness directions as live, neutral questions without treating the proposal as an accepted architecture or implementation plan |
| [2026-08-18-2246-make-the-final-check-verifiable](archive/2026-08-18-2246-make-the-final-check-verifiable/task.md) | completed | Decide what the final exact-head check proves when self-run |
| [2026-08-18-2053-make-the-layer-file-an-entry-point](archive/2026-08-18-2053-make-the-layer-file-an-entry-point/task.md) | completed | Make `.agents/AGENTS.md` a map of what is under it and who owns each part |
| [2026-08-18-1738-rules-for-concurrent-tasks](archive/2026-08-18-1738-rules-for-concurrent-tasks/task.md) | completed | Say what the rules mean when tasks run in parallel |
| [2026-08-18-1640-fix-index-status-precedence](archive/2026-08-18-1640-fix-index-status-precedence/task.md) | completed | Correct which file wins when the index and a task disagree |
| [2026-08-18-1544-approve-after-archival](archive/2026-08-18-1544-approve-after-archival/task.md) | completed | Move the approval gate to after the final exact-head check |
| [2026-08-18-1518-route-findings-without-an-owning-task](archive/2026-08-18-1518-route-findings-without-an-owning-task/task.md) | completed | Give a finding somewhere to go when it has no owning task |
| [2026-08-17-0126-delete-branches-on-merge](archive/2026-08-17-0126-delete-branches-on-merge/task.md) | completed | State that merging deletes the branch, so "short-lived" holds now that agents merge |
| [2026-08-17-0116-add-init-skill](archive/2026-08-17-0116-add-init-skill/task.md) | completed | Ship adoption as a skill an agent can invoke, without the skill becoming the definition of what adoption is |
| [2026-08-13-2054-let-agents-merge-after-approval](archive/2026-08-13-2054-let-agents-merge-after-approval/task.md) | completed | Allow an agent to merge a pull request once a human has approved it, and record what that changes about the gate |
| [2026-08-13-2000-separate-distribution-from-installation](archive/2026-08-13-2000-separate-distribution-from-installation/task.md) | completed | Ship a distribution, install this repository from it, and make the fact that they match a check rather than a claim |
| [2026-08-13-1838-write-the-adoption-procedure](archive/2026-08-13-1838-write-the-adoption-procedure/task.md) | completed | Describe how another repository adopts context-fold, well enough that following the description is the test |
| [2026-08-13-1619-add-convention-checks](archive/2026-08-13-1619-add-convention-checks/task.md) | completed | Enforce the repository invariants that encode decisions, on every change, instead of checking them by hand |
| [2026-08-13-1527-record-iterative-stages](archive/2026-08-13-1527-record-iterative-stages/task.md) | completed | Record that work returns to earlier stages, and state the rule where agents read it |
| [2026-08-13-1510-record-decisions-carry-history](archive/2026-08-13-1510-record-decisions-carry-history/task.md) | completed | Record that source material is not stored raw, and locate where a task-local problem becomes project-scoped |
| [2026-08-13-1447-record-learning-loop](archive/2026-08-13-1447-record-learning-loop/task.md) | completed | Record the loop the project exists to create, and preserve the designs cut to keep it cheap enough to follow |
| [2026-08-13-1439-record-methodology-before-tooling](archive/2026-08-13-1439-record-methodology-before-tooling/task.md) | completed | Record that v0 is conventions in plain files rather than software, and preserve the reasoning that produced it |
| [2026-08-13-1431-record-vendor-neutrality](archive/2026-08-13-1431-record-vendor-neutrality/task.md) | completed | Record that the model does not depend on any agent product, and preserve the alternatives that were rejected |
| [2026-08-13-1313-record-open-questions](archive/2026-08-13-1313-record-open-questions/task.md) | completed | Give the project's unresolved questions and deferred scope a home in the project layer |
| [2026-08-13-0049-record-index-order](archive/2026-08-13-0049-record-index-order/task.md) | completed | Record that the task index is ordered newest first, and state the rule in the portable tasks instructions |
| [2026-08-13-0033-record-merge-strategy](archive/2026-08-13-0033-record-merge-strategy/task.md) | completed | Record how pull requests are merged, and the pull request description convention that follows from it |
| [2026-08-13-0023-bootstrap-tasks-layer](archive/2026-08-13-0023-bootstrap-tasks-layer/task.md) | completed | Establish context-fold v0: the `.agents/` tasks layer, project-layer entry points, and decision records for what is settled |
