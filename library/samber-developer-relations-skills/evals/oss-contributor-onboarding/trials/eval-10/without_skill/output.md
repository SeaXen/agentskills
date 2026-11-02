Here's the one-slide dashboard, delivered as a self-contained HTML file you can open in a browser and export to PDF/PNG for the deck. (File write to disk needs your permission — paste this into a `.html` file if you'd rather not grant it.)

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<title>Lumenstack — Contributing-Path Fix: Q3 Impact</title>
<style>
  :root { color-scheme: light; }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    padding: 40px;
    background: #f9f9f7;
    font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
    display: flex;
    justify-content: center;
  }
  .viz-root {
    --surface-1:      #fcfcfb;
    --text-primary:   #0b0b0b;
    --text-secondary: #52514e;
    --text-muted:     #898781;
    --gridline:       #e1e0d9;
    --baseline:       #c3c2b7;
    --border:         rgba(11,11,11,0.10);
    --series-1:       #2a78d6; /* blue, accent / "after" */
    --series-1-soft:  #86b6ef; /* blue step 250, "before" */
    --good:           #006300; /* success text */
    color-scheme: light;
  }
  .slide {
    width: 1280px;
    height: 720px;
    background: var(--surface-1);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 48px 56px;
    display: flex;
    flex-direction: column;
    color: var(--text-primary);
  }
  .eyebrow {
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.08em;
    color: var(--text-muted);
    text-transform: uppercase;
    margin-bottom: 8px;
  }
  h1 {
    font-size: 28px;
    font-weight: 600;
    margin: 0 0 6px 0;
    line-height: 1.25;
  }
  .subtitle {
    font-size: 15px;
    color: var(--text-secondary);
    margin: 0 0 32px 0;
  }
  .row {
    display: flex;
    gap: 40px;
    flex: 1;
  }
  .panel {
    background: var(--surface-1);
    border: 1px solid var(--gridline);
    border-radius: 6px;
    padding: 28px 32px;
    display: flex;
    flex-direction: column;
  }
  .panel-hero { flex: 0 0 54%; }
  .panel-side { flex: 1; }
  .panel-label {
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    color: var(--text-muted);
    margin-bottom: 4px;
  }
  .panel-tag {
    display: inline-block;
    font-size: 12px;
    font-weight: 600;
    color: var(--good);
    margin-bottom: 18px;
  }
  .hero-figures {
    display: flex;
    align-items: baseline;
    gap: 18px;
    margin-bottom: 6px;
  }
  .hero-value {
    font-size: 64px;
    font-weight: 600;
    line-height: 1;
  }
  .hero-delta {
    font-size: 22px;
    font-weight: 600;
    color: var(--good);
  }
  .hero-caption {
    font-size: 14px;
    color: var(--text-secondary);
    margin-bottom: 22px;
    max-width: 480px;
  }
  .dumbbell-wrap { margin-top: auto; }
  .dumbbell-svg { width: 100%; height: 92px; display: block; }
  .col-chart-svg { width: 100%; height: 220px; display: block; margin-top: 12px; }
  .side-caption {
    font-size: 13px;
    color: var(--text-secondary);
    margin-top: 14px;
    line-height: 1.5;
  }
  .side-caption b { color: var(--text-primary); }
  footer {
    margin-top: 28px;
    padding-top: 18px;
    border-top: 1px solid var(--gridline);
    display: flex;
    gap: 28px;
    font-size: 12.5px;
    color: var(--text-secondary);
    line-height: 1.5;
  }
  footer .foot-item { flex: 1; }
  footer b { color: var(--text-primary); }
