# Should FerroConf apply the 30-40% paid ads template to its 3,000 EUR?

**No. Don't apply it.** Apply a smaller, gated plan instead: spend nothing at first, run one capped paid test, and hold the rest behind a checkpoint.

I read `event-marketing-plan` and both its references. I can't run its one-question-at-a-time interview in a single reply. Where an answer is missing, I state the assumption and say what changes if it's wrong.

## Why the template doesn't fit

1. **The percentages aren't an events standard.** They are B2B/B2C SaaS conventions, borrowed and not measured on events. Don't defend them to your co-organizers or sponsors as industry practice.
2. **Your team can't execute the lines.**
   - Five people on nights and weekends have no capacity for 20-30% "content production".
   - "Events/sponsorships" is barter for you (cross-event swaps, media partners), not cash.
   - Tools at 10-15% (300-450 EUR) buy nothing a volunteer team lacks the hours to use.
3. **Spending it all in week one removes your response to a miss.** The skill's "bad" example is a full spread committed up front. With no tracked links, an early-bird miss looks like a demand problem and gets answered with more ads.

| Template line | Share | Of 3,000 EUR | Problem for FerroConf |
|---|---|---|---|
| Paid ads | 30-40% | 900-1,200 | Needs an ad account in the organization's name and an approver. Ads are "cheap and effective" in MLH's guide for campus audiences only. |
| Content | 20-30% | 600-900 | No capacity to produce it. |
| Events/sponsorships | 10-20% | 300-600 | Partner swaps cost hours, not cash. |
| Tools | 10-15% | 300-450 | No unmet need identified. |
| Testing | 5-10% | 150-300 | This is the one line that matches the recommendation below. |

## Assumptions

- **Pole:** community-run. Cash competes with venue and catering costs, so acquisition leans on owned and barter channels.
- **Spine:** ticketed, so the targets are a percent of expected sales net of comps. If FerroConf is free, switch to the attendance-goal spine (100% of goal two weeks out, 200% one week out). Never mix the two.
- **Missing inputs:** I don't have your positioning, market-fit read, target number, list size or doors date. The skill says to route to `event-positioning` and `event-market-fit` first if those are missing. The allocation below holds without them, but the channel weights need them.

## Recommended allocation

**Posture: barter-only plus a fixed test budget.** Your cash is a small, one-off float, so no standing marketing line justifies the spread.

| Amount | Use | Release rule |
|---|---|---|
| 0 EUR | Owned channels: mailing list, comms hub (one page or QR linking every channel), baseline social. Organizer hours only. | Always on. |
| 0 EUR | Partner channels: cross-event swaps and media/community partners. | Always on. Weighted and scheduled here, deal mechanics in the sibling skills. |
| ~900 EUR (30%) | One capped test: targeted social ads, one named segment, tracked link, one question set in advance ("does this segment register at a cost we'd repeat?"). | Run in the two weeks after the announcement. |
| ~2,100 EUR (70%) | Held reserve. | Release only if the one-month-out checkpoint lands below 40% of expected sales **and** one channel already shows a tracked referral signal. |

The 30/70 split scales the skill's worked example (600 and 1,400 EUR on a 2,000 EUR budget) to your 3,000 EUR. It is a judgement call, not a benchmark.

**Before spending anything:**
- Check who approves the spend. If sponsorship funds about 80% of the event, this 3,000 EUR may belong to catering, not marketing.
- Check that you have an ad account in the organization's name.
- Create a distinct tracked link or registration code per channel. You can't add them retroactively.

## Targets and the calendar

Percentages are of tickets you actually have to sell, so subtract sponsor, speaker, organizer and volunteer comps first. The 320 below is an illustration. Substitute your own net number.

| When | Moment | Target (net 320) |
|---|---|---|
| T-7 months | Marketing running, comms hub live, list building starts | none |
| Announcement | Tickets on sale | a real first-week spike |
| Early-bird close (date fixed by `event-ticket-pricing`, never moved here) | | ~48 (15%) |
| Speaker/agenda announcement | | ~80 (adds ~10%) |
| T-1 month | Reminder send | ~130-160 (40-50%) |
| T-2 weeks | Final surge | surge visible |

**What is evidence and what is my call:**
- **Published whole-funnel checkpoints.** The ladder percentages come from DevOpsDays' guide. They have shifted over time, so treat them as order of magnitude.
- **Judgement.** The channel ranking is mine.
- **Set from scratch.** Every per-channel target is yours to set. No published source gives one.

**If you miss a checkpoint, diagnose before spending:**
- 25-30% at one month out is the band for a team that skipped or delayed its visibility push. That is an execution problem, not proof of missing demand.
- Weak reach (low page traffic or send opens) means add or re-weight channels.
- Healthy reach but low conversion means fix the price or the landing page. Don't buy more reach.
- Healthy reach and healthy conversion means genuine demand shortfall. More ads won't fix it.

## Questions that would change this

1. Ticketed or free? This decides the spine.
2. When are doors, and when are announcement and early-bird close? A short runway favors fast rungs (ads, a partner's next send) over slow ones (building a list, local relationships).
3. How big is your existing list, and where does the audience already gather (meetups, Rust communities, employers)? A large list or a concentrated metro audience would move local engagement up the ranking.
4. Is this a one-off push or a compounding asset across editions? Compounding favors list-building and partner relationships over paid ads.
5. Who approves the 3,000 EUR, and are the other 2,100 EUR spendable at all? If there is no real discretionary cash, delete the spending options and run barter-only.

## Routing

- **Email sends on the calendar:** `event-attendee-email-sequences`
- **Social content and platform mix:** `event-social-media`
- **Registration page conversion:** `event-landing-page`
- **Channel roster and voice (feeds the hub):** `event-comms-channels`
- **Swaps and media partners:** `cross-event-promotion`, `event-media-partnerships`
- **Prices and early-bird date:** `event-ticket-pricing`
- **Message and demand read:** `event-positioning`, `event-market-fit`