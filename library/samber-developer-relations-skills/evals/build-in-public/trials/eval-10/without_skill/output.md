## What to do

Send the direct emails — that part isn't actually in dispute, it's already happening. The real decision is whether to *also* post publicly. Do that too, but not as a CEO blog post. Here's why, and what it should say.

**Why silence is the riskier option here, specifically:**

This isn't an ordinary bug. It's a billing bug — customers had money taken from them without authorization, some repeatedly, over a full day. That creates a paper trail you don't control: bank/card statements, one customer's finance team asking "why six charges," a support ticket that gets screenshotted, a chargeback that a payment processor flags. Any of those can surface on Twitter/HN/Reddit independent of anything you publish. If that happens and there's nothing public from you, the story becomes "they tried to bury a billing bug" instead of "they had a bug and fixed it in a day." Given you've published openly for two years, going silent on the one incident that actually cost people money is the most visible thing you could do — it breaks a two-year pattern right when people are watching closest.

**Why the CEO's instinct (public post) needs bounding, not just green-lighting:**

A big blog-post moment invites more attention than the incident deserves, gives competitors a citable link, and tempts you into over-explaining internals (exact architecture, exact multiplier, exact dollar figures) that help no one and only sharpen the story. Keep it in the same channel and tone as your normal engineering posts/changelog — not a special "Dear customers" CEO letter. Same openness, no extra ceremony.

**Sequencing:**
1. Finish confirming the affected-account list and refunds (already in motion).
2. Send the individual emails first, or at the same time as the public post — never after. Nobody should learn about a charge to their own account from your blog before their own inbox.
3. Get finance/legal to sign off same-day on the refund language and on whether your payment processor has separate notification/dispute-ratio obligations given repeated erroneous charges — this shouldn't delay anything, just a fast read before it goes out.
4. Publish the short post to your usual engineering blog/changelog, not a separate press release.
5. Have support ready with the same short internal brief so anyone answering tickets says the same thing.

**What not to include anywhere public:** exact per-customer dollar amounts, the "six times" detail (that's specific enough to be identifying to that one customer — describe severity in general terms instead), or internal system/service names for the retry or billing pipeline. Describe the mechanism at the level a customer needs to trust the fix, not at the level an internal design doc would.

---

## The customer email (affected accounts only)

**Subject: Billing correction for your account — refund issued**

Hi [Name],

We're writing about a billing issue that affected your account starting [date].

**What happened:** SDK 4.2, released Tuesday, had a bug that caused webhook retries to be billed more than once for accounts using the async client with a custom retry policy. Your account was one of about 300 affected.

**What we've done:**
- Fixed in SDK 4.2.1, released [date/time]. If you're on 4.2, we recommend upgrading.
- We've identified every duplicate charge on your account and issued a full refund. It should appear within [X] business days, depending on your bank or card provider.

**What we're changing:** [1–2 concrete, honest process changes — e.g., "retries now check for an existing charge before billing again, and we've added test coverage for custom retry policies to our release checklist."]

If anything on your statement still looks off, reply directly to this email — [name/title] is personally tracking every affected account until it's resolved.

Sorry for the disruption, and for the extra step of having to check your statement over something on our end.

[Name, Title]

---

## The public post

**Title: Billing issue in SDK 4.2 (webhook retries) — fixed in 4.2.1**

On [date] we shipped SDK 4.2. It included a bug that affected accounts using the async client with a custom retry policy: webhook retries could be billed more than once. About 300 accounts were affected before we caught it and fixed it in 4.2.1, released [date/time] — it's live now.

If your account was affected, you've already received (or will shortly receive) a separate email with the specifics and a refund for the duplicate charges. If you're running 4.2 with a custom retry policy and see something on your invoice that doesn't look right but haven't heard from us, email [support address] and we'll look into it directly.

**What went wrong, briefly:** a retry could be billed again without checking whether it had already succeeded and been charged once. We've added a check for that, plus test coverage for custom retry policies before we ship a release.

We've published openly about our engineering decisions for two years, including the ones that don't make us look good. This is one of those. If we haven't answered your question here, ask us directly — we will.

— [Name / Engineering team]