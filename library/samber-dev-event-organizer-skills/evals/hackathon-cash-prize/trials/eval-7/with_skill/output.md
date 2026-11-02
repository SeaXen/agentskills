# Torvik Open: prize structure draft

I couldn't run the one-question-at-a-time interview, so this draft covers every branch and flags the answers that decide each one. Nothing here is ready to publish. Publishing is the point of no return, so validate it section by section first.

## Bottom line

1. **Don't size a flagship pool yet.** Finance has no Prizes line, and the skill deletes the flagship rung when that line isn't set. A headline pool sized against no ceiling commits money nobody has budgeted. Your intent (attention before the event) meets one of the two conditions for a flagship pool. The other, a Prizes line big enough to hold it, is missing.
2. **Tell finance what the structure needs, not a total.** I'm not proposing a dollar amount. Any figure from me would be invented, and this skill states no currency amounts. What finance needs from you is in section 1.
3. **You can still get a headline.** Build it from signed sponsor commitments and announce it only when the money has landed. Announcing before then is the failure mode where the organizer owns the gap personally.
4. **The prize may not be what moves submissions from 40 to "way more".** That link is an untested assumption. Treat the pitch (section 7) as one lever among several.

## 1. What to tell your finance person

Ask for a ceiling, not a target. The Prizes line is a fixed input I size inside; I don't raise it.

1. **Organizer baseline.**
   - This is the part Torvik Open pays itself, and it is a modest pool sized to whatever finance can carry.
   - It has no relationship to the headline figure.
2. **Sponsor-funded part.**
   - Nothing from the organizer's own line.
   - It grows only with signed commitments, and `event-sponsor-pricing` sells the add-on that funds it.
3. **Cash-timing question.**
   - If sponsors fund prizes, ask when that money clears and where it is held.
   - A sponsorship that clears after the event means the organizer fronts the prize personally.
4. **Procurement lead time.**
   - If the prizes include gear, ask whether she can commit early, because backorders are real.
5. **Counsel or fiscal-host budget.**
   - Reserve a small line for a review of the payout before announcement.
   - It becomes mandatory if any gate in section 6 is live.

Her answer to item 1 decides whether a flagship pool is even possible. Until she sets it, the pool is "modest, sized to the line" plus "sponsor-funded, scaled to signatures".

## 2. Medium (decide this before the size)

My default is **gear**, with credits for sponsor tracks.

| Rung | Verdict for Torvik Open |
|---|---|
| Gear | Default. High perceived value and no payment rail. Needs early ordering, and a unit-count rule (section 4). |
| Credits and vouchers | Good for sponsor tracks, which are near-free for the sponsor. Publish expiry, redemption region and account requirement. |
| Opportunity | Include only with a written commitment from an external party (hiring team, conference, investor). Without one, delete it. Its legal treatment is an open question. |
| Recognition only | Right if you have no legal entity and no fiscal host, or if the aim is to reward winners rather than buy attention. |
| **Cash** | **Deleted** if any winner could be a minor, any winner could be outside your country, or you have no entity or fiscal host. The name "Open" suggests cross-border, so assume cash is deleted until you tell me otherwise. |

Cash is not the recommended answer here. MLH, whose guide frames this decision around behaviour, states: "While cash prizes are easy for events, we do not recommend them. The perceived value of a cash prize is much lower than traditional prizes." That is one organization's stated position, not measured outcomes. A "headline pool" in cash is therefore the hardest version to deliver.

The reasons cash is dearest to hand over are documented. Devpost requires a cash winner to submit tax-identification paperwork before funds release, with separate paperwork for international individuals and for organizations. Credits and vouchers are treated like cash for reporting purposes, so they sit next to cash on the compliance axis.

## 3. Pool

| Rung | Status |
|---|---|
| Flagship | **Deleted for now** (Prizes line unset). Re-promote only if finance sets a line large enough to hold it and your stated intent stays attention-before-event. |
| Sponsor-funded | **Default if any sponsor funds a prize.** Scales with signatures and draws nothing from the Prizes line. |
| Modest, sized to the line | **Default if no sponsor funds a prize.** A real ceiling makes it safe. |
| No monetary pool | Legitimate, but it forgoes the sponsor inventory a funded prize creates. |

