## Who you're segmenting

You're not segmenting **prospects**. There's no standalone purchase decision for the API — it ships inside a broker contract that's already been won through one of six channels. So "an integration that dies" isn't a lost deal. It's a **signed, paying broker who defaults back to a different channel** (portal, EDI batch, email/fax) instead of activating the one you built for them. That's an activation/adoption problem, not an acquisition problem — closer to customer success than to sales or devrel.

Devrel's fix (quickstarts, nicer sandbox) implicitly segments by **developer skill/friction** — the population that struggles to get a POC working. Your actual loss pattern says that's not who's killing deals: two integrations died *after* the POC succeeded. The technical population converted fine. The failure sits with a different population entirely — the one who decides whether the broker's *operations* actually cut over to the API once engineering hands back a working demo.

## Three groups, only one gets touched by a sandbox

1. **The POC team** (broker's engineers/integration devs) — evaluates feasibility. Sandbox and quickstarts speak to them. Not where you're bleeding.
2. **The channel owner** (broker's claims/ops leadership) — owns the process the API would replace. If they never asked for this, a working POC just sits there — nobody's job depends on switching.
3. **The sponsor** (whoever signed the broker contract) — decides if API integration was ever a committed line item, or a "sure, try it" side quest with no budget or deadline attached.

A POC dying after success almost always means #2 or #3 was never really in the room — engineering built something nobody downstream was mandated to adopt.

## Segment the 7 deals on these axes, not on "developer experience"

| Axis | Question to code each deal against |
|---|---|
| Sponsor mandate | Was API integration a named commitment in the contract/renewal, or an unscoped "nice to have"? |
| Replacement vs. addition | Did the API replace a channel causing acute pain (manual entry, EDI lag), or sit alongside an already-tolerable one? |
| Post-POC owner | Was there a named person on the broker's ops side accountable for cutover, independent of the engineer who built the POC? |
| Broker size/capacity | Dedicated platform team (survives champion turnover) vs. one person moonlighting on it? |
| Sequencing | Did the POC happen before or after commercial terms were final? (POC-before-contract deaths are often unrelated to the API at all.) |

Run your 4 wins and 3 losses through this table before touching anything DX-related. If the wins cluster on "replacement + named ops owner + dedicated team" and the losses cluster on "addition + no ops owner + solo champion," you've confirmed the lever is a **cutover playbook and an internal sponsor requirement at contract time** — not sandbox polish.

## What this means for the devrel ask

Don't kill the quickstart/sandbox work — it likely still matters for the subset of large brokers with real platform teams, where DX quality shortens time-to-POC and reduces the number of engineering hours the broker burns before deciding to commit. But it's solving a *speed* problem for a segment that isn't the one currently costing you closed integrations. It won't touch the two deaths you're worried about, because those died downstream of the point DX can influence.

The actionable move: stop treating "developer" as the segment and start treating **broker-side sponsorship + designated ops owner** as the qualifying criteria for even running a POC. If a broker can't name who owns cutover before engineering starts building, that's your leading indicator of a death-after-POC, and it's checkable at deal-scoping time — well before anyone touches a sandbox.