# P1 - Plan: Version flag

Requirement: `sources/REQ-1 version flag.md` · Feature branch: `relay/p1` · Board: [[Board]]

## Goal
`greet --version` prints `greet 0.1.0` and exits 0, so users can tell which version they run. Nothing else about the CLI changes.

## Approach
Add argparse's built-in `action="version"` argument in `build_parser()` in `greet.py`. Add CLI-level tests in `test_greet.py`. One task.

## Open questions
None.

## Tasks
Ticked at Done with the merge hash.

- [x] [[P1-T1 Version flag]]: `--version` flag and CLI tests (merge 585ee0e)
