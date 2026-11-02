ℹ️ This is general guidance from memory, not legal advice. I didn't re-check the live Twitch policy pages. Have counsel review the contract, and confirm the Twitch wording before the stream.

## Questions that change the answer

1. Where are Marco and the Rust streamer based? France, the UK, Germany, and the US have different disclosure rules.
2. Is Marco streaming on his own time, or is it part of his job (paid hours, expected output)?
3. Is the Go SDK open source?
4. Will the paid stream show unreleased features?
5. Do you want to reuse the VOD or clips in your own channels or ads?

## 1) Marco on his own Twitch channel

**Do first (about 1 hour):**

1. **Check his employment contract.** Look at the side-activity clause, the IP clause, and any social media policy. If streaming is now part of the job, the content is probably work product. Write down which one it is.
2. **Write a one-page streaming policy** and have him sign it:
   - Never show secrets, internal dashboards, Slack or DMs, customer data, or unreleased features.
   - Use a dedicated sandbox account and a scoped, rotatable API key.
   - Stream with a short delay.
   - Capture only the code window, not the full desktop.
   - Keep secrets in env vars and out of the code on screen.
3. **Disclose the employment.** Employment is a "material connection" under the FTC Endorsement Guides and under EU and UK ad rules. Marco should say "I work at X" at the start of any stream focused on your SDK. Put it in a Twitch panel and the title too.
4. **Use Twitch's Branded Content label** when a session is effectively promoting your product, especially if you pay or direct him. Check the current policy wording, since employee streams are a gray area. Turning it on is the safe default.
5. **Agree on who owns the code.** Code written on stream with your SDK is his own unless the contract or policy says otherwise. Decide what you want, and ask him to open-source demo projects.
6. **Decide on pay.** If you pay Marco extra for streaming, treat it like the sponsored stream in section 2. If you don't, state that streaming is voluntary so there is no unpaid-work claim.

**Platform notes:**

- VODs, highlights, and clips are public. A leaked key stays visible, so rotate keys at once if one leaks.
- Check music use. Copyrighted music in VODs draws DMCA strikes.
- If you use your logo in his overlay, give written permission under your brand guidelines.

## 2) Paid Rust streamer, 1 hour next month

**Contract (a template review is usually 1–2 hours of legal time). Cover:**

- **Parties:** The streamer, or their agency if they have one.
- **Deliverable:** One live hour on a set date and platform. Include a reschedule and cancel rule, VOD retention, and whether they may re-air it.
- **Fee and payment:** Include any free credits, since credits count as compensation. Expect a tax form (W-8/W-9 or equivalent), an invoice, and VAT handling.
- **Editorial independence:** They keep their honest opinion and you don't approve a script. Limit your review to factual accuracy and to leaks of confidential information. Devs distrust scripted content, so this protects the value you're buying.
- **Disclosure clause:** Spell out what they must do (see below).
- **Claims:** No performance or comparison claims without a substantiated, approved fact sheet from you.
- **Exclusivity:** Decide whether to bar competitor products for a window around the stream. Expect to pay more for this.
- **Usage rights:** Say whether you may repost the VOD and clips, for how long, and where. Paid ads using their face or voice are priced separately.
- **IP:** Recommend that the streamer owns the code they write, with a license to you to showcase it.
- **Conduct and termination:** Include a brand-safety clause, a termination right, and mutual indemnities.
- **Confidentiality:** Cover any pre-release access. Pair it with an embargo and avoid showing unreleased features live.

**Disclosure (shared responsibility, and you are liable too):**

- The streamer turns on Twitch's **Branded Content label**.
- They say it aloud at the start and repeat it at intervals, because viewers join late.
- Put "sponsored" or "#ad" in the title and in any cross-posts.
- If the VOD goes to YouTube, they tick "includes paid promotion". Posts on X need a disclosure tag too.
- Local rules apply. France requires a written contract with mandatory clauses and the label "Publicité" or "Collaboration commerciale". The UK expects "Ad" under ASA/CMA rules. Germany is strict.
- Monitor the stream and have them fix any miss.

**Product setup (do in the next 2 weeks):**

- Create a sandbox tenant and a scoped, time-limited API key with a quota. Revoke it after the stream.
- Run a 30–60 minute dry run a week before. Fix docs and quickstart friction that surfaces.
- Have an engineer on standby in a private channel during the stream.
- Prepare a chat command or link with a unique UTM or code to measure signups. Keep any tracking within your privacy policy.
- Brief your staff: if they chat, they disclose they work at your company, and they don't spam.
- Clear the brand assets and usage rules in writing.

**Timeline:**

| Week | Task |
|---|---|
| 1 | Pick the streamer, send the brief, finalize the contract and tax forms |
| 2 | Build the sandbox and fact sheet, sign the contract |
| 3 | Dry run, fix docs gaps, rotate the keys |
| 4 | Stream, then monitor disclosure, revoke the key, and pay out |

⚠️ **Biggest risks:**

1. Secrets leaking on screen. In the contract, you can require that no keys or customer data appear.
2. Undisclosed sponsorship. This is a liability for both you and the streamer.
3. Claims you can't back up.