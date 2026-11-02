Here are the numbers, sourced individually — there is no single "industry standard" for any of the three metrics you asked for. What exists is a handful of named organizations' published policies, one practitioner handbook's worked example, and (for the third metric) nothing published at all. I'll flag which is which so you don't hand leadership a number that turns out to be one project's internal target dressed up as a market-wide benchmark.

## Time to acknowledge a report

| Target | Who publishes it | Status |
|---|---|---|
| 1 business day | Django (code-of-conduct working-group manual) | Published org target |
| 3 business days | CNCF (code of conduct + incident-resolution procedures) | Published org target |
| 24 hours | Aurora & Gardiner, *How to Respond to Code of Conduct Reports* (Frame Shift Consulting, 2019) | Worked illustration in a practitioner handbook, not a surveyed norm |

No survey ties these to community size. At 30,000 registered users across a forum and a chat server, 24 hours is the tightest of the three published anchors and the one most cited in enforcement literature as the credible floor — use it as your target, not because it's "the standard," but because it's the most defensible sourced number to stand behind if leadership or a reporter asks where it came from.

## Time to resolution (report → decision)

Only one sourced anchor exists: **10 business days**, from Aurora & Gardiner's worked example — again an illustration, not a benchmark drawn from multiple communities. Django and CNCF publish acknowledgment targets but do not publish a resolution-time target. There is no cross-community distribution to pull a percentile from.

If leadership wants a resolution target, 10 business days is the only sourced figure in the literature you can cite by name. The stronger operational point, also sourced (same handbook): the dominant enforcement failure is a team that never quite decides — not one that decides too fast — so the target's real job is forcing a decision date onto the calendar, not hitting a specific number.

## Repeat-offence rate

**No source publishes a target number for this.** Not Django, not CNCF, not the Aurora & Gardiner handbook, not the Contributor Covenant. If you put a specific percentage in the OKR and call it an industry benchmark, that claim won't survive anyone checking. The one thing every source agrees on: read this rate next to report *volume*, never alone — a repeat-offence rate near zero is exactly as consistent with "the ladder works" as with "people stopped reporting." A rate improving alongside flat or growing report volume is the only version of this metric that means what you want it to mean.

Practical route to a credible target: don't import one. Measure your own repeat-offence rate for one quarter first, then set next quarter's OKR as an improvement against your own baseline. That's also the approach the sourced material itself recommends for the other two baselines (95% acknowledged-in-window, 100% cases with a recorded outcome are explicitly self-set design gates in this playbook, meant to be recalibrated from a team's first quarter — not quoted externally either).

## What I'd actually put in the OKR doc

- Acknowledge reports within **24 hours** (sourced: Aurora & Gardiner; tightest defensible published anchor).
- Decide within **10 business days** (sourced: Aurora & Gardiner's worked example — the only published resolution-time figure that exists).
- Establish a repeat-offence baseline this quarter, tracked against report volume; set next quarter's target as measured improvement over your own number — flag to leadership that no external benchmark for this metric exists, so the first quarter's job is producing your own baseline, not beating someone else's.

One more thing worth saying to leadership directly, since it'll come up if anyone fact-checks: these acknowledgment/resolution numbers are what Django and CNCF hold *themselves* to, not a statistic about the field. Framing the OKR as "we're adopting the same targets the Django and CNCF conduct teams publish" is accurate and credible. Framing it as "the industry standard is X" is not — nobody has published that distribution.