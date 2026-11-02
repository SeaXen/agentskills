# ConduitConf edition 2: marketing plan and how to read the first weeks

I read `event-marketing-plan/SKILL.md` and both reference files. The skill's interview asks one question at a time. You wanted a single answer, so I made explicit assumptions (section 1) and listed what to confirm (last section).

⚠️ **Two parts of the plan as stated need changing.** Emailing all 3,800 addresses on day one is a consent risk. Counting the sponsor's 60 tickets as sales would give you a false read of demand. Both are fixed below.

## 1. Assumptions (change any of these and the plan shifts)

| Assumption | Why it matters |
|---|---|
| Ticketed event, so **Spine A** (percent of expected sales, anchored on marketing moments). | Never blend it with the free-event spine, which targets 200% and manages no-shows. |
| Community-run, with a partner meetup and a booth. | Posture becomes barter-only plus a small test budget. A company-run event with a budget line would change that. |
| Announcement is **2026-11-04**. Doors date unknown. | I can only give T-offsets. The skill's earliest anchor is T-7 months for "marketing off and running". If doors are under about 7 months after 11-04, you start behind, so lean on fast channels (list, partner sends) over slow ones (local relationship-building). |
| Positioning and the demand read are not supplied. | The skill says to route to `event-positioning` and `event-market-fit` first. Last year's 210 sales and the 143 "can't make it" ticks are real demand evidence. A message and audience definition still have to exist before any copy goes out. |

## 2. Target, net of comps

The target is **tickets that must be sold**, not seats filled.

`expected sales = target attendance − sponsor 60 − speakers − organizers − volunteers − scholarship/press/partner passes`

- **Illustration only, not your number:** 300 seats, minus 60 sponsor, minus an assumed 25 other comps, gives **N = 215 to sell**. Replace N with your own figure.
- ⚠️ **Check whether last year's 210 included comps.** If it did, net them out before you use the curve. Otherwise this year's pace index compares sold tickets against given-away ones.
- Last year was a first edition, so don't assume a flat 210. Growth is a judgement call. Write down the number you pick and why.

**Checkpoints on N (the DevOpsDays ladder, whole-funnel and published):**

| Checkpoint | Target | Example at N=215 |
|---|---|---|
| First sales week | Any real spike | n/a |
| Early-bird close (date fixed by `event-ticket-pricing`) | ~15% | ~32 |
| Speaker/agenda announcement | ~+10% | ~54 cumulative |
| One month out | 40-50% | 86-108 |
| Final two weeks | A surge | n/a |

Last year's own weekly curve, netted of comps, **beats this ladder**. Use the ladder only as the fallback and for the one-month discriminator.

## 3. The 3,800-address list: do not blast it on day one

The skill flags the owned mailing list as carrying consent exposure. A list collected for one edition and mailed for the next, without documented opt-in, is the one acquisition asset that can force a deletion you can't undo. Your 3,800 is three lists with three different consent positions.

| Source | Day-one email? | Why |
|---|---|---|
| **143 "interested but can't make it this year"** | ✅ Yes, first priority | They told you they wanted this edition. The skill singles this segment out: "not available last time, are you free now" converts people other channels never reach. Check the checkbox wording covers being contacted. |
| **Last year's attendees** | ✅ Yes, if the registration form recorded opt-in to future-edition updates | If it didn't, send one transactional-style "edition 2 is announced" note only if your lawyer or DPO agrees. Otherwise treat them like the segments below. |
| **Partner meetup's export** | ❌ Don't mail it | Those people opted in to the partner, not to you. Instead ask the partner to send the announcement to their own list with a unique tracking code. This is a partner channel, so it routes to `cross-event-promotion`. |
| **Business cards from the booth** | ❌ Not in the bulk send | A card handed over is not marketing consent. Options are a personal one-to-one note from whoever collected it, or a single opt-in invitation, if local law allows. |

- 🟠 I don't know your jurisdiction, and this is not legal advice. If you operate in the EU or UK, GDPR and ePrivacy rules apply. Get a quick DPO or lawyer check before the send. The guardrails above hold either way.
- **Deduplicate** the 143 against the 3,800 before sending, so nobody gets two emails.
- **Send in segments with a tracked link or code per segment.** One blast makes it impossible to tell which segment converted, and the skill says tracking can't be added retroactively.
- Judgement, not a published rule: mailing a cold third-party list can also hurt your sender reputation (bounces, spam complaints) before the real announcement lands.

## 4. Audience-to-channel map

Channel value ranking is judgement. Per-channel targets are yours to set, because no published benchmark exists for them.

| Channel | Segment it's bought for | Weight | Executor |
|---|---|---|---|
| Own mailing list | The 143, opted-in attendees, later opted-in cards | High (default top rung) | `event-attendee-email-sequences` |
| Comms hub (one page plus QR code) | Converts reach from every other channel | One-time build | `event-comms-channels` |
| Partner channels | Partner meetup's audience, plus other aligned meetups | Medium-high | `cross-event-promotion`, `event-media-partnerships` |
| Own social presence | Baseline, running underneath | Low-medium | `event-social-media` |
| Local engagement (meetups, employers) | Regional audience | Medium, in person | Organizers |
| Paid ads | One named segment, test only | Small, conditional | n/a |
| Pre-event press | Skip for now | Low | `event-press-relations` if wanted |

