# Canvas Candlestick Chart for Trade Replay

Custom canvas-based OHLC chart with time-scrubbing and trade-marker overlays. Use when you need: trade replay on historical price action, fast custom charting without TradingView, lightweight embed where TradingView's API key is overkill, or you need to overlay domain-specific markers (trades, signals, alerts) that TradingView's UDF doesn't support.

This pattern was developed for a trade-replay feature where users step through their past trades on a real price chart, with each trade drawn as a colored arrow at the right time and price.

## Why canvas, not a library

- **No external deps**, no API key, no iframe — works offline
- **Full control over marker rendering** (TradingView's UDF doesn't support custom markers with P&L labels)
- **Cheap re-renders** during scrub/playback — the chart is redrawn from data on every `requestAnimationFrame`-ish update
- **Sub-100KB** of code vs 300KB+ for lightweight-charts

The cost: no built-in zoom/pan (you implement it), no indicators (you implement them), and you maintain the renderer.

## Component skeleton

```tsx
"use client";
import { useEffect, useRef } from "react";

type Candle = { ts: number; open: number; high: number; low: number; close: number; volume: number };
type Marker = { ts: number; side: "buy" | "sell"; price: number; pnl?: number };

export function ReplayChart({
  candles, markers, visibleFrom, visibleTo, height = 360,
}: {
  candles: Candle[]; markers: Marker[]; visibleFrom: number; visibleTo: number; height?: number;
}) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const canvas = canvasRef.current!;
    const container = containerRef.current!;
    const ctx = canvas.getContext("2d")!;

    // Resize to device-pixel-ratio
    const dpr = window.devicePixelRatio || 1;
    const rect = container.getBoundingClientRect();
    canvas.width = rect.width * dpr;
    canvas.height = height * dpr;
    canvas.style.width = `${rect.width}px`;
    canvas.style.height = `${height}px`;
    ctx.scale(dpr, dpr);

    const w = rect.width;
    const h = height;
    ctx.fillStyle = "#0f172a";
    ctx.fillRect(0, 0, w, h);  // clear + background

    // ... draw candles, grid, markers here
  }, [candles, markers, visibleFrom, visibleTo, height]);

  return (
    <div ref={containerRef} className="w-full">
      <canvas ref={canvasRef} className="rounded border border-slate-800" />
    </div>
  );
}
```

## DPR scaling — the critical first step

Without DPR scaling, the chart looks blurry on retina/HiDPI displays. With it, it's pixel-perfect:

```ts
const dpr = window.devicePixelRatio || 1;
const rect = container.getBoundingClientRect();
canvas.width = rect.width * dpr;        // internal resolution (sharp)
canvas.height = height * dpr;
canvas.style.width = `${rect.width}px`; // CSS size (what user sees)
canvas.style.height = `${height}px`;
ctx.scale(dpr, dpr);                    // draw in CSS pixels
```

After this, all your draw calls use CSS-pixel coordinates (not raw canvas pixels).

## Price range with auto-padding

```ts
const visible = candles.slice(visibleFrom, visibleTo + 1);
let min = Infinity, max = -Infinity;
for (const c of visible) {
  if (c.low < min) min = c.low;
  if (c.high > max) max = c.high;
}
const pad = (max - min) * 0.04;  // 4% padding so candles don't kiss the edges
min -= pad;
max += pad;
```

The 4% padding is important — without it, the highest wick touches the top axis and the lowest touches the bottom, which looks bad and makes it hard to see the extreme values.

## X / Y scales

```ts
const xPad = 8;
const topPad = 16;
const bottomPad = 24;
const chartW = w - xPad * 2;
const chartH = h - topPad - bottomPad;
const candleW = Math.max(1, chartW / visible.length - 1);

const yScale = (price: number) => topPad + (1 - (price - min) / (max - min)) * chartH;
const xScale = (i: number) => xPad + (i - visibleFrom) * (chartW / Math.max(1, visibleTo - visibleFrom));
```

`candleW - 1` leaves a 1px gap between candles. The `Math.max(1, ...)` is a guard against zero-width when the window has thousands of candles.

## Drawing the candles

```ts
for (let i = 0; i < visible.length; i++) {
  const c = visible[i];
  const x = xScale(visibleFrom + i);
  const yo = yScale(c.open);
  const yc = yScale(c.close);
  const yh = yScale(c.high);
  const yl = yScale(c.low);
  const up = c.close >= c.open;
  ctx.strokeStyle = up ? "#10b981" : "#ef4444";
  ctx.fillStyle = up ? "#10b981" : "#ef4444";

  // Wick (vertical line from high to low)
  ctx.beginPath();
  ctx.moveTo(x + candleW / 2, yh);
  ctx.lineTo(x + candleW / 2, yl);
  ctx.stroke();

  // Body (rectangle from open to close)
  const bodyH = Math.max(1, Math.abs(yc - yo));
  const bodyY = Math.min(yo, yc);
  ctx.fillRect(x, bodyY, candleW, bodyH);
}
```

`Math.max(1, bodyH)` ensures doji candles (open == close) still draw as a visible 1px line.

## Grid + axis labels

