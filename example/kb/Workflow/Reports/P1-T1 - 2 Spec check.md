# Report: P1-T1 - 2 Spec check

- **Date:** 2026-11-06
- **Result:** done

## Summary
Checked the Spec against REQ-1 and `greet.py` on `relay/p1`. The Build line is correct: argparse `action="version"` prints `greet 0.1.0\n` to stdout and exits 0 (probed in a scratch script). AC3 has no CLI-level test.

## Findings or changes

### Findings
| ID | Severity | Finding | Where | Suggested fix |
|---|---|---|---|---|
| F1 | should fix | AC3 (`greet`, `greet NAME`, `--shout` unchanged) has no CLI-level test; existing tests call `greet()` directly, so a broken `build_parser()` would still pass | Spec **Tests**; `test_greet.py:6-10` | Add to **Tests**: `main([])`, `main(["bo"])`, `main(["--shout"])` print the expected lines |
| F2 | nit | Version string is a literal in `build_parser()`; no single source if a second place ever needs it | Spec **Build** | Later: module-level `__version__` |

## Design check
- AC1: match (`greet 0.1.0\n` on stdout, probed).
- AC2: match (`SystemExit(0)` from argparse).
- AC3: gap in tests (F1).

## Decisions you made
- Probe script in `/tmp/app-p1-t1-2-spec-check/probe.py`, outside the worktree.

## Different from the spec
None.

## Open questions / blockers
None.

## Git
```
base (branch + commit): origin/relay/p1 @ 5593eac, equal to relay/p1 after fetch
  git remote get-url origin -> git@github.com:you/greet.git (matches RELAY.md)
  git remote get-url --push --all origin -> git@github.com:you/greet.git (one line, matches)
  git worktree add --detach /tmp/app-p1-t1-2-spec-check/wt origin/relay/p1 ... removed at the end
branch: none (detached, read-only)
commits (hash + message): none
git diff --stat: (empty)
push output (Build, fix round, Done): n/a
```

## Tests
`python3 -m unittest -q` at 5593eac:
```
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

## Suggested next step
`report P1-T1`, then `fix P1-T1` (spec fix for F1).

Verdict: fix round needed: F1
