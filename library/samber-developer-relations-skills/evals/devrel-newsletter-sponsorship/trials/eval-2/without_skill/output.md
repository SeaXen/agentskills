# Is $620 right?

**Probably not as derived.** The arithmetic is correct, but the inputs aren't solid enough to quote from yet. You can fix that in about an hour with data you already have.

## What's wrong with the $620 calculation

1. **The $50 CPM is a Discord claim with no source.** Newsletter CPMs vary a lot by niche, format and what's being counted. I haven't verified any benchmark here, so treat every figure, including mine, as a starting point to check.
2. **Subscribers × CPM isn't what sponsors usually buy.** CPM is normally per thousand opens or delivered impressions, and a sponsor will assume opens. At $50 on opens, 52% of 12,400 is 6,448 opens, or about **$322**. On subscribers, it's $620. Quote the second as a flat fee and defend it with engagement data, not CPM math.
3. **"Opens are real readers" is the weakest assumption.** Apple Mail Privacy Protection and corporate security scanners auto-open emails, so 52% is probably inflated. A 52% rate is high for a list this size, and a dev-tools buyer will know that.
4. **Clicks are the number that matters, and yours are unfiltered.** Link scanners also click links, which is what the "bot click" toggle filters. Clicks from your audience are what a sponsor pays for. Dev-tools sponsors usually think in cost per click or per signup, not CPM.

## Do this before you quote (about an hour)

1. **Turn on the bot-click filter** in Mailcraft. Check whether it applies retroactively. If it doesn't, export raw clicks and filter them yourself.
2. **Export clicks for the last 8–10 issues.** For each issue, record:
   - unique clicks, with and without bot filtering
   - clicks on your top link
   - clicks on any past sponsor or promo link
3. **Look for bot signatures in the raw export.** Several links clicked within 1–2 seconds of delivery, or every link clicked by the same address, means a scanner.
4. **Compute these three numbers:**
   - Human unique clicks per issue, which is your real engagement.
   - Click-to-subscriber rate: human clicks ÷ 12,400.
   - Typical clicks on a sponsor-style link. If you've never run one, use your top editorial link as a proxy.
5. **Check list quality.** Look at the share of subscribers who engaged in the last 90 days. Sponsors pay for the active list, not the total.

## How to turn the data into a price

Use two methods and compare:

- **Per-click:** (expected human clicks on the sponsor link) × (what a click is worth to a dev-tools company). Developer clicks are worth far more than consumer clicks, because the buyer is paying to reach working Go developers.
- **Per-impression:** (verified-ish opens) × (CPM you've sanity-checked against 2–3 comparable newsletters' public rate cards).

Quote a flat per-issue price near the higher of the two, and say what it includes.

## What to say to them now

If they need a number today, before you've pulled the data, quote a **flat $500–$650 per sponsored placement**. That brackets your two rough readings, and a 12k-subscriber niche developer list can support it. Say it's your introductory rate, and offer a first slot with a performance report in exchange for a 3-issue commitment at that rate. Don't send open or click figures yet, and don't say "52% open rate". Once you've filtered the data, say "X human clicks per issue".

## Pitfalls

- **Don't present the unfiltered open rate as fact.** If their tracking shows far fewer clicks than your numbers imply, you lose trust and the repeat bookings.
- **Don't quote "$50 CPM."** It invites a negotiation over a number you can't source. Quote a flat price, and give the rationale only if they ask.
- **Don't price below your floor for exposure.** One sponsored slot costs you roughly an issue's worth of attention from the same readers.

## Next step

Export the clicks, with the bot filter on and off, and paste the per-issue totals here. I can then work out a defensible rate, a one-paragraph pitch for the sponsor, and the performance numbers to promise.