- **Paid ads** wait until one owned channel shows a tracked referral signal. A soft checkpoint alone is not a reason to spend.
- **Page conversion** is owned by `event-landing-page`.

**Budget posture:** barter-only plus a fixed test budget, with the cash held behind a checkpoint. The skill's worked example for a €2,000 community event keeps about 30% as a capped paid test in the two weeks after the announcement and about 70% in reserve. The reserve is released only if the one-month-out checkpoint lands below 40%. Your budget is unknown, so scale that split. If you show a percentage allocation table to anyone, label it: those shares come from B2B/B2C SaaS conventions, not event-industry benchmarks.

## 5. Calendar (relative to doors, pinned to what is fixed)

| When | Moment |
|---|---|
| Now to 11-03 (3 weeks) | Do the consent audit and dedupe. Build the comms hub. Create one tracked code per segment and per partner community. Create a **separate sponsor code**. Get the early-bird date from `event-ticket-pricing`. Brief the partner meetup. |
| **11-04, announcement** | Send to the 143 and the opted-in attendees. The partner sends to its own list. Social and the comms hub go live. |
| Announcement + 1 week | Read the first-week spike (section 6). |
| Announcement + 2 weeks | First readable week. Compute the pace index. Decide whether to release the paid test. |
| Early-bird close | Fixed by pricing; do not move it to make the campaign easier. Checkpoint is ~15% of N. |
| CFP close / speaker announcement | ~+10%. If sales didn't move, check that the announcement actually reached the list. |
| Full agenda | Second program-driven spike. |
| T-1 month | Reminder send. Checkpoint is 40-50% of N. |
| T-2 weeks | Final surge campaign. |

## 6. How to read the first weeks, with the sponsor's 60 tickets

**Rules**

1. **Week one measures reach, not demand.** Announcements spike. The only week-one signal that carries information is no spike at all. That is the earliest warning that no audience exists. First, check the email actually delivered.
2. **Week two is the first readable week.** A quiet middle after the spike is the normal shape, not a failure.
3. **Keep the sponsor's 60 out of the sales line.** They never had to be sold, and they are already subtracted from N.
   - Issue them under the dedicated sponsor code and report them separately.
   - Releasing ticket codes to sponsors is one of the published sales-spike moments. If sponsor staff or guests register in week one, the curve looks hot for a reason that has nothing to do with demand.
   - The skill's rule for early overperformance is: confirm it isn't a comp-inflated or batch-release artifact before you move budget away from anything.
4. **Don't read last year's curve at face value early on.**
   - Last year had no prior-edition list. This year you email people who already said yes, so the first weeks are likely **front-loaded**. A pace index above 100 in weeks 1-2 is expected and proves little.
   - Compare shape from week two, and at early-bird close, not week-one totals.
5. **Net the comps out of both curves** before computing: pace index = tickets sold to date ÷ curve-expected × 100. Above 100 is running hot. Below 100 is a gap with a size and a deadline.

**Diagnosis when you're below the line** (decide these actions now, before launch):

| What you see | Reading | Action |
|---|---|---|
| Low page traffic, low opens, no partner referrals | Execution shortfall. The 25-30% at one month out is where teams that delayed their push land. | Add or re-weight channels. Check whether announcements ran late, the theme is too narrow, or messaging never said who is welcome. |
| Healthy traffic, low conversion | Price or page problem, not channel mix | Route to `event-ticket-pricing` or `event-landing-page`. Don't buy reach. |
| Healthy traffic and conversion, still short | Genuine demand shortfall | Route to `event-market-fit` and your own downgrade decision. A bigger campaign won't fix it. |
| Above the line early | Possibly a comp or batch artifact | Check the sponsor code and the segments before reallocating anything. |

**Per-channel signal:** a channel at zero across two editions loses its weight next edition. If the 143 convert at zero by early-bird close, drop their weight.

## 7. What I need to tighten this

1. **Doors date.** It sets the real T-offsets and whether you are inside the 7-month runway.
2. **Your edition-2 target.** Seats or paid sales, plus the full comp list besides the sponsor's 60.
3. **Did last year's 210 include comps?**
4. **Exact wording of the form's opt-in and the "can't make it" checkbox.** This decides who gets the day-one email.
5. **Cash acquisition budget and who approves it.** I assumed community-run and barter-first.
6. **Is the sponsor's allocation a paid block or a pure comp?** Either way it stays out of the sales line, but it changes the revenue picture.

The skill's persistent-memory step applies if you use memory. Record this edition's spine, net target, channel weights with the segment each serves, fixed dates, budget posture, and planned-versus-actual at each checkpoint. Edition 3 then starts from a real curve.