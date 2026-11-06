---
# Kuznia Relay project config (SPEC section 10). Tools read this front matter.
relay_spec: "1.2"
owner: "<name>"
knowledge_base: "/absolute/path/to/knowledge-base"
repo: "/absolute/path/to/repo"
base: "main"                      # branch or tag work starts from
allowed_remote:
  name: "origin"
  url: "git@github.com:<org>/<repo>.git"
worktrees: "/absolute/path/to/repo/.worktrees"   # task worktrees go here; add it to .git/info/exclude
features:
  - id: P1
    name: "<feature name>"
    requirement: "sources/<file>"
    branch: "feat/<slug>"
    worktree: "/absolute/path/to/repo/.worktrees/p1"
    task_branch_prefix: "wip"     # task branch wip/p1-t1-<slug>, Done tag wip/p1-t1-done
source_precedence:                # strongest first
  - "Decisions.md (dated entries)"
  - "sources/<requirements or tickets>"
  - "sources/<design>"
test_commands:
  unit: "<command>"
  integration: "<command>"
  lint: "<command>"
  done: "<the full list run at Done>"
env:
  toolchain: "<language and runtime versions>"
  vars: "<e.g. TZ=UTC>"
  worktree_setup: "<install and build commands for a new worktree>"
# Optional:
# ui_rule: "Build only from <component library>, the way <existing screen> uses it. No new shared components, no custom CSS."
# models: { planner: "<model>", build: "<model>", review: "<a different model from build>" }
# stop_points_extra: ["<project-specific stop>"]
---
# RELAY.md: project config

Kuznia Relay 1.2. The front matter above is the config; edit it there. Every prompt links this file. The Owner is the only writer.

## Notes
Anything an agent should know that doesn't fit a key: how to run the app locally, test data, known flaky tests.

For client work, add the client's Q&A answers and the statement of work to `source_precedence`.
