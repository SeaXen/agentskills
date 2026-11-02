Root cause: wording is not the leverage point. Skill's own baseline: "we get stars but no pull requests" almost always means step 3 (setup) or step 4/6 (issue queue quality, review), not file prose. You already tested that — two rewrites, zero PRs. Third rewrite won't move it either.

Two real culprits from your numbers:

1. **11 old bugs relabeled "good first issue"** — named failure mode in this skill: "small for someone who knows codebase is not small for stranger." If those 11 lack location, verification command, and named mentor, they're not first issues, just old bugs with a sticker. Zero-uptake in months confirms it.
2. **1 outside PR ever got closed, 2 typo fixes never returned** — signals no second-contribution loop (step 6). Typo-fixers didn't come back for a second one; the closed PR may have died from scope-silence, not scope-reject.

I have no repo access, so I can't cold-run your setup or read your actual 11 issues (skill mandates that before shipping copy — "documentation describing a broken setup is worse than no documentation"). Everything below is a draft skeleton, not verified. Run the cold-run check yourself before publishing:

## CONTRIBUTING.md draft

```markdown
# Contributing to Quillrail

We take code, documentation, tests, bug triage, and examples.
We do not take: new external dependencies, breaking API changes without
a prior issue discussion, and support for stream sources outside CSV.

## Set up

    git clone git@github.com:<you>/quillrail.git && cd quillrail
    go test ./...

Expect: all tests pass in under [N] seconds. No config, no external services.
Prerequisites: Go [version, pinned in go.mod] — nothing else to install.

## Find something to work on

- Beginner-friendly: [link to good-first-issue label query]. Comment to claim;
  claim expires after 14 days with no activity.
- Non-code entry points: docs, adding a test for an uncovered transform,
  triaging open issues — see [link].
- Nothing fits? Open an issue describing the change before writing code.

## Before opening a pull request

    go vet ./... && go test ./... -race

Target the `main` branch. Sign commits with `git commit -s` (DCO).

## After you submit

I respond within a week — solo maintainer, this is the honest number, not
an aspiration. Squash-merge. You're credited in the release notes.
If your PR goes quiet on my end for over a week, ping the thread — I'd
rather be nudged than have it silently rot.

## Stuck?

Comment on the issue or PR thread — usually answered within a day.

## Recognition

Merged contributions are named in the changelog. Two solid PRs and
I'll ask if you want triage/review access.
```

Fill every bracket. Then run `go test ./...` from a truly clean clone before publishing — that's the only way to know the setup line is true.

## Fix the 11 stale issues, don't write new ones

Replace this shape (what you likely have):

```
Title: Improve error handling in the CSV reader
Labels: good first issue
```

With this shape, per issue:

```
Title: Reader panics on empty header row instead of returning ErrEmptyHeader
Labels: good first issue, area/reader, skills/go-io

**Current**: `NewReader(emptyHeaderFile)` panics.
**Expected**: returns `ErrEmptyHeader`, no panic.
**Where**: `reader.go`, `parseHeader()`, near the first `Scan()` call.
**Approach**: check `len(fields) == 0` before use; return typed error.
  Message text is settled — no design discussion needed.
**Verify**: `go test ./... -run TestParseHeader`
**Mentor**: @you — comment to claim, ask anything in-thread.
```

Do this for 3 of the 11 now — that's your floor (skill's own minimum: 3 valid unclaimed at all times). Delete or close the other 8 if they can't reach this shape; a fake-full queue is worse than an honest empty one.

## Templates for when a PR actually lands

Same-day acknowledgement (not full review):

```
Thanks — this is in scope, approach looks right. Full review by [day].
CI red on lint only: run `go vet ./...` locally, should reproduce.
```

If declining:

```
Thanks for writing this — it's a no. [Feature] is out of scope
(CONTRIBUTING lists it) because [reason]. The code itself is clean;
would work well as a separate package, happy to link it from the README.
```

Next: pick 3 of the 11 issues, rewrite them to the strong shape above, post today.