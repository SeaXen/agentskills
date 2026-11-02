Using the **build-in-public** skill's Step 8 ("Plan the downside") and the boundary rules on publishing bad news to resolve this.

## The decision

Post publicly, and email affected accounts individually. This isn't an either/or — it's two different documents for two different readers, and the skill treats them as separate obligations.

- **Support lead is right that affected accounts need direct, specific outreach** — their exact charge, their exact refund, on a channel they'll actually see. That's not something a blog post can do (per-account financial detail doesn't belong in a public post regardless of the outcome).
- **Support lead is wrong that silence is safe.** You've published openly for two years — this project sits at "shipping log + decisions + occasional failures" already. A billing bug that overcharged someone 6x in a day is exactly the kind of thing that surfaces on its own (an angry customer posting a duplicate-charge screenshot costs you far more than the same fact in your own words). The skill's framing: *"Bad news published on your own terms is the highest-value content the practice produces; the same news extracted by someone else is the most damaging."* Going quiet now, after two years of talking about ships and decisions, also reads as the "publishing only wins" failure mode the first time it would have cost you something.
- **CEO is directionally right, with one guardrail:** this has to read as a postmortem, not a PR post. Lead with impact, not with "we fixed it." No spin, no blame, no vagueness about scope. Named customer, exact per-account dollar amounts, and internal process detail stay out — those are the boundary's hard blocks (third-party data without consent), not the CEO's call to make either way.

Publish once, on your blog (your anchor surface), link it from the 4.2.1 release notes/changelog, and don't relitigate it in social replies — point every thread back to the one post. Send the customer email first or same-day, so nobody learns about their own overcharge from your blog before their inbox.

This clears the four-question pre-publish check: no unfixed vulnerability (it's shipped), no third-party data disclosed, no date/number promised you don't control (refund timing is hedged to bank processing), and no sentence here is a problem quoted alone by a competitor or a journalist.

---

## The blog post

```markdown
# 4.2.1: we double-charged about 300 accounts this week

If you're on the async client with a custom retry policy, check your last invoice — 4.2, shipped
Tuesday, could have billed you more than once for the same webhook delivery. We found this
yesterday, shipped a fix an hour ago, and refunds are already going out.

**Who was affected.** Roughly 300 accounts: everyone running the async client with a custom
retry policy on 4.2. If you're on the default retry policy, or on the sync client, this doesn't
apply to you. The worst case we found was a single account charged for the same webhook delivery
six times over about a day.

**What we're doing about it.** Refunds for every duplicate charge are processing now, automatically
— no action needed on your end. Most should post within 3-5 business days, depending on your bank.
If you don't see it reflected by early next week, reply to the email we sent you and we'll look at
your account specifically.

**What happened.** A custom retry policy on the async client changes how long we wait between
retry attempts, but 4.2's retry path stopped checking whether an earlier attempt had already
succeeded before re-submitting it for billing. Under the default policy, timing made this rare
enough that we didn't catch it in testing. Custom policies retry on a different schedule, and some
of those schedules hit the unguarded window reliably.

**The fix.** 4.2.1 is out now. It restores the check we dropped: a webhook delivery is only billed
once, tracked by delivery ID, regardless of how many times the retry policy re-submits it.

**What changes systemically.** We had no test that exercised a custom retry policy against the
billing path — only the default one. That's the actual gap. Every retry-policy variant we support
now runs against the billing path in CI before a release goes out, not just the happy path we
already tested.

We're also auditing every account on 4.2 for the same pattern outside the 300 we've already found,
in case a retry-policy combination we haven't seen yet hit the same bug in a way we didn't catch
from billing logs alone. We expect that audit done by [date] — if it turns up anything, we'll
update this post and email those accounts directly, the same way we did this time.

Questions about your account: reply to the email you got, not this post. General questions on the
bug itself, ask here.
```

---

## The customer email (affected accounts)

```
Subject: 4.2 billing issue on your account — refund in progress

Hi [name],

4.2 of the SDK, shipped Tuesday, had a bug that could double-charge webhook retries on the async
client with a custom retry policy — you're on that configuration, and your account was affected.

What happened on your account: you were charged [N] extra times for [webhook/delivery detail],
totaling [$X]. That refund is already processing and should post within 3-5 business days,
depending on your bank. You don't need to do anything.

The bug is fixed in 4.2.1, out now. Full writeup of what happened and what we're changing is here:
[link to blog post].

If the refund doesn't show up by [date], or the amount looks wrong, reply to this email directly
and we'll sort it out.

Sorry about this — [sign-off]
```

Fill in `[N]`, `[$X]`, and the delivery detail per account before sending; don't batch-send a templated dollar figure.