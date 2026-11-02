# `README.md` — cinderpath/relaykit

```markdown
<div align="center">
  <h1>RelayKit</h1>
  <p><strong>Send events from your app to any destination — webhooks, queues, or other services — with delivery guarantees, retries, and signature verification built in.</strong></p>

  <a href="https://github.com/cinderpath/relaykit/actions"><img src="https://github.com/cinderpath/relaykit/workflows/CI/badge.svg" alt="CI"></a>
  <a href="https://www.npmjs.com/package/@cinderpath/relaykit"><img src="https://img.shields.io/npm/v/@cinderpath/relaykit.svg" alt="npm version"></a>
  <a href="https://github.com/cinderpath/relaykit/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
  <a href="https://discord.gg/cinderpath"><img src="https://img.shields.io/discord/000000000?color=7289da&logo=discord&logoColor=white" alt="Discord"></a>

  <br><br>

  <a href="#table-of-contents">Docs index</a> •
  <a href="#quickstart-first-call-in-5-minutes">Quickstart</a> •
  <a href="#contributing">Contributing</a> •
  <a href="https://discord.gg/cinderpath">Discord</a>
</div>

---

## What is RelayKit?

RelayKit is a Node SDK for **relaying events out of your application**, reliably. Instead of writing your own retry logic, signature scheme, and delivery bookkeeping every time you need to notify another service, you call `relay.events.send()` and RelayKit handles delivery, retries, and confirmation.

- **Reliable delivery** — automatic retries with exponential backoff, dead-letter after N attempts.
- **Verifiable webhooks** — every inbound delivery is signed; verify it in one line.
- **Idempotent by default** — safe to retry a `send()` call without double-delivering.
- **Sandbox included** — a free sandbox key that behaves exactly like production, at 1/10th the traffic limit, so you never test against real data.

This README is the only document you need to go from `npm install` to a verified, production-ready integration. Everything else — API reference, guides, recipes — is indexed below and linked from here, so you never have to guess which of the docs site's 140 pages you actually need.

---

## Table of Contents

- [What is RelayKit?](#what-is-relaykit)
- [Quickstart: first call in 5 minutes](#quickstart-first-call-in-5-minutes)
- [Tutorial: a real integration, step by step](#tutorial-a-real-integration-step-by-step)
  - [Step 1 — Install and authenticate](#step-1--install-and-authenticate)
  - [Step 2 — Send your first event](#step-2--send-your-first-event)
  - [Step 3 — Receive and verify a delivery](#step-3--receive-and-verify-a-delivery)
  - [Step 4 — Handle errors and retries](#step-4--handle-errors-and-retries)
  - [Step 5 — Make it production-ready](#step-5--make-it-production-ready)
  - [Complete code](#complete-code)
- [Troubleshooting](#troubleshooting)
- [Full documentation index](#full-documentation-index)
- [Contributing](#contributing)
- [Support](#support)
- [License](#license)

---

## Quickstart: first call in 5 minutes

### Prerequisites

| Requirement | Version | Check |
|---|---|---|
| Node.js | 18+ | `node --version` |
| npm | 9+ | `npm --version` |
| RelayKit account | any (free) | [cinderpath.com/signup](https://cinderpath.com/signup) |

You'll be comfortable with this guide if you know basic async/await and have made an HTTP call from Node before. Nothing else is assumed.

### 1. Install

```bash
npm install @cinderpath/relaykit
```

### 2. Get a sandbox key

Every new account gets a sandbox key on signup — no card, no approval wait. Find it at **Dashboard → API Keys → Sandbox**. It looks like `rk_sandbox_...`.

Put it in `.env`:

```bash
RELAYKIT_API_KEY=rk_sandbox_xxxxxxxxxxxxxxxx
```

### 3. Send your first event

Create `index.js`:

```javascript
require('dotenv').config();
const { RelayKit } = require('@cinderpath/relaykit');

const relay = new RelayKit({ apiKey: process.env.RELAYKIT_API_KEY });

async function main() {
  const receipt = await relay.events.send({
    type: 'order.created',
    payload: { orderId: '1234', amount: 4200 },
    destination: 'https://webhook.site/your-unique-url', // swap for your own endpoint later
  });

  console.log(receipt);
}

