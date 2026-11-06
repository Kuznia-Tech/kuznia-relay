# Kuznia Relay: a gated workflow for shipping code with AI coding agents

Kuznia Relay lets one engineer deliver real features with AI coding agents (Claude Code, Codex, or any agent CLI) without losing control. Every step runs in a **fresh agent**, every check is separate from its fix, and every claim comes with **evidence in files**: git hashes, diff stats, test output. All state lives in a plain Markdown knowledge base, not in chat.

Spec version 1.2 · [MIT licence](LICENSE)

## Why
Long agent sessions drift, review themselves, and report "done" without proof. Relay splits the work into short legs and passes a baton between them:

```
Owner: prompt P1-T1  →  planner writes the prompt  →  fresh agent does one step, writes a report
Owner: report P1-T1  →  planner reads the evidence, updates the docs, says what's next
```

Each task goes **Analyze → Spec check → Build → Review → Done**. Checks only find problems; fixes happen in separate, scoped rounds followed by a re-check. Small technical calls are made and logged for you to review later; scope, requirements and approvals always stop for you.

## Who it's for
Engineers and small teams who already use coding agents and want them to ship merge-ready work on a real codebase, with a paper trail a reviewer or client can follow. It shines on features that take more than one session.

## What you need
- A coding-agent CLI for the steps (Claude Code, Codex, …) and an LLM session for the planner (can be the same tool).
- Git 2.28+ (the workflow uses worktrees) and a remote agents may push to.
- A folder for the knowledge base, ideally its own git repo (or a synced folder) so every machine sees the same state. [Obsidian](https://obsidian.md) makes the `[[links]]` clickable but is optional.

## Start in 5 minutes
1. **Make the knowledge base** next to your repo:
   ```bash
   git clone https://github.com/Kuznia-Tech/kuznia-relay.git
   cp -R kuznia-relay/kit my-project-kb
   cp kuznia-relay/SPEC.md kuznia-relay/AGENT-RULES.md my-project-kb/
   ```
2. **Fill in `my-project-kb/RELAY.md`** (the YAML front matter at the top): repo path, allowed remote, test commands, your first feature. Put its requirements (ticket, acceptance criteria, design) in `my-project-kb/sources/`.
3. **Create the feature branch from `base` and its worktree**, and push the branch. A sibling folder keeps worktrees out of your repo:
   ```bash
   cd my-project
   git fetch origin
   git branch --no-track feat/my-feature origin/main && git push -u origin feat/my-feature
   git worktree add ../my-project-worktrees/p1 feat/my-feature
   ```
   Set `worktrees: ../my-project-worktrees` and the feature's `worktree` in `RELAY.md` to match (absolute paths are safest).
4. **Start the planner** in the knowledge-base folder. `kit/` ships `AGENTS.md` (read by Codex) and `CLAUDE.md` (read by Claude Code), so the planner loads its instructions and the spec on its own. Then say:
   ```
   plan P1
   prompt P1-T1
   ```
5. **Run the step**: the planner replies with one line such as
   `P1-T1 - 2 Spec check: read and follow /home/you/my-project-kb/Workflow/Prompts/P1-T1 - 2 Spec check.md`
   Paste it into a **fresh** agent session started in your repo, with write access to the knowledge base for its report (Claude Code: `claude --add-dir /home/you/my-project-kb`; Codex: `codex --add-dir /home/you/my-project-kb`). When it has written its report, tell the planner `report P1-T1`. Repeat with `prompt`, `fix`, `approve` until Done.
6. **Deliver**: when every task of the feature is Done, open the pull request from the feature branch to `base` yourself, then remove the task worktrees, task branches and `/tmp` scratch folders.

See [example/](example/) for a complete run on a toy app: a spec check with a finding, a spec fix, Build, Review, a code fix round, a re-check and Done, with every prompt and report.

## What's in the repo
| Path | For |
|---|---|
| [SPEC.md](SPEC.md) | The spec: roles, steps, check-and-fix loop, decisions, naming, config, report contract |
| [AGENT-RULES.md](AGENT-RULES.md) | Rules every coding agent follows, including the git and worktree commands |
| [kit/](kit/) | The knowledge base to copy: config, Board, Decisions, planner instructions, templates |
| [example/](example/) | A worked example taken to Done |
| [extensions/](extensions/) | Optional: [coordinator](extensions/coordinator.md) for unattended runs, [QA](extensions/qa.md) before hand-off |
| [docs/tools.md](docs/tools.md) | Tools you can build on the file contract |
| [CHANGELOG.md](CHANGELOG.md) | Spec versions |

## Good to know
- **The agent rules run on trust today.** Nothing yet stops an agent that ignores "never force-push" or "edit only your report". A hooks pack that enforces them is planned.
- The planner commands are plain text: `where are we?`, `plan`, `new task`, `prompt`, `report`, `approve`, `fix`, `findings`.
- When the loop feels routine, the [coordinator extension](extensions/coordinator.md) can drive it overnight.

## Contributing
Issues and pull requests are welcome; see [CONTRIBUTING.md](CONTRIBUTING.md). File names are a contract that tools parse, so any naming change needs a CHANGELOG entry.

## Pitch material
`pitch/` holds a slide deck and two rendered versions of the spec, for presenting Relay. The spec in `SPEC.md` is the source of truth.
