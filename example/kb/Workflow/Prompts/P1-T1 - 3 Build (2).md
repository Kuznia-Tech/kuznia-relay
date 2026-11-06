# P1-T1 - 3 Build (2)

> Paste into the agent: `P1-T1 - 3 Build (2): read and follow /home/you/relay-example/kb/Workflow/Prompts/P1-T1 - 3 Build (2).md`

- **Rules:** `/home/you/relay-example/kb/AGENT-RULES.md` (every step)
- **Config:** `/home/you/relay-example/kb/RELAY.md`
- **Task card:** `/home/you/relay-example/kb/Workflow/Tasks/P1-T1 Version flag.md` (read first)
- **Step:** 3 Build (2), fix round
- **Branch:** `wip/p1-t1-version-flag` · **Feature branch:** `relay/p1` · **Worktree:** `/home/you/relay-example/app/.worktrees/p1-t1` (exists; its head must be `3904ade`, the last commit in the `3 Build` report)

## Context to read
- The task card (sections **Spec** and **Findings**; Spec lines tagged `(F3)`) and the files it links
- The requirement sources in `RELAY.md`, in precedence order
- `/home/you/relay-example/kb/Workflow/Reports/P1-T1 - 4 Review.md` (F3)
- `/home/you/relay-example/kb/Decisions.md` (F3: option B)

## Your job
1. Check the worktree head equals `3904ade` and matches `origin/wip/p1-t1-version-flag`. If not, stop and report.
2. Fix F3 with option B: untrack `__pycache__/` and add `.gitignore` containing `__pycache__/`.
3. F3 isn't about behaviour: instead of a test, paste the output of `git ls-files __pycache__` before and after the fix.
4. Run `python3 -m unittest -q`. One commit: `[P1-T1] Fix F3`. Push.

## Rules for this step
- Fix only F3, in the existing task worktree. A proof command, since F3 isn't about behaviour. One commit: `[P1-T1] Fix F3`.

## Report
Write `/home/you/relay-example/kb/Workflow/Reports/P1-T1 - 3 Build (2).md` from `/home/you/relay-example/kb/Workflow/Templates/Report.md`.
