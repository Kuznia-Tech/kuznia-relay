# Kuznia Relay: a gated workflow for AI-agent software delivery

**Specification, version 1.2** · 2026-11-06

Kuznia Relay is a way to deliver real software changes with AI coding agents while one human engineer keeps control. Work moves between short-lived agents like a baton. Every agent reads its instructions from a shared knowledge base, does one step, and writes a report back. Nothing important lives in a chat window.

This document and `AGENT-RULES.md` are normative. The words **MUST**, **MUST NOT**, **SHOULD** and **MAY** have their usual meaning (RFC 2119). A team, or a tool, that follows every MUST is Kuznia Relay-compliant. Project-specific values (branch names, test commands, the order of requirement sources) live in a project config file, not in this spec (section 10).

Optional extensions: [coordinator](https://github.com/Kuznia-Tech/kuznia-relay/blob/main/extensions/coordinator.md) (runs the loop for you, e.g. overnight) and [QA](https://github.com/Kuznia-Tech/kuznia-relay/blob/main/extensions/qa.md) (black-box QA before hand-off).

---

## 1. Principles

1. **The knowledge base is the state.** Task cards, prompts, reports and decisions are files. Any agent, any machine, any day can pick up the work by reading them. Chat history is never the source of truth.
2. **One step per agent, fresh context per step.** An agent that reviews code never wrote it. An agent that checks a spec never wrote it.
3. **Checks find, fix rounds fix.** A check never changes what it checks. Fixing is always a separate, scoped round, followed by a re-check.
4. **Evidence over claims.** Reports carry real command output: git hashes, diff stats, test commands and counts, screenshots. The status of the project is rebuilt from that evidence, not from what an agent says.
5. **Small calls are decided, big calls stop.** Technical choices with a clear recommended option are made and logged, so work never waits on trivia. Scope, requirements and approvals stop for the human.
6. **Deliver first, improve later.** Blockers and real problems are fixed before a task is done. Polish goes to a backlog and the task moves on.
7. **Requirements have an explicit order.** When sources disagree, a written precedence list settles it. When it doesn't, the agent keeps current behaviour and reports the conflict instead of choosing.
8. **Fit the codebase.** Agents build from the components and patterns that already exist in the target codebase.

---

## 2. Roles

| Role | Who | Does | Never does |
|---|---|---|---|
| **Owner** | The human engineer (one per project) | Sets up the repo and feature branches, starts agents, approves specs and code, makes scope and requirement calls | Hand-edits the step history of a task card |
| **Planner** | An LLM session that writes the knowledge base and MAY read the code repository | Writes plans, specs, prompts; reads reports; updates task cards, Board, Plan, Decisions, Improvements | Changes the code repository; runs agents |
| **Agent** | A fresh coding-agent session per step | Reads the prompt and the files it links, does exactly one step, writes one report | Edits any knowledge-base file except its own report; pushes outside the allowed remote; opens pull requests |

A project MUST have exactly one Owner. It has one planner, unless the coordinator extension is used (several planners, one coordinator per feature).

---

## 3. Knowledge base layout

The knowledge base is a folder of Markdown files, kept outside the code repo. It SHOULD be its own git repository that the Owner commits (or a synced folder), so every machine sees the same state. Links MAY be plain Markdown or wiki-style `[[links]]` (Obsidian works well), except where section 4 says otherwise. It MUST contain:

```
<project>/
├── RELAY.md                  # this project's config (section 10)
├── SPEC.md, AGENT-RULES.md   # copies of this spec and the agent rules
├── sources/                  # requirement inputs: read-only for everyone but the Owner
├── Decisions.md              # dated log of decisions and answers, newest first; calls to review are marked
├── Improvements.md           # nits and polish for after delivery
├── Implementation/
│   └── <F> - Plan.md         # goal, approach, open questions, task list (ticked with merge hash at Done)
└── Workflow/
    ├── Board.md              # where every task is, what it waits on, blockers, next step
    ├── Tasks/                # one card per task, with its step history
    ├── Prompts/              # written by the planner
    ├── Reports/              # written by agents
    └── Templates/
```

### 3.1 Single writers

| File | Writer |
|---|---|
| Task cards, Board, Plan, Decisions, Improvements | Planner |
| Reports | The agent that ran the step |
| `sources/`, `RELAY.md` | The Owner |

---

## 4. Naming

These names are a contract: tools parse them.

| Thing | Grammar | Example |
|---|---|---|
| Feature | `<F>` = `P` + number | `P1` |
| Task ID | `<F>-T<n>[<letter>]` · one sub-level, for a task split out of `T<n>` | `P1-T7`, `P1-T7c` |
| Step | `<#> <Step>`, `<Step>` one of `Analyze`, `Spec check`, `Build`, `Review`, `Done` | `2 Spec check` |
| Task card | `Workflow/Tasks/<TaskID> <Title>.md` | `Tasks/P1-T2 CSV parser.md` |
| Prompt | `Workflow/Prompts/<TaskID> - <Step>[ (<n>)].md` | `Prompts/P1-T2 - 3 Build (2).md` |
| Report | Same base name as its prompt, in `Workflow/Reports/` | `Reports/P1-T2 - 3 Build (2).md` |
| Finding | `F<n>`, per task, never reused; cross-reference as `<TaskID> F<n>` | `P1-T14 F3` |
| Feature branch | from config, e.g. `feat/<slug>` | `feat/csv-export` |
| Task branch | `<prefix>/<task id lower-case>-<slug>`; slug = title in lower case, words joined by `-` | `wip/p1-t7c-csv-parser` |
| Commit message | starts with `[<TaskID>]`; fix rounds `[<TaskID>] Fix F5-F9`; Done `[<TaskID>] Merge <task branch>` | `[P1-T2] Fix F5-F9` |
| Done tag | `<prefix>/<task id lower-case>-done` on the merge commit | `wip/p1-t2-done` |

**Round numbers.** The first run of a step has no number. Later runs add `(2)`, `(3)`… A fix round and the re-check that follows it **share a number**: `3 Build (2)` fixes what `4 Review` found, and `4 Review (2)` re-checks it. A spec fix has no prompt or report; it is a row `2 Spec fix (n)` in the card's Steps table, numbered as the next run of step 2.

**Prompt and report links** include the folder (`[[Prompts/P1-T2 - 3 Build]]`, `[[Reports/P1-T2 - 3 Build]]`), so a prompt never resolves to the report of the same name. On the Board's "Now" table this is a MUST: tools find the current prompt there.

**Extensions** MAY define extra task ID forms and steps (e.g. `P1-QA`).

---

## 5. The five steps

Every task goes through five steps. The current step is shown at the top of the task card (`step:`) and on the Board.

| # | Step | Who | Output | Exit condition |
|---|---|---|---|---|
| 1 | **Analyze** | Agent, read-only | Answers to the prompt's questions with `file:line` references | Questions answered, or handed to the Owner |
| 2 | **Spec check** | Planner writes the spec, an agent checks it, Owner approves | Spec in the task card; check report | Check is clean (section 6) **and** Owner approves |
| 3 | **Build** | Agent | Commits on the task branch; build report | Tests pass; report written; branch pushed |
| 4 | **Review** | Fresh agent (findings only) + Owner | Review report | Check is clean **and** Owner approves the code |
| 5 | **Done** | Agent or Owner runs the Done prompt; planner records it | Task merged into the feature branch; Done report | Merged, feature tests pass, tagged, pushed; card, Board and Plan updated |

### 5.1 Moving between steps
- **Analyze** MAY be skipped for a small task; the card says why.
- If Build finds the spec wrong, the agent stops and reports it; on `report` the planner logs it as a finding ("found in 3 Build") and runs `2 Spec fix`.
- A task that needs an outside answer is **Blocked** until the answer is logged, then returns to its step.
- A report marked `blocked` or `partly done` keeps the task on its step. The Owner chooses: run the step again (next round, same worktree) or stop the task.
- A task card's `state` field is one of `active`, `blocked`, `parked`, `done`, `cancelled`.

### 5.2 Done, in order
After code approval the planner writes the `5 Done` prompt. Whoever runs it:
1. Checks the remote task branch is still at the approved commit, then merges that commit into the feature branch with `--no-ff` and the Done commit message, in the feature worktree. If the branch moved, it stops: the new code needs a review.
2. Runs the feature's full test list there, not a subset. A file that times out is re-run alone before it counts as a failure.
3. Tags the merge commit with the Done tag and pushes the feature branch and the tag to the allowed remote.
4. Writes the Done report: merge hash, test output, push output.

On `report`, the planner writes the merge hash into the card (`merge:`) and the Board, and ticks the task in the Plan.

**Delivery.** When every task of a feature is Done, the Owner opens the pull request from the feature branch to `base` (agents never do), then removes the task worktrees and branches.

### 5.3 Branches and worktrees
- The Owner creates each feature branch, pushes it, and adds its worktree (listed in `RELAY.md`).
- The first Build creates the task branch from the remote feature branch, in its own worktree. Fix rounds reuse that worktree and first check its head matches the last Build report.
- Read-only steps (Analyze, Spec check, Review) work in a throwaway detached worktree inside their scratch folder and remove it when done.
- Done works in the feature worktree. `AGENT-RULES.md` gives the commands.

---

## 6. Checks and fix rounds

Two steps are checks: **Spec check** and **Review**. A check only finds and logs.

**The loop:** Check → Log → Fix → Re-check → … until clean.

### 6.1 Check
The agent writes its findings in the report's Findings table. Each finding has an ID (continuing from the last ID in the task card), a severity, a location (`file:line` or the Spec line) and a suggested fix (with options A/B/C if there is a real choice). The agent MUST NOT fix anything and MUST NOT offer to. The report's **last line** is `Verdict: clean` or `Verdict: fix round needed: F3, F5`, listing only blocker and should-fix IDs. Nits alone mean `clean`.

### 6.2 Log
On `report`, the planner copies every finding into the task card's Findings table and sets the decision from the severity, without stopping for the Owner:

| Severity | Meaning | Decision |
|---|---|---|
| **blocker** | Can't be built, wrong behaviour, contradicts a decision or a requirement | **fix** |
| **should fix** | Real problem, not fatal: missing test, edge case, unclear spec line | **fix** |
| **nit** | Polish, style, naming | **later** → `Improvements.md` (under "Check before delivery" if it touches an acceptance criterion) |

Two exceptions wait for the Owner: a finding with options (A/B/C) that the decision rule (section 7) doesn't settle, and a finding that needs an outside answer (task → **Blocked**). The Owner MAY change any decision.

### 6.3 Fix round
Only findings marked **fix**, and only those.
- **Spec findings → `2 Spec fix`.** The planner edits the spec and tags each changed line with its finding ID, e.g. `(F5)`. No agent needed.
- **Code findings → `3 Build (n)`.** The prompt lists the finding IDs and points to the report. The agent fixes those and nothing else. For each, it adds a test that fails on the old code, or, for a finding that isn't about behaviour (a committed file, config, docs), a command whose output proves the fix. One round is one commit.
- A fix that needs a file or change the spec doesn't cover goes to `2 Spec fix` first, then Build. If behaviour doesn't change it is a small call under 7.1 with no re-check; if it does, it needs a `2 Spec check (n)` and a new Owner approval.
- If an agent can't fix a finding as written, it stops and reports it. It MUST NOT invent a different fix.

### 6.4 Re-check
A fresh agent runs `2 Spec check (n)` or `4 Review (n)`. Its job, in order:
1. **Each finding from the last round:** fixed / partly / not fixed, with proof (the test, the proof command, or the spec line). The planner marks it **verified** or reopens it.
2. **What the fix round changed:** new problems only. Settled points are not re-raised.
3. **A quick end-to-end pass** over the whole task.

New findings take the next IDs and go round the loop again.

### 6.5 Exit and round limit
A check is **clean** when no blocker or should-fix finding is open. Then the Owner approves (Spec → Build, code → Done).

If the **third** check of the same step still finds a blocker, or a finding is reopened twice, the loop stops. The planner writes a short note in the task card (what keeps failing and why) with options: split the task, rewrite that part of the spec, or change the approach. The Owner picks.

### 6.6 Finding status
`open` → `fixed` (fix round) → `verified` (re-check). Or: `later` (nit), `won't fix` (Owner), `blocked` (needs an outside answer), `reopened` (re-check says not fixed).

---

## 7. Decisions

### 7.1 The decision rule
When a step raises a question that the requirement sources and `Decisions.md` don't answer:
- **Small or technical** (a user-facing string the sources don't give, an engineering option A/B, a status code that keeps existing behaviour): the planner picks the recommended option and continues.
- **Every such call** is logged in `Decisions.md` (date, task, question, options, picked, why, who) and marked **to review**. The Owner tells the planner "ok" or "change" for each; the planner records it, and a reversed call becomes a new finding on the task.
- **Estimates never stop a task.** Note the new size and continue.

Agents decide only things that don't change behaviour (names, how they test, scratch paths) and list them in their report.

### 7.2 Stop points
These always stop for the Owner:
- Spec approval and code approval (unless delegated to a coordinator).
- Anything that needs a client, a designer or another stakeholder.
- Scope changes: work outside the feature, especially changing existing behaviour beyond what the feature needs.
- A change to an acceptance criterion or to an earlier Owner decision.
- The round limit (section 6.5).
- An agent that stops with a question it can't answer from the knowledge base, or fails twice.
- Anything risky: a force push, a push outside the allowed remote, a merge conflict, a red feature suite after a merge.

### 7.3 Source precedence
`RELAY.md` lists the requirement sources in order, strongest first (for example: dated decisions, then tickets and acceptance criteria, then the design). A difference caused by a stronger source is expected, not a mistake. When sources conflict in a way the list doesn't settle, the agent keeps current behaviour, reports it under "Design check", and the Owner decides.

---

## 8. One round of work

1. Owner: `prompt P1-T1`.
2. Planner writes `Workflow/Prompts/P1-T1 - 1 Analyze.md` and replies with **one line** to paste into a fresh agent: `P1-T1 - 1 Analyze: read and follow <absolute path to the prompt>`
3. Owner starts the agent with that line.
4. Agent does the step and writes `Workflow/Reports/P1-T1 - 1 Analyze.md` from the report template.
5. Owner: `report P1-T1`.
6. Planner reads the report and updates the task card, Board, Plan and Decisions, then says what's next.

### 8.1 Commands

The planner MUST support these commands. Tools SHOULD expose them as buttons or slash commands.

| Command | Effect |
|---|---|
| `where are we?` | Current step of every active task, who it waits on, and what's next |
| `plan <F>` | Write `Implementation/<F> - Plan.md` from the feature's requirement doc, with a task list; add a card and a Board row per task |
| `new task <F>: <name>` | Add one task: card, Board row, Plan line |
| `prompt <task>` | Write the prompt for the task's current step; reply with the paste line |
| `report <task>` | Read the report of the highest round of the current step, update the docs, move the step |
| `approve <task>` | Add a dated "Owner approved" row to the card's Steps table; code approval names the reviewed commit. Spec approved → Build; code approved → Done |
| `fix <task>` | Start the fix round: fix spec findings in the card, write the `3 Build (n)` prompt for code findings |
| `findings <task>` | Show open findings: ID, severity, decision, round |

---

## 9. Rules for agents

Every agent follows `AGENT-RULES.md`. Every prompt MUST link it with an absolute path.

---

## 10. Project config (`RELAY.md`)

Every project has one config file, from the `RELAY.md` template. Its YAML front matter is what tools read; prompts link it. The front matter MUST define `relay_spec`, `owner`, `knowledge_base` (an absolute path valid on every machine that runs agents), `repo`, `base`, `allowed_remote` (name and URL of the only remote agents push to), `worktrees` (folder for task worktrees), `features` (each with `id`, `requirement`, `branch`, `worktree`, `task_branch_prefix`), `source_precedence` (section 7.3), `test_commands` (including `done`, the full list run at Done) and `env`; a key that doesn't apply is set to `none`. Paths in it are relative to `knowledge_base` unless absolute. It MAY define `ui_rule`, `models` (reviews SHOULD run on a different model from the build) and `stop_points_extra`. Extensions MAY add keys.

---

## 11. Report contract

A report MUST follow the report template: same sections, same order, real command output in **Git** and **Tests**. A check report ends with its `Verdict:` line (section 6.1); a re-check fills **Previous findings** before new **Findings**.

### 11.1 Task-card front matter

```yaml
id: P1-T2            # task ID
feature: P1
step: 3 Build        # "<#> <Step>" as in section 4
state: active        # active | blocked | parked | done | cancelled
branch: wip/p1-t2-csv-parser
merge:               # merge commit hash, set at Done
```

---

## Appendix A. Lessons (rules with the incidents that produced them)

Each rule below exists because something went wrong without it. More in the coordinator and QA extensions.

| Rule | Why |
|---|---|
| One writer per file | Two writers of the decisions log produced duplicate rows |
| Scratch only in your own `/tmp/<repo>-<task-step>/`; create it first | A browser-test setup in shared `/tmp` was removed by a later step; loose log files piled up; a missing folder silently swallowed output |
| Kill by PID or port, never `pkill -f <pattern>` | A pattern kill on one task probably killed another worktree's test workers mid-suite |
| Never touch another task's worktree | Parallel tasks share one machine; another task's worktree is someone's live build |
| No `--no-verify`; amend with the hook running | A build skipped the hook to get past unrelated lint failures, so the commit never met the checks CI runs |
| Run the full test list at Done, re-run timeouts alone | Subsets missed regressions; timeouts under load looked like failures |
| Fetch and compare with the remote before starting | Work moves between machines overnight |

Changes between versions: `CHANGELOG.md`.
