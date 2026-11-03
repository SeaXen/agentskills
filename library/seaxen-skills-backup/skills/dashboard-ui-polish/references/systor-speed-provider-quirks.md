# Systor speed provider quirks

Concise implementation notes from the Systor `Speed` page work.

## Recommended split
- **WAN primary:** official Ookla CLI
- **LAN/browser primary:** embedded local LibreSpeed page served by the NAS
- **Quick probes only:** Notion / Cloudflare fixed-endpoint checks

## Why the LAN browser embed works
If the NAS already runs a LibreSpeed web UI (for example a Docker container on `:8077`) and the response has no `X-Frame-Options` denial, embed it in the dashboard with an `<iframe>`.

This gives a real browser-based laptop ↔ NAS test path without needing a CLI on the laptop.

## Why Cloudflare should not be iframed
`https://speed.cloudflare.com/` sends `X-Frame-Options: DENY`.

Practical dashboard pattern:
- keep an **Open Cloudflare** button
- if you need an in-dashboard Cloudflare datapoint, use a lightweight browser-side request to `https://speed.cloudflare.com/__down?bytes=...`
- label that result honestly as a probe / mini browser test, not a full clone of Cloudflare's own page behavior

## Provider server selection reality
Only expose server selection where it is real:
- **Ookla:** yes
- **LibreSpeed:** yes
- **Notion probe:** no
- **Simple Cloudflare probe:** no

## Official Ookla CLI gotcha under systemd
Official `speedtest` can fail or return no server list under a thin systemd env if key vars are missing.

In Python helper code, set a sane subprocess env before invoking it:
- `PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin`
- `LANG=C.UTF-8`
- `LC_ALL=C.UTF-8`
- `HOME=/root` (or another real writable home)

Do not trust shell success alone; verify the live web-service API path too.

## LibreSpeed CLI gotcha
`librespeed-cli --list` may print the server list to **stderr** instead of stdout.

When parsing the server catalog:
- prefer `stdout` if populated
- otherwise parse `stderr`

## Verification checklist
- Browser-verify the embedded local LibreSpeed frame actually loads.
- Browser-verify the Ookla server dropdown is populated from the live service route, not only from a shell test.
- Browser-verify inline `Save + apply` controls write config and show success copy.
- Write a fresh Ookla run into history so the UI shows the new provider path, not just old legacy rows.
