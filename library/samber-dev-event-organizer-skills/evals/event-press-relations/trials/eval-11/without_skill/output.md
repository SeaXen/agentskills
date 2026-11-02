**Next:** send me three numbers: the edition 1 and 2 "how did you hear" split (or the nearest proxy), the TerraformDays date, and the proposed press spend. Those turn the ranges below into targets you can defend. Until then, treat them as planning ranges.

I have no edition 1 or 2 data and no ticket-source data. Every number below is tagged:

- `baseline`: derive it from your own history.
- `hypothesis`: my planning assumption, backed by no measurement. Replace it before the board sees it.

Nothing here is sourced from an industry benchmark.

# TerraformDays 3: press KPI sheet (draft v0)

## 1. Two points to settle with the board first

**Earned press is not purchased.** Paid placement is advertising. The spend funds the work that earns coverage: media map, press page, proof pack, briefings, press passes, a freelancer. It does not buy articles. Frame the request as spend on a press program, released in gates (section 5).

**"% of tickets driven by press" is a measured outcome, not a forecastable one.**
- Press mostly builds credibility, not conversions. Developers read an article, then decide on the agenda, speakers, and price.
- Press-driven buyers are also under-counted: they land in "direct" or "search".
- Give the board a range, a written measurement rule, and a floor. Never promise a point estimate.

## 2. Forecast model (replace placeholders with edition 1–2 data)

```
qualified pieces  = tier-1/2 reporters pitched × placement rate
press tickets     = tickets sold × press-attributed share
cost per ticket   = press program spend ÷ press tickets
```

Scenarios for 1,400 tickets. All values are `hypothesis`.

| Scenario | Qualified pieces | Press-attributed share | Press tickets |
|---|---|---|---|
| Low | 6 | 3% | 42 |
| Base | 12 | 5% | 70 |
| High | 20 | 8% | 112 |

The share is a self-reported share of buyers. It is a floor, not a total. Compare the board's spend to the Base row only after you have replaced the placeholders with edition 2 data.

## 3. KPI sheet

Eight metrics, one primary per goal. Each has an owner, so assign names.

| # | Metric | Definition and source | Target | Tag | Action on miss |
|---|---|---|---|---|---|
| 1 | **Verified media map** (input) | Reporters with a byline on the beat in the last few months and a confirmed current employer. Source: media map. | 25–40 | `baseline` (self-set size) | Under 25: delay pitching, build the map first. |
| 2 | **Qualified pieces published** (primary, articles) | Original coverage naming TerraformDays, with a link to the ticket page or site. Excludes press-release reposts, event-listing pages, and syndication duplicates. Source: coverage tracker. | 6 / 12 / 20 (low/base/high) | `hypothesis` | Below the low case at T-3 weeks: re-angle and send a second wave. |
| 3 | **Tier-1 pieces** | Pieces in named tier-1 outlets from the media map. Raw list with dates, because the count is small. | 2–5 | `hypothesis` | None at T-4 weeks: offer the exclusive to one outlet. |
| 4 | **Press-attributed ticket share** (primary, tickets) | Checkout question "How did you hear about us?" with an explicit "Article, newsletter or press" option, plus tagged links. Reported only if the question gets a ≥70% response rate. | 3–8%, planning point 5% | `hypothesis`; set to your edition 2 share once known | Below 3% with a valid response rate: no further press spend next edition. |
| 5 | **Ticket-page visits from coverage** | Referral clicks from article URLs to the ticket page. A floor, never a total. | Baselining | `baseline` after edition 3 | Check whether pieces carry a link at all; ask for corrections. |
| 6 | **New referring domains from coverage** | Durable discoverability. Source: backlink tool and Search Console. | 8–20 | `hypothesis` | Ask for the link on pieces that name you without linking. |
| 7 | **Inbound requests** | Sponsor, speaker, partner or reporter inquiries citing coverage. Raw list with dates. | Report the list, set no number | `baseline` | None; qualitative evidence for the next board review. |
| 8 | **Cost per qualified piece, and per attributed ticket** | Program spend ÷ metric 2, and ÷ (tickets × metric 4). | Set after the edition 2 baseline; compare to your other channels' cost per ticket | `baseline` | Above the other channels: cut press, keep only the owned assets. |

**Counter-metrics:**
- Metric 2 must be read with the exclusion rule, or you can pad it with reposts.
- Metric 4 must be read with its response rate.

**Deleted on purpose:**
- Advertising value equivalency and impressions. Both are refused as measures of value, and neither moves a decision.
- A total press-driven ticket count from analytics. Referrers are stripped, so it can only be a floor.
- A revenue figure attributed to one article.

## 4. Attribution rule (write it down before sales open)

- **Primary instrument:** the checkout question, held constant across editions.
- **Secondary instrument:** tagged links in every pitch, used to compare articles only.
- **Lookback:** from the first press activity to the event date.
- **Wording:** the report says "press-attributed" for self-reported buyers and "influenced" wherever credit is shared. It never says "driven".
- **Confound control:** log every paid promotion, speaker announcement and email blast by date, so a press spike is not credited with their effect.

## 5. Spend gates

- **Gate 1, now:** fund only the owned assets (press page, proof pack, media map, a freelancer if needed). Condition: map ≥25 verified reporters.
- **Gate 2, about T-8 weeks:** fund briefings, press passes, and travel for reporters. Condition: at least 3 tier-1 reporters replied with interest.
- **Gate 3, about T-3 weeks:** fund a second wave only if metric 2 is on a pace to reach the low case.
- **Post-event review:** apply metric 8. Kill the press line next edition if cost per attributed ticket is above your other channels.

## 6. Blind spots to state to the board

- No baseline yet for metrics 4–8, so all targets are ranges for the first cycle.
- Press-driven buyers who arrive through "direct" or "search" are invisible, so metric 4 understates press.
- Third-edition ticket sales also depend on speakers, price and timing, so press cannot take sole credit.
- With about 12 pieces, any percentage swings widely. Read the raw list, not rates.

## 7. Open before the sheet is final

1. Edition 2 ticket-source data, or the nearest proxy.
2. Event date, so I can set the T-minus calendar.
3. Spend amount and ticket price, to compute the break-even tickets: spend ÷ price.