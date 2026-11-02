# Before this ships — 4 things engineering needs to build first

The sandbox only works if a visitor can run it with zero wait. Right now, keys take a day via email, which kills the "click and see it work" moment that's the entire point of embedding StackBlitz. Fix: ship one shared, heavily-throttled demo key baked into the sandbox, separate from real provisioned keys.

- **Create a public demo key** (e.g. `rtcl_test_public_demo`) scoped to a low per-IP rate limit (10–20 req/day is typical for this pattern). Real key issuance stays the manual email flow — the demo key just unblocks the sandbox.
- **Create the StackBlitz project** at `stackblitz.com/edit/reticule-quickstart` using the `index.html`/`index.js` below, then swap the placeholder URL in the embed.
- **Fill in the bracketed placeholders** (`{{...}}`) — API base URL, rate-limit numbers per tier, confidence-score thresholds. I don't have your real values, so I used realistic placeholders rather than inventing numbers and presenting them as fact.
- **Confirm the response shape** (`results[]`, `confidence`, `precision`) matches your actual API. I modeled a standard geocoding response; adjust field names to match reality before publishing.

Everything below this line is the actual page, ready to drop into your docs repo.

---

```markdown
---
title: Getting Started
description: Make your first geocoding call in under 2 minutes, then learn how auth and rate limits work before you integrate.
---

# Getting Started

Reticule turns an address into coordinates and a confidence score. This page gets you a working API call in about 2 minutes — no API key required yet — then covers what you need to know before you build on it: how authentication works and how rate limits are structured.

## Try it now

Edit the address below and hit **Geocode this address**. This sandbox runs on a shared demo key, so there's nothing to sign up for.

<iframe
  src="https://stackblitz.com/edit/reticule-quickstart?embed=1&file=index.js&hideNavigation=1&view=preview&ctl=1"
  style="width:100%; height:520px; border:0; border-radius:8px; overflow:hidden;"
  title="Reticule geocoding API sandbox"
  allow="accelerometer; camera; encrypted-media; geolocation; gyroscope; microphone; midi; payment"
  sandbox="allow-forms allow-modals allow-popups allow-presentation allow-same-origin allow-scripts">
</iframe>

You should see a JSON response with `latitude`, `longitude`, and `confidence`, plus a small map with a pin at the result. That's the whole API — one endpoint, one job.

> ℹ️ The sandbox above runs against a shared, rate-limited demo key. If it returns a 429, you've hit that shared limit, not a bug — see [Rate limits](#rate-limits) below, or run the same call with your own key using the steps below.

## What just happened

```json
{
  "query": "1600 Amphitheatre Parkway, Mountain View, CA",
  "results": [
    {
      "formatted_address": "1600 Amphitheatre Pkwy, Mountain View, CA 94043, USA",
      "latitude": 37.4224764,
      "longitude": -122.0842499,
      "confidence": 0.97,
      "precision": "rooftop"
    }
  ]
}
```

Two fields matter most:

- **`confidence`** — a 0–1 score for how sure we are the result is correct. Use it to decide whether to trust a result automatically or ask a human to confirm it:
  - `{{CONFIDENCE_HIGH_THRESHOLD}}` and above — safe to use directly (e.g. rooftop-level match).
  - `{{CONFIDENCE_MEDIUM_THRESHOLD}}`–`{{CONFIDENCE_HIGH_THRESHOLD}}` — usually correct, worth a lightweight confirmation step for anything high-stakes (billing, shipping).
  - Below `{{CONFIDENCE_MEDIUM_THRESHOLD}}` — treat as a guess (street- or city-level only). Don't auto-commit to it.
- **`precision`** — what kind of match produced the result (`rooftop`, `street`, `city`, ...). Confidence tells you *how sure*; precision tells you *how exact*.

## Get your own API key

Reticule keys aren't self-serve yet — every key is provisioned by hand.

1. Email **{{SALES_EMAIL}}** with your company name, what you're building, and your expected request volume.
2. We provision a sandbox tenant and send you a key, usually the next business day.
3. Your sandbox key looks like `rtcl_test_...` — every call against it behaves identically to production, just under sandbox rate limits (see below).

There's no waitlist form or dashboard signup yet — email is the whole flow. If you're just evaluating the API, the sandbox above already got you a real response; you only need your own key once you're ready to integrate.

## Make the call yourself

Once you have a key, swap it in wherever `YOUR_API_KEY` appears below.

**curl**

```bash
curl -X POST {{API_BASE_URL}}/geocode \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"address": "1600 Amphitheatre Parkway, Mountain View, CA"}'
```

**Node.js**

```javascript
const response = await fetch("{{API_BASE_URL}}/geocode", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${process.env.RETICULE_API_KEY}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    address: "1600 Amphitheatre Parkway, Mountain View, CA",
  }),
});

const data = await response.json();
console.log(data.results[0]);
```

**Python**

```python
import os
import requests

