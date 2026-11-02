Here's the one-slide dashboard.

---

## What it says, and why it's built this way

I led with **median time to first response (11d → 2d)**, not contributor count, because it's the only number on this slide that isn't confounded. Two other things happened in Q3 — a newsletter feature in August, a conference talk in September — and both land inside the same quarter as your "after" data point. A response-time drop is a maintainer-behavior metric; visibility spikes don't cause maintainers to answer faster (if anything, more inbound volume from a newsletter surge should slow that number down, not improve it). That it improved anyway is the cleanest evidence the fix itself changed something.

The contributor count (2 → 1 → 5) is real and worth showing, but per this skill's own baseline: *"four external pull requests a quarter cannot produce a trend, and a conference talk or a front-page mention moves every number below more than a documentation change does."* You have three quarters of data, one of them post-fix, and that one post-fix quarter is the exact quarter carrying both external visibility events. That's not a reason to hide the number — it's a reason to label it "directional, not proof" instead of "5x growth," which is the framing that gets torn apart in the room if anyone on the VP's staff asks "wasn't that the newsletter month?"

I also flagged what's *not* on the slide: second-contribution rate, external merge rate, contributor absence factor, setup-support load. You didn't give me those numbers, and I'm not going to fabricate them to fill a dashboard — they're the metrics that would actually prove retention, not just a one-time bump, and they're listed with when they'll become available (Q3 closes 2026-09-30; first Q3 contributors cross their 90-day mark around December).

