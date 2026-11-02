# DevRel budget-defense case: response to the proposed 40% cut

**Draft for the CFO. Plan lock: 2026-11-09. Program cost: $540k a year, salaries included. 40% = $216k.**

## Assumptions and open inputs (read first)

1. You gave me no metric framework or results numbers, so Section 1 is a table to fill in, not a result. I invented nothing. Every `[ ]` is a figure only you can supply.
2. Nothing here says support "would drown". I can't write that claim without support's confirmation, so it appears only as a pending request (Section 4). It is also the strongest lever you have, so the request matters.
3. I dropped the industry-survey comparison on purpose (see "Why I didn't use the benchmark" below).
4. I assumed the paid community platform ($24k) hosts the forum that support relies on, and that the community manager runs that forum. If that's wrong, the dependency flag in Section 2 goes away.
5. I don't have contract terms for the sponsorships or the video producer. Reversibility and savings timing are marked `[confirm]` where I don't know them.
6. I assumed the CFO's alternative to compare against is paid acquisition or support headcount. Name the real one.

## Headline (to finish once Section 1 has numbers)

> DevRel moved **[the CFO's goal, in their words: e.g. self-serve activation, support load]** from **[X]** to **[Y]**. A 40% cut cannot be reached from the lines that hold that result up without removing the community manager role.
> **Decision asked:** choose one of three cut tiers, by **2026-11-09**.

## 1. Results table (fill from your agreed framework)

Use the goal-ledger spine. The CFO builds the plan from company goals, and a CFO may prefer the bet-portfolio spine, so pick one and don't mix them. Use framework metrics only. Put the claim label in the same cell as each number.

| Company goal the CFO owns | Metric (from framework) | Last 4 quarters | Status | Label |
|---|---|---|---|---|
| [e.g. self-serve revenue] | [e.g. developers reaching first success per month] | [ ] → [ ] | [from threshold] | influenced (touched cohort) |
| [e.g. support cost flat] | [e.g. tickets per 100 new signups] | [ ] → [ ] | [ ] | measured |
| [e.g. enterprise pipeline] | [pipeline influenced, written rule] | [ ] | [ ] | influenced, shared with sales |

Rules for filling it in:
- Use co-movement wording ("rose while the quickstart was rewritten"). Don't write "drove" or "cut" without a holdout or a pre/post read with a recorded pre-period.
- Don't write "sourced", "generated", or an ROI multiple.
- Show raw counts on both sides for anything under about 30 events.
- If a metric is still baselining, give it no status color.

## 2. Tiered cut scenarios (cumulative prefixes of your ranked list)

| Tier | Lines cut | Cost | Share of $540k | Gap to the 40% ask ($216k) | What stops | Metric expected to drop | Reversible | Savings land |
|---|---|---|---|---|---|---|---|---|
| A | 1–2 | $105k | 19.4% | $111k short | two tier-2 sponsorships, swag, travel | DevRel-qualified leads from events `[your lead-source data]` | Yes, at the next sponsorship cycle | When the contracts would have been signed `[confirm]` |
| B | 1–4 | $189k | 35.0% | $27k short | the above, plus the community platform and the video producer | tutorial video output, forum availability. First-success effect unknown. | Video: after the notice period `[confirm]`. Platform: migration and re-seeding cost `[confirm]`. | At contract end `[confirm]` |
| Full list | 1–5 | $299k | 55.4% | $83k over | the above, plus the community manager role | forum first-response time, tickets per 100 signups (likely up) | No: re-hiring and re-ramp take a quarter or more | From the exit date, minus severance |

**What the 40% ask really is.**
- The non-headcount lines total $189k, which is 35%.
- The remaining $27k is not on the cut list.
- The only listed way past 35% is removing the community manager role, which lands at 55%, not 40%.
- So the funder's real decision is whether to remove that role. Don't let the debate stay at "40% vs less".
- Any tier at exactly $216k needs the list re-ranked by `devrel-budget-allocation`. I won't invent one.

**Dependency flag on line 3.**
- The platform (rank 3) and the community manager (rank 5) probably share one dependency: the forum.
- Tier B cuts the platform while keeping the role, which could silently break the forum.
- Either bundle lines 3 and 5 into one step, or send the list back to `devrel-budget-allocation` to re-rank.
- Until then, **Tier A is the only tier I can call free of forum risk.**

**Recommendation: Tier A.** It cuts the lines with the weakest return and keeps every line that holds up a row of the results table. This holds only if Section 1 shows the cut lines are not what moved those rows. Check that before you send.

## 3. Cost per outcome (for a CFO reader)

Fill in:
- Program cost: **$540k (salaries in)**.
- Cost per `[outcome the attribution rule credits to DevRel]`: `$540k / [count]` = **$[ ]**. Label it influenced or measured. If you divide by all outcomes, label it "all outcomes, not attributed".
- Compare it only with the same outcome unit on the same cost basis: paid acquisition per first success, or the cost of a support hire. If the alternative excludes salaries and you include them, say so beside the number.
- Support cost avoided: `[tickets avoided] × [cost per ticket agreed with finance]` = $[ ]. Label it modeled, and show it as avoided cost, never revenue.
- If you can't get finance to agree on the unit value by 2026-11-06, drop every modeled figure and report cost per measured outcome only.

## 4. Dependency inventory (only what the owner confirms)

| Team | What it uses from DevRel | If it stops | Status |
|---|---|---|---|
| Support | forum answers `[share of tickets deflected, if they track it]` | `[support's estimate, e.g. extra tickets a year]` | **Confirmation requested from support lead, due 2026-11-04** |
| Sales / product | `[workshops, docs, feedback loop?]` | `[their estimate]` | `[request, or leave out]` |

**Without written confirmation, nothing goes in the consequence column.** "Support would drown" is your belief, not evidence, and a CFO will ask to see the ticket data. One confirmed estimate from support's own lead is worth more than the whole page.

Message to send to the support lead today:

> We're facing a proposed budget cut that could remove the community manager role and the forum platform. Can you send me by Nov 4: (1) how many tickets a month the forum answers before they reach support, if you track that, and (2) your own estimate of the extra tickets a year if the forum went unmoderated or offline? I'll quote it as your estimate and credit you.

## 5. What did not work

You haven't told me this period's misses. One row for every metric that missed its threshold (what happened, likely cause, what changes, next read date), plus every metric dropped since the last report with its kill-rule reason. If nothing missed, write "No metric missed its threshold this period." Don't leave the section out. A clean page reads as a filtered page.

## 6. Decision asked

Choose one: **Tier A (19%, $105k)**, **Tier B (35%, $189k)**, or **remove the community manager role (55%, $299k)**. A cut of exactly 40% isn't supported by the list.

**Recommendation: Tier A.** It protects the lines behind the results table, and the remaining event spend gets a Q2 read against its threshold, with a further cut if it misses. **Needed by 2026-11-09.**

## Why I didn't use the benchmark

Published DevRel budget figures come from small samples on mixed cost bases (salaries in or out, loaded or media-only). Other companies' numbers don't transfer, and a CFO will probe the sample the moment you cite one. If the CFO raises benchmarks themselves, answer with the program's own trailing quarters and name the benchmark's sample problem. I also have no verified survey figure to cite, and I won't write one from memory.

## Your next steps, in order (about 3 hours of your own time, plus waiting on others)

1. **Today:** send the message to the support lead (Section 4).
2. **Today:** paste your metric framework or current numbers, so I can complete Section 1 and the headline.
3. **By 2026-11-04:** get the contract notice periods for lines 1, 3 and 4, to fill in the `[confirm]` cells.
4. **By 2026-11-06:** ask finance to agree one unit value, such as cost per ticket. If they can't, drop the modeled figures.
5. **2026-11-09:** plan lock.

I dropped causal evidence (a holdout or pre/post test) because 10 days is too short to run one. If the next review is a quarter or more away, record a pre-period now so you can run one then.