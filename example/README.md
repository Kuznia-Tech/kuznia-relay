# Worked example: one task, start to Done

This folder shows one Kuznia Relay task taken through every step, with the files a real run leaves behind. The project is `greet`, a 24-line Python CLI with two tests. The requirement ([REQ-1](kb/sources/REQ-1%20version%20flag.md)) adds a `--version` flag. Task `P1-T1` skips Analyze (logged as a decision), fails its first Spec check on a missing test (F1), gets a spec fix and a clean re-check, is built, fails its first Review on committed `.pyc` files (F3), goes through a spec fix and a code fix round, passes the re-check, and is merged, tested, tagged and pushed at Done. Two nits (F2, F4) go to [Improvements](kb/Improvements.md). `kb/` is the knowledge base at the end of the run; `app/` is the code at Done. Paths such as `/home/you/relay-example/kb` and the remote `git@github.com:you/greet.git` are placeholders.

A real knowledge base also holds copies of `SPEC.md` and `AGENT-RULES.md` from the repository root; they are left out here.

## Walkthrough

Task card: [P1-T1 Version flag](kb/Workflow/Tasks/P1-T1%20Version%20flag.md) · Board: [Board](kb/Workflow/Board.md) · Plan: [P1 - Plan](kb/Implementation/P1%20-%20Plan.md) · Decisions: [Decisions](kb/Decisions.md)

| # | Step | Prompt | Report | What happened | Verdict |
|---|---|---|---|---|---|
| 1 | 1 Analyze | none | none | Skipped: one-line change, REQ-1 gives the behaviour. Logged as a to-review call | |
| 2 | 2 Spec check | [prompt](kb/Workflow/Prompts/P1-T1%20-%202%20Spec%20check.md) | [report](kb/Workflow/Reports/P1-T1%20-%202%20Spec%20check.md) | F1 (should fix): AC3 has no CLI-level test. F2 (nit): version string literal | fix round needed: F1 |
| 3 | 2 Spec fix (2) | none | none | Planner adds the AC3 CLI tests to Spec **Tests**, tagged `(F1)` | |
| 4 | 2 Spec check (2) | [prompt](kb/Workflow/Prompts/P1-T1%20-%202%20Spec%20check%20(2).md) | [report](kb/Workflow/Reports/P1-T1%20-%202%20Spec%20check%20(2).md) | F1 fixed; nothing new | clean |
| 5 | Owner approved | none | none | `approve P1-T1`: spec approved, step moves to 3 Build | |
| 6 | 3 Build | [prompt](kb/Workflow/Prompts/P1-T1%20-%203%20Build.md) | [report](kb/Workflow/Reports/P1-T1%20-%203%20Build.md) | Task branch and worktree created; `3904ade [P1-T1] Add --version flag`; 6 tests OK; pushed. The commit also includes `__pycache__/*.pyc` | |
| 7 | 4 Review | [prompt](kb/Workflow/Prompts/P1-T1%20-%204%20Review.md) | [report](kb/Workflow/Reports/P1-T1%20-%204%20Review.md) | F3 (should fix): committed `.pyc`, options A/B. F4 (nit): duplicated stdout capture | fix round needed: F3 |
| 8 | 2 Spec fix (3) | none | none | Planner picks option B (small call, to review), adds `.gitignore` to Spec **Files** and a proof command to **Tests**, tagged `(F3)` | |
| 9 | 3 Build (2) | [prompt](kb/Workflow/Prompts/P1-T1%20-%203%20Build%20(2).md) | [report](kb/Workflow/Reports/P1-T1%20-%203%20Build%20(2).md) | Head checked at 3904ade; `c66916d [P1-T1] Fix F3`; proof `git ls-files __pycache__` is empty; 6 tests OK; pushed | |
| 10 | 4 Review (2) | [prompt](kb/Workflow/Prompts/P1-T1%20-%204%20Review%20(2).md) | [report](kb/Workflow/Reports/P1-T1%20-%204%20Review%20(2).md) | F3 fixed; nothing new | clean |
| 11 | Owner approved | none | none | `approve P1-T1`: code approved, step moves to 5 Done | |
| 12 | 5 Done | [prompt](kb/Workflow/Prompts/P1-T1%20-%205%20Done.md) | [report](kb/Workflow/Reports/P1-T1%20-%205%20Done.md) | `585ee0e [P1-T1] Merge wip/p1-t1-version-flag` (`--no-ff`) on `relay/p1`; 6 tests OK; tag `wip/p1-t1-done`; branch and tag pushed. Planner sets `merge:`, ticks the Plan, updates the Board | |

After each report the Owner said `report P1-T1` and the planner updated the card, Board, Plan, Decisions and Improvements. While a step was running, the Board's "Now" row linked its prompt as `[[Prompts/P1-T1 - 3 Build]]`; the final Board has no current prompt.

## Run the app

`app/` is a plain folder at its Done state: `greet.py`, `test_greet.py` and `.gitignore`. To make it a repository and check it:

```sh
mkdir -p /home/you/relay-example
cp -R example/app /home/you/relay-example/app
cd /home/you/relay-example/app
git init -b main && git add . && git commit -m "greet at P1-T1 Done"
python3 -m unittest -q        # Ran 6 tests ... OK
python3 greet.py --version    # greet 0.1.0
```

To run the task yourself from the start, first take the app back to its starting state: remove the `--version` line from `greet.py`, the `run` helper, the `CliTest` class and the `contextlib`, `io` and `main` imports from `test_greet.py`, and `.gitignore`. Commit that on `main`, push it to your remote, create `relay/p1` and its worktree as listed in [RELAY.md](kb/RELAY.md), and start with `plan P1`. Your hashes will differ from the ones here.
