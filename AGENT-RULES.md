# Rules for agents

Every Kuznia Relay agent follows these, every step. Prompts link this file. Spec: `SPEC.md` in the knowledge base.

## Before you start
1. Read your prompt, the task card, and every file they link. Paths in the prompt are absolute.
2. Read the requirement sources listed in `RELAY.md` (paths there are relative to the knowledge base) and check your work against them, in its precedence order. Report matches and conflicts under "Design check".
3. Check the remote: `git remote get-url <name>` and `git remote get-url --push --all <name>` (one line, no others) must both equal the `allowed_remote` URL in `RELAY.md`. If not, stop and report.
4. Fetch it and check that the branch you start from matches the remote. Say so in your report, with the base commit.
5. Make your scratch folder in `/tmp` (or your OS temp folder) from the repo folder's name and your prompt's name: lower case, every run of spaces, brackets and dashes turned into one `-`, no trailing `-`. Repo `shop`, `P1-T2 - 3 Build (2)` → `mkdir /tmp/shop-p1-t2-3-build-2/`. If it already exists, stop and report. Quote every path that has spaces.

## Where you work
- **Analyze, Spec check, Review:** a throwaway worktree in your scratch folder, removed when you finish:
  `git worktree add --detach /tmp/<scratch>/wt <remote>/<branch>` … `git worktree remove --force /tmp/<scratch>/wt` (`--force` is fine here: it is your own detached worktree). Then delete your scratch folder.
- **First Build:** create the task branch and its worktree from the remote feature branch:
  `git worktree add --no-track -b <task branch> <worktrees>/<task id lower-case> <remote>/<feature branch>`
  `--no-track` matters: the task branch must never push to the feature branch. Push it with `git push -u <remote> <task branch>`.
- **Fix round (`3 Build (n)`):** reuse that worktree. First check its head equals the last commit in the previous Build report; if not, stop and report.
- **Done:** work in the feature worktree from `RELAY.md`. This is the only step that may touch it.
- Never change another task's worktree.

## While you work
- Do one step: the one your prompt names.
- **Spec check, Review:** change no code. Log findings in the report's Findings table, IDs continuing from the task card. Never fix them, never offer to. The report's last line is `Verdict: clean` or `Verdict: fix round needed: F3, F5` (blocker and should-fix IDs only; nits alone mean clean).
- **Analyze:** change no code. Answer the prompt's questions with `file:line` references. No verdict.
- **Build:** stay on the task branch and inside the spec. If the spec is wrong or unclear, stop and say so in the report. Stage files by name and check `git status` before committing; never commit build output or caches.
- **Fix round:** fix only the listed finding IDs, one commit `[<TaskID>] Fix F3-F5`. For each finding add a test that fails on the old code, or, if the finding isn't about behaviour, a command whose output proves the fix.
- **Done:** fetch, check `<remote>/<task branch>` equals the approved commit named in your prompt (if not, stop: the code changed after review), then merge that commit with `git merge --no-ff -m "[<TaskID>] Merge <task branch>" <approved commit>`, run the full Done test list, tag the merge commit (`git tag <done tag>`), push the feature branch and the tag. Re-run a file that times out on its own before calling it a failure.
- Decide only things that don't change behaviour (names, how you test, scratch paths) and list them under "Decisions you made". Stop and report for everything else.
- When sources conflict in a way the precedence list doesn't settle, or the design conflicts with the code: keep the current behaviour and report it. Don't pick a side.
- If `RELAY.md` has a `ui_rule`, follow it. If no existing component fits, stop and report.

## Git
- Push only to the allowed remote, after each commit, with an explicit target: `git push <remote> <task branch>` (Done: `git push <remote> <feature branch> <done tag>`). Never a bare `git push`. Paste the output in the report.
- Never open a pull request. Never force-push. Never skip hooks (`--no-verify`).

## Shared machine
- Scratch files only in your own `/tmp/<scratch>/`. Never delete anything you didn't create.
- Stop only processes you started, by PID or port. Never `pkill -f` / `killall` with a pattern.

## Always
- Write the report, even when stuck. A partial report beats none. If a command you need failed, paste its output in place of the evidence.
- Publish the report in one move: write `Reports/.<report name>.tmp` next to it, then rename it to `<report name>.md`. A report that exists is complete.
- Edit no knowledge-base file except your report.
- Paste real output: branch, commits, `git diff --stat`, test commands and their counts.
