# Live streaming plan: Marco's channel and the paid Rust streamer

I used the `devrel-live-streaming` skill and its two references. I did not re-read the live platform pages in this session, so recheck the **[platform]** items below before you sign anything. Where I assume something, I say so.

## Do these first

1. **Marco, this week:** put the employer disclosure on screen, in the title and aloud, and tick Twitch's Branded Content box. Audit his past streams for leaked keys. Twitch Affiliates keep past broadcasts for 14 days **[practitioner quoting Twitch help]**, so check soon.
2. **Rust streamer, before any money moves:** put the disclosure and the platform paid-promotion tick in the contract. Send the contract to counsel.
3. **Both:** get a named moderator and a pre-flight checklist in place before the next stream.

## 1. Refusals triggered

| Move | Applies to | What to do instead |
| --- | --- | --- |
| Employee streams the product on a personal channel with no disclosure | Marco, if he doesn't disclose today (I don't know whether he does) | Disclosure line plus branded-content tick (section 2) |
| Host alone, reading chat | Marco, 3 nights a week, probably solo | One named moderator per chat |
| Live-code on the daily machine and accounts | Marco | Pre-flight checklist (section 2) |
| Trust the platform to keep the recording | Marco | Record locally every time; export inside the window |
| Promise a daily stream from one advocate | Marco, at 3 nights a week | Fixed slots, run in seasons |

## 2. Marco: his own channel

**Verdict.** This is the "solo build-along on an advocate's channel" rung. It builds peer credibility, but the channel leaves with him. I wouldn't make it the company program. Keep it, add safeguards, and treat any company-owned show as a separate decision.

### Legal

- **Disclosure of employment.** The US FTC Endorsement Guides (16 CFR 255) treat employment as a material connection that must be disclosed in the content itself **[law]**. If you or Marco are in the UK or EU, those markets have their own advertising and unfair-commercial-practice rules. Ask counsel there.
- **Wording:** "I work at [company]; this is our product." Use it in the title, on screen and aloud.
- **Anything beyond disclosure.** The skill doesn't cover these, so they are my suggestions, not skill content. Ask HR or counsel:
  - Does his employment contract allow off-hours streaming of company work?
  - Who owns the code and recordings from those streams?
  - Does he count as being paid for those nights?

### On the platform (Twitch)

- **Branded Content box.** Twitch exempts only "your own products and services" from the box. Whether an employee streaming the employer's product counts is unclear. Tick it anyway, since it carries no discovery penalty **[platform, Branded Content Guidelines]**.
- **Moderation.** Name a moderator who is not Marco. Before each stream, set up:
  - blocked terms and AutoMod;
  - a Shield Mode preset for raid floods;
  - a rule that only moderators post links.
- **Recordings.** Past broadcasts are off by default **[practitioner quoting Twitch help]**. Run a local recording every time and export before expiry.
- **Account ownership.** Affiliate status sits with whoever owns the login. If you want a company-owned show later, create it on a company login with 2FA and named editor or moderator roles.

### Pre-flight checklist (every stream)

- Use a demo account with scoped, low-limit SDK keys, and rotate them after the stream.
- Use a separate OS user or browser profile with no saved passwords, no personal tabs and notifications off. Clear shell history.
- Keep a privacy scene ready before any credential screen. Never capture the encoder settings window.
- Keep the stream key in a password manager, and prefer RTMPS.
- Check audio first, and make sure the code font is readable on a phone.
- Never review a viewer's private repo on air without written consent.
- Use no copyrighted music.

### If a key or token already appeared on a past stream

Revoke and rotate it now. Audit archives, Highlights and viewer clips. Hand it to your security team as an incident, not a stream fix.

## 3. The paid Rust streamer: one hour next month

**Verdict.** This is the "guest on established developer streams" rung, which the skill ranks as the most efficient way to start. It also adds one disclosure duty because you are paying.

### Contract terms

1. **Disclosure.** Require the platform's branded-content or paid-promotion tick and an on-air line: "[company] is paying for this stream." **[platform]** **[law]**. The platform requirement is enforced. Twitch's Branded Content box is required for paid or sponsored content. YouTube applies its paid-placement and endorsement rules to live streams.
2. **Editorial freedom.** Brief 2–3 points and let them write their own words. Don't script their opinions.
3. **Tagged link.** Give them one, so you can attribute signups.
4. **Reuse rights, if you want clips.** Get written consent to record and reuse their face, voice and code. The skill requires this for guests. Their channel's own rules still apply.
5. **Counsel.** The UK and EU have their own rules on paying streamers. Have counsel review before signing. Payment mechanics, tax forms and invoicing aren't in the skill, so ask finance.

### Platform setup

- **Their channel, their moderation.** Offer to supply a moderator for the hour. Your team must not post your links in their chat without their say-so, because that is policed by each channel.
- **If they stream on LinkedIn:** LinkedIn discourages promotional streams **[platform]**. Make it a teaching session, not a pitch.
- **Setup you provide:**
  - a clean demo account with scoped keys, rotated after;
  - a test call before the day;
  - a goal plus a fallback task for the hour.
- **Product fit.** I assume the streamer can build with the product in the language they use. Your SDK is Go and they are a Rust streamer. If there is no Rust-friendly path, choose the task accordingly. Don't invent one.

## 4. Season cadence and timeline

You said "next month", so I assumed a mid-November session. Today is 2026-10-31.

| When | What |
| --- | --- |
| Now to week -4 | Marco's disclosure fixes, moderator, pre-flight list. Pick the streamer's platform and date. |
| Week -3 | Sign the contract (counsel reviewed). Send the briefing points and the tagged link. |
| Week -2 | Test call. Set up the demo account. The streamer announces the session. |
| Day of | Moderator on, local recording on, privacy scene ready. |
| Within 48 hours | Export the archive and cut 2–4 clips. Rotate keys. Post a recap. |

Marco's 3 nights a week is above what the skill considers sustainable for one person. If you keep it, run it in 6–8 episode seasons with a break, not an open-ended commitment.

## 5. Metrics and stop rule

- **Outcome:** signups from tagged links, "how did you hear" answers naming the stream, and docs or SDK fixes traced to viewer questions.
- **Show health:** average concurrent viewers (not peak), unique chatters divided by average viewers, returning viewers, and archive watch time.
- **Continue bar:** `episodes 6–8 vs 1–3: average viewers [up/flat], chat rate [up/flat]; at least [n] attributed signups or [n] docs fixes over the season`. Set `n` before the next episode and never move it afterward.
- **Stop rule:** at season end, if you are below the bar, drop to the guest rung and say so.
- The skill says no published benchmark exists for developer streams. Take baselines from Marco's last 3 episodes and the paid session.

## 6. Open questions

1. Does Marco disclose his employer on stream today? This is the biggest exposure.
2. Has any key, token or customer data appeared on his past streams?
3. Does he have a moderator, and who could be one? *(owner: to confirm)*
4. What are his average viewers, chatters and attributed signups over the last 6 episodes?
5. Who owns the login for the paid session: the streamer's channel, or one of yours?
6. Where are your company and the streamer based (US, UK, EU)? That decides which advertising rules apply.
7. What is the budget for the streamer?
8. Is there a signup-source field or tagged links today?