# P1-T1 - 2 Spec check

> Paste into the agent: `P1-T1 - 2 Spec check: read and follow /home/you/relay-example/kb/Workflow/Prompts/P1-T1 - 2 Spec check.md`

- **Rules:** `/home/you/relay-example/kb/AGENT-RULES.md` (every step)
- **Config:** `/home/you/relay-example/kb/RELAY.md`
- **Task card:** `/home/you/relay-example/kb/Workflow/Tasks/P1-T1 Version flag.md` (read first)
- **Step:** 2 Spec check
- **Branch:** none (read-only) · **Feature branch:** `relay/p1` · **Worktree:** throwaway, `git worktree add --detach /tmp/app-p1-t1-2-spec-check/wt origin/relay/p1`, removed when you finish

## Context to read
- The task card (section **Spec**) and the files it links
- The requirement sources in `RELAY.md`, in precedence order
- `greet.py` and `test_greet.py` on `relay/p1`

## Your job
1. Check every Spec line against REQ-1 and the code: buildable, complete, testable, consistent.
2. Check that each acceptance criterion maps to a test in **Tests**.
3. Log findings. The card has none yet, so IDs start at F1.

## Rules for this step
- Don't change code.
- Findings table, IDs starting at F1. Never fix, never offer to. Last line: `Verdict: clean` or `Verdict: fix round needed: F…`.

## Report
Write `/home/you/relay-example/kb/Workflow/Reports/P1-T1 - 2 Spec check.md` from `/home/you/relay-example/kb/Workflow/Templates/Report.md`.
