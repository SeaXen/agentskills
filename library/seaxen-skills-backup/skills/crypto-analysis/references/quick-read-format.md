# Crypto quick-read format

Use this as the default compact/readable layout when the user asks for a coin analysis without requesting a long report.

Start with the line: `This channel is for crypto analysis.`

## Order
1. Title: `**<COIN> quick read**`
2. Price, 24h change, market cap, 24h volume
3. Perp funding note when available
4. Spot check / exchange consensus when available
5. Relative valuation when available
6. Timeframe bias for 15m, 4h, 1d with indicator notes
7. Short read paragraph: what the trend means
8. Levels to watch: resistance and support
9. Verdict block: verdict, best setup, invalidation/reclaim notes, long/short trigger
10. Bias: technical bias, overall verdict, trading tilt, action, setup, confidence
11. Optional entry / stop / target / risk
12. Sources and links

## Style rules
- Keep it compact and chat-friendly.
- Use plain bullets, not tables.
- Prefer `~` for approximations.
- Explain funding in one short clause, not a long derivation.
- Summarize each timeframe as structure + key indicators + tilt.
- The verdict line should be a single line with the overall bias.
- If a section is unavailable, still keep the line and write `N/A` so the template stays 1:1.

## Example skeleton
```text
This channel is for crypto analysis.

**<COIN> quick read**
- Price: ~$...
- 24h change: ...%
- Market cap: ~$...
- 24h volume: ~$...
- Perp funding: ... (if available)
- Spot check: ... (if available)
- Relative valuation: ... (if available)

**Timeframe bias**
- 15m: ...
- 4h: ...
- 1d: ...

**Read**
- 1–3 short lines on trend / structure / risk

**Levels to watch**
- Resistance: ...
- Support: ...

**Bias**
- Technical bias: 15m ..., 4h ..., 1d ...
- Overall: LONG / SHORT / NEUTRAL
- Trading tilt: ...
- Action: BUY / SELL / HOLD
- Setup: SCALP / SWING / AUTO ...
- Confidence: ...%

Optional:
- Entry: ...
- Stop: ...
- Target: ...
- Risk: ...
- Sources: ...
- Links: ...
```