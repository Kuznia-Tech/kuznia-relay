# Building tools on Kuznia Relay

Because every state change is a file with a parseable name, tools need no database.

**Built and used in the reference project:**
- **Board panel** (an editor side panel). Parses the "Now" table of `Board.md`, lists every prompt link (`[[Prompts/<name>]]`) with four buttons (**Run**: send the paste line as a message to the current agent session; **Insert**; **Copy**; **Open** in the editor), marks prompts whose same-named report exists (`✓ report`), lists the newest prompts not on the board, and refreshes every few seconds.
- **Coordinator on an agent-thread CLI.** The coordinator (`extensions/coordinator.md`) used an existing command-line client for agent threads: start a thread with the paste line, send a message from a file, poll the thread status, wrap planner messages in `flock`.

**Can be built on the same contract:** a one-click runner that opens a fresh agent session per prompt, a findings dashboard across tasks, a decisions-to-review inbox, a stale-step alert (prompt with no newer report after N hours).

Events a tool can watch:

| Event | Signal |
|---|---|
| Prompt ready | New file in `Workflow/Prompts/` |
| Step finished | Report file with the prompt's base name, modified after the prompt |
| Verdict | Last line of a check report: `Verdict: clean` or `Verdict: fix round needed: F…` |
| Task moved | `step:` / `state:` in task-card front matter |
| Decision to review | New row in `Decisions.md` marked "to review" with an empty Review cell |
| Done | `merge:` set in the task card; Done tag exists on the remote |

