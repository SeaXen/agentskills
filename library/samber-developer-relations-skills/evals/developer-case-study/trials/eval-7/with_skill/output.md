# Results section — Orbit Cargo study

## Verdict on the two marketing lines

Neither ships as worded.

- **"$102,000 saved annually"** — that's $8,500/month × 12, and the skill's number discipline is explicit: don't annualize a one-month result. Worse, that $8,500/month delta isn't isolated — Orbit Cargo also moved to Graviton runners and deleted two flaky test suites in the same month, either of which moves the CI bill on its own. You can't credit the whole delta to the migration.
- **"Over 70% faster builds"** — the arithmetic is fine (22→6 min is a 73% drop), but the underlying number is *queue wait*, not build time. "Builds are 70% faster" overclaims scope you didn't measure. Say "build queue wait," not "builds."

## Evidence ledger

| Claim | Class | Instrument | Window | Note |
|---|---|---|---|---|
| Build queue wait: 22 min → 6 min median | Measured | Buildkite dashboard | Before: 6 wks pre-cutover / After: 3 wks post-cutover | Same instrument both sides, but windows aren't equal length — say so rather than implying a clean apples-to-apples comparison |
| CI bill: $18,400 → $9,900 | Partially measured, confounded | Not stated — confirm (invoice? cloud billing console?) | First month post-cutover | Same month as Graviton runner migration + two flaky-suite deletions. Can't attribute the full delta to this product alone |
| "Support tickets are way down" | Directional | None — untracked | n/a | No instrument behind it. Drop any number; it's an opinion, not a metric |

## Draft — Results

Median build queue wait fell from 22 minutes to 6 minutes — a 73% drop — measured on Orbit Cargo's Buildkite dashboard. The before-figure is the median over the six weeks before cutover; the after-figure is the median over the three weeks since, so the after-window is still half the length of the before-window and will firm up as more data comes in.

Orbit Cargo's monthly CI bill dropped from $18,400 to $9,900 in the first month after the move — a reported figure we can't credit to this migration alone. In the same month the team also moved its runner fleet to Graviton and retired two flaky test suites, either of which would independently cut compute spend and rerun costs. Nobody on their side has broken out how much of the $8,500 drop belongs to which change, so we report the total delta and name what else moved, rather than annualizing it or claiming it whole.

[VP name/title] said support-ticket volume from the build team is down since the move; Orbit Cargo doesn't track ticket counts, so no number is attached to this claim — it stands as their impression, not a measured result.

## Before this ships

1. **Get the CI-bill instrument.** Invoice line item? Billing console export? Needed to even call this "reported" with a straight face, let alone "measured."
2. **Get the VP's name, title, and a verbatim quote** for the support-ticket line — per the skill's quote rule, no placeholder quote goes out. Right now you have a paraphrase, not a quote; either get it on the record or drop the line entirely.
3. **Confirm the after-window will extend.** A 3-week after-window next to a 6-week before-window is publishable as partial, but flag internally that you'll want to refresh this number once you have 6 matching weeks.
4. **If marketing pushes back on losing the $102k headline**, the defensible substitute is the two hard numbers above, not a synthesized annual figure — offer "median build queue wait down 73%, CI spend down ~46% in month one alongside two other infra changes" as the alternative framing.