**Don't launch "Ferrule Friday". Run a release-triggered email instead: 2 sends a month, built from the notes you already write.**

Nothing is created yet. I can't sign up for tools or touch your DNS, so everything below is for you to paste and set up.

## Why not weekly

- A weekly email is 52 sends a year. You ship about 24 releases a year, so roughly half the Fridays would have nothing to say.
- One hour a month covers two release emails at about 20 minutes each, with 20 minutes spare. A weekly column needs about 4 hours a month at 1 hour per issue, so it doesn't fit.
- A newsletter that skips weeks teaches readers to ignore it. A name that says "Friday" makes every skipped week visible.
- Your advisors are right about owning a channel. They're wrong about the format. You have no blog, so the email is the only place anyone hears from you outside GitHub.

Name it **Ferrule Releases**. The name promises "when we ship", not "every Friday".

## The 60-minute budget

| Item | Per month |
|---|---|
| Release notes written once, reused in 3 places | 0 extra (already done) |
| Email polish, 2 releases × 15 min | 30 min |
| Review subscriber count and replies | 10 min |
| Spare for a breaking-change send | 20 min |

## Setup, in order (about 45 minutes once)

1. **Pick the tool (10 min).** Use a list tool with RSS-to-email. Buttondown and Kit both fit. Check the RSS feature on the plan you choose.
2. **Connect the feed (10 min).** Point it at `https://github.com/<owner>/ferrule/releases.atom`. Set it to create a **draft**, not an auto-send. A human reads every email, because a wrong note sent by an automation can't be recalled.
3. **Add signup in 3 places (15 min).**
   - README: one line under the install section.
   - CLI: print `Release news: <url>` once after upgrade or in `ferrule --help`.
   - Hosted-tier signup flow: an unchecked opt-in box. Never opt people in silently.
4. **Send a welcome email (10 min).** Template below. Tell people the frequency up front.

Paste into the README:

```md
Get one short email when a new Ferrule release ships (about 2 a month): [subscribe](<signup-url>)
```

Welcome email:

```text
Subject: You're on the Ferrule release list
Preview: About 2 emails a month, only when we ship.

Thanks for subscribing.

You'll get one email each time we cut a release: what changed, whether it
breaks anything, and what to do about it. About 2 a month. No marketing.

Reply to this email to reach the three of us directly.

Orrin Labs
```

## The per-release routine (20 min)

Write the GitHub release body in this shape. The email copies it.

```md
## Ferrule vX.Y.Z

**Action needed:** none | <one line, if anything breaks>

### What changed
- <effect the user sees, one sentence>
- <effect the user sees, one sentence>

### Fixes
- <one line each, max 3>

Full notes: <release url>
```

Steps for each release:

1. Publish the GitHub release. The feed creates the email draft.
2. Write the subject as `Ferrule X.Y.Z: <the one change that matters>`. Keep it under 60 characters.
3. Open with the "Action needed" line. If it says "none", say so plainly.
4. Cut the body to 150 words or fewer, with one link to the full notes.
5. Read it once, then send.

**Release-note rules** (they keep both the release page and the email honest):

- Lead with what the user sees. Put the mechanism second, or leave it out.
- Put breaking changes first, with who is affected and what to do.
- Include no number you haven't measured.
- Skip dependency bumps, CI changes, and refactors with no visible effect.

## Breaking changes

Don't wait for the next scheduled send. Email the list the same day, and also email hosted-tier customers through your account or billing channel. The newsletter alone won't reach them all.

## When to revisit weekly

Revisit only if all three are true:

- You have 1,000 or more subscribers.
- Replies and clicks show people want more than release notes.
- One person owns it and has the hours.

Until then, use the time on the product.

## Measure (10 min a month)

Track these three:

- Subscriber count.
- Click-through on the "Full notes" link.
- Replies received.

Don't track open rate. Mail-privacy features make it unreliable.

## Next step

Pick the tool and create the account. That's the only step that needs you. Tell me which one you chose and I'll tune the templates to its merge fields and RSS settings.