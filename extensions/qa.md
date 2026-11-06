# Extension: QA

Optional. Black-box QA on the finished feature branch before hand-off, on top of the core loop (`SPEC.md`).

**Validator:** an agent on a *different model* from the one whose work it checks. It re-checks evidence and verdicts, and never changes code, configuration or other reports.

QA is a task of its own, named `<F>-QA[n]` (`P1-QA`, `P1-QA2`), with five steps:

| # | Step | Output |
|---|---|---|
| 1 | **Scenarios** | Numbered scenarios grouped by area, each with priority, preconditions, steps, expected result and source (AC, decision) |
| 2 | **Env** | A shared, seeded test app from a scratch checkout at the exact commit: users per role, named test objects, ports, start/stop scripts |
| 3 | **Run** (per group, in parallel within machine limits) | Per scenario: verdict, evidence (screenshots, API status and body), notes |
| 4 | **Validate** | A different model re-checks every non-Pass and at least one in three Passes, opening every screenshot it cites |
| 5 | **Summary** | Counts, confirmed fails restated (expected vs actual, severity), PR screenshots |

**Verdicts:** `Pass` · `Fail` · `Deviation` (our documented decision differs from the requirement; **never** a Pass) · `Known` (a listed, accepted limitation) · `Blocked` · `Scenario issue`.

Expected results come only from the requirement sources. QA MUST NOT fix anything: confirmed fails become a new corrective task (`new task`, its own ID, branch and Done tag) that goes through the normal steps. Done tasks are never reopened.

If `source_precedence` in `RELAY.md` puts the existing codebase above a requirement, every requirement it overrides is listed as a Deviation.

## Lessons

| Rule | Why |
|---|---|
| Different model for validation | Same-model checks tend to agree with their own blind spots |
| A Deviation is never a Pass | Otherwise our own decisions quietly replace client requirements in sign-off |