## The slide (HTML — save as `.html` and open in a browser)

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>Lumenstack — contributing-path fix, Q3 read</title>
<style>
  :root { color-scheme: light; }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    background: #f9f9f7;
    font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
  }
  .slide {
    width: 1280px;
    height: 720px;
    background: #fcfcfb;
    border: 1px solid rgba(11,11,11,0.10);
    border-radius: 8px;
    padding: 40px 48px 28px;
    display: flex;
    flex-direction: column;
    gap: 18px;
  }
  .eyebrow {
    font-size: 13px;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    color: #898781;
    font-weight: 600;
  }
  h1 {
    margin: 2px 0 0;
    font-size: 27px;
    color: #0b0b0b;
    font-weight: 700;
  }
  .subtitle {
    margin: 2px 0 0;
    font-size: 14px;
    color: #52514e;
    max-width: 980px;
  }
  .row {
    display: flex;
    gap: 20px;
    align-items: stretch;
  }
  .hero {
    flex: 0 0 300px;
    background: #fcfcfb;
    border: 1px solid rgba(11,11,11,0.10);
    border-radius: 8px;
    padding: 18px 20px;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  .hero .label { font-size: 13px; color: #52514e; }
  .hero .value {
    font-size: 56px;
    font-weight: 700;
    color: #0b0b0b;
    line-height: 1.05;
    margin-top: 4px;
    font-variant-numeric: proportional-nums;
  }
  .hero .value .unit { font-size: 24px; color: #52514e; font-weight: 600; }
  .hero .delta {
    margin-top: 8px;
    font-size: 15px;
    font-weight: 600;
    color: #006300;
  }
  .hero .caption {
    margin-top: 10px;
    font-size: 12.5px;
    color: #898781;
    line-height: 1.4;
  }
  .kpis {
    flex: 1;
    display: flex;
    gap: 14px;
  }
  .kpi {
    flex: 1;
    background: #fcfcfb;
    border: 1px solid rgba(11,11,11,0.10);
    border-radius: 8px;
    padding: 14px 16px;
    display: flex;
    flex-direction: column;
  }
  .kpi .label { font-size: 12.5px; color: #52514e; font-weight: 600; }
  .kpi .value { font-size: 34px; font-weight: 700; color: #0b0b0b; margin-top: 2px; }
  .kpi .note { font-size: 11.5px; color: #898781; margin-top: auto; padding-top: 6px; }
  .kpi.open { border-style: dashed; }
  .confound {
    background: #fdf7ea;
    border: 1px solid #eda10055;
    border-left: 4px solid #eda100;
    border-radius: 6px;
    padding: 12px 16px;
    display: flex;
    gap: 12px;
    align-items: flex-start;
  }
  .confound .icon { font-size: 16px; line-height: 1.3; }
  .confound .text { font-size: 13px; color: #3a3a38; line-height: 1.45; }
  .confound .text b { color: #0b0b0b; }
  .bottom { display: flex; gap: 20px; }
  .pending {
    flex: 1.3;
    border: 1px solid rgba(11,11,11,0.10);
    border-radius: 8px;
    padding: 12px 16px;
  }
  .pending .title {
    font-size: 12.5px;
    font-weight: 700;
    color: #52514e;
    text-transform: uppercase;
    letter-spacing: 0.03em;
    margin-bottom: 6px;
  }
  .pending ul { margin: 0; padding-left: 18px; }
  .pending li { font-size: 12.5px; color: #3a3a38; margin-bottom: 3px; }
  .pending li .why { color: #898781; }
  .footnote {
    flex: 1;
    font-size: 11.5px;
    color: #898781;
    line-height: 1.5;
    align-self: center;
  }
</style>
</head>
<body>
  <div class="slide">
    <div>
      <div class="eyebrow">Lumenstack &middot; open-source feature store &middot; contributor-path read-out</div>
      <h1>The contributing-path fix is working on response time. The contributor-count jump is real but not isolated proof.</h1>
      <p class="subtitle">Before/after split: Q1&ndash;Q2 2026 (pre-fix) vs. Q3 2026 (post-fix, still open &mdash; 6 days remain as of this read). Evidence attached to every number; see confounder and pending-data notes below before repeating these numbers upward.</p>
    </div>

    <div class="row" style="flex: 1;">
      <div class="hero">
        <div class="label">Median time to first human response</div>
        <div class="value">2<span class="unit"> days</span></div>
        <div class="delta">&#9660; from 11 days (&minus;82%)</div>
        <div class="caption">
          Cleanest signal in this deck: it's a maintainer-behavior metric, not a
          visibility metric &mdash; the August/September attention spike (right)
          couldn't have caused it, and if anything more inbound volume should have
          pushed it the other way. vs. GitHub OSS Guides' 48-hour published
          reference point: now inside it; was not.
        </div>
      </div>

      <div class="kpis">
        <div class="kpi">
          <div class="label">External contributors &mdash; Q1 2026</div>
          <div class="value">2</div>
          <div class="note">Pre-fix baseline</div>
        </div>
        <div class="kpi">
          <div class="label">External contributors &mdash; Q2 2026</div>
          <div class="value">1</div>
          <div class="note">Pre-fix (fix landed ~last week of quarter)</div>
        </div>
        <div class="kpi open">
          <div class="label">External contributors &mdash; Q3 2026</div>
          <div class="value">5<span style="font-size:16px;color:#898781;">*</span></div>
          <div class="note">*Quarter still open (6 days left) &amp; carries both confounders below</div>
        </div>
      </div>
    </div>

    <div class="confound">
      <div class="icon">&#9888;&#65039;</div>
      <div class="text">
        <b>Read the Q3 jump as (fix + visibility), not fix alone.</b>
        A popular newsletter featured Lumenstack in August, and a conference talk followed in September &mdash;
        both inside the only post-fix quarter we have. This skill's own guidance: a conference talk or a
        front-page mention moves contributor counts more than a documentation change does, and a single
        quarter of data (n=3 total, one post-fix) is below the 4-per-quarter floor needed to call this a trend
        rather than an anecdote with a date attached. The response-time metric above is the one number in this
        deck that visibility can't explain away.
      </div>
    </div>

    <div class="bottom">
      <div class="pending">
        <div class="title">Not on this slide because it isn't measurable yet</div>
        <ul>
          <li>Second-contribution rate (90-day window) <span class="why">&mdash; most Q3 contributors haven't reached day 90</span></li>
          <li>External first-PR merge rate &amp; time-to-merge <span class="why">&mdash; needs a closed quarter</span></li>
          <li>Contributor absence factor (CHAOSS) <span class="why">&mdash; needs a full post-fix year to move meaningfully</span></li>
          <li>Setup-support load (the fastest-visible win) <span class="why">&mdash; not yet counted this cycle</span></li>
        </ul>
      </div>
      <div class="footnote">
        Pull again after Q3 closes (2026-09-30) for a clean quarter, and again once the first Q3 contributors
        cross their 90-day mark (~Dec 2026) for second-contribution rate. 12-of-16 scorecard re-run due next
        quarter. 4-per-quarter trend floor and 90-day window are this skill's own self-set baselines, not
        published standards &mdash; say so if asked where they come from.
      </div>
    </div>
  </div>
</body>
</html>
```

## If the VP pushes for a single number anyway

Give them the response-time drop, not the contributor count: **"Median first response went from 11 days to 2 — inside GitHub's own 48-hour benchmark for the first time — measured over 90 days, unaffected by this quarter's press."** It's smaller-sounding than "5x more contributors," but it's the one claim that survives a follow-up question about the newsletter.