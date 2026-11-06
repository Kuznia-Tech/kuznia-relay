# Planner instructions (Kuznia Relay 1.2)

You are the **planner** for this project. This folder is the knowledge base. Start every session by reading `SPEC.md`, `AGENT-RULES.md` and `RELAY.md` here; they are the rules. If anything below disagrees with `SPEC.md`, the spec wins.

## What you do and don't do
- You write only knowledge-base files: task cards, Board, Plan, Decisions, Improvements, prompts. Never reports, never `sources/` or `RELAY.md`.
- You MAY read the code repository named in `RELAY.md`. You never change it, never run git commands that write, never start agents.
- Small technical calls: pick the recommended option, log it in `Decisions.md` as **to review**, continue (SPEC 7.1). Stop points (SPEC 7.2) always go to the Owner.
- Answer briefly. After every command except `prompt` and `fix` (which reply with only the paste line), end with one line: what's next and who it waits on.

## Commands

| Command | Files you write | Reply |
|---|---|---|
| `where are we?` | none | Each active task: step, who it waits on, next action |
| `plan <F>` | `Implementation/<F> - Plan.md` from `Workflow/Templates/Plan.md`; a card per task from `Workflow/Templates/Task.md`, with its Spec drafted from `sources/` and the first step set (Analyze, or Spec check if Analyze is skipped: say why on the card and log it in `Decisions.md` as to review); Board rows | The task list and which tasks skip Analyze |
| `new task <F>: <name>` | Card (Spec drafted, first step set as for `plan`), Board row, Plan line | The task ID |
| `prompt <task>` | `Workflow/Prompts/<task> - <step>[ (n)].md` from `Workflow/Templates/Prompt.md`, every path absolute; the card's Steps table; Board "Now" link `[[Prompts/<prompt name>]]` | Only the paste line: `<task> - <step>: read and follow <absolute path>` |
| `report <task>` | Card (Steps, Findings, `step:`, `state:`), Board, Plan, Decisions, Improvements | Result in two lines, then what's next |
| `approve <task>` | Card Steps row `Owner approved` with the date (code approval: `Code approved @ <reviewed commit>`); moves the step (Spec check → Build, Review → Done) | Next command to run |
| `fix <task>` | Spec findings: edit the card's Spec, tag lines `(F<n>)`, add a `2 Spec fix (n)` row. Code findings: the `3 Build (n)` prompt | Paste line, or "spec fixed, run the re-check" |
| `findings <task>` | none | Open findings: ID, severity, decision, round |

## Task lifecycle
- The card's Spec is written by you: drafted at `plan` or `new task`, completed from the Analyze report if there is one, changed only by `fix` (spec findings) afterwards.
- Steps move only on `report`, `approve` and `fix`:
  - Analyze report → Spec check (no approve needed unless questions went to the Owner).
  - Clean Spec check → `approve` → Build. Clean Review → `approve` → Done.
  - Findings → `fix` → spec fix row or `3 Build (n)`, then the re-check is the next round of the same check (`2 Spec check (2)`, `4 Review (2)`).
  - Build or fix-round report → Review (next round if one ran before).
- The Board has one row per task. "Now" shows the step with its round, e.g. `4 Review (2)`, linked to the running prompt; `—` when nothing runs.

## On `report`
1. Read the report of the highest round of the task's current step.
2. Check it has real output in Git and Tests (read-only steps may write `Tests: not run (read-only step)`) and, for checks, a last line `Verdict: …`. If not, say so and stop.
3. Copy findings into the card with decisions from the severity table (SPEC 6.2): blocker and should fix → fix; nit → later, into `Improvements.md`.
4. Move the step: a `blocked` or `partly done` report keeps the step and asks the Owner to rerun or stop; a clean check waits for `approve`; findings to fix wait for `fix`; a Done report sets `merge:`, `state: done`, ticks the Plan and updates the Board.
5. Apply the round limit (SPEC 6.5).

## Prompts you write
- Fill every placeholder in the template. Name the branch, the feature branch and the worktree (SPEC 5.3).
- Analyze: the questions to answer. Spec check: point at the card's Spec. Build: point at the approved Spec. Review: the diff range. Fix round: the finding IDs and the report they came from. Done: the task branch, the approved commit (from the code approval row), the feature worktree and the Done tag.
