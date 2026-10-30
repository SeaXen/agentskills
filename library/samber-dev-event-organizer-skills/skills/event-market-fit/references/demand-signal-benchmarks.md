# Demand signal benchmarks

Every number the skill reads against, with its confidence label. Labels: **sourced** (published by a named organization or named practitioner), **synthesis** (assembled from several published figures rather than one citable standard), **self-set** (the user must declare it per event, before measuring).

## Pre-launch baseline

- **Community-to-attendance ratio** (sourced): expect roughly **2-3x the best-attended local meetup's draw** at a first-edition conference. A city whose best meetup draws 40 should plan for 80-120, not the ~250 "typical" first devopsdays edition - that typical figure averages across cities with larger communities (recorded first-year range: 70-700).
- **No baseline exists**: if no local meetup or online community for the topic exists at all, there is nothing to multiply - a distinct red flag from "the baseline is small". The recommended sequence is community-first: cultivate the community, then throw events for it (sourced).
- **Community-size thresholds** (sourced): the verified ladder is **7** (working group optimum), **13** (dysfunction nadir), **50** (non-exclusive social ceiling), **90** (the event-relevant one), **150** (committed-group ceiling). Read the ~60→100 intimacy breakdown as the closest usable guide to when a group outgrows its format: a small conference that worked well at 60 participants has difficulty at 100 sustaining intimacy.
  - The "5/12/45" numbers often quoted alongside this model are a misquote - never cite them.
  - Treat any "grow to N members before launching a conference" rule as self-set; the format response to crossing it belongs to `samber/dev-event-organizer-skills@event-format-selection`.
- **Team formation as an implicit demand check** (sourced): the requirement of ≥3 organizers from ≥3 organizations doubles as a demand probe - a lead who can't recruit two co-organizers outside their own employer has failed an early market test before any ticket exists. The gate itself belongs to `samber/dev-event-organizer-skills@event-first-edition`; read the recruiting difficulty as a signal here.

## Saturation scan

- Check the category's own aggregator/calendar (many franchise events publish one) plus cross-topic calendars such as confs.tech, framed as **load balancing across the field**, not just conflict avoidance (sourced). Extend to large unrelated local events: they compete for venues, travel budgets, and attention.
- **CFP-listing platforms as a saturation count** (synthesis): WikiCFP and similar CFP aggregators let you count how many conferences already target the topic and date window.
- **Event-intelligence graphs** (synthesis): platforms built for sponsors choosing where to spend (event graphs of 150,000+ B2B events with attendance and sponsorship histories) can be inverted by an organizer to see whether a niche is saturated and who owns its audience.
- Reusable red-flag heuristic from a 7-factor market framework (sourced): "exactly one suitable venue, controlled by a single gatekeeper."
- The scan only rules out. A well-run incumbent owning the niche means pivot the concept (narrower vertical, different format band) rather than competing head-on; an empty calendar proves nothing by itself - non-consumption, not a rival event, is usually the biggest competitor.

## Leading instruments

- **CFP oversubscription** (sourced):
  - PyCon US 2025 accepted ~15% of 938 proposals, roughly 6.5:1 - a flagship figure. **2-3:1 on a first local CFP is a strong signal** (the flagship figure scaled down; treat the target as self-set).
  - Submitter diversity counts too: DjangoCon Europe 2024 read 51 first-time speakers among 138 submitters as a vibrancy signal.
  - **Undersubscription** - can't fill the slots with quality talks - **is a sourced stop signal**: the topic lacks a speaker base yet, so stay at meetup scale.
  - Do not compare against academic acceptance rates (CHI 2024: 26.4%) - peer-review selection follows a different logic.
- **Waitlist conversion** (SaaS practice applied to events): declare the waitlist-to-purchase conversion rate that would validate demand **before opening the list** (self-set). "If your target is 10% and your actual conversion is 1%, the waitlist failed to predict revenue."
  - Deposit-backed lists convert **3-5x higher** than free lists and see 60-80% email open rates vs 15-25% - the deposit is what turns curiosity into intent.
  - A waitlist that forms **after** a sellout is one of the highest-intent assets an organizer can own; a pre-launch list is a mailing list until conversion proves otherwise.
- **Paid probe events** (synthesis): 2-3 higher-intensity probes (a paid deep-dive, a mini-hackathon) measuring **paid conversion, not RSVPs**. Benchmark floor: if ~50% of confirmed RSVPs won't show at a free meetup (sourced), or no meaningful share converts to a paid probe, the audience isn't ready for a paid event.

