# Extension: Coordinator

Optional. Add it when the core loop (`SPEC.md`) feels routine and you want it to run without you, for example overnight.

**Coordinator:** a long-running LLM session that drives the loop for the Owner. It sends commands to planners, starts agents, waits for reports, and writes morning summaries. It never edits code, task cards, Board, Plan or Decisions, and never passes a stop point (`SPEC.md` section 7.2). At most one coordinator per feature.

## 1. Loop, per task
1. Find or start the task's planner session.
2. Send the planner the next command (`prompt`, `report`, `fix`, `approve`). Answer small questions in the same message under the decision rule.
3. Take the paste line from the reply and start a **fresh** agent session, titled with the step (`P1-T23 - 4 Review`).
4. When the report exists **and is newer than the step's start**, send `report <task>` to the planner. Back to 2.
5. At a stop point, write the task's summary and move to the next task in the kickoff list that doesn't wait on this one.
6. When no task can move, write the last summaries and end with a three-line status.

## 2. Kickoff and delegation
The kickoff names the tasks in order and whether the coordinator may run **Done** (`Done: yes|no`). The Owner MAY also delegate Spec and code approval ("approve when a check is clean"). The planner logs each delegated approval in `Decisions.md`, marked to review (who: Coordinator). Client questions, scope changes and requirement changes still stop that task; the coordinator moves to another.

## 3. Morning summaries
One file per task in `Workflow/Summaries/<TaskID> - Summary.md` (template: `extensions/Summary-template.md`), newest section on top, short enough to read over coffee:
- **Owner:** what to do, first (or "nothing").
- **Ran:** one line per step.
- **Decided without you:** one line each, linking `Decisions.md`.
- **Know this:** surprises, risks, open items before delivery.
- **Next** and **Git** (branch @ hash, pushed; merge hash and tag if Done).

The coordinator is the only writer of summaries.

## 4. Load, machines and models
- One Build, Review or Done per coordinator at a time. Read-only steps MAY run alongside it when the machine has room (free memory and load checked first).
- Steps MAY run on different models. A **review or validation SHOULD run on a different model** from the one that produced the work.
- Add a `machines` key to `RELAY.md`: where agents run and their limits, e.g. "≤ 3 steps at once; ≥ 4 GB free before starting one".

## 5. Several planners
With one planner per task or feature, planners of different features edit the same Board and `Decisions.md`. Only one planner turn runs at a time, under a file lock (e.g. wrap planner messages in `flock`).

## Lessons

| Rule | Why |
|---|---|
| Wait for a report **newer than the step's start**, not for the file to exist | Re-runs of a step find the previous report and look finished |
| Check the report file, not only the agent's status | Agents sometimes end their turn with "the tests will notify me" and write nothing. After 45 idle minutes, tell them: "Write your report now with the results you have." |
| One planner turn at a time, under a file lock | Planners of different features edit the same Board, Plan and Decisions |
| Use session IDs exactly as the tool prints them | Bare IDs pointed at sessions that "no longer exist" |
