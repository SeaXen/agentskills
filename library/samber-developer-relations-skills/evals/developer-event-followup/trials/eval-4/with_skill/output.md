# DevOpsDays Montreal and Paris: what you can send

**Short answer:** don't send the 20% code to everyone. Send it by email only to the ~40 who ticked "send me product news", and to card holders where the gate below allows it. Publish the code on a public recap page for everyone else. The colleague's CASL claim is a myth.

I used `developer-event-followup` and its two references. This is a plan, not legal advice. Your privacy owner should confirm the rows marked ⚠️.

## Assumptions

You haven't answered the interview yet, so I assumed the following. Tell me which are wrong.

- ℹ️ The ~150 entries are split across both events, and the split is unknown. Montreal is CASL, Paris is France/CNIL.
- ℹ️ The draw form said only "Enter to win - winner announced at closing". It didn't say "your email is used for marketing".
- ℹ️ The "product news" box was a separate, unticked-by-default box.
- ℹ️ Nobody can say what the engineers told card-givers.
- ℹ️ Everyone is an adult working professional. Anyone under 18 gets no marketing at all.

## 1. The CASL claim: wrong on three counts

1. **The six-month window isn't about business cards.** CASL s.10(10) gives six months after an inquiry or application, and two years after a purchase or contract. Both belong to an "existing business relationship".
2. **A card is a different route.** Under s.10(9)(c), implied consent applies when the person disclosed their address to you, didn't say they refuse messages, and the message is relevant to their business role. That route has no statutory expiry. It lapses if the message stops being relevant to their role.
3. **CASL only covers Montreal.** It says nothing about Paris contacts or the draw entries. The "B2B needs no consent" idea is also false in much of the EU.

The code is still not a free pass for Montreal cards, for two reasons:
- A card handed to an engineer is an attendee-initiated disclosure, so the CASL route plausibly works. ⚠️ Confirm with the privacy owner.
- The skill's second test is that the promise made when details were taken must cover the message. If the engineers said nothing about marketing, the card supports a personal note, not a bulk promo.

## 2. Gate table

| Source | What they heard or read | Jurisdiction | Requested reply allowed? | Marketing (the 20% code) allowed? |
|---|---|---|---|---|
| Draw entries, no tick (~110) | "Enter to win, winner announced at closing" | Montreal (CASL) / Paris (France) | Yes, but only the prize notice to the winner | ❌ **No.** A draw entry never widens anything. The ICO says prize-draw consent "can't be carried over for anything else". |
| Draw entries with the "product news" tick (~40) | A separate, ticked opt-in | Montreal / Paris | n/a | ✅ **Yes**, for product news, with sender identification, postal address and unsubscribe link in each message |
| Cards, Montreal | Unknown (assumed: nothing about marketing) | CASL s.10(9)(c) | Yes, for anything the engineer promised | ⚠️ Plausible if the message is relevant to their role. Confirm what was said. |
| Cards, Paris | Unknown (assumed: nothing about marketing) | France, CNIL | Yes, for anything promised | ❌ **No** unless they were informed at collection. France allows B2B prospecting on legitimate interest only when the person was informed at collection, the message relates to their profession, and objecting is easy. Generic addresses (contact@, info@) are excluded. |

Two points on the opted-in 40:
- ⚠️ A discount code is a commercial offer, and the box said "product news". I'd send it inside a product-news email. Have the privacy owner confirm that a promo fits that wording.
- Check each opt-in against the form it came from, since the two events may have used different forms.

## 3. What to do, by segment

**Draw entries without the tick (~110)**
- No email beyond the winner's prize notice.
- Publish a **public recap page** carrying the 20% code and a "get product news" opt-in link. It reaches everyone, needs no contact data, and triggers no review.
- Don't send the entrants an email asking them to opt in. Under prior-consent rules that email can itself count as advertising.
- Delete the raffle data once the prize ships. Keep only the ~40 opted-in records, as a separate record with source and date.

**The ~40 opted-in**
- Send one product-news email with the code. It has to carry sender identification, a postal address and an unsubscribe link.
- Load them into the CRM as marketing-eligible, with source, purpose line and capture date.

**Card givers**
- The engineer who got the card writes a personal note from their own address. It quotes the conversation and delivers whatever was promised.
- Add the code to that note only for Montreal cards where the role-relevance and "what was said" checks pass. Montreal messages need the sender identification and unsubscribe mechanism.
- For Paris cards, send the personal note and leave the promo out unless the engineer told them they'd get offers.

**Everyone, before any send**
1. Dedupe on email. Match against the CRM: existing customers go to the account owner and open deals to the deal owner.
2. Apply earlier unsubscribes and objections first. They override everything above.
3. Never import a bought or rented list. Not an issue here, but marketing may ask.

## 4. Drafts

**Opted-in email (~40)**
```
From: <staffer or DevRel name>, <company>
Subject: Product news, and a 20% code for DevOpsDays folks

Hi <first name>,

You ticked "send me product news" when you entered our draw at DevOpsDays <Montreal/Paris>, so here it is.
<One or two lines of real product news.>
As a thank-you for stopping by: 20% off with code <CODE> until <date>.

<sender identification + postal address + unsubscribe link>
```

**Card note (Montreal, if the checks pass)**
```
Subject: <topic from your conversation>

Hi <first name>,

We talked at DevOpsDays Montreal about <their problem, in their words>.
<The item or next step you agreed.>
If it's useful, there's a 20% code for the team: <CODE>.

<engineer name>
<sender identification + postal address + unsubscribe link>
```

**Winner notice:** prize details only, with no promo.

**Public recap:** slides, answers to the questions you heard most, the 20% code, and the opt-in link.

## 5. Stop rules and measurement

- Send each person at most one message unless they reply or click.
- Pause the batch on the second spam complaint, or if unsubscribes exceed what your last event produced. Company mailboxes rarely report complaints, so count unsubscribes and "who are you?" replies too.
- Honour unsubscribes at once and keep a permanent suppression list. CASL and CAN-SPAM allow 10 business days at most. The right to object in the EU is absolute.
- Tag the cohort (for example `evt-dodmtl-2026` and `evt-dodparis-2026`) on code redemptions and signups. Read redemptions and activations at 30, 60 and 90 days against a non-event baseline. Label the threshold "self-set".
- The skill gives no published benchmark for event follow-up rates, so set the target from your own previous event.

## Questions that would change this plan

1. Exact form text for each event's draw, and whether the product-news box was unticked by default.
2. What the engineers said when they took the cards.
3. The Montreal/Paris split of entries and cards.
4. Does the privacy owner treat Quebec privacy law as stricter than CASL for the draw entries? I haven't assessed that, and it could only make the Montreal rows stricter.