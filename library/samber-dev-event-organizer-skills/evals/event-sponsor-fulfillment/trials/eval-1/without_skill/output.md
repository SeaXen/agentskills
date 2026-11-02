# Harborline DevSummit 2026: sponsor tracker and welcome emails

I did not open the prospectus PDF, so the perk blocks in the emails are placeholders. Read "Before you send" first.

## Before you send

1. **Verify the prospectus perks.** Today is 15 Oct and the event is 14 Nov, so you have 30 days. The prospectus was written months ago. Check each perk against what you can still deliver: print lead times, pre-event promotion windows, booth or talk slots, and the attendee-data terms. Remove or swap any perk you can't deliver before you send. A welcome email that lists a perk becomes a promise.
2. **Decide logo timing per sponsor.** Verilume and Bitmoor are paid, so put their logos up tonight. For Klarstack and Nordpath, check whether your signed agreement ties logo use to signing or to payment.
   - If it ties logos to signing, put all four up. Order them by tier: Platinum, Gold, Gold, Silver.
   - If it ties them to payment, hold Klarstack's logo. Nordpath is a judgment call, since it has paid half.
   - Either way, hold tangible, costly perks until payment clears. Examples: booth, speaking slot, attendee data or lead retrieval, printed placements.
3. **You need logo files.** Use their official SVG or high-res PNG, supplied by them. Don't pull logos off their websites. The emails ask for them.
4. **Don't mention other sponsors' tiers, amounts, or payment status.** The emails below don't.
5. **Fill in the placeholders.** I wrote none of the contact details, deadlines, or perk lists. Dates in the tracker are proposals.

## Money snapshot (as of 15 Oct 2026)

| Sponsor | Tier | Contracted | Received | Outstanding | Status |
|---|---|---|---|---|---|
| Verilume Systems | Platinum | $14,000 | $14,000 (2 Oct) | $0 | ✅ Paid |
| Klarstack | Gold | $6,000 | $0 | $6,000 | ❌ Unpaid, invoice sent 9 Oct (6 days) |
| Nordpath Analytics | Gold | $6,000 | $3,000 | $3,000 | ⚠️ Partial, rest pending their PO |
| Bitmoor | Silver | $2,000 | $2,000 | $0 | ✅ Paid |
| **Total** | | **$28,000** | **$19,000** | **$9,000** | 68% collected |

- ⚠️ Confirm Nordpath's $3,000 has landed in the bank, not just that they said they wired it.
- ⚠️ Your payment terms aren't in what you told me. Check the Klarstack invoice due date. If it's net 30, it isn't late yet and the nudge below is a courtesy.
- ⚠️ $9,000 is 32% of the sponsorship budget. Don't commit spend that depends on it until it arrives.

## Tracker (CSV)

Save as `sponsors.csv` and import it into Sheets or Numbers.

**Tab 1: Sponsors**

```csv
sponsor,tier,contracted_usd,received_usd,outstanding_usd,payment_status,invoice_sent,last_payment_date,payment_note,primary_contact,contact_email,welcome_sent,logo_received,logo_live_on_site,blurb_received,website_url,notes
Verilume Systems,Platinum,14000,14000,0,paid,,2026-10-02,,,,no,no,no,no,,
Klarstack,Gold,6000,0,6000,invoice_unpaid,2026-10-09,,Nudge in welcome email; follow up if unpaid by [DATE],,,no,no,no,no,,
Nordpath Analytics,Gold,6000,3000,3000,partial,,[DATE of first wire],Balance due when their PO clears; need PO number and expected date,,,no,no,no,no,,
Bitmoor,Silver,2000,2000,0,paid,,[DATE],,,,no,no,no,no,,
```

Fill in `outstanding_usd` with a formula: `=C2-D2`.

**Tab 2: Deliverables**

One row per perk per sponsor. Paste the verified perk list per tier here. `gated_on_payment` marks perks you hold until the money clears.

```csv
sponsor,perk,gated_on_payment,deliverable_by,owner,asset_needed_from_sponsor,status,notes
Verilume Systems,[PERK 1 from prospectus],no/yes,[DATE],,[e.g. logo, copy],not_started,
Verilume Systems,[PERK 2],,,,,not_started,
Klarstack,[PERK 1],,,,,not_started,
Nordpath Analytics,[PERK 1],,,,,not_started,
Bitmoor,[PERK 1],,,,,not_started,
```

**Tab 3: Milestones (proposed, adjust to your calendar)**

```csv
date,milestone,applies_to
2026-10-15,Welcome emails sent; logos up for paid sponsors,all
2026-10-22,Sponsor logo + blurb + contact due,all
2026-10-22,Klarstack invoice follow-up if still unpaid,Klarstack
2026-10-24,Nordpath PO number and expected payment date confirmed,Nordpath
2026-10-29,Attendee names / ticket allocations confirmed,all
2026-11-05,Final perk logistics confirmed with each sponsor,all
2026-11-07,All sponsor balances received (hard target),Klarstack; Nordpath
2026-11-14,Event day,all
2026-11-21,Thank-you + recap sent,all
```

