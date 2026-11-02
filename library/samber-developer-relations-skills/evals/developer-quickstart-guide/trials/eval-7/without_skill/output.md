Root cause first, since it decides what "faster" even means here.

**Diagnosis:** a 4-minute local run vs. a 2–4 week customer run isn't a copy-editing gap — no amount of clearer prose closes a 500x gap. Step 1 is `docker pull` + run. In a bank or insurer that step routes through things your laptop never sees: no local admin, egress firewalls with TLS-inspecting proxies, VDI/Citrix desktops with nested virtualization disabled (Docker Desktop won't even start), and a mandatory InfoSec review before any container touches a corporate machine — SBOM, CVE scan, signed image, data-flow diagram. The ticket says "stuck at step 1" because that's exactly where those five things live. The page can't fix a security-review queue.

The real problem: the quickstart conflates two different jobs. "Does this product mask data the way I need" is a 60-second question. "Get this exact binary running inside our regulated network" is a multi-week procurement process, independent of documentation quality. Today both funnel through the same `docker pull`, so every evaluator gets stuck behind their own employer's bureaucracy before seeing a single masked record. Decoupling them is the fix — not shorter sentences.

Below is the rebuilt page and the process change that has to ship alongside it (a doc fix alone won't move the 2–4 week number).

---

# Ferrous Quickstart

## Two ways to start — pick based on what you're trying to do

| I want to... | Use | Time | Needs approval? |
|---|---|---|---|
| See Ferrous mask a record before I install anything | **Try it now** (hosted sandbox) | 60 sec | No |
| Run Ferrous inside our network | **Deploy it here** | 4 min once cleared | Yes — see Pre-Clearance Packet |

Don't make an evaluator solve your customer's network security problem just to see the product work. That decision alone removes step 1 entirely for anyone who's still deciding.

---

## Try it now (no install, no approval, no data leaves your browser)

1. Open **[sandbox.ferrous.example.com](#)** — a hosted, ephemeral Ferrous instance, pre-loaded with synthetic sample records.
2. Click **Mask this record**.
3. See the masked output and the policy that produced it.

That's it. This runs on our infrastructure against synthetic data — nothing about your environment, network, or real data is involved, so there's nothing for your security team to review yet. Use this to confirm Ferrous does what you need before spending any internal capital getting it installed.

When you're ready to test it against your own network/policies, move to **Deploy it here**.

---

## Deploy it here

### Step 0: Tell us your environment (30 seconds, prevents the #1 ticket)

Pick one:

- **A — Standalone sandbox/VM, internet access, local admin.** → Standard path, ~4 minutes.
- **B — Corporate laptop or VDI, restricted or no internet egress.** → Offline Bundle path.
- **C — Fully air-gapped network.** → Offline Bundle path, delivered via your approved transfer channel.

If you're not sure, pick B — it always works and costs you nothing extra.

**Known blocker, check this before anything else if you're on a VDI/Citrix/Horizon desktop:** Docker requires nested virtualization. Most VDI images disable it by default. Ask your desktop team to confirm `nested virtualization: enabled` before filing a ticket that looks like "Docker won't start" — this is a VDI config flag, not a Ferrous or Docker bug.

---

### Path A — Standard (internet + admin)

```bash
docker pull ferrous/engine:latest
docker run -p 8443:8443 ferrous/engine:latest
curl -k https://localhost:8443/health
curl -k -X POST https://localhost:8443/mask -d @sample-record.json
```

Expected: `{"status":"ok"}` from health, then a masked JSON record. Total time: ~4 minutes.

---

### Path B / C — Offline Bundle (restricted network or air-gapped)

Use this if `docker pull` times out, hangs on TLS handshake, or your proxy blocks the registry — this is the expected outcome on a locked-down corporate network, not a sign anything is broken.

1. Download the bundle once, from anywhere with internet access (or have it delivered via your approved file-transfer process): `ferrous-engine-<version>.tar.gz` (includes the image, SHA-256 checksum, and cosign signature).
2. Verify it:
   ```bash
   sha256sum -c ferrous-engine-<version>.tar.gz.sha256
   cosign verify-blob --signature ferrous-engine-<version>.sig ferrous-engine-<version>.tar.gz
   ```
3. Load it into your own approved internal registry — no external registry contact required from this point on:
   ```bash
   docker load -i ferrous-engine-<version>.tar.gz
   docker tag ferrous/engine:<version> <your-internal-registry>/ferrous/engine:<version>
   docker push <your-internal-registry>/ferrous/engine:<version>
   ```
4. Run and test exactly as in Path A, pointing at your internal registry.

No step here requires Ferrous's servers to be reachable from your network at any point after the initial download.

---

## Security Pre-Clearance Packet

Hand this to your security/network team **before** you reach Step 0 — ideally during evaluation or contracting, weeks before anyone opens this page. This is the artifact that actually removes the multi-week wait, because it lets the review run in parallel with legal/procurement instead of starting on day one of onboarding:

- SBOM (SPDX format): `[link]`
- Latest third-party CVE scan report: `[link]`
- Image signing key + cosign verification instructions (above)
- Data-flow diagram: masking happens in-process, in-memory; no record or field value leaves the host running the container
- SOC 2 / relevant compliance attestations: `[link]`

**Field engineers:** send this packet at the start of the evaluation, not at kickoff. If a prospect's security review is already underway when they reach Step 0, the "stuck at step 1" ticket mostly stops happening — the approval is already granted by the time they touch the CLI.

---

## Troubleshooting — mapped to real step-1 failures

| Symptom | Real cause | Fix |
|---|---|---|
| `docker: permission denied` | No local admin / Docker daemon not accessible | Not a config typo — request admin or switch to Path B with your platform team's help |
| TLS handshake timeout / `context deadline exceeded` on pull | Corporate proxy or egress firewall blocking the registry | Expected on restricted networks. Switch to Offline Bundle (Path B) |
| Docker Desktop won't start on a VDI machine | Nested virtualization disabled | Desktop team enables it, or use Path B with a team-owned VM instead |
| `curl: (7) Failed to connect` to localhost health check | Container port not published, or VDI blocks loopback across layers | Confirm `-p 8443:8443` was passed; on VDI, run from inside the same virtual layer as the container |
| No error, just... nothing happens for weeks | Security review hasn't started | This isn't a page problem — send the Pre-Clearance Packet earlier in the sales cycle |

---

## What to measure after shipping this

- Time-to-first-masked-record, split by track (A/B/C) and by hosted-sandbox vs. on-prem — the sandbox number should land near 60 seconds regardless of customer.
- Ticket volume tagged "stuck at step 1," before/after — this should drop hard once Path B exists and the Pre-Clearance Packet ships earlier.
- % of evaluations that use the hosted sandbox before ever touching Docker — if it's low, the two-track split isn't being found; move it higher on the page.

---

One thing I couldn't verify: I don't have your actual current quickstart copy or real ticket text, so the specific error strings and current page structure above are reconstructed from the four facts you gave (4 min local, 2–4 weeks customer, "stuck at step 1," on-prem in regulated industries). Swap in real error strings and current page content before publishing — the structural fix (hosted sandbox + branch by network posture + front-loaded security packet) is what closes the gap; the exact wording is secondary.