</style>
</head>
<body>
  <div class="viz-root">
    <div class="slide">
      <div class="eyebrow">Lumenstack · Open-Source Health</div>
      <h1>The contributing-path fix worked — one metric proves it cleanly, one is confounded</h1>
      <p class="subtitle">Fix shipped Q2 2026 · Reporting window Q1–Q3 2026</p>

      <div class="row">
        <div class="panel panel-hero">
          <div class="panel-label">Median time to first maintainer response</div>
          <span class="panel-tag">● Directly attributable to the fix</span>
          <div class="hero-figures">
            <span class="hero-value">2 days</span>
            <span class="hero-delta">−82%</span>
          </div>
          <p class="hero-caption">Down from 11 days pre-fix. No other Q3 event (newsletter, talk) touches this number — it's a maintainer-side process metric, not an inbound-attention metric. This is the strongest evidence the fix itself worked.</p>

          <div class="dumbbell-wrap">
            <svg class="dumbbell-svg" viewBox="0 0 720 92" preserveAspectRatio="none">
              <line x1="20" y1="70" x2="700" y2="70" stroke="#c3c2b7" stroke-width="1" />
              <line x1="643" y1="40" x2="133" y2="40" stroke="#52514e" stroke-width="2" stroke-linecap="round" />
              <circle cx="643" cy="40" r="7" fill="#86b6ef" stroke="#fcfcfb" stroke-width="2" />
              <text x="643" y="20" text-anchor="middle" font-size="15" font-weight="600" fill="#0b0b0b">11d</text>
              <text x="643" y="86" text-anchor="middle" font-size="11" fill="#898781">before (Q1 median)</text>
              <circle cx="133" cy="40" r="7" fill="#2a78d6" stroke="#fcfcfb" stroke-width="2" />
              <text x="133" y="20" text-anchor="middle" font-size="15" font-weight="600" fill="#0b0b0b">2d</text>
              <text x="133" y="86" text-anchor="middle" font-size="11" fill="#898781">after (Q3 median)</text>
            </svg>
          </div>
        </div>

        <div class="panel panel-side">
          <div class="panel-label">External contributors, by quarter</div>
          <span class="panel-tag" style="color:#898781;">◐ Directional — confounded by two other events</span>

          <svg class="col-chart-svg" viewBox="0 0 420 220" preserveAspectRatio="xMidYMid meet">
            <line x1="30" y1="180" x2="400" y2="180" stroke="#c3c2b7" stroke-width="1" />
            <rect x="70"  y="128" width="24" height="52"  rx="4" fill="#86b6ef" />
            <text x="82" y="118" text-anchor="middle" font-size="16" font-weight="600" fill="#0b0b0b">2</text>
            <text x="82" y="198" text-anchor="middle" font-size="13" fill="#52514e">Q1</text>
            <rect x="198" y="154" width="24" height="26"  rx="4" fill="#86b6ef" />
            <text x="210" y="144" text-anchor="middle" font-size="16" font-weight="600" fill="#0b0b0b">1</text>
            <text x="210" y="198" text-anchor="middle" font-size="13" fill="#52514e">Q2</text>
            <rect x="326" y="50"  width="24" height="130" rx="4" fill="#2a78d6" />
            <text x="338" y="40" text-anchor="middle" font-size="16" font-weight="600" fill="#0b0b0b">5</text>
            <text x="338" y="198" text-anchor="middle" font-size="13" fill="#52514e">Q3</text>
          </svg>

          <p class="side-caption">Q3 also had an <b>Aug. newsletter feature</b> and a <b>Sep. conference talk</b> — both drive first-time contributor discovery independent of how easy contributing actually is. With <b>n=1</b> post-fix quarter, can't separate the fix's share of this jump from the attention spike.</p>
        </div>
      </div>

      <footer>
        <div class="foot-item"><b>Read for the VP:</b> lead with response time — it's the fix's direct, unconfounded output. Cite the contributor jump as supporting, not standalone proof; it's real but it shares the quarter with two marketing events.</div>
        <div class="foot-item"><b>Next quarter's test:</b> Q4 has no newsletter/talk scheduled. If contributors hold above the Q1–Q2 baseline (1–2/quarter) without repeat press, that isolates the fix's effect. If Q4 reverts to ~1–2, most of Q3's jump was the attention spike, not the fix.</div>
      </footer>
    </div>
  </div>
</body>
</html>
```

**Why it's built this way, not as one undifferentiated "everything went up" slide:**

- **Median first-response time (11d → 2d, −82%) is the hero number** because it's the one metric with a clean causal line to the fix — nothing else that happened in Q3 (newsletter, talk) plausibly moves how fast maintainers reply to an already-opened PR. It's the number that will survive a skeptical VP pushing back with "couldn't this just be the newsletter?"
- **Contributor count (2 → 1 → 5) is shown but explicitly flagged as confounded**, not hidden. August newsletter + September conference talk both independently drive first-time contributors, and they land in the same quarter as the fix. Claiming "5 in Q3 proves the fix worked" overstates what one uncontrolled quarter with three simultaneous interventions can prove — and a VP or a skeptical peer catching that gap later costs more credibility than not making the claim now.
- **The footer gives a falsifiable next check** (Q4, no press events scheduled) instead of just hedging — so the slide doesn't just admit uncertainty, it tells the VP how the uncertainty gets resolved next quarter.