main();
```

### 4. Run it

```bash
node index.js
```

Expected output:

```json
{
  "id": "evt_01HZY3QK7X",
  "status": "delivered",
  "attempts": 1,
  "destination": "https://webhook.site/your-unique-url"
}
```

🎉 **That's a working call.** You sent an event, RelayKit delivered it, and you have a receipt proving it. Everything past this point is about receiving that event yourself and hardening the integration — it does not require re-learning anything new.

If you didn't see `"status": "delivered"`, jump to [Troubleshooting](#troubleshooting) before continuing.

---

## Tutorial: a real integration, step by step

The quickstart proved the SDK works. This section builds the integration you'll actually ship: receiving events in your own service, verifying they're genuine, handling failures, and configuring it for production.

### Step 1 — Install and authenticate

Already done above if you followed the quickstart. Two things worth understanding now, because they're the #1 and #2 cause of first-week confusion:

- **Sandbox and production keys are not interchangeable.** A `rk_sandbox_...` key only delivers to destinations you've allow-listed in the sandbox dashboard. A `rk_live_...` key delivers anywhere. Mixing them up is the most common cause of "it worked yesterday, now it silently does nothing."
- **The client is stateless and reusable.** Create one `RelayKit` instance per process (e.g. at module load), not one per request.

```javascript
// relay-client.js — create once, import everywhere
const { RelayKit } = require('@cinderpath/relaykit');

module.exports = new RelayKit({
  apiKey: process.env.RELAYKIT_API_KEY,
});
```

### Step 2 — Send your first event

You already did this in the quickstart. The one addition worth making now is an **idempotency key**, so retried calls (from a crashed process, a retried HTTP handler, etc.) never create a duplicate delivery:

```javascript
const receipt = await relay.events.send({
  type: 'order.created',
  payload: { orderId: '1234', amount: 4200 },
  destination: 'https://api.yourapp.com/webhooks/relaykit',
  idempotencyKey: `order-created-1234`, // same key = same event, no duplicate
});
```

**Checkpoint:** run it twice with the same `idempotencyKey`. You should get back the *same* `receipt.id` both times, with `attempts` unchanged on the second call.

### Step 3 — Receive and verify a delivery

RelayKit delivers by POSTing to the `destination` URL you specified. In development, that URL has to be reachable from the internet — use a tunnel:

```bash
npx ngrok http 3000
```

Set up a receiver with Express:

```javascript
// server.js
const express = require('express');
const { verifyWebhook } = require('@cinderpath/relaykit');

const app = express();

// IMPORTANT: RelayKit signs the raw body. Do not use express.json() on this
// route — it re-serializes the body and breaks signature verification.
app.post(
  '/webhooks/relaykit',
  express.raw({ type: 'application/json' }),
  (req, res) => {
    const signature = req.headers['relaykit-signature'];

    const isValid = verifyWebhook({
      payload: req.body, // raw Buffer
      signature,
      secret: process.env.RELAYKIT_WEBHOOK_SECRET,
    });

    if (!isValid) {
      return res.status(401).send('invalid signature');
    }

    const event = JSON.parse(req.body);
    console.log('Received verified event:', event.type, event.payload);

    res.status(200).send('ok');
  }
);

app.listen(3000, () => console.log('Listening on http://localhost:3000'));
```

Point your ngrok URL + `/webhooks/relaykit` at the `destination` field from Step 2, resend the event, and watch it arrive.

**Checkpoint:** your server logs `Received verified event: order.created {...}`, and RelayKit's dashboard shows the delivery as `200 OK`.

⚠️ **The single most common integration bug**: applying a body-parsing middleware (`express.json()`) globally, before the RelayKit route. That mutates the raw body RelayKit signed, so every signature check fails with a generic `401`. Use `express.raw()` scoped to this one route, as shown above.

### Step 4 — Handle errors and retries

`relay.events.send()` throws a typed `RelayKitError` on failure. Handle the ones you'll actually hit:

```javascript
const { RelayKitError } = require('@cinderpath/relaykit');

try {
  await relay.events.send({ type: 'order.created', payload, destination });
} catch (err) {
  if (err instanceof RelayKitError) {
    switch (err.code) {
      case 'invalid_api_key':
        // Wrong key, or a sandbox key hitting a non-allow-listed destination.
        throw err;
      case 'rate_limited':
        // err.retryAfterMs tells you how long to wait.
        break;
      case 'destination_unreachable':
        // RelayKit already retried internally and gave up; payload is safe
        // in the dashboard's dead-letter view for manual replay.
        break;
      default:
        throw err;
    }
  } else {
    throw err;
  }
}
```

You don't need to implement your own retry loop for transient failures — RelayKit retries internally with backoff before it ever throws `destination_unreachable`. Only handle the terminal states.

### Step 5 — Make it production-ready

```javascript
const relay = new RelayKit({
  apiKey: process.env.RELAYKIT_API_KEY,
  timeoutMs: 10_000,        // default is 30s; tighten if you call synchronously from a request handler
  maxRetries: 5,            // default is 3
  logger: console,          // pass your structured logger (pino, winston) instead of console in prod
});
```

Before going live:

- [ ] Swap `rk_sandbox_...` for `rk_live_...` via environment-specific `.env` files, never hardcoded.
- [ ] Store `RELAYKIT_WEBHOOK_SECRET` in your secrets manager, not `.env` in prod.
- [ ] Confirm your receiver endpoint is on HTTPS — RelayKit refuses to deliver to plain HTTP in production mode.
- [ ] Set an alert on the dashboard's dead-letter queue so failed deliveries don't go unnoticed.

### Complete code

```javascript
// relay-client.js
const { RelayKit } = require('@cinderpath/relaykit');

