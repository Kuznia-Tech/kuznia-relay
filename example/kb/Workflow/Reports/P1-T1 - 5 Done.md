# Report: P1-T1 - 5 Done

- **Date:** 2026-11-06
- **Result:** done

## Summary
Merged `wip/p1-t1-version-flag` into `relay/p1` with `--no-ff` as 585ee0e. Full Done test list passes (6 tests). Tagged `wip/p1-t1-done`; branch and tag pushed.

## Findings or changes
- **Merge hash:** 585ee0e `[P1-T1] Merge wip/p1-t1-version-flag`
- **Done tag:** `wip/p1-t1-done` on 585ee0e
- **Test output and push output:** see Tests and Git below.
- Task branch `wip/p1-t1-version-flag` kept.

## Design check
No change since `4 Review (2)`.

## Decisions you made
None.

## Different from the spec
None.

## Open questions / blockers
None.

## Git
```
base (branch + commit): relay/p1 @ 5593eac = origin/relay/p1 (fetched); origin/wip/p1-t1-version-flag @ c66916d
  git remote get-url origin -> git@github.com:you/greet.git (matches RELAY.md)
  git remote get-url --push --all origin -> git@github.com:you/greet.git (one line, matches)
  worktree: /home/you/relay-example/app/.worktrees/p1 (feature worktree)
branch: relay/p1
commits (hash + message): 585ee0e [P1-T1] Merge wip/p1-t1-version-flag
$ git merge --no-ff -m "[P1-T1] Merge wip/p1-t1-version-flag" c66916d
Merge made by the 'ort' strategy.
 .gitignore    |  1 +
 greet.py      |  1 +
 test_greet.py | 29 ++++++++++++++++++++++++++++-
 3 files changed, 30 insertions(+), 1 deletion(-)
 create mode 100644 .gitignore
$ git log --oneline --graph -4
*   585ee0e [P1-T1] Merge wip/p1-t1-version-flag
|\
| * c66916d [P1-T1] Fix F3
| * 3904ade [P1-T1] Add --version flag
|/
* 5593eac Initial greet CLI
$ git tag wip/p1-t1-done
push output (Build, fix round, Done):
$ git push origin relay/p1 wip/p1-t1-done
To github.com:you/greet.git
   5593eac..585ee0e  relay/p1 -> relay/p1
 * [new tag]         wip/p1-t1-done -> wip/p1-t1-done
```

## Tests
Full Done list from `RELAY.md`, `python3 -m unittest -q` at 585ee0e:
```
----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK
```

## Suggested next step
`report P1-T1`: set `merge: 585ee0e`, tick the Plan, update the Board.
