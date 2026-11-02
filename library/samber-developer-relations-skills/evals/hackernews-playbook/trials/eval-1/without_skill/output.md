# Show HN package for Shiftlog

## Read this first: the upvote plan

Cancel the 9am PT "be ready to upvote" plan. HN detects coordinated voting (same-time votes from new or linked accounts, and votes arriving through a shared link). Detected rings get the votes nullified, the post penalized or killed, and sometimes accounts banned. For a launch that is a lot of downside, and a visibly boosted Show HN also draws "this is astroturfed" comments.

Do this instead:
- Tell the team the post is live, and don't ask anyone to vote.
- Anyone who has used Shiftlog can leave a comment about their own experience. A comment from a user is fine.
- Put your effort into being present for the first 2–3 hours and answering every comment.

Timing is fine. Tuesday around 9am PT is a reasonable slot.

## Title

```
Show HN: Shiftlog – Diff Postgres schemas and generate migrations (Go, MIT)
```

What changed:
- "Fastest, smartest, never write a migration again" is the kind of superlative HN moderators rewrite and commenters mock. A reader will also object that you can't promise "never".
- The new title says what the tool does, the language, and the license. The "Go" and "MIT" tags tell HN readers it's open source and inspectable.

Backup, if you want the pain point in the title:
`Show HN: Shiftlog – Generate Postgres migrations by diffing your schemas`

## Where the "body" goes

On HN, a submission with a URL ignores any text box content. Submit the GitHub repo URL (not the landing page, since HN readers want code) and leave the text field empty. The body below goes in as your first comment. If you'd rather make a text-only post, paste the same content into the text field.

## First comment (post immediately after submitting)

I couldn't see your landing page copy or feature list in this chat, so the bracketed parts are for you to fill in with real details. Delete any line you can't back up.

```
Hi HN, I'm [name], one of the authors of Shiftlog.

Shiftlog is a CLI that diffs two Postgres schemas and generates the migration
that takes one to the other. It's written in Go and MIT licensed.
Repo: [link]

Why we built it: [1-2 honest sentences. For example: "we kept hand-writing
ALTER TABLE migrations that drifted from what was actually in staging, and
reviewing them by eye didn't catch it."]

How it works:
- It reads the source and target schemas [from live databases / from SQL
  files / both], builds a model of tables, columns, indexes, constraints [and
  whatever else you support], and emits SQL for the difference.
- Example:

    shiftlog diff --from [source] --to [target] > 0042_add_orders_index.sql

  [Replace with your real command and a short real output.]

What it does not do (yet):
- [e.g. Renames are ambiguous in a pure diff. Today we treat a rename as
  drop + add unless you annotate it. Say what you actually do.]
- [Destructive changes: do you warn, require a flag, or just emit them?]
- [Data migrations, long-running locks, CREATE INDEX CONCURRENTLY: handled or
  not?]
- [Postgres versions and objects not covered: views, functions, extensions,
  partitions, etc.]

Where it differs from existing tools: [one fair sentence on how it compares
to Atlas, pg-schema-diff, migra, sqitch, or hand-written migrations. Name the
real trade-off, not just "ours is better".]

Generated migrations should still be reviewed before they run. I'd especially
like feedback on [one specific thing: rename detection, safe ordering of
dependent objects, lock behavior]. Happy to answer anything about the
internals.
```

## Notes on what I changed and why

- **Dropped "the fastest, smartest".** If you have benchmarks, show them in the comment ("diffs a 2,000-table schema in X s on Y hardware"). A number beats an adjective on HN.
- **Replaced the feature list with limitations plus one example.** HN readers trust a tool more when you state its edges first. Landing-page bullets read as an ad there.
- **Specific feedback ask.** It gives commenters something concrete to engage with, which helps the thread more than a generic "thoughts?".
- **Show HN rules.** People must be able to try it without signing up. Make sure the README has an install command and a 60-second quickstart, and that you can stay online for the first 2–3 hours.

## Before you post

- [ ] The README quickstart works from a clean machine
- [ ] The first comment has no unfilled brackets and no claim you can't demonstrate
- [ ] The submitting account has some history. A brand-new account gets more scrutiny.
- [ ] Team message says "it's live, here's the link, feel free to comment if you've used it", with no mention of voting

If you paste the landing page copy and feature list, I'll fill in the brackets and tighten the comment against your real details.