module.exports = new RelayKit({
  apiKey: process.env.RELAYKIT_API_KEY,
  timeoutMs: 10_000,
  maxRetries: 5,
});
```

```javascript
// send-order-event.js
const relay = require('./relay-client');
const { RelayKitError } = require('@cinderpath/relaykit');

async function sendOrderCreated(order) {
  try {
    return await relay.events.send({
      type: 'order.created',
      payload: { orderId: order.id, amount: order.amount },
      destination: process.env.RELAYKIT_DESTINATION_URL,
      idempotencyKey: `order-created-${order.id}`,
    });
  } catch (err) {
    if (err instanceof RelayKitError && err.code === 'rate_limited') {
      await new Promise((r) => setTimeout(r, err.retryAfterMs));
      return sendOrderCreated(order);
    }
    throw err;
  }
}

module.exports = { sendOrderCreated };
```

```javascript
// server.js
const express = require('express');
const { verifyWebhook } = require('@cinderpath/relaykit');

const app = express();

app.post(
  '/webhooks/relaykit',
  express.raw({ type: 'application/json' }),
  (req, res) => {
    const isValid = verifyWebhook({
      payload: req.body,
      signature: req.headers['relaykit-signature'],
      secret: process.env.RELAYKIT_WEBHOOK_SECRET,
    });

    if (!isValid) return res.status(401).send('invalid signature');

    const event = JSON.parse(req.body);
    console.log('Received verified event:', event.type, event.payload);
    res.status(200).send('ok');
  }
);

app.listen(3000, () => console.log('Listening on http://localhost:3000'));
```

---

## Troubleshooting

### `invalid_api_key` even though the key looks right

**Cause:** almost always a sandbox key (`rk_sandbox_...`) targeting a `destination` that isn't on the sandbox allow-list, which RelayKit reports as an auth error rather than a destination error.
**Fix:** add the destination in **Dashboard → Sandbox → Allowed Destinations**, or switch to a live key if you're actually in production.

### Signature verification always fails (`401` on every delivery)

**Cause:** a body-parsing middleware (`express.json()`, `body-parser`) applied ahead of the RelayKit route re-serializes the body before you can verify it against the raw bytes RelayKit signed.
**Fix:** use `express.raw({ type: 'application/json' })` scoped to only the RelayKit route, as shown in [Step 3](#step-3--receive-and-verify-a-delivery). Verify before you `JSON.parse`.

### Nothing arrives at my local server

**Cause:** `destination` has to be reachable from the public internet; `localhost:3000` is not.
**Fix:** tunnel it first (`npx ngrok http 3000`) and use the `https://...ngrok...` URL as your destination while developing.

### `ECONNREFUSED` or timeouts calling `relay.events.send()`

**Cause:** usually a corporate proxy or firewall blocking outbound HTTPS to `api.relaykit.dev`.
**Fix:** confirm with `curl -I https://api.relaykit.dev/health`. If that also hangs, it's network policy, not the SDK — check with your infra team before filing an issue.

### `destination_unreachable` after it used to work

**Cause:** RelayKit retried internally (default: 3 attempts, exponential backoff) and your endpoint never returned `2xx`.
**Fix:** check **Dashboard → Deliveries → Dead Letter** for the exact response your server sent back on each attempt — the full response body and status are logged there, so you don't need to reproduce it locally.

### `SyntaxError: Cannot use import statement outside a module`

**Cause:** RelayKit ships both CJS and ESM builds; your `package.json` doesn't declare `"type": "module"` but your code uses `import`.
**Fix:** either add `"type": "module"` to `package.json`, or use `require('@cinderpath/relaykit')` (all examples above use this form deliberately, so they run unmodified either way).

---

## Full documentation index

The docs site groups every page under one of these ten sections. If you're looking for something, it's under one of these — nothing on the site lives outside this structure.

