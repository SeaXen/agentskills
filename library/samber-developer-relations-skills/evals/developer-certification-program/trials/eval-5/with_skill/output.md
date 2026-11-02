# Tessara Payments integrator badge: pricing and success (charter sections 7 and 9)

**Verdict for the plan as given:** keep 149, but change the voucher plan and the success headline. The 149 is defensible only because of the arithmetic below, not because the competitor charges 150. The 2,000-voucher plan costs more than it earns and cannot be shown to deliver the board's 1,000-holder number.

**Gate (one line):** the outside consumer is merchants who browse the directory and shortlist an integrator. That caps the credential at a **skill badge**, which matches what you are building. A hands-on badge fits.

## Section 7: Price, vouchers, verification

### Break-even fee (your costs, not the competitor's)

| Line | Calculation | Result | Source |
|---|---|---|---|
| Yearly fixed | 38,000 build ÷ 2-year version life | 19,000 | your figures |
| Yearly operating | alignment and appeals | 9,000 | your figure |
| Fixed plus operating | 19,000 + 9,000 | 28,000 | |
| Spread over attempts | 28,000 ÷ 500 | 56 | |
| Per-sitting cost | hosting and payment | 22 | your figure |
| **Break-even fee per attempt** | 56 + 22 | **78** | |

- The fee is charged per attempt, so failed attempts pay their own sitting cost.
- Cost per holder is for reporting only: 39,000 ÷ 350 passes ≈ **111** (39,000 = 28,000 + 22 × 500 sittings). Do not use it as the fee, because it recovers failed attempts twice.
- 149 clears the 78 floor, leaving about 71 per paid attempt (about 35,500 a year at 500 attempts).
- "149 because the competitor charges 150" is a borrowed benchmark, so I did not use it. I did not test 149 against what freelancers will pay.
- The skill's test for a freelancer fee is that one engagement repays it. You have not given me a typical engagement value, so that is still unchecked (see open items).

### Vouchers are a cost line, not free

Each redeemed voucher costs 22 in hosting and brings in no revenue. Break-even fee with vouchers = (28,000 + 22 × (paid attempts + redeemed vouchers)) ÷ paid attempts.

| Paid attempts/yr | 0 vouchers redeemed | 500 redeemed | 2,000 redeemed |
|---|---|---|---|
| 500 (plan) | 78 | 100 | **166** |
| 350 | 102 | 133 | **228** |
| 250 | 134 | **178** | **310** |

- If all 2,000 vouchers are redeemed, the floor is 166, which is above 149. You lose about 8,500 a year on top of an already-sunk build.
- 149 breaks even only up to about 1,600 redeemed vouchers, assuming exactly 500 paid attempts.
- Attempt volume is the bigger risk. With 500 vouchers redeemed, 149 holds only while paid attempts stay at or above about 307 a year.
- The 500 attempts a year is your estimate. Nothing in the inputs supports it yet, so treat it as self-set.

**Voucher rules:**
- Cap redeemable vouchers at **500 this year** (self-set). That is about 11,000 of hosting, a budget line the program owner approves explicitly.
- Release vouchers in tranches of 100 to 150, so the second tranche waits on the first one's redemption and pass data.
- Every voucher is single-use, non-transferable, expires in 60 days, and is tracked by campaign.
- Cap compute and lifetime per voucher tenant, and require a verified account. Free sittings attract people who want free compute.
- Never report voucher sittings as organic demand.

**Other pricing rules:**
- Offer seat bundles for integrator firms.
- Publish the prep path and a free practice quiz. Freelancers pay from their own pocket and lose billable days studying.
- Review the fee after the first 100 paid attempts. The floor depends on real attempt volume.

### Verification and revocation
- Issue a signed Open Badges 3.0 credential with a status entry. Revocation updates that status, so wallet copies stop verifying too.
- Verify by credential ID or a holder-shared link.
- The "find a certified integrator" directory is **opt-in per holder**. Show name, firm, badge, region, languages and contact.
- On revocation, show "not valid" with no reason. Publish a candidate agreement with an appeals path and a named decision-maker.

## Section 9: Success measurement, go/no-go, kill rule

### The 1,000-certified target
- **It fails as a headline.** A holder count is a health signal, not an outside consumer's action. Free vouchers can inflate it without any merchant caring.
- **It is also unreachable on your own numbers.** Your plan gives 350 passes a year, so 1,000 organic holders takes about 3 years.
  - If the badge is live now, only about 10 weeks remain to December.
  - At the plan's pass rate that is roughly 70 organic passes by December (self-set arithmetic).
  - The other ~930 would have to come from vouchers.
  - At your 70% pass rate (350 ÷ 500), that needs about **1,330 redeemed vouchers**, about 29,000 in hosting. I assume the voucher cohort passes at the same rate, and it probably passes lower, which pushes both figures up.
- **Dilution risk.** If a thousand holders appear in the directory in ten weeks, mostly from meetup giveaways, merchants lose the signal that made the badge worth browsing.
- **Ask for the board.** Ask the board to re-sign the headline to the outcome metric below. If the board keeps 1,000, report it as a labelled health line: "N holders, M paid, K voucher".
- **Live count.** Put a live verified holder count on the verification page. It shows the number without making it the goal.

### Outcome metric (merchant side)
- **Primary:** merchant contact requests per listed integrator, for badge holders versus non-holders.
- **Secondary:** engagements integrators won citing the badge (a short question on the holder renewal and profile flow).
- **Baseline:** start logging directory contact requests per listing now, before launch. Without a pre-launch baseline you cannot show lift. Allow 4 to 6 weeks (self-set).

### Health signals
- Pass rate per task (a sudden rise suggests a leak).
- Paid versus voucher share of sittings, and pass rate for each.
- Voucher redemption rate.
- Re-alignment time per Tessara Payments release.
- Appeals, revocations and checker failures.
- Holder count, labelled.

### Go/no-go
- The December date is a dated readiness check about 4 weeks before launch.
- Readiness means pilot pass data in hand, all checkers green, and issuing and verification working.
- If it fails, the fallback is a completion badge at launch and the assessed badge next quarter.

### Kill rule (all thresholds are self-set; no external source)
- **Outcome:** no lift in contact requests for holders versus non-holders within 18 months of launch.
- **Maintenance:** re-alignment misses its window on 2 consecutive Tessara Payments releases.
- **Cost:** paid attempts stay below 300 a year for 2 consecutive quarters while the fee is at 149.

## Where each number came from
- **Your figures:** 38,000, 2 years, 9,000, 22, 500 attempts, 350 passes, 2,000 vouchers, 1,000 target, the board sign-off and the 150 competitor price.
- **Derived from yours:** 19,000, 28,000, 56, 78, the 70% pass rate, about 111 per holder, and the scenario table.
- **Self-set by me, to confirm:** the 500-voucher cap, the 60-day expiry, the 100-attempt review, the baseline window and the kill thresholds.
- **Unverified assumptions:** the 10 weeks left to December, which assumes the badge is live now, and a voucher cohort that passes at 70%.
- I did not read the competitor's price page, so 150 is unverified.

## Open items (questions for you)
1. Must the program break even, or is it a cost center? This changes whether the voucher cost is acceptable. I assumed break-even.
2. What does a typical integrator engagement earn? That decides whether 149 is one engagement's worth.
3. Is the badge already live, or does it launch before December?
4. Can you log merchant contact requests per directory listing today?
5. Will the board accept an outcome metric in place of the 1,000-holder number?