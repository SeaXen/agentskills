One quick note before the deliverable: since you have two docs already (root `CONTRIBUTING.md` and the stale `docs/contributing.md`), delete `docs/contributing.md` once you drop this in, so contributors don't land on the outdated one via an old link or search result.

Here's the full `CONTRIBUTING.md`:

```markdown
# Contributing to Portmint

Portmint is a Python CLI that diffs PostgreSQL schemas. It's maintained by one
person, in spare evenings and weekends — figure a few hours a week, not a few
hours a day. That shapes everything below: how fast reviews happen, how much
process there is, and why the setup instructions ask you to be patient with
rough edges.

Thank you for taking the time to contribute. This guide covers what to expect,
how to get a working dev environment, and how to submit a change.

## Before you start

For anything bigger than a typo fix or a small bug fix, open an issue first
and describe what you want to do. This avoids two people fixing the same bug,
or you spending a weekend on a PR that doesn't fit the project's direction.

For small fixes (typos, obvious bugs, missing error messages), skip the issue
and open a PR directly.

Response times will be slow. Expect days, sometimes longer, between a PR going
up and getting a review — this is a nights-and-weekends project, not a funded
one. If you haven't heard back in two weeks, a polite ping on the PR is fine.

## Prerequisites

You need:

- Python (see `pyproject.toml` for the supported version range)
- [uv](https://docs.astral.sh/uv/) for dependency management
- A running PostgreSQL 16 instance that Portmint can connect to and diff
  against

## Setting up your dev environment

```
uv sync
```

This installs dependencies and creates a virtual environment.

**Heads-up:** this setup hasn't been verified on a clean machine since 2024.
If `uv sync`, or anything after it, fails on a fresh checkout, that's useful
information — please open an issue with your OS, Python version, and the
full error. Don't assume it's something you did wrong.

For the full build, test, and local-Postgres setup — including how to point
Portmint at your PostgreSQL 16 instance — see the
**[Development Setup wiki page](https://github.com/samber/portmint/wiki/Development-Setup)**.
It's long enough that duplicating it here would just mean two copies to keep
in sync, so the wiki is the source of truth. If a step there is wrong or
missing, a PR against the wiki is as welcome as one against the code.

## Making a change

- Keep pull requests focused. One fix or one feature per PR — it's faster to
  review and easier to revert if something's wrong.
- Add or update tests for any behavior change. If you fix a bug, add a test
  that fails without your fix.
- Follow the existing code style. If a linter or formatter is configured in
  the repo, run it before opening the PR (see the wiki setup page for the
  exact commands).
- Update relevant docs (README, wiki, docstrings) when behavior changes.
- Write a clear commit message: what changed and why, not just what.

## Opening a pull request

1. Fork the repo and create a branch off `main`.
2. Make your change, with tests.
3. Push and open a PR against `main`.
4. A CLA-signing bot will comment on your PR shortly after you open it, with
   a link to sign. See below — this is required before any PR can be merged.
5. Wait for review. See the response-time note above.

## Contributor License Agreement (CLA)

This project requires a signed CLA before any contribution can be merged.
When you open a pull request, a bot will automatically comment with a link
to review and sign it. You only need to do this once — it's remembered for
future PRs from the same GitHub account.

Your PR won't be merged until the CLA is signed, even if the code review is
otherwise complete, so sign it as soon as the bot comments to avoid it being
the only thing blocking your merge.

## Reporting bugs

Open an issue with:

- What you expected to happen, and what happened instead
- Your Portmint version, Python version, and PostgreSQL version
- The schemas (or a minimal reproduction) you were diffing, if you can share
  them without exposing anything sensitive
- The full command you ran and its output

A minimal reproduction is the single most useful thing you can include — it's
the difference between a same-day fix and a bug that sits for weeks because
it can't be reproduced.

## Suggesting features

Open an issue describing the problem you're trying to solve, not just the
feature you want. Given the limited maintenance time, features get prioritized
by how many people hit the same problem and how well they fit Portmint's
scope as a schema-diffing tool — not by request order.

## Questions

If something in this guide or the wiki is unclear, open an issue. If you had
to guess at something to get set up, that's a documentation bug — flag it.
```