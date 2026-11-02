**Short answer: don't wire the alert on signup. Wire it on a qualification signal, and change what "5-minute email" means before Thursday — otherwise the automation ships and quietly trains your best users to distrust the free tier.**

## Why the 21x stat doesn't transfer here

"Contact within 5 minutes, 21x more likely to qualify" comes from inbound *form-fill* research in sales-led funnels — someone requested contact by submitting a form. A signup on a free CI caching tool is the opposite signal: a developer explicitly chose the path with **no** human involved. Importing the stat here doesn't just fail to help, it actively teaches the one lesson developer audiences punish hardest: *the free tier was bait.* At 2,300 free accounts, a "someone emails you within 60 seconds of signing up" experience reads as being watched, not being helped — expect screenshots on Hacker News, not qualified leads.

## What to alert on instead

Keep the Slack-alert infrastructure — just change the trigger from "signup event" to "qualified account." Roll usage up to an account (workspace/org, API key, or email domain — combine at least two) and fire the alert on whichever of these happens first:

- **Depth** — CI integration live, sustained cache hits across multiple weeks (not a one-day spike)
- **Spread** — a second developer from the same account shows up (invite accepted, second API key, same domain)
- **Boundary contact** (strongest signal, fires alone) — they hit a cache-size/seat limit, opened billing/invoicing pages, or asked about SSO, audit logs, or a security questionnaire

One-sentence rule to hand your head of sales, with the blanks filled from your own conversion data before it ships:

> An account becomes qualified when it has **2+ active developers** and **2+ weeks of production CI usage**, or when **anyone in it hits a limit or opens a billing/security page**. Qualified accounts are contacted by **a technical rep**, within **hours, not minutes**, with **a limits/architecture conversation**. Accounts below the threshold get product and docs only — no human contact.

Response *speed* isn't the problem — instant response to a real signal is fine. The problem is applying it to every signup instead of the ~1-5% that actually show intent.

## The email

One template, used only for qualified accounts, sent by someone who can survive a technical question:

> **Subject: your build cache — quick question**
>
> Hey {first_name},
>
> Noticed {company/team} has a few people running {product} in CI now, with cache hits holding up over the last couple weeks — nice to see it sticking.
>
> A couple of teams at this stage hit the same wall around shared cache limits across parallel jobs. If that's coming up for you, happy to walk through how teams your size usually configure it — 15 minutes, whenever works, no deck.
>
> Also fine if you'd rather just keep going self-serve — our docs cover {relevant limit/config topic} here: {link}.
>
> {sender_name}
> {title, not "Account Executive"}

Notes on why it's built this way:
- Opens with *their own usage*, not a generic value prop — proves you looked, doesn't require a shared workspace object.
- Offers help with what they're already doing (cache limits), never "15 minutes to learn about your needs."
- Explicitly gives them the door back to self-serve — the biggest thing a developer audience needs to hear before a human shows up in their inbox.
- Sender title should read as technical. If a rep in front of engineers can't survive being asked "are you technical or sales," the reply rate craters regardless of copy.

## Call or email?

Email first, for the case above — developers default to async and a cold call this early reads as more pressure, not more help. Reserve calling for when *they* initiated contact (booked a security review, replied asking a question, opened a support ticket about limits) — respond to that fast, same day, because they asked. Never a cold call triggered purely by a product event they didn't ask you to react to.

## The one line to put in front of your head of sales before Thursday

**Do not contact accounts below the threshold — write that down as a rule, not an assumption.** The automation they're building should read "qualified-signal event" off your account-rollup table, not "signup" off your users table. That's a data-model change, not a copy change, so it's worth a five-minute conversation before the Slack integration gets wired to the wrong event.