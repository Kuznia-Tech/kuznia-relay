# Report: P1-T1 - 3 Build (2)

- **Date:** 2026-11-06
- **Result:** done

## Summary
Fixed F3 with option B: untracked `__pycache__/` and added `.gitignore`. One commit, pushed. 6 tests pass.

## Findings or changes
| ID | What changed | Test that fails on the old code, or proof command |
|---|---|---|
| F3 | `git rm -r --cached __pycache__`; new `.gitignore` with `__pycache__/` | Not about behaviour, so a proof command: `git ls-files __pycache__` lists two files at 3904ade and nothing at c66916d (output below) |

Proof:
```
$ git ls-files __pycache__        # before, at 3904ade
__pycache__/greet.cpython-313.pyc
__pycache__/test_greet.cpython-313.pyc
$ git ls-files __pycache__        # after, at c66916d
$
```

## Design check
No change to behaviour.

## Decisions you made
None.

## Different from the spec
None (Spec **Files** lists `.gitignore` since `2 Spec fix (3)`).

## Open questions / blockers
None.

## Git
```
base (branch + commit): wip/p1-t1-version-flag @ 3904ade = origin/wip/p1-t1-version-flag = last commit in the 3 Build report
  git remote get-url origin -> git@github.com:you/greet.git (matches RELAY.md)
  git remote get-url --push --all origin -> git@github.com:you/greet.git (one line, matches)
  worktree: /home/you/relay-example/app/.worktrees/p1-t1 (reused)
branch: wip/p1-t1-version-flag
commits (hash + message): c66916d [P1-T1] Fix F3
git diff --stat:
 .gitignore                             |   1 +
 __pycache__/greet.cpython-313.pyc      | Bin 1496 -> 0 bytes
 __pycache__/test_greet.cpython-313.pyc | Bin 3369 -> 0 bytes
 3 files changed, 1 insertion(+)
push output (Build, fix round, Done):
$ git push origin wip/p1-t1-version-flag
To github.com:you/greet.git
   3904ade..c66916d  wip/p1-t1-version-flag -> wip/p1-t1-version-flag
```

## Tests
`python3 -m unittest -q`:
```
----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK
```

## Suggested next step
`report P1-T1`, then `prompt P1-T1` for 4 Review (2).
