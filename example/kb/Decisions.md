# Decisions

Dated log of decisions and answers, newest first, each with its reason. Single writer: the planner.

Calls made without stopping for the Owner (decision rule: SPEC section 7.1) are marked **to review**. The Owner tells the planner ✅ ok or ❌ change (+ what) for each; the planner fills **Review**. A change becomes a finding on the task.

## 2026-11-06: P1-T1 Version flag
| Question | Options | Picked | Why | Who | Review |
|---|---|---|---|---|---|
| F3: how to remove the committed `.pyc` files | A: untrack only / B: untrack and add `.gitignore` with `__pycache__/` | B | Stops it from happening again; one-line file, no behaviour change. Needs `.gitignore` in Spec **Files**, so `2 Spec fix (3)` before the fix round (SPEC 6.3) | Planner (to review) | ✅ ok |
| Skip 1 Analyze? | A: skip / B: run | A | One-line change in one file; REQ-1 gives the behaviour in full | Planner (to review) | ✅ ok |
