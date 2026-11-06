# Contributing to Kuznia Relay

Thanks for helping. Relay is a spec plus a kit of Markdown files, so most contributions are text.

## Ways to help
- **Report a problem with the spec**: a rule that contradicts another, can't be followed, or leaves you guessing. Use the "Spec problem" issue form and quote the lines.
- **Share a run**: what worked and what you had to invent when using Relay on a real project. These reports shape the next version.
- **Propose a change**: open an issue first for anything bigger than a typo, so we can agree on the rule before the wording.

## Pull requests
1. Keep one change per pull request.
2. Update every file the change touches: `SPEC.md`, `AGENT-RULES.md`, `kit/` (config, templates, planner instructions) and `example/`, so they never disagree.
3. File and folder names, step names, the verdict line, Board links and `RELAY.md` keys are a contract that tools parse. Any change to them needs a `CHANGELOG.md` entry under a new spec version.
4. Keep `SPEC.md` short. Mechanics (commands, formats) belong in `AGENT-RULES.md`, the templates or `kit/AGENTS.md`.
5. Write plainly: short sentences, no jargon a newcomer wouldn't know.

## Versions
The spec follows `major.minor`. A minor version may rename or add files and keys (listed in the CHANGELOG). A major version changes the workflow itself. Releases are tagged `v<version>`.

## Conduct
Everyone taking part follows the [Code of Conduct](CODE_OF_CONDUCT.md).
