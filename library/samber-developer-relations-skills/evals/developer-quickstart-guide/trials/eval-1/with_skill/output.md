Two structural conflicts before this page can pass its own cold-run gate. Fix these, not just the words.

1. **Access is the real bottleneck, not the code.** Hosted-API time budget is 5 min. Sales-gated key = next business day. Both can't be true. Fix below: a shared, rate-limited demo key baked into the sandbox — no signup, no wait, real response. Production key still goes through sales, but *after* success, not blocking it.
2. **Sandbox needs a named owner.** Skill default: no owner kills the sandbox option entirely. You have none today. StackBlitz WebContainers (client-side, no VM to host) is the cheapest sandbox option that exists — but someone still has to keep the demo key alive and the project synced with API changes. Assign one of the four engineers, rotate it.
3. **5-week deadline pushes toward a plain page by default.** You're overriding that for the sandbox on real evidence (competitor conversion) — reasonable, but budget the demo-key work in week 1, not week 4.
4. **I don't have your real endpoint, field names, or tier numbers.** Everything below marked `<TODO>` needs the shipping engineer to fill in before this ships — that's expected, per the skill's ownership rule.

**Success moment:** the sandbox response includes `latitude`, `longitude`, and `confidence` for the address the reader posted.
**Time budget:** 5 minutes, page load to response — the hosted-API baseline holds because the sandbox deletes install and signup entirely.

---

## The page

````markdown
# Geocode your first address in 5 minutes

You'll send an address to Reticule and get back its coordinates plus a
confidence score — no signup, no local install.

## Before you start

- A browser that runs StackBlitz sandboxes: Chrome, Edge, or Firefox.
  (Safari support is inconsistent — switch to Chrome if the sandbox loads blank.)
- Nothing else. The sandbox below already has a working demo key wired in.

## 1. Open the sandbox

<!-- Embed: replace project id once the shipping engineer creates it -->
<iframe
  src="https://stackblitz.com/edit/reticule-geocode-quickstart?embed=1&file=geocode.js&hideNavigation=1&view=preview&ctl=1"
  style="width:100%; height:500px; border:0; border-radius:8px;"
  title="Reticule geocoding quickstart"
  sandbox="allow-forms allow-modals allow-popups allow-presentation allow-same-origin allow-scripts">
</iframe>

The sandbox ships with `geocode.js` and a demo API key already filled in.
Nothing to configure.

## 2. Run it

Click **Run** in the sandbox, or in its terminal panel:

    node geocode.js

`geocode.js`:

    const response = await fetch("https://api.reticule.dev/v1/geocode", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer <RETICULE_QUICKSTART_DEMO_KEY>",
      },
      body: JSON.stringify({
        address: "1600 Amphitheatre Parkway, Mountain View, CA",
      }),
    });

    const result = await response.json();
    console.log(result);

You should see:

    {
      latitude: 37.4224,
      longitude: -122.0842,
      confidence: 0.97,
      formatted_address: "1600 Amphitheatre Pkwy, Mountain View, CA 94043, USA"
    }

Getting `429 Too Many Requests`? The shared demo key hit its limit for
everyone reading this page right now — wait a minute and retry, or
[request your own key](#next-steps).

## 3. Read the response

- `confidence` runs 0–1. Above 0.9 means Reticule matched a specific
  building; lower means it matched a street or area.
- Edit the `address` field to one of your own and rerun — the sandbox
  updates live.

## Your access

The `Authorization: Bearer <key>` header is how every Reticule request
authenticates — same header, every endpoint.

The demo key above is shared across everyone on this page and capped low
on purpose. Real usage runs on your own key, on one of these tiers:

| Tier | Requests | How to get it |
|---|---|---|
| Demo (this page) | `<TODO: req/min>` shared | Already in the sandbox |
| `<TODO: tier name>` | `<TODO: req/min>` | Email `<TODO: sales inbox>` |
| `<TODO: tier name>` | `<TODO: req/min>` | Email `<TODO: sales inbox>` |

Full limits and overage behavior: [rate limits reference](#).

## Next steps

- **Get a production key.** Email `<TODO: sales inbox>` with your company
  name, expected requests/month, and use case — that's what sets your
  tier and turnaround (usually next business day).
- [API reference](#) — every endpoint, including reverse geocoding and
  batch requests.
- [Get help](#) — `<TODO: support channel — does the sales inbox double
  as support for now?>`
````

## Cut list

| Cut | Now lives in |
|---|---|
| Full tier pricing, overage billing | Rate limits reference page |
| Reverse geocoding, batch, webhooks | API reference |
| Confidence-score methodology | Concepts/explanation doc |
| Error catalog beyond `429` | Troubleshooting page |
| Production-key SLA detail | Sales reply / "getting a key" doc |

## Verification plan

1. Open the page in a private browser window — no cached StackBlitz session.
2. Confirm the demo key isn't already rate-limited before starting the clock.
3. Time from page load to seeing `confidence` in the output.
4. Run it twice: once by a Reticule engineer, once by an outside developer
   with zero context — the second one finds the assumptions the first
   can't see.
5. Log any deviation (edited command, different output, late-discovered
   step) as a defect. Fix, then rerun the full protocol — not just the
   failed step.

Ship gate, all five must hold: commands run verbatim · output matches exactly
· zero new prerequisites after step 1 · elapsed time ≤ 5 min · tester never
leaves the page.

Owner: rotate among the four backend engineers — name one before the next
entry, not at launch week.

## Instrumentation

No docs analytics and no dedicated owner, so lean on what you already have —
server logs and the sales inbox — instead of standing up a new stack:

- Log every demo-key request server-side (you already log API calls). That's
  your "success" event, free.
- Add one page-load event on the docs page itself.
- Embed a unique per-pageview token as a custom header
  (`X-Quickstart-Session: <token>`) on the sandbox's pre-filled request, so
  server logs join page-load → real call without new tooling.
- KPI order, cheapest-actionable first: step drop-off (page load vs. token
  seen in logs) → "quickstart" mentions in the sales inbox → median
  time-to-success → completion rate → day-7 return (did they later email
  sales for a real key).
- Set targets from your own 4-week baseline, not a vendor number.

CI regression (cheap, worth it for 4 backend engineers): nightly job hits the
real endpoint with the demo key, asserts `latitude`/`longitude`/`confidence`
are present with correct types. Fails loudly the moment the API drifts from
what the page promises.

**Next:** create the StackBlitz project (`reticule-geocode-quickstart`), issue the shared demo key, and name the rotating owner — those three unblock everything else above.