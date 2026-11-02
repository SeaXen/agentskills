Before the deliverable: this skill's scope check flags this exact request as its named failure mode ("Feature tour disguised as a tutorial" / bolting an objective onto a pre-fixed walkthrough). Quick, concrete notes, then the full artifact:

- **Two steps are explanation, not action.** "Tour of the config file" and "tour of the admin dashboard" have no verb, no single action, no observable output — the template's own rule is that explanation gets one paragraph in **Background**, never a step. I turned both into a single action with real output (run `nlx init`, inspect one field; open the dashboard, confirm one specific state) and moved the rest to a linked reference.
- **"List your streams" is a checkpoint, not a step.** It's literally "run a command, see observable output confirming prior state" — that's the checkpoint definition, not new content. Folding it in gets the primary-step count to 7, the sourced ceiling (Good Docs Project: "avoid procedures more than seven primary steps long").
- **"Overview of our other SDKs" isn't part of this tutorial's skill.** Browsing SDK options doesn't build the capability the learner came for. Moved to **Where to go next** as a short pointer instead of a numbered step, per the template's own ending structure.
- **Every command, code sample, and "expected output" block below is illustrative** — I don't have your actual peer-reviewed source text, only the 9 step titles, so I reconstructed plausible content around them. Before shipping, run it cold end-to-end and replace every output block with what a real run actually printed (pass-threshold criterion 1) and replace the time estimate with a measured one (criterion 4).

If you'd rather I put "list streams" and "other SDKs" back exactly where you had them, say so and I'll revert — the above is what "reads like a proper tutorial" costs, not a required rewrite of your content.

---

# Publish and consume your first event with the Nomadic Labs Streaming SDK

Publish an event to a stream and consume it in real time through a dedicated consumer group, using the Nomadic Labs CLI and TypeScript SDK together.

