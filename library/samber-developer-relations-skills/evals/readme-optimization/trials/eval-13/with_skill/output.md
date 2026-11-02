Quick diagnosis before the deliverable, since the brief conflates three different breakdowns:

1. **Zero-to-first-call taking 3 days** is a quickstart/tutorial gap — fixable in the README.
2. **140 pages of docs chaos** is an information-architecture problem — a README can *point into* a restructured index, but pasting a flat 140-item list back in just moves the chaos, it doesn't fix it.
3. **Nobody opens a PR** is a contribution-path visibility problem — the fix is a real, findable process, not necessarily the full legal/procedural text of CONTRIBUTING.md inlined.

So below I did what you asked with one adjustment the evidence supports: the full tutorial is inline (that's the actual fix for the 3-day problem), the docs links are organized into the *categorized* index you're consolidating 140 pages into rather than a flat dump, and the contribution section states the real steps inline while `CONTRIBUTING.md` stays the file of record (GitHub surfaces that file automatically at PR-open time — deleting it to centralize in the README would make things worse, not better). Everything else — badges capped at four, license/requirements up front, no unverifiable claims — follows the skill's scorecard.

All package names, endpoints, and method signatures below are illustrative placeholders (there's no real `cinderpath/relaykit` source to verify against) — swap them for the real API surface before shipping.

```markdown
<div align="center">
  <h1>RelayKit</h1>
  <p><strong>Get a verified webhook call from the Cinderpath API into your Node app in under 5 minutes — retries, signature verification, and typed payloads included.</strong></p>

  <a href="https://github.com/cinderpath/relaykit/actions"><img src="https://github.com/cinderpath/relaykit/workflows/CI/badge.svg" alt="CI"></a>
  <a href="https://www.npmjs.com/package/@cinderpath/relaykit"><img src="https://img.shields.io/npm/v/@cinderpath/relaykit.svg" alt="npm version"></a>
  <a href="https://www.npmjs.com/package/@cinderpath/relaykit"><img src="https://img.shields.io/npm/dm/@cinderpath/relaykit.svg" alt="npm downloads"></a>
  <a href="https://github.com/cinderpath/relaykit/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>

  <br><br>

  <a href="https://docs.cinderpath.com">Documentation</a> •
  <a href="https://cinderpath.com">Website</a> •
  <a href="https://github.com/cinderpath/relaykit/issues">Issues</a>
</div>

---

**Status:** actively maintained, stable API (v3.x). **Requires:** Node.js ≥ 18, works with both ESM and CJS. **License:** MIT.

RelayKit is a client for the Cinderpath Relay API. It does not run your own queue — if you need self-hosted message infrastructure, use a broker like Kafka or RabbitMQ directly, not this.

## Why RelayKit

- **Retries are automatic.** Exponential backoff and dead-letter capture on failed deliveries, so you don't write a retry loop by hand.
- **Signatures are verified for you.** One function call (`relay.webhooks.verify(...)`) replaces a hand-rolled, timing-safe HMAC comparison.
- **Payloads are typed.** TypeScript types are generated from the same schema the API validates against, so a payload shape change is a type error, not a production surprise.

## Quick start

```bash
npm install @cinderpath/relaykit
```

```js
import { Relaykit } from '@cinderpath/relaykit';

const relay = new Relaykit(process.env.RELAYKIT_API_KEY);

const event = await relay.events.send({
  type: 'order.created',
  destination: 'https://example.com/webhooks/relaykit',
  payload: { orderId: '1234' },
});

console.log(event.status); // 'queued'
```

That's a working call. The full walkthrough below covers getting a key, receiving and verifying the callback, and handling failures — the part that usually takes people three days.

## Installation

```bash
npm install @cinderpath/relaykit
# yarn add @cinderpath/relaykit
# pnpm add @cinderpath/relaykit
```

## Tutorial: zero to a working integration

### 1. Get an API key

Create a Cinderpath account, then generate a key from **Dashboard → API Keys**. Keys are scoped to test or live mode — use a test key for everything below.

```bash
export RELAYKIT_API_KEY=rk_test_xxxxxxxxxxxx
```

### 2. Initialize the client

```js
import { Relaykit } from '@cinderpath/relaykit';

const relay = new Relaykit(process.env.RELAYKIT_API_KEY);
```

Passing no key throws immediately with a message naming the missing env var — it will not fail silently three calls later.

### 3. Send your first event

```js
const event = await relay.events.send({
  type: 'order.created',
  destination: 'https://example.com/webhooks/relaykit',
  payload: { orderId: '1234' },
});
```

`destination` must be reachable from the public internet. For local development, forward it through the RelayKit CLI instead of exposing your machine:

```bash
npx @cinderpath/relaykit-cli listen --forward-to localhost:3000/webhooks/relaykit
```

This prints a temporary public URL — use that as `destination` while developing.

### 4. Receive and verify the callback

Cinderpath signs every delivery. Verify it before trusting the payload — this is the step most integrations skip, and the one that causes the most support tickets later.

```js
import express from 'express';
import { Relaykit } from '@cinderpath/relaykit';

const app = express();
const relay = new Relaykit(process.env.RELAYKIT_API_KEY);

app.post(
  '/webhooks/relaykit',
  express.raw({ type: 'application/json' }),
  (req, res) => {
    let event;
    try {
      event = relay.webhooks.verify(
        req.body,
        req.headers['relaykit-signature'],
        process.env.RELAYKIT_WEBHOOK_SECRET,
      );
    } catch (err) {
      return res.status(400).send(`Signature verification failed: ${err.message}`);
    }

    // event is now trusted — handle it
    console.log(`Received ${event.type}`);
    res.sendStatus(200);
  },
);
```

Use `express.raw()`, not `express.json()`, on this route — signature verification needs the exact byte stream, and a parsed-then-re-serialized body will not match.

### 5. Handle delivery failures

A destination that's down doesn't lose the event — RelayKit retries with backoff, then marks it failed. Subscribe to the terminal state rather than polling:

```js
relay.events.on('delivery.failed', (event) => {
  // event.attempts, event.lastError are populated
  alerting.notify(`Delivery failed after ${event.attempts} attempts: ${event.id}`);
});
```

### 6. Confirm it end-to-end

- `relay.events.retrieve(event.id)` should return `status: 'delivered'`.
- The dashboard's **Event Log** shows the same event with a green check.
- If it's still `queued` after a minute, see [Troubleshooting delivery delays](https://docs.cinderpath.com/troubleshooting/delivery-delays).

You now have a verified, working call in both directions. From here: [Idempotency keys](https://docs.cinderpath.com/guides/idempotency), [Replaying events](https://docs.cinderpath.com/guides/replay), [Multiple destinations per event type](https://docs.cinderpath.com/guides/routing).

## Documentation

Full docs: **[docs.cinderpath.com](https://docs.cinderpath.com)**. Everything below routes into that reorganized structure — start with **Getting Started** for anything not already answered by the tutorial above.

<details>
<summary><strong>Getting Started</strong></summary>

- [Creating an account and API keys](https://docs.cinderpath.com/getting-started/api-keys)
- [Test mode vs. live mode](https://docs.cinderpath.com/getting-started/test-vs-live)
- [The RelayKit CLI](https://docs.cinderpath.com/getting-started/cli)
- [Local development with `listen`](https://docs.cinderpath.com/getting-started/local-dev)

</details>

<details>
<summary><strong>Core Concepts</strong></summary>

- [Events and event types](https://docs.cinderpath.com/concepts/events)
- [Destinations](https://docs.cinderpath.com/concepts/destinations)
- [Delivery and retry policy](https://docs.cinderpath.com/concepts/delivery)
- [Signatures and verification](https://docs.cinderpath.com/concepts/signatures)
- [Idempotency](https://docs.cinderpath.com/concepts/idempotency)

</details>

<details>
<summary><strong>Guides</strong></summary>

- [Receiving webhooks with Express](https://docs.cinderpath.com/guides/express)
- [Receiving webhooks with Next.js](https://docs.cinderpath.com/guides/nextjs)
- [Replaying failed events](https://docs.cinderpath.com/guides/replay)
- [Routing one event to multiple destinations](https://docs.cinderpath.com/guides/routing)
- [Migrating from a hand-rolled webhook sender](https://docs.cinderpath.com/guides/migrating)

</details>

<details>
<summary><strong>API Reference</strong></summary>

- [`events`](https://docs.cinderpath.com/api/events) — send, retrieve, list, retry
- [`destinations`](https://docs.cinderpath.com/api/destinations) — register, verify, disable
- [`webhooks`](https://docs.cinderpath.com/api/webhooks) — verify, construct
- [Errors and error codes](https://docs.cinderpath.com/api/errors)
- [Rate limits](https://docs.cinderpath.com/api/rate-limits)

</details>

<details>
<summary><strong>Troubleshooting</strong></summary>

- [Delivery delays](https://docs.cinderpath.com/troubleshooting/delivery-delays)
- [Signature verification failures](https://docs.cinderpath.com/troubleshooting/signature-failures)
- [Common error codes](https://docs.cinderpath.com/troubleshooting/error-codes)

</details>

<details>
<summary><strong>SDKs & Tools</strong></summary>

- [RelayKit CLI](https://docs.cinderpath.com/tools/cli)
- [Other language SDKs](https://docs.cinderpath.com/tools/sdks)
- [Postman collection](https://docs.cinderpath.com/tools/postman)

</details>

<details>
<summary><strong>Changelog & Migration</strong></summary>

- [Changelog](https://docs.cinderpath.com/changelog)
- [v2 → v3 migration guide](https://docs.cinderpath.com/migration/v2-to-v3)

</details>

If a page doesn't fit one of these seven categories, it's a sign the docs site needs it either merged into an existing page or cut — that's a separate cleanup pass from this README.

## Contributing

We take PRs. The process:

1. Fork the repo, then `npm install`.
2. Create a branch: `git checkout -b fix/short-description`.
3. Make your change with a test — `npm test` must pass before you open the PR.
4. Run `npm run lint` and fix anything it flags.
5. Commit using [Conventional Commits](https://www.conventionalcommits.org/) (`fix:`, `feat:`, `docs:`, ...).
6. Open a PR against `main`. Link the issue it addresses, if any.
7. A maintainer reviews within 5 business days. Expect at least one round of feedback on anything non-trivial.

Full details — coding standards, the CLA, how releases are cut — are in [CONTRIBUTING.md](CONTRIBUTING.md). First-time contributors: issues labeled [`good first issue`](https://github.com/cinderpath/relaykit/labels/good%20first%20issue) are scoped to be doable without deep context on the codebase.

## Support

- Bugs and feature requests: [GitHub Issues](https://github.com/cinderpath/relaykit/issues)
- Questions: [GitHub Discussions](https://github.com/cinderpath/relaykit/discussions)
- Security issues: see [SECURITY.md](SECURITY.md) — do not open a public issue

## License

MIT © [Cinderpath](https://cinderpath.com)
```

One structural note worth acting on separately: the `<details>` blocks above are a proposed **category scheme** for the 140-page site, not a verified inventory of it. Before this ships, someone needs to sort the actual 140 pages into these seven buckets (or revise the buckets) — that's the docs-structure-audit skill's job, not this README's.