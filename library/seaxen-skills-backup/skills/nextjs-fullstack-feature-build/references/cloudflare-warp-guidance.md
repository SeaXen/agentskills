# Cloudflare WARP guidance

Use this when the user asks about WARP performance, configuration, or behavior.

## Quick answers

- **WARP vs WARP+**: WARP is the free consumer VPN-like service; WARP+ routes through Cloudflare’s Argo Smart Routing for potentially lower latency to supported destinations.
- **Latency impact**: WARP adds ~2–10 ms to Cloudflare’s nearest edge, then the same path to destination. If your ISP already has optimal routing to the destination, WARP can add latency. If your ISP has poor peering, WARP can reduce it.
- **Throughput**: Usually same or better due to Cloudflare’s peering, but depends on destination and your local ISP.
- **Resource usage**: WARP daemon (`warp-svc`) uses ~5–20 MB RAM and <1% CPU when idle.

## Modes

| Mode | Behavior | Requires root? |
|------|----------|---------------|
| `warp` (default) | Tunnel + UDP DNS proxying | No for status, yes for mode change |
| `doh` | DNS over HTTPS only, no tunnel | Yes |
| `proxy` | Tunnel for SOCKS5 proxy mode | Yes |
| `tunnel_only` | Tunnel without DNS proxying | Yes |

## Commands

```bash
# Check connection state
warp-cli status

# Switch modes (requires root)
sudo warp-cli mode warp      # default tunnel + DNS
sudo warp-cli mode doh       # DNS over HTTPS only
sudo warp-cli mode proxy     # SOCKS5 proxy mode
sudo warp-cli mode tunnel_only

# Connect/disconnect
warp-cli connect
warp-cli disconnect

# Show current mode
warp-cli settings list | grep mode
```

## Performance testing pattern

When the user asks "does WARP make it faster?" or "does it add latency?":

1. Run baseline tests **with WARP already connected** (if it is).
2. Disable WARP: `warp-cli disconnect`
3. Re-run the same tests.
4. Re-enable WARP: `warp-cli connect`
5. Report the **delta**, not absolute numbers.

Example test commands:

```bash
# Latency to known hosts
curl -o /dev/null -s -w "Cloudflare: %{time_total}s\n" https://cloudflare.com
curl -o /dev/null -s -w "Google: %{time_total}s\n" https://google.com

# Download speed
curl -o /dev/null -s -w "Speed: %{speed_download} B/s\n" https://speed.cloudflare.com/__down?bytes=10000000
```

## Key rule

If WARP is already **Connected** when you check, do **not** change modes without explicit user request. Default install mode is usually sufficient. Only switch modes if the user explicitly asks for a different behavior (e.g., SOCKS5 proxy, DNS-only).

## Common user questions

- **"Is WARP a VPN?"** — WARP behaves like a VPN for consumer devices: it encrypts traffic and can hide your IP. WARP+ adds routing optimizations.
- **"Does WARP slow me down?"** — Measure it. It can add or reduce latency depending on your ISP’s routing to the destination.
- **"Does WARP use much RAM/CPU?"** — No. ~5–20 MB RAM, <1% CPU idle.
- **"Can I use WARP with my app?"** — WARP is a system-level service. It affects all traffic from the machine, not just a specific app. For app-specific tunneling, use Cloudflare Tunnel (`cloudflared`).
- **"Default mode after install?"** — Usually `warp` (tunnel + DNS). Do not change it unless the user asks.