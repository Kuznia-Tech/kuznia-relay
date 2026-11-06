# P1-T1 - 4 Review (2)

> Paste into the agent: `P1-T1 - 4 Review (2): read and follow /home/you/relay-example/kb/Workflow/Prompts/P1-T1 - 4 Review (2).md`

- **Rules:** `/home/you/relay-example/kb/AGENT-RULES.md` (every step)
- **Config:** `/home/you/relay-example/kb/RELAY.md`
- **Task card:** `/home/you/relay-example/kb/Workflow/Tasks/P1-T1 Version flag.md` (read first)
- **Step:** 4 Review (2), re-check
- **Branch:** `wip/p1-t1-version-flag` @ `c66916d` (read-only) · **Feature branch:** `relay/p1` · **Worktree:** throwaway, `git worktree add --detach /tmp/app-p1-t1-4-review-2/wt origin/wip/p1-t1-version-flag`, removed when you finish

## Context to read
- The task card (sections **Spec** and **Findings**) and the files it links
- The requirement sources in `RELAY.md`, in precedence order
- `/home/you/relay-example/kb/Workflow/Reports/P1-T1 - 4 Review.md` (the previous round)
- `/home/you/relay-example/kb/Workflow/Reports/P1-T1 - 3 Build (2).md`

## Your job
1. F3 from the last round: fixed / partly / not fixed, with proof (re-run `git ls-files __pycache__`).
2. Only what `3 Build (2)` changed (`git diff 3904ade..c66916d`): new problems only.
3. A quick end-to-end pass: `git diff origin/relay/p1...origin/wip/p1-t1-version-flag` against the Spec and REQ-1, and `python3 -m unittest -q` in the throwaway worktree.

## Rules for this step
- Don't change code.
- Findings table, IDs continuing from F4. Never fix, never offer to. Last line: `Verdict: clean` or `Verdict: fix round needed: F…`.
- First each finding of the last round (fixed / partly / not fixed, with proof). Then only what the fix round changed. Then a quick end-to-end pass.

## Report
Write `/home/you/relay-example/kb/Workflow/Reports/P1-T1 - 4 Review (2).md` from `/home/you/relay-example/kb/Workflow/Templates/Report.md`.
