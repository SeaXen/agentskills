# Brinefield Summit board prep: conversion target and A/B test

## Short answers

1. **I can't give you a defensible "good" conversion rate for an event page.** The published figures, including 2.35%, describe SaaS and paid-traffic funnels, not event pages. Don't put a rate on a board slide as a target.
2. **Don't run an A/B test first, or at all.** Your traffic is too small for a test to read. Fix the page against a pre-launch checklist instead, and spend the effort on traffic, which is where the 600 gap sits.

## Your slide's numbers don't reconcile

- **Your conversion rate is 2.18%, not 1.6%.** 61 ÷ 2,800 = 2.18%. A 1.6% rate would mean about 45 registrations from 2,800 visits, or about 3,800 visits for 61 registrations. Find which figure is wrong before the board sees it. Likely causes are a different visit definition (sessions vs. unique visitors) or a different date window.
- **At 2.18% you're already within 0.17 points of the 2.35% benchmark.** The gap the slide proposes to close is much smaller than it looks.
- **The 2.35% benchmark isn't event evidence.** It's a generic landing-page average. Using it makes the page look like it's underperforming against a number that doesn't apply.

## 1. Setting the target

- **No numeric conversion threshold.** Any imported rate would be false precision. The team would optimise against a number that means nothing for an event page.
- **Use your own baseline.** Record 2.18% (once the 1.6% discrepancy is resolved) as the starting point, split by traffic channel. Mixed channels hide the real picture. A newsletter list and cold social traffic convert very differently.
- **Registrations and traffic matter more than the rate.** Here is the arithmetic from your own numbers:
  - Pace so far: about 320 visits a week, so about 1,930 visits over six weeks.
  - At 2.18% that gives about 42 more registrations, roughly 103 in total against a 600 target.
  - Lifting conversion from 2.18% to 2.35% adds about 3 registrations.
  - Closing the 539-registration gap at today's rate needs about 24,700 visits, roughly 13 times your current pace. At today's traffic it would need about 28% conversion, which nothing credible supports.
- **The 600 gap is a traffic and channel problem, not a hero-copy problem.** This assumes the target means registrations. If it means people who show up, the gap is larger still, because not everyone who registers attends.
- **Interim targets come from the campaign calendar.** The marketing plan owns the per-phase targets and dates. I don't have them, so I can't set the numbers here.

## 2. Which test first

The answer is none. Your own numbers show why.

- **Visits per arm.** Six weeks leaves about 1,930 visits. Split two ways, that's about 965 visits and about 21 registrations per arm.
- **Below the usual floor.** The common rule of thumb is roughly 1,000 sessions or 30 conversions in the window. You'd have about 965 visits and about 21 conversions per arm, both under it.
- **Detectable lift.** At 965 visits per arm, only a jump from about 2.2% to about 4% (nearly double) would show up above noise (80% power, 5% significance). Hero-copy variants rarely do that.
- **Detecting a more realistic 25% lift** (2.18% to about 2.7%) needs about 11,500 visits per arm, about 12 times what you'll have.
- **One edition, no iteration.** There's no second run to apply what you learn. A test that ends in the final weeks pays off only if the winner then runs long enough to matter.
- **Wrong place for the effort.** Even a real win in the hero moves a few registrations, while the 600 gap needs thousands more qualified visitors.

## What to do instead

Rank the page by first-principles friction. Then pass the four-check pre-launch gate, all four or the page isn't live. These checks are one person's afternoon each.

1. **CTA transitions.** Every CTA change has a date, a named owner, and was actually made on that date. Walk the transition table against the campaign calendar. A stale Propose or "Register" button pointing at a closed or unopened door is the most common failure.
2. **Five-second phone test.** Hand the page to someone who has never seen the event, ideally a marine robotics developer. They should answer what, who, when, where and what it costs in one screen, without scrolling. If they can't, that is the first thing to change, and it addresses the hero concern without needing a test.
3. **Structured data.** An event JSON-LD block validates and carries the real dates, location and URL. A script can check this.
4. **Keyboard-only registration.** The whole flow completes by keyboard, including any date picker and the payment step.

Then run these, in order:

1. **Fix the 1.6% vs 2.18% discrepancy** and split conversion by channel. If one channel converts far below the others, that's the most informative finding you can get from existing data.
2. **Add a manager-forward block**, if tickets are priced. It's a short, linkable section an attendee forwards to whoever approves their travel budget: what the event is, dates, location, cost, and two or three lines on why it's worth the time away. This is likely relevant, since developers often get reimbursed by employers. I haven't seen your page or ladder, so treat it as a hypothesis, not a finding.
3. **Remove dead or competing CTAs.** Only one primary button should show at a time, and it should match what's actually open today.
4. **Put per-channel tracked links on every promotion.** From now on you can see which channels bring registrations. The marketing plan reads them.
5. **Spend the remaining weeks on traffic**: the mailing list, partner and community channels, and speaker and sponsor audiences. This is where the 539-registration gap lives.

## What I assumed

I didn't run the full interview, so these are open and would change the details but not the verdict:

- The event is priced, with a ticket ladder set elsewhere, not a free event.
- Registration is open now and a CFP isn't the active CTA.
- I haven't seen the page, the dates, the positioning statement or the ladder.
- Everything labelled as a checklist item above is a construction of the event-landing-page skill, not a published standard.