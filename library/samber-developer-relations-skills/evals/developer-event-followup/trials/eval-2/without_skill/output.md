# HackZurich follow-up: plan and outreach

**Next action (10 min):** check what consent and data you actually hold (Gate 0 below). Everything else depends on it.

## Position for the VP Sales

Don't call everyone this week. The 5-minute rule comes from studies of inbound leads: people who filled in a form asking to be contacted. These participants didn't ask for a sales call. Most are students, and some are minors. Calling them has three costs:

- **Legal exposure.** HackZurich is Swiss, with many EU participants. Unsolicited calls to individuals fall under the Swiss UWG (rules on unfair competition and telemarketing) and GDPR/ePrivacy. Phone numbers given to the organizer for hackathon logistics usually don't cover a sponsor sales call. Have legal confirm this.
- **Brand cost.** Cold-calling students at a hackathon is the trade-show behavior that costs a developer-facing brand more than the sponsorship bought.
- **Low yield.** Students rarely hold budget. The buyers are the few with a company, a startup, or a job.

The speed rule still applies to people who raise their hand: reply within one business day. That is the part of the VP's idea worth keeping.

## Gate 0: confirm before sending anything

| # | Question | If the answer is "no" |
|---|---|---|
| 1 | Does the organizer's participant data come with consent for sponsor contact? Check the sponsor agreement and the registration terms. | Do not use it. Contact only through the organizer's channel, or people who engaged with you directly. |
| 2 | Do you know who is under 18? | Exclude anyone not verified as 18 or older. Under-18s get no outreach from sales or recruiting. |
| 3 | Do you have a phone number plus consent for calls? | No calls. Email only. |
| 4 | Are the 23 API teams identifiable from your own API logs (keys, signups)? | Use the logs as your source. Your own users are a different legal basis from the organizer's list. |

## Segments

| Tier | Who | Contact | Owner | Timing |
|---|---|---|---|---|
| **A** | 23 teams that used the payments API. Adults only. | Personal email from DevRel/engineering, offering help and credits | DevRel | Mon-Tue |
| **B** | Remaining 38 teams, only those with consent from Gate 0 | One short thank-you email with resources | DevRel | Wed |
| **C** | Everyone without consent, and all minors | Public thank-you post and a post in the organizer's channel. No direct contact. | Marketing | Mon |
| **Hand-raisers** | Anyone who replies with business intent (a company, a launch plan, a volume question) | Call or email from an SDR | SDR | Within 1 business day |

Keep SDRs out of Tiers A and B until someone replies. Engineer-led emails get replies from developers, and sales calls to them don't. SDRs also avoid wasting a week on students who can't buy.

## Week plan

1. **Mon:** Gate 0 check. Split the list into tiers. Send the Tier C public post. Send Tier A emails after review by legal/privacy.
2. **Tue:** Congratulate the winning teams and the best users of your API personally. Offer them a case study or feature.
3. **Wed:** Send Tier B emails. Send the recruiting opt-in (see below).
4. **Thu-Fri:** Triage replies. Hand-raisers go to SDRs the same day.
5. **Day 30, 60 and 90:** Check how many of the 23 teams are still active on the API.

## Metrics, set before sending

- **Primary:** Tier A teams still calling the API at 30 days.
- **Secondary:** replies, hand-raisers, and qualified conversations. A qualified conversation is someone with a real use case and a named next step.
- **Not metrics:** emails sent or calls made.
- **Decision:** set the target cost per qualified conversation now, using your blended acquisition cost. Compare the result against it at the 2-week review and decide whether to renew the sponsorship.

## Recruiting

Do not hand the participant list to the recruiter. Recruiting is a different purpose from the one participants gave data for, and it needs its own consent. Instead:

- Send the opt-in email below to adult participants (Tiers A and B).
- Hand over only people who reply "yes" (Gate 0 permitting).
- Treat high-schoolers as a future pipeline through programs and scholarships, never through direct contact.

## Drafts

### 1. Tier A: teams that used the payments API (from a DevRel engineer)

> **Subject:** Your HackZurich project on [Company] payments: want help finishing it?
>
> Hi [Team/first name],
>
> I'm [Name], an engineer at [Company]. I saw that [team name] built [project] on our payments API at HackZurich. Congratulations on shipping it in a weekend.
>
> If you want to keep going, I can offer:
> - extended sandbox access and [X] in credits for 90 days,
> - a 20-minute call with me to look at your integration and suggest improvements, only if you want it,
> - a feature on our developer blog or community page, if you'd like to share the project.
>
> You can ignore this email and nothing changes. If you'd prefer not to hear from us, just reply "stop" and I'll delete your details.
>
> [Name], [Company], [link to docs and community]

### 2. Tier B: other teams (consent permitting)

> **Subject:** Thanks for the weekend at HackZurich
>
> Hi [first name],
>
> Thanks for building at HackZurich. If you're still working on your project, here are the resources we mentioned at the event: [docs link], [community link], [sandbox signup].
>
> This is the only email you'll get from us unless you reply. If you'd rather we delete your details, reply "stop".
>
> [Name], [Company]

### 3. Recruiting opt-in (adults only, separate from outreach)

> **Subject:** Would you like to hear about jobs and internships at [Company]?
>
> Hi [first name],
>
> You built something good at HackZurich. Our engineering team sometimes hires interns and graduates, and a recruiter would like to introduce themselves.
>
> Reply "yes" and I'll pass your email to [Recruiter name], who will contact you once. Reply "no", or don't reply, and nothing happens: your details stay with me and won't be shared.
>
> [Name], [Company]

### 4. SDR follow-up to a hand-raiser (reply within 1 business day)

> **Subject:** Re: [their subject]
>
> Hi [first name],
>
> Thanks for the note. You mentioned [their use case, in their words]. A few quick questions so I can point you to the right person: what volume do you expect, and which countries or currencies do you need?
>
> I can set up a 20-minute call with a solutions engineer this week, if useful. Which day works?
>
> [SDR name], [Company]

**Call rules for SDRs:** only call people who have replied and shared a number. Open with "you wrote to us about X", not a pitch. Stop if they say no.

### 5. Tier C: public post (marketing)

> Thank you, HackZurich. 61 teams, 23 of them building on payments, and some great projects. Congratulations to all participants, especially [winning teams]. Our docs and community are open to everyone: [links]. If you want help with your project, our engineers are in [community channel].

### 6. Message to your VP Sales

> Thanks for pushing on speed. Here's my proposal: the 5-minute rule applies to people who asked to be contacted, so SDRs respond within one business day to every hand-raiser. For the participants themselves, we start with personal emails from engineers to the 23 teams that used our API (a lower-risk and higher-conversion group). Phone calls to people who never asked for one risk Swiss and EU rules and our developer brand, and most of these participants are students without budget. I've set a target cost per qualified conversation; we'll review at 2 weeks and 30 days, and if the SDR path underperforms we can widen it. Can we agree on that?

## Open questions

- What does your sponsor agreement with HackZurich say about participant data and consent? This decides Tiers B and C.
- What do you know about participants' ages and employment status?
- Who owns the follow-up after this week? The plan needs a named owner for the 30/60/90 checks.
- What's the target cost per qualified conversation, so we can judge this event against it?