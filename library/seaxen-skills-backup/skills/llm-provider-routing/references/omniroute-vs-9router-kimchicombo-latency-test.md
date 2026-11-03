# OmniRoute vs 9Router: kimchicombo Latency Test

## Test Setup
- **Date**: 2026-07-11
- **Endpoints**:
  - 9Router: `http://127.0.0.1:20111/v1`
  - OmniRoute: `http://127.0.0.1:20128/v1`
- **Model**: `kimchicombo`
- **Prompt**: `"Say OK."` (max_tokens: 5, stream: false)

## Results

### 9Router
- **Status**: `401 Unauthorized` (Missing/Invalid API key)
- **Auth Overhead**: ~6ms (TTFB: ~0.006s, Total: ~0.006s)
- **Note**: Cannot test model latency without valid API key

### OmniRoute
- **Status**: `200 OK`
- **Latency (3 runs)**:
  - Run 1: TTFB=7.446s, Total=7.446s
  - Run 2: TTFB=24.274s, Total=24.274s
  - Run 3: TTFB=0.627s, Total=0.627s
- **Average**: ~10.78s (high variance due to backend queueing/cold-start)

## Observations
1. **9Router requires API key** for `kimchicombo` — auth rejection is fast (~6ms)
2. **OmniRoute allows unauthenticated access** to `kimchicombo`
3. **OmniRoute latency is high and inconsistent** — suggests backend load or model cold-start
4. **No direct comparison possible** without 9Router API key

## Recommendations
- For **fair comparison**: Provide valid 9Router API key for `kimchicombo`
- For **router overhead test**: Use public free models (e.g., `kiro:gpt-4o-mini-free`)
- For **OmniRoute backend**: Investigate why `kimchicombo` shows queueing behavior

## Test Commands
```bash
# 9Router (needs valid key)
curl -s -X POST "http://127.0.0.1:20111/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_KEY" \
  -d '{"model": "kimchicombo", "messages": [{"role": "user", "content": "Say OK."}], "max_tokens": 5, "stream": false}' \
  -w "\nTTFB:%{time_starttransfer}s TOTAL:%{time_total}s\n"

# OmniRoute (works without key)
curl -s -X POST "http://127.0.0.1:20128/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -d '{"model": "kimchicombo", "messages": [{"role": "user", "content": "Say OK."}], "max_tokens": 5, "stream": false}' \
  -w "\nTTFB:%{time_starttransfer}s TOTAL:%{time_total}s\n"
```