|                        |                                                                                  |
| ---------------------- | -------------------------------------------------------------------------------- |
| **Time**               | ~25 minutes (author estimate — replace with a measured cold-run time before publishing) |
| **Level**              | Used the Nomadic Labs REST API; new to the streaming SDK                        |
| **You'll need**        | Node.js ≥ 18, npm, a Nomadic Labs account with an API key                       |
| **Assumed knowledge**  | Nomadic Labs REST API concepts — projects, API keys (see [REST API docs](#)); `async`/`await` in TypeScript (see [TS handbook](#)) |

## What you'll build

A stream that carries `orders.created` events from your backend, and a consumer group that reads them in real time — the same producer/consumer shape you'll use for every stream in your account.

By the end of this tutorial, you'll be able to:

- Create a stream and a consumer group from the CLI
- Publish an event from TypeScript code
- Consume that event through your own consumer group and see it arrive

## Background

A **stream** is an ordered, partitioned log of events — the streaming equivalent of the resources you already read and write through the REST API, except events flow in continuously instead of being fetched on request. A **consumer group** is a named reader that tracks its own position in a stream, so multiple services can read the same stream independently without stepping on each other's progress.

## Before you begin

| Requirement                      | Version | Check                                                        |
| --------------------------------- | ------- | ------------------------------------------------------------- |
| Node.js                            | ≥ 18    | `node --version`                                              |
| npm                                | ≥ 9     | `npm --version`                                                |
| Nomadic Labs account + API key     | —       | Sign in at `console.nomadiclabs.dev` → Settings → API Keys    |

Assumed knowledge:

- Nomadic Labs REST API concepts (projects, API keys) — [REST API docs](#)
- `async`/`await` in TypeScript — [TS handbook](#)

## Step 1: Install and authenticate the CLI

Install the CLI globally:

```bash
npm install -g @nomadiclabs/cli
```

Authenticate with the API key from **Before you begin**:

```bash
export NOMADIC_API_KEY="nlk_live_..."
nlx login --api-key "$NOMADIC_API_KEY"
```

Expected output:

```
✔ Authenticated as you@company.com (project: proj_8f2a1c)
```

`command not found: nlx`? npm's global bin directory isn't on your `PATH` — see [Troubleshooting](#nlx-command-not-found).

## Step 2: Generate your project config

```bash
nlx init
```

Expected output:

```
✔ Wrote nomadic.config.yaml
```

This creates `nomadic.config.yaml` in the current directory:

```yaml
project_id: proj_8f2a1c
region: us-east-1
default_stream:
  partitions: 3
  retention: 24h
api_key: ${NOMADIC_API_KEY}
```

The one field every later command reads is `project_id` — it's how `nlx` and the SDK know which project's streams you're working with. The rest of the file is documented in the [config reference](#).

## Step 3: Create a stream

```bash
nlx streams create orders.created --partitions 3 --retention 24h
```

Expected output:

```
✔ Created stream "orders.created" (id: strm_4b7e9a)
```

## Checkpoint: the stream exists

```bash
nlx streams list
```

Expected output:

```
NAME             PARTITIONS   RETENTION   CREATED
orders.created   3            24h         just now
```

You now have a stream your project can publish to and read from. If `orders.created` isn't listed, re-run step 3 — stream names must be unique per project, so a silent failure there usually means it already exists under a slightly different name.

## Step 4: Create a consumer group

```bash
nlx groups create orders-created-worker --stream orders.created
```

Expected output:

```
✔ Created consumer group "orders-created-worker" on stream "orders.created"
```

## Step 5: Confirm the group in the admin dashboard

Open `console.nomadiclabs.dev/streams/orders.created`. Under **Consumer groups**, find `orders-created-worker` and confirm its **Lag** column reads `0` — the group exists and has nothing unread yet, because you haven't published anything.

The dashboard also shows throughput graphs, per-partition offsets, and retention usage for every stream in your project — worth a look later, covered in the [dashboard reference](#).

## Step 6: Publish an event

Install the SDK:

```bash
npm install @nomadiclabs/sdk
```

Create `publish.ts`:

```ts
import { NomadicClient } from "@nomadiclabs/sdk";

const client = new NomadicClient({
  projectId: process.env.NOMADIC_PROJECT_ID!,
  apiKey: process.env.NOMADIC_API_KEY!,
});

await client.stream("orders.created").publish({
  orderId: "ord_1029",
  total: 42.5,
  currency: "USD",
});

console.log("Event published");
```

Run it:

```bash
export NOMADIC_PROJECT_ID="proj_8f2a1c"
npx tsx publish.ts
```

Expected output:

```
Event published
```

`401 Unauthorized`? `NOMADIC_API_KEY` isn't set in this shell — see [Troubleshooting](#401-unauthorized).

## Step 7: Consume the event

Create `consume.ts`:

```ts
import { NomadicClient } from "@nomadiclabs/sdk";

const client = new NomadicClient({
  projectId: process.env.NOMADIC_PROJECT_ID!,
  apiKey: process.env.NOMADIC_API_KEY!,
});

const group = client.consumerGroup("orders-created-worker", {
  stream: "orders.created",
});

group.subscribe((event) => {
  console.log("Received:", event.payload);
});
```

Run it, then publish a fresh event from step 6 in a second terminal (consumer groups start at the latest offset by default, so an event published before the subscriber started won't replay):

```bash
npx tsx consume.ts
```

Expected output:

```
Received: { orderId: 'ord_1029', total: 42.5, currency: 'USD' }
```

## Checkpoint: the event round-trips through your own consumer group

If nothing prints within a couple of seconds, re-run `publish.ts` while `consume.ts` is still running — a group created with the default start position only sees events published after it subscribes. To replay events published earlier, recreate the group with `nlx groups create ... --start-position earliest`.

You've now published and consumed an event end to end, on infrastructure you created yourself in steps 3-4.

**Optional:** before rerunning, predict what happens if you start a *second* `consume.ts` process for the same group while publishing one event — does it print once or twice? [Answer](#).

## What you built

The complete flow, in one place:

```ts
// publish.ts and consume.ts, unchanged from steps 6-7
```

You can now:

- Create a stream and a consumer group without leaving the terminal
- Publish an event from a TypeScript service
- Read that event back through a consumer group and reason about start position

## Troubleshooting

### `nlx: command not found`

**Cause:** npm's global bin directory isn't on your `PATH`.
**Fix:** run `npm config get prefix`, add `<prefix>/bin` to `PATH`, or prefix every command with `npx`.

### `401 Unauthorized`

**Cause:** `NOMADIC_API_KEY` isn't exported in the shell running the command.
**Fix:** `export NOMADIC_API_KEY="nlk_live_..."`, then retry.

### Consumer prints nothing

**Cause:** the event was published before the consumer subscribed, and the group's start position is `latest`.
**Fix:** with the consumer still running, publish a new event, or recreate the group with `--start-position earliest`.

## Where to go next

- **How-to:** [Replay events from a specific offset](#) — the real-world variant of step 7's optional question.
- **Reference:** [Streams and consumer groups API](#) — every option `nlx streams create` and `client.stream()` accept.
- **Explanation:** [Why consumer groups track their own offset](#) — the partitioning model behind step 4-5.

Using a language other than TypeScript? The SDK ships equivalent clients for Python, Go, and Java — see the [SDK overview](#) for the one that matches your stack.