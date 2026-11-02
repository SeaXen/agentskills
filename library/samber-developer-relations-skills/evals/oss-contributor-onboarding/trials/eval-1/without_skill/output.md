Your two rewrites failed for the same reason most CONTRIBUTING.md rewrites fail: they answered "how do I submit a PR" (a process question) when the actual barrier is "will this be worth my time" (a trust question). A stranger looking at 6,200 stars, one maintainer, and a closed PR from someone who tried is reading risk, not opportunity — the closed PR especially. It's public proof that submitting code here can be wasted effort. No amount of "we love contributions! ❤️" copy fixes that; it needs to be answered directly, and the label problem (11 *old* good-first-issues, untouched) needs to be fixed alongside the copy, not instead of it — an 8-month-old "beginner" issue reads as "nobody actually wants this," even if that's not true.

Here's the copy:

```markdown
# Contributing to Quillrail

I maintain Quillrail alone. I read every PR within 48 hours — accepted, rejected,
or "here's what to change," always with a reason. Silence past 48 hours means
ping me; you're owed a response, not a wait.

## Before you write code

For anything bigger than a typo or a one-line fix: comment "I'd like to take
this" on the issue first. This avoids two people solving the same issue in
parallel, and it's your signal that I'm paying attention before you spend time.

For a new transform type, an API change, or anything touching the streaming
core: open an issue describing the approach before writing code. This is the
single biggest reason a PR gets closed instead of merged — not code quality,
but code arriving before the design was agreed on. Ask first, build once.

## What gets merged fast

- One change per PR. Mixing a typo fix with a feature gets it split or bounced.
- Tests for new behavior. `go test ./...` must pass before I look at it.
- `gofmt` and `go vet` clean — CI checks this, so you don't have to guess.
- Match the style of the file you're editing. I won't bounce a PR over a style
  nit I can fix in five seconds during review.

## Issues sized for a first PR

Every `good first issue` now states the target file, the expected diff size,
and why it's still open. If an issue doesn't have those, it's not ready —
flag it and I'll fix the issue, not you.

- `area/docs` — no design risk, usually merges same day.
- `area/tests` — add a missing case to an existing suite, no decisions to make.
- `area/parser`, tagged `<10 lines` — isolated, already covered by tests.

## Setup

\`\`\`bash
git clone https://github.com/<org>/quillrail && cd quillrail
go test ./...
\`\`\`

One command, one test run. If this fails on a clean clone, that's a bug in
the setup, not in your environment — open an issue.

## After you open a PR

1. CI runs automatically. Red CI means fix it before my review, not after.
2. I review within 48 hours, every time.
3. Approved PRs merge within a week. I write the changelog line; you keep the
   commit and the authorship.
4. If I close a PR, you get the specific reason and, where there's a path to
   it, what to change to get it merged. Not just "closed."

## Recognition

Every merged PR adds you to `CONTRIBUTORS.md` and gets you named in that
version's release notes.
```

Two things this copy can't do alone, so don't ship it without them:

- **Rewrite the 11 `good first issue` labels**, not just relabel them. Each needs the file path, expected diff size, and a plain-language reason it's unclaimed, written directly into the issue body — the CONTRIBUTING.md above promises this exists, so it has to actually exist before you publish the rewrite.
- **Decide, honestly, what you'll say about the closed PR** — even indirectly. If someone digs through closed PRs (and a wary first-timer will), a maintainer who visibly explains "here's why, here's what would've worked" reads as safe to approach. One that just says "closed" confirms the fear this whole rewrite is trying to remove.