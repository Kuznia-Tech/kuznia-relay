# P1-T1 - 2 Spec check (2)

> Paste into the agent: `P1-T1 - 2 Spec check (2): read and follow /home/you/relay-example/kb/Workflow/Prompts/P1-T1 - 2 Spec check (2).md`

- **Rules:** `/home/you/relay-example/kb/AGENT-RULES.md` (every step)
- **Config:** `/home/you/relay-example/kb/RELAY.md`
- **Task card:** `/home/you/relay-example/kb/Workflow/Tasks/P1-T1 Version flag.md` (read first)
- **Step:** 2 Spec check (2), re-check
- **Branch:** none (read-only) · **Feature branch:** `relay/p1` · **Worktree:** throwaway, `git worktree add --detach /tmp/app-p1-t1-2-spec-check-2/wt origin/relay/p1`, removed when you finish

## Context to read
- The task card (sections **Spec** and **Findings**) and the files it links
- The requirement sources in `RELAY.md`, in precedence order
- `/home/you/relay-example/kb/Workflow/Reports/P1-T1 - 2 Spec check.md`

## Your job
1. F1 from the last round: fixed / partly / not fixed, with the Spec line as proof.
2. Only what `2 Spec fix (2)` changed (the line tagged `(F1)`): new problems only.
3. A quick end-to-end pass over the whole Spec against REQ-1.

## Rules for this step
- Don't change code.
- Findings table, IDs continuing from F2. Never fix, never offer to. Last line: `Verdict: clean` or `Verdict: fix round needed: F…`.
- First each finding of the last round (fixed / partly / not fixed, with proof). Then only what the fix round changed. Then a quick end-to-end pass.

## Report
Write `/home/you/relay-example/kb/Workflow/Reports/P1-T1 - 2 Spec check (2).md` from `/home/you/relay-example/kb/Workflow/Templates/Report.md`.
