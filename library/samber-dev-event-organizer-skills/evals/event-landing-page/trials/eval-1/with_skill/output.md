# Rivetfest homepage: top to bottom

**Verdict:** the page has no call-to-action button and no email box. Your friend's rule comes from ticketed events and SaaS pages. Rivetfest has no tickets, no registration and no open call, so a button would have nothing behind it. FOSDEM, the free no-registration conference the skill uses as its model, has no CTA for the same reason.

This is built from the event-landing-page skill and its three references. I used the facts you gave me and did not run the full interview. The list at the end shows what I still need from you.

## Why not the email box

- **No action to attach it to.** With no tickets, registration or call for proposals, a capture box has no gated step to feed. A notify-me capture exists to catch interest before something goes on sale, and nothing here goes on sale.
- **It costs more than it looks.** It is the only element on the page that collects personal data. It needs a consent basis, a privacy notice and a deletion path before it ships.
- **A free event with a 3,000-person track record doesn't need one.** The traffic is not wasted if the hero answers what, when, where and cost in five seconds, then leads to the talk archive. That archive is your strongest reason to attend.
- **A mailing list is a separate decision.** If you want one for next year, decide it on its own terms, not as a homepage fix.

## Page shape

**Front door plus practical annexes.** That means a homepage, plus Location, Code of Conduct and Accessibility as their own addressable pages.

- Third parties link to the Code of Conduct and Accessibility pages, and attendees forward them to employers. That needs real addresses, not anchors.
- Move up to the program set (Program and Speakers pages) only once talks and speakers are confirmed.
- This is a sixth edition with an archive, so the structure is worth keeping and rebuilding each year.

## Sections, top to bottom

| # | Section | Content | Posture |
|---|---|---|---|
| 1 | **Hero** | Rivetfest, April 18-19, the Maritime Academy in Tallinn with a map-linked address, and your positioning sentence. The scale signals sit directly under the name: **3,000 attendees · 14 tracks · 120 talks** (label them "last edition"), plus a "Sixth edition" tag, **Free. No registration, just show up.** | Live |
| 2 | **Contrast sentence** | Your anti-positioning line, verbatim: "There are many [archetype] events. This is not one of them." | Live |
| 3 | **Past editions** | Links to editions 1-5, as the DevOpsDays template does | Live |
| 4 | **Video archive** | Last year's recordings, with the channel link | Live, if the speaker agreements allow republishing |
| 5 | **How talks are chosen** | One or two lines: talks are invited by track organizers and there is no open call. Add the organizer contact for anyone who wants to be considered. | Live |
| 6 | **Program and tracks** | None until the program is real. If travel or budget decisions are blocked on it, show a heading plus a real reveal date. | Omit, or "named with a date" |
| 7 | **News** | Dated items, FOSDEM-style | Live |
| 8 | **Sponsors** | Real logos only | Omit until signed |
| 9 | **Venue and getting there** | Address, map, how to reach the Maritime Academy | Live |
| 10 | **Footer cluster** | Accessibility, Code of Conduct, on-the-day info and health policy as one block, plus the organizer contact | Live |

- **No "Register," "Subscribe" or "Propose" button.** The only link-style action is Contact.
- **No manager-forward block.** The cost is "free," and the hero already says so.
- **No "coming soon" placeholders and no fake testimonials.** The archive is your social proof.

## CTA state machine

Because no action is gated, the "CTA" is always Contact. Only the sections change by date. A named person must own each transition.

| From | Phase | Primary | Sections added or removed |
|---|---|---|---|
| now | Announced | Contact | Hero, dates, venue, archive, Code of Conduct |
| program reveal (date TBD) | Program live | Contact | + Program and tracks |
| sponsor signing (dates TBD) | Sponsors confirmed | Contact | + Sponsors |
| April 18 | Live | Practical info | + on-the-day details, health policy |
| after April 19 | Archived | Contact | + new recordings and photos, status line on the hero ("Edition six took place April 18-19") |

If nobody can edit the page by date without a developer, use the manual fallback. Copy each row into your campaign calendar as a dated task with one owner, and set the reminder one day before.

## Structured data

Emit a machine-readable copy of the hero facts and keep it in sync with the visible page.

```json
{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "Rivetfest",
  "description": "<your positioning sentence>",
  "startDate": "<YYY>-04-18",
  "endDate": "<YYYY>-04-19",
  "isAccessibleForFree": true,
  "url": "<canonical URL>",
  "image": "<hero image URL>",
  "location": {
    "@type": "Place",
    "name": "Maritime Academy",
    "address": "<street address, Tallinn>"
  }
}
```

The skill's reference uses `ExhibitionEvent`. It says any matching subtype is acceptable, so I chose plain `Event` with `isAccessibleForFree`.

## Accessibility

The target comes from the accessibility-inclusion sibling, normally WCAG 2.2 AA. Build it in, not on top:

1. **Structure first.** One `h1`, real headings and landmark regions.
2. **Contrast at palette time.** 4.5:1 for normal text, 3:1 for large text and interface components. Check text over the hero photo against its busiest area.
3. **Real links with descriptive text.** Use "Watch last year's talks," never "click here."
4. **Usable at 200% zoom and on narrow screens.** The long date and address strings are what usually break.

A passing page audit is not event accessibility coverage. Physical, sensory and dietary provision belongs to the accessibility-inclusion sibling.

## Pre-launch gate (all four must pass)

1. **Every transition has a date, an owner and a reminder.** Not yet. The dates are TBD, so this fails until you supply them.
2. **What, who, when, where and what it costs are readable in one phone screen.** Hand it to someone who has never seen Rivetfest. Do not judge it yourself.
3. **The structured data validates** and carries the real dates, address and URL.
4. **Keyboard-only pass.** Registration doesn't exist here, so I replaced the skill's registration-flow check with a keyboard-only walk through the nav, the archive and video links, and the map and contact links. This substitution is mine, not the skill's.

All four are the skill's own pre-launch checks, not a published standard. The skill quotes no conversion rate for event pages and I won't invent one. Published rates describe SaaS and paid-traffic funnels, so don't use one to defend the page to your friend.

## What I need from you

- **Positioning sentence and contrast sentence, word for word.** I can't write them.
- **Year, street address and canonical URL** for the structured data and the hero. I assumed this is April 2027 but didn't state a year.
- **Archive rights:**
  - Do the speaker agreements permit republishing recordings?
  - What photo opt-out did last year's attendees have? Free-entry events often have no badges.
  - Without both answers, show only the recordings you are cleared to publish.
- **Real reveal dates** for the program and sponsors, and a named owner per transition.
- **Maintenance:** who edits the page, for how many hours, and can they do it without a developer? If it's one volunteer with a few hours, keep the one-page-plus-three-annexes shape and skip the program pages entirely.