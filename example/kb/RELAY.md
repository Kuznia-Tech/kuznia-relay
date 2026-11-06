---
# Kuznia Relay project config (SPEC section 10). Tools read this front matter.
relay_spec: "1.2"
owner: "You"
knowledge_base: "/home/you/relay-example/kb"
repo: "/home/you/relay-example/app"
base: "main"                      # branch or tag work starts from
allowed_remote:
  name: "origin"
  url: "git@github.com:you/greet.git"
worktrees: "/home/you/relay-example/app/.worktrees"   # task worktrees go here; add it to .git/info/exclude
features:
  - id: P1
    name: "Version flag"
    requirement: "sources/REQ-1 version flag.md"
    branch: "relay/p1"
    worktree: "/home/you/relay-example/app/.worktrees/p1"
    task_branch_prefix: "wip"     # task branch wip/p1-t1-<slug>, Done tag wip/p1-t1-done
source_precedence:                # strongest first
  - "Decisions.md (dated entries)"
  - "sources/REQ-1 version flag.md"
test_commands:
  unit: "python3 -m unittest -q"
  integration: "none"
  lint: "none"
  done: "python3 -m unittest -q"
env:
  toolchain: "Python 3.9+, standard library only"
  vars: "none"
  worktree_setup: "none"
---
# RELAY.md: project config

Kuznia Relay 1.2. The front matter above is the config; edit it there. Every prompt links this file. The Owner is the only writer.

## Notes
`greet` is a one-file Python CLI. Run it with `python3 greet.py [NAME] [--shout]` from the repo root. No test data, no flaky tests.
