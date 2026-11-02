No local copy of the repo is available in this environment, so I couldn't run the audit script or an actual cold-run test, that part of the skill's process (Steps 1-3) isn't possible here. The draft below reflects only what you've told me, with brackets marking anything I couldn't verify.

Two things worth flagging before you paste this in:

- **The old `docs/contributing.md` is a real risk, not just clutter.** Two copies of contributing guidance drift apart silently, one of you will edit the root file next time and forget the other exists. Either delete `docs/contributing.md` or replace its contents with a one-line pointer to the root file (I've included that stub below). Keep the root file as the canonical one; GitHub surfaces it automatically on issues, PRs and the repo sidebar.
- **The CLA firing after the PR opens is a known bad pattern**, not just a quirk. A contributor who writes code, opens a PR, and *then* discovers they need to sign something feels ambushed, even if the CLA itself is reasonable. You can't change when the bot comments without touching the bot, but you can stop it from being a surprise by stating it plainly before the "open a PR" step, which is what the draft does. Whether a CLA is the right choice at all (versus a DCO sign-off, which is one line and costs a typo-fixer nothing) isn't something I've adjudicated here.
- **The setup instructions are honesty-flagged, not verified.** You told me you haven't run this cold since 2024. I wrote the file to say so openly and invite a bug report if it's stale, rather than presenting untested commands as fact. Before you actually publish this, do one real cold clone (a spare VM, a fresh Docker container, ask a friend) and confirm the commands below match reality, this is the single highest-leverage thing you can do for a solo project, because a contributor who hits a broken setup on day one leaves no trace of having tried.

Here's the file, meant to replace what's currently at the repo root:

```markdown
# Contributing to Portmint

Thanks for looking at Portmint. It's a one-person, nights-and-weekends project,
usually a few hours a week, so a couple of things below exist to save both of
us a wasted round trip.

Code, bug reports, documentation fixes and test cases are all welcome.
So is flagging a confusing error message or diff output, even with no patch
attached.

## Out of scope

I haven't written a firm list yet, so treat this as a starting point rather
than a fixed rule: [support for database engines other than Postgres],
[a GUI or web dashboard], [breaking changes to the diff output format without
an issue discussing it first]. Not sure if your idea fits? Open an issue
before you start writing code. I'd rather talk you out of a week of work than
merge something I can't maintain afterward.

## Get it running

You'll need:

- Python [version, see `pyproject.toml`]
- [uv](https://docs.astral.sh/uv/)
- A running PostgreSQL 16 instance you can connect to

```
git clone https://github.com/<you>/portmint.git
cd portmint
uv sync
```

Point Portmint at your Postgres instance, then run the tests:

```
export DATABASE_URL="postgresql://postgres:postgres@localhost:5432/postgres"
uv run pytest
```

Expect the suite to pass in under [a couple of] minutes.

I haven't run this exact sequence on a clean machine since 2024, so it may be
out of date. If a step here doesn't match what actually happens, please open
an issue with the command and the error. That's a real, useful bug report,
not a bother, it's the fastest way this file gets fixed.

The full setup walkthrough, including platform notes and common connection
problems, lives on the wiki: [link]. This section is the minimum to get from
a clone to a passing test suite; the wiki has the rest.

## Find something to work on

[Link to the "good first issue" query, once one exists.] Comment on an issue
to claim it. If there's no update after two weeks, it's back up for grabs,
say so in the issue before picking it up yourself.

Nothing fits? Open an issue describing what you'd like to change before
writing any code.

## Before you open a pull request

```
uv run pytest
[lint/format command, e.g. uv run ruff check .]
```

Target the `main` branch. Keep commits focused and use a short, plain
summary line.

One more thing before you open anything: this project uses a CLA, not a DCO
sign-off. It's a holdover from a former employer rather than something I
chose, but it's a real requirement. After you open your pull request, a bot
will comment with a link to sign it, sign it right away, since nothing else
can move until you do. I'm telling you now so it isn't a surprise later, even
though the bot itself only shows up after the PR exists.

## After you submit

I'm a solo maintainer doing this a few hours a week, so I can't promise
speed, but I aim to leave some kind of reply, even a quick "seen it, will
look properly soon", within a week. No reply after two weeks? A nudge on the
PR is welcome, not rude.

I review in this order: whether it's in scope, whether it's correct and
tested, the design and why, then style, only the style a formatter missed.
I'll say clearly which comments are blocking and which are just suggestions.

[Confirm: squash-merge / rebase / merge commit.] You stay listed as the
author, and you'll get a mention in the release notes.

## Stuck?

Comment on the issue or PR you're working from, that's the one channel I
actively watch. Given the time I have, expect a wait of a few days rather
than a few hours.

## Sticking around

If you come back for a second contribution, tell me, I keep a short list of
things that could use a second pair of hands, including some that go beyond
a single PR.
```

And the stub to drop in at `docs/contributing.md` so old links don't 404:

```markdown
# Contributing

This file moved. See [CONTRIBUTING.md](../CONTRIBUTING.md) at the repository root.
```

Fill in before you publish: repo URL, pinned Python version, the actual lint/format command, the wiki URL, your real merge style, a link to the beginner-issue query (once you've labeled at least a few), and a firmer out-of-scope list. The out-of-scope list matters more than it looks, an empty one is exactly what turns a week of someone's spare time into a PR you have to decline.