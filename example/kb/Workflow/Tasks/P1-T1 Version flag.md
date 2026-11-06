---
id: P1-T1
feature: P1
step: 5 Done
state: done
branch: wip/p1-t1-version-flag
merge: 585ee0e
---
# P1-T1 Version flag

Feature: [[P1 - Plan]] · Tracker: [[Board]] · Config: [[RELAY]]

**Step:** 5 Done · **Waiting on:** nobody · **Next:** none (merged 585ee0e, tag `wip/p1-t1-done`)

## Goal
Add a `--version` flag that prints `greet 0.1.0` and exits 0 (REQ-1).

## Steps
| Step | Prompt | Report | Result | Date |
|---|---|---|---|---|
| 1 Analyze | skipped | | One-line change in one file; REQ-1 gives the behaviour in full ([[Decisions]]) | 2026-11-06 |
| 2 Spec check | [[Prompts/P1-T1 - 2 Spec check]] | [[Reports/P1-T1 - 2 Spec check]] | fix round needed: F1 | 2026-11-06 |
| 2 Spec fix (2) | none (planner) | none | F1 fixed in Spec **Tests** | 2026-11-06 |
| 2 Spec check (2) | [[Prompts/P1-T1 - 2 Spec check (2)]] | [[Reports/P1-T1 - 2 Spec check (2)]] | clean; F1 verified | 2026-11-06 |
| Owner approved | | | Spec approved → 3 Build | 2026-11-06 |
| 3 Build | [[Prompts/P1-T1 - 3 Build]] | [[Reports/P1-T1 - 3 Build]] | 3904ade pushed, 6 tests OK | 2026-11-06 |
| 4 Review | [[Prompts/P1-T1 - 4 Review]] | [[Reports/P1-T1 - 4 Review]] | fix round needed: F3 | 2026-11-06 |
| 2 Spec fix (3) | none (planner) | none | F3 option B: `.gitignore` added to Spec **Files**, proof command to **Tests** (small call, [[Decisions]]) | 2026-11-06 |
| 3 Build (2) | [[Prompts/P1-T1 - 3 Build (2)]] | [[Reports/P1-T1 - 3 Build (2)]] | F3 fixed in c66916d, pushed; proof `git ls-files __pycache__` empty; 6 tests OK | 2026-11-06 |
| 4 Review (2) | [[Prompts/P1-T1 - 4 Review (2)]] | [[Reports/P1-T1 - 4 Review (2)]] | clean; F3 verified | 2026-11-06 |
| Owner approved | | | Code approved @ c66916d → 5 Done | 2026-11-06 |
| 5 Done | [[Prompts/P1-T1 - 5 Done]] | [[Reports/P1-T1 - 5 Done]] | merged 585ee0e into `relay/p1`, 6 tests OK, tagged `wip/p1-t1-done`, pushed | 2026-11-06 |

Other rows: `2 Spec fix (n)` (planner, no prompt or report), `Owner approved` (from `approve`), and each prompt run.

Step names: `1 Analyze`, `2 Spec check`, `3 Build`, `4 Review`, `5 Done`, with `(n)` for later rounds.

## Analysis summary
Skipped (see Steps).

## Spec
- **Build:** in `greet.py`, add `p.add_argument("--version", action="version", version="greet 0.1.0")` to `build_parser()`.
- **Acceptance criteria:**
  1. `greet --version` prints exactly `greet 0.1.0\n` to stdout (REQ-1 AC1).
  2. Exit status is 0 (REQ-1 AC2).
  3. `greet`, `greet NAME` and `--shout` are unchanged; existing tests pass (REQ-1 AC3).
- **Files:** `greet.py`, `test_greet.py`, `.gitignore` with `__pycache__/` (F3)
- **Tests:** a test that calls `main(["--version"])` and asserts `SystemExit` code 0 and the stdout text. Plus CLI tests for AC3: `main([])` prints `Hello, world!`, `main(["bo"])` prints `Hello, bo!`, `main(["--shout"])` prints `HELLO, WORLD!` (F1). Proof that no build output is tracked: `git ls-files __pycache__` prints nothing (F3).
- **Out of scope:** reading the version from package metadata; any other flag.

## Findings
From Spec checks and Reviews, filled in on "report". blocker / should fix → **fix**; nit → **later** ([[Improvements]]).

| ID | Found in | Severity | Finding | Decision | Fixed in | Status |
|---|---|---|---|---|---|---|
| F1 | 2 Spec check | should fix | AC3 has no CLI-level test | fix | 2 Spec fix (2) | verified |
| F2 | 2 Spec check | nit | Version string is a literal, no single source | later | | later |
| F3 | 4 Review | should fix | Commit 3904ade adds `__pycache__/*.pyc` | fix (option B, see [[Decisions]]) | 2 Spec fix (3), 3 Build (2) | verified |
| F4 | 4 Review | nit | Duplicated stdout capture in tests | later | | later |

Status: open → fixed → verified. Or: later, won't fix, blocked, reopened.

## Open questions
None.
