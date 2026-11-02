# Northgate getting-started page — six-language tabs, ready for the conference

Direct answer: this is buildable in nine weeks, but one part of the plan as stated will fail this skill's own pass threshold and needs to change before it ships — **"SDK owner eyeballs it" is not verification.** The skill's failure-mode table says it explicitly: *"Language tabs added, only one tab ever verified → Cold-run every tab; each is its own quickstart sharing a layout. An unverified tab is worse than a missing one, because the reader trusts it identically."* Reading generated code and confirming it looks right catches syntax nonsense; it does not catch "this doesn't compile against the real package," "the field is actually `traceId` not `trace_id` in this SDK version," or "this idiom is wrong for Go." Below is the plan with that one substitution made: each SDK owner still reviews for idiom and correctness, but they also **run it**, once, on a clean machine, against the real published package — which at 10 minutes per language is a half-day of total owner time across five people, not a redesign of your plan.

Everything below follows `developer-quickstart-guide`'s output shape.

---

## 1. Success moment + time budget

**Success moment:** *"You instrument a one-file script, run it, and see the resulting trace appear in your Northgate dashboard."*

Not "the SDK compiled" and not "you called an API" — the reader watches data travel from their laptop, through the SDK, into Northgate, and back out as a visible trace. That's the whole value proposition of an observability product in one screen.

