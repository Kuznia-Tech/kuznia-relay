# Report: P1-T1 - 4 Review

- **Date:** 2026-11-06
- **Result:** done

## Summary
Reviewed `origin/relay/p1...origin/wip/p1-t1-version-flag` (3904ade). Behaviour matches the Spec and REQ-1; 6 tests pass in the throwaway worktree. The commit also adds two compiled `.pyc` files.

## Findings or changes

### Findings
| ID | Severity | Finding | Where | Suggested fix |
|---|---|---|---|---|
| F3 | should fix | Commit adds build output `__pycache__/*.pyc`, outside Spec **Files** (AGENT-RULES: "never commit build output or caches") | 3904ade, `__pycache__/` | A: `git rm -r --cached __pycache__` only. B: A plus `.gitignore` with `__pycache__/` (a file not in Spec **Files**). Recommend B |
| F4 | nit | `run()` helper and `test_version` duplicate the stdout capture | `test_greet.py:7-11`, `test_greet.py:24-28` | Later: one helper that also catches `SystemExit` |

## Design check
- AC1: match, `python3 greet.py --version` prints `greet 0.1.0`.
- AC2: match, exit status 0.
- AC3: match, CLI tests for `greet`, `greet bo`, `--shout`.

## Decisions you made
None.

## Different from the spec
None.

## Open questions / blockers
None.

## Git
```
base (branch + commit): origin/relay/p1 @ 5593eac (fetched)
  git remote get-url origin -> git@github.com:you/greet.git (matches RELAY.md)
  git remote get-url --push --all origin -> git@github.com:you/greet.git (one line, matches)
  git worktree add --detach /tmp/app-p1-t1-4-review/wt origin/wip/p1-t1-version-flag ... removed at the end
branch: origin/wip/p1-t1-version-flag @ 3904ade (detached, read-only)
commits (hash + message): none
git diff --stat (origin/relay/p1...3904ade):
 __pycache__/greet.cpython-313.pyc      | Bin 0 -> 1496 bytes
 __pycache__/test_greet.cpython-313.pyc | Bin 0 -> 3369 bytes
 greet.py                               |   1 +
 test_greet.py                          |  29 ++++++++++++++++++++++++++++-
 4 files changed, 29 insertions(+), 1 deletion(-)
push output (Build, fix round, Done): n/a
```

## Tests
`python3 -m unittest -q` at 3904ade:
```
----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK
```

## Suggested next step
`report P1-T1`, then `fix P1-T1` for F3.

Verdict: fix round needed: F3
