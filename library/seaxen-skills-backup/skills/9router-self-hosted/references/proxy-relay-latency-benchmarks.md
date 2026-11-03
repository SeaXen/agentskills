# Proxy Relay Latency Benchmarks

Measured 2026-07-06 from DietPi host (192.168.0.222) to bynara/mistral-medium-3-5.

## Relay Endpoint Ping (TCP/TLS, no API call)

3 runs each, after DNS warmup:

### Direct Bynara
```
Run 1: TOTAL 0.430s | TTFB 0.298s | CONNECT 0.011s
Run 2: TOTAL 0.983s | TTFB 0.480s | CONNECT 0.009s
Run 3: TOTAL 0.669s | TTFB 0.272s | CONNECT 0.009s
```

### Cloudflare Relay
```
Run 1: TOTAL 0.055s | TTFB 0.055s | CONNECT 0.010s
Run 2: TOTAL 0.047s | TTFB 0.046s | CONNECT 0.013s
Run 3: TOTAL 0.045s | TTFB 0.044s | CONNECT 0.010s
```
Fastest. No cold start. Consistent sub-50ms.

### Deno Relay
```
Run 1: TOTAL 0.519s | TTFB 0.519s | CONNECT 0.171s
Run 2: TOTAL 0.505s | TTFB 0.505s | CONNECT 0.169s
Run 3: TOTAL 0.505s | TTFB 0.505s | CONNECT 0.166s
```
Cold starts visible (~500ms). Consistent once warm.

### Vercel Relay
```
Run 1: TOTAL 1.477s | TTFB 1.475s | CONNECT 0.014s  ← cold start
Run 2: TOTAL 0.205s | TTFB 0.204s | CONNECT 0.015s
Run 3: TOTAL 0.173s | TTFB 0.170s | CONNECT 0.018s
```
Worst cold start (~1.5s). Warm ~184ms.

## Full API Call: bynara/mistral-medium-3-5 via OmniRoute

### Streaming ON (5 runs)

| Run | TTFB    | Total   | Relay latency (x-omniroute-latency-ms) |
|-----|---------|---------|----------------------------------------|
| 1   | 1.450s  | 1.614s  | 156ms                                  |
| 2   | 1.351s  | 1.524s  | 164ms                                  |
| 3   | 1.936s  | 2.130s  | 176ms                                  |
| 4   | 2.013s  | 2.579s  | 213ms                                  |
| 5   | 2.017s  | 4.161s  | 245ms                                  |

### Streaming OFF (2 runs)

| Run | TTFB    | Total   |
|-----|---------|---------|
| 1   | 6.085s  | 6.086s  |
| 2   | 7.091s  | 7.091s  |

### Non-streaming via OmniRoute (earlier test, 3 runs)

| Run | TTFB    | Total   |
|-----|---------|---------|
| 1   | 6.085s  | 6.086s  |
| 2   | 7.091s  | 7.091s  |
| 3   | 2.821s  | 2.821s  |

## Latency Breakdown

```
Total = OmniRoute overhead (~10-20ms, local LAN)
      + Relay hop (~156-245ms, OmniRoute's own measurement)
      + AI provider processing (~1.3-1.8s)
      ─────────────────────────────
      = ~1.5-2.5s with streaming ON
      = ~6-7s with streaming OFF
```

Relay overhead is ~10-15% of total response time. The AI model processing dominates.

## Recommendations

1. **Always use streaming** — 3-4x faster perceived latency
2. **Cloudflare as primary relay** — lowest latency, no cold starts
3. **Deno as backup** — reliable but slower
4. **Vercel only for IP diversity** — worst cold starts
5. **Keep relays warm** — ping every 5 min to prevent cold starts on Deno/Vercel
6. **Monitor `x-omniroute-latency-ms`** header for relay health

## Multi-Account Risk Assessment

| Scale | Risk | Notes |
|-------|------|-------|
| 1-2 extra accounts | Low | Nobody cares |
| 5-10 accounts | Medium | Pattern detection kicks in |
| 10+ accounts | High | Almost certainly flagged |

Linking vectors that get accounts banned together:
- Same GitHub OAuth
- Same email domain (user+1@gmail.com, user+2@gmail.com)
- Same credit card
- Same browser fingerprint
- Identical worker code deployed across accounts

Primary risk is AI provider banning API keys for rate limits, not platform banning accounts.