## Mid-sale: the sales curve

- **The spike ladder** (sourced): sales spike at named moments, not evenly. Judge the curve at its spikes, and always **net of sponsor/speaker/organizer/volunteer comps**.
  - Named moments: tickets announced, early-bird ends, speakers announced, agenda announced, sponsor/speaker codes go out, each reminder email, the final two weeks (a final-fortnight surge is normal, not a red flag).
- **Checkpoint ladder** (sourced; order-of-magnitude):
  - First sales week: any real spike at all - its absence is the earliest warning.
  - Early-bird close: ≈**15%** of expected sales (worked example: 60 of 400).
  - Speaker/agenda announcement: ≈**+10%**.
  - One month out: **40-50%** - but a team that skipped or delayed its visibility push realistically sits at 25-30% at the same point, which is a marketing-execution gap, not a demand verdict. Tell them apart before concluding.
- **Pace index** (sourced): `tickets-to-date ÷ curve-expected × 100` against a chosen expected curve (e.g. 22% of sales in week one, 48% by day 30, 100% by doors). Read from **week two**, not launch day - "launch is a test of reach, not demand." From edition 2 on, judge against the event's own prior curve, never a straight line; the curve is U-shaped (announcement spike, quiet middle, final surge).
  - Worked example: 900-ticket forecast, 45-day window, day-30 expectation 432, actual 356 → pace index 82 → projected final ≈738, i.e. a 162-ticket gap with a size and a deadline attached.
- **Price-fit signature** (sourced): healthy event-page traffic with low conversion in the first two weeks points at price, not demand. Respond with targeted codes/bundles rather than public discounts (public cuts teach the audience to wait); the pricing work belongs to `samber/dev-event-organizer-skills@event-ticket-pricing`.
- **Early-bird share cross-check** (sourced): 30-40% of total tickets sold during early-bird phases is typical; a 500-target conference selling 200 early-birds in week one is on track, one selling 20 has months to diagnose - or reconsider the event.
- **Anti-signal - manufactured scarcity** (sourced): batch releases trigger the ticketing platform's "almost sold out" banner early. Before reading sellout timing as organic demand, ask whether batching was used.

## Lagging signals (post-edition)

- **Attendee return rate**: industry-blended repeat attendance is barely above **30%** (sourced). Treat 30% as a floor a tight developer community should beat, not a target; a practitioner worked example calls 50% healthy for a recurring event. Attendees who report a "peak moment" are 85% likelier to return, yet 78% of organizers believe they deliver one while only 40% of attendees agree - that perception gap is itself a warning sign.
- **Show-up rate**, distinct from return: paid events convert **90-97%** of tickets to attendance; free events see **40-60% no-shows** (sourced). For a company-run free event, show-up rate substitutes for sellout speed as the main attendee signal (a reasoned stand-in, not a measured equivalent; flag it).
- **Sponsor renewal rate**: high-performing events aim for **≥70% per edition**, with multi-event partnerships higher (sourced). The named lever is a **72-hour post-event ROI report** to every sponsor - both the measurement vehicle and the single highest-leverage renewal action ("sell the logo and you get a one-year sponsor; sell the data and you get a partner"). Sponsor renewal is deliberate repeat-budget money, which makes it high-confidence and **independent of ticket buzz** - an edition can sell out and still lose its sponsor base. Delivery of the report belongs to `samber/dev-event-organizer-skills@event-sponsor-fulfillment`.
- **Sellout-speed trend**: read the trend edition over edition, not the absolute. Seconds-to-sellout stories (a major community conference going from 10 days in 2019 to seconds in 2023; a 1,000-ticket revival selling out in under 20 minutes) are mature-brand reads, largely promotional in origin; never a bar for a first edition.
- **Hackathons**: return and oversubscription run on self-set targets. Have the organizer define them (participants, and how many return or keep contributing within three months) and treat any figure as directional - self-set, and flagged as such.

## Composite: the recur/scale read

The three-signal composite (return >30%, renewal ≥70%, sellout-speed trend, tracked separately, **scale only when at least two of three are green**) is a synthesis assembled from the sourced individual thresholds above, not a named industry test. Present it that way rather than as an authority: Julius Solaris, the closest named practitioner voice on event relevance, offers framing questions rather than a quantified test. Derived response thresholds, same confidence label:

- Renewal <70% or return <30% → hold the format flat and fix experience/ROI before scaling.
- Pace index persistently <80 at the one-month checkpoint across two editions → the concept/price/audience combination is misaligned; pivot.
- CFP undersubscription → stay at meetup scale.
