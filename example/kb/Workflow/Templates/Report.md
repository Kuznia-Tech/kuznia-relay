# Report: PX-TY - N Step

- **Date:**
- **Result:** done / partly done / blocked

## Summary
Three lines max: what you did and what came out of it.

## Findings or changes
- Analyze: answer each question from the prompt, with `file:line` references.
- Build: what changed, file by file.
- Build fix round: one row per finding ID: what changed, and the test that fails on the old code (or the proof command for a finding that isn't about behaviour).
- Done: merge hash, Done tag, full test output, push output.
- Spec check / Review: the two tables below. Don't fix anything and don't offer to.

### Previous findings (re-check only)
| ID | Result | Proof |
|---|---|---|
| F3 | fixed / partly / not fixed | test name, or spec line |

### Findings
Most serious first. Continue the IDs from the task card (never reuse one).

| ID | Severity | Finding | Where | Suggested fix |
|---|---|---|---|---|
| F7 | blocker / should fix / nit | one line | `file:line` or spec step | one line; options A/B/C if there is a real choice |

## Design check
One line per point: match, conflict (with what), or gap (not in the sources). If `RELAY.md` has a `ui_rule`: the existing component used and the screen it copies (`file:line`), or what breaks the rule.

## Decisions you made

## Different from the spec
"None" if nothing.

## Open questions / blockers

## Git
```
remote check (fetch and push URLs = allowed_remote):
base (branch + commit):
worktree:
branch:
commits (hash + message):
git diff --stat:
push output (Build, fix round, Done):
```

## Tests
Commands you ran and their result (pass/fail counts). Read-only steps may write "not run (read-only step)".

## Suggested next step

<!-- Spec check / Review only: replace this comment with the verdict as the file's last line, either `Verdict: clean` or `Verdict: fix round needed: F3, F5`. -->