Why 7 Nov for balances: it leaves a week of buffer to pull or adjust payment-gated perks before the event.

## Welcome emails

Placeholders in `[BRACKETS]`. Send each from your own address, individually, not as a group email.

### 1. Verilume Systems (Platinum, paid)

**Subject:** Welcome to Harborline DevSummit as our Platinum sponsor

Hi [FIRST NAME],

Thank you for joining Harborline DevSummit (14 November, [CITY/VENUE]) as our Platinum sponsor. We received your payment on 2 October, so you're all set on that side. Thank you for the speed.

**What your Platinum sponsorship includes**
[PASTE VERIFIED PLATINUM PERKS]

**What we need from you by 22 October**
- Logo: SVG preferred, or PNG at least 1000 px wide, plus a light-background and a dark-background version if you have both
- A 50-word company blurb for the website and event materials
- Your website URL and the one link you want us to use
- A single point of contact for event logistics, with email and mobile
- [ANY PERK-SPECIFIC ITEMS: speaker name and bio, booth requirements, ticket names]

Your logo will go live on the sponsors section of our website [tonight / as soon as we receive it].

I'll be your contact until the event. Reply here or reach me at [PHONE].

Thanks again,
[NAME]
[ROLE], Harborline DevSummit

### 2. Klarstack (Gold, invoice outstanding)

**Subject:** Welcome to Harborline DevSummit as a Gold sponsor

Hi [FIRST NAME],

Thank you for joining Harborline DevSummit (14 November, [CITY/VENUE]) as a Gold sponsor. We're glad to have you.

**What your Gold sponsorship includes**
[PASTE VERIFIED GOLD PERKS]

**What we need from you by 22 October**
- Logo: SVG preferred, or PNG at least 1000 px wide
- A 50-word company blurb for the website and event materials
- Your website URL and the one link you want us to use
- A single point of contact for event logistics, with email and mobile
- [ANY PERK-SPECIFIC ITEMS]

**One admin note.** Our invoice [INVOICE NUMBER] for $6,000 went out on 9 October and we haven't seen payment yet. If it's already in your payables process, no action needed. If it needs a PO, a different billing contact, or a different format, tell me and I'll reissue it today. [IF PAYMENT-GATED: Your [PERK] will be confirmed once the payment is received.]

[LOGO LINE, pick one: "Your logo will go live on our sponsors page as soon as we receive the files." OR "We'll add your logo to the website once the invoice is settled."]

Reply here or reach me at [PHONE].

Thanks,
[NAME]
[ROLE], Harborline DevSummit

### 3. Nordpath Analytics (Gold, half paid)

**Subject:** Welcome to Harborline DevSummit as a Gold sponsor

Hi [FIRST NAME],

Thank you for joining Harborline DevSummit (14 November, [CITY/VENUE]) as a Gold sponsor. We're glad to have you. Thanks also for the first payment of $3,000, which [we've received / I'm confirming with our bank this week].

**What your Gold sponsorship includes**
[PASTE VERIFIED GOLD PERKS]

**What we need from you by 22 October**
- Logo: SVG preferred, or PNG at least 1000 px wide
- A 50-word company blurb for the website and event materials
- Your website URL and the one link you want us to use
- A single point of contact for event logistics, with email and mobile
- [ANY PERK-SPECIFIC ITEMS]

**On the remaining $3,000.** Could you send me the PO number and the date you expect it to clear? The event is on 14 November, so ideally the balance arrives by 7 November. If the PO needs anything from us, such as an invoice referencing the PO number or a W-9, tell me and I'll send it right away. [IF PAYMENT-GATED: [PERK] will be confirmed once the balance is received.]

Your logo will go live on our sponsors page [as soon as we receive the files].

Reply here or reach me at [PHONE].

Thanks,
[NAME]
[ROLE], Harborline DevSummit

### 4. Bitmoor (Silver, paid)

**Subject:** Welcome to Harborline DevSummit as a Silver sponsor

Hi [FIRST NAME],

Thank you for joining Harborline DevSummit (14 November, [CITY/VENUE]) as a Silver sponsor. Your payment is received, so you're all set on that side.

**What your Silver sponsorship includes**
[PASTE VERIFIED SILVER PERKS]

**What we need from you by 22 October**
- Logo: SVG preferred, or PNG at least 1000 px wide
- A 50-word company blurb for the website
- Your website URL and the one link you want us to use
- A single point of contact for event logistics, with email and mobile
- [ANY PERK-SPECIFIC ITEMS]

Your logo will go live on the sponsors section of our website [tonight / as soon as we receive it].

Reply here or reach me at [PHONE].

Thanks,
[NAME]
[ROLE], Harborline DevSummit

## Tonight, in order (about 45 minutes)

1. ⏳ 5 min: check bank for Nordpath's $3,000. Check the Klarstack invoice due date.
2. ⏳ 15 min: open the prospectus, mark each perk keep / change / drop. Fill the Deliverables tab.
3. ⏳ 5 min: decide the logo and payment-gating rule from the agreement.
4. ⏳ 10 min: paste perks into the four emails and send.
5. ⏳ 10 min: put up the logos you already hold the files for. Request the rest.