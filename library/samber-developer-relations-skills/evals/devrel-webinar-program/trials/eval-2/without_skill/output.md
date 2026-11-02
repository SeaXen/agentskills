# Brightfold webinar lead handoff rule, v1

**Parties:** Dana (VP Sales) and Marketing owner
**Applies to:** every episode of the monthly developer webinar
**Review:** after episode 4, or earlier if a complaint or regulator contact comes in

## 1. Purpose

Send Sales the attendees most likely to want a conversation, and don't contact people who haven't agreed to one. We still want most of the ~70 live attendees in Sales' hands. We get there by adding qualifying signals and fixing consent capture, not by auto-pushing everyone.

## 2. Why not "all 70, every time"

- **Consent is currently invalid for EU registrants.** The marketing consent box is ticked by default. Under GDPR, pre-ticked boxes are not valid consent (CJEU *Planet49*, 2019). About a third of registrants are in Germany and France, so for them we have no consent on file. This is the main risk.
- **German rules are the strictest.** Germany's UWG §7 generally requires prior consent for B2B marketing emails, and for B2B phone calls at least a demonstrable presumed consent. A work email plus "they expect a call" doesn't meet that standard.
- **"They gave us their email" covers what the form told them.** If the form and privacy notice only promised webinar access and marketing consent, a sales call goes beyond that purpose. In the US this is a lower legal risk, but it still produces a poor call.
- **The 38% benchmark doesn't support the ask.** An MQL is a lead that passes a scoring threshold, so a 38% rate cannot justify sending 100% of attendees to SDRs. We don't know which source or MQL definition the 38% comes from. We'll measure our own rate (section 7).

## 3. Routing tiers (run the morning after each episode)

| Tier | Who | Action |
|---|---|---|
| **A: Route to SDR** | Passes the **consent gate**, the **fit gate** and the **intent gate** below | Into the SDR queue by 10:00 local, next business day |
| **B: Nurture** | Attended but fails fit or intent, or is a US attendee below the A bar | Recording and follow-up email only. Re-scored at the next episode or on a new signal |
| **C: Hold** | No valid consent for sales contact (see gate 1), or unknown country | No SDR contact. Recording email only if the transactional/marketing basis allows it |

**Gate 1, consent.**
- **US:** register consent is fine as collected, provided the privacy notice was shown. Calls must be manual (no autodialer or prerecorded calls). Any text messages need separate written consent. Honor suppression and opt-outs.
- **Germany:** SDR contact only after an affirmative opt-in to sales contact (unticked box, demo request, or in-webinar "talk to us" click).
- **France:** same as Germany by default. Counsel may confirm that role-relevant B2B contact on legitimate interest, with notice and an easy objection, is acceptable. Until then, treat France as Germany.
- **Unknown country:** treat as EU. Derive country from company country, falling back to phone prefix, then IP.

**Gate 2, fit.** All of: company size at or above a threshold Sales sets in writing (currently unset), a title in a defined buyer or influencer list (engineering lead, platform, payments, product, or above), and a use case that matches our product.

**Gate 3, intent (any one).**
- Watched at least 50% of the session.
- Asked a question or answered a poll.
- Clicked a CTA such as demo, docs or trial.
- Requested contact.
- Chose "evaluating or building now" as the use case.

Both thresholds (company size, 50% watch time) are starting points to tune after episode 2.

## 4. Fast lane

Anyone who requests contact (demo, "talk to sales", chat) goes to the SDR queue the same day, regardless of tiers, as long as the request is documented in the record.

## 5. SDR conduct

- First touch references the webinar topic and, where applicable, what the person asked or clicked. It doesn't open with "you registered".
- Maximum 3 touches over 10 days (email, call, email). No reply means back to nurture.
- Any "stop" or "don't contact me" is recorded and honored within 1 business day, across Sales and Marketing.
- The SDR queue shows tier, country, consent source and timestamp for every lead.

## 6. Form and data changes (Marketing, before episode 1 under this rule)

1. **Untick** the marketing consent box.
2. Split consent: webinar access (required), marketing emails (optional), and "a Brightfold sales rep may contact me" (optional).
3. Make phone optional, and store only what is needed.
4. Link a privacy notice that names the purposes, retention and the right to object.
5. Record country, consent text version and timestamp for every registrant.
6. **Existing registrants** collected with the pre-ticked box are not treated as having consented. Run a re-permission email in Germany and France before any sales contact.
7. Record in the CRM which gate each lead passed.

## 7. Test of the 38% claim

For the next 4 episodes, split Tier A and US-eligible Tier B leads randomly into two groups: SDR gets everyone in group 1, and group 2 follows this rule. Compare:
- meetings held per 100 leads
- opportunities created
- SDR hours per meeting
- unsubscribes and complaints

We agree on the MQL definition before episode 1 and the result decides the thresholds at review. This is a small sample, so read it as directional. If push-all clearly wins on meetings and doesn't raise complaints, we widen the US rule. The EU consent gate doesn't change either way.

## 8. Expected volume (assumption, to be checked after episode 1)

I have no attendee data, so these are guesses. For ~70 live attendees, perhaps 15 to 30 land in Tier A, mostly US plus opted-in EU. Dana should treat that as the starting target.

## 9. Open items before signing

- ⚠️ A privacy or employment lawyer should confirm the Germany and France position, since this is not legal advice.
- Sales names the company-size threshold and buyer title list.
- Confirm what the current form and privacy notice actually told registrants.
- Confirm the phone field is optional or required today.

## 10. Signatures

Dana, VP Sales: ______________ Date: ______

Marketing owner: ______________ Date: ______