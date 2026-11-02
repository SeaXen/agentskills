# Pinebarrow webinar series: measurement sheet

Three items need your decision before the deck (see "Decisions needed"):
1. Don't put the agency's 44% and 39% on the slide as targets.
2. The series' job is signup to first index, so that metric leads the slide.
3. I can't compute attendee-to-MQL: you gave me no attendee or MQL counts, so those cells stay blank.

## 1. Why the agency numbers can't be targets

- **Wrong stage.** The CEO's metric is attendee-to-MQL. The agency's is lead-to-MQL, and the denominators differ. Their "lead" may include registrants who never attended, so the two rates aren't comparable.
- **Wrong definition.** An MQL is whatever each company's scoring says it is. 44% lead-to-MQL means nothing without their scoring rule.
- **Selection bias.** An agency shows its best clients. That is a ceiling, not a baseline.
- **Not derived from our data.** A target should come from our own baseline plus a stated lift. Neither exists yet.
- **Misaligned incentive.** A 39% MQL-to-SQL target rewards sales qualification. The series' job is first index. Chasing MQL volume could pull the series toward gated, sales-flavored content that doesn't produce indexes.
- **Benchmark source.** I can't verify where the 20-40% industry range comes from. Cite its source on the slide, or label it "industry range, source: ___".

**Recommended slide treatment:** show the 20-40% range as context only, and set our own targets after one quarter of baseline data. Put the agency figures in the appendix, labeled "agency-reported, different funnel stage, not our target."

## 2. Sheet structure

Five tabs: **Inputs**, **Funnel**, **Lift**, **Slide**, **Definitions**.

### Tab: Inputs (fill the blanks; never overwrite)

| Cell | Input | Value | Source / owner |
|---|---|---|---|
| B2 | Eligible invite list (unique developers) | 11,000 | Marketing ops |
| B3 | Invites delivered (not just sent) | ___ | Email platform |
| B4 | Registrations (all events, with duplicates) | 3,800 | Webinar platform |
| B5 | Unique registrants | ___ | Dedupe by email |
| B6 | Unique registrants who were on the invite list | ___ | Join on email |
| B7 | Unique attendees (≥ X min live, or on-demand watched) | ___ | Webinar platform |
| B8 | Attendees who created a product account within 30 days | ___ | Join on email or user ID |
| B9 | **Attendees who created a first index within 30 days** | ___ | Product DB |
| B10 | Attendees who became MQL within 30 days | ___ | CRM |
| B11 | MQLs who became SQL | ___ | CRM |
| B12 | LinkedIn impressions (series-attributed posts) | 410,000 | LinkedIn analytics |
| B13 | LinkedIn clicks to registration page | ___ | LinkedIn analytics / UTM |
| B14 | Invite-list non-registrants who created a first index within 30 days | ___ | Product DB |
| B15 | Invite-list non-registrants (= B2 − B6) | `=B2-B6` | |
| B16 | Attendance threshold X (minutes) | ___ | Decide once, then freeze |
| B17 | Attribution window (days) | 30 | Decide once, then freeze |

### Tab: Funnel (all formulas)

| Metric | Formula | Role |
|---|---|---|
| Registrations per unique registrant | `=B4/B5` | Check: how many people the 3,800 really is |
| List reach (invite list → registrant) | `=B6/B2` | Reach |
| Show rate | `=B7/B5` | Event quality |
| Attendee → account | `=B8/B7` | Funnel |
| **Attendee → first index (primary KPI)** | `=B9/B7` | **Series outcome** |
| **Registrant → first index** | `=B9_registrants/B5` | Uses registrants, so no-shows count against us |
| Attendee → MQL (CEO's metric) | `=B10/B7` | Compare to 20-40% context only |
| MQL → SQL | `=B11/B10` | Sales handoff; report, don't target |
| LinkedIn impressions per registration | `=B12/B4` | Context. A 410k / 3,800 ratio is about 108 impressions per registration, but impressions aren't tied to registrations. |
| LinkedIn click-through rate | `=B13/B12` | Only valid with a click count |
| LinkedIn click → registration | `=B4_linkedin/B13` | Needs UTM-tagged registrations |

Mark every cell with a blank input as `n/a`, never 0. A 0 would read as a result.

### Tab: Lift (answers "did the series cause first indexes?")

| Metric | Formula |
|---|---|
| First-index rate, attendees | `=B9/B7` |
| First-index rate, invite-list non-registrants, same window | `=B14/B15` |
| Absolute lift (pts) | attendee rate − non-registrant rate |
| Relative lift | attendee rate ÷ non-registrant rate |

- Attendees chose to show up, so they are more motivated than the control group. Report this as "association with lift", not "caused".
- If attendees index at 18% and non-registrants at 15%, the series adds little.

### Tab: Definitions (freeze before the first number is computed)

1. **Person:** unique, deduped by lowercased email. Registrations are never "people."
2. **Attendee:** watched ≥ B16 minutes, live or on-demand. State which.
3. **First index:** the first successful index creation on the account, from the product DB. Not signup, not trial start.
4. **Window:** B17 days from the event date, or from the on-demand view date.
5. **Attribution:** a person who attended several events counts once, credited to the first event attended.
6. **MQL:** use the current CRM scoring rule, with its date and version written here. Don't change it mid-year.
7. **Time zone and cutoff:** ___.

### Tab: Slide (what the CEO sees)

Title: **Webinars: reach is healthy, activation is the number to watch**

| Block | Content |
|---|---|
| Reach | 3,800 registrations (___ unique people) and ___% of the 11,000 invite list |
| Distribution | 410k LinkedIn impressions, labeled "reach, not conversion" |
| **Outcome** | **___% of attendees created a first index within 30 days; control group ___%** |
| CEO's metric | Attendee-to-MQL ___% (industry range 20-40%, source: ___) |
| Targets | "Q1 target set after the baseline: ___" |

The 3,800 registrations equal at most 34.5% of the invite list (3,800 / 11,000) if every registration were a unique list member. Because it includes duplicates and non-list registrants, the true reach is lower, so don't present 3,800/11,000 as reach.

## 3. Decisions needed

1. **Targets.** Agree to the baseline-first approach in the CEO conversation. Suggested wording: "Those figures are another company's different funnel stage. We'll set our own once we have one quarter of matched data."
2. **Data join.** Can you join webinar emails to product accounts and to the CRM? Without that, B8–B11 stay empty and the primary KPI can't be computed.
3. **Counts.** Are the 3,800 registrations unique people? Do you have the attendee count?
4. **Benchmark source.** Where does the 20-40% come from? If nobody knows, drop it from the slide.
5. **Attendance and window.** Choose B16 and B17 now. Changing them later makes quarters incomparable.

Send me the Inputs values and I'll fill in the Funnel and Lift numbers and the slide.