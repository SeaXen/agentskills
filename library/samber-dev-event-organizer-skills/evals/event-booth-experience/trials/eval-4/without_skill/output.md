**Step 1 (ask the venue, 2 min):** Are booth power drops additional to the 60 attendee outlets? The rest of this plan depends on the answer.

## Inputs from the ratios

| Resource | Math | Result |
|---|---|---|
| Outlets | 600 ÷ 10 | **60** |
| WiFi devices | 600 × 2.5 | **1,500** |
| Booths | given | 14 |

⚠️ The ratios give **device count**, not throughput. No uplink or AP capacity (Mbps) was given, so bandwidth below is a formula plus examples. Ask the venue for the guaranteed uplink in Mbps.

## Power

Assume booth power comes out of the 60 outlets. Reserve 4 for registration, AV and staff. G is the number of Gold sponsors.

| Item | Outlets |
|---|---|
| Every booth, baseline (14 × 1) | 14 |
| Gold extra drop (the package promise) | G |
| Reserve (registration, AV, staff) | 4 |
| Left for attendees | 42 − G |

- **With G = 3:** 39 outlets are left for attendees, or 1 per 15.4 instead of 1 per 10. That is a 35% cut.
- **If the venue adds booth drops on top of the 60:** attendees keep 56 outlets (1 per 10.7), and every booth can have 2 drops. This is the better outcome, so ask for it.
- **Gold:** each Gold booth gets a guaranteed dedicated drop with a 2-outlet strip, which fulfils the package. Confirm the amperage per drop, because the ratios say nothing about watts.
- **Non-Gold booths:** 1 outlet plus a strip. Tell them a 2nd drop is not guaranteed.

## Bandwidth

Per-device fair share = uplink ÷ 1,500.

| Uplink | Per device | Booth staff pool (14 booths × 13 devices = 182) |
|---|---|---|
| 500 Mbps | 0.33 Mbps | 61 Mbps |
| 1 Gbps | 0.67 Mbps | 121 Mbps |
| 2 Gbps | 1.33 Mbps | 243 Mbps |

- **Booth baseline:** 13 devices each (5 staff × 2.5, rounded up). That is about 8.7 Mbps per booth at 1 Gbps.
- **Reality check:** peak concurrency is below 100%, so real per-active-device speed is higher. Treat the table as the floor, not the expected value.
- **Airtime:** WiFi airtime and AP density (1,500 devices) limit you before the uplink does. Ask the venue for the AP count and the channel plan.

## Cloud-gaming demo: do not run it on shared venue WiFi

- **Bandwidth:** a stream needs about 15–45 Mbps down, depending on resolution. 25 Mbps is typical for 1080p60. That equals the fair share of about 37 devices at 1 Gbps, and several visitors playing at once multiplies it.
- **Latency:** it needs low, stable latency (under about 40 ms) and little jitter. Contention among 1,500 devices breaks both, and the demo will stutter even when the uplink has headroom.
- **Fairness:** it would also eat other booths' share.

Options, in order of preference:

1. **Wired Ethernet drop** on its own VLAN or QoS lane, with a 50+ Mbps reservation. Ask the venue for this.
2. **Sponsor's own uplink** (bonded 5G or cellular router), fully off venue WiFi.
3. **Pre-recorded fallback video** at the booth in case either fails.
4. **If WiFi is the only option:** a dedicated 5 GHz SSID and AP for that booth, with the stream capped at one or two concurrent players. Set expectations in writing with the sponsor.

Whichever option the sponsor uses, it should not count against the 13-device booth baseline.

**Next:** email the venue contact three questions: uplink in Mbps, amperage per outlet, and whether booth drops are additional. Paste the answers back and I'll finalize the numbers. Also send me G (the number of Gold sponsors).