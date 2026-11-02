# StreamStack Conf: marketing calendar and registration targets

**Do this week:** make the comms hub live, fix one tracked link per channel, and start the opted-in "notify me" list. It's T-7 months, the earliest start the DevOpsDays guide documents.

## 1. Setup

**Spine: ticketed, percent of expected ticket sales (DevOpsDays ladder).** The event is paid, so the risk is unsold seats, not no-shows. I'm not using the free-event 200% ladder.

**Target net of comps: 375 tickets to sell.**

| Item | Count |
|---|---|
| Expected attendees | 450 |
| Sponsor tickets | 30 |
| Speakers | 12 |
| Organizers | 8 |
| Volunteers | 15 |
| Scholarship passes | 10 |
| **Comps** | **75** |
| **To sell (450 − 75)** | **375** |

Using 450 would inflate every checkpoint by 20% and create a miss that isn't real. If the 450 was already paid-only, rescale every number below by 450/375.

**Assumptions** (I couldn't ask, so these are mine; tell me which are wrong):

- ℹ️ Doors are about Oct 15. "One month out" is a window set by the real date, so shift it if that's wrong.
- ℹ️ **Pole: community-run.** The guides are for community events. If you're company-run, I'm extrapolating, and the budget posture in section 4 changes.
- ⚠️ **Positioning and demand read missing.** The skill says to route to `event-positioning` and `event-market-fit` before planning channels. The calendar and targets don't depend on them. The channel map in section 3 does, so treat it as provisional.
- ⚠️ **Price points come from `event-ticket-pricing`.** I haven't seen them. June 15 and May 5 are treated as fixed, and I don't move them.
- ⚠️ **CFP close date is unknown.** It must fall before July 10. Send it and I'll pin it.

**What's published and what's mine:**

- Whole-funnel checkpoint percentages are published (DevOpsDays). That guide says they have shifted since social audiences fragmented, so treat them as order-of-magnitude.
- The channel value ordering is judgement.
- Every per-channel target is set from scratch, and I haven't set any.

## 2. Calendar with cumulative targets

Targets are cumulative paid tickets. Comp codes don't count toward them.

| Date | Moment | Cumulative target | If missed |
|---|---|---|---|
| **Mar (now), T-7 mo** | Marketing off and running. Comms hub + QR live. Tracked link per channel fixed. Notify-me list opens. | none | n/a |
| Mar–Apr | List building. Rotterdam and Benelux data-meetup presence. Partner and media outreach starts (swaps need lead time). Countdown emails to "tickets May 5". | none | n/a |
| **May 5** | Tickets on sale. Announcement send. | Any real spike in week 1 | No spike is the earliest sign that no audience exists. Check list reach first. |
| May 19 | Week-two read. | none | Launch week measures reach, not demand. Week two is when the pattern becomes readable. |
| Late May | Fixed paid-ads test, only if an owned channel already shows tracked referrals. | none | n/a |
| ~Jun 1 and ~Jun 12 | Early-bird countdown sends. | none | n/a |
| **Jun 15** | Early-bird closes. | **56** (15%) | Materially lower means weak demand, visible early. Diagnose by reach signals (section 5). |
| Jun 16–Jul 9 | Quiet middle. Partner and swap pushes. | none | A flat stretch is the normal curve shape, not an alarm. |
| **Jul 10** | Speakers announced. Hand the 12 speakers a share kit. | **94** (25%, about +38), read Jul 24 | Check the announcement actually reached the list. |
| **Aug 20** | Full agenda published. | carry **94** | The guide has no separate agenda increment. Watch for a visible bump. |
| **~Sep 15, T-1 mo** | Reminder send. Sponsor, speaker, organizer, volunteer and scholarship codes go out. | **150–188** (40–50%) | See below. |
| ~Oct 1, final two weeks | Final surge campaign. | Visible surge | A missing surge after healthy checkpoints points at the page or the price. |
| **Doors, ~Oct 15** | | **~375** | n/a |

**One-month-out reading:**

- **Below 150:** the 25–30% band (94–113) is where a team that delayed its visibility push lands, so first suspect execution, not demand.
- **Before concluding weak demand,** check three things: late speaker or agenda announcements, a theme too narrow for part of the audience, and messaging that never said who is welcome.
- **Code issuance:** comp codes going out around T-1 month cause a registration bump. Exclude them from sales counts, or an early read will look falsely hot.

## 3. Audience-to-channel map (provisional)

Segments below are guesses until you tell me where your audience actually gathers.

| Channel | Weight | Segment it's bought for |
|---|---|---|
| Own mailing list (+ notify-me list) | Primary, from now | Self-funded data engineers and anyone who has already shown interest |
| Comms hub with QR code | Baseline, one-time | Converts reach from every other channel |
| Own social presence | Baseline, kept running | Existing followers. Weak reach alone, so it supports the others. |
| Local and campus engagement (meetups, local employers) | Promote if first edition with no list, or if the audience is mostly Rotterdam-area | Local and regional data teams |
| Partner channels (sponsors' lists, other events, media partners) | Add once you name properties with a matching audience | Employer-funded data teams and managers who approve budgets |
| Paid ads | Fixed test only, late May, one segment | Whatever segment shows a tracked signal first |
| Pre-event press | Light | Local tech media. A real campaign goes to `event-press-relations`. |

If you have a large list, a popular newsletter or podcast, or a sponsor who bundles ad credits, those override these defaults.

## 4. Budget posture

- **Community-run (assumed):** barter-only plus a fixed test budget. Cap and amount are yours to set.
- **Test:** one paid channel, one segment, one tracked link, one question decided in advance.
- **Held reserve:** release it only if the one-month-out reading lands below 40% (under 150) and a channel shows a tracked signal. A miss alone means diagnose, not spend.
- **Company-run with a marketer and a standing budget:** promote to a full spread. Its percentage table (30–40% paid, 20–30% content, 10–20% partner swaps, 10–15% tools, 5–10% testing) is a SaaS convention, not an event-industry standard. Don't present it to a board as one.

## 5. Tracking and miss response

- **Tracked links:** one link or code per channel, decided before May 5, because it can't be added later. Give each partner community its own code.
- **Source field:** "how did you hear" on the form is a cross-check only.
- **Miss response:** read each miss in this order.
  1. Weak reach signals (low page traffic or send opens, no partner referrals) means an execution shortfall. Add or re-weight channels.
  2. Healthy reach but low conversion means the price or page. Route to `event-ticket-pricing` or `event-landing-page`.
  3. Healthy reach and conversion but short of target means a real demand shortfall. That's an `event-market-fit` question, not a bigger campaign.
- **Prior edition:** if there is one, overlay its curve; it beats any published ladder. Record each checkpoint's planned-vs-actual for the next edition.

## 6. Routing

- **Email copy and send moments:** `event-attendee-email-sequences`. Hand over May 5, the early-bird countdown, Jun 15, Jul 10, Aug 20, the T-1 month reminder and the final-two-weeks surge.
- **Social calendar and speaker share kits:** `event-social-media`.
- **Registration page conversion:** `event-landing-page`.
- **Channel roster that feeds the hub:** `event-comms-channels`.
- **Swaps and media partners:** `cross-event-promotion`, `event-media-partnerships`.
- **Real press campaign:** `event-press-relations`.

## Questions that would change this plan

1. Exact doors date?
2. CFP close date?
3. Community-run or company-run?
4. Existing list size, social reach, and a prior edition's sales curve?
5. Cash budget, and who approves it?
6. Which meetups, communities and employers does the audience actually use?