## Booth demo plan: 3×3, two days, rolling traffic

Your instinct to reuse the webinar walkthrough is the actual problem, not the booth itself. A webinar audience already chose to be there, already sat down, and can hear you. Booth traffic didn't choose anything — they're walking to lunch and you have about three seconds to give them a reason to stop. A 15-minute script that opens with "first, install the agent, then configure the collector" fails on every axis: the payoff is 10 minutes away, most people won't be there when it arrives, and "installation steps" isn't something a glazed-over brain processes at 4pm on a loud show floor.

Fix: stop thinking of this as one demo. Build **three demos of different length that share one story**, and pick which one to run based on how long the person is willing to stand still. Below is the full system — physical setup, the three scripts, how to triage in the first ten seconds, lead capture, and staffing for two days.

---

## 1. Fix the environment first — the script doesn't matter if no one can see or hear it

**The window behind you is your biggest liability, not a backdrop.**
- Never mount the demo screen against the back wall/window. That puts a bright light source directly behind the screen from the viewer's angle — their eyes adapt to the window's brightness and your monitor reads as a dim gray rectangle, exactly like trying to read a phone with the sun behind it.
- Pull the monitor(s) forward, onto the front counter or a stand closer to the aisle, so the window is behind the *booth staff*, not behind the *screen*. Attendees then face away from the window when looking at the demo.
- Use the highest-brightness display you have access to (borrow one if needed — a 250-nit consumer monitor will lose the fight with daylight; look for 400+ nits or a matte anti-glare finish).
- Angle screens slightly downward and away from the window's direct reflection line, not flat vertical.
- If the venue allows it, a cheap roll of blackout/frosted static film on the window panel directly behind your booth solves this outright — check with the show's operations desk, it's a common ask.
- Keep one laptop as backup for 1:1 deep dives — you can physically turn it to kill glare for a single visitor in a way you can't with a mounted monitor.

**The loud floor means your hook can't depend on sound.**
- Nobody will hear a spoken pitch from more than arm's reach. Design the passive, no-one's-stopped-yet state of your screen to sell itself with zero audio: big bold visuals, high contrast, large text, motion. Think "billboard," not "slide."
- Once someone stops and you're talking 1:1, normal conversational volume at close range works fine — the noise problem is only about *before* they've committed to stopping.
- Don't caption-dependent your loop either; assume total silence and design for it.

**What runs on the screen when nobody's standing there (the "attract loop"):**
- A single before/after visual on a 15–20 second loop: left side, a tangled service map with a red failing span buried in it; right side, the same failure pinpointed and root-caused in one click, with a big on-screen timer showing something like "12 seconds." No narration needed — the image alone should make an engineer's eyes catch.
- Avoid a logo slide, a bullet list, or anything that requires reading more than 3 seconds to parse. If it needs a sentence to explain, it won't work as a loop.

---

## 2. Triage in the first 10 seconds — this is the actual skill to train your booth staff on

Don't ask "can I tell you about our product?" — it's a wall people walk past on reflex. Open with a **question tied to the pain**, and let their answer and body language tell you which of the three scripts to run.

Opener (works whether they slow down or stop dead):
> "Ever spent an hour trying to figure out which service actually broke a request?"

- **Kept walking, just nodded or half-smiled** → you get the 30-second hook, delivered as they pass. That's it. Don't chase them.
- **Slowed down, made eye contact, maybe a "yeah, constantly"** → 3–5 minute core demo. Most of your traffic lands here.
- **Stopped, put their bag down, asked a follow-up question unprompted** → this is your 15–20 minute person. Move them to the side/stool if you have one, get a business-feeling conversation going, this is your actual pipeline for the show.

Don't run the long script on someone who gave you a polite nod. Don't rush someone who's clearly settling in — that's the conversation the whole booth exists for.

---

## 3. Tier 1 — the 30-second hook (most of your traffic)

Goal: not to explain the product. Goal: to make them remember your name and, ideally, take a card or scan a QR code. You will say maybe four sentences.

**Script:**
> "This is [Product] — we trace a request across every service it touches and show you exactly where it broke, in seconds instead of grepping five different logs. Here, watch—" *(point at the loop, tap the pre-loaded incident)* "—that's a live trace, root cause highlighted, twelve seconds. Grab a card, there's a two-minute version of this on the back if you want to try it yourself later."

- No install talk. No architecture talk. No configuration. Those are irrelevant to someone who hasn't decided you're worth two minutes yet.
- Have a QR code on the table/card linking to a short recorded version of exactly this moment — captures the person who's curious but truly can't stop.

---

## 4. Tier 2 — the 3–5 minute core demo (your bread and butter, run this most)

Goal: land ONE "oh, that's actually useful" moment, tied to a real pain, and get to a name + qualifying question before they drift off.

**Structure (this replaces your 15-minute webinar entirely — no install, no config, ever, on the floor):**

