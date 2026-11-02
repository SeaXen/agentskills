# Northbound CFP rating sheet

**Do this first:** decide how you'll anonymise before you build the sheet. Your plan has two weak spots: "overall quality" is too vague, and the blind review needs a process.

## 1. Problems with the current plan

- **"Overall quality" means something different to each rater.** One person scores writing polish, another topic fit, another novelty. Averaging six different meanings gives noise. Split it into 3 named criteria.
- **1-to-5 averages clump.** Most scores land on 3 or 4. Raters also differ in generosity, so a 3.9 from a harsh rater is worth more than a 3.9 from a lenient one. With 190 proposals and a cutoff at rank 22, you'll have many ties around 3.8 to 4.0.
- **"Without names" needs a mechanism.** Someone has to strip the names, and abstracts leak identity through company names, product names, "at my last job at X", and bios.
- **Scores shared early anchor everyone.** Raters must score privately and independently.
- **The workload is large.** 190 proposals × 6 raters is 1,140 ratings. At 5 minutes each that is about 16 hours per person, which is too much for 3 weeks of side time.

## 2. The sheet: one tab per rater

Each rater gets their own copy, filled out independently. A script merges the copies later. Rows are proposals in a random order, with the same order for everyone.

| Col | Field | Filled by | Notes |
|---|---|---|---|
| A | Proposal ID | script | Random ID such as `P-0147`, not submission order or timestamp |
| B | Title | script | Scrubbed of names and employers |
| C | Abstract (+ outline) | script | Scrubbed. Includes the "what attendees learn" field if the CFP had one |
| D | Topic tag | script | From the CFP form field, for balancing later |
| E | **COI / can identify author?** | rater | `No` / `Suspect` / `Know`. If `Know`, leave F to I blank. A blank is not a zero. |
| F | **Fit** 1-5 | rater | Single-track infra audience, so is this useful to the room? |
| G | **Substance** 1-5 | rater | Concrete experience, depth, evidence, not a product pitch |
| H | **Clarity** 1-5 | rater | Can I tell what the attendee takes away? Judge the idea, not the English. |
| I | **Stage verdict** Y / M / N | rater | "Would I put this on our stage?" |
| J | Comment | rater | Required for any `Y` or `N` or any 1 or 5. One line. |
| K | Flag | rater | Optional: `vendor pitch`, `duplicate topic`, `too broad`, `scope unrealistic for slot` |

Add an **anchor legend** at the top of the sheet. Without it, a 3 means something different to each person.

- **5:** I'd be upset to lose it.
- **4:** strong, and I'd want it on the programme.
- **3:** fine, and I'd take it if there's space.
- **2:** has a real problem.
- **1:** no.

Add one calibration rule: "If more than about 30% of your scores are 4 or 5, you aren't discriminating. The real accept rate is 22 of 190, about 12%."

## 3. Cut the workload with two passes

1. **Pass 1 (week 1 to 2):** all six raters read all 190, but fill only columns E, I and a quick F. This takes about 1 to 2 minutes each, or 3 to 6 hours per person.
2. **Pass 2 (week 2 to 3):** a script picks the roughly 50 to 60 proposals nearest the cutoff plus any with high disagreement. All six then fill F, G, H and J on those. This takes about 3 to 4 hours per person.
3. **Call (week 3):** discuss only the band near the cutoff.

If you prefer one pass, drop column I and keep F to H. Expect about 10 hours per person.

## 4. Merge and aggregate (script, not manual)

- **Per-rater normalisation:** convert each rater's scores to z-scores so generous and harsh raters count equally. Use rank-within-rater as a fallback.
- **Combine criteria:** `score = mean(Fit, Substance, Clarity)`. Weight Fit and Substance higher if you want. Decide the weights now, before anyone sees results.
- **Report per proposal:** mean, median, SD, number of raters, and the share of `Y` verdicts.
- **Skip blanks** from COI recusals. Don't treat them as 0. Require at least 4 raters per proposal.
- **Result tabs:**
  - Ranked list.
  - "Auto-in": top about 10.
  - "Auto-out": bottom about 100.
  - "Discuss": the band near rank 22 plus SD ≥ 1.5.

## 5. Keeping the anonymity promise

1. Have a script strip names, bios, emails and links, not a human. Nobody opens the raw export.
2. Grep abstracts for company and product names. Redact these with a placeholder such as `[company]`.
3. Run a duplicate-speaker and same-company check by script, so no human sees names. It flags "3 proposals from one speaker" or "5 from one employer" for the call.
4. Keep names hidden through the call and the vote. Balance the programme only on the topic tag, level and format.
5. Reveal names only after the 22 are locked.
6. If you want to use names to fix problems after selection, such as speaker diversity, say so to submitters in advance. You told them reviews would be nameless, and a later reveal that changes outcomes would break that.

## 6. Call agenda (120 minutes)

| Min | Item |
|---|---|
| 0–10 | Show the ranked list and the rules for the session. |
| 10–20 | Lock the auto-ins in one vote. |
| 20–95 | Discuss the roughly 35 band proposals at about 2 minutes each. Start with those with the highest disagreement. |
| 95–110 | Check programme balance by topic and level, and apply the duplicate and same-company flags. |
| 110–120 | Final vote and waitlist of 4 to 6. |

Scores are private until the call starts. Nobody discusses a proposal before then.

## 7. Decisions for you

- Two passes or one?
- Criterion weights?
- Minimum raters per proposal, and COI rule: recuse on `Know` only, or on `Suspect` too?
- Tool: Google Sheets with one copy per rater plus a merge script, or a form tool such as Airtable. Sheets is the simplest.