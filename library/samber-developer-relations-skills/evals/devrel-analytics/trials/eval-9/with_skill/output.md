## Nordvale channel backfill — what I can and can't build as described

**The job as specified gets refused, not built.** Two of its premises break this skill's guardrails, and building it as asked would make the board chart *more* wrong than the gaps it's meant to fix.

### 1. It overwrites populated rows

"Filled in by whoever noticed at the time" is still a recorded source — possibly `self_reported` or `journey_linked` quality, just uncoded. The rule is **never overwrite**: backfill touches only rows where `source` is blank. A row someone already populated doesn't get replaced by a heuristic guess, even a good one. If you want those recoded, that's a separate manual reclassification pass with its own review, not part of this job.

### 2. The campaign-window heuristic doesn't pin here

Attributing a blank signup to "whichever campaign was live that week" is only valid evidence when three conditions all hold for that record:

1. The signup date falls inside exactly **one** campaign's window — not zero, not several.
2. The landing page belongs to **that** campaign.
3. That campaign's tags were live at the time.

You said three to five campaigns ran concurrently most months, and they mostly landed on `/get-started`. That fails condition 1 (multiple campaigns overlap almost every week) and condition 2 (a shared landing page can't distinguish which campaign a given visit belongs to) simultaneously, for most of the eight months. There's no fractional or probabilistic split across the concurrent campaigns either — allocating a signup 1/4 to each of four campaigns manufactures attribution, it doesn't recover it. Per record, the honest outcome is binary: pin it, or write `unknown`.

Practically: unless you can name specific weeks where exactly one campaign was live, or where only one of the concurrent campaigns actually used `/get-started`, the heuristic resolves almost nothing across this window. Most of the 40% blank stays `unknown` after this job runs, not filled.

### The job to actually run

Write three fields, not one bare `channel`:

| field | meaning |
|---|---|
| `source` | the channel name, or `unknown` |
| `source_basis` | `journey_linked` \| `self_reported` \| `campaign_window` |
| `source_confidence` | judged on evidence quality — never inferred from `source_basis` alone |

```sql
-- pseudocode, fail-closed
UPDATE signups
SET source = CASE
               WHEN (SELECT count(*) FROM campaigns c
                     WHERE signups.signup_at BETWEEN c.start AND c.end
                       AND c.landing_page = signups.landing_page
                       AND c.tags_live = true) = 1
               THEN (SELECT c.channel FROM campaigns c
                     WHERE signups.signup_at BETWEEN c.start AND c.end
                       AND c.landing_page = signups.landing_page
                       AND c.tags_live = true)
               ELSE 'unknown'
             END,
    source_basis = CASE WHEN <above count = 1> THEN 'campaign_window' ELSE NULL END,
    source_confidence = CASE WHEN <above count = 1> THEN 'low' ELSE NULL END  -- campaign_window is always the weakest basis; never rate it above a specific self-report
WHERE source IS NULL;  -- blanks only, nothing already populated is touched
```

A row that resolves to `unknown` gets no `source_basis`/`source_confidence` — absence of a value, not a manufactured one. That's the visible, fixable gap the skill wants over a silent wrong merge.

To run this for real I need two inputs I don't have: the campaign calendar (start/end date, landing page, tag-live status per campaign) and the raw signup export. Send those and the job runs as-is.

### The chart

**No gapless eight-month trend.** Once the job runs, most months will show a large `unknown` bucket sitting next to whatever `journey_linked`/`self_reported`/pinned-`campaign_window` rows exist — that's the accurate picture of an eight-month period run on 3–5 concurrent campaigns with one shared landing page, not a defect in the chart.

Build it as a stacked bar per month, not a line:

- One segment per real `source`, colored normally.
- `unknown` as its own segment, visually distinct (hatched or greyed, not just another color in the same palette) — so a viewer can't read total bar height as "signups by channel" without noticing how much of it is unattributed.
- Never merge `unknown` into an existing channel's segment to make the bar height "cleaner."
- Label the chart with the coverage rate (% not `unknown`) per month, since that number is the real health metric here, not the channel mix.

If the board wants a trend line specifically, the defensible one is **join coverage over the eight months** — is the unattributed share shrinking — not a channel-mix line that implies attribution which is not there.

### Fixing this so it doesn't recur

The backfill only buys you the past; the 40%-blank problem repeats next quarter unless you fix intake. In `efficiency` order, both are cheap:

- **Tagging vocabulary + per-artifact link registry** — fix source/medium values now, before the next campaign launches. Retroactive merging of `Twitter`/`twitter`/`X` is exactly this kind of unrecoverable mess one decision away.
- **Self-reported source field at signup** — near-zero cost, and it's the only real signal for the months where 3–5 campaigns share a landing page and nothing else can disambiguate them.

Send the campaign calendar and signup export and I'll run the job and produce the actual chart against real numbers.