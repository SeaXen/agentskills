**Next action (10 min):** Send legal one email asking for a gift and travel ruling on the 4 federal and 2 bank guests. That sign-off has the longest lead time and blocks everything else. I'm not a lawyer, so legal and compliance should confirm every rule below.

Timeline: 7 weeks to event, 3 weeks to registration open.

## Sign-off order

| # | Sign-off | Owner | Blocks | Due |
|---|---|---|---|---|
| 1 | Federal and bank VIP gift/travel ruling | Legal + compliance | VIP invites | End of week 1 |
| 2 | Data map and lawful basis for registration data | Privacy/DPO + legal | Form, terms, Salesforce | End of week 1 |
| 3 | VIP budget and T&E rules for non-employees | Finance + exec sponsor | VIP invites, flight booking | End of week 1 |
| 4 | Event terms package (see below) | Legal | Registration open | End of week 2 |
| 5 | Salesforce integration spec and security review | RevOps + security | Build | End of week 2 |
| 6 | AE rules of engagement | Sales leader + legal | Go-live of AE access | Week 3 |
| 7 | Test in sandbox, then go-live approval | RevOps + privacy | Live feed | Registration open |

## 1. The 6 regulated VIPs (rules differ from the other 29)

**Federal (4 guests)**
- Federal employees face strict limits on gifts from outside sources, with a small value cap. Free flights and two hotel nights almost certainly exceed it.
- Exceptions exist: travel paid by a non-federal source for official duty, or free admission to a widely attended event. Both need the agency's ethics office to approve, usually in writing and in advance.
- Each guest must request that approval through their own agency. You can't decide it for them. Agency reviews can take weeks.
- Ask legal: does Tessro hold, bid on, or expect any contract with these agencies? If yes, treat the gratuity and procurement-integrity risk as severe. Default to no paid travel.
- Likely fallback: they attend free where approved, and their agency pays travel and lodging. Budget for either outcome.
- No swag, dinners, or extras for them until ethics clears each item.

**Bank (2 guests)**
- Banks have strict gift and entertainment policies. Federal bank-bribery law also applies to bank officers who accept things of value tied to business.
- Get the guest's own compliance sign-off in writing before booking anything.
- Ask whether the bank is in a live procurement or renewal with Tessro. If so, expect refusal or a cap.

**The other 29 guests**
- Customer employers often have gift policies too. Send every VIP an invitation that tells them to check with their employer first.
- If any guest is a foreign official or works for a state-owned entity, or travels internationally, legal needs to check anti-corruption law.
- Ask tax whether paid travel for non-employees has reporting or deductibility limits.

## 2. Registration to Salesforce

Decisions before RevOps builds anything:

1. **Consent and purpose.** Registration must disclose that data goes to sales follow-up. If you have EU, UK, or Canadian attendees, you may need opt-in consent. Legal decides.
2. **Exclude by default.** Don't sync these to Salesforce:
   - dietary, accessibility, and medical fields (special-category data)
   - passport, date of birth, and travel documents
   - the 6 regulated VIPs. Keep them off the AE worklist entirely. Soliciting a federal employee or a bank buyer at your own event is the exact risk in section 1.
3. **Field mapping.** Sync only name, company, title, email, and ticket type. Add an `Event Source` tag and a consent flag.
4. **Processors.** Confirm a data processing agreement with the registration platform and with any sync tool in between.
5. **Opt-out path.** Attendees who decline sales contact must be suppressed in Salesforce. Test this.
6. **Security review.** Who has access, where the data sits, and how long you keep it.

Event-marketing rule of thumb: an AE working a registration list during the event gets worse results than AEs who set meetings beforehand, so give them a target list built from consented attendees.

## 3. Terms package (legal asked; none exist)

Legal drafts one package. It must be live before registration opens in 3 weeks:

1. **Registration terms.** Eligibility, cancellation and refund, transfer, liability limits, right to remove attendees.
2. **Privacy notice for the event.** What you collect, why, who sees it (including sales), retention, opt-out.
3. **Code of conduct.** Reporting channel and consequences.
4. **Photo, video, and recording notice.** You record sessions, so get consent or give notice at the door.
5. **VIP travel terms.** Non-transferable, cancellation rules, no purchase obligation, attendee's own compliance responsibility, and a representation that they may lawfully accept.
6. **Sponsor or partner data-sharing terms.** Only if you share lists. Default: don't.

Also ask:
- Does event liability or travel insurance cover this?
- Does procurement need a vetted travel agency?

## Critical path

1. **Week 1:** items 1, 2, and 3 start in parallel. Don't invite federal or bank guests.
2. **Week 2:** terms draft and RevOps spec land.
3. **Week 3:** terms live, Salesforce tested in sandbox, registration opens.
4. **Weeks 4–7:** approved VIPs book travel. Ethics responses may still be arriving, so keep the federal slots flexible.

**Fastest risk to cut:** if legal can't clear the 6 regulated guests in 2 weeks, invite them as free-registration-only, travel at their own agency's or bank's expense.

**Next:** Draft the email to legal covering the 6 guests and the registration-to-Salesforce plan. Tell me whether Tessro has live contracts or bids with those agencies and that bank, and I'll write it.