Keep the two parts separate in the budget, because they have different ceilings and different owners.

Two cautions on counting toward a headline:
- **Do not value in-kind sponsor prizes at retail.** `event-sponsor-pricing` values in-kind at the budget line it displaces. A prize may displace a spend you would never have made, so check that the method transfers before you add credits to a "worth" number.
- **Do not publish a total before the money is signed.**

### Does a bigger pool get you more submissions?

Put this to your team as an assumption, because the evidence cuts both ways.

- **Against.**
  - Devpost's organizer guidance says a very low prize can suppress participation.
  - It also says a modest, well-distributed pool performs as well as a much larger one in its own experience, and that more money doesn't guarantee stronger submissions.
  - Engagement, technical support, promotion and simple requirements carry equal weight.
- **For.**
  - ETHGlobal Bangkok drew 713 submissions from roughly 1,950 hackers in the edition with its largest-ever pool.
  - HackYeah pairs nearly 3,000 attendees and over 300 submissions with an undisclosed pool.
  - Neither controls for year-over-year growth or compares against a smaller pool. Read them as texture, not proof.
- **Counterweight.** MLH, PennApps, Papers We Love and NASA Space Apps lead with learning, building and sharing, not prize size. A headline pool competes on ground credible events vacate, and it attracts people who came for the money.

## 4. Split

My default is a **graduated podium** with sponsor tracks added where sponsors fund them.

- **Winner take most:** deleted as soon as any sponsor funds a track, because that sponsor bought a named award and this shape has nowhere to put it.
- **Track only:** correct only if the published brief has tracks and no overall category. Check what last edition published. If an overall category exists, this rung contradicts it.
- **Flat across many tracks:** promoted only if several sponsor tracks are already published and the medium is non-cash, so the repeated per-winner check is a handover rather than a payment.
- **Graduated podium:** one extra award over the cheapest rung, and it gives second and third place something real to finish for. For reference, PennApps split its top-three pool 50/30/20.

Devpost's guidance also backs "many chances to win": participants want a reasonable shot at placing before they commit the hours. This matters for your goal, and it is a split-shape lever as well as a pool lever.

If layered, an award structure can be: a ranked podium, an audience-choice award, one horizontal prize per sponsor technology, and a small separate prize for any non-judged activity. Each layer is one more eligibility and payout check.