1. **Anchor the pain (20 sec)** — "You know that moment where a request is slow and you've got six services and no idea which one's the problem? That's what we're fixing."
2. **Show the trace, live (90 sec)** — Pull up a pre-loaded realistic trace (a checkout flow, an API call — whatever matches the audience's stack). Walk one finger down the waterfall: "Request comes in here, fans out to these three services, and — there — that one call to the payments service took 4 of the 4.2 seconds. Everything else is noise." Click into the failing span, show the error and the exact line/context. Total: root cause found, on stage, in under two minutes of screen time.
3. **One differentiator, stated plainly (30 sec)** — Whatever actually separates you from the obvious alternative (Jaeger, Datadog APM, Honeycomb, whatever your ICP already knows) — say it as a single sentence, not a feature list. E.g., "Unlike most tracers, this ships as a single binary with no code changes — we auto-instrument at the eBPF layer." Pick your real one; don't invent generic ones here.
4. **Turn it back to them (60–90 sec)** — "What's your stack look like — are you already running something for this, or is it mostly logs and hope right now?" Their answer tells you whether to escalate to Tier 3 or wrap here.
5. **Close (20 sec)** — Card/QR + one specific ask: "If you want to see it against your own traces, we're doing that at [next avail] — want me to grab your badge?"

Never open this tier with install/config. If a *technical* visitor explicitly asks "how do I deploy this," that's a great sign — answer it in one sentence ("single binary, one flag, no code changes" or whatever's true) and immediately return to the trace on screen. Don't let deployment mechanics eat your only two minutes of attention.

---

## 5. Tier 3 — the 15–20 minute deep dive (your actual pipeline)

This is the only tier where your old webinar content has a home — and even here, reorder it. Don't open with install. Open the same way Tier 2 does (pain → live trace → root cause), because that's what earned you the 20 minutes in the first place; don't waste it re-litigating the hook.

**Structure:**
1. **Recap the hook fast (1 min)** — "So like I showed you, root-causing in seconds instead of stitching logs together — let's go deeper on how that actually works."
2. **Discovery, briefly, out loud (2–3 min)** — Ask what they run today, team size, what breaks most often for them. This isn't filler — it tells you which of the next parts to spend time on, and it's the material your follow-up email will reference tomorrow.
3. **Deeper walkthrough mapped to what they said (7–10 min)** — Architecture, instrumentation approach, sampling, retention, whatever's relevant to their stack specifically. Install/configure belongs *here*, and only the parts relevant to their environment — not a generic step-by-step.
4. **Proof (2 min)** — one customer story or benchmark that maps to their situation.
5. **Close with a real next step (2 min)** — not "here's a card," but a specific calendar ask: "Want fifteen minutes next week where I run this against a sample from your own stack?" Book it on the spot if you can — a meeting booked at the booth is worth far more than a warm lead who "meant to follow up."

Capture notes immediately after they leave: what they run today, what hurts, what they asked, what you promised. This is what makes tomorrow's follow-up feel specific instead of a mail-merge — and it's the difference between this conversation turning into pipeline or evaporating.

---

## 6. Lead capture — tier it the same way you tier the demo

Don't treat every badge scan as a lead. Score at the moment of capture, not after:

- **Scan only, no real conversation** → one light follow-up touch max, or none. Don't burn a personal email on someone who doesn't remember stopping.
- **Tier 2 conversation** → a short personal note referencing what they said their stack was, plus the relevant asset (the 2-minute recorded version, or a doc matching their pain).
- **Tier 3 conversation / booked meeting** → personal note within 24–48 hours, referencing the specifics you captured, with the concrete next step you agreed on. Every day of delay roughly halves the chance they respond — send this the same evening if you can, not after the show ends.

Bring a simple way to jot 3–5 words per conversation (notes app, a stack of index cards, whatever survives a loud floor) — without it, your Tier 3 follow-ups degenerate into generic templates and lose everything that made them worth having.

---

## 7. Staffing across two days

- Never run the booth solo for a full day — voice and attention both degrade badly by hour four, and a tired pitch reads as a bored pitch.
- Rotate in 2–3 hour shifts if you have more than one person; if it's just you, build in real breaks, not just bathroom trips — walk the floor, reset.
- Assign roles when two people are staffing together: one runs point on Tier 1/2 (higher volume, keeps energy up), the other peels off qualified Tier 3 conversations so the front of the booth never goes empty.
- Rehearse the 30-second hook and the 3-minute core demo out loud, timed, before day one — not the 20-minute version, that one takes care of itself once you know the material. The short ones are the ones that fail from being unrehearsed, because there's no room to recover if you fumble the opening line.

---

## 8. Before the show (this is where most of your actual pipeline comes from, not the floor)

- Pull the attendee/speaker list if available and identify 15–30 people who match your ICP; send a short, specific outreach ("15 min at your booth-side coffee Tuesday?") 1–2 weeks out. A meeting booked in advance is worth far more than hoping the right person walks by.
- Post where your audience already is (mailing list, socials, relevant Slack/Discord communities) that you'll be there — lead with what they get from stopping by, not your booth number.
- Preload 2–3 realistic trace scenarios matched to what this specific conference's audience actually runs, so the demo feels native to them instead of generic.

## After the show

- Send Tier 3 follow-ups same-day or next morning, referencing specifics.
- Send Tier 2 follow-ups within 48 hours with the relevant asset.
- Tag everything by source and tier in your CRM so you can measure cost-per-qualified-conversation for this show against your other channels — that's what decides whether you do this conference again, not badge-scan count.