```ts
ctx.strokeStyle = "#1e293b";
ctx.fillStyle = "#64748b";
ctx.font = "10px ui-monospace, SFMono-Regular, monospace";
ctx.textAlign = "right";
ctx.textBaseline = "middle";

// 5 horizontal grid lines + price labels
for (let i = 0; i <= 4; i++) {
  const y = topPad + (i / 4) * chartH;
  const p = max - (i / 4) * (max - min);  // top = max
  ctx.beginPath();
  ctx.moveTo(xPad, y);
  ctx.lineTo(w - xPad, y);
  ctx.stroke();
  const decimals = p > 1000 ? 1 : p > 10 ? 2 : 4;
  ctx.fillText(p.toFixed(decimals), w - xPad - 2, y);
}

// 5 time axis labels
ctx.textAlign = "center";
ctx.textBaseline = "top";
for (let i = 0; i <= 4; i++) {
  const idx = Math.floor((i / 4) * (visible.length - 1));
  const c = visible[idx];
  if (!c) continue;
  const x = xScale(visibleFrom + idx);
  const d = new Date(c.ts);
  const lbl = `${d.getMonth() + 1}/${d.getDate()} ${d.getHours().toString().padStart(2, "0")}:${d.getMinutes().toString().padStart(2, "0")}`;
  ctx.fillText(lbl, x, h - bottomPad + 4);
}
```

Adaptive decimals on price labels: BTC at $67,432.10 doesn't need 4 decimal places; a small-cap altcoin does. The `p > 1000 ? 1 : p > 10 ? 2 : 4` heuristic is a good default.

## Trade markers as arrows

```ts
for (const m of markers) {
  if (m.ts < visible[0].ts || m.ts > visible[visible.length - 1].ts) continue;
  // Find nearest candle index by ts (markers rarely sit exactly on a candle)
  let idx = 0;
  for (let i = 0; i < visible.length; i++) {
    if (visible[i].ts <= m.ts) idx = i;
  }
  const x = xScale(visibleFrom + idx);
  const y = yScale(m.price);
  const color = m.side === "buy" ? "#22d3ee" : "#fb923c";
  ctx.strokeStyle = color;
  ctx.fillStyle = color;
  ctx.lineWidth = 1.5;

  // Triangular arrow above the price (sell) or below (buy)
  const sz = 6;
  ctx.beginPath();
  if (m.side === "buy") {
    ctx.moveTo(x, y + sz);
    ctx.lineTo(x - sz / 2, y + sz * 2);
    ctx.lineTo(x + sz / 2, y + sz * 2);
  } else {
    ctx.moveTo(x, y - sz);
    ctx.lineTo(x - sz / 2, y - sz * 2);
    ctx.lineTo(x + sz / 2, y - sz * 2);
  }
  ctx.closePath();
  ctx.fill();

  // P&L label next to the arrow
  if (m.pnl !== undefined) {
    ctx.fillStyle = m.pnl >= 0 ? "#86efac" : "#fda4af";
    ctx.font = "9px ui-monospace, SFMono-Regular, monospace";
    ctx.textAlign = "center";
    ctx.textBaseline = m.side === "buy" ? "top" : "bottom";
    const label = `${m.pnl >= 0 ? "+" : ""}$${m.pnl.toFixed(2)}`;
    const ly = m.side === "buy" ? y + sz * 2 + 2 : y - sz * 2 - 2;
    ctx.fillText(label, x, ly);
  }
}
```

Place the P&L label on the side opposite the arrow body so they don't overlap.

## Playback / scrub pattern

For a "play through time" UX, keep the chart windowed:

```tsx
const [windowTo, setWindowTo] = useState(candles.length);
const [playing, setPlaying] = useState(false);

useEffect(() => {
  if (!playing) return;
  const t = setInterval(() => {
    setWindowTo(prev => {
      const next = Math.min(prev + 2 * speed, candles.length);
      if (next >= candles.length) {
        setPlaying(false);
        return candles.length;
      }
      return next;
    });
  }, 250);
  return () => clearInterval(t);
}, [playing, speed, candles.length]);
```

The visible window grows from `windowFrom` to `windowTo`. Use two `<input type="range">` sliders to set both ends — one for the start, one for the end. This gives a "zoom" feel without a proper zoom implementation.

## Performance notes

- **Re-render is O(n) over visible candles** — keep the window reasonable (200-500 candles is the sweet spot)
- **Don't redraw on every mouse move** — only on `visibleFrom` / `visibleTo` changes
- **The useEffect dependency array matters** — list `[candles, markers, visibleFrom, visibleTo, height]` to avoid stale closures
- **Resize observer** — if the container width changes, you need a ResizeObserver to re-trigger the DPR setup:

```ts
useEffect(() => {
  const ro = new ResizeObserver(() => {
    // re-run the canvas setup
  });
  ro.observe(container);
  return () => ro.disconnect();
}, []);
```

For the basic version with a fixed-height container, a `useEffect` re-run on container ref change is enough.

## What this chart can't do

- No volume sub-pane (add it below the price chart as a separate `fillRect` per candle with `volume / maxVolume * height`)
- No MA/EMA overlays (compute the line in JS, draw as a `stroke()` series)
- No tooltips on hover (would need a hit-test pass + a separate DOM element)
- No pinch-zoom on mobile (would need touch handlers + a zoom scale state)

Add these only if you actually need them — the minimal version above is plenty for a "step through my trades" UX.

## Verify

```bash
# Page renders, canvas exists, JS loads
curl -s http://localhost:PORT/replay | grep -E "canvas|chart" | head

# Underlying data API returns candles
curl -s "http://localhost:PORT/api/market/klines?symbol=BTCUSDT&interval=60&days=30" | head -c 200

# Trades API for the same symbol
curl -s "http://localhost:PORT/api/trades?symbol=BTCUSDT&limit=5"
```

In the browser, you should see candles rendered with the trade count matching `markers.length`. If `markers.length === 0` but you have trades in the DB, the issue is the filter — usually a date-range mismatch between the trades `ts` and the candles `ts`.