**Time budget:** 10 minutes per language (SDK/library baseline from the skill's table). Committed per tab, not once for the page — a reader who picks Rust gets the same promise as a reader who picks TypeScript.

**Assumptions I made to write this without a live interview** (flag/correct any that are wrong):
- Northgate issues an instant self-serve or temporary dev API key with no card/sales step. If that's not true yet, fix *that* first — it outranks every other decision here, per the skill's access-mechanism ranking (`no account > temp dev key > instant self-serve key > free tier signup > sales-gated`). A perfect quickstart behind a sales-gated key is still a multi-day quickstart.
- All six SDKs will be on a compatible/synchronized release by conference time. Ship this page against a version tag, not "whatever's on the branch."
- This is a **compounding asset** (six SDKs, officially supported, used by every new reader for years), not a one-off — so the tab switcher and a CI regression job are in scope, not deferred.
- Docusaurus already has a working synced-tabs setup. If it doesn't yet, that's a day of setup, not a blocker.

---

## 2. Defect table

N/A — greenfield page, no existing quickstart to cold-run first.

---

## 3. The quickstart page

Canonical source: **TypeScript**. Every other tab is generated from it, then independently run — not translated line-by-line (that's the parity trap both skills warn about: *"a sample that reads like a transliteration fails idiomaticity even when it is byte-consistent with its siblings"*).

`docs/getting-started.mdx`:

````mdx
---
title: See your first trace in Northgate
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# See your first trace in Northgate in 10 minutes

You'll instrument a five-line script, run it, and watch the resulting trace
show up in your Northgate dashboard.

## Before you start

- A Northgate API key: [create one](https://app.northgate.io/keys) (no card required)
- The runtime for your language, checked below in each tab

<Tabs groupId="northgate-lang">
<TabItem value="ts" label="TypeScript" default>

- Node.js 18+: check with `node --version` ([nodejs.org](https://nodejs.org))

</TabItem>
<TabItem value="py" label="Python">

- Python 3.9+: check with `python --version` ([python.org](https://python.org))

</TabItem>
<TabItem value="go" label="Go">

- Go 1.21+: check with `go version` ([go.dev](https://go.dev))

</TabItem>
<TabItem value="java" label="Java">

- JDK 17+ and Maven: check with `java --version` and `mvn --version`

</TabItem>
<TabItem value="rb" label="Ruby">

- Ruby 3.1+: check with `ruby --version` ([ruby-lang.org](https://ruby-lang.org))

</TabItem>
<TabItem value="rs" label="Rust">

- Rust 1.75+ via rustup: check with `rustc --version` ([rustup.rs](https://rustup.rs))

</TabItem>
</Tabs>

## 1. Install the SDK

<Tabs groupId="northgate-lang">
<TabItem value="ts" label="TypeScript" default>

```
npm install @northgate/sdk@1
```

</TabItem>
<TabItem value="py" label="Python">

```
pip install northgate-sdk==1.4.0
```

</TabItem>
<TabItem value="go" label="Go">

```
go get github.com/northgate-io/northgate-go@v1
```

</TabItem>
<TabItem value="java" label="Java">

Add to `pom.xml`:

```xml
<dependency>
  <groupId>io.northgate</groupId>
  <artifactId>northgate-sdk</artifactId>
  <version>1.4.0</version>
</dependency>
```

</TabItem>
<TabItem value="rb" label="Ruby">

```
gem install northgate-sdk -v 1.4.0
```

</TabItem>
<TabItem value="rs" label="Rust">

Add to `Cargo.toml`:

```toml
[dependencies]
northgate = "1.4"
```

</TabItem>
</Tabs>

## 2. Send a trace

<Tabs groupId="northgate-lang">
<TabItem value="ts" label="TypeScript" default>

Create `send.ts`:

```ts
import { Northgate } from "@northgate/sdk";

const northgate = new Northgate({ apiKey: "<YOUR_NORTHGATE_API_KEY>" });

const span = northgate.startSpan("quickstart.hello");
await new Promise((resolve) => setTimeout(resolve, 50));
span.end();

console.log(span.traceId, span.status);
```

Run it:

```
npx tsx send.ts
```

You should see:

```
trace_01J8Z3K2N4 queued
```
{/* TODO(docs owner): replace with the real string from a cold run before publishing */}

`401 Unauthorized`? The key wasn't copied whole — it ends in a checksum
segment. Copy it again from [the keys page](https://app.northgate.io/keys).

</TabItem>
<TabItem value="py" label="Python">

Create `send.py`:

```python
import time
from northgate import Northgate

northgate = Northgate(api_key="<YOUR_NORTHGATE_API_KEY>")

with northgate.start_span("quickstart.hello") as span:
    time.sleep(0.05)

print(span.trace_id, span.status)
```

Run it:

```
python send.py
```

You should see:

```
trace_01J8Z3K2N4 queued
```

`401 Unauthorized`? Same fix as above — recopy the key.

</TabItem>
<TabItem value="go" label="Go">

Create `main.go`:

```go
package main

import (
	"fmt"
	"time"

	"github.com/northgate-io/northgate-go"
)

func main() {
	client := northgate.NewClient("<YOUR_NORTHGATE_API_KEY>")

	span := client.StartSpan("quickstart.hello")
	time.Sleep(50 * time.Millisecond)
	if err := span.End(); err != nil {
		panic(err)
	}

	fmt.Println(span.TraceID, span.Status)
}
```

Run it:

```
go run main.go
```

You should see:

```
trace_01J8Z3K2N4 queued
```

`401 Unauthorized`? Same fix as above — recopy the key.

</TabItem>
<TabItem value="java" label="Java">

Create `src/main/java/App.java`:

```java
import io.northgate.sdk.Northgate;
import io.northgate.sdk.Span;

public class App {
    public static void main(String[] args) throws InterruptedException {
        Northgate northgate = new Northgate("<YOUR_NORTHGATE_API_KEY>");

        Span span = northgate.startSpan("quickstart.hello");
        Thread.sleep(50);
        span.end();

        System.out.println(span.getTraceId() + " " + span.getStatus());
    }
}
```

Run it:

```
mvn -q compile exec:java -Dexec.mainClass=App
```

You should see:

```
trace_01J8Z3K2N4 queued
```

`401 Unauthorized`? Same fix as above — recopy the key.

</TabItem>
<TabItem value="rb" label="Ruby">

Create `send.rb`:

```ruby
require "northgate"

northgate = Northgate::Client.new(api_key: "<YOUR_NORTHGATE_API_KEY>")

span = northgate.start_span("quickstart.hello")
sleep(0.05)
span.end

puts "#{span.trace_id} #{span.status}"
```

Run it:

```
ruby send.rb
```

You should see:

```
trace_01J8Z3K2N4 queued
```

`401 Unauthorized`? Same fix as above — recopy the key.

</TabItem>
<TabItem value="rs" label="Rust">

Create `src/main.rs`:

```rust
use northgate::Client;
use std::time::Duration;

fn main() {
    let client = Client::new("<YOUR_NORTHGATE_API_KEY>");

    let span = client.start_span("quickstart.hello");
    std::thread::sleep(Duration::from_millis(50));
    span.end().expect("span failed to flush");

    println!("{} {}", span.trace_id(), span.status());
}
```

Run it:

```
cargo run
```

You should see:

```
trace_01J8Z3K2N4 queued
```

`401 Unauthorized`? Same fix as above — recopy the key.

</TabItem>
</Tabs>

## 3. Confirm delivery

Open the trace in your dashboard — replace the ID with the one your script printed:

```
https://app.northgate.io/traces/trace_01J8Z3K2N4
```

You should see status `delivered`, usually within a few seconds.

Still `queued` after 30 seconds? Check that the key belongs to the project
you're viewing — a key from a different project sends the trace somewhere
you can't see it.

## What just happened

Your SDK opened a span, timed it, and shipped it to Northgate asynchronously —
that's why the script's own output says `queued` while the dashboard,
moments later, says `delivered`.

## Next steps

- [Instrument a real request handler](…)
- [SDK reference](…)
- [Community Discord](…)
````

---

## 4. Cut list

| Cut | Where it went |
|---|---|
| A dedicated CLI per language to confirm delivery | Replaced by one shared dashboard-URL step (§3), not tabbed — cuts five install steps and five commands to keep in sync, for zero loss of proof |
| Explaining span/trace/async-delivery concepts up front | "What just happened," two sentences, after the reader has already seen it work |
| Auth theory / how Northgate's collector pipeline works | Belongs in explanation docs, linked from Next steps, not inlined |
| A 7th+ next-step link | Capped at three: build further, look things up, ask a human |
| Full error catalogue per SDK | One fail branch per tab (401), which is the only error a first-run reader can actually hit here |

---

## 5. Verification plan

This is the part that needs the process change. Two tracks:

**Track A — TypeScript (canonical, you run it yourselves)**

Standard cold-run protocol: fresh container, fresh key, no cached npm registry, timer from page load, execute every block verbatim, compare every line of output, log defects with step + elapsed time. Repeat with a second profile (someone who's never touched Northgate). This produces the *real* `You should see` strings — replace every `TODO` marker in the page above with what actually printed. Never ship an invented output string; a reader comparing their terminal to a fabricated line loses trust permanently.

**Track B — the other five (generated, owner-reviewed)**

Generation step: give each SDK owner the TS sample plus the scenario, not the code, to translate — "one span named `quickstart.hello`, sleep ~50ms, end it, print `<id> <status>`, confirm via dashboard URL" — and let idiom win: Python gets a context manager, Go gets an explicit `err` check, Rust gets a `Result` with `.expect()` flagged as a quickstart shortcut, not a production pattern. Translating the TS code token-by-token is exactly the failure mode both skills name (*"a sample that reads like transliterated Java satisfies a diff and fails the reader"*) — generate from the scenario, not from the source file.

Review step, per owner, per language (~10 minutes each, matching the page's own budget — so this is a half-day total, not a week):

1. Run it cold: fresh env, fresh key, no local build cache. Not "does the diff look right" — actually execute it.
2. Confirm the printed line matches the same `<id> <status>` shape the other five tabs show, so a reader switching tabs doesn't hit a different output format.
3. Confirm the trace lands in the dashboard within the stated wait.
4. Sign off with the exact command + output they saw, not "LGTM" — that string becomes the page's documented output for that tab.
5. Anything that needed a silent edit to run is a defect, not a passed review — fix the sample, not the owner's local workaround.

Ship gate, borrowed from the sample-standards skill's own threshold: **all six tabs tier "Run," none tier "eyeballed."** An unrun tab ships labeled "unverified, contributed" (its Community tier) or doesn't ship — it does not ship silently indistinguishable from the five that were actually run.

**Ongoing (this is a 2-year asset, not a launch artifact):**
- One CI job per language, on a schedule and on every SDK release, installing the *published* package (not the working tree) and asserting the trace-ID/status output pattern. This is what stops the page from being correct on conference day and quietly wrong three months later when someone renames a field.
- Fixtures: one disposable Northgate project/key per language's CI job, never a shared human account, with teardown for created spans.
- On CI failure: block the release, don't file a ticket — a stale quickstart costs a reader's trust before it costs their time.

---

## 6. Instrumentation

Nine weeks is a hard date, which per the skill defers everything past step-level drop-off — don't build the full funnel now, wire the one metric that's nearly free and tells you where a tab is breaking:

- Fire one event per tab selection and one at the `traceId`/dashboard confirmation step, tagged by language. This alone tells you post-launch which of the six tabs is quietly broken, without waiting on completion-rate or day-7 numbers.
- Defer: completion rate, median time-to-success, day-7 return. Revisit four weeks after the conference once there's real traffic across all six languages to baseline against — don't import a number from a vendor blog for the target.
- Support tickets/issues quoting a specific tab + step number: cheap to start now, and the fastest signal that "SDK owner ran it once in week 6" missed something a real reader hits in week 11.

---

**Nine-week shape:** weeks 1–2 TS canonical page + cold run + fixed output strings; weeks 2–4 generate + owner-run the other five in parallel; weeks 4–6 CI regression job per language; weeks 6–8 buffer for whatever the cold runs actually found (there will be findings); week 9 freeze. If a language's owner can't produce a real cold run in time, ship that tab labeled unverified rather than silently identical to the other five — a labeled gap is a defect a reader can route around; a silent one is the one that costs them the afternoon.