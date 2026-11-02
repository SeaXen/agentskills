# Brackenmoor State of Edge Functions: raffle announcement and draw runbook

Source: `developer-survey-design` (SKILL.md, `privacy-and-consent.md`, `methodology-and-reporting.md`). I did not read `question-writing.md` or `worked-example.md`, because nothing here needs them. I assumed results will be published, so the claim rules are release blockers. Tell me if that is wrong.

## Read this first (2 min)

**Two changes to marketing's plan, one warning.**

1. **Do not add an email field to the survey.** Step 7 keeps identifiers out of the response table. Contact details for a prize go in a separate form with no join key to the answers.
2. **The raffle will not close the gap.** You are at 9 completes a day, which projects to about 250 by day 28. The target of 1,500 needs about 78 a day. The skill finds draw effects "small and inconsistent", and a public prize also attracts bots.
3. **A donation ranks above a raffle.** Per Step 8, it needs no contact data and no sweepstakes rules. The skill moves to a donation first when the date is near and completes are low, and both are true here. A raffle ranks below donation and badge, and your EU respondents push it to the bottom (Step 8 and the re-ranking block). I give you the raffle runbook because marketing wants it. If you can still choose, run the donation version at the end.

Re-ranking block (per the skill's format):

- `Answer 4 (18 days left, 90 of 1,500): donation promoted over prize draw, because the date is near and completes are too few.`
- `Answer 9 (French organisation, EU and US respondents): prize draw demoted to last of the free options, and Step 7 becomes a release blocker, because contact data, a separate store and per-jurisdiction rules apply.`
- `Answer 5 (not asked): calibration sample not assumed. If you can reach a random slice of Brackenmoor users through the dashboard or CLI, do that before the raffle; it is the only thing that makes rung 2 possible.`

**The target needs rewriting.** An opt-in survey has no margin of error, so 1,500 has no statistical basis. Set the minimum from the subgroups you must compare (Step 9) and write it down before you see the data.

## Before you post anything (ordered, about half a day)

1. **Get the data-protection contact and a lawyer to sign off** on the rules (below). The skill gives a checklist, not legal advice.
2. **Build a separate entry form** with fields for email, country and an "I am 18 or older" confirmation. Put the unticked consent boxes in it (see "Entry form"). It stores nothing from the survey.
3. **Update the privacy notice** on the survey's first page. Add this line to the template: "If you enter the prize draw, you give your email in a separate form. We keep a salted hash of your IP address until `<date>` to detect duplicate entries, then delete it."
4. **Switch on fraud checks** (Step 9 and the cleaning rules): one attention check, one trap option nobody can have used ("EdgeRunner 3.0"), and the salted IP hash in a separate column.
5. **Tag the new traffic.** Use `?src=twitter-raffle` and `?src=reddit-raffle`. Responses before the announcement and after it are different samples, so also record the announcement date. Add a sentence to the methodology: "A prize draw was announced on `<date>`; responses before and after are tagged and reported separately where they differ."
6. **Freeze the wording.** Do not touch questions mid-field. Only the thank-you page and the notice change.

## Official rules (publish on a page the announcement links to)

Draft for counsel to adjust:

> **Brackenmoor State of Edge Functions prize draw: official rules**
>
> **Organiser:** Brackenmoor, `<address>`, France. Contact: `<privacy address>`.
> **No purchase or payment is needed to enter.**
> **Prize:** one `<exact model and spec>` laptop, approximate retail value `<amount and currency>`. No cash alternative.
> **Who can enter:** anyone aged 18 or older, resident in the EU, EEA, UK or US, who completed the survey. `<Counsel: list any excluded states or countries>`. Brackenmoor employees and their immediate families are excluded.
> **How to enter:** complete the survey, then follow the link on the last page to the entry form. One entry per person. Answering the survey is not conditional on entering. Your answers do not affect the draw.
> **Entry period:** `<start>` to `<end, UTC>`.
> **The draw:** one winner, picked on `<date>` by the public method described below. Odds depend on the number of eligible entries.
> **Winner notice:** by email within 3 days of the draw. The winner has 14 days to confirm and give a delivery address. After that we pick the next draw result.
> **Data:** your email goes only into the entry form. We use it to run the draw and contact the winner. We delete all non-winners' emails within 30 days of the draw. We never join it to your survey answers. Full notice: `<link>`.
> **Taxes, duties and shipping:** `<Counsel and accountant: who pays customs, VAT and any US reporting on the prize>`.
> **Not sponsored by Twitter/X or Reddit.**
> **Governing law:** `<counsel>`. Rules filed with `<commissaire de justice / huissier, if counsel advises>`.

## Entry form (separate from the survey)

- Fields: email, country, "I am 18 or older", the rules link.
- Two unticked boxes:
  1. "I accept the official rules."
  2. "Brackenmoor may email me only about this prize."
- **Proof of completion, with no link to answers.** The thank-you page shows a completion code. It is a random nonce plus an HMAC signature made with a secret only you hold. The entry form accepts any validly signed code once. Nothing in the response table stores the code, so nobody can match a code to a set of answers.
- Store entries in a separate table that only one named person can read.

## Announcement copy

Replace the `<…>` placeholders. Put the median time in only after you measure it.

**Twitter/X**

```
The Brackenmoor State of Edge Functions survey is open until <end date>.

~<N> minutes. Anonymous answers. Results published openly in <month>.

To say thanks, we're drawing one <laptop model> for one respondent, picked by a public method anyone can verify. No purchase needed. Rules: <rules link>

Take the survey: <link ?src=twitter-raffle>
```

**Reddit** (self-post for the subreddit)

> **Title:** State of Edge Functions 2026: a 12-minute survey, results published openly
>
> We (Brackenmoor, a French company) are running a survey on how people build and run edge functions. Open until `<end date>`, about `<N>` minutes. `<One sentence on what decisions the results feed.>`
>
> **What happens to your data:** answers are anonymous. We publish aggregate charts, never raw open text. Full notice on page 1.
>
> **The draw:** after you finish, you can enter a draw for a `<laptop model>`. The email goes in a separate form and is never linked to your answers. The winner is picked by a public random method, described in the rules: `<rules link>`. No purchase needed.
>
> **The caveat:** this survey reaches people through our blog, newsletter and communities like this one. Percentages will describe respondents, not all edge-function developers, and the report will say so.
>
> Link: `<link ?src=reddit-raffle>`

Do not use "retweet to enter" or "comment to enter". Entry is only through the form, which keeps the draw away from platform contest rules and away from rewarding engagement over honest answers.

## How to run the draw

**Before the end date**

1. Publish the rules, including the draw method and the exact UTC time of the draw.

**After the entry window closes**

2. Export the entries. Remove invalid and duplicate ones: unverified completion code, repeated code, same normalised email (lowercase, dots and `+tags` stripped), under 18, ineligible country, employee. Keep the removal counts.
3. Sort the remaining entries by entry ID and number them 0 to N−1.
4. **Publish a commitment** (on the rules page, before the draw time): the number N and a SHA-256 hash of the sorted list of entry IDs. This shows you cannot change the list after seeing the result.
5. **At the announced time, take a public random value** that nobody controls, such as the drand beacon round for that time. Compute `winner = value mod N`. The next indexes in order (`+1`, `+2`, …) are the alternates.
6. **Verify the winner:** check the completion code is valid and unused elsewhere, the email works, and the address is in an eligible country. If not, take the alternate.
7. **Publish** the round number, N, the hash, and the winning entry ID (not the name) so anyone can recompute it.
8. **Email the winner.** Allow 14 days, as the rules say.

**After**

9. **Delete every non-winner's email** within 30 days. Drop the IP hash column at cleaning.
10. Keep the winner's details only as long as shipping, accounting and tax require. Write that period in the data map.
11. **Record in the methodology:** the number of entries, the removal counts, the announcement date, and the pre/post-announcement source mix.

## Things this will not fix

- **Selection bias.** Prize hunters are a different population. The report must still say who the sample over-represents, and you must not call the results "developers think…". Use rung 1: "X% of respondents".
- **Trend claims.** If last year had no incentive, compare only core-module questions, and label pre-raffle and post-raffle responses separately.
- **The raffle's real cost.** It is compliance, fraud screening and a prize. It is not a response-rate fix.

## The cheaper version (recommended if you can still choose)

Replace the draw paragraph in both posts with:

> For every completed response between now and `<end date>`, Brackenmoor will donate `<amount>` to `<named open-source project or charity>`, up to `<cap>`. We'll publish the total.

- No emails, no sweepstakes rules, no winner handling, no tax questions.
- The skill finds no evidence separating donations, badges and prize draws, so you lose little.
- Keep the fraud checks on anyway, because any public incentive draws bots.

**Next step for you:** send the rules draft to your data-protection contact and a lawyer today. The 18 days run from now, and the draw cannot start without their sign-off.