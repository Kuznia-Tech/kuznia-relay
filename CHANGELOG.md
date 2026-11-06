# Changelog

Spec versions. File and folder names are a contract (SPEC section 4), so any change to them is listed here.

## 1.2 (2026-11-06)
From the first external review (Codex and Claude dry runs).

**Naming changes (tools must update):**
- Board "Now" links include the folder: `[[Prompts/P1-T2 - 3 Build]]`.
- The check verdict is the report's last line, `Verdict: clean` or `Verdict: fix round needed: F3, F5`; the header field is gone.
- Step names are fixed: `1 Analyze`, `2 Spec check`, `3 Build`, `4 Review`, `5 Done`. A spec fix is a Steps-table row `2 Spec fix (n)`, with no prompt or report.
- Task branches and Done tags cover sub-tasks (`wip/p1-t7c-<slug>`); the slug rule is defined.
- Done merge commits start with `[<TaskID>] Merge`. Finding ranges use an ASCII hyphen (`F5-F9`).
- `RELAY.md` config lives in YAML front matter; new keys `base`, `worktrees`, `allowed_remote.url`, `test_commands.done`.
- Paste line: `P1-T2 - 3 Build: read and follow <path>`.

**Rules:**
- Done has a prompt and a report; the planner records it on `report`. `approve` writes a Steps-table row.
- New section 5.3 on branches and worktrees; the commands are in `AGENT-RULES.md`.
- Fix rounds: a proof command instead of a test for findings that aren't about behaviour; new files go through a spec fix first.
- Prompts use absolute paths; agents check the remote URL against `allowed_remote`.
- New `plan <F>` command and Plan and Improvements templates.
- The planner may read the repo; agents decide only things that don't change behaviour; the Owner's review of a decision goes through the planner.
- The round limit also stops when the same finding is reopened twice.
- `SPEC.md` and `AGENT-RULES.md` are copied into the knowledge base.
- The first Build creates the task branch with `--no-track` and pushes it with `-u`; every push names its target.
- Feature delivery: the Owner opens the feature pull request and cleans up worktrees and branches.
- The remote check covers push URLs too. Code approval names the reviewed commit, and Done merges exactly that commit.
- Scratch folders start with the repo folder name. Reports are published by renaming a temp file. A blocked report keeps the task on its step.
- QA failures become a new corrective task; Done tasks are never reopened.
- The planner's task lifecycle (who writes the Spec, when steps move, Analyze skips decided at `plan`) is in `kit/AGENTS.md`.
- Extensions may add task ID forms, steps and config keys.

## 1.1 (2026-11-05)
- Coordinator, morning summaries, machines, load limits and multi-planner locks moved to `extensions/coordinator.md`.
- QA and the Validator role moved to `extensions/qa.md`; special task IDs (`P1-QA`) are defined there.
- Building tools moved to `docs/tools.md`.
- `Status.md` folded into `Board.md`; `<F> - Log.md` folded into the task card and the Plan; `Decisions to review.md` merged into `Decisions.md`; `Messages.md` removed.
- Task IDs allow one sub-level (`P1-T7c`, not `P1-T7c2a`); free-text round qualifiers removed.
- Source precedence is one ranked list in `RELAY.md`; the agency-specific default list and the UI design rules are no longer in the spec (`ui_rule` stays as an optional config key).
- Rules for agents live only in `AGENT-RULES.md`.
- The report contract and project config point to their templates instead of repeating them; the state diagram is replaced by the rules it carried.
- Links may be plain Markdown, except the Board "Now" table.
- "Kuznia" is spelled without the ź in English text.

## 1.0 (2026-11-05)
- First version: spec, agent rules, templates.
