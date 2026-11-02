# Wrackline newsroom page — spec, copy blocks, and the sponsored-editorial call

## The three requests I'm pushing back on, and why

The tech-press-relations checklist treats these as named anti-patterns because a reporter evaluates your page in the same minute they'd otherwise be writing about you — friction there is a cost paid in coverage, not just conversions.

**"Every asset behind a form."** The press page is an Owned surface that exists to serve Earned coverage (PESO model, Dietrich 2014) — a different job than a gated whitepaper. A reporter on deadline who hits a form for a logo or a headshot does one of two things: uses a low-res grab from Google Images instead, or drops you from the piece. If marketing needs the lead-capture number, get it from a different asset — a benchmark report, a webinar, a template — not from the newsroom page. Gating the newsroom page trades a coverage chance for a lead that a bounced reporter was never going to convert anyway.

**"A contact form instead of an email address."** Same failure, sharper: a form routes into a queue with no visible owner and no SLA. The checklist wants a named contact, a real address, and a response time you'll actually honor — because an unmonitored press address is worse than none, but a monitored one is the single highest-leverage line on the page. Recommendation: `press@wrackline.dev` (or whatever's real), monitored, same-business-day response stated and kept true.

**"The logo pack as a .psd bundle."** A PSD needs Photoshop to open. A reporter or their production desk needs to drop a usable mark into a CMS in under a minute — that's SVG (scales, editable in free tools) and PNG (raster, drop-in), each in light and dark. If there's a real internal need for a layered working file (agency handoff, co-marketing), keep that as a private asset sent on request — don't make it the public download.

**"Three customer logos, no other detail."** Lower stakes, still worth flagging twice: first, displaying a customer's mark at all needs their written sign-off — that's a trademark/brand-guidelines question, not a press-relations one, but it's the same due diligence the skill requires before naming any customer in a story. Second, three bare logos are the weakest form of proof this checklist recognizes — a "trusted by" strip, not evidence. It costs nothing extra to add one cleared line per logo ("monitors edge-function latency across three regions for **Customer A**"); if that's genuinely not available yet, ship the strip as decoration and don't let anyone describe it internally as a case study.

None of this blocks the launch — it just means two things get built (newsroom page, ungated) instead of one (newsroom page, gated), and marketing's lead-capture goal moves to the asset built for it.

## The press page (`/newsroom` or `/press`) — spec and copy blocks

No form anywhere on this page. Every download works without an email address.

```
# Wrackline — Newsroom

## About
[One sentence]  Wrackline is observability for edge workers — traces, logs and
metrics from code running at the CDN edge, without shipping it back to a
central region first.

[One paragraph]  [Founding story / problem statement — fill in]

[~100 words]  [Fuller company description, same wording used on the site and
in bios elsewhere — fill in]

## Facts
- Founded: [date]
- Headquarters: [city]
- Team size: [band, e.g. 11-50]
- Funding: [amount / round / lead, or "not disclosed"]
- Pronunciation note: WRACK-line — a wrackline is the tideline of debris a
  wave leaves on a beach; worth stating since it's not a common word.

## Leadership
[Name], [title] — [2-3 sentence third-person bio]. [High-res headshot,
downloadable, no form.]
[Repeat per spokesperson.]

## Logo pack
Download (.zip): SVG + PNG, light and dark. [direct link, no gate]
Usage: minimum clear space [X]px, minimum size [X]px, don't recolor, don't
stretch, always capitalize as "Wrackline."

## Product
- [3-5 screenshots]
- [One short demo recording, <2 min]

## Trusted by
[Customer A logo] [Customer B logo] [Customer C logo]
[If cleared: one line per logo on what they use Wrackline for.]

## Coverage
[Most recent first. Leave the section present but empty until the first
placement lands — an empty, honestly-labeled section reads better to a
reporter checking before they write than a padded one.]

## Press contact
[Name], [title] — press@wrackline.dev — we reply same business day, Mon-Fri.
```

## The technical proof pack (link from the newsroom page)

This is the part that decides whether a Wrackline story survives its own comment section, and it's what separates a page a reporter can write from one they can only repeat:

- A running artifact — sandbox, docs playground, or install command available now, not "on request."
- Every latency/overhead claim with the hardware, runtime versions, workload shape, and a harness a stranger can rerun. For an edge-observability product this is the claim readers will check first.
- Architecture note: what's genuinely new here versus assembled from OpenTelemetry / existing edge runtimes — say which.
- A comparison table against real alternatives (Cloudflare's own observability, Datadog, whatever's actually competing), including the rows where Wrackline loses.
- Known limitations, stated plainly — which workloads or edge runtimes this doesn't cover yet.
- Licence and pricing, unambiguous.
- Security/compliance posture, if any part of the buying motion is enterprise rather than pure bottom-up developer adoption.

## The sponsored editorial offers — no, and I won't draft the pieces under this work

Both outlets are offering **Paid** placement — one of the four PESO quadrants, and explicitly the one this skill doesn't touch: "when a user asks you to buy coverage, say no and name the boundary: paid placement is advertising, with different rules and different disclosure." Writing the two pieces as part of a press-relations engagement would blur exactly the line that makes earned coverage worth anything — so I'm declining to draft them here, not because sponsored content is improper, but because it's a different discipline with different rules, and this skill's answer to "should we buy coverage" is no by design.

On whether to buy it at all, plainly:

- **"Partner content" is a soft label.** For a technical, skeptical-of-vendor-content audience, a euphemistic tag reads as an attempt to borrow editorial credibility without earning it — the same failure mode the skill calls out for licence-change euphemisms ("a clarification" instead of naming the change). If you run these, push both outlets for the clearest disclosure they'll allow — "Sponsored," "Advertisement," "Paid Partner Post" — over "partner content."
- **It buys reach, not credibility.** Treat the $12k combined as a paid-media spend decision, not a PR one: compare it against other paid channels (a newsletter placement, a docs-SEO investment) on reach and cost, never report it alongside earned coverage numbers, and never let it appear in the newsroom "Coverage" section above — that section is Earned only, or the whole page loses credibility with the next reporter who checks it.
- **It only works if the content is actually useful.** A sponsored post that reads like the pitch's weak twin — adjectives standing in for a checkable claim — gets the same instant dismissal from a developer audience that an ungated logo pack was built to avoid. If you proceed, the piece needs a real technical claim with methodology, same bar as the proof pack above, or it's money spent to be skipped.
- **Check the wall.** Ask each outlet how their sponsored and editorial teams are separated before signing — at the outlets developer press actually reads, buying sponsored space at a publication whose reporters you're also pitching this quarter can read as leverage rather than coincidence to the reporter, even when the two desks are genuinely independent.

My recommendation: pass on both, or take them only with disclosure tightened to an unambiguous label, content held to the same evidentiary bar as the proof pack, and the spend kept entirely out of any earned-media reporting. If you want the copy written once that's decided, that's a copywriting engagement I can pick up separately — it just isn't this one.