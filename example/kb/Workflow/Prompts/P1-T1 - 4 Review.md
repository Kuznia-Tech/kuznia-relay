# P1-T1 - 4 Review

> Paste into the agent: `P1-T1 - 4 Review: read and follow /home/you/relay-example/kb/Workflow/Prompts/P1-T1 - 4 Review.md`

- **Rules:** `/home/you/relay-example/kb/AGENT-RULES.md` (every step)
- **Config:** `/home/you/relay-example/kb/RELAY.md`
- **Task card:** `/home/you/relay-example/kb/Workflow/Tasks/P1-T1 Version flag.md` (read first)
- **Step:** 4 Review
- **Branch:** `wip/p1-t1-version-flag` @ `3904ade` (read-only) · **Feature branch:** `relay/p1` · **Worktree:** throwaway, `git worktree add --detach /tmp/app-p1-t1-4-review/wt origin/wip/p1-t1-version-flag`, removed when you finish

## Context to read
- The task card (sections **Spec** and **Findings**) and the files it links
- The requirement sources in `RELAY.md`, in precedence order
- `/home/you/relay-example/kb/Workflow/Reports/P1-T1 - 3 Build.md`

## Your job
1. Review `git diff origin/relay/p1...origin/wip/p1-t1-version-flag` against the Spec and REQ-1.
2. Run `python3 -m unittest -q` yourself in the throwaway worktree.
3. Log findings. IDs continue from F2.

## Rules for this step
- Don't change code.
- Findings table, IDs continuing from F2. Never fix, never offer to. Last line: `Verdict: clean` or `Verdict: fix round needed: F…`.

## Report
Write `/home/you/relay-example/kb/Workflow/Reports/P1-T1 - 4 Review.md` from `/home/you/relay-example/kb/Workflow/Templates/Report.md`.
