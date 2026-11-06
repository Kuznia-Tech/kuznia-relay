# P1-T1 - 3 Build

> Paste into the agent: `P1-T1 - 3 Build: read and follow /home/you/relay-example/kb/Workflow/Prompts/P1-T1 - 3 Build.md`

- **Rules:** `/home/you/relay-example/kb/AGENT-RULES.md` (every step)
- **Config:** `/home/you/relay-example/kb/RELAY.md`
- **Task card:** `/home/you/relay-example/kb/Workflow/Tasks/P1-T1 Version flag.md` (read first)
- **Step:** 3 Build
- **Branch:** `wip/p1-t1-version-flag` · **Feature branch:** `relay/p1` · **Worktree:** `/home/you/relay-example/app/.worktrees/p1-t1`, create it with `git -C /home/you/relay-example/app worktree add --no-track -b wip/p1-t1-version-flag /home/you/relay-example/app/.worktrees/p1-t1 origin/relay/p1`

## Context to read
- The task card (section **Spec**, approved) and the files it links
- The requirement sources in `RELAY.md`, in precedence order

## Your job
1. Create the task branch and worktree above.
2. Implement the Spec **Build** line in `greet.py`.
3. Add the tests in Spec **Tests** to `test_greet.py`.
4. Run `python3 -m unittest -q`. Commit as `[P1-T1] Add --version flag`. Push the branch to `origin`.

## Rules for this step
- Only the task branch, only the spec. Stop and report if the spec is wrong.

## Report
Write `/home/you/relay-example/kb/Workflow/Reports/P1-T1 - 3 Build.md` from `/home/you/relay-example/kb/Workflow/Templates/Report.md`.