1. **Getting Started**
   - [Installation](https://docs.relaykit.dev/getting-started/installation)
   - [Authentication & API keys](https://docs.relaykit.dev/getting-started/authentication)
   - [Sandbox vs. production](https://docs.relaykit.dev/getting-started/environments)
   - [This tutorial, expanded](https://docs.relaykit.dev/getting-started/tutorial)

2. **Core Concepts**
   - [Events](https://docs.relaykit.dev/concepts/events)
   - [Destinations](https://docs.relaykit.dev/concepts/destinations)
   - [Delivery guarantees & retries](https://docs.relaykit.dev/concepts/delivery-guarantees)
   - [Idempotency](https://docs.relaykit.dev/concepts/idempotency)

3. **Sending Events**
   - [`events.send()` reference](https://docs.relaykit.dev/sending/send)
   - [Batching](https://docs.relaykit.dev/sending/batching)
   - [Scheduling future delivery](https://docs.relaykit.dev/sending/scheduling)
   - [Rate limits](https://docs.relaykit.dev/sending/rate-limits)

4. **Receiving & Webhooks**
   - [Verifying signatures](https://docs.relaykit.dev/webhooks/verifying-signatures)
   - [Framework recipes](https://docs.relaykit.dev/webhooks/frameworks) — Express, Fastify, Next.js, Koa
   - [Replaying failed deliveries](https://docs.relaykit.dev/webhooks/replay)
   - [Testing webhooks locally](https://docs.relaykit.dev/webhooks/local-testing)

5. **SDKs & Client Libraries**
   - [Node.js SDK reference](https://docs.relaykit.dev/sdks/node) *(this repo)*
   - [Python SDK](https://docs.relaykit.dev/sdks/python)
   - [Go SDK](https://docs.relaykit.dev/sdks/go)
   - [REST API (no SDK)](https://docs.relaykit.dev/sdks/rest)

6. **API Reference**
   - [Full endpoint reference](https://docs.relaykit.dev/api-reference)
   - [Error codes](https://docs.relaykit.dev/api-reference/errors)
   - [Pagination & filtering](https://docs.relaykit.dev/api-reference/pagination)

7. **Guides & Recipes**
   - [Migrating from raw webhooks](https://docs.relaykit.dev/guides/migrating-from-raw-webhooks)
   - [Multi-tenant destination routing](https://docs.relaykit.dev/guides/multi-tenant-routing)
   - [Zero-downtime key rotation](https://docs.relaykit.dev/guides/key-rotation)

8. **Observability & Operations**
   - [Dashboard overview](https://docs.relaykit.dev/operations/dashboard)
   - [Dead-letter queue](https://docs.relaykit.dev/operations/dead-letter-queue)
   - [Alerts & monitoring](https://docs.relaykit.dev/operations/alerts)
   - [SLA & status page](https://docs.relaykit.dev/operations/status)

9. **Errors & Troubleshooting**
   - [Common errors](https://docs.relaykit.dev/troubleshooting/common-errors) *(mirrors this README's Troubleshooting section, kept in sync)*
   - [Debugging delivery failures](https://docs.relaykit.dev/troubleshooting/delivery-failures)

10. **Changelog & Migration**
    - [Changelog](https://docs.relaykit.dev/changelog)
    - [Breaking-change migration guides](https://docs.relaykit.dev/migrations)

---

## Contributing

We want PRs, not just issues. Here's the entire process — no separate document to go dig up.

### Before you write code

- Check [open issues](https://github.com/cinderpath/relaykit/issues) for something labeled **`good first issue`** if you're new to the codebase.
- For anything larger than a typo or a bugfix, open an issue first describing the change. We'd rather redirect you before you write code than after.

### Local setup

```bash
git clone https://github.com/cinderpath/relaykit.git
cd relaykit
npm install
npm test          # should pass on a clean checkout, no config needed
```

No API keys, no Docker, no external service required to run the test suite — it runs entirely against a mocked transport layer.

### Making a change

1. Branch off `main`: `git checkout -b fix/short-description`.
2. Write the fix or feature, plus a test. PRs without a test for the behavior they change are asked to add one, not merged as-is.
3. Run the full check before pushing:
   ```bash
   npm run lint && npm run typecheck && npm test
   ```
4. Commit using [Conventional Commits](https://www.conventionalcommits.org/): `fix: correct retry backoff calculation`, `feat: add batch send support`.

### Opening the PR

- Fill in the PR template — it asks for what changed and why, not a novel.
- Link the issue it resolves (`Fixes #123`) if there is one.
- One logical change per PR. A bugfix and an unrelated refactor in the same PR will be asked to split.

### What happens after you open it

- A maintainer reviews within **2 business days** — if that doesn't happen, ping the PR, that's on us.
- CI must pass (lint, typecheck, test, build) before merge.
- We merge with squash, so your commit history inside the branch can be messy; the PR title becomes the final commit message, so make that one good.

### Code of conduct

Covered by our [Code of Conduct](https://github.com/cinderpath/relaykit/blob/main/CODE_OF_CONDUCT.md). Short version: be respectful, assume good faith, no harassment.

---

## Support

- **Bugs & feature requests:** [GitHub Issues](https://github.com/cinderpath/relaykit/issues)
- **Questions & discussion:** [Discord](https://discord.gg/cinderpath)
- **Security issues:** email `security@cinderpath.com` — do not open a public issue for vulnerabilities.

## License

MIT © [Cinderpath](https://cinderpath.com)
```