Sponsor block and bottom are below. Two things changed from the brief.

- **Label stays.** Lumora's item matches our editorial items in font and layout, but it carries a "Sponsor" label. An unlabelled paid item is not allowed in our issues. Only the label differs from an editorial item.
- **Five bottom asks become one ask, one event and one footer line.** The issue carries one ask.

## 1. Sponsor block

Slot: after the lead item (the default, since I have no charter). Same typography as editorial items. Label in words: **Sponsor**. If your house uses "Sponsored" or "Together with", swap it in.

**Version A: edited copy, send to Lumora for approval**

> **Sponsor**
>
> **[Lumora: observability platform](SIGNUP_URL)**
> Lumora is an observability platform. You can start on a free plan.

- I cut "#1 fastest in the world" because we cannot verify a superlative ranking. I cut "don't miss out" as pressure language.
- I kept one link, signup. Docs and pricing are dropped, because a sponsor slot gets one link.
- If Lumora wants a different link, swap it. "Free plan" comes from their "Start free", so Lumora must confirm it is true.

**Version B: fallback if Lumora cannot approve before send**

> **Sponsor**
>
> **[Lumora](SIGNUP_URL)**
> Observability platform.

Tell Lumora what changed. Draft message:

> Hi, we edited your item for this issue. We removed the "#1 fastest in the world" claim, because we run only claims we can attribute, and "don't miss out". We kept one link, to signup. Please confirm by [TIME]. After that we run the shorter label-and-name version. We can discuss superlatives or extra links for a future slot.

## 2. Bottom of the issue

Five asks go to three places.

**Events** (dated items go here):

> **[Webinar: TITLE](WEBINAR_URL)**
> Nov 14, TIME, online. One sentence on what attendees learn.

**Issue-level ask**, once, at the end:

> **[Register for the Nov 14 webinar](WEBINAR_URL)**

**Footer**, one line of standing links:

> [Star us on GitHub](GITHUB_URL) · [Join our Discord](DISCORD_URL) · [Follow us on Bluesky](BLUESKY_URL)

Then the required lines:

> Submit an item: reply to this email. Spotted an error? Reply and we fix the archive. [Archive](ARCHIVE_URL) · [Unsubscribe](UNSUB_URL) · SENDER_ADDRESS

**Driftwood beta sign-up:** it waits for a later issue. If your boss wants it now, there are two options:
- Make it the single ask instead of the webinar. The webinar then stays in Events only.
- Add a "Shipped" item. I need three facts from you: availability (beta, plan, region), the first step a reader takes, and the signup URL. I do not invent any of these.

## 3. Plain-text part (relevant lines)

```
SPONSOR
Lumora: observability platform
https://SIGNUP_URL
Lumora is an observability platform. You can start on a free plan.

EVENTS
Webinar: TITLE
https://WEBINAR_URL
Nov 14, TIME, online.

Register for the Nov 14 webinar:
https://WEBINAR_URL

Star us on GitHub: https://GITHUB_URL
Join our Discord: https://DISCORD_URL
Follow us on Bluesky: https://BLUESKY_URL
```

## 4. Pre-send report

| Check | Status |
|---|---|
| Sponsor in slot with label | pass |
| Tone-pass cut lists clear in sponsor and editor prose | pass |
| One sponsor link | pass |
| One issue-level ask | pass |
| Descriptive link text, plain-text part with full URLs | pass |
| Lumora approves Version A | **blocked**: send them the edit |
| All URLs (signup, webinar, GitHub, Discord, Bluesky, archive, unsubscribe) | **blocked**: I have none, placeholders used |
| Webinar title, time and registration page | **blocked** |
| Test send in Gmail, Apple Mail on a phone and classic Outlook, in light and dark mode | **blocked** |
| Links resolve through the tracking domain | **blocked** |

**Date to check:** Nov 14, 2026 is a **Saturday**. Confirm the date before you send, because readers will act on it.

**Open questions:**
1. Is Version A or B the one that ships if Lumora is silent? Our house label wording?
2. Do you have a charter or previous issue? I used the default order and sponsor-after-lead.
3. Does your sending tool accept raw HTML inside markdown? Does it have a preview-text field? I need this to match Lumora's block to your editorial styling exactly.
4. Driftwood beta: single ask, Shipped item, or later?

Next, in the next 10 minutes: send Lumora the Version A message above. Their reply sets which version ships, and you have 4 hours.