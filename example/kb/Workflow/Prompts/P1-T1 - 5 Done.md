# P1-T1 - 5 Done

> Paste into the agent: `P1-T1 - 5 Done: read and follow /home/you/relay-example/kb/Workflow/Prompts/P1-T1 - 5 Done.md`

- **Rules:** `/home/you/relay-example/kb/AGENT-RULES.md` (every step)
- **Config:** `/home/you/relay-example/kb/RELAY.md`
- **Task card:** `/home/you/relay-example/kb/Workflow/Tasks/P1-T1 Version flag.md` (read first)
- **Step:** 5 Done
- **Branch:** `wip/p1-t1-version-flag` · **Approved commit:** `c66916d` · **Feature branch:** `relay/p1` · **Worktree:** `/home/you/relay-example/app/.worktrees/p1` (the feature worktree)

## Context to read
- The task card (Steps: code approved) and the files it links
- `/home/you/relay-example/kb/Workflow/Reports/P1-T1 - 4 Review (2).md`

## Your job
1. In the feature worktree, fetch and check `relay/p1` equals `origin/relay/p1` and `origin/wip/p1-t1-version-flag` is at `c66916d`.
2. `git merge --no-ff -m "[P1-T1] Merge wip/p1-t1-version-flag" c66916d`
3. Run the full Done test list from `RELAY.md`: `python3 -m unittest -q`.
4. Tag the merge commit `wip/p1-t1-done`.
5. `git push origin relay/p1 wip/p1-t1-done`

## Rules for this step
- In the feature worktree: merge `--no-ff` with `[P1-T1] Merge wip/p1-t1-version-flag`, run the full Done test list, tag `wip/p1-t1-done`, push branch and tag.
- A merge conflict or a red suite after the merge: stop and report, don't push.
- Keep the task branch.

## Report
Write `/home/you/relay-example/kb/Workflow/Reports/P1-T1 - 5 Done.md` from `/home/you/relay-example/kb/Workflow/Templates/Report.md`.