**Unit rule for gear or credits** (these are counted per person, and cash isn't):
- Plan in whole units against the team-size cap in the brief. `hackathon-brief-design` owns that cap.
- State the fate of leftover units before the event: returned, raffled, or held. MLH's practice is to save receipts so a prize can be returned if a winning team is smaller than the cap.
- Publish whether the award follows the submitted roster or the people on stage.

## 5. Eligibility to receive (draft for the brief)

This is the narrow question of who may legally receive an award once a rules-eligible team has won. Eligibility to compete lives in `hackathon-brief-design`, so hand this text to it rather than publishing it yourself. The two skills hadn't drawn this split before, so expect the brief owner to look for it elsewhere.

> Prizes are awarded to the team named in the submission. Organizers, volunteers, mentors and judges may build projects and demo them, and are not eligible to receive a prize. [DECIDE: Sponsor employees may / may not receive a prize funded by their own employer.] [DECIDE, if a minor can win: A winner under the age of majority in the organizer's country will be asked to have a parent or guardian receive the prize on their behalf.] Where a prize cannot be delivered to a winner's location, we will agree an alternative of comparable value with that winner. Prizes are awarded per team member up to the team-size limit stated above; unclaimed units are [DECIDE: returned / raffled / held]. To receive a prize you will be asked to confirm your identity and any information we are required to collect; we will tell you exactly what that is when you claim. [DECIDE: if you adopt a continuing condition, such as the repo staying public, state the date the award becomes final and what happens if the condition fails.]

Don't publish with a bracket still in it. A leftover bracket advertises that the question was seen and skipped.

Two points to settle before publication:
- Whether organizers, volunteers, mentors and judges may build is a separate permission from whether they may win. The paragraph keeps them apart.
- A sponsor's employee winning that sponsor's own track is a live conflict, different from the judging conflict. Answer it in the sponsorship agreement before the event.

## 6. Payout mechanic and exposure routing

**Default: standard-form payout.**
- One published eligibility paragraph and one claim step, written before the event while they're cheap.
- The claim step collects identity or status information appropriate to the medium, and it names the category rather than a document.

**Gates, which override efficiency.** A minor in the winner pool, a winner outside your country, or a sponsor employee eligible for their own sponsor's track each carry a legal obligation. If any is live, counsel or the fiscal host reviews the payout before any prize is announced, whatever rung looks cheapest. Informal handover is deleted if the prize is cash or a cash equivalent, or if any winner could be a minor or outside your country.

**Routing.** I don't answer any of these, and every specific threshold or form is jurisdiction-specific and changes.

| Exposure category | Live? | Route to |
|---|---|---|
| Contest-law classification (skill-based contest or game of chance) | Always check; a random draw as tie-break is the main trigger | Counsel |
| Payer-side tax reporting and withholding | Live if the prize has monetary value (cash, vouchers) | Fiscal host or counsel |
| Cross-border payment | Likely live for an "Open" event | Your bank or platform for the rail; counsel for the rules |
| Minors receiving an award | Depends on your age rules in the brief | Fiscal host or counsel |
| Sponsor employees on their own track | Live once any track is sponsor-funded | The sponsorship agreement, then counsel |
| Organizers, volunteers, mentors, judges | Live | Answered by published practice (section 5) |

If you have no legal entity, the standard route is a fiscal host. MLH names Hack Club and Hack+ as hackathon-specific options. Ask any host who holds signing authority and how long their review takes, where funds sit and what fees apply, and how long between money arriving and being spendable.

## 7. How to pitch it

Pitch what you can prove, and don't pitch a number you can't yet pay.

1. **Lead with the reachable prize.** Many named awards that a team can realistically win do more for submissions than one distant headline. This is what Devpost's guidance supports.
2. **Add the other levers.** Devpost lists engagement, technical support, promotion and simple requirements as equal in weight, and these are cheap compared to prize money.
3. **If you want a headline, make it a signed sponsor total.** Publish "up to" figures only as commitments land, and never announce a sponsor prize before the sponsorship is signed. Describe a gear or credits headline by what it is, not by retail value.
4. **Publish the whole structure before submissions close.** A prize announced after teams chose what to build has already failed to motivate anything.
5. **Be careful with the press angle.** "Biggest pool" selects for money-motivated participants. A claim about the winners' prizes (what they get, how many teams) is easier to defend and attracts the participants you want.

## 8. Measurement (self-set, not an industry standard)

Don't borrow another event's pool or split as a target. For the 40-submission goal, decide with your team what "way more" means as a number. I won't set it for you.

**Pass gate before the brief is published: all six of these exist in writing with zero blanks.**
1. Medium.
2. Total pool, with the budget line it fits inside.
3. Split, with an award count.
4. Eligibility-to-receive text.
5. Payout mechanic, naming who hands over what.
6. Exposure categories, with the person each was routed to.

Signals to record afterwards, picking two or three and writing down the revision each would trigger:
- awards handed over versus announced
- winners who never claimed
- prize units left over against the team-size rule
- any eligibility question on the day that had no published answer

## 9. Answers I need before this can be finished

Reply with any of these and I'll re-rank the affected menu.

1. **Prizes line:** what has finance set, and when will she set it? (Decides whether a flagship pool stays deleted.)
2. **Last edition:** what tracks and places did it publish, and did any promise a prize?
3. **Sponsors:** which ones fund a prize, and is the funding cash, credits, hardware, or an opportunity they control?
4. **Winners:** could any be a minor, and could any be outside your country?
5. **Entity:** do you have a legal entity, or a fiscal host? (Decides who can sign a payout.)
6. **Staff:** may organizers, volunteers, mentors, judges or sponsor employees compete, and if so, may they win?
7. **Intent:** do you want the prize to buy attention before the event or reward winners after it?
8. **Effort ceiling:** how many organizer hours can go into prizes, and will anyone chase winners for paperwork?
9. **Deadline and cadence:** by when must the structure be published, and is this one edition or recurring?

I assumed answers where I couldn't ask: cash deleted for cross-border risk, sponsor-funded as the pool default, and graduated podium as the split default. If your answers differ, the defaults move.