response = requests.post(
    "{{API_BASE_URL}}/geocode",
    headers={"Authorization": f"Bearer {os.environ['RETICULE_API_KEY']}"},
    json={"address": "1600 Amphitheatre Parkway, Mountain View, CA"},
)
print(response.json()["results"][0])
```

Keep the key out of client-side code and out of source control — if a key does leak, email {{SALES_EMAIL}} and we'll rotate it.

## How authentication works

- Every request needs `Authorization: Bearer <key>`. There's no query-param or basic-auth option.
- Keys are prefixed by environment: `rtcl_test_...` for sandbox tenants, `rtcl_live_...` for production. Both use the same endpoint and request shape — only the rate limits and billing differ.
- A key belongs to your tenant, not to an individual person. Anyone on your team can use it; if someone leaves, ask us to rotate it rather than sharing it further.
- There's currently one key per tenant — no per-environment or per-service key scoping yet. If you need to isolate a key to one service, mention it in your provisioning email.

## Rate limits

Every tier gets a per-second cap and a daily cap. Both are enforced per key.

| Tier | Requests/sec | Daily cap | Who it's for |
|---|---|---|---|
| Sandbox (default on every new key) | {{SANDBOX_RPS}}/sec | {{SANDBOX_DAILY}}/day | Evaluation and the sandbox above |
| Starter | {{STARTER_RPS}}/sec | {{STARTER_DAILY}}/day | Small production workloads |
| Growth | {{GROWTH_RPS}}/sec | {{GROWTH_DAILY}}/day | Higher-volume production |
| Enterprise | Custom | Custom | Contact {{SALES_EMAIL}} |

Every response includes headers so you can track where you stand without guessing:

```
X-RateLimit-Limit: {{SANDBOX_RPS}}
X-RateLimit-Remaining: 4
X-RateLimit-Reset: 1732000000
```

If you go over, you get a `429` with a `Retry-After` header (seconds until you can try again):

```json
{
  "error": "rate_limit_exceeded",
  "message": "You've exceeded your rate limit for this tier.",
  "retry_after": 12
}
```

Back off and retry after that window — don't tighten a polling loop against a 429, it'll just compound.

## Common errors

| Status | Meaning | Fix |
|---|---|---|
| 401 | Missing or invalid `Authorization` header | Check the key is present and prefixed correctly (`rtcl_test_` / `rtcl_live_`) |
| 422 | `address` missing or unparseable | Make sure `address` is a non-empty string in the JSON body |
| 429 | Rate limit exceeded | Read `Retry-After` and back off; consider a higher tier |
| 500 | Something broke on our end | Retry with backoff; email {{SALES_EMAIL}} if it persists |

## Next steps

- Read the full [API reference]({{API_REFERENCE_URL}}) for every field in the response.
- Ready for a production key? Email {{SALES_EMAIL}} — see [Get your own API key](#get-your-own-api-key).
- Questions or stuck? Email {{SUPPORT_EMAIL}}.
```

---

**StackBlitz project contents** (create at `stackblitz.com/edit/reticule-quickstart`, vanilla JS template):

`index.html`

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Reticule sandbox</title>
    <style>
      body { font-family: -apple-system, system-ui, sans-serif; max-width: 560px; margin: 24px auto; padding: 0 16px; }
      input { width: 100%; padding: 10px; font-size: 16px; box-sizing: border-box; }
      button { margin-top: 10px; padding: 10px 16px; font-size: 16px; cursor: pointer; }
      pre { background: #0f172a; color: #e2e8f0; padding: 16px; border-radius: 8px; overflow: auto; font-size: 13px; }
      iframe#map { width: 100%; height: 220px; border: 0; border-radius: 8px; margin-top: 12px; display: none; }
    </style>
  </head>
  <body>
    <h2>Try Reticule</h2>
    <input id="address" value="1600 Amphitheatre Parkway, Mountain View, CA" />
    <button id="go">Geocode this address</button>
    <pre id="output">// Response will show up here</pre>
    <iframe id="map"></iframe>
    <script type="module" src="index.js"></script>
  </body>
</html>
```

`index.js`

```javascript
// Shared, heavily rate-limited — for sandbox use only. Never use in real integrations.
const DEMO_API_KEY = "rtcl_test_public_demo";
const API_BASE = "{{API_BASE_URL}}";

const button = document.getElementById("go");
const output = document.getElementById("output");
const map = document.getElementById("map");

button.addEventListener("click", async () => {
  const address = document.getElementById("address").value;
  output.textContent = "Loading...";
  map.style.display = "none";

  const response = await fetch(`${API_BASE}/geocode`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${DEMO_API_KEY}`,
    },
    body: JSON.stringify({ address }),
  });

  const data = await response.json();
  output.textContent = JSON.stringify(data, null, 2);

  if (!response.ok) return;

  const top = data.results[0];
  if (top) {
    const { latitude, longitude } = top;
    const delta = 0.01;
    const bbox = [longitude - delta, latitude - delta, longitude + delta, latitude + delta].join(",");
    map.src = `https://www.openstreetmap.org/export/embed.html?bbox=${bbox}&marker=${latitude},${longitude}`;
    map.style.display = "block";
  }
});
```

The map uses OpenStreetMap's public embed endpoint — no map API key needed, which keeps the sandbox self-contained.