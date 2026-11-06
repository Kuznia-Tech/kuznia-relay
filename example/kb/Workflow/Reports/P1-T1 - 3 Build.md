# Report: P1-T1 - 3 Build

- **Date:** 2026-11-06
- **Result:** done

## Summary
Added `--version` to `build_parser()` and four CLI tests (version and AC3). 6 tests pass. Branch pushed.

## Findings or changes
- `greet.py`: `p.add_argument("--version", action="version", version="greet 0.1.0")` in `build_parser()`.
- `test_greet.py`: helper `run(argv)`; class `CliTest` with `test_version`, `test_default_cli`, `test_name_cli`, `test_shout_cli`.

## Design check
- AC1, AC2: `test_version`.
- AC3: `test_default_cli`, `test_name_cli`, `test_shout_cli`, plus the two existing tests.

## Decisions you made
- Test helper name `run`.

## Different from the spec
None.

## Open questions / blockers
None.

## Git
```
base (branch + commit): origin/relay/p1 @ 5593eac
  git remote get-url origin -> git@github.com:you/greet.git (matches RELAY.md)
  git remote get-url --push --all origin -> git@github.com:you/greet.git (one line, matches)
  git worktree add --no-track -b wip/p1-t1-version-flag /home/you/relay-example/app/.worktrees/p1-t1 origin/relay/p1
branch: wip/p1-t1-version-flag
commits (hash + message): 3904ade [P1-T1] Add --version flag
git diff --stat:
 __pycache__/greet.cpython-313.pyc      | Bin 0 -> 1496 bytes
 __pycache__/test_greet.cpython-313.pyc | Bin 0 -> 3369 bytes
 greet.py                               |   1 +
 test_greet.py                          |  29 ++++++++++++++++++++++++++++-
 4 files changed, 29 insertions(+), 1 deletion(-)
push output (Build, fix round, Done):
$ git push -u origin wip/p1-t1-version-flag
To github.com:you/greet.git
 * [new branch]      wip/p1-t1-version-flag -> wip/p1-t1-version-flag
branch 'wip/p1-t1-version-flag' set up to track 'origin/wip/p1-t1-version-flag'.
```

## Tests
`python3 -m unittest -q`:
```
----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK
```

## Suggested next step
`report P1-T1`, then `prompt P1-T1` for 4 Review.
