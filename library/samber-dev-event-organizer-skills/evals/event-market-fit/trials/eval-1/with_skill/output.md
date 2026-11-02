# Data Circus: demand read before the venue booking

**Call: don't book the 250-seat venue. Hold, and resize.** Demand for a paid event looks plausible at roughly 90–135 seats. Nothing you've given me supports 250.

I'd normally ask my interview questions one at a time. This is a single-pass read, so I've marked my assumptions and listed the open questions at the end.

One caveat on the method: every composite here is assembled from individually sourced signals. The assembly is a synthesis, not an industry standard.

## 1. Job statement and stage

**Stage:** concept only. You have a monthly meetup, a Slack, and a free interest form. Nothing is on sale and no CFP has run.

**Assumed ownership:** community-run, with a paid ticket and external sponsors. Tell me if that's wrong.

**Job statement (draft, please correct):** "When I'm a data engineer in the North of England with no peer group beyond my own team, I want to spend a day with about 100 relevant peers and local practitioners' talks, so I can validate my approach and widen my network."

- That job is already served by your monthly meetup, which is free and nearby.
- The conference has to be a clearly bigger job than the meetup to justify £120 plus a day off.
- **Four forces:**
  - **Push:** isolation and stale knowledge.
  - **Pull:** unknown. Which speakers or topics couldn't the meetup offer?
  - **Anxiety:** a first edition has no track record, and £120 is real money.
  - **Habit:** the free monthly meetup, Slack and YouTube.

The job statement is a product-practice thinking tool, not an event-industry authority.

## 2. Baseline and saturation

| Your claim | What the evidence says | Label |
|---|---|---|
| "First-edition conferences draw ~250." | The ~250 figure averages across cities with larger communities. Recorded first-year range is 70–700. The better predictor is **2–3× your best local meetup draw**. | sourced |
| 250 seats is the plan. | Your best night was 45 and your usual is ~30. That gives **90–135 attendees at best, or 60–90 off a typical night**. 250 is **5.5× your record** and ~8× your usual. | sourced ratio, applied to your numbers |
| "Groups shift at 5, 12 and 45, and we're past 45." | **"5/12/45" is a misquote.** The verified thresholds are 7, 13, 50, 90 and 150. | sourced |
| "Community is clearly ready." | Crossing a size threshold isn't a demand test. Any "grow to N members first" rule is self-set. | sourced |
| 380 Slack members. | Membership isn't attendance. Your own meetup draw (30–45) is the conversion evidence. About 12% of Slack members show up on your best night. | reasoning |

**Event-relevant threshold:** the verified one is ~90. A small event that works at 60 struggles to keep intimacy at 100. Your realistic range of 90–135 sits right on that edge, which is a format question for `event-format-selection`.

**Saturation scan:** I haven't run it, because I can't verify current calendars from here. Before committing, check:
- confs.tech and WikiCFP for data-engineering events in the UK in spring.
- Large unrelated Leeds events competing for venues and attention.
- Any incumbent data conference in the North that already owns this audience.

The scan can only rule things out. An empty calendar proves nothing.

## 3. Instruments: threshold vs. actual

### The interest form (210 "I'd come!")

- **It's a free, undeposited signal.** That puts it in the "curiosity read as intent" class. Free RSVPs are deleted from the evidence menu, not ranked low.
- **The size check:** 250 seats net of comps means ~230 paying buyers. 210 responses would need over 100% conversion to fill that. Even your own number can't fill 250.
- **It can't support 135 either.** That would need ~64% of respondents to buy at £120. For comparison, ~50% of free RSVPs don't show up at all (sourced).
- **Unknowns:** how many respondents are Leeds-local, and how many are already your regulars. If the form overlaps with your 30–45 regulars, the unique-demand count is lower still.

| Instrument | Declared pass threshold | Actual | Read |
|---|---|---|---|
| Interest form (free) | none was declared | 210 | **Uninformative** (curiosity) |
| Community baseline | n/a | 30–45 draw → 90–135 | Supports ~90–135, not 250 |
| CFP probe | none yet | not run | **Missing** |
| Deposit-backed waitlist | none yet | not run | **Missing** |
| Saturation scan | n/a | not run | **Missing** |

## 4. Composite read

Only one signal class exists so far: community baseline. The skill requires at least two independent classes for a call, so this is a **provisional read** and not a verdict.

- **Supports a conference:** you have an active meetup, a 380-member Slack, and 210 people willing to click a form. That points to real, local, un-monetised interest.
- **Against 250 seats:** the baseline multiplier gives 90–135, and a paid ticket should push you toward the **low end**. Your meetup is free, and the ratio is built on draw, not on paid conversion.
- **Unmeasured:** whether anyone will pay £120. You have no deposit data, no CFP, and no price test.

## 5. The call, with the differential

**Hold, and resize to a demand-tested number. Don't stop.** The concept isn't contradicted. The scale and the evidence are the problem.

**Differential:**
- **Demand gap or execution gap?** Neither is measurable yet. The skill's mid-sale diagnostics (checkpoint ladder, pace index) only work once tickets are on sale.
- **The risk if you book 250 seats now:** you'd start from a hole you can already see. At 135 attendees you're at 54% of capacity. At 90 you're at 36%. That's a first-edition failure signature and would be misread as a demand verdict.
- **Revenue sanity (arithmetic, not forecast):**
  - 250 × £120 = £30,000.
  - 90–135 × £120 = £10,800–£16,200.
  - Check the venue deposit and break-even against the lower range.

## 6. What to do next (before the venue)

Run these in order. Declare each pass threshold **before** you open it.

1. **Cheap, this week: saturation scan.** Check the calendars listed above.
2. **CFP probe (self-set target 2–3:1 oversubscription).** A first local CFP that can't reach 2–3 proposals per slot is a sourced stop signal. It means you stay at meetup scale. It also tests the speaker base independent of your regulars.
3. **Deposit-backed waitlist.** Take a small refundable deposit from the 210 and from your Slack.
   - Declare the target before opening it, e.g. "X paid deposits means we proceed with N seats". The number must be yours.
   - Deposit-backed lists convert 3–5× better than free ones (sourced practice from SaaS).
4. **Optional probe, if the team disagrees or the venue deposit is large:** one paid half-day event or deep-dive. Measure paid conversion, not RSVPs. This is the highest-evidence, highest-effort option, and the skill promotes it when the next commitment is large.
5. **Size the room off the result.** Pick the room size from the waitlist and CFP results. Prefer a venue with flexible capacity or a scalable hold.

Then re-run this read. If the waitlist and CFP are green, the call becomes **go at that size**.

## 7. Routing

- `event-first-edition`: launch scoping, the "≥3 organizers from ≥3 organizations" gate, and scope or budget tiers.
- `event-format-selection`: format at ~90–135 attendees and the ~90 intimacy threshold.
- `event-ticket-pricing`: whether £120 fits Leeds and a first edition, once you see conversion.
- `event-positioning`: sharpening the job statement and the pull.

## Open questions (they change the read)

1. Is the event community-run, with external sponsors?
2. What is the venue deposit deadline? A near deadline favours the CFP and waitlist over a probe event.
3. Is this a one-off bet or the start of an annual event?
4. How many of the 210 respondents are Leeds-local and not already regulars?
5. How many organizers do you have, from how many organizations?
6. Is the team aligned on the 250-seat idea, or is it contested?