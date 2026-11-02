# Fixing event lead conversion for a PLG observability platform

## Short answer

Don't send the 5-email blast to everyone. Do respond within 24 hours, but tier the follow-up and make the first touch a product action, not a sequence.

Your CEO has half of it right: speed matters, and the follow-up gap is real. But "80% never followed up" is a claim about leads in general. Don't build the plan on the number, because it doesn't tell you why your nine shows failed. Test the cause before you pick the fix.

## Step 1: Diagnose last year's nine shows (about 2 hours of work)

Pull every lead from the nine shows and answer these four questions. Each points to a different fix.

| Question | If yes, the real problem is |
|---|---|
| Did the leads get any follow-up, and how fast? | Follow-up gap. The CEO is right. |
| Did they follow-up but get a generic sales-style message? | Message and channel, not speed. |
| Were most leads badge scans with no conversation or context? | Qualification. No sequence will fix this. |
| Did you pick the wrong events (wrong audience, wrong seniority)? | Event selection. The follow-up is irrelevant. |

Also check these:
- **Cost per show.** Add fee, travel, swag, and loaded staff time. Staff time is usually the line that doubles the total.
- **Product-side match.** Match event leads to signups by email or domain. Many may have signed up before or after the show without your CRM crediting the event.
- **Per-show results.** Rank the nine by qualified conversations and opportunities. Expect a few shows to account for most of the result, which is normal. The answer may be "cut four shows", not "email harder".

## Step 2: Why the blast backfires with your audience

- **Developers punish pitch sequences.** The people who scanned a badge at a booth are mostly practitioners who half remember you. Five emails in 30 days looks like spam, and it burns your sending domain for the real lead emails too.
- **Consent.** If any scans came from EU attendees, check what the badge scan consented to. Emailing a 30-day marketing sequence to everyone may not be allowed. Have your privacy lead review this before you send anything.
- **PLG changes what a "lead" is.** The best outcome for a developer is a working signup, not a meeting. Your first touch should lead to a product action: a pre-filled sandbox, a signup link with an event code, or a quick-win guide.
- **Enterprise buyers need a person.** For those, a personal note from the person they spoke to beats a sequence.

## Step 3: The system to build

### Before the show
1. **Set one primary goal per show:** product signups, enterprise pipeline, or awareness. Don't set all three.
2. **Set a threshold before you sign.** Define a target cost per qualified conversation and a minimum count that makes the trip worth staffing. If you can't set one, don't sign.
3. **Define "qualified conversation":** the person has the problem, holds or influences the decision, and agrees to a named next step.
4. **Create an event-specific signup URL or code** (for example `/signup?src=kubecon26`), so product signups are attributable.
5. **Pre-book 10 to 20 meetings** with named target accounts via outreach 1 to 3 weeks out.

### At the booth
- Staff with engineers who can debug a stranger's setup.
- Log every real conversation immediately: name, company, problem they mentioned, agreed next step, and a tier tag (A, B or C below). This note is what makes the follow-up good.
- Badge scans without a conversation get tier C and nothing else.

### Within 24 hours: tiered follow-up

| Tier | Who | Action |
|---|---|---|
| **A: Hot** | Real conversation, buyer or champion, stated pain, or enterprise target account | Personal email from the person they met, referencing what they said, with one concrete next step. Route to sales (AE or SDR) in the CRM the same day. |
| **B: Warm** | Real conversation, practitioner, interested but no buying role | One short email with a link to the pre-filled sandbox or a guide for the problem they mentioned, via the event signup URL. Add to the PLG nurture. |
| **C: Scan only** | No conversation | One light touch ("thanks for stopping by, here's the trial link") if consent allows, otherwise nothing. No sequence. |

### Follow-up sequence (tiers A and B only)
Keep it short and trigger it on behavior, not on a calendar.
1. **Day 0 to 1:** the tiered message above.
2. **Day 3 to 5, only if they haven't signed up:** one useful asset tied to their stated problem, such as a short walkthrough or a post on how someone solved it.
3. **Day 10 to 14, only if they signed up but haven't sent data:** a "stuck? here's the fastest path" message, from an engineer if possible.
4. **Day 30:** a final note only if they're in tier A and sales hasn't engaged. After that, drop them into the regular nurture.

If someone replies or books, stop the sequence. That's 3 to 4 touches at most, and fewer for most people.

### Handoff to sales
- Sales-owned follow-up covers tier A plus any signup that crosses your product-qualified-lead (PQL) threshold. Agree on the PQL definition (for example, data ingested plus team invites) with sales and growth. Don't improvise it.
- Set a response-time SLA on tier A (for example, same business day) and track whether it's met.

## Step 4: Measure what decides renewal

| Tier | Metrics |
|---|---|
| Vanity (track, don't report as success) | Badge scans, booth traffic, impressions |
| Real | Qualified conversations, meetings booked, event-code signups, activated accounts at 30/60/90 days |
| Decisive | Cost per qualified conversation, cost per opportunity, influenced pipeline |

- Use self-reported attribution ("heard about us at X") plus event-code tagging. Don't claim last-click credit for deals the event only touched.
- Judge each show against its pre-set threshold, then verdict within two weeks: **renew**, **renegotiate** (right audience, wrong package), or **drop**.
- Judge first-time shows on awareness expectations. But don't renew a show that has missed its threshold twice.

## Step 5: Portfolio changes to consider

- Concentrate. Double down on the two or three shows that perform, with speaking slots, side events, and more staff. Cut the tail.
- Check for niche or regional events (50 to 200 attendees) with SRE and platform engineers. They often beat big conferences on cost per qualified conversation.
- Try a host-your-own dinner of 8 to 14 target accounts near a conference. It often beats a booth on meetings per dollar for enterprise.
- Keep 15 to 25% of the events budget unallocated, because contracts for the good events close about a quarter ahead.

## What to say to your CEO

> "You're right that speed matters, so we'll respond within 24 hours. But a five-email blast to every badge scan is likely to hurt our domain and our developer reputation, and may not be allowed for EU contacts. Instead we'll tier leads: personal follow-up for buyers, a product-first message for practitioners, and nothing for people we never spoke to. Before we spend more, I'm checking our nine shows to see whether the problem is follow-up, lead quality, or show selection. I'll bring the numbers by [date]."

## What I'd need from you to sharpen this

1. Rough numbers: leads per show, how many had a real conversation, how many follow-ups happened and when.
2. Total spend across the nine shows.
3. Your PQL definition today, and whether sales or growth owns event leads.
4. Whether your audience is mostly EU, and what badge scans consented to.
5. Which one or two shows, if any, produced real pipeline.

With those, I can rank the nine shows, set thresholds, and write the actual email templates for tiers A and B.