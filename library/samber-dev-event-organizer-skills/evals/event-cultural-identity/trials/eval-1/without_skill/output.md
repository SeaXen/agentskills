# ForgeConf Vibe Guide

## 1. The core voice (all channels)

The board's brief is: **welcoming but professional, fun but serious.** Read it as one voice with two layers:

- **Serious about:** the attendee's time, money, safety, and the quality of the content.
- **Fun about:** ourselves, the DevOps world's shared pain, and the feeling of being in a room full of people who get it.

**One-line voice:** *A well-run event staffed by friendly people who know their stuff and don't take themselves too seriously.*

Every channel gets the same personality. Channels differ in **how loud the fun is**, not in who we are.

### The dials

Rate each channel on two dials from 1 to 5.

| Channel | Fun (1 = dry, 5 = jokey) | Formality (1 = casual, 5 = formal) | Role |
|---|---|---|---|
| Website | 4 | 2 | The friend who invites you |
| Email | 2 | 3 | The organizer who has your back |
| MC | 3 | 3 | The host who sets the room's mood |
| Signage | 2 | 1 | The helpful local who points the way |

### Rules that apply everywhere

1. **Clarity beats cleverness.** If a joke makes the reader pause on where, when, or how much, cut it.
2. **Jokes target shared pain, never people.** Safe: flaky pipelines, YAML indentation, "it works on my machine," Friday deploys, on-call. Off limits: anyone's identity, a named company's failures, a speaker's mistakes, an attendee's skill level.
3. **One joke per unit.** That means one per paragraph, email, announcement, or sign. The joke goes after the useful information, never before it.
4. **Plain language.** Short sentences, active voice, no corporate filler ("we are delighted to announce"), no jargon beyond what a mixed junior and senior audience knows.
5. **Run by volunteers, and it shows in a good way.** Warm and honest, never sloppy. We can say "we're volunteers, so please be kind to the registration queue." We never use it as an excuse for errors.
6. **Dutch directness is welcome.** Say what's happening and what we need from the reader. Don't pad.
7. **Inclusive by default.** Use "you all" and "everyone." Avoid insider references that make newcomers feel they're outside the club. If a meme needs 10 years of context, skip it.
8. **Safety and logistics are never jokes.** This covers the code of conduct, accessibility, emergencies, cancellations, payments, and refunds.

---

## 2. Website: *"The friend who invites you"*

**Personality:** Playful, confident, inviting. This is where the fun is loudest, and where a first-time visitor decides whether we're their kind of people.

**Fun 4 / Formality 2**

### Do
- Use memes and humor in headlines, section intros, the FAQ, and 404 and empty states.
- Lead with what the visitor gets (talks, workshops, hallway conversations), then add the wink.
- Keep a clear, boring, joke-free zone for **dates, venue, ticket prices, schedule, accessibility, and code of conduct.**
- Write the FAQ as if answering a nervous first-timer: "Will I be the only one who doesn't know Kubernetes? No. Several hundred of us are still figuring it out."
- Use meme formats sparingly and keep them self-explanatory. The text must stand on its own for someone who doesn't know the template.

### Don't
- Don't put a meme in the checkout, refund policy, or CoC pages.
- Don't use more than one meme or joke per screen.
- Don't use memes that depend on a specific tool war or a named vendor.
- Don't let humor replace information. If the joke is removed, the sentence still has to be complete.
- Don't use stale meme formats. If it's been on the front page of a meme site for years, retire it.

### Examples

| Instead of | Write |
|---|---|
| "ForgeConf 2026: The premier DevOps event in the Netherlands." | "400 DevOps people, one city, zero production incidents. (We make no promises about the Wi-Fi.)" |
| "Registration is now open." | "Tickets are live. Please register before the deploy freeze on your good intentions." |
| "Ask us anything." | "Questions? Ask us. We've heard weirder ones than yours." |

*Check: the Wi-Fi line is a joke about shared pain. If our Wi-Fi really is a risk, don't joke. Fix it or say nothing.*

**Test before publishing:** Could a sponsor's CTO and a first-year junior both read this and smile, without either feeling talked down to?

---

## 3. Email: *"The organizer who has your back"*

**Personality:** Warm, clear, reliable, lightly dry. Email carries real obligations: tickets, schedules, invoices, sponsor deliverables. People forward it and file it, so it must be unambiguous.

