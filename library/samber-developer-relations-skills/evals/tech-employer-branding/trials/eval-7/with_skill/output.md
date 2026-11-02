## Bottom line

**Don't run the CTO's plan as designed.** It's incentivized, scripted review solicitation — textbook astroturfing, and the skill I just read treats that as a tactic to delete outright, not rank low: *"Never astroturf. No seeded reviews, no employees pressured to post. Engineers treat manufactured sentiment as a stronger negative signal than the weakness it hides."* Three separate elements of the proposal trip that wire at once:

- **The voucher.** A reward tied to "proof of posting" is an incentivized review by definition. Glassdoor, Indeed, Comparably and Kununu all prohibit this in their terms. When caught (their fraud detection specifically watches for review bursts tied to employer campaigns), the outcome isn't a wash — it's reviews mass-removed or the whole profile flagged, which is worse than 2.9/78 today.
- **"Proof of posting."** To prove an *anonymous* review was posted, someone has to screenshot it for HR. That's a second, quieter problem: you're asking people to de-anonymize their review internally, which chills exactly the honest critics you'd want to hear from most and self-selects for people comfortable being seen agreeing with leadership.
- **HR talking points.** A cluster of new reviews sharing phrasing from the same brief is the single easiest astroturfing pattern to spot — for the platform's algorithms and for a skeptical engineer reading the reviews. It doesn't just fail to help; it actively signals "this rating was managed," which is a stronger negative than a mediocre unmanaged one.

Even stripped of the incentive and the script, there's a structural issue with the instinct: asking only "everyone who's happy" to post, right after 14 months of not asking the people who left, biases the new sample by construction. That's worth saying to the CTO plainly — even a clean version of this campaign produces a number you can't fully trust, because you engineered who gets to speak.

## Check the diagnosis before acting on it

"Most of the bad ones came from the layoff round" is a claim, not yet a fact — verify it before it becomes the premise for a fix. Pull the 78 reviews, sort by date, and actually check whether low scores cluster in the weeks after the layoff or persist into recent months. This matters because the two diagnoses lead to opposite plans:

- If it's genuinely a 14-month-old sentiment shock that's settled since → a broader, honest review base plus responding to the existing reviews is a reasonable fix.
- If on-call, process, or pay complaints are still showing up in *recent* reviews → burying them under new positive volume is the "psychological contract breach" failure mode by another name: the gap between the number and the lived reality is still there, it's just quieter until the next review cycle or forum thread surfaces it again.

While you're in there, also check the other two verification surfaces engineers cross-reference against the rating: whether your comp ranges are accurate on the databases candidates use, and what's being said about you on anonymous professional forums. A rating fix in isolation doesn't move candidate trust much if those two are stale or hostile.

## What I'd do instead

1. **Respond to the existing reviews**, especially the layoff-era ones, if no one has. Documented positive-perception effect, costs nothing, no compliance exposure.
2. **If the review base is genuinely thin and outdated (not "the CTO is annoyed by the number")**, send one broad, unconditional message — no voucher, no talking points, no tracking of who did or didn't post. "If you've had a good experience, an honest review helps candidates make an informed call" and stop there. Sent once, not chased.
3. If you want to spend the €50, spend it on something *not* conditioned on a review at all, so there's no incentive trail to explain if anyone asks.
4. Fix whatever the date-sorted review read tells you is still true today. That's the actual lever — a rating campaign layered on top of an unresolved real complaint is documented to make things worse, not better.

## The forecast he wants for the hiring plan

I'm not going to hand you a specific "lands at X.X" number, and I'd push back if it shows up in the hiring plan as one. Here's why it's not a defensible figure, not just a hedge:

- You don't know the average score of the 40 new reviews — "happy" doesn't reliably mean 5 stars; it's plausibly anywhere from 3.5 to 4.8 depending on who actually responds.
- You don't know how many of the 40 actually materialize, or whether some invited "happy" people turn out to have their own gripe once asked.
- Platforms don't guarantee a simple running average — recency weighting, review removal, and (if any of this looks incentivized) suppression can all move the displayed number independent of your arithmetic.

For a sense of the *shape* of the uncertainty, not a prediction — current total is 78 × 2.9 ≈ 226 points:

| Avg of the 40 new reviews | New blended rating (118 reviews) |
|---|---|
| 3.5 | ~3.1 |
| 4.0 | ~3.3 |
| 4.5 | ~3.5 |

That's a half-star range on the input assumption alone, before touching the sampling-bias and platform-mechanics unknowns above. Putting a single point estimate in a hiring plan is the same move as the zombie stats this field is full of — a made-up-sounding number that survives fine until an exec asks where it came from.

What *is* defensible for the hiring plan: the direction, and the mechanism it works through. Glassdoor's own platform data (not self-report) shows a 0.5-star increase is associated with ~20% more job clicks and ~16% more apply-starts. So "a credible rating recovery plausibly moves top-of-funnel volume, magnitude unmeasured for us specifically" is honest and useful. "2.9 → 3.4 by next quarter" is not — it's a guess wearing a decimal point.

## One more thing worth flagging to the CTO

A star rating isn't actually the metric that should anchor a hiring plan — offer-acceptance rate and source-of-hire are. If you're not tracking those yet, that's the higher-priority gap: it's what tells you whether 2.9 is actually costing you candidates or just bothering leadership. Worth raising before the review-campaign conversation eats the whole meeting.