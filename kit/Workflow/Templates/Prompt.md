# PX-TY - N Step

> Paste into the agent: `PX-TY - N Step: read and follow <knowledge_base>/Workflow/Prompts/PX-TY - N Step.md`

All paths below are absolute: start each with the knowledge base path.

- **Rules:** `<knowledge_base>/AGENT-RULES.md` (every step)
- **Config:** `<knowledge_base>/RELAY.md`
- **Task card:** `<knowledge_base>/Workflow/Tasks/PX-TY Name.md` (read first)
- **Step:** N Step
- **Branch:** `<task branch>` · **Feature branch:** `<feature branch>` · **Worktree:** `<path>` (see "Where you work" in the rules)

## Context to read
- The task card and the files it links
- The requirement sources in `RELAY.md`, in precedence order
- (re-check, fix round) `<knowledge_base>/Workflow/Reports/<previous report>.md`

## Your job
Numbered list. One step only.

## Rules for this step
- (Analyze / Spec check / Review) Don't change code.
- (Spec check / Review) Findings table, IDs continuing from F<last>. Never fix, never offer to. Last line: `Verdict: clean` or `Verdict: fix round needed: F…`.
- (Re-check) First each finding of the last round (fixed / partly / not fixed, with proof). Then only what the fix round changed. Then a quick end-to-end pass.
- (Build fix round) Fix only F<a>-F<b>, in the existing task worktree. A failing-first test per finding, or a proof command if it isn't about behaviour. One commit: `[PX-TY] Fix F<a>-F<b>`.
- (Build) Only the task branch, only the spec. Stop and report if the spec is wrong.
- (Done) In the feature worktree: merge `--no-ff` with `[PX-TY] Merge <task branch>`, run the full Done test list, tag `<done tag>`, push branch and tag.

## Report
Write `<knowledge_base>/Workflow/Reports/PX-TY - N Step.md` from `<knowledge_base>/Workflow/Templates/Report.md`.
