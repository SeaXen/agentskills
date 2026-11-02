# Partner workshop enablement for Tessaract

## Verdict

⚠️ A recorded webinar, a deck, and a lab repo will get you partners who can *present* but not *deliver*. Your biggest risks are a solo consultant running a hands-on lab for 20-30 people and nobody checking quality before customers see it.

Keep your recorded webinar. Make it step 1 of 5, not the whole plan.

## 1. Fix the staffing model first

A hands-on lab for 20-30 people breaks with one person. Attendees get stuck at different steps, and the lead can't teach and debug at once.

- **Hands-on lab:** 1 lead plus 1 assistant. If a partner insists on solo, cap the group at 12-15.
- **Demo-led or lecture-style workshop:** 1 consultant can handle 20-30.
- **Make it a rule in the partner agreement,** not a suggestion.
- **Check each partner's bench.** Three partners with one consultant each means they can staff at most one workshop at a time.

## 2. Five-stage readiness path

| Stage | What happens | Gate to pass |
|---|---|---|
| 1. Learn | Recorded webinar, self-paced modules, product basics | Short knowledge quiz (80%+) |
| 2. Practice | Consultant completes the lab alone in a fresh sandbox, timed | Lab finished, issues logged |
| 3. Teach-back | Live 60-minute dry run to your SEs, who play difficult attendees | SE scores it against a rubric |
| 4. Shadow, then co-deliver | The partner watches 1 SE-led workshop, then leads 1 with an SE present | SE sign-off on a delivery scorecard |
| 5. Certified solo | Partner delivers independently | First 2 solo workshops are reviewed (recording or feedback survey) |

- **Certification expires.** Recertify yearly or on each major product release.
- **Cost to your SEs:** roughly 6-8 SE hours per consultant, plus 2 workshops of SE presence per partner. That is manageable for 3 partners but not for 15, so plan to train partner trainers later.

## 3. Turn the materials into a delivery kit

The deck and repo alone are not enough. Add:

- **Facilitator guide:** timings, talking points, and the questions attendees always ask, with answers.
- **Lab troubleshooting guide:** the top 10 failure points and how to fix each.
- **Pre-work and attendee prerequisites:** accounts, tools, and network access, sent a week ahead.
- **Delivery scorecard and attendee survey:** the same ones your SEs use, so quality is comparable.
- **Escalation path:** a Slack or Teams channel plus a named SE contact with a response-time promise.
- **Localization:** German and Brazilian Portuguese decks and lab instructions. Decide whether the product UI and lab text are translated or only the slides. Partners will otherwise translate on their own, and versions will drift.

## 4. Make the lab partner-proof

This is the most common point of failure.

- **Hosted, ephemeral sandboxes per attendee,** not "clone the repo and set it up locally." Local setups fail on corporate laptops and proxies, and every failure costs the facilitator 10 minutes.
- **Synthetic data only.** Partners and attendees must never touch real customer traffic or credentials in the lab.
- **Cold-run test:** have someone outside the SE team complete the lab from the written instructions only, and fix everything they hit.
- **Version-pin the lab** to a product release, and keep a changelog so partners know what changed.
- **Check cost:** compute sandbox spend per attendee and decide who pays (you or the partner).

## 5. Commercial and legal terms

Settle these before enablement starts. They are where partnerships usually stall.

- **Who sells and invoices the workshop:** the partner (their service revenue) or you (partner as subcontractor)? This changes what you can control.
- **Customer relationship and leads:** who owns attendee data, and do leads from partner workshops route to you? Get a GDPR-compliant data-sharing clause for Germany and LGPD compliance for Brazil.
- **Brand and content licensing:** partners may use and adapt your materials only within the agreement, and may not rebrand them.
- **Quality clause:** you can suspend a partner's delivery rights if scores fall below a threshold.
- **Conflict check:** does any partner also resell a competing API security product? If yes, they may steer workshops toward it.
- **Pricing:** decide whether customers pay for workshops, or whether partners deliver them free as pre-sales (in which case you may need to fund them through marketing development funds).

## 6. Start with a pilot, not all three at once

- **Pilot:** 1 partner in Germany and 1 in Brazil. Choose the ones with the strongest technical bench and a real customer already waiting.
- **Run 2-3 workshops each,** then review the scorecards and fix the kit.
- **Onboard the third partner** after the kit has been fixed once.
- **Why:** four SEs cannot shadow three partners at once without hurting their own customer work.

## 7. Timeline (about 10 weeks)

1. **Weeks 1-2:** Settle staffing, commercial terms, and sandbox plan. Choose pilot partners.
2. **Weeks 2-5:** Build the facilitator guide, sandbox lab, scorecard, and localization. Cold-run test.
3. **Weeks 4-6:** Pilot partners complete stages 1-3.
4. **Weeks 6-9:** Stage 4 shadow and co-delivery.
5. **Week 10:** Review scorecards, fix the kit, certify, then onboard partner 3.

## 8. Metrics to track

- Partner-delivered workshop count, and attendee satisfaction versus SE-led workshops
- Lab completion rate and the number of facilitator interventions per session
- Time an SE spends per partner workshop (this should fall over time)
- Follow-on pipeline from partner workshops
- Partner certification pass rate and time to certify

## Questions that would change this plan

1. Are these workshops free pre-sales or paid services?
2. Do the partners have any competing product alliances?
3. Is the lab hosted today, or is it a repo people run locally?
4. Do the partners' consultants already know API security deeply, or are they generalists?
5. Is 2 SE days per partner for the pilot realistic given your current load?

Do you want me to draft the facilitator guide outline or the delivery scorecard next?