**Fun 2 / Formality 3**

### Fix the "sponsors are cc'd" problem

Don't write every email for the most formal reader in the cc line. Split by audience:

| Email type | Audience | Tone |
|---|---|---|
| **Attendee emails** (confirmations, schedule, travel, reminders, post-event thanks) | Attendees only. No sponsors cc'd. | Warm and clear, with one light touch. |
| **Sponsor emails** (contracts, deliverables, logistics) | Sponsor contacts, organizers | Professional and precise, friendly in the opening and closing. |
| **Mixed-thread emails** (sponsor cc'd on attendee-facing issues) | Mixed | Same as sponsor emails. Keep jokes out of the body. A friendly sign-off is enough. |

**Rule:** Move sponsors to bcc or a separate thread when they don't need to be in the conversation. A formal tone should be a choice for the content, not a side effect of cc lists.

### Do
- Put the **action and the deadline** in the first two lines.
- Use short paragraphs, clear subject lines, and bullets for logistics.
- Open with a human greeting and sign with a real name.
- Allow one dry line in attendee emails, usually near the end.
- Spell out dates with the weekday and time zone (e.g., "Thursday 12 March, 09:00 CET").

### Don't
- Don't use "Dear Sir/Madam," "please be informed that," or "kindly revert."
- Don't use memes, GIFs, or emoji-heavy subject lines.
- Don't joke in emails about money, delays, cancellations, or complaints.
- Don't write a wall of text. If it exceeds a short screen, restructure it.

### Examples

**Attendee reminder**
> **Subject:** Your ForgeConf ticket and what to bring
>
> Hi Sam,
>
> You're all set for ForgeConf. Here's what you need:
>
> - **Your ticket:** attached, scan it at the entrance
> - **Doors open:** 08:30 on the first day
> - **Where:** [venue and address]
>
> Bring a charger and a sense of adventure. We'll supply coffee, which is arguably the real infrastructure.
>
> See you in Rotterdam,
> Anna, on behalf of the ForgeConf team

**Sponsor email**
> **Subject:** ForgeConf booth logistics: action needed by 20 Feb
>
> Hello Jan,
>
> To keep your booth setup smooth, we need three things from you by 20 February:
>
> 1. Names of the staff attending
> 2. Delivery details for shipped materials
> 3. Power and network requirements
>
> Thank you for supporting a volunteer-run event. We'll confirm everything in writing once we have your details.
>
> Warm regards,
> Anna, ForgeConf Sponsor Team

---

## 4. MC: *"The host who sets the room's mood"*

**Personality:** Confident, warm, well-prepared, lightly funny. The MC is the human face of the voice, and the tone has to work live, out loud, in front of 400 people.

**Fun 3 / Formality 3**

### Fix the brief

"Keep it serious and professional" contradicts the board's "fun but serious" and will produce a stiff host. The corrected brief for the MC:

> **Be serious about the content and the people. Be relaxed about yourself.**
> You protect the speakers' time and the audience's attention, and you set a tone where it's comfortable to be curious.

### Do
- Greet the room warmly and open each day with energy. A relaxed first minute sets the tone for everyone.
- Introduce speakers with respect: name, role, and one sentence on why the talk matters. The humor never targets the speaker.
- Keep transitions short and stay on schedule.
- Use self-deprecating or situational humor ("we've survived another coffee shortage") rather than anything about individuals.
- Read housekeeping clearly, in plain language: exits, breaks, Wi-Fi, the CoC contact, and where to ask for help.
- Stay calm and direct when something goes wrong: "We're fixing the projector, so take two minutes. Coffee's that way."

### Don't
- Don't improvise jokes about speakers, sponsors, or attendees.
- Don't read the sponsor message in a comic voice. It should be friendly and clear.
- Don't joke during incidents, safety announcements, or anything involving the CoC.
- Don't use inside jokes that exclude newcomers.
- Don't go over the one-joke-per-announcement rule.

### Cue card (give this to the MC)

| Moment | Mood | Example line |
|---|---|---|
| Opening | Warm, energetic | "Welcome to ForgeConf. If you're here for the first time: hello. If you've been before: you know where the coffee is." |
| Speaker intro | Respectful, curious | "Our next speaker has run production systems at scale. Please welcome Maria Jansen, who will show us how to make deploys boring." |
| Housekeeping | Plain, clear | "Exits are at the back and on both sides. If anything feels off, find someone in a green volunteer shirt." |
| Delay or technical issue | Calm, honest | "We have a short technical pause. We'll resume at 10:45." |
| Sponsor thanks | Sincere | "None of this happens without our sponsors. Please stop by their booths and say thanks." |
| Close | Grateful, upbeat | "Thank you for making this room what it is. Go talk to someone you haven't met yet." |

---

## 5. Signage: *"The helpful local who points the way"*

**Personality:** Clear, friendly, minimal. Signs are read in passing, from a distance, often by someone who is slightly lost, tired, or in a hurry. Fun here is a quiet smile, never a pause.

**Fun 2 / Formality 1**

### Do
- Put the **function first**: where, what, and which direction. Use large, high-contrast type and arrows.
- Use short phrases of 2–6 words.
- Add a small wink only on non-critical signs (coffee, lounge areas, social spaces, the quiet room).
- Use consistent terms for each place and keep them identical across signs, website, and the program. Pick one name per room and use it everywhere.
- Include icons and symbols alongside the text.
- Make sure the signage meets accessibility requirements: step-free routes, contrast, large type, and clear marking of accessible toilets and quiet spaces.

### Don't
- Don't make wayfinding signs funny at the cost of clarity. Registration, exits, toilets, first aid, and the CoC contact use plain language only.
- Don't use memes on signs. They need context and time to read.
- Don't use small print, long sentences, or more than one message per sign.
- Don't mix languages on one sign without a clear layout. If using English and Dutch, keep the layout consistent.

### Examples

| Sign type | Text | Humor level |
|---|---|---|
| Registration | **Registration →** | None |
| Exits / first aid | **Exit** / **First aid** | None |
| Main stage | **Main Stage, Hall A** | None |
| Coffee | **Coffee. Yes, here.** | Light |
| Lounge | **Quiet corner. Be nice to your brain.** | Light |
| Wi-Fi | **Wi-Fi: [network] / [password]** | None |
| Feedback wall | **What worked? What broke? Tell us.** | Light |

---

## 6. Consistency checklist

Before anything goes out, check:

1. **Is the information complete without the joke?**
2. **Is the joke about a shared experience, not a person or company?**
3. **Would a newcomer understand it?**
4. **Does it match the channel's dial?** Website can be loud, signage can't.
5. **Is it safe to forward?** Assume a sponsor, a speaker, and an attendee's manager will all read it.
6. **Is it a logistics, money, safety, or CoC message?** If yes, remove the humor.

## 7. Quick reference

| | Website | Email | MC | Signage |
|---|---|---|---|---|
| **Role** | Friend who invites | Organizer with your back | Host who sets the mood | Helpful local |
| **Fun** | 4 | 2 | 3 | 2 |
| **Formality** | 2 | 3 | 3 | 1 |
| **Memes** | Yes, sparingly | No | No | No |
| **Humor target** | Shared pain | Light, dry | Ourselves | Quiet wink |
| **Always joke-free** | Checkout, CoC, refunds | Money, delays, complaints | Safety, CoC, incidents | Exits, first aid, registration |

## 8. Rollout (suggested)

1. **Board** approves the core voice and the dials (section 1).
2. **Audit** the existing website copy: keep the playful headlines and strip memes from logistics pages.
3. **Split** email lists and cc habits so attendee emails stop inheriting sponsor formality.
4. **Brief the MC** with the corrected brief and the cue card, and let them rehearse.
5. **Review signage** for clarity first, humor second, before printing.
6. **Review after the event.** Collect feedback from attendees, sponsors, and the MC. Adjust the dials for next year.

## Open questions for the board

- Which language(s) do signs and the MC use: English only, or Dutch too?
- Are there sponsor-contract constraints on how sponsors are mentioned on stage or on the site?
- Who owns final sign-off on tone, so nobody re-litigates it per channel?

Note: I couldn't load the tone-of-voice skill, so I wrote this guide from scratch using your brief. The example copy uses placeholder names and details (Sam, Anna, Maria Jansen, venue, dates). Swap in real ones before circulating.